
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = REPO_ROOT / "reports" / "policy" / "latest_pair_policy_review.json"
OUT_DIR = REPO_ROOT / "reports" / "policy_dry_run"
VIS_DIR = REPO_ROOT / "visuals" / "policy_dry_run" / "v0_4_6"

CLASS_ORDER = ["TSEK-B", "TSEK-C", "TSEK-D", "TSEK-E", "HUMAN_REVIEW"]
CLASS_RANK = {c: i for i, c in enumerate(CLASS_ORDER)}

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def simulate_class(row: dict[str, Any]) -> tuple[str, str]:
    policy_class = row.get("policy_class", "")
    current = row.get("current_classification", "UNKNOWN")

    if policy_class == "TSEK-C_RETAIN":
        return current, "retain"
    if policy_class == "TSEK-D_CANDIDATE":
        return "TSEK-D", "candidate_downgrade"
    if policy_class == "TSEK-E_CANDIDATE":
        return "TSEK-E", "candidate_hard_reject"
    if policy_class == "HUMAN_REVIEW":
        return "HUMAN_REVIEW", "human_review_required"
    return current, "unknown_policy_retain"

def drift_severity(current: str, simulated: str) -> int:
    if current == simulated:
        return 0
    return max(1, CLASS_RANK.get(simulated, 99) - CLASS_RANK.get(current, 99))

def build_rows(policy: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for row in policy.get("policy_rows", []):
        simulated, action = simulate_class(row)
        current = row.get("current_classification", "UNKNOWN")
        rows.append({
            "gate_a": row.get("gate_a"),
            "gate_b": row.get("gate_b"),
            "current_classification": current,
            "policy_class": row.get("policy_class"),
            "simulated_policy_classification": simulated,
            "simulation_action": action,
            "drifted": current != simulated,
            "drift_severity": drift_severity(current, simulated),
            "finding_codes": row.get("finding_codes", []),
            "findings_count": row.get("findings_count", 0),
            "current_A_TSEK": row.get("current_A_TSEK"),
            "current_diagnostic_average": row.get("current_diagnostic_average"),
            "recommended_action": row.get("recommended_action"),
            "reason": row.get("reason"),
            "policy_enforced": False,
        })
    return rows

def generate_charts(summary: dict[str, Any]) -> list[str]:
    chart_paths: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        write_text(OUT_DIR / "chart_generation_skipped.txt", f"matplotlib unavailable: {exc}\n")
        return chart_paths

    VIS_DIR.mkdir(parents=True, exist_ok=True)

    def savefig(path: Path) -> None:
        plt.tight_layout()
        plt.savefig(path, dpi=180, bbox_inches="tight")
        plt.close()
        chart_paths.append(str(path.relative_to(REPO_ROOT)).replace("\\", "/"))

    current_counts = summary["current_class_counts"]
    simulated_counts = summary["simulated_class_counts"]
    labels = sorted(set(current_counts) | set(simulated_counts), key=lambda x: CLASS_RANK.get(x, 99))

    x = list(range(len(labels)))
    width = 0.35
    plt.figure(figsize=(9, 4))
    plt.bar([i - width/2 for i in x], [current_counts.get(k, 0) for k in labels], width=width, label="current")
    plt.bar([i + width/2 for i in x], [simulated_counts.get(k, 0) for k in labels], width=width, label="simulated")
    plt.xticks(x, labels, rotation=25, ha="right")
    plt.ylabel("Pair count")
    plt.title("Current vs Simulated Policy Classification")
    plt.legend()
    savefig(VIS_DIR / "current_vs_simulated_class_counts.png")

    action_counts = summary["simulation_action_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(action_counts.keys()), list(action_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Pair count")
    plt.title("Policy Dry-Run Action Counts")
    savefig(VIS_DIR / "policy_dry_run_action_counts.png")

    gate_counts = summary["drift_by_gate"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Drift involvement count")
    plt.title("Class Drift Involvement by Gate")
    savefig(VIS_DIR / "class_drift_by_gate.png")

    return chart_paths

def summarize(rows: list[dict[str, Any]], policy: dict[str, Any]) -> dict[str, Any]:
    current_counts = Counter(r["current_classification"] for r in rows)
    simulated_counts = Counter(r["simulated_policy_classification"] for r in rows)
    action_counts = Counter(r["simulation_action"] for r in rows)
    drift_rows = [r for r in rows if r["drifted"]]
    drift_by_gate = Counter()
    for r in drift_rows:
        drift_by_gate[r["gate_a"]] += 1
        drift_by_gate[r["gate_b"]] += 1

    pair_count = len(rows)
    drift_count = len(drift_rows)
    human_review_count = simulated_counts.get("HUMAN_REVIEW", 0)
    downgrade_count = sum(1 for r in drift_rows if r["simulated_policy_classification"] == "TSEK-D")
    hard_reject_count = sum(1 for r in drift_rows if r["simulated_policy_classification"] == "TSEK-E")

    over_penalty_flag = drift_count / max(1, pair_count) > 0.35 or hard_reject_count > 0
    simulator_recommendation = (
        "do_not_enforce_yet_over_penalty_review_required"
        if over_penalty_flag
        else "safe_for_human_review_not_enforcement"
        if human_review_count > 0
        else "candidate_safe_for_limited_enforcement"
    )

    summary = {
        "schema": "tau-scaling-pair-policy-dry-run-v0.4.6",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "policy_source": "reports/policy/latest_pair_policy_review.json",
        "pair_count": pair_count,
        "drift_count": drift_count,
        "drift_ratio": round(drift_count / max(1, pair_count), 4),
        "human_review_count": human_review_count,
        "downgrade_count": downgrade_count,
        "hard_reject_count": hard_reject_count,
        "current_class_counts": dict(current_counts),
        "simulated_class_counts": dict(simulated_counts),
        "simulation_action_counts": dict(action_counts),
        "drift_by_gate": dict(drift_by_gate),
        "over_penalty_flag": over_penalty_flag,
        "simulator_recommendation": simulator_recommendation,
        "policy_enforced": False,
        "dry_run_rows": rows,
        "boundary": "Pair policy dry-run simulates classifier-policy impact only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.4.7 should generate policy impact explanation cards before any classifier enforcement candidate.",
    }
    charts = generate_charts(summary)
    summary["chart_paths"] = charts
    return summary

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.6 Pair Policy Dry-Run Simulator",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Pair count: `{summary['pair_count']}`",
        f"- Drift count: `{summary['drift_count']}`",
        f"- Drift ratio: `{summary['drift_ratio']}`",
        f"- Downgrade count: `{summary['downgrade_count']}`",
        f"- Human review count: `{summary['human_review_count']}`",
        f"- Hard reject count: `{summary['hard_reject_count']}`",
        f"- Over-penalty flag: `{summary['over_penalty_flag']}`",
        f"- Recommendation: `{summary['simulator_recommendation']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Current vs Simulated Class Counts",
        "",
        "| Class | Current | Simulated |",
        "|---|---:|---:|",
    ]
    labels = sorted(set(summary["current_class_counts"]) | set(summary["simulated_class_counts"]), key=lambda x: CLASS_RANK.get(x, 99))
    for label in labels:
        lines.append(f"| `{label}` | {summary['current_class_counts'].get(label, 0)} | {summary['simulated_class_counts'].get(label, 0)} |")

    lines += [
        "",
        "## Simulation Actions",
        "",
        "| Action | Count |",
        "|---|---:|",
    ]
    for k, v in summary["simulation_action_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Drift by Gate",
        "",
        "| Gate | Drift involvement count |",
        "|---|---:|",
    ]
    for k, v in sorted(summary["drift_by_gate"].items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Dry-Run Rows",
        "",
        "| Gate A | Gate B | Current | Simulated | Action | Drifted | Reason |",
        "|---|---|---|---|---|---:|---|",
    ]
    for r in summary["dry_run_rows"]:
        reason = str(r.get("reason", "")).replace("|", "\\|")
        lines.append(f"| `{r['gate_a']}` | `{r['gate_b']}` | `{r['current_classification']}` | `{r['simulated_policy_classification']}` | `{r['simulation_action']}` | `{r['drifted']}` | {reason} |")

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main() -> None:
    policy = read_json(POLICY_PATH)
    rows = build_rows(policy)
    summary = summarize(rows, policy)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "pair_policy_dry_run_v0_4_6.json", summary)
    write_json(OUT_DIR / "latest_pair_policy_dry_run.json", summary)
    md = render_md(summary)
    write_text(OUT_DIR / "pair_policy_dry_run_v0_4_6.md", md)
    write_text(OUT_DIR / "latest_pair_policy_dry_run.md", md)

    print(json.dumps({
        "schema": summary["schema"],
        "pair_count": summary["pair_count"],
        "drift_count": summary["drift_count"],
        "drift_ratio": summary["drift_ratio"],
        "downgrade_count": summary["downgrade_count"],
        "human_review_count": summary["human_review_count"],
        "hard_reject_count": summary["hard_reject_count"],
        "over_penalty_flag": summary["over_penalty_flag"],
        "simulator_recommendation": summary["simulator_recommendation"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/policy_dry_run/latest_pair_policy_dry_run.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
