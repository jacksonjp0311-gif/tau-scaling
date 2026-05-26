# TAU-SCALING-SA v0.4.0b - Synthetic Gate Expectation Calibration

Generated: 2026-05-26T13:22:30.617950+00:00

## Purpose

Repair the v0.4.0a synthetic gate suite after one scenario failed due to an incorrect expected class.

## Diagnosis

The `multi_gate_stress_low_disclosure` scenario disables almost every hard gate while leaving source disclosure intact. Under the current classifier algebra, only one of eleven hard gates survives, so `diagnostic_average` is below the TSEK-D threshold and the correct class is TSEK-E.

## Repair

- Calibrate expected class for `multi_gate_stress_low_disclosure` from TSEK-D to TSEK-E.
- Add non-zero exit behavior when any synthetic scenario fails.
- Regenerate reports and charts.
- Add L-016 to the README failure-learning ledger.

## Required Validation

```powershell
python scripts/benchmarks/run_synthetic_gate_suite.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## Boundary

This repair calibrates local synthetic expectations only. It does not alter Tau Scaling gate math, classifier thresholds, silicon evidence, product evidence, manufacturing evidence, process-node equivalence, or universal-law claims.
