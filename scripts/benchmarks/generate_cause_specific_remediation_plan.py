
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CAUSES = ROOT / "reports" / "over_penalty_causes" / "latest_over_penalty_cause_decomposition.json"
OUT = ROOT / "reports" / "remediation_plan"
TASKS = OUT / "tasks" / "v0_5_3"
VIS = ROOT / "visuals" / "remediation_plan" / "v0_5_3"

def rjson(p): return json.loads(p.read_text(encoding="utf-8"))
def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")
def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def task_for(card, idx):
    primary = card.get("primary_cause")
    causes = card.get("causes", [])
    gate_pair = card.get("gate_pair")
    if primary == "high_diagnostic_support":
        remediation_class = "support_aware_negative_control"
        action = "Design a support-aware negative control before reconsidering downgrade pressure."
        validation = [
            "build disabled negative-control case",
            "compare downgrade pressure against high-support retention baseline",
            "rerun cause decomposition",
            "keep mutation_allowed false",
        ]
    elif primary == "heuristic_over_sensitivity" or "heuristic_over_sensitivity" in causes:
        remediation_class = "disabled_calibration_plan"
        action = "Create a disabled calibration plan that tests threshold sensitivity without changing classifier behavior."
        validation = [
            "run calibration as report-only",
            "compare blocker count before/after proposal",
            "do not activate policy",
            "keep mutation_allowed false",
        ]
    elif primary == "missing_finding_provenance":
        remediation_class = "finding_provenance_repair"
        action = "Add explicit finding provenance before the candidate can be reconsidered."
        validation = [
            "emit finding provenance record",
            "rerun policy impact cards",
            "rerun decision record",
            "keep mutation_allowed false",
        ]
    else:
        remediation_class = "manual_remediation_review"
        action = "Retain block and collect additional diagnostic features."
        validation = [
            "manual review required",
            "no automatic downgrade",
            "keep mutation_allowed false",
        ]
    return {
        "schema": "tau-scaling-remediation-task-v0.5.3",
        "task_id": f"remediation-task-v0-5-3-{idx:03d}",
        "source_card_id": card.get("card_id"),
        "gate_pair": gate_pair,
        "primary_cause": primary,
        "causes": causes,
        "remediation_class": remediation_class,
        "remediation_action": action,
        "required_validation": validation,
        "status": "planned_not_applied",
        "mutation_allowed": False,
        "policy_enforced": False,
        "non_claim_lock": "Remediation tasks are local classifier-governance planning artifacts only.",
    }

def task_md(t):
    checks = "\n".join(f"- {x}" for x in t["required_validation"])
    return f"""# {t['task_id']}

- Source card: `{t['source_card_id']}`
- Gate pair: `{t['gate_pair']}`
- Remediation class: `{t['remediation_class']}`
- Status: `{t['status']}`
- Mutation allowed: `{t['mutation_allowed']}`
- Policy enforced: `{t['policy_enforced']}`

## Action

{t['remediation_action']}

## Required Validation

{checks}

## Boundary

{t['non_claim_lock']}
"""

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
    for title, data, fname in [
        ("Remediation Class Counts", summary["remediation_class_counts"], "remediation_class_counts.png"),
        ("Primary Cause Counts", summary["primary_cause_counts"], "remediation_primary_cause_counts.png"),
        ("Gate Involvement", summary["gate_involvement_counts"], "remediation_gate_involvement.png"),
    ]:
        plt.figure(figsize=(9, 4))
        plt.bar(list(data.keys()), list(data.values()))
        plt.xticks(rotation=25, ha="right")
        plt.ylabel("Count")
        plt.title(title)
        save(fname)
    return paths

def report(summary):
    lines = [
        "# Tau Scaling v0.5.3 Cause-Specific Remediation Plan",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Source cause cards: `{summary['source_cause_card_count']}`",
        f"- Remediation task count: `{summary['remediation_task_count']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Remediation Class Counts",
        "",
        "| Class | Count |",
        "|---|---:|",
    ]
    for k,v in summary["remediation_class_counts"].items():
        lines.append(f"| `{k}` | {v} |")
    lines += ["", "## Tasks", "", "| Task | Gate pair | Class | Status | Action |", "|---|---|---|---|---|"]
    for t in summary["remediation_tasks"]:
        action = t["remediation_action"].replace("|", "\\|")
        lines.append(f"| `{t['task_id']}` | `{t['gate_pair']}` | `{t['remediation_class']}` | `{t['status']}` | {action} |")
    lines += ["", "## Charts", ""]
    for p in summary["chart_paths"]:
        rel = os.path.relpath(ROOT / p, OUT).replace("\\", "/")
        lines.append(f"![{Path(p).stem}]({rel})")
        lines.append("")
    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main():
    cause = rjson(CAUSES)
    cards = cause.get("cause_cards", [])
    tasks = [task_for(c, i+1) for i,c in enumerate(cards)]
    TASKS.mkdir(parents=True, exist_ok=True)
    for t in tasks:
        wjson(TASKS / f"{t['task_id']}.json", t)
        wtext(TASKS / f"{t['task_id']}.md", task_md(t))
    class_counts, cause_counts, gate_counts = Counter(), Counter(), Counter()
    for t in tasks:
        class_counts[t["remediation_class"]] += 1
        cause_counts[t["primary_cause"]] += 1
        # gate pair format A+B
        for g in str(t["gate_pair"]).split("+"):
            if g and g != "None":
                gate_counts[g] += 1
    if class_counts.get("support_aware_negative_control", 0) > 0:
        final = "build_support_aware_negative_controls_next"
    elif class_counts.get("disabled_calibration_plan", 0) > 0:
        final = "build_disabled_calibration_plan_next"
    else:
        final = "retain_block_and_collect_more_features"
    summary = {
        "schema": "tau-scaling-cause-specific-remediation-plan-v0.5.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": "reports/over_penalty_causes/latest_over_penalty_cause_decomposition.json",
        "source_cause_card_count": len(cards),
        "remediation_task_count": len(tasks),
        "remediation_class_counts": dict(class_counts),
        "primary_cause_counts": dict(cause_counts),
        "gate_involvement_counts": dict(gate_counts),
        "remediation_tasks": tasks,
        "mutation_allowed": False,
        "policy_enforced": False,
        "final_recommendation": final,
        "boundary": "Cause-specific remediation planning is local classifier-governance planning only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.4 should implement support-aware negative controls as disabled/report-only tests.",
    }
    summary["chart_paths"] = charts(summary)
    wjson(OUT / "cause_specific_remediation_plan_v0_5_3.json", summary)
    wjson(OUT / "latest_cause_specific_remediation_plan.json", summary)
    wtext(OUT / "cause_specific_remediation_plan_v0_5_3.md", report(summary))
    wtext(OUT / "latest_cause_specific_remediation_plan.md", report(summary))
    print(json.dumps({
        "schema": summary["schema"],
        "source_cause_card_count": summary["source_cause_card_count"],
        "remediation_task_count": summary["remediation_task_count"],
        "remediation_class_counts": summary["remediation_class_counts"],
        "final_recommendation": summary["final_recommendation"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/remediation_plan/latest_cause_specific_remediation_plan.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
