
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTER = ROOT / "reports" / "calibration_counterfactuals" / "latest_calibration_counterfactuals.json"
OUT = ROOT / "reports" / "counterfactual_decision"
VIS = ROOT / "visuals" / "counterfactual_decision" / "v0_5_7"

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def charts(s):
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

    data = s["decision_counts"]
    plt.figure(figsize=(8,4))
    plt.bar(list(data.keys()), list(data.values()))
    plt.xticks(rotation=20, ha="right")
    plt.title("Counterfactual Decision Classification")
    plt.ylabel("Count")
    save("counterfactual_decision_counts.png")

    metrics = {
        "safe": s["safe_candidate_count"],
        "rejected": s["rejected_count"],
        "drift": s["counterfactual_drift_count"],
        "total": s["counterfactual_count"],
    }
    plt.figure(figsize=(8,4))
    plt.bar(list(metrics.keys()), list(metrics.values()))
    plt.title("Counterfactual Evidence Metrics")
    plt.ylabel("Count")
    save("counterfactual_decision_metrics.png")

    status = s.get("source_status_counts", {})
    plt.figure(figsize=(8,4))
    plt.bar(list(status.keys()), list(status.values()))
    plt.xticks(rotation=20, ha="right")
    plt.title("Source Counterfactual Status Counts")
    plt.ylabel("Rows")
    save("counterfactual_source_status_counts.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.5.7 Counterfactual Decision Record",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Decision",
        "",
        f"- Decision: `{s['decision']}`",
        f"- Selected report-only threshold: `{s['selected_report_only_threshold']}`",
        f"- Reason: {s['decision_reason']}",
        f"- Next step: {s['next_step']}",
        "",
        "## Evidence Summary",
        "",
        f"- Counterfactual count: `{s['counterfactual_count']}`",
        f"- Safe candidates: `{s['safe_candidate_count']}`",
        f"- Rejected candidates: `{s['rejected_count']}`",
        f"- Drift count: `{s['counterfactual_drift_count']}`",
        f"- Review allowed: `{s['review_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Charts",
        "",
    ]
    for p in s["chart_paths"]:
        rel = os.path.relpath(ROOT / p, OUT).replace("\\", "/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    c = rjson(COUNTER)
    total = int(c.get("counterfactual_count", 0) or 0)
    safe = int(c.get("safe_candidate_count", 0) or 0)
    rejected = int(c.get("rejected_count", 0) or 0)
    drift = int(c.get("counterfactual_drift_count", 0) or 0)

    if total > 0 and safe == total and rejected == 0 and drift == 0:
        decision = "SAFE_FOR_REVIEW_NOT_APPLICATION"
        reason = "All counterfactual rows preserved support controls with zero drift and zero rejected rows."
        review = True
    elif rejected > 0:
        decision = "REJECTED_SUPPORT_CONTROL_VIOLATION"
        reason = "At least one counterfactual violated support-aware retention."
        review = False
    elif drift > 0:
        decision = "NEEDS_MORE_CONTROLS"
        reason = "Counterfactual drift was observed."
        review = False
    else:
        decision = "INSUFFICIENT_COUNTERFACTUAL_EVIDENCE"
        reason = "Counterfactual evidence was incomplete."
        review = False

    s = {
        "schema": "tau-scaling-counterfactual-decision-record-v0.5.7",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_counterfactuals": "reports/calibration_counterfactuals/latest_calibration_counterfactuals.json",
        "selected_report_only_threshold": c.get("selected_report_only_threshold"),
        "counterfactual_count": total,
        "safe_candidate_count": safe,
        "rejected_count": rejected,
        "counterfactual_drift_count": drift,
        "source_status_counts": c.get("status_counts", {}),
        "decision": decision,
        "decision_reason": reason,
        "next_step": "Bundle evidence for review; do not apply classifier mutation." if review else "Do not advance candidate.",
        "decision_counts": {decision: 1},
        "review_allowed": review,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "final_recommendation": "review_candidate_without_application" if review else "do_not_review_candidate_yet",
        "boundary": "Counterfactual decision records are local classifier-governance decision artifacts. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.8 should produce a review package with evidence bundle and mutation still disabled.",
    }
    s["chart_paths"] = charts(s)
    wjson(OUT / "counterfactual_decision_record_v0_5_7.json", s)
    wjson(OUT / "latest_counterfactual_decision_record.json", s)
    wtext(OUT / "counterfactual_decision_record_v0_5_7.md", report(s))
    wtext(OUT / "latest_counterfactual_decision_record.md", report(s))
    print(json.dumps({
        "schema": s["schema"],
        "selected_report_only_threshold": s["selected_report_only_threshold"],
        "decision": s["decision"],
        "review_allowed": s["review_allowed"],
        "application_allowed": s["application_allowed"],
        "mutation_allowed": s["mutation_allowed"],
        "calibration_applied": s["calibration_applied"],
        "final_recommendation": s["final_recommendation"],
        "chart_count": len(s["chart_paths"]),
        "report": "reports/counterfactual_decision/latest_counterfactual_decision_record.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
