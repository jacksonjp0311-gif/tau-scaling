
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "reports" / "human_approval" / "human_approval_artifact_template_v0_6_2.json"
OUT = ROOT / "reports" / "approval_fixtures"
VIS = ROOT / "visuals" / "approval_fixtures" / "v0_6_5"
FIXTURE_DIR = OUT / "fixtures" / "v0_6_5"

DECISIONS = [
    ("approve_replay_only_fixture", "APPROVE_REPLAY_ONLY"),
    ("deny_fixture", "DENY"),
    ("request_more_evidence_fixture", "REQUEST_MORE_EVIDENCE"),
]

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

def make_fixture(base, fixture_name, decision):
    fx = dict(base)
    fx["artifact_status"] = "FIXTURE_ONLY_NOT_LIVE_APPROVAL"
    fx["approval_decision"] = decision
    fx["approver"] = "fixture-only"
    fx["approval_timestamp"] = datetime.now(timezone.utc).isoformat()
    fx["fixture_name"] = fixture_name
    fx["fixture_only"] = True
    fx["fixture_boundary"] = "This fixture tests validator behavior only. It is not a live human approval artifact."
    locks = dict(fx.get("explicit_locks", {}))
    # Even the approval fixture permits replay interpretation only; branch/runtime/classifier mutation remain false.
    locks["branch_creation_allowed"] = False
    locks["runtime_mutation_allowed"] = False
    locks["classifier_mutation_allowed"] = False
    locks["application_allowed"] = False
    locks["calibration_applied"] = False
    locks["policy_enforced"] = False
    fx["explicit_locks"] = locks
    return fx

def validate_fixture(fx):
    decision = fx.get("approval_decision")
    locks = fx.get("explicit_locks", {}) or {}
    required_statement = str(fx.get("required_statement", ""))
    approver = str(fx.get("approver", "")).strip()
    ts = str(fx.get("approval_timestamp", "")).strip()

    base_valid = (
        fx.get("schema") == "tau-scaling-human-approval-artifact-v0.6.2"
        and decision in ["APPROVE_REPLAY_ONLY", "DENY", "REQUEST_MORE_EVIDENCE"]
        and bool(approver)
        and bool(ts)
        and fx.get("scope") == "candidate_branch_replay_only"
        and "does not authorize classifier mutation" in required_statement
        and locks.get("runtime_mutation_allowed") is False
        and locks.get("classifier_mutation_allowed") is False
        and locks.get("application_allowed") is False
        and locks.get("calibration_applied") is False
        and locks.get("policy_enforced") is False
    )

    if decision == "APPROVE_REPLAY_ONLY" and base_valid:
        expected_outcome = "VALID_FOR_REPLAY_ONLY_FIXTURE"
        replay_allowed_if_live = True
    elif decision == "DENY" and base_valid:
        expected_outcome = "DENIAL_FIXTURE_BLOCKS_REPLAY"
        replay_allowed_if_live = False
    elif decision == "REQUEST_MORE_EVIDENCE" and base_valid:
        expected_outcome = "MORE_EVIDENCE_FIXTURE_BLOCKS_REPLAY"
        replay_allowed_if_live = False
    else:
        expected_outcome = "INVALID_FIXTURE"
        replay_allowed_if_live = False

    return {
        "fixture_name": fx.get("fixture_name"),
        "approval_decision": decision,
        "fixture_valid": bool(base_valid),
        "expected_outcome": expected_outcome,
        "replay_allowed_if_live": replay_allowed_if_live,
        "branch_creation_allowed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "fixture_only": True,
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

    rows = summary["fixture_results"]
    plt.figure(figsize=(9, 4))
    plt.bar([r["approval_decision"] for r in rows], [int(r["fixture_valid"]) for r in rows])
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Fixture valid")
    plt.title("Approval Fixture Validity")
    save("approval_fixture_validity.png")

    plt.figure(figsize=(9, 4))
    plt.bar([r["approval_decision"] for r in rows], [int(r["replay_allowed_if_live"]) for r in rows])
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Replay allowed if live")
    plt.title("Approval Fixture Replay Semantics")
    save("approval_fixture_replay_semantics.png")

    locks = {
        "live_approval_present": int(summary["live_approval_present"]),
        "fixture_only": int(summary["fixture_only"]),
        "branch_created": int(summary["branch_created"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(locks.keys()), list(locks.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Approval Fixture Lock State")
    save("approval_fixture_lock_state.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.5 Approval Fixture and Denial Fixture Validator",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Fixture Result",
        "",
        f"- Fixture status: `{s['fixture_status']}`",
        f"- Fixture count: `{s['fixture_count']}`",
        f"- Valid fixture count: `{s['valid_fixture_count']}`",
        f"- Live approval present: `{s['live_approval_present']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        "",
        "## Fixture Matrix",
        "",
        "| Fixture | Decision | Valid | Expected outcome | Replay if live |",
        "|---|---|---|---|---|",
    ]
    for r in s["fixture_results"]:
        lines.append(
            f"| `{r['fixture_name']}` | `{r['approval_decision']}` | `{r['fixture_valid']}` | `{r['expected_outcome']}` | `{r['replay_allowed_if_live']}` |"
        )
    lines += ["", "## Fixture Files", ""]
    for p in s["fixture_paths"]:
        lines.append(f"- `{p}`")
    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    base = rjson(TEMPLATE)
    fixture_paths = []
    results = []

    for fixture_name, decision in DECISIONS:
        fx = make_fixture(base, fixture_name, decision)
        path = FIXTURE_DIR / f"{fixture_name}.json"
        wjson(path, fx)
        fixture_paths.append(rel(path))
        results.append(validate_fixture(fx))

    valid_count = sum(1 for r in results if r["fixture_valid"])
    approval_fixture = next((r for r in results if r["approval_decision"] == "APPROVE_REPLAY_ONLY"), None)
    denial_fixture = next((r for r in results if r["approval_decision"] == "DENY"), None)
    more_evidence_fixture = next((r for r in results if r["approval_decision"] == "REQUEST_MORE_EVIDENCE"), None)

    semantic_pass = (
        valid_count == len(results)
        and approval_fixture and approval_fixture["replay_allowed_if_live"] is True
        and denial_fixture and denial_fixture["replay_allowed_if_live"] is False
        and more_evidence_fixture and more_evidence_fixture["replay_allowed_if_live"] is False
    )

    summary = {
        "schema": "tau-scaling-approval-fixture-denial-fixture-validator-v0.6.5",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_template": rel(TEMPLATE),
        "fixture_status": "FIXTURES_VALIDATED__NO_LIVE_APPROVAL_CREATED" if semantic_pass else "FIXTURE_VALIDATION_FAILED",
        "fixture_count": len(results),
        "valid_fixture_count": valid_count,
        "fixture_results": results,
        "fixture_paths": fixture_paths,
        "fixture_only": True,
        "live_approval_present": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Fixture semantics are validated. A future live approval artifact may be validated separately, but fixtures do not authorize replay.",
        "boundary": "Approval fixtures are local classifier-governance test fixtures. They are not live approvals, do not create branches, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.6 should add a live-approval handoff check that refuses to treat fixtures as approvals.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "approval_fixture_validator_v0_6_5.json", summary)
    wjson(OUT / "latest_approval_fixture_validator.json", summary)
    wtext(OUT / "approval_fixture_validator_v0_6_5.md", report(summary))
    wtext(OUT / "latest_approval_fixture_validator.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "fixture_status": summary["fixture_status"],
        "fixture_count": summary["fixture_count"],
        "valid_fixture_count": summary["valid_fixture_count"],
        "live_approval_present": summary["live_approval_present"],
        "branch_created": summary["branch_created"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/approval_fixtures/latest_approval_fixture_validator.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
