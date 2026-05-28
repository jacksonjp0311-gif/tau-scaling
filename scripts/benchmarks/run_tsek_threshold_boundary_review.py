
from __future__ import annotations
import json, os, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "tsek_threshold_review"
VIS = ROOT / "visuals" / "tsek_threshold_review" / "v0_7_4"

CORE_FILES = [
    ROOT / "src" / "tau_scaling" / "core" / "classifier.py",
    ROOT / "src" / "tau_scaling" / "core" / "runtime.py",
    ROOT / "src" / "tau_scaling" / "core" / "models.py",
]
REPORTS = {
    "gate_algebra": ROOT / "reports" / "gate_algebra" / "latest_gate_algebra_map.json",
    "tau_vector_semantics": ROOT / "reports" / "tau_vector_semantics" / "latest_tau_vector_semantics_ledger.json",
    "synthetic_gate": ROOT / "reports" / "gates" / "latest_synthetic_gate_report.json",
    "sensitivity": ROOT / "reports" / "sensitivity" / "latest_sensitivity_sweep.json",
    "interactions": ROOT / "reports" / "interactions" / "latest_gate_interaction_matrix.json",
    "release": ROOT / "reports" / "release" / "latest_release_readiness.json",
}
BENCHMARK_DIRS = [
    ROOT / "reports" / "benchmarks",
    ROOT / "reports" / "gates",
    ROOT / "reports" / "interactions",
    ROOT / "reports" / "explanations",
    ROOT / "reports" / "regression_review",
]

TSEK_CLASSES = ["TSEK-A", "TSEK-B", "TSEK-C", "TSEK-D", "TSEK-E"]

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def read_json(path: Path):
    if not path.exists():
        return {"missing": True, "path": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"parse_error": str(exc), "path": str(path)}

def wjson(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")

def scan_classifier_code():
    text = "\n".join(read_text(p) for p in CORE_FILES)
    class_counts = {c: len(re.findall(re.escape(c), text)) for c in TSEK_CLASSES}
    threshold_terms = {
        "threshold": len(re.findall(r"threshold", text, re.I)),
        "score": len(re.findall(r"score", text, re.I)),
        "downgrade": len(re.findall(r"downgrade", text, re.I)),
        "finding": len(re.findall(r"finding", text, re.I)),
        "hard_gate": len(re.findall(r"hard[_ -]?gate", text, re.I)),
        "evidence": len(re.findall(r"evidence", text, re.I)),
        "support": len(re.findall(r"support", text, re.I)),
    }
    numeric_literals = sorted(set(re.findall(r"(?<![A-Za-z0-9_])(?:0?\.\d+|1\.0|[2-9]\.\d+)(?![A-Za-z0-9_])", text)))[:80]
    functions = sorted(set(re.findall(r"def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", text)))
    return {
        "class_counts": class_counts,
        "threshold_terms": threshold_terms,
        "numeric_literals_seen": numeric_literals,
        "function_count": len(functions),
        "functions": functions[:100],
    }

def scan_reports_for_classes():
    counts = Counter()
    sources = []
    for d in BENCHMARK_DIRS:
        if d.exists():
            for p in sorted(d.rglob("*.json")):
                text = read_text(p)
                if not text.strip():
                    continue
                local = {c: text.count(c) for c in TSEK_CLASSES}
                if any(local.values()):
                    for c, n in local.items():
                        counts[c] += n
                    sources.append(rel(p))
    return dict(counts), sources[:100]

def classify(code, report_counts, reports):
    gaps = []
    release = reports["release"]
    gate = reports["gate_algebra"]
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    gate_ready = gate.get("gate_algebra_status") == "GATE_ALGEBRA_MAP_READY__TARGETED_GATE_GAPS_IDENTIFIED"

    if not release_passed:
        gaps.append("release_not_passing")
    if not gate_ready:
        gaps.append("gate_algebra_not_ready")
    if sum(code["class_counts"].values()) == 0:
        gaps.append("tsek_classes_not_visible_in_core_code")
    if code["threshold_terms"]["threshold"] == 0:
        gaps.append("threshold_terms_not_explicit_in_classifier_scan")
    if code["threshold_terms"]["downgrade"] == 0:
        gaps.append("downgrade_terms_not_explicit_in_classifier_scan")
    if not report_counts:
        gaps.append("no_tsek_class_distribution_found_in_reports")
    if report_counts.get("TSEK-A", 0) == 0:
        gaps.append("no_tsek_a_observed_in_report_scan")
    if report_counts.get("TSEK-D", 0) == 0:
        gaps.append("no_tsek_d_observed_in_report_scan")

    status = "TSEK_THRESHOLD_BOUNDARY_REVIEW_READY__NO_THRESHOLD_CHANGE" if release_passed and gate_ready else "TSEK_THRESHOLD_BOUNDARY_REVIEW_NEEDS_REPAIR"
    return gaps, status, release_passed, gate_ready

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        wtext(OUT / "chart_generation_skipped.txt", str(exc))
        return paths

    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        p = VIS / name
        plt.tight_layout()
        plt.savefig(p, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(p))

    class_counts = summary["core_tsek_class_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(class_counts.keys()), list(class_counts.values()))
    plt.ylabel("Core mentions")
    plt.title("TSEK Class Mentions in Core Code")
    save("tsek_core_class_mentions.png")

    report_counts = summary["report_tsek_class_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(TSEK_CLASSES, [report_counts.get(c, 0) for c in TSEK_CLASSES])
    plt.ylabel("Report mentions")
    plt.title("TSEK Class Mentions in Reports")
    save("tsek_report_class_mentions.png")

    terms = summary["threshold_terms"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(terms.keys()), list(terms.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Core mentions")
    plt.title("Threshold Boundary Term Visibility")
    save("tsek_threshold_term_visibility.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.4 TSEK Threshold Boundary Review",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Review Result",
        "",
        f"- Threshold review status: `{summary['threshold_review_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Gate algebra ready: `{summary['gate_algebra_ready']}`",
        f"- Gap count: `{summary['gap_count']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        "",
        "## Core TSEK Class Visibility",
        "",
        "| Class | Core mentions | Report mentions |",
        "|---|---:|---:|",
    ]
    for c in TSEK_CLASSES:
        lines.append(f"| `{c}` | {summary['core_tsek_class_counts'].get(c, 0)} | {summary['report_tsek_class_counts'].get(c, 0)} |")

    lines += [
        "",
        "## Threshold Term Visibility",
        "",
        "| Term | Core mentions |",
        "|---|---:|",
    ]
    for k, v in summary["threshold_terms"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += ["", "## Numeric Literals Observed", ""]
    if summary["numeric_literals_seen"]:
        lines.append("```text")
        for item in summary["numeric_literals_seen"]:
            lines.append(item)
        lines.append("```")
    else:
        lines.append("- `none_detected`")

    lines += ["", "## Targeted Gaps", ""]
    if summary["gaps"]:
        for gap in summary["gaps"]:
            lines.append(f"- `{gap}`")
    else:
        lines.append("- `none_detected_in_v0_7_4_scan`")

    lines += [
        "",
        "## Boundary Decision",
        "",
        "This layer is **review-only**. It does not alter thresholds, class weights, downgrade logic, support constraints, or classifier behavior.",
        "",
        "## Next Tau Work",
        "",
        "1. Build a TSEK threshold table from current classifier logic.",
        "2. Add non-mutating threshold explanation cards for each class boundary.",
        "3. Compare observed report class distributions against expected downgrade/promotion pathways.",
        "4. Design under-penalty and over-penalty negative controls before any threshold change.",
        "",
        "## Charts",
        "",
    ]
    for p in summary["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    reports = {k: read_json(v) for k, v in REPORTS.items()}
    code = scan_classifier_code()
    report_counts, report_sources = scan_reports_for_classes()
    gaps, status, release_passed, gate_ready = classify(code, report_counts, reports)

    summary = {
        "schema": "tau-scaling-tsek-threshold-boundary-review-v0.7.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "threshold_review_status": status,
        "release_passed": bool(release_passed),
        "gate_algebra_ready": bool(gate_ready),
        "core_tsek_class_counts": code["class_counts"],
        "report_tsek_class_counts": report_counts,
        "threshold_terms": code["threshold_terms"],
        "numeric_literals_seen": code["numeric_literals_seen"],
        "classifier_function_count": code["function_count"],
        "classifier_functions": code["functions"],
        "report_sources_scanned_with_tsek_classes": report_sources,
        "gaps": gaps,
        "gap_count": len(gaps),
        "replay_allowed": False,
        "executor_ran": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "thresholds_changed": False,
        "classifier_changed": False,
        "next_recommendation": "Move to v0.7.5 TSEK Boundary Explanation Cards before any classifier threshold changes.",
        "boundary": "TSEK threshold boundary reviews are local classifier-governance analysis artifacts. They inspect current threshold/class-boundary visibility without changing classifier behavior. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "tsek_threshold_boundary_review_v0_7_4.json", summary)
    wjson(OUT / "latest_tsek_threshold_boundary_review.json", summary)
    wtext(OUT / "tsek_threshold_boundary_review_v0_7_4.md", make_md(summary))
    wtext(OUT / "latest_tsek_threshold_boundary_review.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "threshold_review_status": summary["threshold_review_status"],
        "release_passed": summary["release_passed"],
        "gate_algebra_ready": summary["gate_algebra_ready"],
        "gap_count": summary["gap_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
