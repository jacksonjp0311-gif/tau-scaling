
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "reports" / "candidate_branch" / "latest_candidate_branch_gate.json"
SIGNOFF = ROOT / "reports" / "review_signoff" / "latest_review_signoff_gate.json"
OUT = ROOT / "reports" / "candidate_replay"
VIS = ROOT / "visuals" / "candidate_replay" / "v0_6_1"

REPLAY_STEPS = [
    ("baseline_claim", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json"),
    ("promotion_path_claim", "python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json"),
    ("support_controls", "python scripts/benchmarks/run_support_aware_negative_controls.py"),
    ("calibration_counterfactuals", "python scripts/benchmarks/run_calibration_counterfactuals.py"),
    ("review_signoff", "python scripts/benchmarks/run_review_signoff_gate.py"),
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
        "branch_proposal_allowed": int(summary["branch_proposal_allowed"]),
        "human_approval_present": int(summary["human_approval_present"]),
        "replay_allowed": int(summary["replay_allowed"]),
        "branch_created": int(summary["branch_created"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Candidate Replay Gate State")
    save("candidate_replay_gate_state.png")

    steps = summary["replay_steps"]
    plt.figure(figsize=(10, 4))
    plt.bar([s["step_id"] for s in steps], [int(s["included"]) for s in steps])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Included")
    plt.title("Replay Harness Planned Steps")
    save("candidate_replay_steps.png")

    classes = {summary["replay_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(classes.keys()), list(classes.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Candidate Replay Status")
    save("candidate_replay_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.1 Candidate Branch Replay Harness",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Replay Gate Result",
        "",
        f"- Replay status: `{s['replay_status']}`",
        f"- Replay allowed: `{s['replay_allowed']}`",
        f"- Human approval present: `{s['human_approval_present']}`",
        f"- Branch proposal allowed: `{s['branch_proposal_allowed']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Replay Plan",
        "",
        "| Step | Included | Command | Purpose |",
        "|---|---|---|---|",
    ]
    for step in s["replay_steps"]:
        lines.append(
            f"| `{step['step_id']}` | `{step['included']}` | `{step['command']}` | {step['purpose']} |"
        )
    lines += [
        "",
        "## Approval Boundary",
        "",
        s["approval_boundary"],
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
    candidate = rjson(CANDIDATE)
    signoff = rjson(SIGNOFF)

    proposal_allowed = bool(candidate.get("branch_proposal_allowed"))
    human_approval_present = bool(candidate.get("human_approval_present"))
    signoff_ready = signoff.get("signoff_status") == "REVIEW_SIGNOFF_READY_NOT_APPLICATION"

    # This harness is intentionally blocked unless a future explicit approval artifact exists.
    replay_allowed = proposal_allowed and signoff_ready and human_approval_present
    status = "REPLAY_BLOCKED__HUMAN_APPROVAL_ARTIFACT_REQUIRED"
    if replay_allowed:
        status = "REPLAY_READY__APPROVAL_PRESENT"

    replay_steps = [
        {
            "step_id": sid,
            "command": cmd,
            "included": True,
            "purpose": "Replay baseline/candidate evidence without changing default runtime behavior.",
        }
        for sid, cmd in REPLAY_STEPS
    ]

    summary = {
        "schema": "tau-scaling-candidate-branch-replay-harness-v0.6.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_candidate_branch_gate": "reports/candidate_branch/latest_candidate_branch_gate.json",
        "input_review_signoff": "reports/review_signoff/latest_review_signoff_gate.json",
        "selected_report_only_threshold": candidate.get("selected_report_only_threshold"),
        "proposed_branch_name": candidate.get("proposed_branch_name"),
        "branch_proposal_allowed": proposal_allowed,
        "human_approval_required": True,
        "human_approval_present": human_approval_present,
        "replay_allowed": replay_allowed,
        "replay_status": status,
        "replay_steps": replay_steps,
        "branch_created": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "approval_boundary": "Replay is intentionally blocked until a separate explicit human approval artifact exists. This v0.6.1 layer prepares the replay harness and proves the block.",
        "final_recommendation": "Add an explicit human approval artifact before replaying any candidate branch. Do not create a branch or mutate classifier behavior from this report.",
        "boundary": "Candidate branch replay harnesses are local classifier-governance planning artifacts. They do not create branches by default, do not change classifier behavior, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.2 should add a human approval artifact template or explicit approval-denial ledger before replay can proceed.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "candidate_branch_replay_harness_v0_6_1.json", summary)
    wjson(OUT / "latest_candidate_branch_replay_harness.json", summary)
    wtext(OUT / "candidate_branch_replay_harness_v0_6_1.md", report(summary))
    wtext(OUT / "latest_candidate_branch_replay_harness.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "replay_status": summary["replay_status"],
        "branch_proposal_allowed": summary["branch_proposal_allowed"],
        "human_approval_required": summary["human_approval_required"],
        "human_approval_present": summary["human_approval_present"],
        "replay_allowed": summary["replay_allowed"],
        "branch_created": summary["branch_created"],
        "application_allowed": summary["application_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/candidate_replay/latest_candidate_branch_replay_harness.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
