
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "threshold_governance_summary"
VIS = ROOT / "visuals" / "threshold_governance_summary" / "v0_7_9"

INPUTS = {
    "tau_mechanics": ROOT / "reports" / "tau_mechanics_review" / "latest_tau_mechanics_return_review.json",
    "tau_vector": ROOT / "reports" / "tau_vector_semantics" / "latest_tau_vector_semantics_ledger.json",
    "gate_algebra": ROOT / "reports" / "gate_algebra" / "latest_gate_algebra_map.json",
    "threshold_review": ROOT / "reports" / "tsek_threshold_review" / "latest_tsek_threshold_boundary_review.json",
    "boundary_cards": ROOT / "reports" / "tsek_boundary_cards" / "latest_tsek_boundary_explanation_cards.json",
    "penalty_controls": ROOT / "reports" / "penalty_controls" / "latest_over_under_penalty_negative_controls.json",
    "sensitivity": ROOT / "reports" / "threshold_sensitivity_dry_run" / "latest_threshold_sensitivity_dry_run.json",
    "decision": ROOT / "reports" / "threshold_decision_record" / "latest_threshold_decision_record.json",
    "release": ROOT / "reports" / "release" / "latest_release_readiness.json",
}

CHAIN = [
    ("v0.7.1", "tau_mechanics", "mechanics_status"),
    ("v0.7.2", "tau_vector", "semantics_status"),
    ("v0.7.3", "gate_algebra", "gate_algebra_status"),
    ("v0.7.4", "threshold_review", "threshold_review_status"),
    ("v0.7.5", "boundary_cards", "card_status"),
    ("v0.7.6", "penalty_controls", "control_status"),
    ("v0.7.7", "sensitivity", "dry_run_status"),
    ("v0.7.8", "decision", "decision_status"),
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

def build_chain(data):
    rows = []
    for version, key, status_key in CHAIN:
        d = data[key]
        rows.append({
            "version": version,
            "artifact": key,
            "status": d.get(status_key, "MISSING" if d.get("missing") else "RECORDED"),
            "missing": bool(d.get("missing")),
            "thresholds_changed": bool(d.get("thresholds_changed", False)),
            "classifier_changed": bool(d.get("classifier_changed", False)),
            "mutation_allowed": bool(d.get("mutation_allowed", False)),
            "application_allowed": bool(d.get("application_allowed", False)),
            "calibration_applied": bool(d.get("calibration_applied", False)),
            "replay_allowed": bool(d.get("replay_allowed", False)),
            "gap_count": int(d.get("gap_count", 0) or 0),
        })
    return rows

def summarize_decision(data):
    decision = data["decision"]
    sensitivity = data["sensitivity"]
    return {
        "threshold_decision": decision.get("threshold_decision", "UNKNOWN"),
        "decision_status": decision.get("decision_status", "UNKNOWN"),
        "decision_rationale": decision.get("decision_rationale", ""),
        "scenario_count": int(sensitivity.get("scenario_count", 0) or 0),
        "high_attention_count": int(sensitivity.get("high_attention_count", 0) or 0),
        "moderate_attention_count": int(sensitivity.get("moderate_attention_count", 0) or 0),
        "low_attention_count": int(sensitivity.get("low_attention_count", 0) or 0),
    }

def classify(data, rows):
    release = data["release"]
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0

    violations = []
    for row in rows:
        for key in ["thresholds_changed", "classifier_changed", "mutation_allowed", "application_allowed", "calibration_applied", "replay_allowed"]:
            if row.get(key) is True:
                violations.append({"artifact": row["artifact"], "violation": key})

    missing = [row["artifact"] for row in rows if row["missing"]]
    decision = data["decision"].get("threshold_decision")
    locked = release_passed and not violations and not missing and decision == "DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE"

    status = "THRESHOLD_GOVERNANCE_SUMMARY_LOCKED__DEFER_CHANGE_NO_MUTATION" if locked else "THRESHOLD_GOVERNANCE_SUMMARY_NEEDS_REVIEW"
    return status, locked, release_passed, violations, missing

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

    rows = summary["chain_rows"]
    plt.figure(figsize=(10, 4))
    plt.bar([r["version"] for r in rows], [0 if r["missing"] else 1 for r in rows])
    plt.ylabel("Present")
    plt.title("Threshold Governance Chain Coverage")
    save("threshold_governance_chain_coverage.png")

    plt.figure(figsize=(10, 4))
    plt.bar([r["version"] for r in rows], [r["gap_count"] for r in rows])
    plt.ylabel("Gap count")
    plt.title("Threshold Governance Gap Counts")
    save("threshold_governance_gap_counts.png")

    locks = {
        "summary_locked": int(summary["summary_locked"]),
        "release_passed": int(summary["release_passed"]),
        "violations": summary["violation_count"],
        "missing": summary["missing_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(locks.keys()), list(locks.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Value")
    plt.title("Threshold Governance Summary Health")
    save("threshold_governance_summary_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.9 Threshold Governance Summary",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Summary Result",
        "",
        f"- Summary status: `{summary['summary_status']}`",
        f"- Summary locked: `{summary['summary_locked']}`",
        f"- Threshold decision: `{summary['threshold_decision']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Violation count: `{summary['violation_count']}`",
        f"- Missing count: `{summary['missing_count']}`",
        "",
        "## Threshold Decision",
        "",
        f"- Decision status: `{summary['decision_status']}`",
        f"- Rationale: {summary['decision_rationale']}",
        f"- Scenario count: `{summary['scenario_count']}`",
        f"- High attention count: `{summary['high_attention_count']}`",
        "",
        "## v0.7.x Chain",
        "",
        "| Version | Artifact | Status | Gaps | Threshold changed | Classifier changed | Mutation |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in summary["chain_rows"]:
        lines.append(f"| `{row['version']}` | `{row['artifact']}` | `{row['status']}` | {row['gap_count']} | `{row['thresholds_changed']}` | `{row['classifier_changed']}` | `{row['mutation_allowed']}` |")

    lines += [
        "",
        "## Governance Conclusion",
        "",
        "The current threshold decision is **defer threshold change pending more evidence**. This is the correct outcome because report-only sensitivity found high-attention pressure while preserving all mutation and threshold locks.",
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
        "## Next Tau Work",
        "",
        "1. Freeze current thresholds unless human review requests a candidate branch.",
        "2. Add more scenario evidence for high-attention pressure surfaces.",
        "3. Preserve current classifier until stronger evidence exists.",
        "4. Consider v0.8.0 as a stable Tau threshold governance milestone.",
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
    data = {k: read_json(v) for k, v in INPUTS.items()}
    rows = build_chain(data)
    summary_status, locked, release_passed, violations, missing = classify(data, rows)
    decision = summarize_decision(data)

    summary = {
        "schema": "tau-scaling-threshold-governance-summary-v0.7.9",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary_status": summary_status,
        "summary_locked": bool(locked),
        "release_passed": bool(release_passed),
        **decision,
        "chain_rows": rows,
        "violation_count": len(violations),
        "violations": violations,
        "missing_count": len(missing),
        "missing_artifacts": missing,
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
        "next_recommendation": "Move to v0.8.0 Stable Tau Threshold Governance Milestone or add more scenario evidence before any candidate branch.",
        "boundary": "Threshold governance summaries are local classifier-governance milestone artifacts. They summarize threshold review, controls, dry-runs, and decisions. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "threshold_governance_summary_v0_7_9.json", summary)
    wjson(OUT / "latest_threshold_governance_summary.json", summary)
    wtext(OUT / "threshold_governance_summary_v0_7_9.md", make_md(summary))
    wtext(OUT / "latest_threshold_governance_summary.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "summary_status": summary["summary_status"],
        "summary_locked": summary["summary_locked"],
        "threshold_decision": summary["threshold_decision"],
        "scenario_count": summary["scenario_count"],
        "high_attention_count": summary["high_attention_count"],
        "violation_count": summary["violation_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/threshold_governance_summary/latest_threshold_governance_summary.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
