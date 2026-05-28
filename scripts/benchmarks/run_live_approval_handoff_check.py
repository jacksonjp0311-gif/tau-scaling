
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "reports" / "approval_fixtures" / "latest_approval_fixture_validator.json"
LIVE_DIR = ROOT / "reports" / "human_approval" / "live"
OUT = ROOT / "reports" / "live_approval_handoff"
VIS = ROOT / "visuals" / "live_approval_handoff" / "v0_6_6"

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

def find_live_approval():
    if not LIVE_DIR.exists():
        return None
    candidates = sorted(LIVE_DIR.glob("*.json"))
    for p in candidates:
        try:
            data = rjson(p)
        except Exception:
            continue
        if data.get("fixture_only") is True:
            continue
        if data.get("approval_decision") in ["APPROVE_REPLAY_ONLY", "DENY", "REQUEST_MORE_EVIDENCE"]:
            return p
    return None

def validate_live(data):
    if not data:
        return {
            "live_approval_present": False,
            "live_approval_valid": False,
            "approval_decision": "MISSING",
            "validation_status": "LIVE_APPROVAL_MISSING",
            "reason": "No live approval artifact was found in reports/human_approval/live/.",
        }

    locks = data.get("explicit_locks", {}) or {}
    decision = data.get("approval_decision")
    required_statement = str(data.get("required_statement", ""))
    ok = (
        data.get("schema") == "tau-scaling-human-approval-artifact-v0.6.2"
        and data.get("fixture_only") is not True
        and decision in ["APPROVE_REPLAY_ONLY", "DENY", "REQUEST_MORE_EVIDENCE"]
        and bool(str(data.get("approver", "")).strip())
        and bool(str(data.get("approval_timestamp", "")).strip())
        and data.get("scope") == "candidate_branch_replay_only"
        and "does not authorize classifier mutation" in required_statement
        and locks.get("runtime_mutation_allowed") is False
        and locks.get("classifier_mutation_allowed") is False
        and locks.get("application_allowed") is False
        and locks.get("calibration_applied") is False
        and locks.get("policy_enforced") is False
    )

    if ok and decision == "APPROVE_REPLAY_ONLY":
        status = "LIVE_APPROVAL_VALID_FOR_REPLAY_ONLY"
        reason = "A non-fixture live approval artifact explicitly approves replay only while preserving all mutation/application locks."
    elif ok and decision == "DENY":
        status = "LIVE_APPROVAL_DENIES_REPLAY"
        reason = "A valid non-fixture live approval artifact denies replay."
    elif ok and decision == "REQUEST_MORE_EVIDENCE":
        status = "LIVE_APPROVAL_REQUESTS_MORE_EVIDENCE"
        reason = "A valid non-fixture live approval artifact requests more evidence before replay."
    else:
        status = "LIVE_APPROVAL_INVALID"
        reason = "A live approval artifact was found, but it did not satisfy all schema, identity, statement, and lock requirements."

    return {
        "live_approval_present": True,
        "live_approval_valid": bool(ok),
        "approval_decision": decision,
        "validation_status": status,
        "reason": reason,
    }

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

    gates = {
        "live_present": int(summary["live_approval_present"]),
        "live_valid": int(summary["live_approval_valid"]),
        "fixture_misuse": int(summary["fixture_misuse_detected"]),
        "replay_allowed": int(summary["replay_allowed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Live Approval Handoff Gate")
    save("live_approval_handoff_gate.png")

    fixture_state = {
        "fixtures_valid": int(summary["fixtures_validated"]),
        "live_approval_present": int(summary["live_approval_present"]),
        "replay_allowed": int(summary["replay_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(fixture_state.keys()), list(fixture_state.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Fixture vs Live Approval Separation")
    save("fixture_vs_live_approval.png")

    status = {summary["handoff_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(status.keys()), list(status.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Live Approval Handoff Status")
    save("live_approval_handoff_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.6 Live Approval Handoff Check",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Handoff Result",
        "",
        f"- Handoff status: `{s['handoff_status']}`",
        f"- Live approval path: `{s['live_approval_path']}`",
        f"- Live approval present: `{s['live_approval_present']}`",
        f"- Live approval valid: `{s['live_approval_valid']}`",
        f"- Fixture misuse detected: `{s['fixture_misuse_detected']}`",
        f"- Approval decision: `{s['approval_decision']}`",
        f"- Replay allowed: `{s['replay_allowed']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        "",
        "## Reason",
        "",
        s["reason"],
        "",
        "## Charts",
        "",
    ]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    fixtures = rjson(FIXTURES)
    fixture_paths = [ROOT / p for p in fixtures.get("fixture_paths", [])]
    fixture_misuse = any(str(p).startswith(str(LIVE_DIR)) for p in fixture_paths)

    live_path = find_live_approval()
    live_data = rjson(live_path) if live_path else None
    live = validate_live(live_data)

    fixtures_validated = fixtures.get("fixture_status") == "FIXTURES_VALIDATED__NO_LIVE_APPROVAL_CREATED"
    replay_allowed = live["live_approval_valid"] and live["approval_decision"] == "APPROVE_REPLAY_ONLY" and not fixture_misuse

    if replay_allowed:
        handoff_status = "LIVE_APPROVAL_HANDOFF_VALID_FOR_REPLAY_ONLY"
    elif fixture_misuse:
        handoff_status = "HANDOFF_BLOCKED__FIXTURE_MISUSE_DETECTED"
    elif not live["live_approval_present"]:
        handoff_status = "HANDOFF_BLOCKED__NO_LIVE_APPROVAL"
    elif live["validation_status"] == "LIVE_APPROVAL_DENIES_REPLAY":
        handoff_status = "HANDOFF_BLOCKED__LIVE_DENIAL"
    elif live["validation_status"] == "LIVE_APPROVAL_REQUESTS_MORE_EVIDENCE":
        handoff_status = "HANDOFF_BLOCKED__MORE_EVIDENCE_REQUESTED"
    else:
        handoff_status = "HANDOFF_BLOCKED__LIVE_APPROVAL_INVALID"

    summary = {
        "schema": "tau-scaling-live-approval-handoff-check-v0.6.6",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_fixture_validator": rel(FIXTURES),
        "live_approval_directory": rel(LIVE_DIR),
        "live_approval_path": rel(live_path) if live_path else "MISSING",
        "fixtures_validated": bool(fixtures_validated),
        "fixture_misuse_detected": bool(fixture_misuse),
        "live_approval_present": live["live_approval_present"],
        "live_approval_valid": live["live_approval_valid"],
        "approval_decision": live["approval_decision"],
        "handoff_status": handoff_status,
        "reason": live["reason"],
        "replay_allowed": bool(replay_allowed),
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Replay may be prepared in a future layer only if handoff_status is LIVE_APPROVAL_HANDOFF_VALID_FOR_REPLAY_ONLY." if replay_allowed else "Keep replay blocked. A non-fixture live approval artifact is required.",
        "boundary": "Live approval handoff checks are local classifier-governance boundary artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.7 should create an approval-gated replay executor that still refuses to run unless the live approval handoff is valid.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "live_approval_handoff_check_v0_6_6.json", summary)
    wjson(OUT / "latest_live_approval_handoff_check.json", summary)
    wtext(OUT / "live_approval_handoff_check_v0_6_6.md", report(summary))
    wtext(OUT / "latest_live_approval_handoff_check.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "handoff_status": summary["handoff_status"],
        "live_approval_present": summary["live_approval_present"],
        "live_approval_valid": summary["live_approval_valid"],
        "fixture_misuse_detected": summary["fixture_misuse_detected"],
        "approval_decision": summary["approval_decision"],
        "replay_allowed": summary["replay_allowed"],
        "branch_created": summary["branch_created"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/live_approval_handoff/latest_live_approval_handoff_check.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
