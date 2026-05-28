# Tau Scaling as an Evidence-Gated Public Claim System

## Source Population, Primary-Validation Gaps, and Non-Claim Locks

**Author:** James Paul Jackson  
**Version:** TAU-SCALING-SA v0.9.1 — Manuscript Draft Scaffold  
**Date:** 2026-05-28  
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
raw public claim
  -> claim ledger
  -> source provenance map
  -> source intake card
  -> public source population
  -> primary-source validation gap review
  -> publishable finding
  -> milestone package
  -> manuscript scaffold
```

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
| Public claims analyzed | 8 |
| Source-populated claims | 8 |
| Primary-source confirmed claims | 0 |
| Independent-source confirmed claims | 0 |
| High validation-gap claims | 8 |
| Release findings | 0 |

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
