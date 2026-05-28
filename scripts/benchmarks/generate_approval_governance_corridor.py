
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "approval_corridor"
VIS = ROOT / "visuals" / "approval_corridor" / "v0_7_0"

INPUTS = {
    "candidate_branch": ROOT / "reports" / "candidate_branch" / "latest_candidate_branch_gate.json",
    "candidate_replay": ROOT / "reports" / "candidate_replay" / "latest_candidate_branch_replay_harness.json",
    "human_approval_template": ROOT / "reports" / "human_approval" / "latest_human_approval_template_report.json",
    "approval_validator": ROOT / "reports" / "approval_validator" / "latest_human_approval_validator.json",
    "approval_gated_replay": ROOT / "reports" / "approval_gated_replay" / "latest_approval_gated_replay_dry_run.json",
    "approval_fixtures": ROOT / "reports" / "approval_fixtures" / "latest_approval_fixture_validator.json",
    "live_approval_handoff": ROOT / "reports" / "live_approval_handoff" / "latest_live_approval_handoff_check.json",
    "replay_executor": ROOT / "reports" / "replay_executor" / "latest_approval_gated_replay_executor.json",
    "blocked_continuity": ROOT / "reports" / "blocked_continuity" / "latest_blocked_state_continuity.json",
    "blocked_trend": ROOT / "reports" / "blocked_trend_review" / "latest_blocked_state_trend_review.json",
    "release_readiness": ROOT / "reports" / "release" / "latest_release_readiness.json",
}

STATES = [
    ("v0.6.0", "candidate_branch", "candidate_branch_status"),
    ("v0.6.1", "candidate_replay", "replay_status"),
    ("v0.6.2", "human_approval_template", "approval_template_status"),
    ("v0.6.3", "approval_validator", "validator_status"),
    ("v0.6.4", "approval_gated_replay", "dry_run_status"),
    ("v0.6.5", "approval_fixtures", "fixture_status"),
    ("v0.6.6", "live_approval_handoff", "handoff_status"),
    ("v0.6.7", "replay_executor", "executor_status"),
    ("v0.6.8", "blocked_continuity", "continuity_status"),
    ("v0.6.9", "blocked_trend", "trend_status"),
]

FORBIDDEN = [
    "review_to_application",
    "signoff_to_branch_creation",
    "template_to_approval",
    "fixture_to_live_approval",
    "handoff_to_mutation",
    "replay_readiness_to_execution",
    "blocked_state_to_failure",
    "local_runtime_evidence_to_silicon_validation",
]

def rjson(path: Path):
    if not path.exists():
        return {"missing": True}
    return json.loads(path.read_text(encoding="utf-8"))

def wjson(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def rel(path: Path):
    return str(path.relative_to(ROOT)).replace("\\", "/")

def build_rows(data):
    rows = []
    for version, key, status_key in STATES:
        d = data[key]
        rows.append({
            "version": version,
            "state_id": key,
            "status": d.get(status_key, "MISSING" if d.get("missing") else "RECORDED"),
            "missing": bool(d.get("missing")),
            "replay_allowed": bool(d.get("replay_allowed", False)),
            "executor_ran": bool(d.get("executor_ran", False)),
            "branch_created": bool(d.get("branch_created", False)),
            "mutation_allowed": bool(d.get("mutation_allowed", False)),
            "application_allowed": bool(d.get("application_allowed", False)),
            "calibration_applied": bool(d.get("calibration_applied", False)),
            "policy_enforced": bool(d.get("policy_enforced", False)),
        })
    return rows

def make_charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        wtext(OUT / "chart_generation_skipped.txt", str(exc))
        return paths

    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        path = VIS / name
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(path))

    rows = summary["corridor_states"]
    labels = [r["version"] for r in rows]

    plt.figure(figsize=(11, 4))
    plt.bar(labels, [0 if r["missing"] else 1 for r in rows])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Present")
    plt.title("Approval Corridor State Coverage")
    save("approval_corridor_state_coverage.png")

    counters = {
        "replay_allowed": sum(r["replay_allowed"] for r in rows),
        "executor_ran": sum(r["executor_ran"] for r in rows),
        "branch_created": sum(r["branch_created"] for r in rows),
        "mutation_allowed": sum(r["mutation_allowed"] for r in rows),
        "application_allowed": sum(r["application_allowed"] for r in rows),
        "calibration_applied": sum(r["calibration_applied"] for r in rows),
    }
    plt.figure(figsize=(10, 4))
    plt.bar(list(counters.keys()), list(counters.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Forbidden Transition Counters")
    save("approval_corridor_forbidden_counters.png")

    health = {
        "corridor_locked": int(summary["corridor_locked"]),
        "release_passed": int(summary["release_passed"]),
        "violation_count": summary["violation_count"],
        "missing_count": summary["missing_count"],
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(health.keys()), list(health.values()))
    plt.ylabel("Value")
    plt.title("Approval Corridor Health")
    save("approval_corridor_health_summary.png")
    return paths

def make_md(summary):
    lines = [
        "# Tau Scaling v0.7.0 Approval-Governance Corridor Milestone",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Milestone Result",
        "",
        f"- Corridor status: `{summary['corridor_status']}`",
        f"- Corridor locked: `{summary['corridor_locked']}`",
        f"- Release passed: `{summary['release_passed']}`",
        f"- Violation count: `{summary['violation_count']}`",
        f"- Missing count: `{summary['missing_count']}`",
        "",
        "## Corridor State Chain",
        "",
        "| Version | State | Status | Replay | Executed | Mutation | Application |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for r in summary["corridor_states"]:
        lines.append(f"| `{r['version']}` | `{r['state_id']}` | `{r['status']}` | `{r['replay_allowed']}` | `{r['executor_ran']}` | `{r['mutation_allowed']}` | `{r['application_allowed']}` |")
    lines += ["", "## Forbidden Transitions", ""]
    for item in summary["forbidden_transitions"]:
        lines.append(f"- `{item}`")
    lines += [
        "",
        "## Hard Locks",
        "",
        "```text",
        "replay_allowed: false",
        "executor_ran: false",
        "branch_created: false",
        "mutation_allowed: false",
        "application_allowed: false",
        "calibration_applied: false",
        "policy_enforced: false",
        "```",
        "",
        "## Charts",
        "",
    ]
    for p in summary["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += [
        "## Boundary",
        "",
        summary["boundary"],
        "",
        "## Tau Return Plan",
        "",
        summary["tau_return_plan"],
        "",
    ]
    return "\n".join(lines)

def main():
    data = {k: rjson(p) for k, p in INPUTS.items()}
    rows = build_rows(data)

    release = data["release_readiness"]
    release_passed = release.get("passed") is True and len(release.get("findings", [])) == 0 and len(release.get("step_failures", [])) == 0

    violations = []
    for row in rows:
        for key in ["replay_allowed", "executor_ran", "branch_created", "mutation_allowed", "application_allowed", "calibration_applied", "policy_enforced"]:
            if row.get(key) is True:
                violations.append({"state_id": row["state_id"], "violation": key})

    missing_states = [r["state_id"] for r in rows if r["missing"]]
    corridor_locked = release_passed and not violations and not missing_states
    corridor_status = "APPROVAL_CORRIDOR_MILESTONE_LOCKED__NO_EXECUTION_NO_MUTATION" if corridor_locked else "APPROVAL_CORRIDOR_MILESTONE_NEEDS_REVIEW"

    summary = {
        "schema": "tau-scaling-approval-governance-corridor-milestone-v0.7.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "corridor_status": corridor_status,
        "corridor_locked": bool(corridor_locked),
        "release_passed": bool(release_passed),
        "violation_count": len(violations),
        "violations": violations,
        "missing_count": len(missing_states),
        "missing_states": missing_states,
        "corridor_states": rows,
        "forbidden_transitions": FORBIDDEN,
        "replay_allowed": False,
        "executor_ran": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "next_recommendation": "Return to Tau mechanics after packaging this corridor.",
        "tau_return_plan": "Shift back to core Tau Scaling: inspect tau-vector semantics, gate algebra, TSEK thresholds, synthetic gate suite, sensitivity sweeps, evidence-card design, and classifier calibration boundaries. Do not add more approval gates unless a real live approval workflow is intentionally introduced.",
        "boundary": "Approval-governance corridor milestones are local classifier-governance milestone artifacts. They summarize authority boundaries and execution locks. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    summary["chart_paths"] = make_charts(summary)

    wjson(OUT / "approval_governance_corridor_milestone_v0_7_0.json", summary)
    wjson(OUT / "latest_approval_governance_corridor_milestone.json", summary)
    wtext(OUT / "approval_governance_corridor_milestone_v0_7_0.md", make_md(summary))
    wtext(OUT / "latest_approval_governance_corridor_milestone.md", make_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "corridor_status": summary["corridor_status"],
        "corridor_locked": summary["corridor_locked"],
        "release_passed": summary["release_passed"],
        "violation_count": summary["violation_count"],
        "missing_count": summary["missing_count"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/approval_corridor/latest_approval_governance_corridor_milestone.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
