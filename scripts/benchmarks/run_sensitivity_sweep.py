from __future__ import annotations

import json
import os
import statistics
import time
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tau_scaling.core.runtime import TauScalingRuntime

REPO_ROOT = Path(__file__).resolve().parents[2]
SEED_DIR = REPO_ROOT / "configs" / "seeds" / "sweeps"
REPORT_DIR = REPO_ROOT / "reports" / "sensitivity"
VIS_DIR = REPO_ROOT / "visuals" / "sensitivity" / "v0_4_1"

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

def run_seed(runtime: TauScalingRuntime, seed: dict[str, Any], sweep: str, x_name: str, x_value: float) -> dict[str, Any]:
    t0 = time.perf_counter()
    result = runtime.run(seed)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    evidence = load_json(Path(result.evidence_path))
    classification = evidence["classification"]
    admissible = classification["admissible_claim"]
    return {
        "sweep": sweep,
        "x_name": x_name,
        "x_value": x_value,
        "run_id": result.run_id,
        "classification": result.classification,
        "A_TSEK": result.admissible_score,
        "diagnostic_average": admissible.get("diagnostic_average", 0.0),
        "findings_count": result.findings_count,
        "finding_codes": [f["code"] for f in classification.get("findings", [])],
        "logicfolding_margin": evidence.get("logicfolding_survivability", {}).get("logicfolding_margin"),
        "gamma_tau_ETP": evidence.get("energy_thermal_pdn_pvt", {}).get("gamma_tau_ETP"),
        "elapsed_ms": round(elapsed_ms, 4),
        "evidence_path": str(Path(result.evidence_path).relative_to(REPO_ROOT)).replace("\\", "/"),
    }

def make_sweeps() -> list[dict[str, Any]]:
    base = base_seed()
    scenarios: list[dict[str, Any]] = []

    # LogicFolding margin sweep: vertical penalty moves margin across zero.
    # Base margin = rho*wire - sum penalties = .75*42 - (8+5+3+2+4) = 9.5.
    for vertical in [0, 4, 8, 12, 16, 20, 24, 28, 32, 40]:
        seed = deepcopy(base)
        seed["claim_card"]["claim_id"] = f"sweep-lf-vertical-{vertical}"
        seed["claim_card"]["claim_text"] = "Sensitivity sweep: LogicFolding vertical penalty threshold."
        seed["logicfolding_survivability"]["expected_vertical_penalty_ps"] = float(vertical)
        scenarios.append({"sweep": "logicfolding_vertical_penalty", "x_name": "vertical_penalty_ps", "x_value": float(vertical), "seed": seed})

    # gamma_tau_ETP sweep: tau_gain crosses ETP threshold near denominator 0.95*1.05*1.02 ~= 1.01745.
    for tau_gain in [0.70, 0.85, 0.95, 1.00, 1.02, 1.05, 1.10, 1.22, 1.35, 1.50]:
        seed = deepcopy(base)
        seed["claim_card"]["claim_id"] = f"sweep-etp-taugain-{str(tau_gain).replace('.', '_')}"
        seed["claim_card"]["claim_text"] = "Sensitivity sweep: gamma_tau_ETP tau gain threshold."
        seed["energy_thermal_pdn_pvt"]["tau_gain"] = float(tau_gain)
        scenarios.append({"sweep": "gamma_tau_etp_tau_gain", "x_name": "tau_gain", "x_value": float(tau_gain), "seed": seed})

    # Overclaim pressure: A_TSEK declines, with hard block at >=1.
    for overclaim in [0.0, 0.05, 0.10, 0.25, 0.50, 0.70, 0.90, 0.99, 1.0]:
        seed = deepcopy(base)
        seed["claim_card"]["claim_id"] = f"sweep-overclaim-{str(overclaim).replace('.', '_')}"
        seed["claim_card"]["claim_text"] = "Sensitivity sweep: overclaim pressure."
        seed["overclaim"] = float(overclaim)
        scenarios.append({"sweep": "overclaim_pressure", "x_name": "overclaim", "x_value": float(overclaim), "seed": seed})

    return scenarios

def write_seed_manifest(scenarios: list[dict[str, Any]]) -> None:
    SEED_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    for s in scenarios:
        path = SEED_DIR / f"{s['sweep']}__{s['x_name']}__{str(s['x_value']).replace('.', '_')}.json"
        write_json(path, s["seed"])
        manifest.append({
            "sweep": s["sweep"],
            "x_name": s["x_name"],
            "x_value": s["x_value"],
            "path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"),
        })
    write_json(SEED_DIR / "sensitivity_sweep_manifest_v0_4_1.json", {
        "schema": "tau-scaling-sensitivity-sweep-manifest-v0.4.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scenarios": manifest,
        "non_claim_lock": "Sensitivity sweep seeds are synthetic local runtime diagnostics only.",
    })

def summarize(results: list[dict[str, Any]], charts: list[str]) -> dict[str, Any]:
    by_sweep: dict[str, Any] = {}
    for sweep in sorted({r["sweep"] for r in results}):
        rows = [r for r in results if r["sweep"] == sweep]
        transitions = []
        previous = None
        for row in sorted(rows, key=lambda r: r["x_value"]):
            if previous and previous["classification"] != row["classification"]:
                transitions.append({
                    "from_x": previous["x_value"],
                    "to_x": row["x_value"],
                    "from_class": previous["classification"],
                    "to_class": row["classification"],
                })
            previous = row
        by_sweep[sweep] = {
            "points": len(rows),
            "classes": {c: sum(1 for r in rows if r["classification"] == c) for c in sorted({r["classification"] for r in rows})},
            "min_A_TSEK": min(r["A_TSEK"] for r in rows),
            "max_A_TSEK": max(r["A_TSEK"] for r in rows),
            "min_diagnostic_average": min(r["diagnostic_average"] for r in rows),
            "max_diagnostic_average": max(r["diagnostic_average"] for r in rows),
            "transitions": transitions,
        }
    return {
        "schema": "tau-scaling-sensitivity-sweep-v0.4.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_points": len(results),
        "sweeps": by_sweep,
        "mean_elapsed_ms": round(statistics.mean(r["elapsed_ms"] for r in results), 4),
        "results": results,
        "chart_paths": charts,
        "boundary": "Sensitivity sweeps are synthetic local runtime diagnostics only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.",
    }

def generate_charts(results: list[dict[str, Any]]) -> list[str]:
    chart_paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(REPORT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return chart_paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)
    class_to_y = {"TSEK-E": 0, "TSEK-D": 1, "TSEK-C": 2, "TSEK-B": 3, "TSEK-A": 4}

    def savefig(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        chart_paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    for sweep in sorted({r["sweep"] for r in results}):
        rows = sorted([r for r in results if r["sweep"] == sweep], key=lambda r: r["x_value"])
        xs = [r["x_value"] for r in rows]

        plt.figure(figsize=(9, 5))
        plt.plot(xs, [r["A_TSEK"] for r in rows], marker="o")
        plt.title(f"A_TSEK sensitivity - {sweep}")
        plt.xlabel(rows[0]["x_name"])
        plt.ylabel("A_TSEK")
        savefig(VIS_DIR / f"{sweep}_a_tsek_curve.png")

        plt.figure(figsize=(9, 5))
        plt.plot(xs, [r["diagnostic_average"] for r in rows], marker="o")
        plt.title(f"Diagnostic average sensitivity - {sweep}")
        plt.xlabel(rows[0]["x_name"])
        plt.ylabel("diagnostic_average")
        savefig(VIS_DIR / f"{sweep}_diagnostic_average_curve.png")

        plt.figure(figsize=(9, 5))
        plt.step(xs, [class_to_y.get(r["classification"], -1) for r in rows], where="mid")
        plt.yticks(list(class_to_y.values()), list(class_to_y.keys()))
        plt.title(f"Class transition curve - {sweep}")
        plt.xlabel(rows[0]["x_name"])
        plt.ylabel("TSEK class")
        savefig(VIS_DIR / f"{sweep}_class_transition_curve.png")

    # Combined class transition surface.
    sweeps = sorted({r["sweep"] for r in results})
    max_len = max(sum(1 for r in results if r["sweep"] == s) for s in sweeps)
    matrix = []
    for sweep in sweeps:
        row = [class_to_y.get(r["classification"], -1) for r in sorted([r for r in results if r["sweep"] == sweep], key=lambda r: r["x_value"])]
        row = row + [-1] * (max_len - len(row))
        matrix.append(row)
    plt.figure(figsize=(10, 4))
    plt.imshow(matrix, aspect="auto", vmin=0, vmax=4)
    plt.yticks(range(len(sweeps)), sweeps)
    plt.xlabel("sweep point index")
    plt.title("Sensitivity class transition heatmap")
    plt.colorbar(label="TSEK class index")
    savefig(VIS_DIR / "sensitivity_class_transition_heatmap.png")

    return chart_paths

def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.1 Synthetic Gate Sensitivity Sweep",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Total sweep points: `{summary['total_points']}`",
        f"- Mean elapsed ms: `{summary['mean_elapsed_ms']}`",
        f"- Chart count: `{len(summary['chart_paths'])}`",
        "",
        "## Sweep Summary",
        "",
        "| Sweep | Points | Classes | A_TSEK range | Diagnostic avg range | Transitions |",
        "|---|---:|---|---|---|---|",
    ]
    for sweep, data in summary["sweeps"].items():
        classes = ", ".join(f"{k}:{v}" for k, v in sorted(data["classes"].items()))
        transitions = "; ".join(f"{t['from_class']}->{t['to_class']} @ {t['from_x']}..{t['to_x']}" for t in data["transitions"]) or "none"
        lines.append(
            f"| `{sweep}` | {data['points']} | {classes} | {data['min_A_TSEK']}..{data['max_A_TSEK']} | {data['min_diagnostic_average']}..{data['max_diagnostic_average']} | {transitions} |"
        )

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, REPORT_DIR).replace("\\", "/")
        lines.extend([f"![{Path(chart).stem}]({rel})", ""])

    lines += [
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main() -> None:
    runtime = TauScalingRuntime(REPO_ROOT)
    scenarios = make_sweeps()
    write_seed_manifest(scenarios)
    results = [run_seed(runtime, s["seed"], s["sweep"], s["x_name"], s["x_value"]) for s in scenarios]
    charts = generate_charts(results)
    summary = summarize(results, charts)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(REPORT_DIR / "sensitivity_sweep_v0_4_1.json", summary)
    write_json(REPORT_DIR / "latest_sensitivity_sweep.json", summary)
    md = render_markdown(summary)
    write_text(REPORT_DIR / "sensitivity_sweep_v0_4_1.md", md)
    write_text(REPORT_DIR / "latest_sensitivity_sweep.md", md)
    print(json.dumps({
        "schema": summary["schema"],
        "total_points": summary["total_points"],
        "chart_count": len(summary["chart_paths"]),
        "sweeps": {k: {"points": v["points"], "classes": v["classes"], "transitions": v["transitions"]} for k, v in summary["sweeps"].items()},
        "report": "reports/sensitivity/latest_sensitivity_sweep.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
