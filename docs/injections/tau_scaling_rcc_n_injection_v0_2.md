# Tau Scaling RCC-N / OMN-Style Repository Injection v0.2

Date: 2026-05-26

## Purpose

Inject OMN-style repository structure, README trisection, RCC-N navigation, mini READMEs, docs/context indexes, route maps, validation surfaces, and version records into the Tau Scaling runtime repo.

## Preserved locks

- No classifier loosening.
- No independent silicon validation claim.
- No product endorsement.
- No process-node equivalence claim.
- Navigation is not validation.
- Documentation is not correctness.

## Validation

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests