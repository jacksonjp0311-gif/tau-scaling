
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "reports" / "review_package" / "latest_review_package.json"
OUT = ROOT / "reports" / "review_signoff"
VIS = ROOT / "visuals" / "review_signoff" / "v0_5_9"

CHECKS = [
    ("evidence_bundle_complete", "All v0.5.2-v0.5.7 evidence inputs are present."),
    ("review_status_ready", "Review package status is READY_FOR_HUMAN_REVIEW_NOT_APPLICATION."),
    ("decision_safe_for_review", "Decision class is SAFE_FOR_REVIEW_NOT_APPLICATION."),
    ("review_allowed_true", "Review is allowed."),
    ("application_allowed_false", "Application is not allowed."),
    ("mutation_allowed_false", "Classifier mutation is not allowed."),
    ("policy_enforced_false", "Policy is not enforced."),
    ("calibration_applied_false", "Calibration is not applied."),
    ("threshold_present", "A selected report-only threshold is present."),
    ("non_claim_boundary_present", "Boundary/non-claim language is present."),
]

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
def rel(p): return str(p.relative_to(ROOT)).replace("\\", "/")

def evaluate(pkg):
    rows = []
    missing = pkg.get("missing_inputs", [])
    for check_id, desc in CHECKS:
        if check_id == "evidence_bundle_complete":
            passed = len(missing) == 0
            observed = f"missing_inputs={len(missing)}"
        elif check_id == "review_status_ready":
            passed = pkg.get("review_package_status") == "READY_FOR_HUMAN_REVIEW_NOT_APPLICATION"
            observed = str(pkg.get("review_package_status"))
        elif check_id == "decision_safe_for_review":
            passed = pkg.get("decision_class") == "SAFE_FOR_REVIEW_NOT_APPLICATION"
            observed = str(pkg.get("decision_class"))
        elif check_id == "review_allowed_true":
            passed = pkg.get("review_allowed") is True
            observed = str(pkg.get("review_allowed"))
        elif check_id == "application_allowed_false":
            passed = pkg.get("application_allowed") is False
            observed = str(pkg.get("application_allowed"))
        elif check_id == "mutation_allowed_false":
            passed = pkg.get("mutation_allowed") is False
            observed = str(pkg.get("mutation_allowed"))
        elif check_id == "policy_enforced_false":
            passed = pkg.get("policy_enforced") is False
            observed = str(pkg.get("policy_enforced"))
        elif check_id == "calibration_applied_false":
            passed = pkg.get("calibration_applied") is False
            observed = str(pkg.get("calibration_applied"))
        elif check_id == "threshold_present":
            passed = pkg.get("selected_report_only_threshold") is not None
            observed = str(pkg.get("selected_report_only_threshold"))
        elif check_id == "non_claim_boundary_present":
            boundary = str(pkg.get("boundary", ""))
            passed = "do not change classifier behavior" in boundary.lower() and "not validate silicon" in boundary.lower()
            observed = "boundary_present" if boundary else "missing_boundary"
        else:
            passed = False
            observed = "unknown"
        rows.append({
            "check_id": check_id,
            "description": desc,
            "passed": bool(passed),
            "observed": observed,
            "required_for_signoff": True,
        })
    return rows

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

    counts = summary["check_counts"]
    plt.figure(figsize=(7,4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.ylabel("Check count")
    plt.title("Review Signoff Checklist Results")
    save("review_signoff_check_counts.png")

    locks = {
        "review_allowed": int(summary["review_allowed"]),
        "application_allowed": int(summary["application_allowed"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
        "calibration_applied": int(summary["calibration_applied"]),
    }
    plt.figure(figsize=(8,4))
    plt.bar(list(locks.keys()), list(locks.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Review Signoff Lock States")
    save("review_signoff_lock_states.png")

    classes = summary["signoff_class_counts"]
    plt.figure(figsize=(8,4))
    plt.bar(list(classes.keys()), list(classes.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Count")
    plt.title("Signoff Classification")
    save("review_signoff_class_counts.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.5.9 Review Checklist and Signoff Gate",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Signoff Result",
        "",
        f"- Signoff status: `{s['signoff_status']}`",
        f"- Checklist pass count: `{s['check_pass_count']}`",
        f"- Checklist fail count: `{s['check_fail_count']}`",
        f"- Review allowed: `{s['review_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Calibration applied: `{s['calibration_applied']}`",
        f"- Final recommendation: `{s['final_recommendation']}`",
        "",
        "## Checklist",
        "",
        "| Check | Passed | Observed | Description |",
        "|---|---|---|---|",
    ]
    for row in s["checklist"]:
        lines.append(f"| `{row['check_id']}` | `{row['passed']}` | `{row['observed']}` | {row['description']} |")
    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    pkg = rjson(PKG)
    checklist = evaluate(pkg)
    pass_count = sum(1 for r in checklist if r["passed"])
    fail_count = len(checklist) - pass_count
    signoff_status = "REVIEW_SIGNOFF_READY_NOT_APPLICATION" if fail_count == 0 else "SIGNOFF_BLOCKED"
    summary = {
        "schema": "tau-scaling-review-checklist-signoff-gate-v0.5.9",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_review_package": "reports/review_package/latest_review_package.json",
        "signoff_status": signoff_status,
        "checklist": checklist,
        "check_pass_count": pass_count,
        "check_fail_count": fail_count,
        "check_counts": {"passed": pass_count, "failed": fail_count},
        "signoff_class_counts": {signoff_status: 1},
        "selected_report_only_threshold": pkg.get("selected_report_only_threshold"),
        "review_allowed": signoff_status == "REVIEW_SIGNOFF_READY_NOT_APPLICATION",
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "final_recommendation": "Human review may begin. Application and mutation remain blocked." if fail_count == 0 else "Repair signoff checklist failures before review.",
        "boundary": "Review signoff gates are local classifier-governance signoff artifacts. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.0 should create a human-approved candidate branch only after explicit external signoff, still non-mutating by default.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "review_signoff_gate_v0_5_9.json", summary)
    wjson(OUT / "latest_review_signoff_gate.json", summary)
    wtext(OUT / "review_signoff_gate_v0_5_9.md", report(summary))
    wtext(OUT / "latest_review_signoff_gate.md", report(summary))
    print(json.dumps({
        "schema": summary["schema"],
        "signoff_status": summary["signoff_status"],
        "check_pass_count": summary["check_pass_count"],
        "check_fail_count": summary["check_fail_count"],
        "review_allowed": summary["review_allowed"],
        "application_allowed": summary["application_allowed"],
        "mutation_allowed": summary["mutation_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/review_signoff/latest_review_signoff_gate.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
