
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DECISION_PATH = REPO_ROOT / "reports" / "policy_decision" / "latest_policy_decision_record.json"
DRY_RUN_PATH = REPO_ROOT / "reports" / "policy_dry_run" / "latest_pair_policy_dry_run.json"
OUT_DIR = REPO_ROOT / "reports" / "regression_review"
VIS_DIR = REPO_ROOT / "visuals" / "regression_review" / "v0_4_9"

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def review_row(row: dict[str, Any], dry_lookup: dict[str, dict[str, Any]]) -> dict[str, Any]:
    gate_pair = row.get("gate_pair")
    dry = dry_lookup.get(gate_pair, {})
    decision = row.get("decision")
    simulated = row.get("simulated_policy_classification")
    current = row.get("current_classification")

    is_candidate = decision == "APPROVE_FOR_REGRESSION_REVIEW"
    is_human = decision == "DEFER_TO_HUMAN_REVIEW"

    drift_severity = int(dry.get("drift_severity", 0) or 0)
    findings_count = int(dry.get("findings_count", row.get("findings_count", 0) or 0))
    diagnostic_average = dry.get("current_diagnostic_average", row.get("current_diagnostic_average"))
    a_tsek = dry.get("current_A_TSEK", row.get("current_A_TSEK"))

    # Local over-penalty heuristic: a controlled downgrade is suspicious only if it is
    # based on weak policy pressure, high diagnostic support, or missing provenance.
    high_support = isinstance(diagnostic_average, (int, float)) and diagnostic_average >= 0.75
    missing_findings = findings_count == 0
    high_severity = drift_severity >= 2

    over_penalty_flag = bool(is_candidate and (high_support or missing_findings or high_severity))
    regression_passed = bool(is_candidate and not over_penalty_flag and simulated == "TSEK-D")
    human_review_passed = bool(is_human and simulated == "HUMAN_REVIEW")

    if regression_passed:
        outcome = "REGRESSION_REVIEW_PASS"
        recommendation = "Keep as controlled-downgrade candidate for future enforcement-candidate review."
    elif over_penalty_flag:
        outcome = "OVER_PENALTY_REVIEW_REQUIRED"
        recommendation = "Do not enforce. Review evidence pressure, diagnostic support, and finding provenance."
    elif human_review_passed:
        outcome = "HUMAN_REVIEW_CONFIRMED"
        recommendation = "Keep human-review routing. Do not convert to automatic downgrade."
    else:
        outcome = "NO_ENFORCEMENT_PATH"
        recommendation = "Retain current classifier behavior."

    return {
        "gate_pair": gate_pair,
        "gate_a": row.get("gate_a"),
        "gate_b": row.get("gate_b"),
        "current_classification": current,
        "simulated_policy_classification": simulated,
        "decision": decision,
        "decision_class": row.get("decision_class"),
        "drift_severity": drift_severity,
        "findings_count": findings_count,
        "current_A_TSEK": a_tsek,
        "current_diagnostic_average": diagnostic_average,
        "high_support_flag": high_support,
        "missing_findings_flag": missing_findings,
        "high_severity_flag": high_severity,
        "over_penalty_flag": over_penalty_flag,
        "regression_passed": regression_passed,
        "review_outcome": outcome,
        "recommendation": recommendation,
        "mutation_allowed": False,
        "policy_enforced": False,
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

    outcome_counts = summary["review_outcome_counts"]
    plt.figure(figsize=(10, 4))
    plt.bar(list(outcome_counts.keys()), list(outcome_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Case count")
    plt.title("Regression Review Outcomes")
    save(VIS_DIR / "regression_review_outcomes.png")

    gate_counts = summary["regression_gate_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Regression candidate involvement")
    plt.title("Regression Candidate Involvement by Gate")
    save(VIS_DIR / "regression_candidate_gate_counts.png")

    flags = {
        "over_penalty": summary["over_penalty_count"],
        "regression_pass": summary["regression_pass_count"],
        "human_review": summary["human_review_confirmed_count"],
    }
    plt.figure(figsize=(8, 4))
    plt.bar(list(flags.keys()), list(flags.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Count")
    plt.title("Regression / Over-Penalty Review Summary")
    save(VIS_DIR / "regression_over_penalty_summary.png")

    return paths

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.9 Regression and Over-Penalty Review",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Input decision rows: `{summary['input_decision_rows']}`",
        f"- Controlled downgrade candidates: `{summary['controlled_downgrade_candidate_count']}`",
        f"- Regression pass count: `{summary['regression_pass_count']}`",
        f"- Over-penalty count: `{summary['over_penalty_count']}`",
        f"- Human review confirmed count: `{summary['human_review_confirmed_count']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        "",
        "## Review Outcomes",
        "",
        "| Outcome | Count |",
        "|---|---:|",
    ]
    for k, v in summary["review_outcome_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Review Rows",
        "",
        "| Gate pair | Current | Simulated | Decision | Outcome | Over-penalty | Regression passed | Recommendation |",
        "|---|---|---|---|---|---:|---:|---|",
    ]
    for row in summary["review_rows"]:
        rec = row["recommendation"].replace("|", "\\|")
        lines.append(
            f"| `{row['gate_pair']}` | `{row['current_classification']}` | `{row['simulated_policy_classification']}` | "
            f"`{row['decision']}` | `{row['review_outcome']}` | `{row['over_penalty_flag']}` | `{row['regression_passed']}` | {rec} |"
        )

    lines += ["", "## Charts", ""]
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
    decision = read_json(DECISION_PATH)
    dry = read_json(DRY_RUN_PATH)
    dry_lookup = {r.get("gate_a") + "+" + r.get("gate_b"): r for r in dry.get("dry_run_rows", [])}

    rows = [review_row(row, dry_lookup) for row in decision.get("decision_rows", [])]
    outcome_counts = Counter(row["review_outcome"] for row in rows)
    gate_counts = Counter()
    for row in rows:
        if row["decision"] == "APPROVE_FOR_REGRESSION_REVIEW":
            gate_counts[row["gate_a"]] += 1
            gate_counts[row["gate_b"]] += 1

    regression_pass_count = sum(1 for row in rows if row["regression_passed"])
    over_penalty_count = sum(1 for row in rows if row["over_penalty_flag"])
    human_review_confirmed_count = outcome_counts.get("HUMAN_REVIEW_CONFIRMED", 0)
    controlled_count = sum(1 for row in rows if row["decision"] == "APPROVE_FOR_REGRESSION_REVIEW")

    if over_penalty_count > 0:
        final = "do_not_enforce__over_penalty_review_required"
    elif regression_pass_count == controlled_count and controlled_count > 0:
        final = "eligible_for_enforcement_candidate_design__mutation_still_locked"
    else:
        final = "insufficient_for_enforcement_candidate"

    summary = {
        "schema": "tau-scaling-regression-over-penalty-review-v0.4.9",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_decision_record": "reports/policy_decision/latest_policy_decision_record.json",
        "input_dry_run": "reports/policy_dry_run/latest_pair_policy_dry_run.json",
        "input_decision_rows": len(rows),
        "controlled_downgrade_candidate_count": controlled_count,
        "regression_pass_count": regression_pass_count,
        "over_penalty_count": over_penalty_count,
        "human_review_confirmed_count": human_review_confirmed_count,
        "review_outcome_counts": dict(outcome_counts),
        "regression_gate_counts": dict(gate_counts),
        "review_rows": rows,
        "mutation_allowed": False,
        "policy_enforced": False,
        "final_recommendation": final,
        "boundary": "Regression and over-penalty review is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.5.0 should create an enforcement-candidate design only if mutation remains locked and regression review passes.",
    }
    summary["chart_paths"] = generate_charts(summary)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "regression_over_penalty_review_v0_4_9.json", summary)
    write_json(OUT_DIR / "latest_regression_over_penalty_review.json", summary)
    write_text(OUT_DIR / "regression_over_penalty_review_v0_4_9.md", render_md(summary))
    write_text(OUT_DIR / "latest_regression_over_penalty_review.md", render_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "input_decision_rows": summary["input_decision_rows"],
        "controlled_downgrade_candidate_count": summary["controlled_downgrade_candidate_count"],
        "regression_pass_count": summary["regression_pass_count"],
        "over_penalty_count": summary["over_penalty_count"],
        "human_review_confirmed_count": summary["human_review_confirmed_count"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "final_recommendation": summary["final_recommendation"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/regression_review/latest_regression_over_penalty_review.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
