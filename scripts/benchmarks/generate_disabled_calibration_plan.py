
from __future__ import annotations
import json, os, math
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEG = ROOT / "reports" / "negative_controls" / "latest_support_aware_negative_controls.json"
OUT = ROOT / "reports" / "calibration_plan"
VIS = ROOT / "visuals" / "calibration_plan" / "v0_5_5"

CANDIDATE_THRESHOLDS = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def evaluate_threshold(threshold, controls):
    retained = 0
    violated = 0
    margins = []
    rows = []
    for c in controls:
        diag = c.get("current_diagnostic_average")
        high = isinstance(diag, (int, float)) and diag >= threshold
        expected_retain = bool(c.get("negative_control_passed")) and bool(c.get("high_support_detected"))
        # The calibration plan is acceptable only if every already-passing high-support
        # control remains retained under the candidate threshold.
        preserves = (not expected_retain) or high
        if expected_retain and preserves:
            retained += 1
        if expected_retain and not preserves:
            violated += 1
        margin = None if not isinstance(diag, (int, float)) else round(diag - threshold, 6)
        if margin is not None:
            margins.append(margin)
        rows.append({
            "control_id": c.get("control_id"),
            "gate_pair": c.get("gate_pair"),
            "diagnostic_average": diag,
            "threshold": threshold,
            "expected_retain": expected_retain,
            "preserves_retention": preserves,
            "margin": margin,
        })
    return {
        "threshold": threshold,
        "retained_control_count": retained,
        "violation_count": violated,
        "minimum_margin": min(margins) if margins else None,
        "rows": rows,
        "candidate_status": "admissible_report_only" if violated == 0 else "rejected_retention_violation",
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
        paths.append(str(p.relative_to(ROOT)).replace("\\", "/"))

    results = summary["threshold_results"]
    labels = [str(r["threshold"]) for r in results]

    plt.figure(figsize=(9,4))
    plt.bar(labels, [r["retained_control_count"] for r in results])
    plt.xlabel("Candidate threshold")
    plt.ylabel("Retained controls")
    plt.title("High-Support Retention by Candidate Threshold")
    save("calibration_retention_by_threshold.png")

    plt.figure(figsize=(9,4))
    plt.bar(labels, [r["violation_count"] for r in results])
    plt.xlabel("Candidate threshold")
    plt.ylabel("Retention violations")
    plt.title("Retention Violations by Candidate Threshold")
    save("calibration_violation_by_threshold.png")

    margins = [r["minimum_margin"] if r["minimum_margin"] is not None else 0 for r in results]
    plt.figure(figsize=(9,4))
    plt.bar(labels, margins)
    plt.xlabel("Candidate threshold")
    plt.ylabel("Minimum support margin")
    plt.title("Minimum Support Margin by Threshold")
    save("calibration_minimum_margin.png")

    return paths

def report(summary):
    lines = [
        "# Tau Scaling v0.5.5 Disabled Calibration Plan",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Source negative controls: `{summary['source_negative_control_count']}`",
        f"- Passing source controls: `{summary['source_passed_control_count']}`",
        f"- Candidate thresholds: `{summary['candidate_threshold_count']}`",
        f"- Admissible report-only thresholds: `{summary['admissible_threshold_count']}`",
        f"- Rejected thresholds: `{summary['rejected_threshold_count']}`",
        f"- Selected report-only threshold: `{summary['selected_report_only_threshold']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Threshold Results",
        "",
        "| Threshold | Retained controls | Violations | Minimum margin | Status |",
        "|---:|---:|---:|---:|---|",
    ]
    for r in summary["threshold_results"]:
        lines.append(f"| {r['threshold']} | {r['retained_control_count']} | {r['violation_count']} | {r['minimum_margin']} | `{r['candidate_status']}` |")
    lines += ["", "## Charts", ""]
    for p in summary["chart_paths"]:
        rel = os.path.relpath(ROOT / p, OUT).replace("\\", "/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    neg = rjson(NEG)
    controls = neg.get("negative_controls", [])
    passed = [c for c in controls if c.get("negative_control_passed")]

    results = [evaluate_threshold(t, controls) for t in CANDIDATE_THRESHOLDS]
    admissible = [r for r in results if r["candidate_status"] == "admissible_report_only"]

    # Conservative selection: among admissible thresholds, use the highest threshold that
    # preserves all passing support controls. If none, no calibration candidate is allowed.
    selected = admissible[-1]["threshold"] if admissible else None
    final = "draft_report_only_calibration_candidate_preserving_support_controls" if selected is not None else "do_not_calibrate__support_retention_violation"

    summary = {
        "schema": "tau-scaling-disabled-calibration-plan-v0.5.5",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_negative_controls": "reports/negative_controls/latest_support_aware_negative_controls.json",
        "source_negative_control_count": len(controls),
        "source_passed_control_count": len(passed),
        "candidate_threshold_count": len(CANDIDATE_THRESHOLDS),
        "admissible_threshold_count": len(admissible),
        "rejected_threshold_count": len(results) - len(admissible),
        "selected_report_only_threshold": selected,
        "threshold_results": results,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "final_recommendation": final,
        "boundary": "Disabled calibration planning is local report-only classifier-governance analysis. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.6 should run calibration counterfactuals without applying classifier mutation.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "disabled_calibration_plan_v0_5_5.json", summary)
    wjson(OUT / "latest_disabled_calibration_plan.json", summary)
    wtext(OUT / "disabled_calibration_plan_v0_5_5.md", report(summary))
    wtext(OUT / "latest_disabled_calibration_plan.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "source_negative_control_count": summary["source_negative_control_count"],
        "source_passed_control_count": summary["source_passed_control_count"],
        "candidate_threshold_count": summary["candidate_threshold_count"],
        "admissible_threshold_count": summary["admissible_threshold_count"],
        "rejected_threshold_count": summary["rejected_threshold_count"],
        "selected_report_only_threshold": summary["selected_report_only_threshold"],
        "final_recommendation": summary["final_recommendation"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/calibration_plan/latest_disabled_calibration_plan.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
