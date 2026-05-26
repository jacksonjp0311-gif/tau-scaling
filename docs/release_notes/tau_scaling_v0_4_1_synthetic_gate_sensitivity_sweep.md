# TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep

Generated: 2026-05-26T14:52:13.832518+00:00

## Purpose

Move from discrete synthetic gate scenarios to threshold curves.

## Additions

- `scripts/benchmarks/run_sensitivity_sweep.py`
- `configs/seeds/sweeps/`
- `reports/sensitivity/`
- `visuals/sensitivity/v0_4_1/`
- README/AGENTS/route-map/benchmark-atlas updates.

## Sweep Families

```text
logicfolding_vertical_penalty
gamma_tau_etp_tau_gain
overclaim_pressure
```

## Boundary

Sensitivity sweeps are synthetic local runtime diagnostics only. They do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
