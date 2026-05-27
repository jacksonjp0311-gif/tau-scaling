
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
IMPACT_PATH = REPO_ROOT / "reports" / "policy_impact" / "latest_policy_impact_cards.json"
OUT_DIR = REPO_ROOT / "reports" / "policy_decision"
VIS_DIR = REPO_ROOT / "visuals" / "policy_decision" / "v0_4_8"

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def decide(card: dict[str, Any]) -> tuple[str, str, str]:
    impact = card.get("impact_class")
    risk = card.get("risk_label")

    if impact == "manual_review_required":
        return (
            "DEFER_TO_HUMAN_REVIEW",
            "manual_review_gate",
            "Do not enforce automatically. Human review is required before any classifier-policy mutation.",
        )
    if impact == "controlled_policy_downgrade":
        return (
            "APPROVE_FOR_REGRESSION_REVIEW",
            "controlled_downgrade_candidate",
            "Candidate for future controlled downgrade, but only after regression and over-penalty review.",
        )
    if impact == "hard_reject_candidate":
        return (
            "REJECT_ENFORCEMENT_FOR_NOW",
            "hard_reject_risk",
            "Do not enforce. Hard-reject policy requires explicit provenance and regression review.",
        )
    return (
        "RETAIN_CURRENT_BEHAVIOR",
        risk or "low",
        "No class drift; retain current behavior.",
    )

def decision_row(card: dict[str, Any]) -> dict[str, Any]:
    decision, decision_class, rationale = decide(card)
    return {
        "card_id": card.get("card_id"),
        "gate_pair": card.get("gate_pair"),
        "gate_a": card.get("gate_a"),
        "gate_b": card.get("gate_b"),
        "current_classification": card.get("current_classification"),
        "simulated_policy_classification": card.get("simulated_policy_classification"),
        "impact_class": card.get("impact_class"),
        "risk_label": card.get("risk_label"),
        "decision": decision,
        "decision_class": decision_class,
        "decision_rationale": rationale,
        "finding_codes": card.get("finding_codes", []),
        "policy_enforced": False,
        "mutation_allowed": False,
        "non_claim_lock": "Policy decisions are local classifier-governance decisions only; they do not validate silicon or product claims.",
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

    decision_counts = summary["decision_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(decision_counts.keys()), list(decision_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Decision count")
    plt.title("Policy Decision Counts")
    save(VIS_DIR / "policy_decision_counts.png")

    class_counts = summary["decision_class_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(class_counts.keys()), list(class_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Decision class count")
    plt.title("Policy Decision Classes")
    save(VIS_DIR / "policy_decision_class_counts.png")

    gate_counts = summary["decision_gate_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Decision involvement")
    plt.title("Decision Involvement by Gate")
    save(VIS_DIR / "policy_decision_gate_counts.png")

    return paths

def render_md(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.8 Policy Decision Record",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Input impact cards: `{summary['input_card_count']}`",
        f"- Mutation allowed: `{summary['mutation_allowed']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        f"- Final recommendation: `{summary['final_recommendation']}`",
        "",
        "## Decision Counts",
        "",
        "| Decision | Count |",
        "|---|---:|",
    ]
    for k, v in summary["decision_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Decision Rows",
        "",
        "| Card | Gate pair | Current | Simulated | Impact | Decision | Mutation allowed |",
        "|---|---|---|---|---|---|---:|",
    ]
    for row in summary["decision_rows"]:
        lines.append(
            f"| `{row['card_id']}` | `{row['gate_pair']}` | `{row['current_classification']}` | "
            f"`{row['simulated_policy_classification']}` | `{row['impact_class']}` | `{row['decision']}` | `{row['mutation_allowed']}` |"
        )

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += [
        "## Decision Lock",
        "",
        "This record does not permit classifier mutation. It only converts impact cards into a governed decision surface.",
        "",
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)

def main() -> None:
    impact = read_json(IMPACT_PATH)
    cards = impact.get("cards", [])
    rows = [decision_row(card) for card in cards]

    decision_counts = Counter(row["decision"] for row in rows)
    decision_class_counts = Counter(row["decision_class"] for row in rows)
    gate_counts = Counter()
    for row in rows:
        gate_counts[row["gate_a"]] += 1
        gate_counts[row["gate_b"]] += 1

    mutation_allowed = False
    final_recommendation = "no_classifier_mutation__prepare_regression_review_for_controlled_downgrades"

    summary = {
        "schema": "tau-scaling-policy-decision-record-v0.4.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": "reports/policy_impact/latest_policy_impact_cards.json",
        "input_card_count": len(cards),
        "decision_counts": dict(decision_counts),
        "decision_class_counts": dict(decision_class_counts),
        "decision_gate_counts": dict(gate_counts),
        "decision_rows": rows,
        "mutation_allowed": mutation_allowed,
        "policy_enforced": False,
        "final_recommendation": final_recommendation,
        "boundary": "Policy decision records are local classifier-governance artifacts only. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.4.9 should run regression/over-penalty review for the six controlled downgrade candidates before any enforcement candidate.",
    }
    summary["chart_paths"] = generate_charts(summary)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "policy_decision_record_v0_4_8.json", summary)
    write_json(OUT_DIR / "latest_policy_decision_record.json", summary)
    write_text(OUT_DIR / "policy_decision_record_v0_4_8.md", render_md(summary))
    write_text(OUT_DIR / "latest_policy_decision_record.md", render_md(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "input_card_count": summary["input_card_count"],
        "decision_counts": summary["decision_counts"],
        "mutation_allowed": summary["mutation_allowed"],
        "policy_enforced": summary["policy_enforced"],
        "final_recommendation": summary["final_recommendation"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/policy_decision/latest_policy_decision_record.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
