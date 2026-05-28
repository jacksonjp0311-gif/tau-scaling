from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
POP_MANIFEST = ROOT / "sources" / "primary_source_intake" / "source_population_manifest_v0_8_8.json"
REPORT_DIR = ROOT / "reports" / "primary_source_gap_review"
BRIEF_DIR = ROOT / "reports" / "publishable_findings"
VIS_DIR = ROOT / "visuals" / "primary_source_gap_review" / "v0_8_9"

PRIMARY_REQUIREMENTS_BY_CATEGORY = {
    "methodology_claim": [
        "first-party Huawei/HiSilicon methodology document or conference paper",
        "formal definition of Tau Scaling terms and equations",
        "scope statement separating architecture method from measured validation",
    ],
    "architecture_interpretation": [
        "first-party LogicFolding architecture disclosure",
        "physical-design or packaging description",
        "latency / interconnect / data-movement measurement protocol",
        "thermal / power / PDN / PVT disclosure",
    ],
    "reported_metric": [
        "first-party metric definition and denominator",
        "baseline and candidate measurement method",
        "energy-normalized measurement",
        "uncertainty or reproducibility statement",
    ],
    "roadmap_projection": [
        "first-party roadmap source",
        "date-bound target statement",
        "separation of roadmap target from achieved result",
        "intermediate milestone evidence",
    ],
    "media_interpretation": [
        "primary-source trace for each media interpretation",
        "independent benchmark or reproduction before any promotion",
        "clear separation between narrative and technical evidence",
    ],
}

COMMON_GATES = [
    "declared workload",
    "baseline artifact",
    "candidate artifact",
    "measurement method",
    "energy companion",
    "thermal companion",
    "yield / manufacturing evidence",
    "PDN / PVT robustness",
    "independent reproduction",
    "negative controls",
]

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_population():
    if not POP_MANIFEST.exists():
        raise FileNotFoundError(f"missing v0.8.8 source population manifest: {POP_MANIFEST}")
    obj = json.loads(POP_MANIFEST.read_text(encoding="utf-8"))
    entries = obj.get("entries", [])
    if not entries:
        raise RuntimeError("source population manifest has no entries")
    return obj, entries

def score_gap(entry):
    category = entry.get("source_category", "unknown_or_unresolved")
    primary_reqs = PRIMARY_REQUIREMENTS_BY_CATEGORY.get(category, [
        "source category resolution",
        "primary-source trace",
        "independent corroboration",
    ])
    source_records = entry.get("source_records", [])
    primary_confirmed = bool(entry.get("primary_source_confirmed"))
    independent_confirmed = bool(entry.get("independent_source_confirmed"))
    populated = bool(entry.get("source_populated"))

    missing_primary = [] if primary_confirmed else primary_reqs
    missing_independent = [] if independent_confirmed else ["independent reproduction or third-party measurement"]
    missing_common = list(COMMON_GATES)

    gap_count = len(missing_primary) + len(missing_independent) + len(missing_common)
    source_count = len(source_records)
    secondary_only = populated and not primary_confirmed

    # This is a gap score, not a claim score: high means more missing validation layers.
    gap_severity = "HIGH"
    if primary_confirmed and independent_confirmed:
        gap_severity = "MEDIUM"
    if primary_confirmed and independent_confirmed and not missing_common:
        gap_severity = "LOW"

    return {
        "claim_id": entry.get("claim_id"),
        "claim_title": entry.get("claim_title"),
        "current_class": entry.get("current_class"),
        "source_category": category,
        "source_records_count": source_count,
        "source_populated": populated,
        "secondary_source_only": secondary_only,
        "primary_source_confirmed": primary_confirmed,
        "independent_source_confirmed": independent_confirmed,
        "source_confidence": float(entry.get("source_confidence", 0.0)),
        "missing_primary_requirements": missing_primary,
        "missing_independent_requirements": missing_independent,
        "missing_common_evidence_gates": missing_common,
        "gap_count": gap_count,
        "gap_severity": gap_severity,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
    }

def make_svg(rows):
    total = len(rows)
    populated = sum(1 for r in rows if r["source_populated"])
    primary = sum(1 for r in rows if r["primary_source_confirmed"])
    independent = sum(1 for r in rows if r["independent_source_confirmed"])
    high = sum(1 for r in rows if r["gap_severity"] == "HIGH")
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="820" viewBox="0 0 1500 820">',
        '<rect width="1500" height="820" fill="#030712"/>',
        '<text x="750" y="78" text-anchor="middle" fill="#67e8f9" font-size="44" font-family="Segoe UI" font-weight="700">Primary Source Validation Gap Review v0.8.9</text>',
        '<text x="750" y="122" text-anchor="middle" fill="#cbd5e1" font-size="22" font-family="Segoe UI">Public source population is complete; primary and independent validation remain missing</text>',
        f'<text x="180" y="220" fill="#f8fafc" font-size="27" font-family="Segoe UI">Total public claims: {total}</text>',
        f'<rect x="180" y="250" width="{max(1,populated)*105}" height="46" rx="12" fill="#22c55e"/>',
        f'<text x="180" y="335" fill="#f8fafc" font-size="27" font-family="Segoe UI">Source-populated: {populated}</text>',
        f'<rect x="180" y="365" width="{max(1,primary)*105}" height="46" rx="12" fill="#f59e0b"/>',
        f'<text x="180" y="450" fill="#f8fafc" font-size="27" font-family="Segoe UI">Primary-source confirmed: {primary}</text>',
        f'<rect x="180" y="480" width="{max(1,independent)*105}" height="46" rx="12" fill="#a78bfa"/>',
        f'<text x="180" y="565" fill="#f8fafc" font-size="27" font-family="Segoe UI">Independent-source confirmed: {independent}</text>',
        f'<rect x="180" y="595" width="{max(1,high)*105}" height="46" rx="12" fill="#ef4444"/>',
        f'<text x="180" y="680" fill="#f8fafc" font-size="27" font-family="Segoe UI">High validation-gap claims: {high}</text>',
        '<text x="750" y="770" text-anchor="middle" fill="#94a3b8" font-size="21" font-family="Segoe UI">Publishable finding: source-populated but not primary-validated; no claim promotion.</text>',
        '</svg>',
    ])

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    pop, entries = load_population()
    rows = [score_gap(e) for e in entries]

    claim_count = len(rows)
    populated_count = sum(1 for r in rows if r["source_populated"])
    primary_count = sum(1 for r in rows if r["primary_source_confirmed"])
    independent_count = sum(1 for r in rows if r["independent_source_confirmed"])
    secondary_only_count = sum(1 for r in rows if r["secondary_source_only"])
    high_gap_count = sum(1 for r in rows if r["gap_severity"] == "HIGH")
    avg_gap_count = round(mean([r["gap_count"] for r in rows]), 4) if rows else 0.0
    avg_source_conf = round(mean([r["source_confidence"] for r in rows]), 4) if rows else 0.0

    summary = {
        "schema": "tau-scaling-primary-source-validation-gap-review-v0.8.9",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_manifest": str(POP_MANIFEST.relative_to(ROOT)),
        "claim_count": claim_count,
        "source_populated_count": populated_count,
        "secondary_source_only_count": secondary_only_count,
        "primary_source_confirmed_count": primary_count,
        "independent_source_confirmed_count": independent_count,
        "high_gap_claim_count": high_gap_count,
        "average_gap_count": avg_gap_count,
        "average_source_confidence": avg_source_conf,
        "rows": rows,
        "publishable_findings": [
            "All eight public Tau claims are now source-populated from public reporting.",
            "Zero claims have primary-source confirmation in the current repo state.",
            "Zero claims have independent-source confirmation in the current repo state.",
            "The current evidence field supports source-bounded analysis, not claim validation or promotion.",
            "The strongest publishable contribution is a reproducible separation between public narrative, source provenance, validation gaps, and non-claim locks.",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "primary_source_validation_claimed": False,
        "independent_validation_claimed": False,
        "boundary": "v0.8.9 is a primary-source validation gap review. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "primary_source_gap_review_v0_8_9.json", summary)
    write_json(REPORT_DIR / "latest_primary_source_gap_review.json", summary)

    md = "# Primary Source Validation Gap Review v0.8.9\n\n"
    md += "## Purpose\n\nIdentify what primary and independent evidence is still missing after public source population.\n\n"
    md += "## Publishable Summary\n\n"
    for finding in summary["publishable_findings"]:
        md += f"- {finding}\n"
    md += "\n## Metrics\n\n"
    for key in [
        "claim_count",
        "source_populated_count",
        "secondary_source_only_count",
        "primary_source_confirmed_count",
        "independent_source_confirmed_count",
        "high_gap_claim_count",
        "average_gap_count",
        "average_source_confidence",
    ]:
        md += f"- {key}: `{summary[key]}`\n"
    md += "\n## Gap Matrix\n\n"
    md += "| Claim | Source category | Source-populated | Primary confirmed | Independent confirmed | Gap severity | Gap count |\n|---|---|---:|---:|---:|---|---:|\n"
    for r in rows:
        md += f"| `{r['claim_id']}` | {r['source_category']} | {r['source_populated']} | {r['primary_source_confirmed']} | {r['independent_source_confirmed']} | {r['gap_severity']} | {r['gap_count']} |\n"
    md += "\n## Boundary\n\n" + summary["boundary"] + "\n"
    md += "\n## Visual\n\n![Primary source gap review](../../visuals/primary_source_gap_review/v0_8_9/primary_source_gap_review.svg)\n"
    write(REPORT_DIR / "primary_source_gap_review_v0_8_9.md", md)
    write(REPORT_DIR / "latest_primary_source_gap_review.md", md)

    brief = "# Publishable Findings Brief v0.8.9\n\n"
    brief += "## Title\n\nTau Scaling as an Evidence-Gated Public Claim System: Source Population Without Primary Validation\n\n"
    brief += "## Core Finding\n\nThe public Tau Scaling evidence field is source-populatable but not yet primary-source validated or independently reproduced in the current repository state.\n\n"
    brief += "## Quantitative Snapshot\n\n"
    brief += f"- Public claims analyzed: `{claim_count}`\n"
    brief += f"- Source-populated claims: `{populated_count}`\n"
    brief += f"- Primary-source confirmed claims: `{primary_count}`\n"
    brief += f"- Independent-source confirmed claims: `{independent_count}`\n"
    brief += f"- Secondary-source-only claims: `{secondary_only_count}`\n"
    brief += f"- High validation-gap claims: `{high_gap_count}`\n"
    brief += f"- Average source confidence: `{avg_source_conf}`\n\n"
    brief += "## Claim Boundary\n\nThis is publishable as a claim-governance and evidence-provenance result. It is not publishable as silicon validation, product validation, benchmark superiority, or proof of a universal Tau Scaling law.\n\n"
    brief += "## Reproducible Artifacts\n\n"
    brief += "- `sources/primary_source_intake/source_population_manifest_v0_8_8.json`\n"
    brief += "- `reports/primary_source_gap_review/latest_primary_source_gap_review.md`\n"
    brief += "- `reports/public_source_population/latest_public_source_population_pass.md`\n"
    brief += "- `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md`\n"
    brief += "- `reports/release/latest_release_readiness.md`\n"
    write(BRIEF_DIR / "publishable_findings_brief_v0_8_9.md", brief)
    write(BRIEF_DIR / "latest_publishable_findings_brief.md", brief)
    write_json(BRIEF_DIR / "latest_publishable_findings_brief.json", {
        "schema": "tau-scaling-publishable-findings-brief-v0.8.9",
        "generated_at": summary["generated_at"],
        "title": "Tau Scaling as an Evidence-Gated Public Claim System: Source Population Without Primary Validation",
        "metrics": {k: summary[k] for k in [
            "claim_count",
            "source_populated_count",
            "secondary_source_only_count",
            "primary_source_confirmed_count",
            "independent_source_confirmed_count",
            "high_gap_claim_count",
            "average_gap_count",
            "average_source_confidence",
        ]},
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
    })

    write(REPORT_DIR / "README.md", "# Primary Source Gap Review Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.9 - Primary Source Validation Gap Review**\n\n## Purpose\n\nThis folder stores primary-source and independent-validation gap review reports.\n\nBoundary: gap review is not validation or promotion.\n")
    write(BRIEF_DIR / "README.md", "# Publishable Findings Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.9 - Publishable Findings Brief**\n\n## Purpose\n\nThis folder stores publication-facing summaries bounded by evidence and non-claim locks.\n\nBoundary: publishable findings here are claim-governance findings, not silicon validation.\n")
    write(VIS_DIR / "README.md", "# v0.8.9 Primary Source Gap Review Visuals\n\nCharts:\n\n- `primary_source_gap_review.svg`\n\nBoundary: validation-gap visualization only.\n")
    write(VIS_DIR / "primary_source_gap_review.svg", make_svg(rows))

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": claim_count,
        "source_populated_count": populated_count,
        "primary_source_confirmed_count": primary_count,
        "independent_source_confirmed_count": independent_count,
        "high_gap_claim_count": high_gap_count,
        "average_gap_count": avg_gap_count,
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "source_validation_claimed": summary["source_validation_claimed"],
        "report": "reports/primary_source_gap_review/latest_primary_source_gap_review.md",
        "brief": "reports/publishable_findings/latest_publishable_findings_brief.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()