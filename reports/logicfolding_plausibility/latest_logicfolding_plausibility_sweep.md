# LogicFolding Plausibility Sweep v0.8.3

## Purpose

Test when the TSEK LogicFolding inequality becomes plausible under synthetic priors.

```text
rho_c * E[delta_tau_wire] > E[tau_vertical] + tau_route + tau_sync + tau_variation + tau_closure
gamma_tau_ETP > 1
```

## Research Finding

LogicFolding is conditionally plausible when critical-path coverage and wire-delay savings are high enough to dominate vertical, routing, synchronization, variation, and closure costs, and when energy/thermal/PDN-normalized tau gain remains above one.

## Scenario Results

| Scenario | Mean margin ps | Mean gamma_tau_ETP | Margin pass % | Gamma pass % | Closure proxy pass % | Joint pass % | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Conservative public | -63.899 | 0.7087 | 0.0 | 4.28 | 4.42 | 0.0 | not_plausible_under_declared_priors |
| Balanced engineering | -18.949 | 1.2578 | 7.6 | 82.18 | 83.18 | 5.98 | narrow_plausibility_window |
| Optimistic reported path | 35.766 | 2.1046 | 99.16 | 100.0 | 100.0 | 99.16 | plausible_under_declared_priors |
| Aggressive best-case | 96.797 | 3.3571 | 100.0 | 100.0 | 100.0 | 100.0 | plausible_under_declared_priors |
| Thermal stressed | 24.561 | 0.8033 | 92.38 | 17.24 | 100.0 | 15.84 | narrow_plausibility_window |
| Closure stressed | -38.973 | 1.2423 | 2.2 | 78.34 | 37.1 | 1.72 | narrow_plausibility_window |

## Strongest Scenario

`Aggressive best-case` with joint pass `100.0%`.

## Falsification Pressure

Thermal-stressed and closure-stressed priors show how plausible timing gains can collapse when companion gates dominate.

## Visual

![LogicFolding plausibility sweep](../../visuals/logicfolding_plausibility/v0_8_3/logicfolding_plausibility_sweep.svg)

## Boundary

This sweep tests synthetic plausibility of a TSEK inequality. It does not validate Huawei silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
