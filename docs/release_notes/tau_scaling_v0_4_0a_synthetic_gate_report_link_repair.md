# TAU-SCALING-SA v0.4.0a - Synthetic Gate Report Link Repair

Generated: 2026-05-26T13:13:36.809169+00:00

## Purpose

Repair the v0.4.0 synthetic gate report renderer after charts were generated but Markdown report rendering failed.

## Root Cause

`run_synthetic_gate_suite.py` attempted to compute image links with:

```python
Path(REPO_ROOT / chart).relative_to(REPORT_DIR)
```

That fails because chart files live under `visuals/`, while `REPORT_DIR` is `reports/benchmarks/v0_4_0`.

## Repair

The Markdown renderer now emits repo-root-safe relative links from `reports/benchmarks/v0_4_0` to `visuals/...`.

## Required Validation

```powershell
python scripts/benchmarks/run_synthetic_gate_suite.py
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
```

## Boundary

This repair affects report rendering only. It does not alter Tau Scaling gate math, classifier thresholds, silicon evidence, product evidence, manufacturing evidence, or universal-law claims.
