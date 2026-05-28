from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "sources" / "primary_source_intake"
INPUT_MANIFEST = SOURCE_DIR / "source_seed_manifest_v0_8_7.json"
OUTPUT_MANIFEST = SOURCE_DIR / "source_population_manifest_v0_8_8.json"
REPORT_DIR = ROOT / "reports" / "public_source_population"
VIS_DIR = ROOT / "visuals" / "public_source_population" / "v0_8_8"

# Public sources discovered during v0.8.8 review.
# These records are bounded as public / secondary unless primary_source_confirmed is explicitly true.
SOURCE_POOL = {
    "reuters_huawei_tau_2026_05_25": {
        "url": "https://www.reuters.com/world/asia-pacific/huawei-proposes-new-path-chip-development-amid-us-sanctions-2026-05-25/",
        "title": "China's Huawei reveals chip design breakthrough amid US sanctions",
        "source_type": "news_report_public_secondary",
        "date": "2026-05-25",
        "author_or_org": "Reuters",
        "primary_source_confirmed": False,
        "independent_source_confirmed": False,
        "confidence": 0.62,
    },
    "wired_huawei_chip_queen_tau_2026_05_27": {
        "url": "https://www.wired.com/story/huawei-chip-queen-moores-law-tau",
        "title": "Huawei's 'Chip Queen' Throws Down the Gauntlet",
        "source_type": "news_report_public_secondary",
        "date": "2026-05-27",
        "author_or_org": "WIRED",
        "primary_source_confirmed": False,
        "independent_source_confirmed": False,
        "confidence": 0.56,
    },
    "toms_logicfolding_tau_2026_05_25": {
        "url": "https://www.tomshardware.com/tech-industry/semiconductors/huawei-claims-sanctions-busting-breakthrough-with-1-4nm-class-chips-by-2031-claims-55-percent-higher-transistor-density-firm-claims-new-logicfolding-chip-architecture-can-bypass-euv-restrictions-introduces-tau-scaling-law-to-replace-moores-law",
        "title": "Huawei claims sanctions-busting breakthrough with 1.4nm-class chips by 2031",
        "source_type": "technical_media_public_secondary",
        "date": "2026-05-25",
        "author_or_org": "Tom's Hardware",
        "primary_source_confirmed": False,
        "independent_source_confirmed": False,
        "confidence": 0.50,
    },
    "toi_logicfolding_explainer_2026": {
        "url": "https://timesofindia.indiatimes.com/technology/tech-news/explained-what-is-huaweis-logicfolding-tau-scaling-law-and-how-it-plans-to-build-1-4nm-chips-without-asml/articleshow/131314122.cms",
        "title": "Explained: What is Huawei's LogicFolding, Tau Scaling Law, and how it plans to build 1.4nm chips without ASML",
        "source_type": "explainer_public_secondary",
        "date": "2026-05",
        "author_or_org": "Times of India",
        "primary_source_confirmed": False,
        "independent_source_confirmed": False,
        "confidence": 0.42,
    },
    "toms_ascend_roadmap_2025": {
        "url": "https://www.tomshardware.com/tech-industry/semiconductors/huawei-unveils-ascend-roadmap-backed-by-in-house-hbm",
        "title": "Huawei reveals long-range Ascend chip roadmap",
        "source_type": "technical_media_public_secondary",
        "date": "2025",
        "author_or_org": "Tom's Hardware",
        "primary_source_confirmed": False,
        "independent_source_confirmed": False,
        "confidence": 0.45,
    },
}

CLAIM_SOURCE_MAP = {
    "tau-public-001-methodology": {
        "source_ids": ["reuters_huawei_tau_2026_05_25", "wired_huawei_chip_queen_tau_2026_05_27"],
        "claim_excerpt_or_paraphrase": "Huawei presented Tau Scaling as a system-level, time/data-movement scaling principle rather than ordinary transistor shrinking.",
        "allowed_carry": "methodology framing and source-bounded public claim",
        "blocked_carry": ["independent validation", "silicon proof", "universal law"],
    },
    "tau-public-002-logicfolding": {
        "source_ids": ["reuters_huawei_tau_2026_05_25", "toms_logicfolding_tau_2026_05_25", "toi_logicfolding_explainer_2026"],
        "claim_excerpt_or_paraphrase": "LogicFolding is publicly described as a Tau-scaling architecture intended to shorten wiring/data movement.",
        "allowed_carry": "architecture hypothesis and plausibility test target",
        "blocked_carry": ["measured speedup proof", "full-chip validation", "energy-normalized gain without data"],
    },
    "tau-public-003-density-equivalent": {
        "source_ids": ["toms_logicfolding_tau_2026_05_25", "reuters_huawei_tau_2026_05_25"],
        "claim_excerpt_or_paraphrase": "Public reports describe a 1.4nm-class or density-equivalent target, not conventional process-node equivalence.",
        "allowed_carry": "reported metric requiring normalization",
        "blocked_carry": ["node equivalence", "manufacturing validation", "yield proof"],
    },
    "tau-public-004-roadmap-1p4nm-class": {
        "source_ids": ["reuters_huawei_tau_2026_05_25", "toms_logicfolding_tau_2026_05_25"],
        "claim_excerpt_or_paraphrase": "Public reports describe a 2031 target for 1.4nm-class transistor-density equivalence.",
        "allowed_carry": "roadmap projection",
        "blocked_carry": ["achieved product result", "near-term proof", "process-node equivalence"],
    },
    "tau-public-005-unified-bus": {
        "source_ids": ["reuters_huawei_tau_2026_05_25", "wired_huawei_chip_queen_tau_2026_05_27"],
        "claim_excerpt_or_paraphrase": "Public reporting emphasizes improving data movement across chips, circuits, and systems.",
        "allowed_carry": "system data-movement hypothesis",
        "blocked_carry": ["bus implementation proof", "workload proof", "full-system benchmark proof"],
    },
    "tau-public-006-hione-optical-io": {
        "source_ids": ["toms_ascend_roadmap_2025"],
        "claim_excerpt_or_paraphrase": "Public roadmap reporting discusses Huawei AI-chip/system interconnect and memory bandwidth ambitions, but does not confirm this specific claim as primary evidence.",
        "allowed_carry": "related roadmap/context only",
        "blocked_carry": ["specific HiONE validation", "optical I/O proof", "full-system superiority"],
    },
    "tau-public-007-3d-folding": {
        "source_ids": ["toms_logicfolding_tau_2026_05_25", "toi_logicfolding_explainer_2026"],
        "claim_excerpt_or_paraphrase": "Public explainers describe folding/stacking logic as a route to shortening wire lengths.",
        "allowed_carry": "topology/path-shortening hypothesis",
        "blocked_carry": ["automatic speedup", "thermal closure proof", "yield proof"],
    },
    "tau-public-008-ai-gap-closure": {
        "source_ids": ["wired_huawei_chip_queen_tau_2026_05_27", "reuters_huawei_tau_2026_05_25", "toms_ascend_roadmap_2025"],
        "claim_excerpt_or_paraphrase": "Public reports frame Tau Scaling and Ascend roadmaps as part of Huawei's AI-chip competitiveness strategy.",
        "allowed_carry": "public competitiveness narrative",
        "blocked_carry": ["benchmark superiority", "AI gap closure proof", "market or investment conclusion"],
    },
}

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_manifest():
    if not INPUT_MANIFEST.exists():
        raise FileNotFoundError(f"missing v0.8.7 manifest: {INPUT_MANIFEST}")
    return json.loads(INPUT_MANIFEST.read_text(encoding="utf-8"))

def populate_entry(entry):
    claim_id = entry["claim_id"]
    mapping = CLAIM_SOURCE_MAP.get(claim_id, {})
    source_ids = mapping.get("source_ids", [])
    sources = [SOURCE_POOL[sid] | {"source_id": sid} for sid in source_ids]
    primary_confirmed = any(s["primary_source_confirmed"] for s in sources)
    independent_confirmed = any(s["independent_source_confirmed"] for s in sources)
    conf = max([s["confidence"] for s in sources], default=0.0)

    # Preserve original fields but make the population status explicit.
    out = dict(entry)
    out["source_population_version"] = "v0.8.8"
    out["source_records"] = sources
    out["source_url"] = sources[0]["url"] if sources else entry.get("source_url", "TODO: paste primary source URL")
    out["source_title"] = sources[0]["title"] if sources else entry.get("source_title", "TODO: paste exact source title")
    out["source_type"] = sources[0]["source_type"] if sources else entry.get("source_type", "TODO")
    out["source_date"] = sources[0]["date"] if sources else entry.get("source_date", "TODO")
    out["source_author_or_org"] = sources[0]["author_or_org"] if sources else entry.get("source_author_or_org", "TODO")
    out["claim_excerpt_or_paraphrase"] = mapping.get("claim_excerpt_or_paraphrase", entry.get("claim_excerpt_or_paraphrase", "TODO"))
    out["paraphrase_boundary"] = "Bounded paraphrase from public secondary reporting; not a primary-source quote unless primary_source_confirmed is true."
    out["allowed_carry"] = mapping.get("allowed_carry", entry.get("allowed_carry"))
    out["blocked_carry"] = mapping.get("blocked_carry", entry.get("blocked_carry", []))
    out["source_confidence"] = conf
    out["primary_source_confirmed"] = primary_confirmed
    out["independent_source_confirmed"] = independent_confirmed
    out["source_populated"] = bool(sources)
    out["source_validated"] = False
    out["ready_for_claim_review"] = False
    out["claim_promotion_allowed"] = False
    out["notes"] = "Populated from public secondary sources. Primary source and independent validation remain required before promotion review."
    return out

def make_svg(entries):
    populated = sum(1 for e in entries if e.get("source_populated"))
    primary = sum(1 for e in entries if e.get("primary_source_confirmed"))
    total = len(entries)
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720">',
        '<rect width="1400" height="720" fill="#030712"/>',
        '<text x="700" y="78" text-anchor="middle" fill="#67e8f9" font-size="44" font-family="Segoe UI" font-weight="700">Public Source Population Pass v0.8.8</text>',
        '<text x="700" y="122" text-anchor="middle" fill="#cbd5e1" font-size="22" font-family="Segoe UI">Public secondary sources populated; primary validation remains separate</text>',
        f'<text x="220" y="230" fill="#f8fafc" font-size="28" font-family="Segoe UI">Total claims: {total}</text>',
        f'<rect x="220" y="255" width="{max(1, populated)*95}" height="54" rx="14" fill="#22c55e"/>',
        f'<text x="220" y="340" fill="#f8fafc" font-size="28" font-family="Segoe UI">Source-populated: {populated}</text>',
        f'<rect x="220" y="365" width="{max(1, primary)*95}" height="54" rx="14" fill="#f59e0b"/>',
        f'<text x="220" y="450" fill="#f8fafc" font-size="28" font-family="Segoe UI">Primary-source confirmed: {primary}</text>',
        '<text x="700" y="640" text-anchor="middle" fill="#94a3b8" font-size="21" font-family="Segoe UI">Populated does not mean validated. Validated does not mean promoted.</text>',
        '</svg>',
    ])

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    entries = [populate_entry(e) for e in manifest.get("entries", [])]
    populated_count = sum(1 for e in entries if e.get("source_populated"))
    primary_count = sum(1 for e in entries if e.get("primary_source_confirmed"))
    independent_count = sum(1 for e in entries if e.get("independent_source_confirmed"))
    avg_conf = round(mean([float(e.get("source_confidence", 0.0)) for e in entries]), 4) if entries else 0.0

    out_manifest = {
        "schema": "tau-scaling-public-source-population-manifest-v0.8.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_manifest": str(INPUT_MANIFEST.relative_to(ROOT)),
        "entries": entries,
        "source_pool": SOURCE_POOL,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "primary_source_validation_claimed": False,
    }
    write_json(OUTPUT_MANIFEST, out_manifest)

    summary = {
        "schema": "tau-scaling-public-source-population-pass-v0.8.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_count": len(entries),
        "source_populated_count": populated_count,
        "primary_source_confirmed_count": primary_count,
        "independent_source_confirmed_count": independent_count,
        "average_source_confidence": avg_conf,
        "manifest": str(OUTPUT_MANIFEST.relative_to(ROOT)),
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "v0.8.8 populates source records from public secondary sources. It does not claim primary-source validation, source validation, claim promotion, silicon validation, product validation, benchmark superiority, or universal Tau Scaling proof.",
    }
    write_json(REPORT_DIR / "public_source_population_pass_v0_8_8.json", summary)
    write_json(REPORT_DIR / "latest_public_source_population_pass.json", summary)

    md = "# Public Source Population Pass v0.8.8\n\n"
    md += "## Purpose\n\nPopulate the v0.8.7 source queue with bounded public source records discovered during source review.\n\n"
    md += "## Summary\n\n"
    md += f"- Claim count: `{len(entries)}`\n"
    md += f"- Source-populated claims: `{populated_count}`\n"
    md += f"- Primary-source confirmed claims: `{primary_count}`\n"
    md += f"- Independent-source confirmed claims: `{independent_count}`\n"
    md += f"- Average source confidence: `{avg_conf}`\n"
    md += f"- Manifest: `{summary['manifest']}`\n\n"
    md += "## Claim Source Table\n\n"
    md += "| Claim | Populated | Primary confirmed | Source validation claimed | Leading source |\n|---|---:|---:|---:|---|\n"
    for e in entries:
        leading = e.get("source_records", [{}])[0].get("title", "none") if e.get("source_records") else "none"
        md += f"| `{e['claim_id']}` | {e.get('source_populated')} | {e.get('primary_source_confirmed')} | {e.get('source_validated')} | {leading} |\n"
    md += "\n## Boundary\n\n" + summary["boundary"] + "\n"
    md += "\n## Visual\n\n![Public source population](../../visuals/public_source_population/v0_8_8/public_source_population_pass.svg)\n"
    write(REPORT_DIR / "public_source_population_pass_v0_8_8.md", md)
    write(REPORT_DIR / "latest_public_source_population_pass.md", md)

    write(REPORT_DIR / "README.md", "# Public Source Population Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.8 - Public Source Population Pass**\n\n## Purpose\n\nThis folder stores bounded public source population reports.\n\n## README Update Rule\n\nUpdate this mini README whenever public source population rules or source confidence fields change.\n\nBoundary: source population is not source validation or claim promotion.\n")
    write(VIS_DIR / "README.md", "# v0.8.8 Public Source Population Visuals\n\nCharts:\n\n- `public_source_population_pass.svg`\n\nBoundary: source population visualization only.\n")
    write(VIS_DIR / "public_source_population_pass.svg", make_svg(entries))

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "source_populated_count": summary["source_populated_count"],
        "primary_source_confirmed_count": summary["primary_source_confirmed_count"],
        "independent_source_confirmed_count": summary["independent_source_confirmed_count"],
        "average_source_confidence": summary["average_source_confidence"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "source_validation_claimed": summary["source_validation_claimed"],
        "report": "reports/public_source_population/latest_public_source_population_pass.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()