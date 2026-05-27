
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
NEXUS_PATH = REPO_ROOT / "reports" / "nexus_feedback" / "latest_nexus_feedback.json"
READINESS_PATH = REPO_ROOT / "reports" / "enforcement_readiness" / "latest_enforcement_readiness_gate.json"
OUT_DIR = REPO_ROOT / "reports" / "nexus_target_refresh"
VIS_DIR = REPO_ROOT / "visuals" / "nexus_target_refresh" / "v0_5_1"

COMPLETION_EVIDENCE = {
    "TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator": [
        "reports/policy_dry_run/latest_pair_policy_dry_run.json",
        "reports/policy_dry_run/latest_pair_policy_dry_run.md",
    ],
    "TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards": [
        "reports/policy_impact/latest_policy_impact_cards.json",
        "reports/policy_impact/latest_policy_impact_cards.md",
    ],
    "TAU-SCALING-SA v0.4.8 - Policy Decision Record": [
        "reports/policy_decision/latest_policy_decision_record.json",
        "reports/policy_decision/latest_policy_decision_record.md",
    ],
    "TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review": [
        "reports/regression_review/latest_regression_over_penalty_review.json",
        "reports/regression_review/latest_regression_over_penalty_review.md",
    ],
    "TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate": [
        "reports/enforcement_readiness/latest_enforcement_readiness_gate.json",
        "reports/enforcement_readiness/latest_enforcement_readiness_gate.md",
    ],
}

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def evidence_complete(paths: list[str]) -> bool:
    return all((REPO_ROOT / p).exists() for p in paths)

def classify_priority(priority: dict[str, Any]) -> dict[str, Any]:
    target = priority.get("target_next", "")
    evidence = COMPLETION_EVIDENCE.get(target)
    if evidence and evidence_complete(evidence):
        status = "COMPLETED_RETIRED"
        reason = "Target evidence exists; recommendation should be retired from active Nexus queue."
    else:
        status = "ACTIVE"
        reason = "No completion evidence found for target."

    return {
        "id": priority.get("id"),
        "rank": priority.get("rank"),
        "surface": priority.get("surface"),
        "signal": priority.get("signal"),
        "severity": priority.get("severity"),
        "recommendation": priority.get("recommendation"),
        "target_next": target,
        "completion_status": status,
        "completion_reason": reason,
    }

def build_active_blocker(readiness: dict[str, Any]) -> dict[str, Any]:
    blocked = int(readiness.get("blocked_by_over_penalty_count", 0) or 0)
    eligible = int(readiness.get("eligible_candidate_design_count", 0) or 0)
    enforcement = bool(readiness.get("enforcement_candidate_enabled", False))
    mutation = bool(readiness.get("mutation_allowed", False))

    if blocked > 0 and eligible == 0 and not enforcement and not mutation:
        return {
            "id": "NF-ACTIVE-001",
            "rank": 1,
            "surface": "enforcement_readiness",
            "signal": "all_controlled_downgrades_blocked",
            "severity": "high",
            "target_next": "TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition",
            "recommendation": "Decompose why all controlled downgrades are blocked before any enforcement-candidate design.",
            "evidence": {
                "blocked_by_over_penalty_count": blocked,
                "eligible_candidate_design_count": eligible,
                "enforcement_candidate_enabled": enforcement,
                "mutation_allowed": mutation,
                "source": "reports/enforcement_readiness/latest_enforcement_readiness_gate.json",
            },
        }

    return {
        "id": "NF-ACTIVE-001",
        "rank": 1,
        "surface": "nexus_feedback",
        "signal": "no_active_blocker_detected",
        "severity": "low",
        "target_next": "TAU-SCALING-SA v0.5.2 - Nexus Maintenance",
        "recommendation": "No active enforcement blocker detected; maintain Nexus target tracking.",
        "evidence": {
            "source": "reports/enforcement_readiness/latest_enforcement_readiness_gate.json",
        },
    }

def generate_charts(summary: dict[str, Any]) -> list[str]:
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(OUT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def save(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    status_counts = summary["status_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(status_counts.keys()), list(status_counts.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Priority count")
    plt.title("Nexus Priority Completion Status")
    save(VIS_DIR / "nexus_priority_completion_status.png")

    active = summary["active_blocker"]["evidence"]
    keys = ["blocked_by_over_penalty_count", "eligible_candidate_design_count"]
    vals = [active.get(k, 0) for k in keys]
    plt.figure(figsize=(8, 4))
    plt.bar(keys, vals)
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Count")
    plt.title("Current Active Enforcement Blocker")
    save(VIS_DIR / "active_enforcement_blocker_counts.png")

    severity_counts = summary["retired_severity_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(severity_counts.keys()), list(severity_counts.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Retired priority count")
    plt.title("Retired Priorities by Severity")
    save(VIS_DIR / "retired_priority_severity_counts.png")

    return paths

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.5.1 Nexus Target Refresh and Completed-Signal Retirement",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Input Nexus priorities: `{summary['input_priority_count']}`",
        f"- Completed/retired priorities: `{summary['completed_signal_count']}`",
        f"- Active priorities retained from old Nexus: `{summary['active_old_signal_count']}`",
        f"- Current active blocker: `{summary['active_blocker']['signal']}`",
        f"- Next current target: `{summary['next_current_target']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Retired / Active Old Priorities",
        "",
        "| ID | Old target | Status | Reason |",
        "|---|---|---|---|",
    ]
    for row in summary["priority_refresh_rows"]:
        reason = row["completion_reason"].replace("|", "\\|")
        lines.append(f"| `{row['id']}` | `{row['target_next']}` | `{row['completion_status']}` | {reason} |")

    active = summary["active_blocker"]
    lines += [
        "",
        "## New Active Blocker",
        "",
        f"- ID: `{active['id']}`",
        f"- Surface: `{active['surface']}`",
        f"- Signal: `{active['signal']}`",
        f"- Severity: `{active['severity']}`",
        f"- Recommendation: {active['recommendation']}",
        f"- Target next: `{active['target_next']}`",
        "",
        "## Charts",
        "",
    ]

    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += [
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main() -> None:
    nexus = read_json(NEXUS_PATH)
    readiness = read_json(READINESS_PATH)

    priorities = nexus.get("priorities", [])
    rows = [classify_priority(p) for p in priorities]
    status_counts = Counter(r["completion_status"] for r in rows)
    retired = [r for r in rows if r["completion_status"] == "COMPLETED_RETIRED"]
    active_old = [r for r in rows if r["completion_status"] == "ACTIVE"]
    retired_severity_counts = Counter(r.get("severity", "unknown") for r in retired)
    active_blocker = build_active_blocker(readiness)

    summary = {
        "schema": "tau-scaling-nexus-target-refresh-v0.5.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_nexus_feedback": "reports/nexus_feedback/latest_nexus_feedback.json",
        "input_enforcement_readiness": "reports/enforcement_readiness/latest_enforcement_readiness_gate.json",
        "input_priority_count": len(priorities),
        "completed_signal_count": len(retired),
        "active_old_signal_count": len(active_old),
        "status_counts": dict(status_counts),
        "retired_severity_counts": dict(retired_severity_counts),
        "priority_refresh_rows": rows,
        "active_blocker": active_blocker,
        "next_current_target": active_blocker["target_next"],
        "mutation_allowed": False,
        "policy_enforced": False,
        "boundary": "Nexus target refresh is repository self-observation and queue hygiene only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": active_blocker["target_next"],
    }
    summary["chart_paths"] = generate_charts(summary)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "nexus_target_refresh_v0_5_1.json", summary)
    write_json(OUT_DIR / "latest_nexus_target_refresh.json", summary)
    write_text(OUT_DIR / "nexus_target_refresh_v0_5_1.md", render_md(summary))
    write_text(OUT_DIR / "latest_nexus_target_refresh.md", render_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "input_priority_count": summary["input_priority_count"],
        "completed_signal_count": summary["completed_signal_count"],
        "active_old_signal_count": summary["active_old_signal_count"],
        "next_current_target": summary["next_current_target"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/nexus_target_refresh/latest_nexus_target_refresh.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
