
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "threshold_sensitivity_dry_run"
VIS = ROOT / "visuals" / "threshold_sensitivity_dry_run" / "v0_7_7"

PENALTY = ROOT / "reports" / "penalty_controls" / "latest_over_under_penalty_negative_controls.json"
BOUNDARY = ROOT / "reports" / "tsek_boundary_cards" / "latest_tsek_boundary_explanation_cards.json"
THRESHOLD = ROOT / "reports" / "tsek_threshold_review" / "latest_tsek_threshold_boundary_review.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

SIMULATED_ADJUSTMENTS = [
    {"scenario": "tighten_promotion_boundary_report_only", "direction": "promotion_harder", "target": "TSEK-B/TSEK-C", "risk_checked": "under_penalty_sparse_evidence_claim"},
    {"scenario": "soften_rejection_boundary_report_only", "direction": "rejection_harder_to_trigger", "target": "TSEK-C/TSEK-E", "risk_checked": "over_penalty_high_support_claim"},
    {"scenario": "expose_tsek_d_intermediate_report_only", "direction": "intermediate_visibility", "target": "TSEK-C/TSEK-D/TSEK-E", "risk_checked": "missing_intermediate_tsek_d_path"},
    {"scenario": "reserve_tsek_a_report_only", "direction": "strong_class_guard", "target": "TSEK-A/TSEK-B", "risk_checked": "reserved_tsek_a_overclaim_guard"},
    {"scenario": "gate_gap_neutrality_report_only", "direction": "no_direct_penalty", "target": "gate_family_to_tsek_score", "risk_checked": "gate_gap_penalty_alignment"},
]

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

def rel(path: Path):
    return str(path.relative_to(ROOT)).replace("\\", "/")

def build_scenarios(penalty):
    controls = {c["control_id"]: c for c in penalty.get("controls", [])}
    rows = []
    for item in SIMULATED_ADJUSTMENTS:
        control = controls.get(item["risk_checked"], {})
        pressure = int(control.get("pressure_score", 0))
        if pressure >= 8:
            sensitivity = "high_attention"
        elif pressure >= 4:
            sensitivity = "moderate_attention"
        else:
            sensitivity = "low_attention"

        rows.append({
            "schema": "tau-scaling-threshold-sensitivity-dry-run-scenario-v0.7.7",
            **item,
            "control_pressure_score": pressure,
            "sensitivity_class": sensitivity,
            "simulated_only": True,
            "current_classifier_output_changed": False,
            "threshold_change_allowed": False,
            "classifier_change_allowed": False,
            "mutation_allowed": False,
            "dry_run_result": "REPORT_ONLY_REVIEW_REQUIRED",
            "interpretation": "Scenario defines pressure to inspect later; it does not change thresholds or classifier behavior.",
        })
    return rows

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

    rows = summary["dry_run_scenarios"]
    plt.figure(figsize=(11, 4))
    plt.bar([r["scenario"] for r in rows], [r["control_pressure_score"] for r in rows])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Pressure score")
    plt.title("Threshold Sensitivity Dry-Run Pressure")
    save("threshold_sensitivity_pressure_scores.png")

    counts = {}
    for r in rows:
        counts[r["sensitivity_class"]] = counts.get(r["sensitivity_class"], 0) + 1
    plt.figure(figsize=(8, 4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.ylabel("Scenario count")
    plt.title("Threshold Sensitivity Classes")
    save("threshold_sensitivity_classes.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "controls_ready": int(summary["controls_ready"]),
        "scenarios": summary["scenario_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("Threshold Sensitivity Dry-Run Health")
    save("threshold_sensitivity_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.7 Threshold Sensitivity Dry-Run",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Dry-Run Result",
        "",
        f"- Dry-run status: `{summary['dry_run_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Controls ready: `{summary['controls_ready']}`",
        f"- Scenario count: `{summary['scenario_count']}`",
        f"- Thresholds changed: `{summary['thresholds_changed']}`",
        f"- Classifier changed: `{summary['classifier_changed']}`",
        "",
        "## Report-Only Scenarios",
        "",
        "| Scenario | Direction | Target | Pressure | Sensitivity |",
        "|---|---|---|---:|---|",
    ]
    for r in summary["dry_run_scenarios"]:
        lines.append(f"| `{r['scenario']}` | `{r['direction']}` | `{r['target']}` | {r['control_pressure_score']} | `{r['sensitivity_class']}` |")

    lines += [
        "",
        "## Interpretation",
        "",
        "This dry-run only models where threshold sensitivity should be inspected. It does not change thresholds, class logic, or runtime classifier behavior.",
        "",
        "## Next Tau Work",
        "",
        "1. Convert high-attention sensitivity scenarios into a decision record.",
        "2. Decide whether any scenario deserves a future candidate branch proposal.",
        "3. Keep all changes report-only until explicit human review.",
        "4. Preserve local-runtime evidence boundary.",
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
    penalty = read_json(PENALTY)
    boundary = read_json(BOUNDARY)
    threshold = read_json(THRESHOLD)
    release = read_json(RELEASE)

    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    controls_ready = penalty.get("control_status") == "PENALTY_CONTROLS_DEFINED__REPORT_ONLY_NO_MUTATION"
    boundary_ready = boundary.get("card_status") == "TSEK_BOUNDARY_CARDS_READY__NO_THRESHOLD_CHANGE"
    threshold_ready = threshold.get("threshold_review_status") == "TSEK_THRESHOLD_BOUNDARY_REVIEW_READY__NO_THRESHOLD_CHANGE"

    scenarios = build_scenarios(penalty)
    for row in scenarios:
        wjson(OUT / "scenarios" / f"{row['scenario']}_v0_7_7.json", row)

    status = "THRESHOLD_SENSITIVITY_DRY_RUN_READY__REPORT_ONLY_NO_MUTATION" if release_passed and controls_ready and boundary_ready and threshold_ready else "THRESHOLD_SENSITIVITY_DRY_RUN_NEEDS_REVIEW"

    summary = {
        "schema": "tau-scaling-threshold-sensitivity-dry-run-v0.7.7",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run_status": status,
        "release_passed": bool(release_passed),
        "controls_ready": bool(controls_ready),
        "boundary_cards_ready": bool(boundary_ready),
        "threshold_review_ready": bool(threshold_ready),
        "scenario_count": len(scenarios),
        "dry_run_scenarios": scenarios,
        "high_attention_count": sum(1 for s in scenarios if s["sensitivity_class"] == "high_attention"),
        "moderate_attention_count": sum(1 for s in scenarios if s["sensitivity_class"] == "moderate_attention"),
        "low_attention_count": sum(1 for s in scenarios if s["sensitivity_class"] == "low_attention"),
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
        "next_recommendation": "Move to v0.7.8 Threshold Decision Record if the dry-run surfaces review-worthy pressure.",
        "boundary": "Threshold sensitivity dry-runs are local classifier-governance analysis artifacts. They model sensitivity pressure using report-only controls. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "threshold_sensitivity_dry_run_v0_7_7.json", summary)
    wjson(OUT / "latest_threshold_sensitivity_dry_run.json", summary)
    wtext(OUT / "threshold_sensitivity_dry_run_v0_7_7.md", make_md(summary))
    wtext(OUT / "latest_threshold_sensitivity_dry_run.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "dry_run_status": summary["dry_run_status"],
        "release_passed": summary["release_passed"],
        "controls_ready": summary["controls_ready"],
        "scenario_count": summary["scenario_count"],
        "high_attention_count": summary["high_attention_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
