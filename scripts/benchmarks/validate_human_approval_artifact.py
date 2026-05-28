
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "reports" / "human_approval" / "human_approval_artifact_template_v0_6_2.json"
REPLAY = ROOT / "reports" / "candidate_replay" / "latest_candidate_branch_replay_harness.json"
OUT = ROOT / "reports" / "approval_validator"
VIS = ROOT / "visuals" / "approval_validator" / "v0_6_3"

def rjson(p):
    return json.loads(p.read_text(encoding="utf-8"))

def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def rel(p):
    return str(p.relative_to(ROOT)).replace("\\", "/")

def validate_artifact(artifact):
    checks = []

    def add(check_id, passed, observed, required=True):
        checks.append({
            "check_id": check_id,
            "passed": bool(passed),
            "observed": observed,
            "required": required,
        })

    decision = artifact.get("approval_decision")
    approver = str(artifact.get("approver", "")).strip()
    ts = str(artifact.get("approval_timestamp", "")).strip()
    required_statement = str(artifact.get("required_statement", "")).strip()
    locks = artifact.get("explicit_locks", {}) or {}

    add("schema_is_v0_6_2", artifact.get("schema") == "tau-scaling-human-approval-artifact-v0.6.2", str(artifact.get("schema")))
    add("decision_is_explicit", decision in ["APPROVE_REPLAY_ONLY", "DENY", "REQUEST_MORE_EVIDENCE"], str(decision))
    add("approver_present", bool(approver), approver or "missing")
    add("timestamp_present", bool(ts), ts or "missing")
    add("scope_replay_only", artifact.get("scope") == "candidate_branch_replay_only", str(artifact.get("scope")))
    add("required_statement_present", "does not authorize classifier mutation" in required_statement, "present" if required_statement else "missing")
    add("runtime_mutation_locked", locks.get("runtime_mutation_allowed") is False, str(locks.get("runtime_mutation_allowed")))
    add("classifier_mutation_locked", locks.get("classifier_mutation_allowed") is False, str(locks.get("classifier_mutation_allowed")))
    add("application_locked", locks.get("application_allowed") is False, str(locks.get("application_allowed")))
    add("calibration_unapplied", locks.get("calibration_applied") is False, str(locks.get("calibration_applied")))
    add("policy_unenforced", locks.get("policy_enforced") is False, str(locks.get("policy_enforced")))

    return checks

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        wtext(OUT / "chart_generation_skipped.txt", str(e))
        return paths
    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        p = VIS / name
        plt.tight_layout()
        plt.savefig(p, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(p))

    counts = {
        "passed": summary["check_pass_count"],
        "failed": summary["check_fail_count"],
    }
    plt.figure(figsize=(7, 4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.ylabel("Check count")
    plt.title("Human Approval Validator Checks")
    save("approval_validator_check_counts.png")

    gates = {
        "approval_valid": int(summary["approval_valid"]),
        "replay_allowed": int(summary["replay_allowed"]),
        "branch_creation_allowed": int(summary["branch_creation_allowed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
        "application_allowed": int(summary["application_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Approval Validator Gate State")
    save("approval_validator_gate_state.png")

    classes = {summary["validator_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(classes.keys()), list(classes.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Approval Validator Status")
    save("approval_validator_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.3 Human Approval Artifact Validator",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Validator Result",
        "",
        f"- Validator status: `{s['validator_status']}`",
        f"- Approval decision: `{s['approval_decision']}`",
        f"- Approval valid: `{s['approval_valid']}`",
        f"- Replay allowed: `{s['replay_allowed']}`",
        f"- Branch creation allowed: `{s['branch_creation_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Validation Checks",
        "",
        "| Check | Passed | Observed | Required |",
        "|---|---|---|---|",
    ]
    for row in s["checks"]:
        lines.append(f"| `{row['check_id']}` | `{row['passed']}` | `{row['observed']}` | `{row['required']}` |")
    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    artifact = rjson(TEMPLATE)
    replay = rjson(REPLAY)
    checks = validate_artifact(artifact)

    pass_count = sum(1 for c in checks if c["passed"])
    fail_count = sum(1 for c in checks if c["required"] and not c["passed"])

    decision = artifact.get("approval_decision")
    approval_valid = (
        fail_count == 0
        and decision == "APPROVE_REPLAY_ONLY"
        and replay.get("replay_status") == "REPLAY_BLOCKED__HUMAN_APPROVAL_ARTIFACT_REQUIRED"
    )

    if approval_valid:
        status = "APPROVAL_VALID_FOR_REPLAY_ONLY"
    elif decision == "DENY":
        status = "APPROVAL_DENIED"
    elif decision == "REQUEST_MORE_EVIDENCE":
        status = "APPROVAL_REQUESTS_MORE_EVIDENCE"
    else:
        status = "APPROVAL_INVALID_OR_TEMPLATE_ONLY"

    summary = {
        "schema": "tau-scaling-human-approval-artifact-validator-v0.6.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_approval_artifact": rel(TEMPLATE),
        "input_candidate_replay": rel(REPLAY),
        "approval_decision": decision,
        "validator_status": status,
        "approval_valid": bool(approval_valid),
        "checks": checks,
        "check_pass_count": pass_count,
        "check_fail_count": fail_count,
        "replay_allowed": bool(approval_valid),
        "branch_creation_allowed": False,
        "branch_created": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Replay may be prepared only if approval_valid is true. Branch creation and mutation remain blocked." if approval_valid else "Approval is not valid for replay. Keep replay blocked.",
        "boundary": "Human approval validators are local classifier-governance validation artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.4 should add approval-gated replay dry-run only if approval_valid is true; otherwise preserve blocked state.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "human_approval_validator_v0_6_3.json", summary)
    wjson(OUT / "latest_human_approval_validator.json", summary)
    wtext(OUT / "human_approval_validator_v0_6_3.md", report(summary))
    wtext(OUT / "latest_human_approval_validator.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "validator_status": summary["validator_status"],
        "approval_decision": summary["approval_decision"],
        "approval_valid": summary["approval_valid"],
        "check_pass_count": summary["check_pass_count"],
        "check_fail_count": summary["check_fail_count"],
        "replay_allowed": summary["replay_allowed"],
        "branch_creation_allowed": summary["branch_creation_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/approval_validator/latest_human_approval_validator.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
