from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
INTAKE_CARD_DIR = ROOT / "reports" / "source_evidence_intake" / "cards"
SOURCE_DIR = ROOT / "sources" / "primary_source_intake"
MANIFEST_PATH = SOURCE_DIR / "source_seed_manifest_v0_8_7.json"
REPORT_DIR = ROOT / "reports" / "primary_source_intake"
VIS_DIR = ROOT / "visuals" / "primary_source_intake" / "v0_8_7"

REQUIRED_POPULATION_FIELDS = [
    "source_url",
    "source_title",
    "source_type",
    "source_date",
    "source_author_or_org",
    "claim_excerpt_or_paraphrase",
    "paraphrase_boundary",
]

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def is_filled(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        s = value.strip()
        return bool(s) and not s.upper().startswith("TODO") and s.upper() not in {"TBD", "UNSET", "MISSING"}
    if isinstance(value, list):
        return bool(value)
    return True

def load_cards():
    if not INTAKE_CARD_DIR.exists():
        raise FileNotFoundError(f"missing intake card directory: {INTAKE_CARD_DIR}")
    cards = []
    for path in sorted(INTAKE_CARD_DIR.glob("*_intake_card.json")):
        cards.append(json.loads(path.read_text(encoding="utf-8")))
    if not cards:
        raise RuntimeError("no source intake cards found")
    return cards

def default_manifest(cards):
    entries = []
    for card in cards:
        entries.append({
            "claim_id": card["claim_id"],
            "claim_title": card.get("claim_title"),
            "current_class": card.get("current_class"),
            "source_category": card.get("source_category"),
            "source_url": "TODO: paste primary source URL",
            "source_title": "TODO: paste exact source title",
            "source_type": card.get("source_type", "TODO"),
            "source_date": "TODO: YYYY-MM-DD or source date string",
            "source_author_or_org": "TODO: source author or organization",
            "claim_excerpt_or_paraphrase": "TODO: quote <=25 words or bounded paraphrase",
            "paraphrase_boundary": card.get("paraphrase_boundary", "TODO: define paraphrase boundary"),
            "source_confidence": 0.0,
            "primary_source_confirmed": False,
            "independent_source_confirmed": False,
            "notes": "Fill manually after source review. Do not infer beyond the source boundary.",
        })
    return {
        "schema": "tau-scaling-primary-source-seed-manifest-v0.8.7",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "purpose": "Manual intake queue for primary source details. This file is intentionally TODO-filled until sources are reviewed.",
        "entries": entries,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
    }

def ensure_manifest(cards):
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    if not MANIFEST_PATH.exists():
        manifest = default_manifest(cards)
        write_json(MANIFEST_PATH, manifest)
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

def evaluate_entry(entry):
    filled = [field for field in REQUIRED_POPULATION_FIELDS if is_filled(entry.get(field))]
    missing = [field for field in REQUIRED_POPULATION_FIELDS if field not in filled]
    complete = len(missing) == 0 and bool(entry.get("primary_source_confirmed")) and float(entry.get("source_confidence", 0.0)) >= 0.70
    return {
        "claim_id": entry["claim_id"],
        "source_category": entry.get("source_category"),
        "filled_fields": len(filled),
        "missing_fields": missing,
        "primary_source_confirmed": bool(entry.get("primary_source_confirmed")),
        "independent_source_confirmed": bool(entry.get("independent_source_confirmed")),
        "source_confidence": float(entry.get("source_confidence", 0.0)),
        "source_populated": complete,
        "ready_for_claim_review": False,
    }

def make_svg(scores):
    populated = sum(1 for s in scores if s["source_populated"])
    total = len(scores)
    queued = total - populated
    queued_w = max(1, queued) * 95
    pop_w = max(1, populated) * 95
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720">',
        '<rect width="1400" height="720" fill="#030712"/>',
        '<text x="700" y="78" text-anchor="middle" fill="#67e8f9" font-size="44" font-family="Segoe UI" font-weight="700">Primary Source Intake Queue v0.8.7</text>',
        '<text x="700" y="122" text-anchor="middle" fill="#cbd5e1" font-size="22" font-family="Segoe UI">Sources are queued until manually populated and confirmed</text>',
        f'<rect x="220" y="220" width="{queued_w}" height="54" rx="14" fill="#f59e0b"/>',
        f'<text x="220" y="205" fill="#f8fafc" font-size="25" font-family="Segoe UI">Queued / TODO: {queued}</text>',
        f'<rect x="220" y="360" width="{pop_w}" height="54" rx="14" fill="#22c55e"/>',
        f'<text x="220" y="345" fill="#f8fafc" font-size="25" font-family="Segoe UI">Source-populated: {populated}</text>',
        '<text x="700" y="640" text-anchor="middle" fill="#94a3b8" font-size="21" font-family="Segoe UI">Queue creation is not source validation and does not promote claims.</text>',
        '</svg>',
    ]
    return "\n".join(parts)

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    cards = load_cards()
    manifest = ensure_manifest(cards)
    entries = manifest.get("entries", [])
    scores = [evaluate_entry(e) for e in entries]

    source_populated_count = sum(1 for s in scores if s["source_populated"])
    ready_count = sum(1 for s in scores if s["ready_for_claim_review"])
    avg_filled = round(mean([s["filled_fields"] for s in scores]), 4) if scores else 0.0
    avg_conf = round(mean([s["source_confidence"] for s in scores]), 4) if scores else 0.0

    summary = {
        "schema": "tau-scaling-primary-source-intake-queue-v0.8.7",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest": str(MANIFEST_PATH.relative_to(ROOT)),
        "claim_count": len(entries),
        "source_populated_count": source_populated_count,
        "ready_for_claim_review_count": ready_count,
        "average_filled_fields": avg_filled,
        "average_source_confidence": avg_conf,
        "scores": scores,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "Primary source intake queue prepares manual source population only. It does not invent sources, validate sources, promote claims, validate silicon, validate products, or establish a universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "primary_source_intake_queue_v0_8_7.json", summary)
    write_json(REPORT_DIR / "latest_primary_source_intake_queue.json", summary)

    md = "# Primary Source Intake Queue v0.8.7\n\n"
    md += "## Purpose\n\nCreate a governed manual queue for filling source-intake cards with primary-source details.\n\n"
    md += "## Summary\n\n"
    md += f"- Claim count: `{len(entries)}`\n"
    md += f"- Source-populated count: `{source_populated_count}`\n"
    md += f"- Ready for claim review: `{ready_count}`\n"
    md += f"- Average filled fields: `{avg_filled}`\n"
    md += f"- Average source confidence: `{avg_conf}`\n"
    md += f"- Manifest: `{summary['manifest']}`\n\n"
    md += "## Queue Table\n\n"
    md += "| Claim | Source category | Filled fields | Missing fields | Primary confirmed | Source populated |\n|---|---|---:|---|---:|---:|\n"
    for s in scores:
        md += f"| `{s['claim_id']}` | {s['source_category']} | {s['filled_fields']} | {', '.join(s['missing_fields'])} | {s['primary_source_confirmed']} | {s['source_populated']} |\n"
    md += "\n## Required Manual Population Fields\n\n"
    for field in REQUIRED_POPULATION_FIELDS:
        md += f"- `{field}`\n"
    md += "\n## Visual\n\n![Primary source intake queue](../../visuals/primary_source_intake/v0_8_7/primary_source_intake_queue.svg)\n\n"
    md += "## Boundary\n\n" + summary["boundary"] + "\n"
    write(REPORT_DIR / "primary_source_intake_queue_v0_8_7.md", md)
    write(REPORT_DIR / "latest_primary_source_intake_queue.md", md)

    write(REPORT_DIR / "README.md", "# Primary Source Intake Queue Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.7 - Primary Source Intake Queue / Source Population Scaffold**\n\n## Purpose\n\nThis folder stores the manual source-population queue generated from source evidence intake cards.\n\n## Primary command\n\n```powershell\npython scripts/benchmarks/run_primary_source_intake_queue.py\n```\n\n## README Update Rule\n\nUpdate this mini README whenever primary-source population fields or queue rules change.\n\nBoundary: source queueing is not source validation or claim promotion.\n")
    write(VIS_DIR / "README.md", "# v0.8.7 Primary Source Intake Visuals\n\nCharts:\n\n- `primary_source_intake_queue.svg`\n\nBoundary: queue visualization only.\n")
    write(VIS_DIR / "primary_source_intake_queue.svg", make_svg(scores))

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "source_populated_count": summary["source_populated_count"],
        "ready_for_claim_review_count": summary["ready_for_claim_review_count"],
        "average_filled_fields": summary["average_filled_fields"],
        "average_source_confidence": summary["average_source_confidence"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "source_validation_claimed": summary["source_validation_claimed"],
        "report": "reports/primary_source_intake/latest_primary_source_intake_queue.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()