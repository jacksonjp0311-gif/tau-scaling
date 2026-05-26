# Tau Scaling README Lock Visibility Repair Status

Generated: 2026-05-26T05:01:10-04:00

Repo:

    C:\Users\jacks\OneDrive\Desktop\tau-scaling

Patch applied:

- Ensured root README exposes validator-visible non-claim locks.
- Added / reinforced:
  - Roadmap coherence is not validation.
  - Simulation is not silicon evidence.
  - Documentation is not correctness.
  - documentation_is_not_correctness
  - RCC-N navigation is not code correctness.
  - Density equivalence is not node equivalence.
  - Local path win is not full-chip win.
  - Context reconstruction is not correctness proof.
  - Validation remains required.

Validation commands:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

Boundary:

This patch repairs README/RCC-N visibility only. It does not change runtime behavior, classifier logic, silicon validation status, product evidence, node-equivalence status, or Tau Scaling claim strength.