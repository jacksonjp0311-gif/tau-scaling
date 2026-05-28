
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "threshold_decision_record"
VIS = ROOT / "visuals" / "threshold_decision_record" / "v0_7_8"

DRY_RUN = ROOT / "reports" / "threshold_sensitivity_dry_run" / "latest_threshold_sensitivity_dry_run.json"
PENALTY = ROOT / "reports" / "penalty_controls" / "latest_over_under_penalty_negative_controls.json"
BOUNDARY = ROOT / "reports" / "tsek_boundary_cards" / "latest_tsek_boundary_explanation_cards.json"
RELEASE = ROOT / "reports" / "release" / "latest_release_readiness.json"

DECISION_OPTIONS = [
    "REJECT_THRESHOLD_CHANGE",
    "DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE",
    "REVIEW_READY_REPORT_ONLY",
    "CANDIDATE_BRANCH_REQUIRED_BEFORE_ANY_MUTATION",
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

def decide(dry, penalty, boundary, release):
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    dry_ready = dry.get("dry_run_status") == "THRESHOLD_SENSITIVITY_DRY_RUN_READY__REPORT_ONLY_NO_MUTATION"
    controls_ready = penalty.get("control_status") == "PENALTY_CONTROLS_DEFINED__REPORT_ONLY_NO_MUTATION"
    cards_ready = boundary.get("card_status") == "TSEK_BOUNDARY_CARDS_READY__NO_THRESHOLD_CHANGE"

    high = int(dry.get("high_attention_count", 0))
    moderate = int(dry.get("moderate_attention_count", 0))
    low = int(dry.get("low_attention_count", 0))
    scenario_count = int(dry.get("scenario_count", 0))

    if not release_passed or not dry_ready or not controls_ready or not cards_ready:
        decision = "DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE"
        rationale = "One or more prerequisite report-only layers is not in the expected ready state."
    elif high > 0:
        decision = "DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE"
        rationale = "High-attention threshold pressure exists; threshold tuning is not justified without additional evidence and review."
    elif scenario_count == 0:
        decision = "REJECT_THRESHOLD_CHANGE"
        rationale = "No scenarios exist to justify threshold change."
    else:
        decision = "REVIEW_READY_REPORT_ONLY"
        rationale = "Report-only sensitivity exists, but no classifier mutation is authorized."

    return {
        "release_passed": bool(release_passed),
        "dry_run_ready": bool(dry_ready),
        "controls_ready": bool(controls_ready),
        "boundary_cards_ready": bool(cards_ready),
        "high_attention_count": high,
        "moderate_attention_count": moderate,
        "low_attention_count": low,
        "scenario_count": scenario_count,
        "decision": decision,
        "rationale": rationale,
    }

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

    decision = {summary["threshold_decision"]: 1}
    plt.figure(figsize=(10, 4))
    plt.bar(list(decision.keys()), list(decision.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Selected")
    plt.title("Threshold Decision Record")
    save("threshold_decision_selected.png")

    attention = {
        "high": summary["high_attention_count"],
        "moderate": summary["moderate_attention_count"],
        "low": summary["low_attention_count"],
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(attention.keys()), list(attention.values()))
    plt.ylabel("Scenario count")
    plt.title("Threshold Decision Attention Counts")
    save("threshold_decision_attention_counts.png")

    locks = {
        "thresholds_changed": int(summary["thresholds_changed"]),
        "classifier_changed": int(summary["classifier_changed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
        "review_ready": int(summary["threshold_decision"] == "REVIEW_READY_REPORT_ONLY"),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(locks.keys()), list(locks.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("Threshold Decision Locks")
    save("threshold_decision_locks.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.8 Threshold Decision Record",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Decision Result",
        "",
        f"- Decision status: `{summary['decision_status']}`",
        f"- Threshold decision: `{summary['threshold_decision']}`",
        f"- Rationale: {summary['decision_rationale']}",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Dry-run ready: `{summary['dry_run_ready']}`",
        f"- Controls ready: `{summary['controls_ready']}`",
        f"- Boundary cards ready: `{summary['boundary_cards_ready']}`",
        "",
        "## Attention Counts",
        "",
        f"- High attention: `{summary['high_attention_count']}`",
        f"- Moderate attention: `{summary['moderate_attention_count']}`",
        f"- Low attention: `{summary['low_attention_count']}`",
        f"- Scenario count: `{summary['scenario_count']}`",
        "",
        "## Explicit Locks",
        "",
        "```text",
        f"thresholds_changed: {str(summary['thresholds_changed']).lower()}",
        f"classifier_changed: {str(summary['classifier_changed']).lower()}",
        f"mutation_allowed: {str(summary['mutation_allowed']).lower()}",
        f"application_allowed: {str(summary['application_allowed']).lower()}",
        f"calibration_applied: {str(summary['calibration_applied']).lower()}",
        "```",
        "",
        "## Interpretation",
        "",
        "This decision record converts the report-only sensitivity dry-run into a governance decision. It does not tune thresholds, alter classifier scoring, or authorize mutation.",
        "",
        "## Next Tau Work",
        "",
        "1. If decision is report-only review-ready, prepare a human-readable summary of the pressure surfaces.",
        "2. If decision is deferred, gather additional scenario evidence before any candidate branch.",
        "3. If decision is rejected, freeze current thresholds and document why.",
        "4. Preserve no-threshold-change and no-classifier-mutation locks.",
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
    dry = read_json(DRY_RUN)
    penalty = read_json(PENALTY)
    boundary = read_json(BOUNDARY)
    release = read_json(RELEASE)

    decision = decide(dry, penalty, boundary, release)

    status = "THRESHOLD_DECISION_RECORDED__NO_MUTATION"
    summary = {
        "schema": "tau-scaling-threshold-decision-record-v0.7.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "decision_status": status,
        "threshold_decision": decision["decision"],
        "decision_rationale": decision["rationale"],
        **{k: v for k, v in decision.items() if k not in {"decision", "rationale"}},
        "decision_options": DECISION_OPTIONS,
        "input_threshold_sensitivity_dry_run": rel(DRY_RUN),
        "input_penalty_controls": rel(PENALTY),
        "input_boundary_cards": rel(BOUNDARY),
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
        "candidate_branch_created": False,
        "next_recommendation": "Move to v0.7.9 Threshold Governance Summary or freeze v0.7.x as a Tau threshold analysis milestone.",
        "boundary": "Threshold decision records are local classifier-governance decision artifacts. They convert report-only dry-run evidence into a non-mutating decision. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "threshold_decision_record_v0_7_8.json", summary)
    wjson(OUT / "latest_threshold_decision_record.json", summary)
    wtext(OUT / "threshold_decision_record_v0_7_8.md", make_md(summary))
    wtext(OUT / "latest_threshold_decision_record.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "decision_status": summary["decision_status"],
        "threshold_decision": summary["threshold_decision"],
        "release_passed": summary["release_passed"],
        "dry_run_ready": summary["dry_run_ready"],
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
        "report": "reports/threshold_decision_record/latest_threshold_decision_record.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
