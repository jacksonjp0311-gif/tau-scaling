# Tau Scaling — Evidence-Gated Tau-Claim Runtime

[![RCC-N](https://img.shields.io/badge/RCC--N-passing-brightgreen)](#rcc-nexus-status)
[![Architecture](https://img.shields.io/badge/architecture-passing-brightgreen)](#validation-status)
[![Tests](https://img.shields.io/badge/tests-6%20OK-brightgreen)](#validation-status)
[![Claim Class](https://img.shields.io/badge/latest%20claim-TSEK--C-yellow)](#current-public-metrics)

**Repository:** `tau-scaling`  
**Package / CLI:** `tau_scaling` / `tau-scaling`  
**Current checkpoint:** `TAU-SCALING-SA v0.2.3 — README / Nexus Public Polish`  
**Previous seal:** `TAU-SCALING-SA v0.2.2 — Version Seal / Release Manifest Layer`

Tau Scaling is a local-first, evidence-gated Python runtime for evaluating tau-scaling claims through structured claim cards, workload declarations, tau vectors, LogicFolding survivability checks, edge-to-surface boundary algebra, energy / thermal / PDN / PVT gates, Monte Carlo checker stress, TSEK classification, evidence packages, and RCC-N / OMN-style repository navigation.

> **Core law:** No workload, no tau claim. No baseline, no gain. No gates, no validation. No evidence, no strong class.

---

## Human Director Box

### What this repository is

This repo is a governed claim-evaluation workbench. It turns a tau-scaling claim into a structured audit path:

```text
claim
→ source boundary
→ claim card
→ workload profile
→ tau vector
→ baseline / candidate manifests
→ LogicFolding survivability
→ edge-surface boundary model
→ energy / thermal / PDN / PVT gates
→ Monte Carlo checker stress
→ TSEK classifier
→ evidence package
→ reports / ledgers / visuals
→ release manifest
```

### What this repository is not

This repo does **not** independently validate silicon, Huawei product metrics, manufacturing capability, benchmark superiority, process-node equivalence, investment value, or universal Tau Scaling law. It is a local runtime for evidence discipline and claim classification.

---

## Current Public Metrics

| Surface | Result |
|---|---:|
| Current release seal | `TAU-SCALING-SA v0.2.2` |
| README polish layer | `v0.2.3` |
| Package version | `0.2.0` |
| Latest expected runtime class | `TSEK-C` |
| Latest expected `A_TSEK` | `0.0000` |
| RCC-N checker | passing |
| Architecture validator | passing |
| Unit tests | `6 OK` |
| Mini README coverage | `1.0` |
| Major dirs checked | `25` |
| Claim status | local runtime evidence only |

The latest demo remains `TSEK-C` by design: the system is refusing to promote a claim beyond disclosed evidence.

---

## Quick Start

```powershell
cd "C:\Users\jacks\OneDrive\Desktop\tau-scaling"
.\.venv\Scripts\Activate.ps1

python -m tau_scaling --help
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
```

---

## Repository Layers

This repo combines three layers:

| Layer | Purpose | Main paths |
|---|---|---|
| Tau Scaling runtime | Executes claim cards, gates, classifier, evidence emission | `src/tau_scaling/`, `configs/seeds/`, `tests/` |
| RCC-N navigation | Makes the repo self-locating for humans and AI agents | `rcc/nexus/`, `docs/context/`, folder `README.md` files |
| Codex documentation shell | Records source boundaries, releases, architecture, non-claim locks | `docs/`, `reports/`, `releases/`, `visuals/` |

---

# PART I - Human README
## What Tau Scaling Tests

| Seed / surface | Purpose |
|---|---|
| `logicfolding_claim_card.json` | Tests global LogicFolding survivability and downgrade behavior. |
| `edge_surface_boundary_toy.json` | Tests edge-bound resource starvation vs. surface-coupled scaling. |
| `gamma_tau_etp_toy.json` | Tests energy / thermal / PDN-normalized tau gain. |
| `monte_carlo_stress_toy.json` | Tests checker sensitivity under synthetic priors. |
| `codex_tau_vector_toy.json` | Tests Codex governance-latency analogy while preserving physical non-equivalence. |

Tau Scaling rewards bounded evidence emission, not confident overclaiming.

## Project Structure Director

| Surface | What it does | Why it matters |
|---|---|---|
| `AGENTS.md` | Defines agent entry order and patch discipline. | Prevents blind patching. |
| `README.md` | Human, RCC Nexus, and AI Agent root orientation. | Public front door. |
| `README_90_SECONDS.md` | Compressed onboarding. | Fast adoption surface. |
| `configs/seeds/` | Runnable claim-card and toy seeds. | Makes assumptions inspectable. |
| `src/tau_scaling/` | Executable runtime implementation. | Contains Tau Scaling behavior. |
| `tests/` | Runtime and gate tests. | Catches scaffold regressions. |
| `docs/context/` | Repository context and validation surface. | Main self-description layer. |
| `docs/software_architecture/` | TAU-SCALING-SA architecture lane. | Connects theory to software. |
| `docs/injections/` | RCC-N / structure injection records. | Records governance additions. |
| `docs/release_notes/` | Version continuity records. | Preserves lineage. |
| `rcc/nexus/` | Route map, protocol, Echo template, task matrix. | Makes the repo agent-navigable. |
| `reports/rcc_nexus/` | RCC-N checker outputs. | Makes navigation health inspectable. |
| `reports/architecture/` | Architecture validator outputs. | Makes contract health inspectable. |
| `releases/` | Release manifest JSON/MD. | Machine-readable checkpoint surface. |
| `artifacts/runs/latest/` | Latest runtime evidence package. | Primary runtime output. |
| `outputs/` | Stable mirrored evidence surfaces. | Human/agent-friendly output mirror. |
| `visuals/tau_scaling/` | Classification/dashboard visuals. | Public explanation surface. |

## Evidence Artifacts

Primary runtime artifacts are written under:

```text
artifacts/runs/latest/
```

Mirrored evidence surfaces are written under:

```text
outputs/evidence/
outputs/reports/
outputs/plots/
outputs/ledger/
```

Release and validation surfaces are written under:

```text
releases/
reports/rcc_nexus/
reports/architecture/
reports/release/
docs/benchmarks/
```

---

# PART II - RCC Nexus README
## RCC Nexus Identity

RCC tells the agent what the repository means.  
RCC-N tells the agent where it is.  
Validation tells the agent whether reality agreed.

## Repository Sphere

| Shell | Meaning |
|---|---|
| center | Source boundary, non-claim locks, architecture, context indexes. |
| inner | Runtime primitives: claim cards, tau vectors, gate records, schemas. |
| middle | Processes: CLI flow, examples, tests, scripts, checker workflows. |
| outer | Evidence / reflection: artifacts, outputs, ledgers, reports, visuals, release notes. |

## Nexus Meridians

`source`, `validation`, `evidence`, `drift`, `agent`, `safety`, `runtime`, `tau`, `release`, `documentation`

## Nexus Sectors

`core`, `schemas`, `tau`, `runtime`, `validation`, `evidence`, `rcc`, `agent`, `examples`, `release`

## Primary Nexus Files

| File | Role |
|---|---|
| `docs/context/repository_context_index.json` | Repository meaning map. |
| `docs/context/rcc_nexus_index.json` | Nexus route and coverage index. |
| `docs/context/validation_surface.md` | Validation commands and claim boundaries. |
| `rcc/nexus/README.md` | RCC-N local orientation. |
| `rcc/nexus/rcc_nexus_protocol.md` | Nexus protocol. |
| `rcc/nexus/route_map.json` | Machine-readable routing map. |
| `rcc/nexus/task_routing_matrix.md` | Task-to-validation routing. |
| `rcc/nexus/echo_location_template.md` | Mini README Echo Location template. |
| `rcc/nexus/agent_handoff_contract.md` | Agent handoff rules. |
| `scripts/rcc/check_rcc_nexus.py` | RCC-N checker. |
| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Latest RCC-N report. |

## RCC Nexus Echo Location

| Field | Value |
|---|---|
| Shell | center |
| Meridians | source, safety, agent, runtime, evidence |
| Sector | rcc |
| Version / TTL | RCC-N-v1.7 / 180 days |
| Last verified | 2026-05-26 |
| Local role | Root orientation surface for humans, RCC Nexus navigation, and AI agents. |

## RCC-N Status

The Nexus is working when the following command passes with zero warnings:

```powershell
python scripts/rcc/check_rcc_nexus.py
```

Expected current state:

```text
passed: true
errors: 0
warnings: 0
mini_readme_coverage: 1.0
major_dirs_checked: 25
```

RCC-N checks repository navigation and context integrity. It does not prove code correctness, patch safety, independent silicon validation, product performance, process-node equivalence, AI understanding, or production readiness.

---

# PART III - AI Agent README
## AI Operating Contract

Before editing, an AI agent must read:

1. `README.md`
2. `README_90_SECONDS.md`
3. `AGENTS.md`
4. `docs/context/repository_context_index.json`
5. `docs/context/rcc_nexus_index.json`
6. `rcc/nexus/route_map.json`
7. the target folder `README.md`
8. relevant source and tests

After editing, run the validation command associated with the changed surface.

## Patch Routing Matrix

| Change type | Read first | Validate |
|---|---|---|
| Runtime patch | `src/tau_scaling/README.md`, `tests/` | `python -m unittest discover -s tests` |
| Claim classifier patch | `src/tau_scaling/claims/README.md`, latest evidence | `python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json` |
| RCC docs patch | `README.md`, `docs/context/`, `rcc/nexus/` | `python scripts/rcc/check_rcc_nexus.py` |
| Architecture docs patch | `docs/software_architecture/`, `docs/architecture/` | `python scripts/validation/validate_architecture_contracts.py` |
| Release / benchmark patch | `releases/`, `docs/benchmarks/`, `reports/release/` | full validation set |

## Required Validation

```powershell
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
```

---

## Public Non-Claim Locks

- Roadmap coherence is not validation.
- Simulation is not silicon evidence.
- Documentation is not correctness.
- RCC-N navigation is not code correctness.
- Density equivalence is not node equivalence.
- Local path win is not full-chip win.
- Context reconstruction is not correctness proof.
- Evidence packages are task-bounded artifacts, not universal proof.
- Tau Scaling runtime outputs do not independently validate silicon, product metrics, manufacturing capability, benchmark superiority, process-node equivalence, or universal physical law.
- Validation remains required.

Machine-readable lock IDs:

```text
roadmap_coherence_is_not_validation
simulation_is_not_silicon_evidence
documentation_is_not_correctness
navigation_is_not_validation
context_reconstruction_is_not_correctness_proof
density_equivalence_is_not_node_equivalence
local_path_win_is_not_full_chip_win
validation_remains_required
```

---

## Release Lineage

| Version | Meaning |
|---|---|
| v0.1 | Minimal Tau Scaling runtime scaffold. |
| v0.2-RCCN | RCC-N / OMN-style repository structure injection. |
| v0.2.1 | Root cleanup and identity guard. |
| v0.2.2 | Version seal and release manifest layer. |
| v0.2.3 | README / Nexus public polish layer. |
| v0.3 planned | Evidence Promotion Path Layer. |

## Next Recommended Version

**TAU-SCALING-SA v0.3 — Evidence Promotion Path Layer**

Recommended goals:

- Add a second claim-card seed where yield evidence is disclosed.
- Add a missing-gate explainer.
- Add a promotion-requirements report.
- Add a release/checkpoint validator.
- Add a public metrics refresh command.
- Preserve strict downgrade behavior: do not promote claims by weakening gates.
## RCC-N Validator-Visible Lock IDs

- roadmap_coherence_is_not_validation
- simulation_is_not_silicon_validation
- simulation_is_not_silicon_evidence
- documentation_is_not_correctness
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win
- validation_remains_required

Human-readable equivalents:

- Roadmap coherence is not validation.
- Simulation is not silicon validation.
- Simulation is not silicon evidence.
- Documentation is not correctness.
- RCC-N navigation is not code correctness.
- Density equivalence is not node equivalence.
- Local path win is not full-chip win.
- Context reconstruction is not correctness proof.
- Validation remains required.