from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
SOURCE_LEDGER = ROOT / "reports" / "public_source_ledger" / "latest_public_source_ledger.json"
REPORT_DIR = ROOT / "reports" / "source_evidence_intake"
CARD_DIR = REPORT_DIR / "cards"
VIS_DIR = ROOT / "visuals" / "source_evidence_intake" / "v0_8_6"

REQUIRED_FIELDS = [
    "source_url",
    "source_title",
    "source_type",
    "source_date",
    "source_author_or_org",
    "claim_excerpt_or_paraphrase",
    "paraphrase_boundary",
    "allowed_carry",
    "blocked_carry",
    "independent_evidence_required",
    "measurement_package_required",
    "promotion_blockers",
]

SOURCE_TYPE_GUIDANCE = {
    "methodology_claim": {
        "source_type": "paper_or_methodology_document",
        "paraphrase_boundary": "May describe the method and evaluation protocol; may not imply independent silicon validation.",
        "measurement_package_required": ["workload", "baseline", "method", "energy", "thermal", "yield", "pdn_pvt", "independent"],
    },
    "reported_metric": {
        "source_type": "reported_metric_or_company_claim",
        "paraphrase_boundary": "May record disclosed metric language; must preserve metric scope and denominator.",
        "measurement_package_required": ["workload", "baseline", "method", "energy", "thermal", "yield", "pdn_pvt", "independent"],
    },
    "roadmap_projection": {
        "source_type": "roadmap_or_forward_projection",
        "paraphrase_boundary": "May record projected target only; must not convert projection into achieved result.",
        "measurement_package_required": ["roadmap_source", "target_date", "achieved_result_evidence", "independent"],
    },
    "media_interpretation": {
        "source_type": "media_or_public_interpretation",
        "paraphrase_boundary": "May record narrative framing only; must not treat narrative as independent technical validation.",
        "measurement_package_required": ["primary_source_trace", "independent", "benchmark_method", "uncertainty"],
    },
    "architecture_interpretation": {
        "source_type": "architecture_inference_or_interpretation",
        "paraphrase_boundary": "May motivate an architecture hypothesis; must not claim measured speedup without workload and method evidence.",
        "measurement_package_required": ["workload", "baseline", "route_length_or_latency", "energy", "thermal", "closure", "yield", "independent"],
    },
    "independent_evidence": {
        "source_type": "independent_measurement_or_reproduction",
        "paraphrase_boundary": "May support stronger class only if method, uncertainty, and baseline are available.",
        "measurement_package_required": ["workload", "baseline", "method", "uncertainty", "reproduction", "negative_controls"],
    },
    "unknown_or_unresolved": {
        "source_type": "unresolved_source",
        "paraphrase_boundary": "May not carry technical promotion until source category is resolved.",
        "measurement_package_required": ["source_url", "source_type", "primary_source_trace"],
    },
}

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_source_entries():
    if not SOURCE_LEDGER.exists():
        raise FileNotFoundError(f"missing source ledger: {SOURCE_LEDGER}")
    ledger = json.loads(SOURCE_LEDGER.read_text(encoding="utf-8"))
    entries = ledger.get("entries", [])
    if not entries:
        raise RuntimeError("source ledger has no entries")
    return entries

def build_card(entry):
    cat = entry.get("source_category", "unknown_or_unresolved")
    guidance = SOURCE_TYPE_GUIDANCE.get(cat, SOURCE_TYPE_GUIDANCE["unknown_or_unresolved"])
    card = {
        "schema": "tau-scaling-source-evidence-intake-card-v0.8.6",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_id": entry.get("claim_id"),
        "claim_title": entry.get("title"),
        "current_class": entry.get("current_class"),
        "source_category": cat,
        "source_url": "TODO: add primary source URL",
        "source_title": "TODO: add source title",
        "source_type": guidance["source_type"],
        "source_date": "TODO: add publication/disclosure date",
        "source_author_or_org": "TODO: add author or organization",
        "claim_excerpt_or_paraphrase": "TODO: add short quote or bounded paraphrase; avoid unsupported expansion",
        "paraphrase_boundary": guidance["paraphrase_boundary"],
        "allowed_carry": entry.get("allowed_carry"),
        "blocked_carry": entry.get("blocked_carry", []),
        "independent_evidence_required": True,
        "measurement_package_required": guidance["measurement_package_required"],
        "promotion_blockers": entry.get("promotion_blockers", []),
        "intake_status": "TEMPLATE_NEEDS_SOURCE",
        "source_complete": False,
        "ready_for_promotion_review": False,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "boundary": "Source intake cards collect provenance requirements only. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }
    missing = [field for field in REQUIRED_FIELDS if not card.get(field)]
    card["missing_required_fields"] = missing
    return card

def score_card(card):
    hard_todos = sum(1 for k in ["source_url", "source_title", "source_date", "source_author_or_org", "claim_excerpt_or_paraphrase"] if str(card.get(k, "")).startswith("TODO"))
    blockers = len(card.get("promotion_blockers", []))
    complete = hard_todos == 0 and blockers == 0
    return {
        "claim_id": card["claim_id"],
        "source_category": card["source_category"],
        "intake_status": card["intake_status"],
        "todo_fields": hard_todos,
        "promotion_blocker_count": blockers,
        "source_complete": complete,
        "ready_for_promotion_review": False,
    }

def make_svg(scores):
    cats = {}
    for s in scores:
        cats[s["source_category"]] = cats.get(s["source_category"], 0) + 1
    y = 170
    rows = []
    colors = ["#22c55e", "#a78bfa", "#f59e0b", "#fb7185", "#67e8f9", "#94a3b8"]
    for i, (cat, count) in enumerate(sorted(cats.items())):
        w = max(80, count * 110)
        color = colors[i % len(colors)]
        rows.append(f'<text x="80" y="{y+25}" fill="#e5e7eb" font-size="22" font-family="Segoe UI">{cat}</text>')
        rows.append(f'<rect x="560" y="{y}" width="{w}" height="34" rx="10" fill="{color}"/>')
        rows.append(f'<text x="{580+w}" y="{y+25}" fill="#f8fafc" font-size="22" font-family="Segoe UI">{count}</text>')
        y += 62
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720"><rect width="1400" height="720" fill="#030712"/><text x="700" y="72" text-anchor="middle" fill="#67e8f9" font-size="44" font-family="Segoe UI" font-weight="700">Source Evidence Intake Cards v0.8.6</text><text x="700" y="116" text-anchor="middle" fill="#cbd5e1" font-size="23" font-family="Segoe UI">Source cards are templates until primary source details are filled</text>' + "".join(rows) + '<text x="700" y="680" text-anchor="middle" fill="#94a3b8" font-size="20" font-family="Segoe UI">Intake cards collect provenance. They do not promote claims.</text></svg>'

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    entries = load_source_entries()
    cards = [build_card(e) for e in entries]
    scores = [score_card(c) for c in cards]

    for card in cards:
        write_json(CARD_DIR / f"{card['claim_id']}_intake_card.json", card)

    source_complete_count = sum(1 for s in scores if s["source_complete"])
    ready_count = sum(1 for s in scores if s["ready_for_promotion_review"])
    avg_todo = round(mean([s["todo_fields"] for s in scores]), 4) if scores else 0.0

    summary = {
        "schema": "tau-scaling-source-evidence-intake-cards-v0.8.6",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_count": len(cards),
        "source_complete_count": source_complete_count,
        "ready_for_promotion_review_count": ready_count,
        "average_todo_fields": avg_todo,
        "scores": scores,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "claim_promotion_allowed": False,
        "boundary": "Source evidence intake cards are templates for source discipline. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "source_evidence_intake_cards_v0_8_6.json", summary)
    write_json(REPORT_DIR / "latest_source_evidence_intake_cards.json", summary)

    md = "# Source Evidence Intake Cards v0.8.6\n\n"
    md += "## Purpose\n\nConvert the v0.8.5 Public Source Ledger into concrete intake cards that require primary source details before any stronger source-carry claim can be considered.\n\n"
    md += "## Summary\n\n"
    md += f"- Claim count: `{len(cards)}`\n"
    md += f"- Source-complete cards: `{source_complete_count}`\n"
    md += f"- Ready for promotion review: `{ready_count}`\n"
    md += f"- Average TODO fields: `{avg_todo}`\n\n"
    md += "## Card Table\n\n"
    md += "| Claim | Source category | Intake status | TODO fields | Promotion blockers |\n|---|---|---|---:|---:|\n"
    for card, score in zip(cards, scores):
        md += f"| `{card['claim_id']}` | {card['source_category']} | {card['intake_status']} | {score['todo_fields']} | {score['promotion_blocker_count']} |\n"
    md += "\n## Required Intake Fields\n\n"
    for f in REQUIRED_FIELDS:
        md += f"- `{f}`\n"
    md += "\n## Visual\n\n![Source evidence intake cards](../../visuals/source_evidence_intake/v0_8_6/source_evidence_intake_cards.svg)\n\n"
    md += "## Boundary\n\n" + summary["boundary"] + "\n"
    write(REPORT_DIR / "source_evidence_intake_cards_v0_8_6.md", md)
    write(REPORT_DIR / "latest_source_evidence_intake_cards.md", md)

    write(REPORT_DIR / "README.md", "# Source Evidence Intake Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.6 - Source Evidence Intake Cards**\n\n## Purpose\n\nThis folder stores source-intake cards generated from public source provenance records.\n\n## Primary command\n\n```powershell\npython scripts/benchmarks/generate_source_evidence_intake_cards.py\n```\n\n## README Update Rule\n\nUpdate this mini README whenever source intake schemas, card fields, or source requirements change.\n\nBoundary: source intake is not claim validation.\n")
    write(VIS_DIR / "README.md", "# v0.8.6 Source Evidence Intake Visuals\n\nCharts:\n\n- `source_evidence_intake_cards.svg`\n\nBoundary: intake visualization only.\n")
    write(VIS_DIR / "source_evidence_intake_cards.svg", make_svg(scores))

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "source_complete_count": summary["source_complete_count"],
        "ready_for_promotion_review_count": summary["ready_for_promotion_review_count"],
        "average_todo_fields": summary["average_todo_fields"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "report": "reports/source_evidence_intake/latest_source_evidence_intake_cards.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()