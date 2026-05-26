# Tau Scaling in 90 Seconds

Tau Scaling is a local Python runtime for evidence-gating tau-scaling claims.

## Core chain

    claim → claim card → workload → tau vector → gates → stress test → TSEK class → evidence package

## First command

    python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json

## Validation

    python -m unittest discover -s tests
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py

## Non-claim lock

Roadmap coherence is not validation. Simulation is not silicon evidence. Density equivalence is not node equivalence. Local path win is not full-chip win.