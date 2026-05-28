
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "stable_tau_threshold_governance"
VIS = ROOT / "visuals" / "stable_tau_threshold_governance" / "v0_8_0"

INPUTS = {
    "approval_corridor": ROOT / "reports" / "approval_corridor" / "latest_approval_governance_corridor_milestone.json",
    "tau_mechanics": ROOT / "reports" / "tau_mechanics_review" / "latest_tau_mechanics_return_review.json",
    "tau_vector": ROOT / "reports" / "tau_vector_semantics" / "latest_tau_vector_semantics_ledger.json",
    "gate_algebra": ROOT / "reports" / "gate_algebra" / "latest_gate_algebra_map.json",
    "threshold_review": ROOT / "reports" / "tsek_threshold_review" / "latest_tsek_threshold_boundary_review.json",
    "boundary_cards": ROOT / "reports" / "tsek_boundary_cards" / "latest_tsek_boundary_explanation_cards.json",
    "penalty_controls": ROOT / "reports" / "penalty_controls" / "latest_over_under_penalty_negative_controls.json",
    "threshold_sensitivity": ROOT / "reports" / "threshold_sensitivity_dry_run" / "latest_threshold_sensitivity_dry_run.json",
    "threshold_decision": ROOT / "reports" / "threshold_decision_record" / "latest_threshold_decision_record.json",
    "threshold_governance": ROOT / "reports" / "threshold_governance_summary" / "latest_threshold_governance_summary.json",
    "release": ROOT / "reports" / "release" / "latest_release_readiness.json",
}

CHAIN = [
    ("v0.7.0", "approval_corridor", "corridor_status"),
    ("v0.7.1", "tau_mechanics", "mechanics_status"),
    ("v0.7.2", "tau_vector", "semantics_status"),
    ("v0.7.3", "gate_algebra", "gate_algebra_status"),
    ("v0.7.4", "threshold_review", "threshold_review_status"),
    ("v0.7.5", "boundary_cards", "card_status"),
    ("v0.7.6", "penalty_controls", "control_status"),
    ("v0.7.7", "threshold_sensitivity", "dry_run_status"),
    ("v0.7.8", "threshold_decision", "decision_status"),
    ("v0.7.9", "threshold_governance", "summary_status"),
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

def rows(data):
    out = []
    for version, key, status_key in CHAIN:
        d = data[key]
        out.append({
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
            "branch_created": bool(d.get("branch_created", False)),
            "gap_count": int(d.get("gap_count", 0) or 0),
        })
    return out

def classify(data, chain_rows):
    release = data["release"]
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0
    gov = data["threshold_governance"]
    decision = data["threshold_decision"]

    violations = []
    for row in chain_rows:
        for key in ["thresholds_changed", "classifier_changed", "mutation_allowed", "application_allowed", "calibration_applied", "replay_allowed", "branch_created"]:
            if row[key] is True:
                violations.append({"artifact": row["artifact"], "violation": key})

    missing = [row["artifact"] for row in chain_rows if row["missing"]]
    correct_decision = decision.get("threshold_decision") == "DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE"
    gov_locked = gov.get("summary_locked") is True
    milestone_locked = release_passed and not violations and not missing and correct_decision and gov_locked

    status = "STABLE_TAU_THRESHOLD_GOVERNANCE_MILESTONE_LOCKED__NO_MUTATION" if milestone_locked else "STABLE_TAU_THRESHOLD_GOVERNANCE_MILESTONE_NEEDS_REVIEW"
    return status, milestone_locked, release_passed, correct_decision, gov_locked, violations, missing

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

    rows = summary["milestone_chain"]
    plt.figure(figsize=(11, 4))
    plt.bar([r["version"] for r in rows], [0 if r["missing"] else 1 for r in rows])
    plt.ylabel("Present")
    plt.title("v0.8.0 Milestone Chain Coverage")
    save("stable_tau_threshold_chain_coverage.png")

    plt.figure(figsize=(11, 4))
    plt.bar([r["version"] for r in rows], [r["gap_count"] for r in rows])
    plt.ylabel("Gap count")
    plt.title("v0.8.0 Milestone Gap Compression")
    save("stable_tau_threshold_gap_compression.png")

    health = {
        "milestone_locked": int(summary["milestone_locked"]),
        "release_passed": int(summary["release_passed"]),
        "decision_deferred": int(summary["threshold_decision_deferred"]),
        "violations": summary["violation_count"],
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Value")
    plt.title("v0.8.0 Stable Milestone Health")
    save("stable_tau_threshold_milestone_health.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.8.0 Stable Tau Threshold Governance Milestone",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Milestone Result",
        "",
        f"- Milestone status: `{summary['milestone_status']}`",
        f"- Milestone locked: `{summary['milestone_locked']}`",
        f"- Threshold decision: `{summary['threshold_decision']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Threshold governance locked: `{summary['threshold_governance_locked']}`",
        f"- Violation count: `{summary['violation_count']}`",
        f"- Missing count: `{summary['missing_count']}`",
        "",
        "## Milestone Chain",
        "",
        "| Version | Artifact | Status | Gaps | Threshold changed | Classifier changed | Mutation |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in summary["milestone_chain"]:
        lines.append(f"| `{row['version']}` | `{row['artifact']}` | `{row['status']}` | {row['gap_count']} | `{row['thresholds_changed']}` | `{row['classifier_changed']}` | `{row['mutation_allowed']}` |")

    lines += [
        "",
        "## Stable Decision",
        "",
        "The stable v0.8.0 decision is to **defer threshold change pending more evidence**. The system found real pressure surfaces, but not enough evidence to tune thresholds or mutate classifier behavior.",
        "",
        "## Explicit Locks",
        "",
        "```text",
        f"thresholds_changed: {str(summary['thresholds_changed']).lower()}",
        f"classifier_changed: {str(summary['classifier_changed']).lower()}",
        f"mutation_allowed: {str(summary['mutation_allowed']).lower()}",
        f"application_allowed: {str(summary['application_allowed']).lower()}",
        f"calibration_applied: {str(summary['calibration_applied']).lower()}",
        f"candidate_branch_created: {str(summary['candidate_branch_created']).lower()}",
        "```",
        "",
        "## What This Milestone Means",
        "",
        "v0.8.0 closes the first Tau mechanics return arc: approval containment, tau semantics, gate algebra, threshold review, boundary cards, penalty controls, dry-run, decision record, and governance summary.",
        "",
        "## Next Work",
        "",
        "1. Add more scenario evidence for the two high-attention threshold pressures.",
        "2. Keep thresholds frozen unless human review explicitly requests a candidate branch.",
        "3. Keep classifier mutation disabled.",
        "4. Use v0.8.x for evidence expansion, not threshold tuning.",
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
    chain_rows = rows(data)
    status, locked, release_passed, decision_deferred, gov_locked, violations, missing = classify(data, chain_rows)
    decision = data["threshold_decision"].get("threshold_decision", "UNKNOWN")

    summary = {
        "schema": "tau-scaling-stable-tau-threshold-governance-milestone-v0.8.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "milestone_status": status,
        "milestone_locked": bool(locked),
        "release_passed": bool(release_passed),
        "threshold_decision": decision,
        "threshold_decision_deferred": bool(decision_deferred),
        "threshold_governance_locked": bool(gov_locked),
        "milestone_chain": chain_rows,
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
        "next_recommendation": "Use v0.8.x for scenario evidence expansion. Do not tune thresholds or mutate classifier behavior without explicit human review and a candidate branch gate.",
        "boundary": "Stable Tau threshold governance milestones are local classifier-governance milestone artifacts. They package evidence, dry-runs, and decisions into a stable release surface. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "stable_tau_threshold_governance_milestone_v0_8_0.json", summary)
    wjson(OUT / "latest_stable_tau_threshold_governance_milestone.json", summary)
    wtext(OUT / "stable_tau_threshold_governance_milestone_v0_8_0.md", make_md(summary))
    wtext(OUT / "latest_stable_tau_threshold_governance_milestone.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "milestone_status": summary["milestone_status"],
        "milestone_locked": summary["milestone_locked"],
        "threshold_decision": summary["threshold_decision"],
        "threshold_decision_deferred": summary["threshold_decision_deferred"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
