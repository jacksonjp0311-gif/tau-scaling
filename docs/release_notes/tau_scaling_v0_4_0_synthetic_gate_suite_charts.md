# TAU-SCALING-SA v0.4.0 - Synthetic Gate Test Suite + Benchmark Finding Charts

Generated: 2026-05-26T13:09:00.346036+00:00

## Purpose

Move Tau Scaling from release-readiness infrastructure into controlled local experimental diagnostics.

## Additions

- Synthetic gate seeds under `configs/seeds/tests/`.
- Synthetic gate suite runner: `scripts/benchmarks/run_synthetic_gate_suite.py`.
- Benchmark charts under `visuals/benchmarks/v0_4_0/`.
- Per-finding charts under `visuals/findings/v0_4_0/`.
- Reports under `reports/benchmarks/`, `reports/gates/`, and `reports/findings/`.
- README, AGENTS, and route map updated for v0.4.0.

## Boundary

This release validates local runtime downgrade behavior under synthetic conditions only. It does not validate silicon, product claims, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
