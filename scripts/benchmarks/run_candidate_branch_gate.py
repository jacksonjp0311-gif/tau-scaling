
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIGNOFF = ROOT / "reports" / "review_signoff" / "latest_review_signoff_gate.json"
REVIEW = ROOT / "reports" / "review_package" / "latest_review_package.json"
OUT = ROOT / "reports" / "candidate_branch"
VIS = ROOT / "visuals" / "candidate_branch" / "v0_6_0"

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
def rel(p): return str(p.relative_to(ROOT)).replace("\\", "/")

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

    gate = {
        "signoff_ready": int(summary["signoff_ready"]),
        "branch_proposal_allowed": int(summary["branch_proposal_allowed"]),
        "branch_created": int(summary["branch_created"]),
        "application_allowed": int(summary["application_allowed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate.keys()), list(gate.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Candidate Branch Gate State")
    save("candidate_branch_gate_state.png")

    checks = {
        "signoff_pass": int(summary["signoff_check_pass_count"]),
        "signoff_fail": int(summary["signoff_check_fail_count"]),
    }
    plt.figure(figsize=(7, 4))
    plt.bar(list(checks.keys()), list(checks.values()))
    plt.ylabel("Check count")
    plt.title("Signoff Checklist Counts")
    save("candidate_branch_signoff_counts.png")

    classes = {summary["candidate_branch_status"]: 1}
    plt.figure(figsize=(9, 4))
    plt.bar(list(classes.keys()), list(classes.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Candidate Branch Status")
    save("candidate_branch_status.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.0 Human-Approved Candidate Branch Gate",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Gate Result",
        "",
        f"- Candidate branch status: `{s['candidate_branch_status']}`",
        f"- Selected report-only threshold: `{s['selected_report_only_threshold']}`",
        f"- Signoff ready: `{s['signoff_ready']}`",
        f"- Branch proposal allowed: `{s['branch_proposal_allowed']}`",
        f"- Branch created: `{s['branch_created']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Human Approval Requirement",
        "",
        s["human_approval_requirement"],
        "",
        "## Candidate Branch Proposal",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Proposed branch name | `{s['proposed_branch_name']}` |",
        f"| Source signoff | `{s['input_review_signoff']}` |",
        f"| Source review package | `{s['input_review_package']}` |",
        f"| Default branch creation | `{s['branch_created']}` |",
        f"| Runtime behavior changed | `false` |",
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
    signoff = rjson(SIGNOFF)
    review = rjson(REVIEW)

    signoff_ready = signoff.get("signoff_status") == "REVIEW_SIGNOFF_READY_NOT_APPLICATION"
    pass_count = int(signoff.get("check_pass_count", 0) or 0)
    fail_count = int(signoff.get("check_fail_count", 0) or 0)
    threshold = signoff.get("selected_report_only_threshold", review.get("selected_report_only_threshold"))

    status = "CANDIDATE_BRANCH_PROPOSAL_READY__HUMAN_APPROVAL_REQUIRED" if signoff_ready and fail_count == 0 else "CANDIDATE_BRANCH_BLOCKED"

    summary = {
        "schema": "tau-scaling-human-approved-candidate-branch-gate-v0.6.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_review_signoff": "reports/review_signoff/latest_review_signoff_gate.json",
        "input_review_package": "reports/review_package/latest_review_package.json",
        "candidate_branch_status": status,
        "selected_report_only_threshold": threshold,
        "signoff_ready": bool(signoff_ready),
        "signoff_check_pass_count": pass_count,
        "signoff_check_fail_count": fail_count,
        "branch_proposal_allowed": bool(signoff_ready and fail_count == 0),
        "branch_created": False,
        "proposed_branch_name": "candidate/v0.6.0-threshold-0.8-review-only",
        "human_approval_required": True,
        "human_approval_present": False,
        "human_approval_requirement": "A human approval artifact must be added before creating any candidate branch or implementation pathway. This gate only prepares a proposal.",
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "final_recommendation": "Prepare human review disposition. Do not create branch, apply calibration, or mutate classifier behavior from this report alone.",
        "boundary": "Human-approved candidate branch gates are local classifier-governance proposal artifacts. They do not create a branch by default, do not change classifier behavior, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.1 should replay a candidate branch only after explicit human approval artifact exists.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "candidate_branch_gate_v0_6_0.json", summary)
    wjson(OUT / "latest_candidate_branch_gate.json", summary)
    wtext(OUT / "candidate_branch_gate_v0_6_0.md", report(summary))
    wtext(OUT / "latest_candidate_branch_gate.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "candidate_branch_status": summary["candidate_branch_status"],
        "selected_report_only_threshold": summary["selected_report_only_threshold"],
        "branch_proposal_allowed": summary["branch_proposal_allowed"],
        "human_approval_required": summary["human_approval_required"],
        "human_approval_present": summary["human_approval_present"],
        "branch_created": summary["branch_created"],
        "application_allowed": summary["application_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/candidate_branch/latest_candidate_branch_gate.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
