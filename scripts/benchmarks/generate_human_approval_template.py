
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPLAY = ROOT / "reports" / "candidate_replay" / "latest_candidate_branch_replay_harness.json"
CANDIDATE = ROOT / "reports" / "candidate_branch" / "latest_candidate_branch_gate.json"
OUT = ROOT / "reports" / "human_approval"
VIS = ROOT / "visuals" / "human_approval" / "v0_6_2"

APPROVAL_TEMPLATE = {
    "schema": "tau-scaling-human-approval-artifact-v0.6.2",
    "artifact_status": "TEMPLATE_ONLY_NOT_APPROVED",
    "approval_decision": "UNSET",
    "allowed_values": ["APPROVE_REPLAY_ONLY", "DENY", "REQUEST_MORE_EVIDENCE"],
    "approver": "",
    "approval_timestamp": "",
    "scope": "candidate_branch_replay_only",
    "selected_report_only_threshold": 0.8,
    "candidate_branch": "candidate/v0.6.0-threshold-0.8-review-only",
    "explicit_locks": {
        "branch_creation_allowed": False,
        "runtime_mutation_allowed": False,
        "classifier_mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "policy_enforced": False
    },
    "required_statement": "I understand this approval, if set to APPROVE_REPLAY_ONLY, authorizes replay only and does not authorize classifier mutation, runtime mutation, calibration application, production use, silicon validation, or product claims.",
    "notes": ""
}

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
        "template_created": 1,
        "approval_present": int(summary["human_approval_present"]),
        "replay_allowed": int(summary["replay_allowed"]),
        "branch_creation_allowed": int(summary["branch_creation_allowed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Human Approval Gate State")
    save("human_approval_gate_state.png")

    decisions = {summary["approval_template_status"]: 1}
    plt.figure(figsize=(8, 4))
    plt.bar(list(decisions.keys()), list(decisions.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Approval Artifact Template Status")
    save("human_approval_template_status.png")

    locks = summary["lock_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(locks.keys()), list(locks.values()))
    plt.ylabel("Count")
    plt.title("Approval Artifact Lock Counts")
    save("human_approval_lock_counts.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.2 Human Approval Artifact Template",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Approval Template Result",
        "",
        f"- Approval template status: `{s['approval_template_status']}`",
        f"- Template path: `{s['approval_template_path']}`",
        f"- Human approval present: `{s['human_approval_present']}`",
        f"- Replay allowed: `{s['replay_allowed']}`",
        f"- Branch creation allowed: `{s['branch_creation_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Template Instructions",
        "",
        s["template_instructions"],
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
    replay = rjson(REPLAY)
    candidate = rjson(CANDIDATE)

    template = dict(APPROVAL_TEMPLATE)
    template["selected_report_only_threshold"] = candidate.get("selected_report_only_threshold", 0.8)
    template["candidate_branch"] = candidate.get("proposed_branch_name", template["candidate_branch"])
    template["generated_at"] = datetime.now(timezone.utc).isoformat()
    template_path = OUT / "human_approval_artifact_template_v0_6_2.json"
    wjson(template_path, template)

    lock_values = template["explicit_locks"]
    false_locks = sum(1 for v in lock_values.values() if v is False)
    true_locks = sum(1 for v in lock_values.values() if v is True)

    summary = {
        "schema": "tau-scaling-human-approval-artifact-template-v0.6.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_candidate_replay": "reports/candidate_replay/latest_candidate_branch_replay_harness.json",
        "input_candidate_branch_gate": "reports/candidate_branch/latest_candidate_branch_gate.json",
        "approval_template_path": rel(template_path),
        "approval_template_status": "TEMPLATE_CREATED__NOT_APPROVED",
        "human_approval_required": True,
        "human_approval_present": False,
        "approval_decision": "UNSET",
        "replay_allowed": False,
        "branch_creation_allowed": False,
        "branch_created": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "lock_counts": {"false_locks": false_locks, "true_locks": true_locks},
        "template_instructions": "To approve replay in a future layer, copy the template to a local approval artifact, set approval_decision to APPROVE_REPLAY_ONLY, fill approver and timestamp, and preserve every explicit lock unless a separate stronger governance artifact exists.",
        "approval_boundary": "This v0.6.2 layer creates a template only. It does not approve replay, create a branch, apply calibration, or mutate classifier behavior.",
        "final_recommendation": "Use this template for a future explicit approval or denial artifact. Do not replay or create branches from the template alone.",
        "boundary": "Human approval artifact templates are local classifier-governance templates. They do not create approval by themselves, do not change classifier behavior, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.3 should add an approval artifact validator that refuses replay unless the approval artifact is explicitly completed.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "human_approval_template_report_v0_6_2.json", summary)
    wjson(OUT / "latest_human_approval_template_report.json", summary)
    wtext(OUT / "human_approval_template_report_v0_6_2.md", report(summary))
    wtext(OUT / "latest_human_approval_template_report.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "approval_template_status": summary["approval_template_status"],
        "approval_template_path": summary["approval_template_path"],
        "human_approval_required": summary["human_approval_required"],
        "human_approval_present": summary["human_approval_present"],
        "approval_decision": summary["approval_decision"],
        "replay_allowed": summary["replay_allowed"],
        "branch_creation_allowed": summary["branch_creation_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/human_approval/latest_human_approval_template_report.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
