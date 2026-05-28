
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "reports" / "approval_validator" / "latest_human_approval_validator.json"
REPLAY = ROOT / "reports" / "candidate_replay" / "latest_candidate_branch_replay_harness.json"
OUT = ROOT / "reports" / "approval_gated_replay"
VIS = ROOT / "visuals" / "approval_gated_replay" / "v0_6_4"

DRY_RUN_STEPS = [
    ("baseline_claim_replay", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json"),
    ("promotion_path_replay", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json"),
    ("support_control_replay", "python scripts/benchmarks/run_support_aware_negative_controls.py"),
    ("counterfactual_replay", "python scripts/benchmarks/run_calibration_counterfactuals.py"),
    ("review_signoff_replay", "python scripts/benchmarks/run_review_signoff_gate.py"),
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
        "approval_valid": int(summary["approval_valid"]),
        "dry_run_allowed": int(summary["dry_run_allowed"]),
        "dry_run_executed": int(summary["dry_run_executed"]),
        "branch_created": int(summary["branch_created"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Approval-Gated Replay State")
    save("approval_gated_replay_state.png")

    steps = summary["dry_run_steps"]
    plt.figure(figsize=(10, 4))
    plt.bar([s["step_id"] for s in steps], [int(s["eligible"]) for s in steps])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Eligible if approved")
    plt.title("Approval-Gated Replay Planned Steps")
    save("approval_gated_replay_steps.png")

    status = {summary["dry_run_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(status.keys()), list(status.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Approval-Gated Replay Status")
    save("approval_gated_replay_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.4 Approval-Gated Replay Dry-Run",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Dry-Run Result",
        "",
        f"- Dry-run status: `{s['dry_run_status']}`",
        f"- Approval valid: `{s['approval_valid']}`",
        f"- Dry-run allowed: `{s['dry_run_allowed']}`",
        f"- Dry-run executed: `{s['dry_run_executed']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Planned Replay Steps",
        "",
        "| Step | Eligible if approved | Executed now | Command |",
        "|---|---|---|---|",
    ]
    for step in s["dry_run_steps"]:
        lines.append(
            f"| `{step['step_id']}` | `{step['eligible']}` | `{step['executed']}` | `{step['command']}` |"
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
    validator = rjson(VALIDATOR)
    replay = rjson(REPLAY)

    approval_valid = bool(validator.get("approval_valid"))
    dry_run_allowed = approval_valid and bool(validator.get("replay_allowed"))
    dry_run_executed = False

    if dry_run_allowed:
        status = "DRY_RUN_READY__NOT_EXECUTED_BY_DEFAULT"
        block_reason = "Approval is valid, but this layer still records the dry-run plan without changing runtime behavior."
    else:
        status = "DRY_RUN_BLOCKED__APPROVAL_NOT_VALID"
        block_reason = "Approval validator did not produce approval_valid=true. Replay remains blocked."

    steps = [
        {
            "step_id": sid,
            "command": cmd,
            "eligible": bool(dry_run_allowed),
            "executed": False,
        }
        for sid, cmd in DRY_RUN_STEPS
    ]

    summary = {
        "schema": "tau-scaling-approval-gated-replay-dry-run-v0.6.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_approval_validator": rel(VALIDATOR),
        "input_candidate_replay": rel(REPLAY),
        "approval_valid": approval_valid,
        "approval_decision": validator.get("approval_decision"),
        "dry_run_allowed": dry_run_allowed,
        "dry_run_executed": dry_run_executed,
        "dry_run_status": status,
        "dry_run_steps": steps,
        "block_reason": block_reason,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Keep replay blocked until approval_valid is true." if not dry_run_allowed else "Approval is valid; next layer may run a bounded replay plan without mutation.",
        "boundary": "Approval-gated replay dry-runs are local classifier-governance planning artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.5 should add an explicit approval fixture or denial fixture validator before any executable replay path.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "approval_gated_replay_dry_run_v0_6_4.json", summary)
    wjson(OUT / "latest_approval_gated_replay_dry_run.json", summary)
    wtext(OUT / "approval_gated_replay_dry_run_v0_6_4.md", report(summary))
    wtext(OUT / "latest_approval_gated_replay_dry_run.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "dry_run_status": summary["dry_run_status"],
        "approval_valid": summary["approval_valid"],
        "dry_run_allowed": summary["dry_run_allowed"],
        "dry_run_executed": summary["dry_run_executed"],
        "branch_created": summary["branch_created"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
