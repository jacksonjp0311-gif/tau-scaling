from __future__ import annotations

import json
import statistics
import time
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tau_scaling.core.runtime import TauScalingRuntime

REPO_ROOT = Path(__file__).resolve().parents[2]
SEED_DIR = REPO_ROOT / "configs" / "seeds" / "tests"
REPORT_DIR = REPO_ROOT / "reports" / "benchmarks" / "v0_4_0"
GATE_REPORT_DIR = REPO_ROOT / "reports" / "gates"
FINDING_REPORT_DIR = REPO_ROOT / "reports" / "findings"
VIS_BENCH = REPO_ROOT / "visuals" / "benchmarks" / "v0_4_0"
VIS_FIND = REPO_ROOT / "visuals" / "findings" / "v0_4_0"

GATES = ["B_source", "B_metric", "B_baseline", "B_method", "B_workload", "B_tau", "B_LF", "B_ETP", "B_PVT", "B_yield", "B_evidence"]

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

def set_claim(seed: dict[str, Any], scenario_id: str, text: str) -> dict[str, Any]:
    seed = deepcopy(seed)
    seed.setdefault("claim_card", {})["claim_id"] = scenario_id
    seed["claim_card"]["claim_text"] = text
    return seed

def scenario_definitions() -> list[dict[str, Any]]:
    base = base_seed()
    scenarios: list[dict[str, Any]] = []

    def add(name: str, description: str, expected_class: str, expected_codes: list[str], mutator):
        seed = set_claim(base, name, description)
        seed = mutator(seed)
        scenarios.append({"id": name, "description": description, "expected_class": expected_class, "expected_codes": expected_codes, "seed": seed})

    add("control_all_disclosed_promotable", "All hard gates disclosed; expected promotion-path TSEK-B without independent validation.", "TSEK-B", [], lambda s: s)
    add("yield_missing_downgrade", "Yield is not reported; expect B_yield downgrade.", "TSEK-C", ["TSEK_B_yield_MISSING"], lambda s: (s["yield_method_disclosure"].update({"yield_reported": False}) or s))
    add("missing_workload_downgrade", "Workload class and dominant tau term missing; expect B_workload downgrade.", "TSEK-C", ["TSEK_B_workload_MISSING"], lambda s: (s["workload_profile"].update({"workload_class": "", "dominant_tau_term": ""}) or s))
    add("missing_baseline_downgrade", "Tau vector baseline missing; expect B_baseline downgrade.", "TSEK-C", ["TSEK_B_baseline_MISSING"], lambda s: (s["tau_vector"].pop("baseline", None) and s) or s)
    add("logicfolding_high_vertical_penalty_downgrade", "Vertical and closure penalties erase LogicFolding margin; expect B_LF downgrade.", "TSEK-C", ["TSEK_B_LF_MISSING"], lambda s: (s["logicfolding_survivability"].update({"expected_vertical_penalty_ps": 90.0, "routing_penalty_ps": 20.0, "sync_penalty_ps": 15.0, "variation_penalty_ps": 15.0, "closure_penalty_ps": 20.0}) or s))
    add("etp_thermal_pdn_fail_downgrade", "Energy/thermal/PDN normalization overwhelms tau gain; expect B_ETP downgrade.", "TSEK-C", ["TSEK_B_ETP_MISSING"], lambda s: (s["energy_thermal_pdn_pvt"].update({"tau_gain": 1.05, "energy_ratio_new_over_old": 1.30, "thermal_ratio_new_over_old": 1.35, "pdn_droop_ratio_new_over_old": 1.25}) or s))
    add("pvt_closure_fail_downgrade", "Post-route and PVT closure fail; expect B_PVT downgrade.", "TSEK-C", ["TSEK_B_PVT_MISSING"], lambda s: (s["pvt_closure"].update({"post_route_closure_passed": False, "pvt_variation_passed": False, "pdn_reported": False}) or s))
    add("evidence_package_missing_downgrade", "Evidence package marked incomplete; expect B_evidence downgrade.", "TSEK-C", ["TSEK_B_evidence_MISSING"], lambda s: (s["evidence_disclosure"].update({"evidence_package_complete": False}) or s))
    add("independent_validation_overclaim_block", "Independent validation is claimed without evidence; expect TSEK-E blocking overclaim.", "TSEK-E", ["TSEK_OVERCLAIM_INDEPENDENT_VALIDATION"], lambda s: (s["claim_card"].update({"independent_validation_claimed": True}) or s))
    def multi(s):
        s["claim_card"].update({"claim_text": "", "claim_type": ""})
        s["workload_profile"].update({"workload_class": "", "dominant_tau_term": ""})
        s["tau_vector"].update({"weights_declared": False, "dominant_tau_improved": False})
        s["tau_vector"].pop("baseline", None)
        s["yield_method_disclosure"].update({"method_disclosed": False, "yield_reported": False})
        s["logicfolding_survivability"].update({"expected_vertical_penalty_ps": 90.0, "routing_penalty_ps": 25.0})
        s["energy_thermal_pdn_pvt"].update({"tau_gain": 0.8, "energy_ratio_new_over_old": 1.4, "thermal_ratio_new_over_old": 1.4, "pdn_droop_ratio_new_over_old": 1.4})
        s["pvt_closure"].update({"post_route_closure_passed": False, "pvt_variation_passed": False, "pdn_reported": False})
        s["evidence_disclosure"].update({"evidence_package_complete": False})
        return s
    add("multi_gate_stress_low_disclosure", "Multiple disclosure and gate surfaces fail together; expect broad downgrade.", "TSEK-D", ["TSEK_B_metric_MISSING", "TSEK_B_baseline_MISSING", "TSEK_B_method_MISSING", "TSEK_B_workload_MISSING", "TSEK_B_tau_MISSING", "TSEK_B_LF_MISSING", "TSEK_B_ETP_MISSING", "TSEK_B_PVT_MISSING", "TSEK_B_yield_MISSING", "TSEK_B_evidence_MISSING"], multi)
    return scenarios

def write_seeds(scenarios: list[dict[str, Any]]) -> None:
    SEED_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    for scenario in scenarios:
        path = SEED_DIR / f"{scenario['id']}.json"
        write_json(path, scenario["seed"])
        manifest.append({"id": scenario["id"], "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"), "description": scenario["description"], "expected_class": scenario["expected_class"], "expected_codes": scenario["expected_codes"]})
    write_json(SEED_DIR / "synthetic_gate_manifest_v0_4_0.json", {"schema": "tau-scaling-synthetic-gate-manifest-v0.4.0", "generated_at": datetime.now(timezone.utc).isoformat(), "scenarios": manifest, "non_claim_lock": "Synthetic gate seeds test local runtime downgrade behavior only; they are not silicon/product validation."})

def run_suite(scenarios: list[dict[str, Any]]) -> dict[str, Any]:
    runtime = TauScalingRuntime(REPO_ROOT)
    results = []
    for scenario in scenarios:
        t0 = time.perf_counter()
        result = runtime.run(scenario["seed"])
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        evidence = load_json(Path(result.evidence_path))
        classification = evidence["classification"]
        admissible = classification["admissible_claim"]
        finding_codes = [f["code"] for f in classification.get("findings", [])]
        expected_codes = scenario["expected_codes"]
        expected_found = all(code in finding_codes for code in expected_codes)
        class_passed = result.classification == scenario["expected_class"]
        row = {
            "id": scenario["id"], "description": scenario["description"], "run_id": result.run_id,
            "classification": result.classification, "expected_class": scenario["expected_class"],
            "class_passed": class_passed, "A_TSEK": result.admissible_score,
            "diagnostic_average": admissible.get("diagnostic_average", 0.0),
            "findings_count": result.findings_count, "finding_codes": finding_codes,
            "expected_codes": expected_codes, "expected_findings_present": expected_found,
            "unexpected_missing_expected_codes": [code for code in expected_codes if code not in finding_codes],
            "elapsed_ms": round(elapsed_ms, 4),
            "evidence_path": str(Path(result.evidence_path).relative_to(REPO_ROOT)).replace("\\", "/"),
            "gate_values": {gate: admissible.get(gate, 0.0) for gate in GATES},
            "logicfolding_margin": evidence.get("logicfolding_survivability", {}).get("logicfolding_margin"),
            "gamma_tau_ETP": evidence.get("energy_thermal_pdn_pvt", {}).get("gamma_tau_ETP"),
            "edge_surface": evidence.get("edge_surface_boundary", {}),
        }
        row["scenario_passed"] = class_passed and expected_found
        results.append(row)
    return {
        "schema": "tau-scaling-synthetic-gate-suite-v0.4.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_scenarios": len(results),
        "passed_scenarios": sum(1 for r in results if r["scenario_passed"]),
        "failed_scenarios": sum(1 for r in results if not r["scenario_passed"]),
        "all_scenarios_passed": all(r["scenario_passed"] for r in results),
        "class_counts": dict(Counter(r["classification"] for r in results)),
        "finding_counts": dict(Counter(code for r in results for code in r["finding_codes"])),
        "gate_failure_counts": {gate: sum(1 for r in results if r["gate_values"].get(gate, 0) == 0) for gate in GATES},
        "mean_elapsed_ms": round(statistics.mean(r["elapsed_ms"] for r in results), 4),
        "results": results,
        "boundary": "Synthetic gate suite validates local runtime downgrade behavior only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.",
    }

def try_charts(summary: dict[str, Any]) -> list[str]:
    chart_paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(REPORT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return chart_paths
    VIS_BENCH.mkdir(parents=True, exist_ok=True)
    VIS_FIND.mkdir(parents=True, exist_ok=True)
    results = summary["results"]
    ids = [r["id"] for r in results]
    def savefig(path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        chart_paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))
    plt.figure(figsize=(10, 5)); counts = summary["class_counts"]; plt.bar(list(counts.keys()), list(counts.values())); plt.title("Synthetic Gate Suite - Class Distribution"); plt.ylabel("Scenario count"); savefig(VIS_BENCH / "class_distribution.png")
    for metric, title, ylabel, filename in [("A_TSEK","A_TSEK by Synthetic Scenario","A_TSEK","a_tsek_by_scenario.png"),("findings_count","Finding Count by Synthetic Scenario","Findings","finding_count_by_scenario.png"),("diagnostic_average","Diagnostic Average by Synthetic Scenario","Diagnostic average","diagnostic_average_by_scenario.png"),("elapsed_ms","Runtime Elapsed ms by Scenario","Elapsed ms","elapsed_ms_by_scenario.png")]:
        plt.figure(figsize=(14, 6)); plt.bar(ids, [r[metric] for r in results]); plt.title(title); plt.ylabel(ylabel); plt.xticks(rotation=60, ha="right"); savefig(VIS_BENCH / filename)
    matrix = [[r["gate_values"].get(g, 0) for g in GATES] for r in results]
    plt.figure(figsize=(13, 7)); plt.imshow(matrix, aspect="auto", vmin=0, vmax=1); plt.title("Gate Pass/Fail Heatmap"); plt.yticks(range(len(ids)), ids); plt.xticks(range(len(GATES)), GATES, rotation=45, ha="right"); plt.colorbar(label="Gate value"); savefig(VIS_BENCH / "gate_heatmap.png")
    finding_counts = summary["finding_counts"]
    if finding_counts:
        plt.figure(figsize=(14, 6)); plt.bar(list(finding_counts.keys()), list(finding_counts.values())); plt.title("Finding Code Frequency"); plt.ylabel("Count"); plt.xticks(rotation=60, ha="right"); savefig(VIS_BENCH / "finding_code_frequency.png")
    by_code = defaultdict(list)
    for r in results:
        for code in r["finding_codes"]:
            by_code[code].append(r["id"])
    for code, scenarios in sorted(by_code.items()):
        vals = [1 if r["id"] in scenarios else 0 for r in results]
        plt.figure(figsize=(14, 4)); plt.bar(ids, vals); plt.title(f"Finding Presence - {code}"); plt.ylabel("Present"); plt.xticks(rotation=60, ha="right")
        safe = code.lower().replace("tsek_", "").replace("_", "-")
        savefig(VIS_FIND / f"finding_{safe}.png")
    return chart_paths

def render_markdown(summary: dict[str, Any], charts: list[str]) -> str:
    lines = ["# Tau Scaling v0.4.0 Synthetic Gate Suite","",f"Generated: `{summary['generated_at']}`","", "## Result","", f"- Total scenarios: `{summary['total_scenarios']}`", f"- Passed scenarios: `{summary['passed_scenarios']}`", f"- Failed scenarios: `{summary['failed_scenarios']}`", f"- All scenarios passed: `{summary['all_scenarios_passed']}`", f"- Mean elapsed ms: `{summary['mean_elapsed_ms']}`", "", "## Benchmark Charts", ""]
    for chart in charts:
        if chart.startswith("visuals/benchmarks/"):
            rel = Path(REPO_ROOT / chart).relative_to(REPORT_DIR).as_posix(); lines.extend([f"![{Path(chart).stem}]({rel})", ""])
    lines.extend(["## Scenario Findings", "", "| Scenario | Expected | Actual | A_TSEK | Diagnostic avg | Findings | Passed |", "|---|---|---|---:|---:|---:|---|"])
    for r in summary["results"]:
        lines.append(f"| `{r['id']}` | {r['expected_class']} | {r['classification']} | {r['A_TSEK']} | {r['diagnostic_average']} | {r['findings_count']} | {r['scenario_passed']} |")
    lines.extend(["", "## Finding Code Frequency", "", "| Finding code | Count |", "|---|---:|"])
    for code, count in sorted(summary["finding_counts"].items()):
        lines.append(f"| `{code}` | {count} |")
    lines.extend(["", "## Finding Charts", ""])
    for chart in charts:
        if chart.startswith("visuals/findings/"):
            rel = Path(REPO_ROOT / chart).relative_to(REPORT_DIR).as_posix(); lines.extend([f"![{Path(chart).stem}]({rel})", ""])
    lines.extend(["## Gate Failure Counts", "", "| Gate | Failures |", "|---|---:|"])
    for gate, count in sorted(summary["gate_failure_counts"].items()):
        lines.append(f"| `{gate}` | {count} |")
    lines.extend(["", "## Boundary", "", summary["boundary"], ""])
    return "\n".join(lines)

def main() -> None:
    scenarios = scenario_definitions()
    write_seeds(scenarios)
    summary = run_suite(scenarios)
    charts = try_charts(summary)
    summary["chart_paths"] = charts
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(REPORT_DIR / "synthetic_gate_suite_v0_4_0.json", summary)
    write_json(REPO_ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.json", summary)
    md = render_markdown(summary, charts)
    write_text(REPORT_DIR / "synthetic_gate_suite_v0_4_0.md", md)
    write_text(REPO_ROOT / "reports" / "benchmarks" / "latest_synthetic_gate_suite.md", md)
    write_text(GATE_REPORT_DIR / "latest_synthetic_gate_report.md", md)
    write_json(GATE_REPORT_DIR / "latest_synthetic_gate_report.json", summary)
    write_text(FINDING_REPORT_DIR / "latest_finding_charts.md", md)
    write_json(FINDING_REPORT_DIR / "latest_finding_summary.json", {"schema": "tau-scaling-finding-summary-v0.4.0", "generated_at": summary["generated_at"], "finding_counts": summary["finding_counts"], "chart_paths": [p for p in charts if p.startswith("visuals/findings/")], "non_claim_lock": summary["boundary"]})
    print(json.dumps({"schema": summary["schema"], "all_scenarios_passed": summary["all_scenarios_passed"], "total_scenarios": summary["total_scenarios"], "passed_scenarios": summary["passed_scenarios"], "failed_scenarios": summary["failed_scenarios"], "class_counts": summary["class_counts"], "finding_counts": summary["finding_counts"], "chart_count": len(charts), "report": "reports/benchmarks/latest_synthetic_gate_suite.md"}, indent=2, sort_keys=True))
if __name__ == "__main__":
    main()
