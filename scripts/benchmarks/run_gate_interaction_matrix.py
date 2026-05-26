from __future__ import annotations

import json
import os
import statistics
import time
from copy import deepcopy
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any

from tau_scaling.core.runtime import TauScalingRuntime

REPO_ROOT = Path(__file__).resolve().parents[2]
SEED_DIR = REPO_ROOT / "configs" / "seeds" / "interactions"
REPORT_DIR = REPO_ROOT / "reports" / "interactions"
VIS_DIR = REPO_ROOT / "visuals" / "interactions" / "v0_4_2"

GATE_ORDER = [
    "B_source",
    "B_metric",
    "B_baseline",
    "B_method",
    "B_workload",
    "B_tau",
    "B_LF",
    "B_ETP",
    "B_PVT",
    "B_yield",
    "B_evidence",
]

CLASS_TO_Y = {"TSEK-E": 0, "TSEK-D": 1, "TSEK-C": 2, "TSEK-B": 3, "TSEK-A": 4}

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def base_seed() -> dict[str, Any]:
    return load_json(REPO_ROOT / "configs" / "seeds" / "logicfolding_promotion_path_claim_card.json")

def fail_gate(seed: dict[str, Any], gate: str) -> dict[str, Any]:
    seed = deepcopy(seed)
    if gate == "B_source":
        seed.setdefault("source_boundary", {})["source_declared"] = False
        seed["source_boundary"]["reported_claims_separated_from_validation"] = False
    elif gate == "B_metric":
        seed.setdefault("claim_card", {})["claim_text"] = ""
        seed["claim_card"]["claim_type"] = ""
    elif gate == "B_baseline":
        seed.setdefault("tau_vector", {}).pop("baseline", None)
    elif gate == "B_method":
        seed.setdefault("yield_method_disclosure", {})["method_disclosed"] = False
    elif gate == "B_workload":
        seed.setdefault("workload_profile", {})["workload_class"] = ""
        seed["workload_profile"]["dominant_tau_term"] = ""
    elif gate == "B_tau":
        seed.setdefault("tau_vector", {})["weights_declared"] = False
        seed["tau_vector"]["dominant_tau_improved"] = False
    elif gate == "B_LF":
        seed.setdefault("logicfolding_survivability", {})["expected_vertical_penalty_ps"] = 90.0
        seed["logicfolding_survivability"]["routing_penalty_ps"] = 25.0
        seed["logicfolding_survivability"]["sync_penalty_ps"] = 15.0
        seed["logicfolding_survivability"]["variation_penalty_ps"] = 15.0
        seed["logicfolding_survivability"]["closure_penalty_ps"] = 20.0
    elif gate == "B_ETP":
        seed.setdefault("energy_thermal_pdn_pvt", {})["tau_gain"] = 0.85
        seed["energy_thermal_pdn_pvt"]["energy_ratio_new_over_old"] = 1.40
        seed["energy_thermal_pdn_pvt"]["thermal_ratio_new_over_old"] = 1.40
        seed["energy_thermal_pdn_pvt"]["pdn_droop_ratio_new_over_old"] = 1.40
    elif gate == "B_PVT":
        seed.setdefault("pvt_closure", {})["post_route_closure_passed"] = False
        seed["pvt_closure"]["pvt_variation_passed"] = False
        seed["pvt_closure"]["pdn_reported"] = False
    elif gate == "B_yield":
        seed.setdefault("yield_method_disclosure", {})["yield_reported"] = False
    elif gate == "B_evidence":
        seed.setdefault("evidence_disclosure", {})["evidence_package_complete"] = False
    else:
        raise ValueError(f"unknown gate: {gate}")
    return seed

def scenario_seed(gate_a: str, gate_b: str) -> dict[str, Any]:
    seed = base_seed()
    seed = fail_gate(seed, gate_a)
    seed = fail_gate(seed, gate_b)
    seed.setdefault("claim_card", {})["claim_id"] = f"interaction-{gate_a}-{gate_b}".replace("_", "-")
    seed["claim_card"]["claim_text"] = f"Gate interaction matrix scenario: {gate_a} + {gate_b}."
    seed.setdefault("metadata", {})["interaction_gates"] = [gate_a, gate_b]
    seed["metadata"]["non_claim_lock"] = "Synthetic interaction scenario; local runtime diagnostic only."
    return seed

def write_seeds() -> list[dict[str, Any]]:
    SEED_DIR.mkdir(parents=True, exist_ok=True)
    scenarios: list[dict[str, Any]] = []
    for gate_a, gate_b in combinations(GATE_ORDER, 2):
        seed = scenario_seed(gate_a, gate_b)
        fname = f"{gate_a.lower()}__{gate_b.lower()}.json"
        path = SEED_DIR / fname
        write_json(path, seed)
        scenarios.append({
            "gate_a": gate_a,
            "gate_b": gate_b,
            "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
            "seed": seed,
        })
    write_json(SEED_DIR / "gate_interaction_manifest_v0_4_2.json", {
        "schema": "tau-scaling-gate-interaction-manifest-v0.4.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "gates": GATE_ORDER,
        "scenario_count": len(scenarios),
        "scenarios": [{k: s[k] for k in ("gate_a", "gate_b", "path")} for s in scenarios],
        "non_claim_lock": "Gate interaction seeds are synthetic local runtime diagnostics only.",
    })
    return scenarios

def run_scenario(runtime: TauScalingRuntime, scenario: dict[str, Any]) -> dict[str, Any]:
    t0 = time.perf_counter()
    result = runtime.run(scenario["seed"])
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    evidence = load_json(Path(result.evidence_path))
    classification = evidence["classification"]
    admissible = classification["admissible_claim"]
    finding_codes = [f["code"] for f in classification.get("findings", [])]
    return {
        "gate_a": scenario["gate_a"],
        "gate_b": scenario["gate_b"],
        "classification": result.classification,
        "class_index": CLASS_TO_Y.get(result.classification, -1),
        "A_TSEK": result.admissible_score,
        "diagnostic_average": admissible.get("diagnostic_average", 0.0),
        "findings_count": result.findings_count,
        "finding_codes": finding_codes,
        "gate_values": {g: admissible.get(g, 0.0) for g in GATE_ORDER},
        "logicfolding_margin": evidence.get("logicfolding_survivability", {}).get("logicfolding_margin"),
        "gamma_tau_ETP": evidence.get("energy_thermal_pdn_pvt", {}).get("gamma_tau_ETP"),
        "elapsed_ms": round(elapsed_ms, 4),
        "run_id": result.run_id,
        "evidence_path": str(Path(result.evidence_path).relative_to(REPO_ROOT)).replace("\\", "/"),
        "scenario_passed": scenario["gate_a"] in GATE_ORDER and scenario["gate_b"] in GATE_ORDER,
    }

def build_matrix(results: list[dict[str, Any]], value_key: str) -> list[list[float]]:
    idx = {g: i for i, g in enumerate(GATE_ORDER)}
    n = len(GATE_ORDER)
    matrix = [[float("nan") for _ in range(n)] for _ in range(n)]
    for r in results:
        i, j = idx[r["gate_a"]], idx[r["gate_b"]]
        matrix[i][j] = r[value_key]
        matrix[j][i] = r[value_key]
    return matrix

def generate_charts(results: list[dict[str, Any]]) -> list[str]:
    chart_paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(REPORT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return chart_paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def savefig(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        chart_paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    for key, title, filename, vmin, vmax, cbar in [
        ("class_index", "Gate Pair Class Transition Matrix", "gate_pair_class_matrix.png", 0, 4, "TSEK class index"),
        ("A_TSEK", "Gate Pair A_TSEK Matrix", "gate_pair_a_tsek_matrix.png", 0, 1, "A_TSEK"),
        ("diagnostic_average", "Gate Pair Diagnostic Average Matrix", "gate_pair_diagnostic_average_matrix.png", 0, 1, "Diagnostic average"),
        ("findings_count", "Gate Pair Finding Count Matrix", "gate_pair_finding_count_matrix.png", 0, None, "Findings count"),
    ]:
        matrix = build_matrix(results, key)
        plt.figure(figsize=(9, 8))
        if vmax is None:
            img = plt.imshow(matrix, aspect="auto", vmin=vmin)
        else:
            img = plt.imshow(matrix, aspect="auto", vmin=vmin, vmax=vmax)
        plt.title(title)
        plt.xticks(range(len(GATE_ORDER)), GATE_ORDER, rotation=45, ha="right")
        plt.yticks(range(len(GATE_ORDER)), GATE_ORDER)
        plt.colorbar(img, label=cbar)
        savefig(VIS_DIR / filename)

    class_counts: dict[str, int] = {}
    for r in results:
        class_counts[r["classification"]] = class_counts.get(r["classification"], 0) + 1
    plt.figure(figsize=(7, 4))
    plt.bar(list(class_counts.keys()), list(class_counts.values()))
    plt.title("Gate Interaction Class Distribution")
    plt.ylabel("Pair count")
    savefig(VIS_DIR / "interaction_class_distribution.png")

    sorted_results = sorted(results, key=lambda r: (r["class_index"], r["A_TSEK"], r["diagnostic_average"]))
    labels = [f"{r['gate_a']}+{r['gate_b']}" for r in sorted_results]
    plt.figure(figsize=(13, 5))
    plt.bar(labels, [r["diagnostic_average"] for r in sorted_results])
    plt.title("Diagnostic Average by Gate Pair")
    plt.ylabel("Diagnostic average")
    plt.xticks(rotation=75, ha="right", fontsize=6)
    savefig(VIS_DIR / "diagnostic_average_by_pair.png")

    return chart_paths

def summarize(results: list[dict[str, Any]], charts: list[str]) -> dict[str, Any]:
    class_counts: dict[str, int] = {}
    for r in results:
        class_counts[r["classification"]] = class_counts.get(r["classification"], 0) + 1

    strongest_pairs = sorted(results, key=lambda r: (r["class_index"], r["diagnostic_average"], r["A_TSEK"]))[:10]
    least_severe_pairs = sorted(results, key=lambda r: (-r["class_index"], -r["diagnostic_average"], -r["A_TSEK"]))[:10]

    return {
        "schema": "tau-scaling-gate-interaction-matrix-v0.4.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "gate_count": len(GATE_ORDER),
        "pair_count": len(results),
        "all_pairs_executed": len(results) == (len(GATE_ORDER) * (len(GATE_ORDER) - 1) // 2),
        "class_counts": class_counts,
        "mean_A_TSEK": round(statistics.mean(r["A_TSEK"] for r in results), 4),
        "mean_diagnostic_average": round(statistics.mean(r["diagnostic_average"] for r in results), 4),
        "mean_elapsed_ms": round(statistics.mean(r["elapsed_ms"] for r in results), 4),
        "strongest_downgrade_pairs": strongest_pairs,
        "least_severe_pairs": least_severe_pairs,
        "results": results,
        "chart_paths": charts,
        "boundary": "Gate interaction matrices are synthetic local runtime diagnostics only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.",
    }

def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.2 Gate Interaction Matrix",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Gates: `{summary['gate_count']}`",
        f"- Gate pairs: `{summary['pair_count']}`",
        f"- All pairs executed: `{summary['all_pairs_executed']}`",
        f"- Mean A_TSEK: `{summary['mean_A_TSEK']}`",
        f"- Mean diagnostic average: `{summary['mean_diagnostic_average']}`",
        f"- Chart count: `{len(summary['chart_paths'])}`",
        "",
        "## Class Counts",
        "",
        "| Class | Count |",
        "|---|---:|",
    ]
    for cls, count in sorted(summary["class_counts"].items()):
        lines.append(f"| `{cls}` | {count} |")

    lines += [
        "",
        "## Strongest Downgrade Pairs",
        "",
        "| Gate A | Gate B | Class | A_TSEK | Diagnostic avg | Findings |",
        "|---|---|---|---:|---:|---:|",
    ]
    for r in summary["strongest_downgrade_pairs"]:
        lines.append(f"| `{r['gate_a']}` | `{r['gate_b']}` | {r['classification']} | {r['A_TSEK']} | {r['diagnostic_average']} | {r['findings_count']} |")

    lines += [
        "",
        "## Least Severe Pairs",
        "",
        "| Gate A | Gate B | Class | A_TSEK | Diagnostic avg | Findings |",
        "|---|---|---|---:|---:|---:|",
    ]
    for r in summary["least_severe_pairs"]:
        lines.append(f"| `{r['gate_a']}` | `{r['gate_b']}` | {r['classification']} | {r['A_TSEK']} | {r['diagnostic_average']} | {r['findings_count']} |")

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, REPORT_DIR).replace("\\", "/")
        lines.extend([f"![{Path(chart).stem}]({rel})", ""])

    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main() -> None:
    runtime = TauScalingRuntime(REPO_ROOT)
    scenarios = write_seeds()
    results = [run_scenario(runtime, s) for s in scenarios]
    charts = generate_charts(results)
    summary = summarize(results, charts)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(REPORT_DIR / "gate_interaction_matrix_v0_4_2.json", summary)
    write_json(REPORT_DIR / "latest_gate_interaction_matrix.json", summary)
    md = render_markdown(summary)
    write_text(REPORT_DIR / "gate_interaction_matrix_v0_4_2.md", md)
    write_text(REPORT_DIR / "latest_gate_interaction_matrix.md", md)
    print(json.dumps({
        "schema": summary["schema"],
        "gate_count": summary["gate_count"],
        "pair_count": summary["pair_count"],
        "all_pairs_executed": summary["all_pairs_executed"],
        "class_counts": summary["class_counts"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/interactions/latest_gate_interaction_matrix.md",
    }, indent=2, sort_keys=True))
    if not summary["all_pairs_executed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
