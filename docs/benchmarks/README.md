# Benchmark Documentation

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder records benchmark interpretation, chart registries, and non-claim boundaries.

## Primary Files

| File | Role |
|---|---|
| `benchmark_atlas.md` | Versioned benchmark/finding/chart registry. |

## Current Findings

- v0.3.2 established collision-proof benchmark identity.
- v0.4.0 generated synthetic gate charts but exposed a Markdown path bug.
- v0.4.0a repaired chart report links but exposed one expectation mismatch.
- v0.4.0b calibrated expectations and achieved 10/10 synthetic scenarios.
- v0.4.0c adds this atlas/index layer.

## Boundary

Benchmark documentation is local-runtime interpretation only. It is not silicon validation or product validation.

## AI / RCC Update Rule

If benchmark commands, reports, charts, folders, or interpretation boundaries change, update this mini README, the root `README.md`, `docs/benchmarks/benchmark_atlas.md`, and the relevant RCC route surfaces in the same commit.

Required follow-up validation:

```powershell
python scripts/rcc/audit_readme_surface.py
python scripts/release/validate_release.py
```

Non-claim lock: AI/RCC update guidance improves navigation and context alignment only. It is not code correctness, silicon validation, product validation, benchmark superiority proof, or universal Tau Scaling proof.
