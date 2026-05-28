
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

INPUTS = {
    "cause_decomposition": ROOT / "reports" / "over_penalty_causes" / "latest_over_penalty_cause_decomposition.json",
    "remediation_plan": ROOT / "reports" / "remediation_plan" / "latest_cause_specific_remediation_plan.json",
    "negative_controls": ROOT / "reports" / "negative_controls" / "latest_support_aware_negative_controls.json",
    "calibration_plan": ROOT / "reports" / "calibration_plan" / "latest_disabled_calibration_plan.json",
    "calibration_counterfactuals": ROOT / "reports" / "calibration_counterfactuals" / "latest_calibration_counterfactuals.json",
    "counterfactual_decision": ROOT / "reports" / "counterfactual_decision" / "latest_counterfactual_decision_record.json",
}
OUT = ROOT / "reports" / "review_package"
VIS = ROOT / "visuals" / "review_package" / "v0_5_8"

def rjson(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def wjson(p: Path, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")

def load_inputs():
    loaded = {}
    missing = []
    for k, p in INPUTS.items():
        if p.exists():
            loaded[k] = rjson(p)
        else:
            missing.append(rel(p))
    return loaded, missing

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

    stages = summary["stage_summary"]
    labels = [s["stage"] for s in stages]
    counts = [s["primary_count"] for s in stages]
    plt.figure(figsize=(10, 4))
    plt.bar(labels, counts)
    plt.xticks(rotation=35, ha="right")
    plt.ylabel("Primary count")
    plt.title("Review Package Evidence Chain")
    save("review_package_evidence_chain.png")

    gates = {
        "review_allowed": int(bool(summary["review_allowed"])),
        "application_allowed": int(bool(summary["application_allowed"])),
        "mutation_allowed": int(bool(summary["mutation_allowed"])),
        "calibration_applied": int(bool(summary["calibration_applied"])),
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Review vs Application Locks")
    save("review_package_lock_states.png")

    decision = summary["decision_class_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(decision.keys()), list(decision.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Review Package Decision Classification")
    save("review_package_decision_counts.png")

    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.5.8 Review Package and Evidence Bundle",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Review Decision",
        "",
        f"- Review package status: `{s['review_package_status']}`",
        f"- Decision class: `{s['decision_class']}`",
        f"- Selected report-only threshold: `{s['selected_report_only_threshold']}`",
        f"- Review allowed: `{s['review_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Policy enforced: `{s['policy_enforced']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        "",
        "## Evidence Chain",
        "",
        "| Stage | Source | Primary metric | Count | Status |",
        "|---|---|---|---:|---|",
    ]
    for st in s["stage_summary"]:
        lines.append(f"| {st['stage']} | `{st['source']}` | `{st['primary_metric']}` | {st['primary_count']} | `{st['status']}` |")

    lines += [
        "",
        "## Bundle Files",
        "",
        "| Bundle Item | Path |",
        "|---|---|",
    ]
    for item in s["bundle_items"]:
        lines.append(f"| {item['name']} | `{item['path']}` |")

    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")

    lines += [
        "## Final Recommendation",
        "",
        s["final_recommendation"],
        "",
        "## Boundary",
        "",
        s["boundary"],
        "",
    ]
    return "\n".join(lines)

def main():
    data, missing = load_inputs()

    cause = data.get("cause_decomposition", {})
    remediation = data.get("remediation_plan", {})
    negative = data.get("negative_controls", {})
    cal_plan = data.get("calibration_plan", {})
    counter = data.get("calibration_counterfactuals", {})
    decision = data.get("counterfactual_decision", {})

    decision_class = decision.get("decision", "UNKNOWN")
    review_allowed = bool(decision.get("review_allowed", False))
    application_allowed = False
    mutation_allowed = False
    policy_enforced = False
    calibration_applied = False

    stages = [
        {
            "stage": "cause_decomposition",
            "source": rel(INPUTS["cause_decomposition"]),
            "primary_metric": "cause_card_count",
            "primary_count": int(cause.get("cause_card_count", 0) or 0),
            "status": "loaded" if "cause_decomposition" in data else "missing",
        },
        {
            "stage": "remediation_plan",
            "source": rel(INPUTS["remediation_plan"]),
            "primary_metric": "remediation_task_count",
            "primary_count": int(remediation.get("remediation_task_count", 0) or 0),
            "status": "loaded" if "remediation_plan" in data else "missing",
        },
        {
            "stage": "negative_controls",
            "source": rel(INPUTS["negative_controls"]),
            "primary_metric": "passed_control_count",
            "primary_count": int(negative.get("passed_control_count", 0) or 0),
            "status": "loaded" if "negative_controls" in data else "missing",
        },
        {
            "stage": "calibration_plan",
            "source": rel(INPUTS["calibration_plan"]),
            "primary_metric": "admissible_threshold_count",
            "primary_count": int(cal_plan.get("admissible_threshold_count", 0) or 0),
            "status": "loaded" if "calibration_plan" in data else "missing",
        },
        {
            "stage": "calibration_counterfactuals",
            "source": rel(INPUTS["calibration_counterfactuals"]),
            "primary_metric": "safe_candidate_count",
            "primary_count": int(counter.get("safe_candidate_count", 0) or 0),
            "status": "loaded" if "calibration_counterfactuals" in data else "missing",
        },
        {
            "stage": "counterfactual_decision",
            "source": rel(INPUTS["counterfactual_decision"]),
            "primary_metric": "review_allowed",
            "primary_count": int(review_allowed),
            "status": decision_class,
        },
    ]

    complete = not missing and review_allowed and not application_allowed and not mutation_allowed and not calibration_applied
    status = "READY_FOR_HUMAN_REVIEW_NOT_APPLICATION" if complete else "INCOMPLETE_OR_NOT_REVIEW_READY"

    bundle_items = [
        {"name": k, "path": rel(p), "exists": p.exists()}
        for k, p in INPUTS.items()
    ]

    summary = {
        "schema": "tau-scaling-review-package-evidence-bundle-v0.5.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "review_package_status": status,
        "missing_inputs": missing,
        "selected_report_only_threshold": decision.get("selected_report_only_threshold", counter.get("selected_report_only_threshold")),
        "decision_class": decision_class,
        "decision_class_counts": {decision_class: 1},
        "review_allowed": review_allowed,
        "application_allowed": application_allowed,
        "mutation_allowed": mutation_allowed,
        "policy_enforced": policy_enforced,
        "calibration_applied": calibration_applied,
        "stage_summary": stages,
        "bundle_items": bundle_items,
        "source_decision_record": rel(INPUTS["counterfactual_decision"]),
        "final_recommendation": "Send this package to review. Do not apply calibration, mutate classifier behavior, or enforce policy from this package alone." if complete else "Repair missing or non-review-ready evidence before packaging.",
        "boundary": "Review packages are local classifier-governance evidence bundles. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.9 should create a review checklist / signoff gate, still with mutation disabled.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "review_package_v0_5_8.json", summary)
    wjson(OUT / "latest_review_package.json", summary)
    wtext(OUT / "review_package_v0_5_8.md", report(summary))
    wtext(OUT / "latest_review_package.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "review_package_status": summary["review_package_status"],
        "decision_class": summary["decision_class"],
        "selected_report_only_threshold": summary["selected_report_only_threshold"],
        "review_allowed": summary["review_allowed"],
        "application_allowed": summary["application_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "missing_input_count": len(summary["missing_inputs"]),
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/review_package/latest_review_package.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
