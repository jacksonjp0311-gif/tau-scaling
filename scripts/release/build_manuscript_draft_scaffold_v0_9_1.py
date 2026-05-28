from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MILESTONE_JSON = ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.json"
MILESTONE_MD = ROOT / "reports" / "public_research_milestone" / "latest_public_research_milestone.md"
FINDINGS_MD = ROOT / "reports" / "publishable_findings" / "latest_publishable_findings_brief.md"
GAP_MD = ROOT / "reports" / "primary_source_gap_review" / "latest_primary_source_gap_review.md"
REPORT_DIR = ROOT / "reports" / "manuscript_draft"
DOCS_DIR = ROOT / "docs" / "manuscript"
RELEASE_DIR = ROOT / "releases" / "public_research_milestone_v0_9_0"
VIS_DIR = ROOT / "visuals" / "manuscript_draft" / "v0_9_1"

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

def make_ascii_flow() -> str:
    return """raw public claim
  -> claim ledger
  -> source provenance map
  -> source intake card
  -> public source population
  -> primary-source validation gap review
  -> publishable finding
  -> milestone package
  -> manuscript scaffold
"""

def make_svg(metrics: dict) -> str:
    claims = metrics.get("claim_count", 0)
    populated = metrics.get("source_populated_count", 0)
    primary = metrics.get("primary_source_confirmed_count", 0)
    independent = metrics.get("independent_source_confirmed_count", 0)
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        '<rect width="1600" height="900" fill="#020617"/>',
        '<text x="800" y="80" text-anchor="middle" fill="#67e8f9" font-size="46" font-family="Segoe UI" font-weight="700">Manuscript Draft Scaffold v0.9.1</text>',
        '<text x="800" y="126" text-anchor="middle" fill="#cbd5e1" font-size="24" font-family="Segoe UI">A paper scaffold from a bounded evidence-governance package</text>',
        f'<text x="190" y="240" fill="#f8fafc" font-size="30" font-family="Segoe UI">Claims analyzed: {claims}</text>',
        f'<text x="190" y="310" fill="#f8fafc" font-size="30" font-family="Segoe UI">Source-populated: {populated}</text>',
        f'<text x="190" y="380" fill="#f8fafc" font-size="30" font-family="Segoe UI">Primary-source confirmed: {primary}</text>',
        f'<text x="190" y="450" fill="#f8fafc" font-size="30" font-family="Segoe UI">Independent-source confirmed: {independent}</text>',
        '<rect x="850" y="220" width="470" height="70" rx="18" fill="#0f172a" stroke="#67e8f9"/>',
        '<text x="1085" y="264" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Evidence-governance result</text>',
        '<rect x="850" y="330" width="470" height="70" rx="18" fill="#0f172a" stroke="#f59e0b"/>',
        '<text x="1085" y="374" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">Not silicon validation</text>',
        '<rect x="850" y="440" width="470" height="70" rx="18" fill="#0f172a" stroke="#ef4444"/>',
        '<text x="1085" y="484" text-anchor="middle" fill="#e2e8f0" font-size="24" font-family="Segoe UI">No claim promotion</text>',
        '<text x="800" y="820" text-anchor="middle" fill="#94a3b8" font-size="22" font-family="Segoe UI">Paper-ready structure: abstract, method, artifacts, results, limitations, reproducibility, non-claim locks.</text>',
        '</svg>',
    ])

def manuscript_markdown(metrics: dict) -> str:
    title = "Tau Scaling as an Evidence-Gated Public Claim System"
    subtitle = "Source Population, Primary-Validation Gaps, and Non-Claim Locks"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""# {title}

## {subtitle}

**Author:** James Paul Jackson  
**Version:** TAU-SCALING-SA v0.9.1 — Manuscript Draft Scaffold  
**Date:** {now}  
**Repository artifact:** `tau-scaling`

---

## Abstract

This manuscript scaffold presents Tau Scaling as a public semiconductor-claim governance problem rather than as a validated silicon result. The repository evaluates public Tau Scaling and LogicFolding claims through a reproducible evidence pipeline: claim ledger, source provenance, source intake cards, public source population, primary-source validation gap review, release validation, and non-claim locks. In the current repository state, eight public claims are source-populated from public reporting, zero are primary-source confirmed, and zero are independently confirmed. The contribution is therefore a reproducible source-provenance and validation-gap artifact, not a claim of silicon validation, product validation, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.

## 1. Introduction

Public semiconductor claims often blend roadmap language, media interpretation, methodology framing, reported metrics, and implied validation. This creates an epistemic problem: a claim may be publicly visible without being primary-source confirmed, independently reproduced, or measurement-complete.

The `tau-scaling` repository treats this as a claim-governance problem. It does not ask whether a public claim is exciting. It asks what evidence class the claim belongs to, what source category supports it, what validation gates are missing, and which interpretations are blocked by the current evidence.

## 2. Research Question

Can public Tau Scaling claims be converted into a reproducible evidence-governance artifact that separates public source population from primary-source validation and claim promotion?

## 3. Method

The method is a staged evidence pipeline:

```text
{make_ascii_flow()}```

Each stage emits artifacts under versioned reports, manifests, visuals, and release checks. The pipeline preserves a hard distinction between:

- source-populated claims,
- primary-source confirmed claims,
- independently confirmed claims,
- source-validated claims,
- claim-promoted claims.

## 4. Repository Artifacts

The v0.9.0 public research milestone package includes:

- `releases/public_research_milestone_v0_9_0/README.md`
- `releases/public_research_milestone_v0_9_0/public_research_milestone_manifest_v0_9_0.json`
- `reports/public_research_milestone/latest_public_research_milestone.md`
- `reports/publishable_findings/latest_publishable_findings_brief.md`
- `reports/primary_source_gap_review/latest_primary_source_gap_review.md`
- `reports/public_source_population/latest_public_source_population_pass.md`
- `reports/evidence_sufficiency/latest_evidence_sufficiency_matrix.md`
- `reports/release/latest_release_readiness.md`

## 5. Results

| Metric | Value |
|---|---:|
| Public claims analyzed | {metrics.get("claim_count", 0)} |
| Source-populated claims | {metrics.get("source_populated_count", 0)} |
| Primary-source confirmed claims | {metrics.get("primary_source_confirmed_count", 0)} |
| Independent-source confirmed claims | {metrics.get("independent_source_confirmed_count", 0)} |
| High validation-gap claims | {metrics.get("high_gap_claim_count", 0)} |
| Release findings | {metrics.get("release_findings", 0)} |

The key result is not that Tau Scaling is validated. The key result is that the public claim field is now structured enough to show what is populated, what is missing, and what cannot yet be claimed.

## 6. Interpretation

The current evidence state supports the following bounded statement:

> Tau Scaling can be represented as an evidence-gated public claim system. The public claim field is source-populated, but not primary-source confirmed or independently validated in the current repository state.

This is publishable as an evidence-governance and source-provenance result.

## 7. Limitations

This artifact does not validate semiconductor performance. It does not establish Huawei product performance, manufacturing capability, process-node equivalence, benchmark superiority, investment relevance, or a universal Tau Scaling law. It also does not replace first-party disclosures, formal papers, patents, measurement protocols, silicon data, workload-specific benchmarks, or independent reproduction.

## 8. Reproducibility

Primary commands:

```powershell
python scripts/benchmarks/generate_tau_public_claim_ledger.py
python scripts/benchmarks/generate_public_source_ledger.py
python scripts/benchmarks/generate_source_evidence_intake_cards.py
python scripts/benchmarks/run_primary_source_intake_queue.py
python scripts/benchmarks/populate_public_source_intake_v0_8_8.py
python scripts/benchmarks/generate_primary_source_gap_review_v0_8_9.py
python scripts/release/build_public_research_milestone_v0_9_0.py
python scripts/release/build_manuscript_draft_scaffold_v0_9_1.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## 9. Non-Claim Locks

- Coherence is not truth.
- Public reporting is not primary validation.
- Source population is not source validation.
- Source validation is not claim promotion.
- A roadmap target is not an achieved result.
- A density-equivalence claim is not process-node equivalence.
- A local release pass is not silicon validation.

## 10. Future Work

The next technical step is to locate and evaluate first-party Huawei/HiSilicon material, formal technical disclosures, patents, conference records, or independent measurement sources. Any future source validation must preserve the distinction between public narrative, primary source confirmation, independent reproduction, and claim promotion.

## Citation Note

Cite this artifact as a repository-based evidence-governance manuscript scaffold, not as semiconductor validation.
"""

def latex_escape(s: str) -> str:
    return (s.replace("\\", r"\textbackslash{}")
             .replace("&", r"\&")
             .replace("%", r"\%")
             .replace("$", r"\$")
             .replace("#", r"\#")
             .replace("_", r"\_")
             .replace("{", r"\{")
             .replace("}", r"\}")
             .replace("~", r"\textasciitilde{}")
             .replace("^", r"\textasciicircum{}"))

def manuscript_latex(metrics: dict) -> str:
    # Simple one-file LaTeX scaffold, not compiled here.
    return r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{amsmath}

\title{Tau Scaling as an Evidence-Gated Public Claim System\\
\large Source Population, Primary-Validation Gaps, and Non-Claim Locks}
\author{James Paul Jackson}
\date{TAU-SCALING-SA v0.9.1}

\begin{document}
\maketitle

\begin{abstract}
This manuscript scaffold presents Tau Scaling as a public semiconductor-claim governance problem rather than as a validated silicon result. The repository evaluates public Tau Scaling and LogicFolding claims through a reproducible evidence pipeline. In the current repository state, eight public claims are source-populated from public reporting, zero are primary-source confirmed, and zero are independently confirmed. The contribution is therefore a reproducible source-provenance and validation-gap artifact, not a claim of silicon validation, product validation, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.
\end{abstract}

\section{Introduction}
Public semiconductor claims often blend roadmap language, media interpretation, methodology framing, reported metrics, and implied validation. The tau-scaling repository treats this as a claim-governance problem.

\section{Method}
The method converts public claims into a staged evidence pipeline:
claim ledger, source provenance, source intake cards, public source population, primary-source validation gap review, milestone package, and manuscript scaffold.

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
The current evidence state supports a bounded claim: Tau Scaling can be represented as an evidence-gated public claim system. It does not validate silicon or promote any technical claim beyond available evidence.

\section{Limitations}
This artifact does not validate semiconductor performance, Huawei product performance, manufacturing capability, process-node equivalence, benchmark superiority, or a universal Tau Scaling law.

\section{Reproducibility}
All source-provenance, validation-gap, release-readiness, and manuscript-scaffold artifacts are stored in the repository under reports, releases, sources, visuals, and docs.

\section{Non-Claim Locks}
Public reporting is not primary validation. Source population is not source validation. Source validation is not claim promotion. A roadmap target is not an achieved result.

\end{document}
"""

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)

    milestone = load_json(MILESTONE_JSON)
    metrics = milestone.get("metrics", {})

    md = manuscript_markdown(metrics)
    tex = manuscript_latex(metrics)

    write(DOCS_DIR / "tau_scaling_public_claim_system_v0_9_1.md", md)
    write(DOCS_DIR / "tau_scaling_public_claim_system_v0_9_1.tex", tex)
    write(DOCS_DIR / "README.md", "# Manuscript Drafts\n\nCurrent manuscript: `tau_scaling_public_claim_system_v0_9_1.md`\n\nBoundary: manuscript drafts describe evidence-governance artifacts, not semiconductor validation.\n")

    manifest = {
        "schema": "tau-scaling-manuscript-draft-scaffold-v0.9.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "Tau Scaling as an Evidence-Gated Public Claim System",
        "markdown": str((DOCS_DIR / "tau_scaling_public_claim_system_v0_9_1.md").relative_to(ROOT)),
        "latex": str((DOCS_DIR / "tau_scaling_public_claim_system_v0_9_1.tex").relative_to(ROOT)),
        "source_milestone": str(MILESTONE_JSON.relative_to(ROOT)),
        "metrics": metrics,
        "sections": [
            "abstract",
            "introduction",
            "research question",
            "method",
            "repository artifacts",
            "results",
            "interpretation",
            "limitations",
            "reproducibility",
            "non-claim locks",
            "future work",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "manuscript_claims_silicon_validation": False,
        "boundary": "v0.9.1 creates a manuscript draft scaffold from the v0.9.0 package. It does not validate sources, promote claims, validate silicon, validate products, or prove a universal Tau Scaling law.",
    }
    write_json(REPORT_DIR / "manuscript_draft_scaffold_v0_9_1.json", manifest)
    write_json(REPORT_DIR / "latest_manuscript_draft_scaffold.json", manifest)

    report = "# Manuscript Draft Scaffold v0.9.1\n\n"
    report += "## Outputs\n\n"
    report += f"- Markdown manuscript: `{manifest['markdown']}`\n"
    report += f"- LaTeX manuscript: `{manifest['latex']}`\n"
    report += "- Visual: `visuals/manuscript_draft/v0_9_1/manuscript_draft_scaffold.svg`\n\n"
    report += "## Boundary\n\n" + manifest["boundary"] + "\n"
    write(REPORT_DIR / "manuscript_draft_scaffold_v0_9_1.md", report)
    write(REPORT_DIR / "latest_manuscript_draft_scaffold.md", report)
    write(REPORT_DIR / "README.md", "# Manuscript Draft Reports\n\nCurrent layer: **TAU-SCALING-SA v0.9.1 - Manuscript Draft Scaffold**\n\nBoundary: manuscript scaffolding is not source validation or claim promotion.\n")

    write(VIS_DIR / "manuscript_draft_scaffold.svg", make_svg(metrics))
    write(VIS_DIR / "README.md", "# v0.9.1 Manuscript Draft Visuals\n\n- `manuscript_draft_scaffold.svg`\n\nBoundary: manuscript visualization only.\n")

    print(json.dumps({
        "schema": manifest["schema"],
        "markdown": manifest["markdown"],
        "latex": manifest["latex"],
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
        "report": "reports/manuscript_draft/latest_manuscript_draft_scaffold.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()