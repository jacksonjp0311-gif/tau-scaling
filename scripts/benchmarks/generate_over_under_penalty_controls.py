
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "penalty_controls"
VIS = ROOT / "visuals" / "penalty_controls" / "v0_7_6"

BOUNDARY_CARDS = ROOT / "reports" / "tsek_boundary_cards" / "latest_tsek_boundary_explanation_cards.json"
THRESHOLD_REVIEW = ROOT / "reports" / "tsek_threshold_review" / "latest_tsek_threshold_boundary_review.json"
GATE_ALGEBRA = ROOT / "reports" / "gate_algebra" / "latest_gate_algebra_map.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

CONTROL_CLASSES = [
    {
        "control_id": "over_penalty_high_support_claim",
        "risk_type": "over_penalty",
        "target_class_boundary": "TSEK-C/TSEK-E",
        "purpose": "Detect cases where high-support local evidence is pushed too harshly into rejection.",
        "expected_behavior": "retain_or_explain_controlled_downgrade",
    },
    {
        "control_id": "under_penalty_sparse_evidence_claim",
        "risk_type": "under_penalty",
        "target_class_boundary": "TSEK-B/TSEK-C",
        "purpose": "Detect cases where sparse evidence is promoted too strongly.",
        "expected_behavior": "downgrade_or_block_promotion",
    },
    {
        "control_id": "missing_intermediate_tsek_d_path",
        "risk_type": "boundary_gap",
        "target_class_boundary": "TSEK-C/TSEK-D/TSEK-E",
        "purpose": "Detect whether the intermediate weak class is absent because of design or insufficient scenario coverage.",
        "expected_behavior": "explain_absence_or_add_future_scenario",
    },
    {
        "control_id": "reserved_tsek_a_overclaim_guard",
        "risk_type": "overclaim",
        "target_class_boundary": "TSEK-A/TSEK-B",
        "purpose": "Prevent local runtime evidence from being misread as externally validated strong proof.",
        "expected_behavior": "keep_tsek_a_reserved_without_external_evidence",
    },
    {
        "control_id": "gate_gap_penalty_alignment",
        "risk_type": "gate_mapping",
        "target_class_boundary": "gate_family_to_tsek_score",
        "purpose": "Check whether known gate visibility gaps are treated as explanation targets rather than direct penalty changes.",
        "expected_behavior": "report_only_no_threshold_change",
    },
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

def build_controls(cards, threshold, gate):
    attention = cards.get("attention_card_count", 0)
    gate_gaps = gate.get("gap_count", 0)
    threshold_gaps = threshold.get("gap_count", 0)
    controls = []
    for item in CONTROL_CLASSES:
        pressure_score = 0
        if item["risk_type"] in {"over_penalty", "under_penalty", "boundary_gap", "overclaim"}:
            pressure_score += int(attention)
        if item["risk_type"] in {"gate_mapping", "over_penalty"}:
            pressure_score += int(gate_gaps)
        if item["risk_type"] in {"boundary_gap", "under_penalty"}:
            pressure_score += int(threshold_gaps)

        controls.append({
            "schema": "tau-scaling-over-under-penalty-control-v0.7.6",
            **item,
            "pressure_score": pressure_score,
            "control_status": "REPORT_ONLY_CONTROL_DEFINED",
            "threshold_change_allowed": False,
            "classifier_change_allowed": False,
            "mutation_allowed": False,
            "control_result": "pending_future_dry_run",
            "evidence_boundary": "Control is based on local reports and explanation cards only; it is not product, silicon, manufacturing, or universal Tau validation.",
        })
    return controls

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

    controls = summary["controls"]
    plt.figure(figsize=(11, 4))
    plt.bar([c["control_id"] for c in controls], [c["pressure_score"] for c in controls])
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Pressure score")
    plt.title("Over/Under-Penalty Control Pressure")
    save("penalty_control_pressure_scores.png")

    types = {}
    for c in controls:
        types[c["risk_type"]] = types.get(c["risk_type"], 0) + 1
    plt.figure(figsize=(8, 4))
    plt.bar(list(types.keys()), list(types.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Control count")
    plt.title("Penalty Control Risk Types")
    save("penalty_control_risk_types.png")

    health = {
        "release_passed": int(summary["release_passed"]),
        "cards_ready": int(summary["cards_ready"]),
        "controls_defined": summary["control_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("Penalty Controls Health")
    save("penalty_controls_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.6 Over/Under-Penalty Negative Controls",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Control Result",
        "",
        f"- Control status: `{summary['control_status']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Boundary cards ready: `{summary['cards_ready']}`",
        f"- Control count: `{summary['control_count']}`",
        f"- Thresholds changed: `{summary['thresholds_changed']}`",
        f"- Classifier changed: `{summary['classifier_changed']}`",
        "",
        "## Controls",
        "",
        "| Control | Risk | Boundary | Pressure | Expected behavior |",
        "|---|---|---|---:|---|",
    ]
    for c in summary["controls"]:
        lines.append(f"| `{c['control_id']}` | `{c['risk_type']}` | `{c['target_class_boundary']}` | {c['pressure_score']} | `{c['expected_behavior']}` |")

    lines += [
        "",
        "## Interpretation",
        "",
        "These controls define what must be tested before any threshold dry-run or classifier-policy change. They do not run a threshold change and do not alter classifier behavior.",
        "",
        "## Next Tau Work",
        "",
        "1. Convert these controls into report-only synthetic scenarios.",
        "2. Compare current TSEK output against expected over/under-penalty behavior.",
        "3. Separate true rejection from over-penalty collapse.",
        "4. Preserve threshold and classifier mutation locks until dry-run evidence exists.",
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
    cards = read_json(BOUNDARY_CARDS)
    threshold = read_json(THRESHOLD_REVIEW)
    gate = read_json(GATE_ALGEBRA)
    release = read_json(RELEASE)

    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    cards_ready = cards.get("card_status") == "TSEK_BOUNDARY_CARDS_READY__NO_THRESHOLD_CHANGE"
    controls = build_controls(cards, threshold, gate)

    for control in controls:
        wjson(OUT / "controls" / f"{control['control_id']}_v0_7_6.json", control)

    status = "PENALTY_CONTROLS_DEFINED__REPORT_ONLY_NO_MUTATION" if release_passed and cards_ready else "PENALTY_CONTROLS_NEED_REVIEW"

    summary = {
        "schema": "tau-scaling-over-under-penalty-negative-controls-v0.7.6",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "control_status": status,
        "release_passed": bool(release_passed),
        "cards_ready": bool(cards_ready),
        "control_count": len(controls),
        "controls": controls,
        "attention_card_count": cards.get("attention_card_count", 0),
        "threshold_gap_count": threshold.get("gap_count", 0),
        "gate_gap_count": gate.get("gap_count", 0),
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
        "next_recommendation": "Move to v0.7.7 Threshold Sensitivity Dry-Run using these report-only controls.",
        "boundary": "Over/under-penalty negative controls are local classifier-governance analysis artifacts. They define test controls before threshold dry-runs. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "over_under_penalty_negative_controls_v0_7_6.json", summary)
    wjson(OUT / "latest_over_under_penalty_negative_controls.json", summary)
    wtext(OUT / "over_under_penalty_negative_controls_v0_7_6.md", make_md(summary))
    wtext(OUT / "latest_over_under_penalty_negative_controls.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "control_status": summary["control_status"],
        "release_passed": summary["release_passed"],
        "cards_ready": summary["cards_ready"],
        "control_count": summary["control_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/penalty_controls/latest_over_under_penalty_negative_controls.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
