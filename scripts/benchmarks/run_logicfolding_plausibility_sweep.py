from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "reports" / "logicfolding_plausibility"
VIS_DIR = ROOT / "visuals" / "logicfolding_plausibility" / "v0_8_3"

SCENARIOS = [
    {"scenario_id":"conservative_public","label":"Conservative public","rho":[0.20,0.55],"wire":[8,38],"vertical":[10,34],"route":[6,26],"sync":[3,16],"variation":[3,18],"closure":[5,24],"tau_gain":[1.02,1.45],"energy":[1.00,1.55],"thermal":[1.00,1.45],"pdn":[1.00,1.30]},
    {"scenario_id":"balanced_engineering","label":"Balanced engineering","rho":[0.45,0.75],"wire":[25,75],"vertical":[8,24],"route":[4,18],"sync":[2,10],"variation":[2,10],"closure":[4,16],"tau_gain":[1.15,1.95],"energy":[0.90,1.30],"thermal":[0.90,1.25],"pdn":[0.95,1.18]},
    {"scenario_id":"optimistic_reported_path","label":"Optimistic reported path","rho":[0.65,0.90],"wire":[55,125],"vertical":[5,18],"route":[2,12],"sync":[1,8],"variation":[1,7],"closure":[2,12],"tau_gain":[1.45,2.75],"energy":[0.80,1.18],"thermal":[0.85,1.18],"pdn":[0.90,1.12]},
    {"scenario_id":"aggressive_best_case","label":"Aggressive best-case","rho":[0.78,0.98],"wire":[90,180],"vertical":[3,12],"route":[1,8],"sync":[0.5,5],"variation":[0.5,5],"closure":[1,7],"tau_gain":[1.80,3.50],"energy":[0.75,1.05],"thermal":[0.80,1.08],"pdn":[0.85,1.05]},
    {"scenario_id":"thermal_stressed","label":"Thermal stressed","rho":[0.60,0.88],"wire":[50,120],"vertical":[6,18],"route":[3,14],"sync":[2,8],"variation":[2,9],"closure":[3,12],"tau_gain":[1.40,2.50],"energy":[1.05,1.55],"thermal":[1.35,2.10],"pdn":[1.00,1.25]},
    {"scenario_id":"closure_stressed","label":"Closure stressed","rho":[0.55,0.82],"wire":[45,110],"vertical":[6,20],"route":[12,34],"sync":[5,18],"variation":[5,18],"closure":[18,48],"tau_gain":[1.30,2.20],"energy":[0.90,1.35],"thermal":[0.95,1.35],"pdn":[0.95,1.30]},
]

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def rng_value(rng, pair):
    return rng.uniform(float(pair[0]), float(pair[1]))

def run_scenario(scenario, samples=5000):
    rng = random.Random(8300 + sum(ord(ch) for ch in scenario["scenario_id"]))
    margins = []
    gammas = []
    pass_margin = 0
    pass_gamma = 0
    pass_closure = 0
    pass_joint = 0

    for _ in range(samples):
        rho = rng_value(rng, scenario["rho"])
        wire = rng_value(rng, scenario["wire"])
        vertical = rng_value(rng, scenario["vertical"])
        route = rng_value(rng, scenario["route"])
        sync = rng_value(rng, scenario["sync"])
        variation = rng_value(rng, scenario["variation"])
        closure = rng_value(rng, scenario["closure"])
        tau_gain = rng_value(rng, scenario["tau_gain"])
        energy = rng_value(rng, scenario["energy"])
        thermal = rng_value(rng, scenario["thermal"])
        pdn = rng_value(rng, scenario["pdn"])

        margin = rho * wire - (vertical + route + sync + variation + closure)
        gamma = tau_gain / (energy * thermal * pdn)
        closure_ok = closure < (rho * wire * 0.55)

        margins.append(margin)
        gammas.append(gamma)

        if margin > 0:
            pass_margin += 1
        if gamma > 1:
            pass_gamma += 1
        if closure_ok:
            pass_closure += 1
        if margin > 0 and gamma > 1 and closure_ok:
            pass_joint += 1

    def pct(x):
        return round(100 * x / samples, 3)

    joint = pct(pass_joint)
    if joint >= 75:
        verdict = "plausible_under_declared_priors"
    elif joint >= 25:
        verdict = "conditional_plausibility"
    elif joint > 0:
        verdict = "narrow_plausibility_window"
    else:
        verdict = "not_plausible_under_declared_priors"

    return {
        "scenario_id": scenario["scenario_id"],
        "label": scenario["label"],
        "samples": samples,
        "mean_margin_ps": round(mean(margins), 3),
        "mean_gamma_tau_etp": round(mean(gammas), 4),
        "pass_margin_pct": pct(pass_margin),
        "pass_gamma_pct": pct(pass_gamma),
        "post_route_closure_proxy_pass_pct": pct(pass_closure),
        "joint_pass_pct": joint,
        "verdict": verdict,
    }

def make_svg(results):
    max_joint = max([r["joint_pass_pct"] for r in results] + [1])
    rows = []
    y = 175
    for r in results:
        bar = int(520 * r["joint_pass_pct"] / max_joint) if max_joint else 0
        if r["joint_pass_pct"] >= 75:
            color = "#22c55e"
        elif r["joint_pass_pct"] >= 25:
            color = "#22d3ee"
        elif r["joint_pass_pct"] > 0:
            color = "#f59e0b"
        else:
            color = "#ef4444"
        rows.append('<text x="70" y="' + str(y+22) + '" fill="#e5e7eb" font-size="22" font-family="Segoe UI">' + r["label"] + '</text>')
        rows.append('<rect x="420" y="' + str(y) + '" width="' + str(bar) + '" height="32" rx="12" fill="' + color + '"/>')
        rows.append('<text x="' + str(450+bar) + '" y="' + str(y+24) + '" fill="#f8fafc" font-size="21" font-family="Segoe UI">' + str(r["joint_pass_pct"]) + '%</text>')
        rows.append('<text x="1040" y="' + str(y+22) + '" fill="#cbd5e1" font-size="20" font-family="Segoe UI">margin ' + str(r["mean_margin_ps"]) + ' ps | gamma ' + str(r["mean_gamma_tau_etp"]) + '</text>')
        y += 78

    return '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="760" viewBox="0 0 1400 760"><rect width="1400" height="760" fill="#030712"/><text x="700" y="75" text-anchor="middle" fill="#67e8f9" font-size="50" font-family="Segoe UI" font-weight="700">LogicFolding Plausibility Sweep</text><text x="700" y="120" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Joint pass = margin greater than 0, gamma_tau_ETP greater than 1, and closure proxy passes</text>' + "".join(rows) + '<text x="700" y="710" text-anchor="middle" fill="#94a3b8" font-size="21" font-family="Segoe UI">Synthetic plausibility only. This is not silicon validation, product validation, or benchmark superiority proof.</text></svg>'

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    results = [run_scenario(s) for s in SCENARIOS]
    strongest = max(results, key=lambda r: r["joint_pass_pct"])
    weakest = min(results, key=lambda r: r["joint_pass_pct"])

    summary = {
        "schema": "tau-scaling-logicfolding-plausibility-sweep-v0.8.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scenario_count": len(results),
        "samples_per_scenario": results[0]["samples"] if results else 0,
        "results": results,
        "strongest_scenario": strongest,
        "weakest_scenario": weakest,
        "research_finding": "LogicFolding is conditionally plausible when critical-path coverage and wire-delay savings are high enough to dominate vertical, routing, synchronization, variation, and closure costs, and when energy/thermal/PDN-normalized tau gain remains above one.",
        "falsification_pressure": "Thermal-stressed and closure-stressed priors show how plausible timing gains can collapse when companion gates dominate.",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "This sweep tests synthetic plausibility of a TSEK inequality. It does not validate Huawei silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "logicfolding_plausibility_sweep_v0_8_3.json", summary)
    write_json(REPORT_DIR / "latest_logicfolding_plausibility_sweep.json", summary)

    lines = [
        "# LogicFolding Plausibility Sweep v0.8.3",
        "",
        "## Purpose",
        "",
        "Test when the TSEK LogicFolding inequality becomes plausible under synthetic priors.",
        "",
        "```text",
        "rho_c * E[delta_tau_wire] > E[tau_vertical] + tau_route + tau_sync + tau_variation + tau_closure",
        "gamma_tau_ETP > 1",
        "```",
        "",
        "## Research Finding",
        "",
        summary["research_finding"],
        "",
        "## Scenario Results",
        "",
        "| Scenario | Mean margin ps | Mean gamma_tau_ETP | Margin pass % | Gamma pass % | Closure proxy pass % | Joint pass % | Verdict |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in results:
        lines.append("| " + r["label"] + " | " + str(r["mean_margin_ps"]) + " | " + str(r["mean_gamma_tau_etp"]) + " | " + str(r["pass_margin_pct"]) + " | " + str(r["pass_gamma_pct"]) + " | " + str(r["post_route_closure_proxy_pass_pct"]) + " | " + str(r["joint_pass_pct"]) + " | " + r["verdict"] + " |")

    lines += [
        "",
        "## Strongest Scenario",
        "",
        "`" + strongest["label"] + "` with joint pass `" + str(strongest["joint_pass_pct"]) + "%`.",
        "",
        "## Falsification Pressure",
        "",
        summary["falsification_pressure"],
        "",
        "## Visual",
        "",
        "![LogicFolding plausibility sweep](../../visuals/logicfolding_plausibility/v0_8_3/logicfolding_plausibility_sweep.svg)",
        "",
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    write(REPORT_DIR / "logicfolding_plausibility_sweep_v0_8_3.md", "\n".join(lines))
    write(REPORT_DIR / "latest_logicfolding_plausibility_sweep.md", "\n".join(lines))

    write(REPORT_DIR / "README.md", "# LogicFolding Plausibility Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.3 - LogicFolding Plausibility Sweep**\n\n## Purpose\n\nThis folder stores synthetic plausibility sweeps for the TSEK LogicFolding survivability inequality.\n\n## Primary command\n\n```powershell\npython scripts/benchmarks/run_logicfolding_plausibility_sweep.py\n```\n\n## README Update Rule\n\nUpdate this mini README whenever LogicFolding scenarios, priors, outputs, or visuals change.\n\nBoundary: plausibility sweeps are synthetic research instruments only.\n")
    write(ROOT / "visuals" / "logicfolding_plausibility" / "README.md", "# LogicFolding Plausibility Visuals\n\nCurrent layer: **TAU-SCALING-SA v0.8.3 - LogicFolding Plausibility Sweep**\n\n## Purpose\n\nThis folder stores visuals for LogicFolding plausibility sweeps.\n\n## README Update Rule\n\nUpdate this mini README whenever charts or scenario visualizations change.\n\nBoundary: visual summaries are not silicon validation.\n")
    write(VIS_DIR / "README.md", "# v0.8.3 LogicFolding Plausibility Visuals\n\nCharts:\n\n- `logicfolding_plausibility_sweep.svg`\n\nBoundary: synthetic plausibility visualization only.\n")
    write(VIS_DIR / "logicfolding_plausibility_sweep.svg", make_svg(results))

    print(json.dumps({
        "schema": summary["schema"],
        "scenario_count": summary["scenario_count"],
        "samples_per_scenario": summary["samples_per_scenario"],
        "strongest_scenario": strongest["scenario_id"],
        "strongest_joint_pass_pct": strongest["joint_pass_pct"],
        "weakest_scenario": weakest["scenario_id"],
        "weakest_joint_pass_pct": weakest["joint_pass_pct"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "report": "reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()