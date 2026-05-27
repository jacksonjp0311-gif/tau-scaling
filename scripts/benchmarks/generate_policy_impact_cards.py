
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DRY_RUN = REPO_ROOT / "reports" / "policy_dry_run" / "latest_pair_policy_dry_run.json"
OUT_DIR = REPO_ROOT / "reports" / "policy_impact"
CARD_DIR = OUT_DIR / "cards" / "v0_4_7"
VIS_DIR = REPO_ROOT / "visuals" / "policy_impact" / "v0_4_7"

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def classify_impact(row: dict[str, Any]) -> str:
    sim = row.get("simulated_policy_classification")
    if sim == "HUMAN_REVIEW":
        return "manual_review_required"
    if sim == "TSEK-D":
        return "controlled_policy_downgrade"
    if sim == "TSEK-E":
        return "hard_reject_candidate"
    return "no_policy_drift"

def risk_label(row: dict[str, Any]) -> str:
    action = row.get("simulation_action")
    if action == "human_review_required":
        return "review_risk"
    if action == "candidate_downgrade":
        return "downgrade_risk"
    if action == "candidate_hard_reject":
        return "hard_reject_risk"
    return "low"

def card_for(row: dict[str, Any], index: int) -> dict[str, Any]:
    current = row.get("current_classification")
    simulated = row.get("simulated_policy_classification")
    impact_class = classify_impact(row)
    risk = risk_label(row)
    gate_pair = f"{row.get('gate_a')}+{row.get('gate_b')}"
    explanation = (
        f"Pair {gate_pair} remains {current}; no simulated policy drift."
        if not row.get("drifted")
        else f"Pair {gate_pair} would move from {current} to {simulated} under dry-run policy."
    )
    if simulated == "HUMAN_REVIEW":
        decision = "Do not enforce automatically; route to human policy review."
    elif simulated == "TSEK-D":
        decision = "Candidate controlled downgrade; explain and regression-test before enforcement."
    elif simulated == "TSEK-E":
        decision = "Hard reject candidate; block enforcement until explicit provenance and regression review."
    else:
        decision = "Retain current behavior."

    return {
        "schema": "tau-scaling-policy-impact-card-v0.4.7",
        "card_id": f"policy-impact-v0-4-7-{index:03d}",
        "gate_a": row.get("gate_a"),
        "gate_b": row.get("gate_b"),
        "gate_pair": gate_pair,
        "current_classification": current,
        "simulated_policy_classification": simulated,
        "policy_class": row.get("policy_class"),
        "simulation_action": row.get("simulation_action"),
        "impact_class": impact_class,
        "risk_label": risk,
        "drifted": row.get("drifted"),
        "drift_severity": row.get("drift_severity"),
        "finding_codes": row.get("finding_codes", []),
        "findings_count": row.get("findings_count", 0),
        "current_A_TSEK": row.get("current_A_TSEK"),
        "current_diagnostic_average": row.get("current_diagnostic_average"),
        "reason": row.get("reason"),
        "recommended_action_from_policy": row.get("recommended_action"),
        "impact_explanation": explanation,
        "decision_hint": decision,
        "policy_enforced": False,
        "non_claim_lock": "Policy impact cards explain simulated classifier-governance effects only; they do not validate silicon or product claims.",
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

    impact_counts = summary["impact_class_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(impact_counts.keys()), list(impact_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Card count")
    plt.title("Policy Impact Class Counts")
    save(VIS_DIR / "policy_impact_class_counts.png")

    risk_counts = summary["risk_label_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(risk_counts.keys()), list(risk_counts.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Card count")
    plt.title("Policy Impact Risk Labels")
    save(VIS_DIR / "policy_impact_risk_labels.png")

    gate_counts = summary["drift_gate_counts"]
    plt.figure(figsize=(9, 4))
    plt.bar(list(gate_counts.keys()), list(gate_counts.values()))
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Drift-card involvement")
    plt.title("Policy Impact Drift by Gate")
    save(VIS_DIR / "policy_impact_drift_by_gate.png")

    return paths

def render_card_md(card: dict[str, Any]) -> str:
    return "\n".join([
        f"# {card['card_id']}",
        "",
        f"- Gate pair: `{card['gate_pair']}`",
        f"- Current class: `{card['current_classification']}`",
        f"- Simulated class: `{card['simulated_policy_classification']}`",
        f"- Impact class: `{card['impact_class']}`",
        f"- Risk label: `{card['risk_label']}`",
        f"- Drifted: `{card['drifted']}`",
        "",
        "## Explanation",
        "",
        card["impact_explanation"],
        "",
        "## Decision Hint",
        "",
        card["decision_hint"],
        "",
        "## Boundary",
        "",
        card["non_claim_lock"],
        "",
    ])

def render_report(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.4.7 Policy Impact Explanation Cards",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Input dry-run rows: `{summary['input_rows']}`",
        f"- Drift cards: `{summary['drift_card_count']}`",
        f"- Controlled downgrade cards: `{summary['controlled_downgrade_count']}`",
        f"- Manual review cards: `{summary['manual_review_count']}`",
        f"- Hard reject candidate cards: `{summary['hard_reject_candidate_count']}`",
        f"- Policy enforced: `{summary['policy_enforced']}`",
        "",
        "## Impact Classes",
        "",
        "| Impact class | Count |",
        "|---|---:|",
    ]
    for k, v in summary["impact_class_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Risk Labels",
        "",
        "| Risk label | Count |",
        "|---|---:|",
    ]
    for k, v in summary["risk_label_counts"].items():
        lines.append(f"| `{k}` | {v} |")

    lines += [
        "",
        "## Cards",
        "",
        "| Card | Gate pair | Current | Simulated | Impact | Decision hint |",
        "|---|---|---|---|---|---|",
    ]
    for c in summary["cards"]:
        rel = os.path.relpath(CARD_DIR / f"{c['card_id']}.md", OUT_DIR).replace("\\", "/")
        hint = c["decision_hint"].replace("|", "\\|")
        lines.append(f"| [`{c['card_id']}`]({rel}) | `{c['gate_pair']}` | `{c['current_classification']}` | `{c['simulated_policy_classification']}` | `{c['impact_class']}` | {hint} |")

    lines += ["", "## Charts", ""]
    for chart in summary["chart_paths"]:
        rel = os.path.relpath(REPO_ROOT / chart, OUT_DIR).replace("\\", "/")
        lines += [f"![{Path(chart).stem}]({rel})", ""]

    lines += ["## Boundary", "", summary["boundary"], ""]
    return "\n".join(lines)

def main() -> None:
    dry = read_json(DRY_RUN)
    rows = dry.get("dry_run_rows", [])
    drift_rows = [r for r in rows if r.get("drifted")]
    cards = [card_for(row, i + 1) for i, row in enumerate(drift_rows)]

    CARD_DIR.mkdir(parents=True, exist_ok=True)
    for card in cards:
        write_json(CARD_DIR / f"{card['card_id']}.json", card)
        write_text(CARD_DIR / f"{card['card_id']}.md", render_card_md(card))

    impact_counts = Counter(c["impact_class"] for c in cards)
    risk_counts = Counter(c["risk_label"] for c in cards)
    gate_counts = Counter()
    for c in cards:
        gate_counts[c["gate_a"]] += 1
        gate_counts[c["gate_b"]] += 1

    summary = {
        "schema": "tau-scaling-policy-impact-explanation-cards-v0.4.7",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input": "reports/policy_dry_run/latest_pair_policy_dry_run.json",
        "input_rows": len(rows),
        "drift_card_count": len(cards),
        "controlled_downgrade_count": impact_counts.get("controlled_policy_downgrade", 0),
        "manual_review_count": impact_counts.get("manual_review_required", 0),
        "hard_reject_candidate_count": impact_counts.get("hard_reject_candidate", 0),
        "impact_class_counts": dict(impact_counts),
        "risk_label_counts": dict(risk_counts),
        "drift_gate_counts": dict(gate_counts),
        "policy_enforced": False,
        "cards": cards,
        "boundary": "Policy impact explanation cards explain dry-run classifier-policy effects only. They do not change classifier behavior and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.4.8 should create a policy decision record before any enforcement candidate.",
    }
    summary["chart_paths"] = generate_charts(summary)

    write_json(OUT_DIR / "policy_impact_cards_v0_4_7.json", summary)
    write_json(OUT_DIR / "latest_policy_impact_cards.json", summary)
    write_text(OUT_DIR / "policy_impact_cards_v0_4_7.md", render_report(summary))
    write_text(OUT_DIR / "latest_policy_impact_cards.md", render_report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "input_rows": summary["input_rows"],
        "drift_card_count": summary["drift_card_count"],
        "controlled_downgrade_count": summary["controlled_downgrade_count"],
        "manual_review_count": summary["manual_review_count"],
        "hard_reject_candidate_count": summary["hard_reject_candidate_count"],
        "policy_enforced": summary["policy_enforced"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/policy_impact/latest_policy_impact_cards.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
