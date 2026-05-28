
from __future__ import annotations
import json, os, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "gate_algebra"
VIS = ROOT / "visuals" / "gate_algebra" / "v0_7_3"

SOURCE_DIRS = [
    ROOT / "src" / "tau_scaling" / "core",
    ROOT / "src" / "tau_scaling" / "gates",
    ROOT / "src" / "tau_scaling" / "tau",
    ROOT / "src" / "tau_scaling" / "claims",
]
SEED_DIR = ROOT / "configs" / "seeds"
SEMANTICS = ROOT / "reports" / "tau_vector_semantics" / "latest_tau_vector_semantics_ledger.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

GATE_FAMILIES = {
    "workload": ["workload", "task", "profile"],
    "baseline": ["baseline", "gain", "candidate"],
    "logicfolding": ["logicfolding", "survivability", "survive"],
    "edge_surface": ["edge", "surface", "boundary"],
    "energy_thermal": ["energy", "thermal", "power"],
    "pdn_pvt": ["pdn", "pvt", "voltage", "process", "temperature"],
    "monte_carlo": ["monte", "carlo", "stress", "prior"],
    "evidence": ["evidence", "finding", "package"],
    "classifier": ["tsek", "class", "score", "threshold"],
}

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

def source_text():
    chunks = []
    files = []
    for d in SOURCE_DIRS:
        if d.exists():
            for p in sorted(d.rglob("*.py")):
                chunks.append(read_text(p))
                files.append(rel(p))
    return "\n".join(chunks), files

def scan_gate_families(text: str, seed_text: str):
    rows = []
    for family, terms in GATE_FAMILIES.items():
        core_count = sum(len(re.findall(re.escape(t), text, re.I)) for t in terms)
        seed_count = sum(len(re.findall(re.escape(t), seed_text, re.I)) for t in terms)
        if core_count and seed_count:
            status = "core_and_seed_visible"
        elif core_count:
            status = "core_visible_seed_implicit"
        elif seed_count:
            status = "seed_visible_core_implicit"
        else:
            status = "not_visible"
        rows.append({
            "gate_family": family,
            "terms": terms,
            "core_count": core_count,
            "seed_count": seed_count,
            "visibility_status": status,
            "mutation_allowed": False,
        })
    return rows

def seed_gate_matrix():
    rows = []
    for p in sorted(SEED_DIR.glob("*.json")):
        text = read_text(p).lower()
        row = {"path": rel(p)}
        for family, terms in GATE_FAMILIES.items():
            row[family] = any(t in text for t in terms)
        row["visible_family_count"] = sum(1 for f in GATE_FAMILIES if row[f])
        rows.append(row)
    return rows

def classify(rows, matrix, semantics, release):
    gaps = []
    if any(r["visibility_status"] == "not_visible" for r in rows):
        gaps.append("some_gate_families_not_visible_in_core_or_seed_scan")
    if any(r["visibility_status"] == "seed_visible_core_implicit" for r in rows):
        gaps.append("some_gate_families_seed_visible_but_core_implicit")
    if any(r["visibility_status"] == "core_visible_seed_implicit" for r in rows):
        gaps.append("some_gate_families_core_visible_but_seed_implicit")
    if matrix and any(row["visible_family_count"] < 3 for row in matrix):
        gaps.append("some_seed_cards_have_sparse_gate_family_visibility")
    if semantics.get("semantics_status") != "TAU_VECTOR_SEMANTICS_LEDGER_READY__TARGETED_FIELDS_IDENTIFIED":
        gaps.append("tau_vector_semantics_not_in_expected_ready_state")

    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    if not release_passed:
        gaps.append("release_not_passing")

    status = "GATE_ALGEBRA_MAP_READY__TARGETED_GATE_GAPS_IDENTIFIED" if release_passed else "GATE_ALGEBRA_MAP_NEEDS_RELEASE_REVIEW"
    return gaps, status, release_passed

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

    rows = summary["gate_family_rows"]
    plt.figure(figsize=(11, 4))
    plt.bar([r["gate_family"] for r in rows], [r["core_count"] for r in rows])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Core mentions")
    plt.title("Gate Algebra Core Visibility")
    save("gate_algebra_core_visibility.png")

    plt.figure(figsize=(11, 4))
    plt.bar([r["gate_family"] for r in rows], [r["seed_count"] for r in rows])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Seed mentions")
    plt.title("Gate Algebra Seed Visibility")
    save("gate_algebra_seed_visibility.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "semantics_ready": int(summary["semantics_ready"]),
        "gap_count": summary["gap_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.ylabel("Value")
    plt.title("Gate Algebra Map Health")
    save("gate_algebra_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.3 Gate Algebra Map",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Map Result",
        "",
        f"- Gate algebra status: `{summary['gate_algebra_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Semantics ready: `{summary['semantics_ready']}`",
        f"- Source files scanned: `{summary['source_file_count']}`",
        f"- Seed count: `{summary['seed_count']}`",
        f"- Gap count: `{summary['gap_count']}`",
        "",
        "## Gate Family Map",
        "",
        "| Gate family | Core count | Seed count | Visibility |",
        "|---|---:|---:|---|",
    ]
    for r in summary["gate_family_rows"]:
        lines.append(f"| `{r['gate_family']}` | {r['core_count']} | {r['seed_count']} | `{r['visibility_status']}` |")
    lines += [
        "",
        "## Seed Gate Matrix",
        "",
        "| Seed | Visible families |",
        "|---|---:|",
    ]
    for row in summary["seed_gate_matrix"]:
        lines.append(f"| `{row['path']}` | {row['visible_family_count']} |")
    lines += ["", "## Targeted Gaps", ""]
    if summary["gaps"]:
        for gap in summary["gaps"]:
            lines.append(f"- `{gap}`")
    else:
        lines.append("- `none_detected_in_v0_7_3_scan`")
    lines += [
        "",
        "## Next Tau Work",
        "",
        "1. Build a gate-to-tau-vector mapping table.",
        "2. Separate evidence-required gates from classifier-weighted gates.",
        "3. Identify gate families that can over-penalize high-support claims.",
        "4. Add tests for gate-family downgrade behavior before changing thresholds.",
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
    text, source_files = source_text()
    seed_text = "\n".join(read_text(p) for p in sorted(SEED_DIR.glob("*.json")))
    semantics = read_json(SEMANTICS)
    release = read_json(RELEASE)

    gate_rows = scan_gate_families(text, seed_text)
    matrix = seed_gate_matrix()
    gaps, status, release_passed = classify(gate_rows, matrix, semantics, release)
    semantics_ready = semantics.get("semantics_status") == "TAU_VECTOR_SEMANTICS_LEDGER_READY__TARGETED_FIELDS_IDENTIFIED"

    summary = {
        "schema": "tau-scaling-gate-algebra-map-v0.7.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "gate_algebra_status": status,
        "release_passed": bool(release_passed),
        "semantics_ready": bool(semantics_ready),
        "source_files": source_files,
        "source_file_count": len(source_files),
        "seed_count": len(matrix),
        "gate_family_rows": gate_rows,
        "seed_gate_matrix": matrix,
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
        "next_recommendation": "Move to v0.7.4 TSEK Threshold Boundary Review after gate-family visibility is mapped.",
        "boundary": "Gate algebra maps are local classifier-governance analysis artifacts. They map gate visibility and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "gate_algebra_map_v0_7_3.json", summary)
    wjson(OUT / "latest_gate_algebra_map.json", summary)
    wtext(OUT / "gate_algebra_map_v0_7_3.md", make_md(summary))
    wtext(OUT / "latest_gate_algebra_map.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "gate_algebra_status": summary["gate_algebra_status"],
        "release_passed": summary["release_passed"],
        "semantics_ready": summary["semantics_ready"],
        "source_file_count": summary["source_file_count"],
        "seed_count": summary["seed_count"],
        "gap_count": summary["gap_count"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/gate_algebra/latest_gate_algebra_map.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
