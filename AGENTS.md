# AGENTS.md — Tau Scaling Agent Operating Contract

Current contract: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**

## Mission

Operate inside the Tau Scaling Nexus without drifting repository state, claim boundaries, validation surfaces, or public README.

This repository is a local-first, evidence-gated tau-claim runtime. It does not independently validate silicon, product metrics, manufacturing capability, benchmark superiority, process-node equivalence, or a universal Tau Scaling law.

## Required Read Order

Before editing, read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `docs/context/repository_context_index.json`
5. `docs/context/rcc_nexus_index.json`
6. `rcc/nexus/route_map.json`
7. `rcc/nexus/task_routing_matrix.md`
8. the target folder `README.md`
9. relevant source, tests, evidence, reports, or claim cards

## Geometry Route Rule

Every patch must identify its route:

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

Shell meanings:

```text
center  = source boundaries, non-claim locks, architecture, context indexes
inner   = claim cards, tau vectors, gates, schemas, classifier state
middle  = CLI flows, tests, scripts, benchmarks, release validator
outer   = reports, evidence packages, ledgers, visuals, release notes
```

## Required Validation

For every non-trivial patch, run:

```powershell
python scripts/release/validate_release.py
python scripts/rcc/audit_readme_surface.py
python scripts/benchmarks/run_synthetic_gate_suite.py
python scripts/benchmarks/run_sensitivity_sweep.py
python scripts/benchmarks/run_gate_interaction_matrix.py
python -m unittest discover -s tests
```

## Task-Specific Routing

| Task | Read first | Required validation |
|---|---|---|
| Runtime patch | `src/tau_scaling/README.md`, `tests/`, latest evidence | `python scripts/release/validate_release.py` |
| Claim classifier patch | `src/tau_scaling/claims/README.md`, claim cards, evidence packages | release validator + baseline/promotion claims |
| Gate logic patch | `src/tau_scaling/gates/README.md`, gate tests, synthetic claim cards | release validator + gate suite |
| README / mini README patch | root README, target mini README, route map | README audit + release validator |
| RCC-N patch | `docs/context/`, `rcc/nexus/`, route map | RCC-N checker + README audit + release validator |
| Benchmark patch | `scripts/benchmarks/`, `reports/benchmarks/`, `docs/benchmarks/` | release validator + benchmark summary |
| Synthetic gate test patch | `configs/seeds/tests/`, `reports/gates/`, gate docs | release validator + synthetic gate report |
| Sensitivity sweep patch | `configs/seeds/sweeps/`, `reports/sensitivity/`, `visuals/sensitivity/` | release validator + sensitivity report + benchmark atlas update |
| Gate interaction patch | `configs/seeds/interactions/`, `reports/interactions/`, `visuals/interactions/` | release validator + interaction matrix report + benchmark atlas update |
| Public claim replay patch | source boundary docs, `configs/seeds/public_claims/`, claim reports | release validator + claim replay report |
| Directory structure patch | Full Directory Box, affected mini READMEs, context indexes | README audit + RCC-N + release validator |

## v0.4.1 Sensitivity-Sweep Start Rule

Do not begin or promote v0.4.1 Synthetic Gate Sensitivity Sweep work unless:

```text
release validator: passed
README audit: passed
unit tests: OK
AGENTS.md: synchronized with README Required Validation
task_routing_matrix.md: includes synthetic gate, sensitivity sweep, benchmark atlas, and public claim routes
benchmark atlas: current
reflection layer: current
```

## Failure Learning Rule

If a failure occurs, update the AI Failure Learning Ledger in `README.md` and the affected local mini README when the failure teaches a reusable rule.

Failures are repository memory, not blame records.

## Non-Claim Locks

- navigation_is_not_validation
- documentation_is_not_correctness
- simulation_is_not_silicon_validation
- simulation_is_not_silicon_evidence
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win
- context_reconstruction_is_not_correctness_proof
- validation_remains_required
- release_readiness_is_not_silicon_validation
- synthetic_gate_tests_are_not_product_validation
- geometric_routing_is_not_ai_understanding


## Synthetic Gate Charts

v0.4.0 requires benchmark and finding charts under `visuals/benchmarks/v0_4_0/` and `visuals/findings/v0_4_0/` whenever synthetic gate behavior changes.


## Reflection Rule

After any release-like README, benchmark, chart, or route evolution, update:

```text
README.md
AGENTS.md
rcc/nexus/task_routing_matrix.md
docs/reflection/
reports/reflection/
```

Non-claim lock: reflection improves continuity and routing only. It is not external validation.
