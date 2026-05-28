
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "reports" / "calibration_plan" / "latest_disabled_calibration_plan.json"
NEG = ROOT / "reports" / "negative_controls" / "latest_support_aware_negative_controls.json"
OUT = ROOT / "reports" / "calibration_counterfactuals"
VIS = ROOT / "visuals" / "calibration_counterfactuals" / "v0_5_6"

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def simulate(control, threshold):
    diag = control.get("current_diagnostic_average")
    high_support = isinstance(diag, (int, float)) and diag >= threshold
    current_behavior = control.get("observed_report_only_behavior")
    proposed_behavior = "retain_blocked_no_downgrade" if high_support else "eligible_for_review_not_enforcement"
    support_pass_preserved = bool(control.get("negative_control_passed")) and proposed_behavior == "retain_blocked_no_downgrade"
    drift = current_behavior != proposed_behavior
    return {
        "control_id": control.get("control_id"),
        "gate_pair": control.get("gate_pair"),
        "diagnostic_average": diag,
        "selected_threshold": threshold,
        "current_behavior": current_behavior,
        "proposed_report_only_behavior": proposed_behavior,
        "counterfactual_drift": drift,
        "support_pass_preserved": support_pass_preserved,
        "counterfactual_status": "safe_report_only_candidate" if support_pass_preserved else "rejected_support_control_violation",
    }

def charts(summary):
    paths=[]
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        wtext(OUT/"chart_generation_skipped.txt", str(e))
        return paths
    VIS.mkdir(parents=True, exist_ok=True)
    def save(name):
        p=VIS/name
        plt.tight_layout()
        plt.savefig(p,dpi=180,bbox_inches="tight")
        plt.close()
        paths.append(str(p.relative_to(ROOT)).replace("\\","/"))

    counts=summary["status_counts"]
    plt.figure(figsize=(8,4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Counterfactual count")
    plt.title("Calibration Counterfactual Status")
    save("counterfactual_status_counts.png")

    drift=summary["drift_counts"]
    plt.figure(figsize=(8,4))
    plt.bar(list(drift.keys()), list(drift.values()))
    plt.ylabel("Count")
    plt.title("Current vs Proposed Drift")
    save("counterfactual_drift_counts.png")

    vals=[r["diagnostic_average"] for r in summary["counterfactual_rows"] if isinstance(r.get("diagnostic_average"), (int,float))]
    plt.figure(figsize=(8,4))
    plt.bar([str(i+1) for i in range(len(vals))], vals)
    plt.axhline(summary["selected_report_only_threshold"], linestyle="--")
    plt.xlabel("Counterfactual")
    plt.ylabel("Diagnostic average")
    plt.title("Counterfactual Diagnostic Support vs Threshold")
    save("counterfactual_support_threshold.png")
    return paths

def report(summary):
    lines=[
        "# Tau Scaling v0.5.6 Calibration Counterfactuals",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Selected report-only threshold: `{summary['selected_report_only_threshold']}`",
        f"- Counterfactual count: `{summary['counterfactual_count']}`",
        f"- Safe report-only candidates: `{summary['safe_candidate_count']}`",
        f"- Rejected counterfactuals: `{summary['rejected_count']}`",
        f"- Drift count: `{summary['counterfactual_drift_count']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        f"- Calibration applied: `{summary['calibration_applied']}`",
        "",
        "## Counterfactual Rows",
        "",
        "| Control | Gate pair | Diagnostic | Current behavior | Proposed behavior | Drift | Support preserved | Status |",
        "|---|---|---:|---|---|---|---|---|",
    ]
    for r in summary["counterfactual_rows"]:
        lines.append(
            f"| `{r['control_id']}` | `{r['gate_pair']}` | `{r['diagnostic_average']}` | "
            f"`{r['current_behavior']}` | `{r['proposed_report_only_behavior']}` | `{r['counterfactual_drift']}` | "
            f"`{r['support_pass_preserved']}` | `{r['counterfactual_status']}` |"
        )
    lines += ["", "## Charts", ""]
    for p in summary["chart_paths"]:
        rel=os.path.relpath(ROOT/p, OUT).replace("\\","/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    plan=rjson(PLAN)
    neg=rjson(NEG)
    threshold=plan.get("selected_report_only_threshold")
    controls=neg.get("negative_controls", [])
    rows=[simulate(c, threshold) for c in controls]

    status=Counter(r["counterfactual_status"] for r in rows)
    drift=Counter("drift" if r["counterfactual_drift"] else "no_drift" for r in rows)
    rejected=status.get("rejected_support_control_violation", 0)
    safe=status.get("safe_report_only_candidate", 0)
    final = "counterfactual_candidate_safe_for_review_not_application" if rejected == 0 else "do_not_review_calibration_candidate__support_violation"

    summary={
        "schema":"tau-scaling-calibration-counterfactuals-v0.5.6",
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "input_calibration_plan":"reports/calibration_plan/latest_disabled_calibration_plan.json",
        "input_negative_controls":"reports/negative_controls/latest_support_aware_negative_controls.json",
        "selected_report_only_threshold":threshold,
        "counterfactual_count":len(rows),
        "safe_candidate_count":safe,
        "rejected_count":rejected,
        "counterfactual_drift_count":drift.get("drift",0),
        "status_counts":dict(status),
        "drift_counts":dict(drift),
        "counterfactual_rows":rows,
        "mutation_allowed":False,
        "policy_enforced":False,
        "calibration_applied":False,
        "final_recommendation":final,
        "boundary":"Calibration counterfactuals are local report-only classifier-governance simulations. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation":"v0.5.7 should produce a counterfactual decision record before any classifier mutation is discussed.",
    }
    summary["chart_paths"]=charts(summary)
    wjson(OUT/"calibration_counterfactuals_v0_5_6.json", summary)
    wjson(OUT/"latest_calibration_counterfactuals.json", summary)
    wtext(OUT/"calibration_counterfactuals_v0_5_6.md", report(summary))
    wtext(OUT/"latest_calibration_counterfactuals.md", report(summary))
    print(json.dumps({
        "schema":summary["schema"],
        "selected_report_only_threshold":summary["selected_report_only_threshold"],
        "counterfactual_count":summary["counterfactual_count"],
        "safe_candidate_count":summary["safe_candidate_count"],
        "rejected_count":summary["rejected_count"],
        "counterfactual_drift_count":summary["counterfactual_drift_count"],
        "final_recommendation":summary["final_recommendation"],
        "mutation_allowed":summary["mutation_allowed"],
        "policy_enforced":summary["policy_enforced"],
        "calibration_applied":summary["calibration_applied"],
        "chart_count":len(summary["chart_paths"]),
        "report":"reports/calibration_counterfactuals/latest_calibration_counterfactuals.md",
    }, indent=2, sort_keys=True))
if __name__=="__main__":
    main()
