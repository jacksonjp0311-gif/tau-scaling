# Tau Scaling as an Evidence-Gated Public Claim System

## Source Population, Primary-Validation Gaps, and Non-Claim Locks

**Author:** James Paul Jackson  
**Version:** TAU-SCALING-SA v0.9.3 — Manuscript Polish and Submission Package  
**Date:** 2026-05-28  
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
| Public claims analyzed | 8 |
| Source-populated claims | 8 |
| Primary-source confirmed claims | 0 |
| Independent-source confirmed claims | 0 |
| High validation-gap claims | 8 |
| Release findings | 0 |

The principal result is not validation of Tau Scaling. The principal result is the reproducible separation of public claim visibility, source population, primary-source confirmation, independent validation, and claim promotion.

## Evidence Table

# Evidence Table v0.9.2

| Claim | Class | Source category | Sources | Primary? | Independent? | Gap | Promotion? |
|---|---|---|---:|---:|---:|---|---:|
| `tau-public-001-methodology` | TSEK-C | methodology_claim | 2 | False | False | HIGH (14) | False |
| `tau-public-002-logicfolding` | TSEK-C | architecture_interpretation | 3 | False | False | HIGH (15) | False |
| `tau-public-003-density-equivalent` | TSEK-C | reported_metric | 2 | False | False | HIGH (15) | False |
| `tau-public-004-roadmap-1p4nm-class` | TSEK-C | roadmap_projection | 2 | False | False | HIGH (15) | False |
| `tau-public-005-unified-bus` | TSEK-C | architecture_interpretation | 2 | False | False | HIGH (15) | False |
| `tau-public-006-hione-optical-io` | TSEK-C | reported_metric | 1 | False | False | HIGH (15) | False |
| `tau-public-007-3d-folding` | TSEK-C | architecture_interpretation | 2 | False | False | HIGH (15) | False |
| `tau-public-008-ai-gap-closure` | TSEK-C | media_interpretation | 3 | False | False | HIGH (14) | False |

## Boundary

Source-populated does not mean source-validated. No claim is promoted by this table.


## Figure Index and Captions

# Figure Pack v0.9.2

## fig:public-research-milestone

- Path: `visuals/public_research_milestone/v0_9_0/public_research_milestone.svg`
- Caption: Public research milestone summary showing eight source-populated claims, zero primary-source confirmations, and zero independent confirmations.
- Boundary: Visualization of evidence-governance state only.

## fig:primary-source-gap

- Path: `visuals/primary_source_gap_review/v0_8_9/primary_source_gap_review.svg`
- Caption: Primary-source validation gap review showing the separation between source population, primary-source confirmation, and independent validation.
- Boundary: Validation-gap visualization only.

## fig:public-source-population

- Path: `visuals/public_source_population/v0_8_8/public_source_population_pass.svg`
- Caption: Public source population pass showing that all public claims can be populated from public reporting while source validation remains unclaimed.
- Boundary: Source population visualization only.

## fig:manuscript-scaffold

- Path: `visuals/manuscript_draft/v0_9_1/manuscript_draft_scaffold.svg`
- Caption: Manuscript scaffold view showing the transformation from evidence package to paper-style structure.
- Boundary: Manuscript structure visualization only.



## Limitations

# Limitations Table v0.9.2

| Limitation | Impact | Next evidence required |
|---|---|---|
| No primary-source confirmation | Public reports cannot be treated as first-party validation. | Huawei/HiSilicon paper, patent, conference material, technical note, or formal disclosure. |
| No independent reproduction | Claims cannot be promoted to independently verified status. | Third-party measurement, benchmark reproduction, or peer-reviewed validation. |
| No workload-complete benchmark | Reported gains cannot be generalized across workloads. | Declared workload, baseline, candidate artifact, measurement method, and uncertainty. |
| No energy / thermal / PDN / PVT companion evidence | Time or density claims cannot be treated as complete scaling claims. | Power, thermal, robustness, yield, and variation data. |
| Roadmap language may be confused with achieved result | 2031 or node-equivalent targets must not be interpreted as current silicon proof. | Date-bound milestone trace and achieved-result evidence. |


## Artifact Map

# Artifact Map v0.9.2

| Artifact | Path | Role |
|---|---|---|
| Claim ledger | `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md` | Defines public claims and current TSEK classes. |
| Public source ledger | `reports/public_source_ledger/latest_public_source_ledger.md` | Maps claims to source categories and source-carry boundaries. |
| Source population manifest | `sources/primary_source_intake/source_population_manifest_v0_8_8.json` | Stores bounded public source records. |
| Primary-source gap review | `reports/primary_source_gap_review/latest_primary_source_gap_review.md` | Identifies missing primary and independent evidence. |
| Milestone package | `releases/public_research_milestone_v0_9_0/README.md` | Packages the public research spine. |
| Manuscript draft | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md` | Converts the package into a paper-style draft. |


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
