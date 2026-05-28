from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
CLAIM_DIR = ROOT / "claims" / "public_tau"
REPORT_DIR = ROOT / "reports" / "public_source_ledger"
VIS_DIR = ROOT / "visuals" / "public_source_ledger" / "v0_8_5"
REFLECTION_DIR = ROOT / "docs" / "reflection"

SOURCE_CATEGORIES = [
    "methodology_claim",
    "reported_metric",
    "roadmap_projection",
    "media_interpretation",
    "architecture_interpretation",
    "independent_evidence",
    "unknown_or_unresolved",
]

DEFAULT_SOURCES = {
    "tau-public-001-methodology": {
        "source_category": "methodology_claim",
        "source_boundary": "Allowed to describe a claim-evaluation method; not allowed to imply independent silicon validation.",
        "allowed_carry": "methodology framing",
        "blocked_carry": ["silicon validation", "product proof", "benchmark superiority", "universal Tau law"],
        "provenance_confidence": 0.65,
    },
    "tau-public-002-logicfolding": {
        "source_category": "architecture_interpretation",
        "source_boundary": "Allowed to motivate LogicFolding plausibility testing; not allowed to prove measured timing gain without workload/baseline/method data.",
        "allowed_carry": "mechanism hypothesis and plausibility regime testing",
        "blocked_carry": ["measured gain", "full-chip win", "energy-normalized improvement without data"],
        "provenance_confidence": 0.55,
    },
    "tau-public-003-density-equivalent": {
        "source_category": "reported_metric",
        "source_boundary": "Allowed to record reported density-equivalence language; not allowed to equate density equivalence with process-node equivalence.",
        "allowed_carry": "reported metric requiring normalization",
        "blocked_carry": ["node equivalence", "manufacturing capability proof", "yield proof"],
        "provenance_confidence": 0.55,
    },
    "tau-public-004-roadmap-1p4nm-class": {
        "source_category": "roadmap_projection",
        "source_boundary": "Allowed to record roadmap projection; not allowed to treat projection as achieved product result.",
        "allowed_carry": "roadmap hypothesis",
        "blocked_carry": ["achieved silicon result", "process-node equivalence", "near-term certainty"],
        "provenance_confidence": 0.45,
    },
    "tau-public-005-unified-bus": {
        "source_category": "architecture_interpretation",
        "source_boundary": "Allowed to evaluate architectural communication hypothesis; not allowed to claim workload improvement without latency/bandwidth/energy evidence.",
        "allowed_carry": "architecture hypothesis",
        "blocked_carry": ["end-to-end speedup proof", "energy-normalized improvement", "product validation"],
        "provenance_confidence": 0.5,
    },
    "tau-public-006-hione-optical-io": {
        "source_category": "reported_metric",
        "source_boundary": "Allowed to record I/O or interconnect acceleration claim; not allowed to infer full workload improvement without integration data.",
        "allowed_carry": "I/O claim requiring integration evidence",
        "blocked_carry": ["full-system proof", "workload proof", "thermal/yield proof"],
        "provenance_confidence": 0.5,
    },
    "tau-public-007-3d-folding": {
        "source_category": "architecture_interpretation",
        "source_boundary": "Allowed to test topology/path-shortening plausibility; not allowed to ignore vertical overhead, closure, thermal, and yield burdens.",
        "allowed_carry": "topology hypothesis",
        "blocked_carry": ["automatic speedup", "full-chip timing proof", "manufacturing proof"],
        "provenance_confidence": 0.55,
    },
    "tau-public-008-ai-gap-closure": {
        "source_category": "media_interpretation",
        "source_boundary": "Allowed to record public competitiveness narrative; not allowed to treat narrative as independent benchmark evidence.",
        "allowed_carry": "public narrative requiring source separation",
        "blocked_carry": ["independent validation", "product superiority", "investment or market proof"],
        "provenance_confidence": 0.35,
    },
}

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def infer_category(claim_id: str, title: str) -> str:
    s = (claim_id + " " + title).lower()
    if "roadmap" in s or "1p4" in s:
        return "roadmap_projection"
    if "gap" in s or "compet" in s:
        return "media_interpretation"
    if "density" in s or "metric" in s or "io" in s or "optical" in s:
        return "reported_metric"
    if "logic" in s or "bus" in s or "3d" in s or "fold" in s or "topolog" in s:
        return "architecture_interpretation"
    return "methodology_claim"

def load_claims():
    claims = []
    if CLAIM_DIR.exists():
        for path in sorted(CLAIM_DIR.glob("*.json")):
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
                claim_id = obj.get("claim_id") or obj.get("id") or path.stem
                title = obj.get("title") or obj.get("claim") or claim_id
                current_class = obj.get("current_class") or obj.get("tsek_class") or obj.get("classification") or "TSEK-C"
                category = obj.get("source_category") or infer_category(claim_id, title)
                base = DEFAULT_SOURCES.get(claim_id, {})
                claims.append({
                    "claim_id": claim_id,
                    "title": title,
                    "current_class": current_class,
                    "source_category": base.get("source_category", category),
                    "source_boundary": base.get("source_boundary", "Source boundary unresolved; claim may only be treated as a public claim card pending provenance review."),
                    "allowed_carry": base.get("allowed_carry", "bounded public-claim classification"),
                    "blocked_carry": base.get("blocked_carry", ["silicon validation", "product validation", "benchmark superiority", "universal Tau law"]),
                    "provenance_confidence": base.get("provenance_confidence", 0.25),
                    "source_path": str(path.relative_to(ROOT)),
                    "requires_source_url": True,
                    "requires_primary_source": True,
                    "requires_independent_source_for_promotion": True,
                })
            except Exception:
                pass
    if claims:
        return claims

    # fallback if claim JSONs are absent
    return [
        {
            "claim_id": cid,
            "title": cid.replace("-", " "),
            "current_class": "TSEK-C" if cid not in {"tau-public-004-roadmap-1p4nm-class", "tau-public-008-ai-gap-closure"} else "TSEK-D",
            "source_category": spec["source_category"],
            "source_boundary": spec["source_boundary"],
            "allowed_carry": spec["allowed_carry"],
            "blocked_carry": spec["blocked_carry"],
            "provenance_confidence": spec["provenance_confidence"],
            "source_path": "synthetic/default",
            "requires_source_url": True,
            "requires_primary_source": True,
            "requires_independent_source_for_promotion": True,
        }
        for cid, spec in DEFAULT_SOURCES.items()
    ]

def class_promotion_blockers(entry):
    blockers = []
    if entry["source_category"] in {"roadmap_projection", "media_interpretation"}:
        blockers.append("source category cannot carry achieved-result claims")
    if entry["requires_primary_source"]:
        blockers.append("primary source URL / citation required")
    if entry["requires_independent_source_for_promotion"]:
        blockers.append("independent corroboration required before promotion")
    if entry["current_class"] in {"TSEK-C", "TSEK-D", "TSEK-E"}:
        blockers.append("current evidence class remains bounded")
    return blockers

def make_svg(entries):
    colors = {
        "methodology_claim": "#67e8f9",
        "reported_metric": "#a78bfa",
        "roadmap_projection": "#f59e0b",
        "media_interpretation": "#fb7185",
        "architecture_interpretation": "#22c55e",
        "independent_evidence": "#10b981",
        "unknown_or_unresolved": "#94a3b8",
    }
    counts = {}
    for e in entries:
        counts[e["source_category"]] = counts.get(e["source_category"], 0) + 1
    rows = []
    y = 170
    for cat in SOURCE_CATEGORIES:
        c = counts.get(cat, 0)
        if c == 0:
            continue
        w = 110 * c
        rows.append(f'<text x="80" y="{y+25}" fill="#e5e7eb" font-size="22" font-family="Segoe UI">{cat}</text>')
        rows.append(f'<rect x="520" y="{y}" width="{w}" height="34" rx="10" fill="{colors.get(cat, "#94a3b8")}"/>')
        rows.append(f'<text x="{540+w}" y="{y+25}" fill="#f8fafc" font-size="22" font-family="Segoe UI">{c}</text>')
        y += 62
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720"><rect width="1400" height="720" fill="#030712"/><text x="700" y="72" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Public Source Ledger v0.8.5</text><text x="700" y="116" text-anchor="middle" fill="#cbd5e1" font-size="23" font-family="Segoe UI">Claim provenance categories and source-carry boundaries</text>' + "".join(rows) + '<text x="700" y="680" text-anchor="middle" fill="#94a3b8" font-size="20" font-family="Segoe UI">Source provenance maps claim boundaries only. It does not promote claims or validate silicon.</text></svg>'

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    REFLECTION_DIR.mkdir(parents=True, exist_ok=True)

    entries = load_claims()
    for e in entries:
        e["promotion_blockers"] = class_promotion_blockers(e)
        write_json(REPORT_DIR / "claim_sources" / f"{e['claim_id']}_source_record.json", e)

    counts = {}
    for e in entries:
        counts[e["source_category"]] = counts.get(e["source_category"], 0) + 1
    avg_conf = round(mean([float(e["provenance_confidence"]) for e in entries]), 4) if entries else 0.0

    summary = {
        "schema": "tau-scaling-public-source-ledger-v0.8.5",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_count": len(entries),
        "source_category_counts": counts,
        "average_provenance_confidence": avg_conf,
        "entries": entries,
        "law_of_sufficient_form": {
            "law": "When enough governed form is in place, structure begins to hold itself.",
            "operational_form": "A system becomes self-stabilizing when its claims, evidence, routing, validation, memory, and non-claim locks are all visible to both humans and agents.",
        },
        "research_finding": "Public Tau claims now have a provenance map separating methodology, reported metrics, roadmap projections, media interpretation, architecture interpretation, and independent evidence requirements.",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "Source provenance maps source-carry boundaries only. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "public_source_ledger_v0_8_5.json", summary)
    write_json(REPORT_DIR / "latest_public_source_ledger.json", summary)

    md = "# Public Source Ledger / Claim Provenance Map v0.8.5\n\n"
    md += "## Purpose\n\nTie each public Tau claim to a source category, source boundary, and allowed/blocked source-carry rule.\n\n"
    md += "## Source Category Summary\n\n"
    md += "| Source category | Count |\n|---|---:|\n"
    for cat, count in sorted(counts.items()):
        md += f"| {cat} | {count} |\n"
    md += f"\nAverage provenance confidence: `{avg_conf}`\n\n"
    md += "## Claim Provenance Table\n\n"
    md += "| Claim | Current class | Source category | Allowed carry | Promotion blockers |\n|---|---|---|---|---|\n"
    for e in entries:
        blockers = "; ".join(e["promotion_blockers"])
        md += f"| `{e['claim_id']}` | {e['current_class']} | {e['source_category']} | {e['allowed_carry']} | {blockers} |\n"
    md += "\n## Law of Sufficient Form\n\n"
    md += "> When enough governed form is in place, structure begins to hold itself.\n\n"
    md += "Operational form: A system becomes self-stabilizing when its claims, evidence, routing, validation, memory, and non-claim locks are all visible to both humans and agents.\n\n"
    md += "## Visual\n\n![Public source ledger](../../visuals/public_source_ledger/v0_8_5/public_source_ledger.svg)\n\n"
    md += "## Boundary\n\n" + summary["boundary"] + "\n"
    write(REPORT_DIR / "public_source_ledger_v0_8_5.md", md)
    write(REPORT_DIR / "latest_public_source_ledger.md", md)

    write(REPORT_DIR / "README.md", "# Public Source Ledger Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map**\n\n## Purpose\n\nThis folder stores source provenance records and source-carry boundary reports for public Tau claims.\n\n## Primary command\n\n```powershell\npython scripts/benchmarks/generate_public_source_ledger.py\n```\n\n## README Update Rule\n\nUpdate this mini README whenever public claim provenance, source categories, or source-carry boundaries change.\n\nBoundary: source provenance is not claim validation.\n")
    write(VIS_DIR / "README.md", "# v0.8.5 Public Source Ledger Visuals\n\nCharts:\n\n- `public_source_ledger.svg`\n\nBoundary: provenance visualization only.\n")
    write(VIS_DIR / "public_source_ledger.svg", make_svg(entries))

    reflection = "# Reflection: Law of Sufficient Form\n\n"
    reflection += "## Law\n\n"
    reflection += "When enough governed form is in place, structure begins to hold itself.\n\n"
    reflection += "## Operational Form\n\n"
    reflection += "A system becomes self-stabilizing when its claims, evidence, routing, validation, memory, and non-claim locks are all visible to both humans and agents.\n\n"
    reflection += "## Tau Scaling Context\n\n"
    reflection += "This reflection was added at v0.8.5 after the repo established a claim ledger, plausibility sweep, evidence sufficiency matrix, README information architecture compression, Nexus surface synchronization, and zero-finding release readiness.\n\n"
    reflection += "The law is reflective and operational. It does not prove correctness by itself. It names the condition under which repository structure can begin to preserve orientation across humans and agents.\n\n"
    reflection += "## Boundary\n\nReflection is repository memory and process insight. It is not silicon validation, product validation, benchmark superiority proof, or universal Tau Scaling proof.\n"
    write(REFLECTION_DIR / "law_of_sufficient_form_v0_8_5.md", reflection)

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "source_category_counts": summary["source_category_counts"],
        "average_provenance_confidence": summary["average_provenance_confidence"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "report": "reports/public_source_ledger/latest_public_source_ledger.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()