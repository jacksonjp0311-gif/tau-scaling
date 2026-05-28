from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MANUSCRIPT_MD = ROOT / "docs" / "manuscript" / "tau_scaling_public_claim_system_v0_9_1.md"
MANUSCRIPT_TEX = ROOT / "docs" / "manuscript" / "tau_scaling_public_claim_system_v0_9_1.tex"
EVIDENCE_MD = ROOT / "docs" / "manuscript" / "evidence_table_v0_9_2.md"
EVIDENCE_TEX = ROOT / "docs" / "manuscript" / "evidence_table_v0_9_2.tex"
FIGURE_MD = ROOT / "docs" / "manuscript" / "figure_pack_v0_9_2.md"
LIMITATIONS_MD = ROOT / "docs" / "manuscript" / "limitations_table_v0_9_2.md"
ARTIFACT_MAP_MD = ROOT / "docs" / "manuscript" / "artifact_map_v0_9_2.md"
RESULTS_MD = ROOT / "docs" / "manuscript" / "paper_ready_results_summary_v0_9_2.md"

MILESTONE_JSON = ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.json"
EVIDENCE_JSON = ROOT / "reports" / "manuscript_evidence_pack" / "latest_manuscript_evidence_pack.json"
GAP_JSON = ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.json"
RELEASE_JSON = ROOT / "reports" / "release" / "latest_release_readiness.json"

REPORT_DIR = ROOT / "reports" / "manuscript_submission_package"
DOCS_DIR = ROOT / "docs" / "manuscript"
SUBMISSION_DIR = ROOT / "releases" / "manuscript_submission_package_v0_9_3"
VIS_DIR = ROOT / "visuals" / "manuscript_submission_package" / "v0_9_3"

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}

def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except Exception:
        return str(path)

def copy_file(path: Path, dest_dir: Path) -> dict:
    if path.exists():
        dest = dest_dir / path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        return {"source": rel(path), "packaged_as": rel(dest), "exists": True}
    return {"source": rel(path), "packaged_as": None, "exists": False}

def make_svg(metrics: dict) -> str:
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="82" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Manuscript Submission Package v0.9.3</text>',
        '<text x="800" y="130" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">Polished manuscript bundle with evidence tables, captions, limitations, and non-claim locks</text>',
        f'<text x="190" y="245" fill="#f8fafc" font-size="30" font-family="Segoe UI">Claims analyzed: {metrics.get("claim_count", 0)}</text>',
        f'<text x="190" y="315" fill="#f8fafc" font-size="30" font-family="Segoe UI">Source-populated claims: {metrics.get("source_populated_count", 0)}</text>',
        f'<text x="190" y="385" fill="#f8fafc" font-size="30" font-family="Segoe UI">Primary-source confirmed: {metrics.get("primary_source_confirmed_count", 0)}</text>',
        f'<text x="190" y="455" fill="#f8fafc" font-size="30" font-family="Segoe UI">Independent-source confirmed: {metrics.get("independent_source_confirmed_count", 0)}</text>',
        f'<text x="190" y="525" fill="#f8fafc" font-size="30" font-family="Segoe UI">Release findings: {metrics.get("release_findings", 0)}</text>',
        '<rect x="900" y="250" width="450" height="76" rx="18" fill="#0f172a" stroke="#22c55e"/>',
        '<text x="1125" y="298" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Submission README</text>',
        '<rect x="900" y="380" width="450" height="76" rx="18" fill="#0f172a" stroke="#67e8f9"/>',
        '<text x="1125" y="428" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Polished MD + LaTeX</text>',
        '<rect x="900" y="510" width="450" height="76" rx="18" fill="#0f172a" stroke="#ef4444"/>',
        '<text x="1125" y="558" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">No validation overclaim</text>',
        '<text x="800" y="820" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">Submission package is a communication shell for evidence governance, not silicon proof.</text>',
        '</svg>',
    ])

def build_polished_markdown(metrics: dict) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    evidence = read(EVIDENCE_MD)
    figures = read(FIGURE_MD)
    limitations = read(LIMITATIONS_MD)
    artifacts = read(ARTIFACT_MAP_MD)

    return f"""# Tau Scaling as an Evidence-Gated Public Claim System

## Source Population, Primary-Validation Gaps, and Non-Claim Locks

**Author:** James Paul Jackson  
**Version:** TAU-SCALING-SA v0.9.3 — Manuscript Polish and Submission Package  
**Date:** {today}  
**Repository:** `tau-scaling`  
**Artifact type:** Repository-based evidence-governance manuscript

---

## Abstract

Public semiconductor narratives often combine roadmap projections, media interpretation, methodology framing, reported metrics, and implied validation. This manuscript presents a repository-based method for converting public Tau Scaling and LogicFolding claims into an evidence-gated claim system. The pipeline emits claim ledgers, source-provenance maps, source intake cards, public source population records, primary-source validation-gap matrices, figure packs, and release-readiness checks. In the current repository state, eight public Tau claims are source-populated from public reporting, zero are primary-source confirmed, and zero are independently confirmed. The contribution is a reproducible evidence-governance artifact for separating public narrative from validation status. It is not a claim of silicon validation, product validation, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.

## Contribution Statement

This work contributes:

1. A reproducible repository method for public semiconductor claim governance.
2. A source-provenance workflow that separates public reporting from primary-source confirmation.
3. A validation-gap matrix for identifying what evidence remains missing.
4. A manuscript-ready artifact set: evidence table, figure captions, limitations table, artifact map, and release-check surface.
5. Explicit non-claim locks that prevent publication framing from exceeding the available evidence.

## Research Question

Can public Tau Scaling claims be represented as a reproducible evidence-governance system that separates source population from primary validation and claim promotion?

## Method Summary

The method is a staged evidence pipeline:

```text
public claim
  -> claim ledger
  -> source provenance map
  -> source intake card
  -> source population manifest
  -> primary-source validation gap review
  -> public research milestone package
  -> manuscript draft and evidence pack
  -> submission package
```

The pipeline makes each transition auditable. A claim can be source-populated without being source-validated. A source-validated claim is still not promoted unless evidence gates, review gates, and independent support are satisfied.

## Results

| Metric | Value |
|---|---:|
| Public claims analyzed | {metrics.get("claim_count", 0)} |
| Source-populated claims | {metrics.get("source_populated_count", 0)} |
| Primary-source confirmed claims | {metrics.get("primary_source_confirmed_count", 0)} |
| Independent-source confirmed claims | {metrics.get("independent_source_confirmed_count", 0)} |
| High validation-gap claims | {metrics.get("high_gap_claim_count", 0)} |
| Release findings | {metrics.get("release_findings", 0)} |

The principal result is not validation of Tau Scaling. The principal result is the reproducible separation of public claim visibility, source population, primary-source confirmation, independent validation, and claim promotion.

## Evidence Table

{evidence}

## Figure Index and Captions

{figures}

## Limitations

{limitations}

## Artifact Map

{artifacts}

## Data and Code Availability

All artifacts are repository-local. The submission package includes the manuscript, evidence tables, figure captions, limitations table, artifact map, public research milestone package, release-readiness report, and non-claim locks. Key paths:

- `releases/manuscript_submission_package_v0_9_3/`
- `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.md`
- `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.tex`
- `reports/manuscript_submission_package/latest_manuscript_submission_package.md`
- `reports/release/latest_release_readiness.md`

## Ethics and Non-Claim Statement

This manuscript concerns evidence governance. It should not be read as investment advice, industrial validation, product endorsement, national capability assessment, or proof of semiconductor performance. Public reporting is not primary validation. Source population is not source validation. Source validation is not claim promotion.

## Reproducibility Commands

```powershell
python scripts/benchmarks/generate_tau_public_claim_ledger.py
python scripts/benchmarks/generate_public_source_ledger.py
python scripts/benchmarks/generate_source_evidence_intake_cards.py
python scripts/benchmarks/run_primary_source_intake_queue.py
python scripts/benchmarks/populate_public_source_intake_v0_8_8.py
python scripts/benchmarks/generate_primary_source_gap_review_v0_8_9.py
python scripts/release/build_public_research_milestone_v0_9_0.py
python scripts/release/build_manuscript_draft_scaffold_v0_9_1.py
python scripts/release/build_manuscript_evidence_pack_v0_9_2.py
python scripts/release/build_manuscript_submission_package_v0_9_3.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## Conclusion

The current repository state supports a narrow, publishable claim: Tau Scaling public claims can be transformed into a reproducible evidence-governance artifact with source-population and validation-gap surfaces. The current evidence does not support silicon validation, product validation, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.
"""

def build_polished_latex(metrics: dict) -> str:
    return r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{amsmath}

\title{Tau Scaling as an Evidence-Gated Public Claim System\\
\large Source Population, Primary-Validation Gaps, and Non-Claim Locks}
\author{James Paul Jackson}
\date{TAU-SCALING-SA v0.9.3}

\begin{document}
\maketitle

\begin{abstract}
Public semiconductor narratives often combine roadmap projections, media interpretation, methodology framing, reported metrics, and implied validation. This manuscript presents a repository-based method for converting public Tau Scaling and LogicFolding claims into an evidence-gated claim system. In the current repository state, eight public Tau claims are source-populated from public reporting, zero are primary-source confirmed, and zero are independently confirmed. The contribution is a reproducible evidence-governance artifact for separating public narrative from validation status. It is not a claim of silicon validation, product validation, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.
\end{abstract}

\section{Contribution}
This work contributes a reproducible repository method for public semiconductor claim governance, a source-provenance workflow, a validation-gap matrix, manuscript-ready evidence tables, and explicit non-claim locks.

\section{Research Question}
Can public Tau Scaling claims be represented as a reproducible evidence-governance system that separates source population from primary validation and claim promotion?

\section{Method}
The method converts public claims into a staged evidence pipeline: claim ledger, source provenance map, source intake card, source population manifest, primary-source validation gap review, public research milestone package, manuscript draft, evidence pack, and submission package.

\section{Results}
\begin{center}
\begin{tabular}{lr}
\toprule
Metric & Value\\
\midrule
Public claims analyzed & """ + str(metrics.get("claim_count", 0)) + r"""\\
Source-populated claims & """ + str(metrics.get("source_populated_count", 0)) + r"""\\
Primary-source confirmed claims & """ + str(metrics.get("primary_source_confirmed_count", 0)) + r"""\\
Independent-source confirmed claims & """ + str(metrics.get("independent_source_confirmed_count", 0)) + r"""\\
High validation-gap claims & """ + str(metrics.get("high_gap_claim_count", 0)) + r"""\\
Release findings & """ + str(metrics.get("release_findings", 0)) + r"""\\
\bottomrule
\end{tabular}
\end{center}

\section{Interpretation}
The principal result is not validation of Tau Scaling. The principal result is the reproducible separation of public claim visibility, source population, primary-source confirmation, independent validation, and claim promotion.

\section{Limitations}
This manuscript does not validate semiconductor performance, Huawei product performance, manufacturing capability, process-node equivalence, benchmark superiority, or a universal Tau Scaling law.

\section{Data and Code Availability}
All artifacts are repository-local under docs, reports, releases, sources, visuals, and scripts.

\section{Ethics and Non-Claim Statement}
This manuscript concerns evidence governance. It should not be read as investment advice, industrial validation, product endorsement, national capability assessment, or proof of semiconductor performance.

\section{Conclusion}
The current repository state supports a narrow, publishable claim: Tau Scaling public claims can be transformed into a reproducible evidence-governance artifact with source-population and validation-gap surfaces.

\end{document}
"""

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    milestone = load_json(MILESTONE_JSON)
    evidence = load_json(EVIDENCE_JSON)
    gap = load_json(GAP_JSON)
    release = load_json(RELEASE_JSON)

    metrics = dict(milestone.get("metrics", {}))
    metrics.setdefault("claim_count", evidence.get("claim_count", 0))
    metrics.setdefault("source_populated_count", evidence.get("source_populated_count", 0))
    metrics.setdefault("primary_source_confirmed_count", evidence.get("primary_source_confirmed_count", 0))
    metrics.setdefault("independent_source_confirmed_count", evidence.get("independent_source_confirmed_count", 0))
    metrics.setdefault("high_gap_claim_count", gap.get("high_gap_claim_count", 0))
    metrics["release_findings"] = len(release.get("findings", [])) if isinstance(release.get("findings", []), list) else int(release.get("findings", 0) or 0)

    polished_md = build_polished_markdown(metrics)
    polished_tex = build_polished_latex(metrics)

    md_path = DOCS_DIR / "tau_scaling_public_claim_system_v0_9_3.md"
    tex_path = DOCS_DIR / "tau_scaling_public_claim_system_v0_9_3.tex"
    write(md_path, polished_md)
    write(tex_path, polished_tex)

    packaged = []
    for path in [
        md_path,
        tex_path,
        EVIDENCE_MD,
        EVIDENCE_TEX,
        FIGURE_MD,
        LIMITATIONS_MD,
        ARTIFACT_MAP_MD,
        RESULTS_MD,
        ROOT / "reports" / "manuscript_evidence_pack" / "latest_manuscript_evidence_pack.md",
        ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.md",
        ROOT / "reports" / "release" / "latest_release_readiness.md",
    ]:
        packaged.append(copy_file(path, SUBMISSION_DIR))

    submission_readme = "# Manuscript Submission Package v0.9.3\n\n"
    submission_readme += "## Title\n\nTau Scaling as an Evidence-Gated Public Claim System\n\n"
    submission_readme += "## Submission Files\n\n"
    for item in packaged:
        status = "included" if item["exists"] else "missing"
        submission_readme += f"- `{item['source']}`: {status}"
        if item["packaged_as"]:
            submission_readme += f" -> `{item['packaged_as']}`"
        submission_readme += "\n"
    submission_readme += "\n## Submission Boundary\n\nThis package is submission-facing evidence-governance material. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or a universal Tau Scaling law.\n"
    write(SUBMISSION_DIR / "README.md", submission_readme)

    availability = "# Data Availability Statement v0.9.3\n\nAll data and artifacts used by this manuscript are repository-local and reproducible from scripts in `scripts/benchmarks/` and `scripts/release/`. Public source records are stored as bounded source-population manifests. No claim promotion is made.\n"
    ethics = "# Ethics and Non-Claim Statement v0.9.3\n\nThis manuscript concerns evidence governance and source provenance. It is not investment advice, product endorsement, industrial validation, national capability assessment, or semiconductor performance proof.\n"
    write(SUBMISSION_DIR / "DATA_AVAILABILITY.md", availability)
    write(SUBMISSION_DIR / "ETHICS_AND_NON_CLAIM_STATEMENT.md", ethics)

    manifest = {
        "schema": "tau-scaling-manuscript-submission-package-v0.9.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "Tau Scaling as an Evidence-Gated Public Claim System",
        "markdown": rel(md_path),
        "latex": rel(tex_path),
        "submission_dir": rel(SUBMISSION_DIR),
        "packaged_files": packaged,
        "metrics": metrics,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "submission_claims_silicon_validation": False,
        "boundary": "v0.9.3 packages a submission-facing manuscript. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.",
    }
    write_json(SUBMISSION_DIR / "submission_manifest_v0_9_3.json", manifest)
    write_json(REPORT_DIR / "manuscript_submission_package_v0_9_3.json", manifest)
    write_json(REPORT_DIR / "latest_manuscript_submission_package.json", manifest)

    report_md = "# Manuscript Polish and Submission Package v0.9.3\n\n"
    report_md += "## Outputs\n\n"
    report_md += f"- Polished Markdown: `{rel(md_path)}`\n"
    report_md += f"- Polished LaTeX: `{rel(tex_path)}`\n"
    report_md += f"- Submission package: `{rel(SUBMISSION_DIR)}`\n"
    report_md += "- Data availability statement\n"
    report_md += "- Ethics and non-claim statement\n\n"
    report_md += "## Lock State\n\n"
    for key in [
        "thresholds_changed",
        "classifier_changed",
        "mutation_allowed",
        "application_allowed",
        "claim_promotion_allowed",
        "source_validation_claimed",
        "submission_claims_silicon_validation",
    ]:
        report_md += f"- {key}: `{manifest[key]}`\n"
    report_md += "\n## Boundary\n\n" + manifest["boundary"] + "\n"
    write(REPORT_DIR / "manuscript_submission_package_v0_9_3.md", report_md)
    write(REPORT_DIR / "latest_manuscript_submission_package.md", report_md)
    write(REPORT_DIR / "README.md", "# Manuscript Submission Package Reports\n\nCurrent layer: **TAU-SCALING-SA v0.9.3 - Manuscript Polish and Submission Package**\n\nBoundary: submission packaging is not claim promotion.\n")

    write(VIS_DIR / "manuscript_submission_package.svg", make_svg(metrics))
    write(VIS_DIR / "README.md", "# v0.9.3 Manuscript Submission Visuals\n\n- `manuscript_submission_package.svg`\n\nBoundary: submission-package visualization only.\n")

    print(json.dumps({
        "schema": manifest["schema"],
        "markdown": manifest["markdown"],
        "latex": manifest["latex"],
        "submission_dir": manifest["submission_dir"],
        "claim_count": metrics.get("claim_count", 0),
        "source_populated_count": metrics.get("source_populated_count", 0),
        "primary_source_confirmed_count": metrics.get("primary_source_confirmed_count", 0),
        "independent_source_confirmed_count": metrics.get("independent_source_confirmed_count", 0),
        "thresholds_changed": manifest["thresholds_changed"],
        "classifier_changed": manifest["classifier_changed"],
        "mutation_allowed": manifest["mutation_allowed"],
        "application_allowed": manifest["application_allowed"],
        "claim_promotion_allowed": manifest["claim_promotion_allowed"],
        "source_validation_claimed": manifest["source_validation_claimed"],
        "report": "reports/manuscript_submission_package/latest_manuscript_submission_package.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()