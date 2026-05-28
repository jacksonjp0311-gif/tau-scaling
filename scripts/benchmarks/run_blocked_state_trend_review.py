
from __future__ import annotations
import json, os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTINUITY = ROOT / "reports" / "blocked_continuity" / "latest_blocked_state_continuity.json"
LEDGER = ROOT / "reports" / "blocked_continuity" / "blocked_state_continuity_ledger.jsonl"
OUT = ROOT / "reports" / "blocked_trend_review"
VIS = ROOT / "visuals" / "blocked_trend_review" / "v0_6_9"

def rjson(p):
    return json.loads(p.read_text(encoding="utf-8"))

def read_jsonl(p):
    if not p.exists():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows

def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def rel(p):
    return str(p.relative_to(ROOT)).replace("\\", "/")

def classify(rows, continuity):
    entry_count = len(rows)
    executor_statuses = Counter(row.get("executor_status", "UNKNOWN") for row in rows)
    handoff_statuses = Counter(row.get("handoff_status", "UNKNOWN") for row in rows)
    replay_allowed_count = sum(1 for row in rows if row.get("replay_allowed") is True)
    mutation_allowed_count = sum(1 for row in rows if row.get("mutation_allowed") is True)
    execution_count = sum(1 for row in rows if row.get("executor_ran") is True)
    branch_count = sum(1 for row in rows if row.get("branch_created") is True)
    live_approval_present_count = sum(1 for row in rows if row.get("live_approval_present") is True)

    current_executor = continuity.get("executor_status")
    current_handoff = continuity.get("handoff_status")
    current_blocked = continuity.get("executor_blocked") is True and continuity.get("handoff_blocked") is True

    if mutation_allowed_count or execution_count or branch_count:
        status = "TREND_REVIEW_ALERT__UNEXPECTED_EXECUTION_OR_MUTATION"
        recommendation = "Stop promotion and inspect continuity ledger immediately."
    elif replay_allowed_count:
        status = "TREND_REVIEW_ALERT__REPLAY_ALLOWED_ENTRY_PRESENT"
        recommendation = "Inspect live approval chain before any next layer."
    elif current_blocked and current_handoff == "HANDOFF_BLOCKED__NO_LIVE_APPROVAL":
        status = "TREND_REVIEW_CONFIRMED__GOVERNANCE_BLOCK_STILL_VALID"
        recommendation = "Continue only with blocked-state observability or live-approval preparation; do not replay."
    elif entry_count == 0:
        status = "TREND_REVIEW_INCOMPLETE__NO_LEDGER_ENTRIES"
        recommendation = "Run blocked-state continuity ledger before trend review."
    else:
        status = "TREND_REVIEW_NEEDS_HUMAN_INSPECTION"
        recommendation = "Inspect latest executor/handoff status before continuing."

    return {
        "entry_count": entry_count,
        "executor_status_counts": dict(executor_statuses),
        "handoff_status_counts": dict(handoff_statuses),
        "replay_allowed_count": replay_allowed_count,
        "mutation_allowed_count": mutation_allowed_count,
        "execution_count": execution_count,
        "branch_count": branch_count,
        "live_approval_present_count": live_approval_present_count,
        "current_executor_status": current_executor,
        "current_handoff_status": current_handoff,
        "trend_status": status,
        "recommendation": recommendation,
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
        paths.append(rel(p))

    counts = summary["executor_status_counts"] or {"none": 0}
    plt.figure(figsize=(10, 4))
    plt.bar(list(counts.keys()), list(counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Ledger entries")
    plt.title("Blocked Trend Executor Status Counts")
    save("blocked_trend_executor_status_counts.png")

    handoff = summary["handoff_status_counts"] or {"none": 0}
    plt.figure(figsize=(10, 4))
    plt.bar(list(handoff.keys()), list(handoff.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Ledger entries")
    plt.title("Blocked Trend Handoff Status Counts")
    save("blocked_trend_handoff_status_counts.png")

    risk = {
        "replay_allowed": summary["replay_allowed_count"],
        "executor_ran": summary["execution_count"],
        "branch_created": summary["branch_count"],
        "mutation_allowed": summary["mutation_allowed_count"],
        "live_approval_present": summary["live_approval_present_count"],
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(risk.keys()), list(risk.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Ledger count")
    plt.title("Blocked Trend Risk Counters")
    save("blocked_trend_risk_counters.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.9 Blocked-State Trend Review",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Trend Result",
        "",
        f"- Trend status: `{s['trend_status']}`",
        f"- Ledger entries: `{s['entry_count']}`",
        f"- Current executor status: `{s['current_executor_status']}`",
        f"- Current handoff status: `{s['current_handoff_status']}`",
        f"- Replay allowed entries: `{s['replay_allowed_count']}`",
        f"- Executor-ran entries: `{s['execution_count']}`",
        f"- Branch-created entries: `{s['branch_count']}`",
        f"- Mutation-allowed entries: `{s['mutation_allowed_count']}`",
        "",
        "## Recommendation",
        "",
        s["recommendation"],
        "",
        "## Status Counts",
        "",
        "### Executor Status Counts",
        "",
        "| Executor status | Count |",
        "|---|---:|",
    ]
    for k, v in s["executor_status_counts"].items():
        lines.append(f"| `{k}` | {v} |")
    lines += [
        "",
        "### Handoff Status Counts",
        "",
        "| Handoff status | Count |",
        "|---|---:|",
    ]
    for k, v in s["handoff_status_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    continuity = rjson(CONTINUITY)
    rows = read_jsonl(LEDGER)
    trend = classify(rows, continuity)

    summary = {
        "schema": "tau-scaling-blocked-state-trend-review-v0.6.9",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_blocked_continuity": rel(CONTINUITY),
        "input_blocked_ledger": rel(LEDGER),
        **trend,
        "retirement_recommendation": "do_not_retire_approval_pathway_yet",
        "continuation_recommendation": "continue_blocked_observability_or_create_live_approval_preparation_layer",
        "replay_allowed": False,
        "executor_ran": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "boundary": "Blocked-state trend reviews are local classifier-governance analysis artifacts. They review blocked execution continuity. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.7.0 should package the approval-governance corridor as a stable governance milestone, not continue adding gates indefinitely.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "blocked_state_trend_review_v0_6_9.json", summary)
    wjson(OUT / "latest_blocked_state_trend_review.json", summary)
    wtext(OUT / "blocked_state_trend_review_v0_6_9.md", report(summary))
    wtext(OUT / "latest_blocked_state_trend_review.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "trend_status": summary["trend_status"],
        "entry_count": summary["entry_count"],
        "current_executor_status": summary["current_executor_status"],
        "current_handoff_status": summary["current_handoff_status"],
        "replay_allowed_count": summary["replay_allowed_count"],
        "execution_count": summary["execution_count"],
        "branch_count": summary["branch_count"],
        "mutation_allowed_count": summary["mutation_allowed_count"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/blocked_trend_review/latest_blocked_state_trend_review.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
