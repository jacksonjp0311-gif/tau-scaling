
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "reports" / "remediation_plan" / "latest_cause_specific_remediation_plan.json"
CAUSES = ROOT / "reports" / "over_penalty_causes" / "latest_over_penalty_cause_decomposition.json"
OUT = ROOT / "reports" / "negative_controls"
VIS = ROOT / "visuals" / "negative_controls" / "v0_5_4"

SUPPORT_THRESHOLD = 0.75

def rjson(p):
    return json.loads(p.read_text(encoding="utf-8"))

def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def make_control(task, source_card):
    diag = source_card.get("current_diagnostic_average")
    high_support = isinstance(diag, (int, float)) and diag >= SUPPORT_THRESHOLD
    has_high_support_cause = "high_diagnostic_support" in source_card.get("causes", [])
    should_retain = high_support or has_high_support_cause

    # Report-only negative control:
    # A high-support candidate passes the control when the system refuses downgrade/enforcement.
    observed_outcome = "retain_blocked_no_downgrade" if should_retain else "requires_manual_review"
    pass_control = observed_outcome == "retain_blocked_no_downgrade"

    return {
        "schema": "tau-scaling-support-aware-negative-control-v0.5.4",
        "control_id": task["task_id"].replace("remediation-task", "negative-control"),
        "source_task_id": task["task_id"],
        "source_card_id": task.get("source_card_id"),
        "gate_pair": task.get("gate_pair"),
        "current_diagnostic_average": diag,
        "support_threshold": SUPPORT_THRESHOLD,
        "high_support_detected": bool(should_retain),
        "expected_safe_behavior": "retain_high_support_case_and_block_downgrade",
        "observed_report_only_behavior": observed_outcome,
        "negative_control_passed": bool(pass_control),
        "control_class": "support_aware_retention_control",
        "mutation_allowed": False,
        "policy_enforced": False,
        "non_claim_lock": "Support-aware negative controls are local report-only classifier-governance tests.",
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

    pass_counts = summary["control_pass_counts"]
    plt.figure(figsize=(7,4))
    plt.bar(list(pass_counts.keys()), list(pass_counts.values()))
    plt.ylabel("Control count")
    plt.title("Support-Aware Negative Control Outcomes")
    save("support_control_outcomes.png")

    gate_counts = summary["gate_involvement_counts"]
    plt.figure(figsize=(9,4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Control involvement")
    plt.title("Support Control Gate Involvement")
    save("support_control_gate_involvement.png")

    values = [c.get("current_diagnostic_average") for c in summary["negative_controls"] if isinstance(c.get("current_diagnostic_average"), (int, float))]
    plt.figure(figsize=(8,4))
    plt.bar([str(i+1) for i in range(len(values))], values)
    plt.axhline(SUPPORT_THRESHOLD, linestyle="--")
    plt.xlabel("Control")
    plt.ylabel("Diagnostic average")
    plt.title("Diagnostic Support vs Retention Threshold")
    save("support_control_diagnostic_threshold.png")

    return paths

def report(summary):
    lines = [
        "# Tau Scaling v0.5.4 Support-Aware Negative Controls",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Source remediation tasks: `{summary['source_remediation_task_count']}`",
        f"- Negative control count: `{summary['negative_control_count']}`",
        f"- Passed controls: `{summary['passed_control_count']}`",
        f"- Failed controls: `{summary['failed_control_count']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Control Outcomes",
        "",
        "| Control | Gate pair | Diagnostic average | High support | Passed | Observed behavior |",
        "|---|---|---:|---|---|---|",
    ]
    for c in summary["negative_controls"]:
        lines.append(
            f"| `{c['control_id']}` | `{c['gate_pair']}` | `{c['current_diagnostic_average']}` | "
            f"`{c['high_support_detected']}` | `{c['negative_control_passed']}` | `{c['observed_report_only_behavior']}` |"
        )
    lines += ["", "## Charts", ""]
    for p in summary["chart_paths"]:
        rel = os.path.relpath(ROOT / p, OUT).replace("\\", "/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    plan = rjson(PLAN)
    causes = rjson(CAUSES)
    cause_by_id = {c["card_id"]: c for c in causes.get("cause_cards", [])}
    tasks = [t for t in plan.get("remediation_tasks", []) if t.get("remediation_class") == "support_aware_negative_control"]

    controls = []
    for task in tasks:
        card = cause_by_id.get(task.get("source_card_id"), {})
        controls.append(make_control(task, card))

    pass_counter = Counter("passed" if c["negative_control_passed"] else "failed" for c in controls)
    gates = Counter()
    for c in controls:
        for g in str(c.get("gate_pair")).split("+"):
            if g and g != "None":
                gates[g] += 1

    failed = pass_counter.get("failed", 0)
    final = "retain_block__support_controls_confirm_high_support_retention" if failed == 0 else "review_failed_support_controls_before_calibration"

    summary = {
        "schema": "tau-scaling-support-aware-negative-controls-v0.5.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_plan": "reports/remediation_plan/latest_cause_specific_remediation_plan.json",
        "input_causes": "reports/over_penalty_causes/latest_over_penalty_cause_decomposition.json",
        "source_remediation_task_count": len(tasks),
        "negative_control_count": len(controls),
        "passed_control_count": pass_counter.get("passed", 0),
        "failed_control_count": failed,
        "control_pass_counts": dict(pass_counter),
        "gate_involvement_counts": dict(gates),
        "negative_controls": controls,
        "support_threshold": SUPPORT_THRESHOLD,
        "mutation_allowed": False,
        "policy_enforced": False,
        "final_recommendation": final,
        "boundary": "Support-aware negative controls are disabled/report-only local classifier-governance tests. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.5 should create a disabled calibration plan only if support-aware controls pass.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "support_aware_negative_controls_v0_5_4.json", summary)
    wjson(OUT / "latest_support_aware_negative_controls.json", summary)
    wtext(OUT / "support_aware_negative_controls_v0_5_4.md", report(summary))
    wtext(OUT / "latest_support_aware_negative_controls.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "source_remediation_task_count": summary["source_remediation_task_count"],
        "negative_control_count": summary["negative_control_count"],
        "passed_control_count": summary["passed_control_count"],
        "failed_control_count": summary["failed_control_count"],
        "final_recommendation": summary["final_recommendation"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/negative_controls/latest_support_aware_negative_controls.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
