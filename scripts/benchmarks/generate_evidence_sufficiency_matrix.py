from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
CLAIM_DIR = ROOT / "claims" / "public_tau"
REPORT_DIR = ROOT / "reports" / "evidence_sufficiency"
VIS_DIR = ROOT / "visuals" / "evidence_sufficiency" / "v0_8_4"

GATES = ["workload", "baseline", "method", "energy", "thermal", "yield", "pdn_pvt", "independent"]

DEFAULT_CLAIMS = [
    {"claim_id":"tau-public-001-methodology","title":"Tau methodology as a scaling-analysis frame","current_class":"TSEK-C","claim_family":"methodology","missing_gates":["workload","baseline","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-002-logicfolding","title":"LogicFolding reduces effective communication or timing burden","current_class":"TSEK-C","claim_family":"mechanism","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-003-density-equivalent","title":"Density-equivalent improvement claim","current_class":"TSEK-C","claim_family":"metric","missing_gates":["baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-004-roadmap-1p4nm-class","title":"Roadmap projection toward 1.4nm-class competitiveness","current_class":"TSEK-D","claim_family":"roadmap","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-005-unified-bus","title":"Unified bus / cross-layer communication improvement","current_class":"TSEK-C","claim_family":"architecture","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-006-hione-optical-io","title":"HiONE / optical I/O style communication acceleration","current_class":"TSEK-C","claim_family":"io","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-007-3d-folding","title":"3D folding or topology-based path shortening","current_class":"TSEK-C","claim_family":"topology","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
    {"claim_id":"tau-public-008-ai-gap-closure","title":"AI gap closure or competitiveness projection","current_class":"TSEK-D","claim_family":"roadmap","missing_gates":["workload","baseline","method","energy","thermal","yield","pdn_pvt","independent"]},
]

FAMILY_REQUIREMENTS = {
    "methodology": {
        "promote_to_b": ["formal method statement", "declared workload model", "baseline comparator", "repeatable calculation or simulation artifact"],
        "promote_to_a": ["independent reproduction", "cross-workload replication", "public methods package", "adversarial negative controls"],
        "downgrade": ["method cannot reproduce stated class", "undefined baseline", "method changes after result"],
    },
    "mechanism": {
        "promote_to_b": ["post-route timing comparison", "wire-delay reduction estimate", "vertical/routing/sync overhead estimate", "energy/thermal/PDN companion data"],
        "promote_to_a": ["independent silicon or EDA reproduction", "post-route closed design", "measured energy-delay product", "PVT and yield disclosure"],
        "downgrade": ["wire savings erased by overhead", "thermal collapse", "closure failure", "no workload-specific gain"],
    },
    "metric": {
        "promote_to_b": ["exact metric definition", "baseline node/class comparator", "normalization rule", "energy/area/timing companion metrics"],
        "promote_to_a": ["independent benchmark replication", "measurement protocol", "uncertainty bounds", "raw table availability"],
        "downgrade": ["density equivalence treated as node equivalence", "single proxy metric without companion gates", "ambiguous denominator"],
    },
    "roadmap": {
        "promote_to_b": ["milestone evidence", "dated roadmap assumptions", "dependency list", "measured intermediate artifact"],
        "promote_to_a": ["completed independent product-level validation", "published measurement package", "yield/manufacturing evidence", "third-party reproduction"],
        "downgrade": ["roadmap language treated as achieved result", "missing schedule assumptions", "unbounded extrapolation"],
    },
    "architecture": {
        "promote_to_b": ["architecture diagram", "workload-specific traffic model", "latency/bandwidth baseline", "energy/thermal/PDN model"],
        "promote_to_a": ["independent implementation", "post-layout or silicon measurement", "stress workloads", "failure-mode disclosure"],
        "downgrade": ["local path win not full-chip win", "unmodeled contention", "routing/PDN overhead dominates"],
    },
    "io": {
        "promote_to_b": ["I/O bandwidth baseline", "latency profile", "energy per bit", "integration overhead estimate"],
        "promote_to_a": ["measured package/system result", "independent link characterization", "thermal/yield disclosure", "end-to-end workload gain"],
        "downgrade": ["I/O win not tied to workload", "integration overhead dominates", "energy per bit worsens"],
    },
    "topology": {
        "promote_to_b": ["topology model", "wire-length/path reduction estimate", "vertical interconnect penalty estimate", "closure/thermal/yield analysis"],
        "promote_to_a": ["post-route closed design", "measured timing-energy result", "PVT/yield sweep", "independent reproduction"],
        "downgrade": ["topology helps only before routing", "vertical overhead dominates", "manufacturability/yield collapse"],
    },
}

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def infer_family(claim_id, title):
    s = (claim_id + " " + title).lower()
    if "logic" in s:
        return "mechanism"
    if "density" in s:
        return "metric"
    if "roadmap" in s or "gap" in s or "1p4" in s:
        return "roadmap"
    if "bus" in s:
        return "architecture"
    if "io" in s or "optical" in s:
        return "io"
    if "3d" in s or "fold" in s or "topolog" in s:
        return "topology"
    return "methodology"

def infer_missing(current_class):
    if current_class == "TSEK-B":
        return ["independent", "yield"]
    if current_class == "TSEK-D":
        return GATES[:]
    return ["energy", "thermal", "yield", "pdn_pvt", "independent"]

def load_claims():
    claims = []
    if CLAIM_DIR.exists():
        for path in sorted(CLAIM_DIR.glob("*.json")):
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
                claim_id = obj.get("claim_id") or obj.get("id") or path.stem
                title = obj.get("title") or obj.get("claim") or claim_id
                current_class = obj.get("current_class") or obj.get("tsek_class") or obj.get("classification") or "TSEK-C"
                family = obj.get("claim_family") or obj.get("family") or infer_family(claim_id, title)
                missing = obj.get("missing_gates") or obj.get("missing_evidence_gates") or infer_missing(current_class)
                claims.append({
                    "claim_id": claim_id,
                    "title": title,
                    "current_class": current_class,
                    "claim_family": family,
                    "missing_gates": [g for g in missing if g in GATES],
                    "source_path": str(path.relative_to(ROOT)),
                })
            except Exception:
                pass
    return claims or DEFAULT_CLAIMS

def sufficiency_score(missing_gates):
    return round((len(GATES) - len(missing_gates)) / len(GATES), 4)

def class_action(current_class, score):
    if current_class in ["TSEK-D", "TSEK-E"]:
        return "hold_or_downgrade_until_source_evidence_improves"
    if score >= 0.875:
        return "eligible_for_tsek_b_review"
    return "remain_current_class_pending_evidence"

def build_matrix(claim):
    req = FAMILY_REQUIREMENTS.get(claim["claim_family"], FAMILY_REQUIREMENTS["methodology"])
    missing = claim["missing_gates"]
    score = sufficiency_score(missing)
    current_class = claim["current_class"]
    return {
        "claim_id": claim["claim_id"],
        "title": claim["title"],
        "claim_family": claim["claim_family"],
        "current_class": current_class,
        "source_path": claim.get("source_path", "synthetic/default"),
        "evidence_gates": GATES,
        "missing_gates": missing,
        "evidence_sufficiency_score": score,
        "recommended_action": class_action(current_class, score),
        "keep_current_conditions": [f"Missing {gate} evidence keeps claim at or below {current_class}." for gate in missing],
        "promote_to_tsek_b_requires": req["promote_to_b"],
        "promote_to_tsek_a_requires": req["promote_to_a"],
        "downgrade_or_reject_if": req["downgrade"],
        "measurement_package": {
            "minimum": ["workload", "baseline", "method", "tau vector", "gate evidence table"],
            "strong": ["energy", "thermal", "PDN/PVT", "yield/manufacturability", "negative controls"],
            "independent": ["third-party reproduction", "raw measurements", "uncertainty bounds", "replication protocol"],
        },
        "non_claim_lock": "Evidence sufficiency requirements define promotion conditions only. They do not promote the claim or validate silicon by themselves.",
    }

def make_svg(matrices):
    rows = []
    y = 170
    max_missing = max([len(m["missing_gates"]) for m in matrices] + [1])
    for m in matrices:
        missing = len(m["missing_gates"])
        width = int(560 * missing / max_missing)
        if m["current_class"] == "TSEK-D":
            color = "#f59e0b"
        elif m["current_class"] == "TSEK-E":
            color = "#ef4444"
        elif missing <= 2:
            color = "#22c55e"
        else:
            color = "#22d3ee"
        rows.append('<text x="60" y="' + str(y+23) + '" fill="#e5e7eb" font-size="20" font-family="Segoe UI">' + m["claim_id"] + '</text>')
        rows.append('<rect x="455" y="' + str(y) + '" width="' + str(width) + '" height="30" rx="10" fill="' + color + '"/>')
        rows.append('<text x="' + str(480+width) + '" y="' + str(y+23) + '" fill="#f8fafc" font-size="19" font-family="Segoe UI">' + str(missing) + ' missing | ' + m["current_class"] + '</text>')
        y += 58
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="700" viewBox="0 0 1400 700"><rect width="1400" height="700" fill="#030712"/><text x="700" y="72" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Evidence Sufficiency Matrix v0.8.4</text><text x="700" y="116" text-anchor="middle" fill="#cbd5e1" font-size="23" font-family="Segoe UI">Missing evidence gates by public Tau claim</text>' + "".join(rows) + '<text x="700" y="660" text-anchor="middle" fill="#94a3b8" font-size="20" font-family="Segoe UI">Promotion requirements only. No classifier mutation, no threshold mutation, no silicon validation.</text></svg>'

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    claims = load_claims()
    matrices = [build_matrix(c) for c in claims]
    for matrix in matrices:
        write_json(REPORT_DIR / "claim_matrices" / f"{matrix['claim_id']}_evidence_matrix.json", matrix)

    class_counts = {}
    for m in matrices:
        class_counts[m["current_class"]] = class_counts.get(m["current_class"], 0) + 1

    avg_score = round(mean([m["evidence_sufficiency_score"] for m in matrices]), 4) if matrices else 0.0
    avg_missing = round(mean([len(m["missing_gates"]) for m in matrices]), 4) if matrices else 0.0

    summary = {
        "schema": "tau-scaling-evidence-sufficiency-matrix-v0.8.4",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_count": len(matrices),
        "class_counts": class_counts,
        "average_evidence_sufficiency_score": avg_score,
        "average_missing_gates": avg_missing,
        "matrices": matrices,
        "research_finding": "Public Tau claims can now be evaluated by explicit evidence sufficiency requirements rather than narrative plausibility.",
        "promotion_lock": "No claim is promoted by this matrix. Promotion requires disclosed evidence satisfying the required gates and independent review.",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "Evidence sufficiency matrices are promotion-condition artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }

    write_json(REPORT_DIR / "evidence_sufficiency_matrix_v0_8_4.json", summary)
    write_json(REPORT_DIR / "latest_evidence_sufficiency_matrix.json", summary)

    lines = [
        "# Evidence Sufficiency Matrix v0.8.4",
        "",
        "## Purpose",
        "",
        "Define the evidence required to preserve, promote, downgrade, or reject each public Tau claim.",
        "",
        "## Summary",
        "",
        f"- Claim count: `{summary['claim_count']}`",
        f"- Average evidence sufficiency score: `{summary['average_evidence_sufficiency_score']}`",
        f"- Average missing gates: `{summary['average_missing_gates']}`",
        "- Classifier changed: `false`",
        "- Thresholds changed: `false`",
        "- Mutation allowed: `false`",
        "",
        "## Claim Matrix",
        "",
        "| Claim | Current class | Family | Score | Missing gates | Recommended action |",
        "|---|---|---|---:|---:|---|",
    ]
    for m in matrices:
        lines.append(f"| `{m['claim_id']}` | {m['current_class']} | {m['claim_family']} | {m['evidence_sufficiency_score']} | {len(m['missing_gates'])} | {m['recommended_action']} |")

    lines += [
        "",
        "## Promotion Rules",
        "",
        "A claim may be considered for TSEK-B review only when workload, baseline, method, and companion gate evidence are disclosed.",
        "",
        "A claim may be considered for TSEK-A review only when independent reproduction, measurement protocol, uncertainty bounds, and negative controls are available.",
        "",
        "## Downgrade Rules",
        "",
        "- Roadmap language treated as achieved result forces downgrade pressure.",
        "- Density equivalence treated as node equivalence forces downgrade pressure.",
        "- Timing gain without energy/thermal/PDN/yield companion evidence remains bounded.",
        "- LogicFolding fails if wire savings are erased by vertical, routing, sync, variation, closure, thermal, or yield burden.",
        "",
        "## Visual",
        "",
        "![Evidence sufficiency matrix](../../visuals/evidence_sufficiency/v0_8_4/evidence_sufficiency_matrix.svg)",
        "",
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    write(REPORT_DIR / "evidence_sufficiency_matrix_v0_8_4.md", "\n".join(lines))
    write(REPORT_DIR / "latest_evidence_sufficiency_matrix.md", "\n".join(lines))

    write(REPORT_DIR / "README.md", "# Evidence Sufficiency Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**\n\n## Purpose\n\nThis folder stores promotion-condition matrices for public Tau claims.\n\n## Primary command\n\n```powershell\npython scripts/benchmarks/generate_evidence_sufficiency_matrix.py\n```\n\n## README Update Rule\n\nUpdate this mini README whenever evidence sufficiency requirements, claim matrices, or promotion/downgrade rules change.\n\nBoundary: evidence sufficiency matrices are promotion-condition artifacts only.\n")
    write(ROOT / "visuals" / "evidence_sufficiency" / "README.md", "# Evidence Sufficiency Visuals\n\nCurrent layer: **TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**\n\n## Purpose\n\nThis folder stores visuals summarizing missing evidence gates and claim sufficiency.\n\n## README Update Rule\n\nUpdate this mini README whenever evidence sufficiency visuals change.\n\nBoundary: visuals are not claim validation.\n")
    write(VIS_DIR / "README.md", "# v0.8.4 Evidence Sufficiency Visuals\n\nCharts:\n\n- `evidence_sufficiency_matrix.svg`\n\nBoundary: promotion-condition visualization only.\n")
    write(VIS_DIR / "evidence_sufficiency_matrix.svg", make_svg(matrices))

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "average_evidence_sufficiency_score": summary["average_evidence_sufficiency_score"],
        "average_missing_gates": summary["average_missing_gates"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "report": "reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()