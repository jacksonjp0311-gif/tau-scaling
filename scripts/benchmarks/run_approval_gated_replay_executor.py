
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "reports" / "live_approval_handoff" / "latest_live_approval_handoff_check.json"
OUT = ROOT / "reports" / "replay_executor"
VIS = ROOT / "visuals" / "replay_executor" / "v0_6_7"

EXECUTOR_PLAN = [
    ("baseline_claim", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json"),
    ("promotion_path_claim", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json"),
    ("support_aware_negative_controls", "python scripts/benchmarks/run_support_aware_negative_controls.py"),
    ("calibration_counterfactuals", "python scripts/benchmarks/run_calibration_counterfactuals.py"),
    ("review_signoff_gate", "python scripts/benchmarks/run_review_signoff_gate.py"),
    ("candidate_branch_gate", "python scripts/benchmarks/run_candidate_branch_gate.py"),
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
        "handoff_valid": int(summary["handoff_valid"]),
        "executor_allowed": int(summary["executor_allowed"]),
        "executor_ran": int(summary["executor_ran"]),
        "branch_created": int(summary["branch_created"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Approval-Gated Replay Executor State")
    save("replay_executor_gate_state.png")

    steps = summary["executor_steps"]
    plt.figure(figsize=(10, 4))
    plt.bar([s["step_id"] for s in steps], [int(s["would_run_if_authorized"]) for s in steps])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Would run if authorized")
    plt.title("Replay Executor Planned Steps")
    save("replay_executor_steps.png")

    status = {summary["executor_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(status.keys()), list(status.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Replay Executor Status")
    save("replay_executor_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.7 Approval-Gated Replay Executor",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Executor Result",
        "",
        f"- Executor status: `{s['executor_status']}`",
        f"- Handoff status: `{s['handoff_status']}`",
        f"- Handoff valid: `{s['handoff_valid']}`",
        f"- Executor allowed: `{s['executor_allowed']}`",
        f"- Executor ran: `{s['executor_ran']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        "",
        "## Executor Plan",
        "",
        "| Step | Would run if authorized | Executed now | Command |",
        "|---|---|---|---|",
    ]
    for step in s["executor_steps"]:
        lines.append(
            f"| `{step['step_id']}` | `{step['would_run_if_authorized']}` | `{step['executed_now']}` | `{step['command']}` |"
        )
    lines += [
        "",
        "## Block Reason",
        "",
        s["block_reason"],
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
    handoff = rjson(HANDOFF)

    handoff_valid = handoff.get("handoff_status") == "LIVE_APPROVAL_HANDOFF_VALID_FOR_REPLAY_ONLY"
    executor_allowed = bool(handoff_valid and handoff.get("replay_allowed") is True)
    executor_ran = False

    if executor_allowed:
        executor_status = "EXECUTOR_READY__NOT_RUN_BY_DEFAULT"
        block_reason = "Live approval handoff is valid. This layer still records executor readiness without running commands by default."
    else:
        executor_status = "EXECUTOR_BLOCKED__LIVE_APPROVAL_HANDOFF_NOT_VALID"
        block_reason = "Live approval handoff is not valid for replay. Executor remains blocked."

    steps = [
        {
            "step_id": sid,
            "command": cmd,
            "would_run_if_authorized": bool(executor_allowed),
            "executed_now": False,
        }
        for sid, cmd in EXECUTOR_PLAN
    ]

    summary = {
        "schema": "tau-scaling-approval-gated-replay-executor-v0.6.7",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_live_approval_handoff": rel(HANDOFF),
        "handoff_status": handoff.get("handoff_status"),
        "handoff_valid": bool(handoff_valid),
        "executor_allowed": bool(executor_allowed),
        "executor_ran": bool(executor_ran),
        "executor_status": executor_status,
        "executor_steps": steps,
        "block_reason": block_reason,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Keep executor blocked until live approval handoff is valid." if not executor_allowed else "Executor readiness exists, but command execution still requires a separate run authorization layer.",
        "boundary": "Approval-gated replay executors are local classifier-governance execution-boundary artifacts. This report does not execute replay commands by default, does not create branches, does not mutate classifier behavior, does not apply calibration, and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.8 should add explicit run authorization if live handoff becomes valid; otherwise continue blocked-state observability.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "approval_gated_replay_executor_v0_6_7.json", summary)
    wjson(OUT / "latest_approval_gated_replay_executor.json", summary)
    wtext(OUT / "approval_gated_replay_executor_v0_6_7.md", report(summary))
    wtext(OUT / "latest_approval_gated_replay_executor.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "executor_status": summary["executor_status"],
        "handoff_status": summary["handoff_status"],
        "handoff_valid": summary["handoff_valid"],
        "executor_allowed": summary["executor_allowed"],
        "executor_ran": summary["executor_ran"],
        "branch_created": summary["branch_created"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/replay_executor/latest_approval_gated_replay_executor.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
