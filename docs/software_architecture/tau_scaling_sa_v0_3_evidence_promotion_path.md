# TAU-SCALING-SA v0.3 â€” Evidence Promotion Path Layer

Generated: 2026-05-26T05:30:39-04:00

## Status

Architecture layer for the next Tau Scaling runtime evolution. This document is implementation-guiding and downgrade-preserving.

## Core Purpose

v0.3 adds an evidence-promotion path without weakening TSEK gates. The runtime must show how a claim moves from a downgraded local demonstration toward stronger evidence classes only when specific missing evidence surfaces are declared.

Current behavior remains valid:

`	ext
logicfolding_claim_card.json
â†’ missing yield evidence / independent validation
â†’ TSEK-C
â†’ A_TSEK = 0.0000
`

v0.3 adds a controlled ladder:

`	ext
TSEK-C demo claim
â†’ disclosed-yield promotion-path seed
â†’ missing-gate explainer
â†’ promotion requirements report
â†’ evidence ladder comparison
â†’ no strong claim unless all gates survive
`

## Runtime Invariant

No gate may be weakened to produce a better class. The only valid promotion path is additional disclosed evidence.

## Promotion Ladder

| Tier | Required condition | Meaning |
|---|---|---|
| TSEK-C | public/source-bounded or simulated evidence only | Claim remains interpretive/runtime-local. |
| TSEK-B candidate | workload, baseline, candidate, tau vector, gates, yield method, and yield result are disclosed | Stronger local evidence surface, still not independent silicon validation. |
| TSEK-A candidate | independent validation package present and reproducible under declared workload | High evidence class, still bounded by task and source. |

## Required v0.3 Runtime Surfaces

1. A second seed: configs/seeds/logicfolding_promotion_path_claim_card.json.
2. A promotion-path architecture note: docs/architecture/evidence_promotion_path.md.
3. A protocol note: docs/protocols/evidence_promotion_path.md.
4. Root README update rule requiring directory box + mini README synchronization.
5. Mini README update rule injected into every folder-level README.
6. Current public metrics updated after each release/checkpoint.

## Evidence Promotion Rules

A claim may only move upward when the evidence changes, not when wording changes.

Required promotion fields:

`json
{
  "yield_method_disclosure": {
    "method_disclosed": true,
    "yield_reported": true
  },
  "evidence_disclosure": {
    "evidence_package_complete": true,
    "independent_validation_present": false
  }
}
`

This may improve a candidate classification, but it must not become an independent-validation claim while independent_validation_present remains false.

## AI Directory and Mini README Rule

Every AI or human patch that changes repository structure must update:

1. Root README Full Directory Box.
2. Any affected folder-level mini README.
3. docs/context/repository_context_index.json when routing changes.
4. docs/context/rcc_nexus_index.json when Nexus positioning changes.
5. cc/nexus/route_map.json when task routes change.
6. Relevant validation reports after checks are rerun.

If a folder is added, removed, renamed, or repurposed, the mini README update is mandatory in the same commit.

## Non-Claim Locks

- Simulation is not silicon validation.
- Yield disclosure is not independent validation.
- Documentation is not correctness.
- RCC-N navigation is not code correctness.
- Local path win is not full-chip win.
- Density equivalence is not node equivalence.
- Evidence packages are task-bounded artifacts, not universal proof.

## Validation Commands

`powershell
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json
`

## Boundary

v0.3 is a promotion-path architecture. It does not independently validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or a universal Tau Scaling law.