# RCC Context Map — Tau Scaling

## Public spine

Tau Scaling runtime converts public or internal scaling claims into structured evidence packages.

## Main code surfaces

| Path | Purpose |
|---|---|
| `src/tau_scaling/core/` | runtime orchestration |
| `src/tau_scaling/claims/` | claim cards, classification, downgrade logic |
| `src/tau_scaling/gates/` | LogicFolding, edge-surface, gamma tau ETP, PVT, evidence gates |
| `src/tau_scaling/simulation/` | Monte Carlo checker stress tests |
| `src/tau_scaling/evidence/` | evidence package writer, reports, visuals |
| `configs/seeds/` | runnable example inputs |
| `artifacts/runs/` | emitted runtime outputs |

## Agent rules

1. Do not upgrade TSEK class without evidence.
2. Do not treat Monte Carlo as silicon validation.
3. Do not treat density equivalence as node equivalence.
4. Preserve source boundaries.
5. Emit evidence for every run.
