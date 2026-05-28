
from __future__ import annotations
import json, os, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "tau_mechanics_review"
VIS = ROOT / "visuals" / "tau_mechanics_review" / "v0_7_1"

PATHS = {
    "runtime": ROOT / "src" / "tau_scaling" / "core" / "runtime.py",
    "classifier": ROOT / "src" / "tau_scaling" / "core" / "classifier.py",
    "models": ROOT / "src" / "tau_scaling" / "core" / "models.py",
    "release": ROOT / "reports" / "release" / "latest_release_readiness.json",
    "synthetic_gate": ROOT / "reports" / "gates" / "latest_synthetic_gate_report.json",
    "sensitivity": ROOT / "reports" / "sensitivity" / "latest_sensitivity_sweep.json",
    "interactions": ROOT / "reports" / "interactions" / "latest_gate_interaction_matrix.json",
    "benchmark": ROOT / "reports" / "benchmarks" / "latest_benchmark_summary.json",
    "approval_corridor": ROOT / "reports" / "approval_corridor" / "latest_approval_governance_corridor_milestone.json",
}

SEED_DIR = ROOT / "configs" / "seeds"

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

def extract_code_signals():
    text = "\n".join(read_text(p) for p in [PATHS["runtime"], PATHS["classifier"], PATHS["models"]])
    tokens = {
        "tau_mentions": len(re.findall(r"\btau\b|tau_", text, re.I)),
        "gate_mentions": len(re.findall(r"\bgate\b|gates|threshold", text, re.I)),
        "tsek_mentions": len(re.findall(r"TSEK", text)),
        "evidence_mentions": len(re.findall(r"evidence", text, re.I)),
        "baseline_mentions": len(re.findall(r"baseline", text, re.I)),
        "workload_mentions": len(re.findall(r"workload", text, re.I)),
    }
    functions = sorted(set(re.findall(r"def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", text)))
    classes = sorted(set(re.findall(r"class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", text)))
    return {"token_counts": tokens, "function_count": len(functions), "class_count": len(classes), "functions": functions[:80], "classes": classes[:80]}

def collect_seed_cards():
    cards = []
    for p in sorted(SEED_DIR.glob("*.json")):
        data = read_json(p)
        text = json.dumps(data).lower()
        cards.append({
            "path": rel(p),
            "has_workload": "workload" in text,
            "has_baseline": "baseline" in text,
            "has_candidate": "candidate" in text,
            "has_tau": "tau" in text,
            "has_gate": "gate" in text or "thermal" in text or "pdn" in text or "pvt" in text,
            "keys": sorted(list(data.keys())) if isinstance(data, dict) else [],
        })
    return cards

def classify_mechanics(code, cards, reports):
    coverage = {
        "seed_count": len(cards),
        "seeds_with_workload": sum(c["has_workload"] for c in cards),
        "seeds_with_baseline": sum(c["has_baseline"] for c in cards),
        "seeds_with_candidate": sum(c["has_candidate"] for c in cards),
        "seeds_with_tau": sum(c["has_tau"] for c in cards),
        "seeds_with_gate": sum(c["has_gate"] for c in cards),
    }
    release = reports["release"]
    approval = reports["approval_corridor"]
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    corridor_locked = approval.get("corridor_locked") is True

    gaps = []
    if coverage["seed_count"] == 0:
        gaps.append("no_seed_cards_found")
    if coverage["seeds_with_tau"] < coverage["seed_count"]:
        gaps.append("some_seed_cards_do_not_surface_tau_terms")
    if coverage["seeds_with_gate"] < coverage["seed_count"]:
        gaps.append("some_seed_cards_do_not_surface_gate_terms")
    if code["token_counts"]["tsek_mentions"] == 0:
        gaps.append("tsek_not_visible_in_core_code_scan")
    if not release_passed:
        gaps.append("release_not_passing")
    if not corridor_locked:
        gaps.append("approval_corridor_not_locked")

    if not gaps:
        status = "TAU_MECHANICS_REVIEW_READY__RETURN_TO_CORE_ENGINE"
    else:
        status = "TAU_MECHANICS_REVIEW_READY__TARGETED_GAPS_IDENTIFIED"

    return coverage, gaps, status, release_passed, corridor_locked

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        wtext(OUT / "chart_generation_skipped.txt", str(exc))
        return paths

    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        path = VIS / name
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(path))

    counts = summary["code_signals"]["token_counts"]
    plt.figure(figsize=(10, 4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Tau Mechanics Code Signal Scan")
    save("tau_mechanics_code_signals.png")

    cov = summary["seed_coverage"]
    ordered = ["seed_count", "seeds_with_workload", "seeds_with_baseline", "seeds_with_candidate", "seeds_with_tau", "seeds_with_gate"]
    plt.figure(figsize=(10, 4))
    plt.bar(ordered, [cov[k] for k in ordered])
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Tau Mechanics Seed Coverage")
    save("tau_mechanics_seed_coverage.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "corridor_locked": int(summary["approval_corridor_locked"]),
        "mechanics_gaps": summary["gap_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("Tau Mechanics Return Health")
    save("tau_mechanics_return_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.1 Tau Mechanics Return Review",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Review Result",
        "",
        f"- Mechanics status: `{summary['mechanics_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Approval corridor locked: `{summary['approval_corridor_locked']}`",
        f"- Seed count: `{summary['seed_coverage']['seed_count']}`",
        f"- Gap count: `{summary['gap_count']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        "",
        "## Core Code Signals",
        "",
        "| Signal | Count |",
        "|---|---:|",
    ]
    for k, v in summary["code_signals"]["token_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Seed Coverage",
        "",
        "| Seed | Workload | Baseline | Candidate | Tau | Gate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for card in summary["seed_cards"]:
        lines.append(f"| `{card['path']}` | `{card['has_workload']}` | `{card['has_baseline']}` | `{card['has_candidate']}` | `{card['has_tau']}` | `{card['has_gate']}` |")

    lines += ["", "## Targeted Gaps", ""]
    if summary["gaps"]:
        for gap in summary["gaps"]:
            lines.append(f"- `{gap}`")
    else:
        lines.append("- `none_detected_in_v0_7_1_scan`")

    lines += [
        "",
        "## Next Tau Work",
        "",
        "1. Define the tau-vector field names and units more explicitly.",
        "2. Separate gate algebra from classifier scoring in documentation and tests.",
        "3. Review TSEK threshold definitions and downgrade/promotion boundaries.",
        "4. Connect synthetic gate suite outputs back to claim-card evidence requirements.",
        "5. Add negative controls for tau-vector overfitting and gate over-penalty.",
        "",
        "## Charts",
        "",
    ]
    for p in summary["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += [
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main():
    reports = {k: read_json(v) for k, v in PATHS.items() if k not in {"runtime", "classifier", "models"}}
    code = extract_code_signals()
    cards = collect_seed_cards()
    coverage, gaps, status, release_passed, corridor_locked = classify_mechanics(code, cards, reports)

    summary = {
        "schema": "tau-scaling-tau-mechanics-return-review-v0.7.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mechanics_status": status,
        "release_passed": bool(release_passed),
        "approval_corridor_locked": bool(corridor_locked),
        "code_signals": code,
        "seed_coverage": coverage,
        "seed_cards": cards,
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
        "next_recommendation": "Move from governance containment into Tau mechanics: tau vectors, gate algebra, TSEK thresholds, synthetic gate suite interpretation, and evidence-card design.",
        "boundary": "Tau mechanics return reviews are local classifier-governance analysis artifacts. They inspect runtime mechanics and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "tau_mechanics_return_review_v0_7_1.json", summary)
    wjson(OUT / "latest_tau_mechanics_return_review.json", summary)
    wtext(OUT / "tau_mechanics_return_review_v0_7_1.md", make_md(summary))
    wtext(OUT / "latest_tau_mechanics_return_review.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "mechanics_status": summary["mechanics_status"],
        "release_passed": summary["release_passed"],
        "approval_corridor_locked": summary["approval_corridor_locked"],
        "seed_count": summary["seed_coverage"]["seed_count"],
        "gap_count": summary["gap_count"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/tau_mechanics_review/latest_tau_mechanics_return_review.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
