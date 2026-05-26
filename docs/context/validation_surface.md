# Validation Surface — Tau Scaling

## Core commands

    python -m unittest discover -s tests
    python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py

## Evidence surfaces

- artifacts/runs/latest/evidence_package.json
- outputs/evidence/latest_evidence_package.json
- outputs/reports/latest_tau_scaling_summary.md
- reports/rcc_nexus/latest_rcc_nexus_check.md

## Boundary

Validation commands test local runtime, documentation, and evidence-surface integrity. They do not independently validate silicon, Huawei product metrics, process-node equivalence, or manufacturing claims.