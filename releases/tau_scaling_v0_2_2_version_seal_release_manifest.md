# TAU-SCALING-SA v0.2.2 — Version Seal / Release Manifest Layer

Generated: 2026-05-26T09:11:14Z

## Status

**Sealed local checkpoint.**

This release records the clean local Tau Scaling runtime + RCC-N repository-structure checkpoint after root cleanup and version alignment.

## Current Results

| Surface | Result |
|---|---:|
| Package version | 0.2.0 |
| Latest run id | 20260526T091115Z |
| Latest TSEK class | TSEK-C |
| Latest A_TSEK | 0 |
| Diagnostic average | 0.9091 |
| Findings | 1 |
| RCC-N checker | passed |
| RCC-N errors | 0 |
| RCC-N warnings | 0 |
| Mini README coverage | 1 |
| Major dirs checked | 25 |
| Architecture validator | passed |
| Architecture errors | 0 |
| Architecture warnings | 0 |
| Unit tests | 6 OK |
| Runtime demo | evidence emitted |

## Release Surfaces

| Surface | Path |
|---|---|
| Release manifest JSON | $ManifestJsonPath |
| Release manifest MD | $ManifestMdPath |
| Latest evidence package | rtifacts/runs/latest/evidence_package.json |
| Classifier result | rtifacts/runs/latest/scoring/classifier_result.json |
| Downgrade ledger | rtifacts/runs/latest/ledger/downgrade_ledger.jsonl |
| RCC-N report | eports/rcc_nexus/latest_rcc_nexus_check.md |
| Architecture report | eports/architecture/latest_architecture_contract_validation.md |
| Cleanup report | eports/cleanup/latest_root_cleanup_status.md |

## Interpretation

The checkpoint proves local repo functionality only:

`	ext
Runtime works.
Evidence emits.
RCC-N navigation validates.
Mini READMEs are covered.
Architecture contract validates.
Root identity is cleaned.
Version identity is aligned.
`

The checkpoint does **not** prove independent silicon validation, product performance, manufacturing capability, benchmark superiority, process-node equivalence, or a universal physical law.

## Current Classification Boundary

The latest demo remains **TSEK-C**.

That is correct because the evidence package intentionally preserves downgrade discipline. A simulation-backed or roadmap-backed claim does not become a strong admissible silicon claim unless missing evidence gates are disclosed and independently validated.

## Non-Claim Locks

- Roadmap coherence is not validation.
- Simulation is not silicon evidence.
- Documentation is not correctness.
- RCC-N navigation is not code correctness.
- Density equivalence is not node equivalence.
- Local path win is not full-chip win.
- Context reconstruction is not correctness proof.
- Validation remains required.

## Validation Commands

`powershell
python -m unittest discover -s tests
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
`

## Next Recommended Version

**TAU-SCALING-SA v0.3 — Evidence Promotion Path Layer**

Recommended goals:

- Add a second seed where yield evidence is disclosed.
- Add promotion requirements report.
- Add missing-gate explainer.
- Add current public metrics auto-refresh.
- Add release/checkpoint validator.