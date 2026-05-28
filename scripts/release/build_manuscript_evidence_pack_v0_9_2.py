from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]

MANUSCRIPT_MD = ROOT / "docs" / "manuscript" / "tau_scaling_public_claim_system_v0_9_1.md"
MANUSCRIPT_TEX = ROOT / "docs" / "manuscript" / "tau_scaling_public_claim_system_v0_9_1.tex"

CLAIM_JSON = ROOT / "reports" / "tau_claim_ledger" / "latest_tau_public_claim_ledger.json"
SOURCE_POP_JSON = ROOT / "sources" / "primary_source_intake" / "source_population_manifest_v0_8_8.json"
GAP_JSON = ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.json"
MILESTONE_JSON = ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.json"
MANUSCRIPT_JSON = ROOT / "reports" / "manuscript_draft" / "latest_manuscript_draft_scaffold.json"

REPORT_DIR = ROOT / "reports" / "manuscript_evidence_pack"
DOCS_DIR = ROOT / "docs" / "manuscript"
VIS_DIR = ROOT / "visuals" / "manuscript_evidence_pack" / "v0_9_2"

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)

def find_gap_rows(gap: dict) -> list[dict]:
    return gap.get("rows", []) if isinstance(gap.get("rows"), list) else []

def find_source_entries(pop: dict) -> list[dict]:
    return pop.get("entries", []) if isinstance(pop.get("entries"), list) else []

def leading_source(entry: dict) -> str:
    records = entry.get("source_records", [])
    if records:
        return records[0].get("title", "public source")
    return "not populated"

def source_count(entry: dict) -> int:
    records = entry.get("source_records", [])
    return len(records) if isinstance(records, list) else 0

def build_evidence_rows(pop_entries: list[dict], gap_rows: list[dict]) -> list[dict]:
    gap_by_id = {row.get("claim_id"): row for row in gap_rows}
    rows = []
    for entry in pop_entries:
        claim_id = entry.get("claim_id")
        gap = gap_by_id.get(claim_id, {})
        rows.append({
            "claim_id": claim_id,
            "claim_title": entry.get("claim_title", ""),
            "current_class": entry.get("current_class", ""),
            "source_category": entry.get("source_category", ""),
            "source_records_count": source_count(entry),
            "leading_source": leading_source(entry),
            "source_populated": bool(entry.get("source_populated", False)),
            "primary_source_confirmed": bool(entry.get("primary_source_confirmed", False)),
            "independent_source_confirmed": bool(entry.get("independent_source_confirmed", False)),
            "gap_severity": gap.get("gap_severity", "HIGH"),
            "gap_count": int(gap.get("gap_count", 0) or 0),
            "claim_promotion_allowed": False,
        })
    return rows

def markdown_table(rows: list[dict]) -> str:
    text = "| Claim | Class | Source category | Sources | Primary? | Independent? | Gap | Promotion? |\n"
    text += "|---|---|---|---:|---:|---:|---|---:|\n"
    for row in rows:
        text += (
            f"| `{row['claim_id']}` | {row['current_class']} | {row['source_category']} | "
            f"{row['source_records_count']} | {row['primary_source_confirmed']} | "
            f"{row['independent_source_confirmed']} | {row['gap_severity']} ({row['gap_count']}) | "
            f"{row['claim_promotion_allowed']} |\n"
        )
    return text

def latex_table(rows: list[dict]) -> str:
    lines = [
        r"\begin{table}[ht]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{llllrrr}",
        r"\toprule",
        r"Claim & Class & Source type & Sources & Primary & Independent & Gap\\",
        r"\midrule",
    ]
    for row in rows:
        lines.append(
            f"{row['claim_id'].replace('_','-')} & {row['current_class']} & {row['source_category'].replace('_',' ')} & "
            f"{row['source_records_count']} & {str(row['primary_source_confirmed'])} & "
            f"{str(row['independent_source_confirmed'])} & {row['gap_severity']}\\\\"
        )
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Evidence and validation-gap status for public Tau Scaling claims. Source population does not imply primary validation or claim promotion.}",
        r"\label{tab:evidence-gap-status}",
        r"\end{table}",
    ]
    return "\n".join(lines) + "\n"

def figure_index() -> list[dict]:
    figs = [
        {
            "id": "fig:public-research-milestone",
            "path": "visuals/public_research_milestone/v0_9_0/public_research_milestone.svg",
            "caption": "Public research milestone summary showing eight source-populated claims, zero primary-source confirmations, and zero independent confirmations.",
            "boundary": "Visualization of evidence-governance state only.",
        },
        {
            "id": "fig:primary-source-gap",
            "path": "visuals/primary_source_gap_review/v0_8_9/primary_source_gap_review.svg",
            "caption": "Primary-source validation gap review showing the separation between source population, primary-source confirmation, and independent validation.",
            "boundary": "Validation-gap visualization only.",
        },
        {
            "id": "fig:public-source-population",
            "path": "visuals/public_source_population/v0_8_8/public_source_population_pass.svg",
            "caption": "Public source population pass showing that all public claims can be populated from public reporting while source validation remains unclaimed.",
            "boundary": "Source population visualization only.",
        },
        {
            "id": "fig:manuscript-scaffold",
            "path": "visuals/manuscript_draft/v0_9_1/manuscript_draft_scaffold.svg",
            "caption": "Manuscript scaffold view showing the transformation from evidence package to paper-style structure.",
            "boundary": "Manuscript structure visualization only.",
        },
    ]
    return figs

def limitations_table() -> list[dict]:
    return [
        {
            "limitation": "No primary-source confirmation",
            "impact": "Public reports cannot be treated as first-party validation.",
            "next_evidence_required": "Huawei/HiSilicon paper, patent, conference material, technical note, or formal disclosure.",
        },
        {
            "limitation": "No independent reproduction",
            "impact": "Claims cannot be promoted to independently verified status.",
            "next_evidence_required": "Third-party measurement, benchmark reproduction, or peer-reviewed validation.",
        },
        {
            "limitation": "No workload-complete benchmark",
            "impact": "Reported gains cannot be generalized across workloads.",
            "next_evidence_required": "Declared workload, baseline, candidate artifact, measurement method, and uncertainty.",
        },
        {
            "limitation": "No energy / thermal / PDN / PVT companion evidence",
            "impact": "Time or density claims cannot be treated as complete scaling claims.",
            "next_evidence_required": "Power, thermal, robustness, yield, and variation data.",
        },
        {
            "limitation": "Roadmap language may be confused with achieved result",
            "impact": "2031 or node-equivalent targets must not be interpreted as current silicon proof.",
            "next_evidence_required": "Date-bound milestone trace and achieved-result evidence.",
        },
    ]

def artifact_map() -> list[dict]:
    return [
        {"artifact": "Claim ledger", "path": "reports/tau_claim_ledger/latest_tau_public_claim_ledger.md", "role": "Defines public claims and current TSEK classes."},
        {"artifact": "Public source ledger", "path": "reports/public_source_ledger/latest_public_source_ledger.md", "role": "Maps claims to source categories and source-carry boundaries."},
        {"artifact": "Source population manifest", "path": "sources/primary_source_intake/source_population_manifest_v0_8_8.json", "role": "Stores bounded public source records."},
        {"artifact": "Primary-source gap review", "path": "reports/primary_source_gap_review/latest_primary_source_gap_review.md", "role": "Identifies missing primary and independent evidence."},
        {"artifact": "Milestone package", "path": "releases/public_research_milestone_v0_9_0/README.md", "role": "Packages the public research spine."},
        {"artifact": "Manuscript draft", "path": "docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md", "role": "Converts the package into a paper-style draft."},
    ]

def make_svg(summary: dict) -> str:
    claims = summary["claim_count"]
    sources = summary["source_populated_count"]
    primary = summary["primary_source_confirmed_count"]
    independent = summary["independent_source_confirmed_count"]
    tables = summary["table_count"]
    figures = summary["figure_count"]
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="82" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Manuscript Evidence Pack v0.9.2</text>',
        '<text x="800" y="130" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Tables, captions, limitations, artifact map, and result summary</text>',
        f'<text x="190" y="240" fill="#f8fafc" font-size="30" font-family="Segoe UI">Evidence table rows: {claims}</text>',
        f'<text x="190" y="310" fill="#f8fafc" font-size="30" font-family="Segoe UI">Source-populated claims: {sources}</text>',
        f'<text x="190" y="380" fill="#f8fafc" font-size="30" font-family="Segoe UI">Primary-source confirmed: {primary}</text>',
        f'<text x="190" y="450" fill="#f8fafc" font-size="30" font-family="Segoe UI">Independent-source confirmed: {independent}</text>',
        f'<text x="190" y="520" fill="#f8fafc" font-size="30" font-family="Segoe UI">Manuscript tables: {tables}</text>',
        f'<text x="190" y="590" fill="#f8fafc" font-size="30" font-family="Segoe UI">Figures indexed: {figures}</text>',
        '<rect x="900" y="250" width="430" height="76" rx="18" fill="#0f172a" stroke="#22c55e"/>',
        '<text x="1115" y="298" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Paper-ready evidence table</text>',
        '<rect x="900" y="380" width="430" height="76" rx="18" fill="#0f172a" stroke="#f59e0b"/>',
        '<text x="1115" y="428" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Caption + limitation pack</text>',
        '<rect x="900" y="510" width="430" height="76" rx="18" fill="#0f172a" stroke="#ef4444"/>',
        '<text x="1115" y="558" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">No validation overclaim</text>',
        '<text x="800" y="820" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">Evidence pack strengthens readability; it does not promote claims.</text>',
        '</svg>',
    ])

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    pop = load_json(SOURCE_POP_JSON)
    gap = load_json(GAP_JSON)
    milestone = load_json(MILESTONE_JSON)
    manuscript = load_json(MANUSCRIPT_JSON)

    rows = build_evidence_rows(find_source_entries(pop), find_gap_rows(gap))
    figs = figure_index()
    limits = limitations_table()
    artifacts = artifact_map()

    summary = {
        "schema": "tau-scaling-manuscript-evidence-table-figure-pack-v0.9.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "claim_count": len(rows),
        "source_populated_count": sum(1 for r in rows if r["source_populated"]),
        "primary_source_confirmed_count": sum(1 for r in rows if r["primary_source_confirmed"]),
        "independent_source_confirmed_count": sum(1 for r in rows if r["independent_source_confirmed"]),
        "average_gap_count": round(mean([r["gap_count"] for r in rows]), 4) if rows else 0.0,
        "table_count": 4,
        "figure_count": len(figs),
        "artifact_count": len(artifacts),
        "limitation_count": len(limits),
        "outputs": {
            "evidence_table_md": "docs/manuscript/evidence_table_v0_9_2.md",
            "evidence_table_tex": "docs/manuscript/evidence_table_v0_9_2.tex",
            "figure_pack_md": "docs/manuscript/figure_pack_v0_9_2.md",
            "limitations_table_md": "docs/manuscript/limitations_table_v0_9_2.md",
            "artifact_map_md": "docs/manuscript/artifact_map_v0_9_2.md",
            "paper_ready_results_md": "docs/manuscript/paper_ready_results_summary_v0_9_2.md",
        },
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "evidence_pack_claims_silicon_validation": False,
        "boundary": "v0.9.2 creates manuscript tables and figure captions only. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }

    evidence_md = "# Evidence Table v0.9.2\n\n" + markdown_table(rows) + "\n## Boundary\n\nSource-populated does not mean source-validated. No claim is promoted by this table.\n"
    evidence_tex = latex_table(rows)

    fig_md = "# Figure Pack v0.9.2\n\n"
    for fig in figs:
        fig_md += f"## {fig['id']}\n\n- Path: `{fig['path']}`\n- Caption: {fig['caption']}\n- Boundary: {fig['boundary']}\n\n"

    lim_md = "# Limitations Table v0.9.2\n\n"
    lim_md += "| Limitation | Impact | Next evidence required |\n|---|---|---|\n"
    for item in limits:
        lim_md += f"| {item['limitation']} | {item['impact']} | {item['next_evidence_required']} |\n"

    art_md = "# Artifact Map v0.9.2\n\n"
    art_md += "| Artifact | Path | Role |\n|---|---|---|\n"
    for item in artifacts:
        art_md += f"| {item['artifact']} | `{item['path']}` | {item['role']} |\n"

    result_md = "# Paper-Ready Results Summary v0.9.2\n\n"
    result_md += "## Result Statement\n\n"
    result_md += "The current Tau Scaling artifact supports a bounded source-provenance and validation-gap claim: public Tau Scaling claims can be represented as an evidence-gated public claim system. The public claim field is source-populated, but not primary-source confirmed or independently validated in the current repository state.\n\n"
    result_md += "## Quantitative Results\n\n"
    for key in [
        "claim_count",
        "source_populated_count",
        "primary_source_confirmed_count",
        "independent_source_confirmed_count",
        "average_gap_count",
        "table_count",
        "figure_count",
        "artifact_count",
        "limitation_count",
    ]:
        result_md += f"- {key}: `{summary[key]}`\n"
    result_md += "\n## Boundary\n\nThis result is publishable as evidence-governance and source-provenance analysis. It is not publishable as silicon validation.\n"

    write(DOCS_DIR / "evidence_table_v0_9_2.md", evidence_md)
    write(DOCS_DIR / "evidence_table_v0_9_2.tex", evidence_tex)
    write(DOCS_DIR / "figure_pack_v0_9_2.md", fig_md)
    write(DOCS_DIR / "limitations_table_v0_9_2.md", lim_md)
    write(DOCS_DIR / "artifact_map_v0_9_2.md", art_md)
    write(DOCS_DIR / "paper_ready_results_summary_v0_9_2.md", result_md)

    report_md = "# Manuscript Evidence Table and Figure Pack v0.9.2\n\n"
    report_md += "## Outputs\n\n"
    for label, path in summary["outputs"].items():
        report_md += f"- {label}: `{path}`\n"
    report_md += "\n## Lock State\n\n"
    for key in [
        "thresholds_changed",
        "classifier_changed",
        "mutation_allowed",
        "application_allowed",
        "claim_promotion_allowed",
        "source_validation_claimed",
        "evidence_pack_claims_silicon_validation",
    ]:
        report_md += f"- {key}: `{summary[key]}`\n"
    report_md += "\n## Boundary\n\n" + summary["boundary"] + "\n"

    write_json(REPORT_DIR / "manuscript_evidence_pack_v0_9_2.json", summary)
    write_json(REPORT_DIR / "latest_manuscript_evidence_pack.json", summary)
    write(REPORT_DIR / "manuscript_evidence_pack_v0_9_2.md", report_md)
    write(REPORT_DIR / "latest_manuscript_evidence_pack.md", report_md)
    write(REPORT_DIR / "README.md", "# Manuscript Evidence Pack Reports\n\nCurrent layer: **TAU-SCALING-SA v0.9.2 - Manuscript Evidence Table and Figure Pack**\n\nBoundary: evidence tables and figure captions are not claim promotion.\n")

    write(VIS_DIR / "manuscript_evidence_pack.svg", make_svg(summary))
    write(VIS_DIR / "README.md", "# v0.9.2 Manuscript Evidence Pack Visuals\n\n- `manuscript_evidence_pack.svg`\n\nBoundary: table/figure-pack visualization only.\n")

    print(json.dumps({
        "schema": summary["schema"],
        "claim_count": summary["claim_count"],
        "source_populated_count": summary["source_populated_count"],
        "primary_source_confirmed_count": summary["primary_source_confirmed_count"],
        "independent_source_confirmed_count": summary["independent_source_confirmed_count"],
        "table_count": summary["table_count"],
        "figure_count": summary["figure_count"],
        "thresholds_changed": summary["thresholds_changed"],
        "classifier_changed": summary["classifier_changed"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "claim_promotion_allowed": summary["claim_promotion_allowed"],
        "source_validation_claimed": summary["source_validation_claimed"],
        "report": "reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()