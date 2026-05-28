
from __future__ import annotations
import json, os, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "tau_vector_semantics"
VIS = ROOT / "visuals" / "tau_vector_semantics" / "v0_7_2"

CORE_FILES = [
    ROOT / "src" / "tau_scaling" / "core" / "runtime.py",
    ROOT / "src" / "tau_scaling" / "core" / "classifier.py",
    ROOT / "src" / "tau_scaling" / "core" / "models.py",
]
SEED_DIR = ROOT / "configs" / "seeds"
MECH = ROOT / "reports" / "tau_mechanics_review" / "latest_tau_mechanics_return_review.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

TAU_TERMS = [
    "tau_gain",
    "tau_vector",
    "logicfolding",
    "survivability",
    "edge_surface",
    "energy",
    "thermal",
    "pdn",
    "pvt",
    "monte_carlo",
    "baseline",
    "candidate",
    "workload",
]

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

def flatten_keys(obj, prefix=""):
    keys = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else str(k)
            keys.append(p)
            keys.extend(flatten_keys(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:20]):
            p = f"{prefix}[]" if prefix else "[]"
            keys.extend(flatten_keys(v, p))
    return keys

def seed_semantics():
    rows = []
    all_keys = Counter()
    for p in sorted(SEED_DIR.glob("*.json")):
        data = read_json(p)
        text = json.dumps(data).lower()
        keys = flatten_keys(data)
        for k in keys:
            all_keys[k] += 1
        present_terms = [term for term in TAU_TERMS if term.lower() in text]
        rows.append({
            "path": rel(p),
            "key_count": len(keys),
            "present_tau_terms": present_terms,
            "term_count": len(present_terms),
            "has_workload": "workload" in text,
            "has_baseline": "baseline" in text,
            "has_candidate": "candidate" in text,
            "has_tau": "tau" in text,
            "has_gate": any(x in text for x in ["gate", "thermal", "pdn", "pvt", "energy"]),
        })
    return rows, dict(all_keys.most_common(80))

def code_semantics():
    text = "\n".join(read_text(p) for p in CORE_FILES)
    rows = []
    for term in TAU_TERMS:
        rows.append({
            "term": term,
            "core_count": len(re.findall(re.escape(term), text, re.I)),
            "seed_count": 0,
            "semantic_status": "core_visible" if re.search(re.escape(term), text, re.I) else "seed_or_report_only",
        })
    # symbolic field approximations from code names / dict keys
    functions = sorted(set(re.findall(r"def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", text)))
    classes = sorted(set(re.findall(r"class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", text)))
    return rows, functions, classes

def classify(rows, seeds, mechanics, release):
    gaps = []
    seed_count = len(seeds)
    if seed_count == 0:
        gaps.append("no_seed_cards_found")
    if any(not s["has_tau"] for s in seeds):
        gaps.append("some_seed_cards_do_not_explicitly_surface_tau_terms")
    if any(not s["has_gate"] for s in seeds):
        gaps.append("some_seed_cards_do_not_explicitly_surface_gate_terms")
    if any(not s["has_baseline"] for s in seeds):
        gaps.append("some_seed_cards_do_not_explicitly_surface_baseline_terms")
    if any(r["core_count"] == 0 for r in rows if r["term"] in ["tau_vector", "tau_gain"]):
        gaps.append("tau_vector_or_tau_gain_semantics_need_more_explicit_core_naming")

    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    mechanics_ready = mechanics.get("release_passed") is True and mechanics.get("approval_corridor_locked") is True

    if release_passed and mechanics_ready:
        status = "TAU_VECTOR_SEMANTICS_LEDGER_READY__TARGETED_FIELDS_IDENTIFIED"
    else:
        status = "TAU_VECTOR_SEMANTICS_LEDGER_NEEDS_REVIEW"

    return gaps, status, release_passed, mechanics_ready

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

    terms = summary["tau_term_rows"]
    plt.figure(figsize=(10, 4))
    plt.bar([r["term"] for r in terms], [r["core_count"] for r in terms])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Core code mentions")
    plt.title("Tau Vector Semantics Core Term Visibility")
    save("tau_vector_core_term_visibility.png")

    seeds = summary["seed_semantic_rows"]
    plt.figure(figsize=(10, 4))
    plt.bar([Path(s["path"]).stem for s in seeds], [s["term_count"] for s in seeds])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Tau term count")
    plt.title("Seed Card Tau Term Coverage")
    save("tau_vector_seed_term_coverage.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "mechanics_ready": int(summary["mechanics_ready"]),
        "gaps": summary["gap_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.ylabel("Value")
    plt.title("Tau Vector Semantics Health")
    save("tau_vector_semantics_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.2 Tau Vector Semantics Ledger",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Ledger Result",
        "",
        f"- Semantics status: `{summary['semantics_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Mechanics ready: `{summary['mechanics_ready']}`",
        f"- Seed count: `{summary['seed_count']}`",
        f"- Gap count: `{summary['gap_count']}`",
        "",
        "## Tau Term Ledger",
        "",
        "| Term | Core count | Status |",
        "|---|---:|---|",
    ]
    for r in summary["tau_term_rows"]:
        lines.append(f"| `{r['term']}` | {r['core_count']} | `{r['semantic_status']}` |")
    lines += [
        "",
        "## Seed Semantics",
        "",
        "| Seed | Tau terms | Workload | Baseline | Candidate | Gate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for s in summary["seed_semantic_rows"]:
        lines.append(f"| `{s['path']}` | {s['term_count']} | `{s['has_workload']}` | `{s['has_baseline']}` | `{s['has_candidate']}` | `{s['has_gate']}` |")
    lines += ["", "## Targeted Gaps", ""]
    if summary["gaps"]:
        for gap in summary["gaps"]:
            lines.append(f"- `{gap}`")
    else:
        lines.append("- `none_detected_in_v0_7_2_scan`")
    lines += [
        "",
        "## Next Tau Work",
        "",
        "1. Convert implicit tau terms into an explicit tau-vector schema table.",
        "2. Define field-level semantics: what each tau component means, what evidence supports it, and which gates consume it.",
        "3. Add claim-card negative controls for overloaded tau fields.",
        "4. Review TSEK score sensitivity to individual tau-vector components.",
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
    mechanics = read_json(MECH)
    release = read_json(RELEASE)
    seeds, key_counts = seed_semantics()
    term_rows, functions, classes = code_semantics()

    seed_texts = {Path(s["path"]).name: set(s["present_tau_terms"]) for s in seeds}
    for row in term_rows:
        row["seed_count"] = sum(1 for terms in seed_texts.values() if row["term"] in terms)

    gaps, status, release_passed, mechanics_ready = classify(term_rows, seeds, mechanics, release)

    summary = {
        "schema": "tau-scaling-tau-vector-semantics-ledger-v0.7.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "semantics_status": status,
        "release_passed": bool(release_passed),
        "mechanics_ready": bool(mechanics_ready),
        "seed_count": len(seeds),
        "tau_term_rows": term_rows,
        "seed_semantic_rows": seeds,
        "seed_key_counts_top": key_counts,
        "core_function_count": len(functions),
        "core_class_count": len(classes),
        "core_functions": functions[:80],
        "core_classes": classes[:80],
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
        "next_recommendation": "Move to v0.7.3 Gate Algebra Map: explicitly map tau-vector fields to gates and TSEK scoring.",
        "boundary": "Tau vector semantics ledgers are local classifier-governance analysis artifacts. They document semantics and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "tau_vector_semantics_ledger_v0_7_2.json", summary)
    wjson(OUT / "latest_tau_vector_semantics_ledger.json", summary)
    wtext(OUT / "tau_vector_semantics_ledger_v0_7_2.md", make_md(summary))
    wtext(OUT / "latest_tau_vector_semantics_ledger.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "semantics_status": summary["semantics_status"],
        "release_passed": summary["release_passed"],
        "mechanics_ready": summary["mechanics_ready"],
        "seed_count": summary["seed_count"],
        "gap_count": summary["gap_count"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
