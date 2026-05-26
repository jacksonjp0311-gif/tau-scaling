# Tau Scaling: Evidence-Gated Tau-Claim Runtime

## Repository Description

Tau Scaling is a governed Tau Scaling claim-evaluation runtime with TSEK v1.3 source-boundary discipline, claim-card contracts, tau-vector contracts, LogicFolding survivability checks, edge-to-surface boundary algebra, energy/thermal/PDN/PVT gates, Monte Carlo checker stress tests, claim gates, evidence packages, and RCC-N repository navigation.

This repo combines three layers:

1. **Tau Scaling runtime:** claim cards, workload profiles, tau vectors, baseline/candidate comparison, LogicFolding margin, edge/surface ratios, gamma_tau_ETP, Monte Carlo stress, TSEK classification, and evidence package emission.
2. **RCC-N navigation:** Human Director Box, README trisection, repository sphere, route maps, Echo Location records, Nexus context index, and validation-bound AI operating protocol.
3. **Codex documentation shell:** software architecture, source boundary, injection records, validation surfaces, non-claim locks, and folder-level mini READMEs.

Boundary: this description improves discoverability and maintenance discipline. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, independent silicon validation, product performance, process-node equivalence, manufacturing disclosure, or universal Tau Scaling law.

> Tau Scaling is a local-first reference runtime for testing whether a tau-scaling claim can declare a workload, vectorize time, compare baseline/candidate surfaces, pass LogicFolding and energy/thermal/PDN/PVT gates, preserve non-claim locks, and emit audit-ready evidence packages.

Important boundary: this is not a claim to validate Huawei product metrics or independently validate silicon. TSEK remains a Codex extraction and claim-governance framework.

## Human Director Box

### What is this?

Tau Scaling is a governed software workbench for post-Moore tau-scaling claim evaluation. It tests whether a local runtime can transform a public or internal scaling claim into a claim card, tau vector, workload profile, gate record, Monte Carlo stress result, evidence package, and TSEK classification.

### What changed?

This update injects the OMN-style README trisection and RCC-N navigation shell:

- PART I - Human README
- PART II - RCC Nexus README
- PART III - AI Agent README

It also adds folder-level mini READMEs with RCC Nexus Echo Location blocks, a docs/context shell, rcc/nexus route maps, software-architecture documents, injection records, and local validation scripts.

### Current health snapshot

| Surface | Current result |
|---|---:|
| Package / CLI | 	au_scaling |
| Current software layer | TAU-SCALING-SA v0.1.0 |
| Current RCC-N injection | Tau Scaling RCC-N / OMN-style repo structure |
| Latest run id | $LatestRunId |
| Latest TSEK class | $Class |
| Latest A_TSEK | $ATSEK |
| Latest diagnostic average | $DiagAvg |
| Latest findings | $FindingCount |
| Evidence emission | state, evidence, report, visuals, ledger |
| Evidence mirror | outputs/evidence/latest_evidence_package.json |
| Tests | run python -m unittest discover -s tests |
| Claim status | runtime-validated locally only |
| Source boundary | He Tingbo / Huawei public claims separated from independent validation |
| RCC-N profile | Full candidate for this repo because public-claim and evidence surfaces are active |
| GEN boundary | GEN-R repository navigation, not full GEN v1.0 |
| Non-claim lock | simulation is not silicon validation |

### What this is not

- Not independent silicon validation.
- Not proof of Huawei product metrics.
- Not process-node equivalence proof.
- Not semiconductor manufacturing disclosure.
- Not product endorsement.
- Not investment advice.
- Not proof that Tau Scaling is a universal physical law.
- Not proof that RCC-N navigation proves code correctness or patch safety.

### Where do I start?

1. Read this README.
2. Open docs/context/repository_context_index.json.
3. Open docs/context/rcc_nexus_index.json.
4. Open cc/nexus/route_map.json.
5. Run python scripts/rcc/check_rcc_nexus.py.
6. Run python -m unittest discover -s tests.
7. Run python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json.
8. Review outputs/evidence/.

---

# PART I - Human README

## Current Identity

Tau Scaling is a local Python reference runtime for testing whether a tau-scaling claim can:

- declare its source boundary,
- load a claim card,
- declare a workload profile,
- declare a tau vector,
- declare baseline and candidate architectures,
- compute a LogicFolding survivability margin,
- compute edge-to-surface boundary ratios,
- compute gamma_tau_ETP,
- check PVT / closure / PDN / yield disclosures,
- run Monte Carlo checker stress,
- gate claims,
- emit evidence packages and ledgers,
- expose repository context through RCC mini READMEs,
- expose geometric repository navigation through RCC-N.

The current repo is a minimal scaffold and claim-governance runtime, not a production semiconductor validation platform.

## Quick Start

Activate local environment:

    .\.venv\Scripts\Activate.ps1

Run CLI help:

    python -m tau_scaling --help

Run demo claim:

    python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json

Classify latest evidence:

    python -m tau_scaling classify --evidence artifacts/runs/latest/evidence_package.json

Run tests:

    python -m unittest discover -s tests

Run RCC-N checker:

    python scripts/rcc/check_rcc_nexus.py

Run architecture contract validator:

    python scripts/validation/validate_architecture_contracts.py

## What Tau Scaling Tests

| Task | Purpose |
|---|---|
| logicfolding_claim_card | Tests global LogicFolding survivability and evidence downgrade behavior. |
| edge_surface_boundary_toy | Tests edge-bound resource starvation versus surface-coupled scaling. |
| gamma_tau_etp_toy | Tests energy/thermal/PDN-normalized tau gain. |
| monte_carlo_stress_toy | Tests checker sensitivity under synthetic priors. |
| codex_tau_vector_toy | Tests Codex governance latency analogy while preserving physical non-equivalence. |

Tau Scaling rewards bounded evidence emission, not confident overclaiming.

## Project Structure Director

| Surface | What it does | Why it matters |
|---|---|---|
| AGENTS.md | Gives coding agents the entry order, route rules, and validation requirements. | Prevents blind patching. |
| README.md | Provides Human, RCC Nexus, and AI Agent layers. | Makes repo readable by humans and AI agents. |
| README_90_SECONDS.md | Provides adoption compression. | Reduces onboarding friction. |
| configs/ | Stores runtime and seed configuration. | Makes runtime assumptions inspectable. |
| docs/context/ | Stores repository context index, Nexus index, validation surface, and drift reports. | Main repository self-description surface. |
| docs/software_architecture/ | Stores TAU-SCALING-SA software architecture shell. | Keeps theory-to-software direction explicit. |
| docs/injections/ | Stores RCC/RCC-N injection records. | Records governance additions as explicit injections. |
| cc/nexus/ | Stores RCC-N protocol, route maps, task matrix, Echo template, and handoff contract. | Makes the repo agent-navigable. |
| scripts/rcc/ | Stores RCC-N checker and future repair scripts. | Enforces repository-context integrity. |
| src/tau_scaling/ | Stores executable runtime implementation. | Contains Tau Scaling runtime behavior. |
| 	ests/ | Stores implementation-health validation. | Catches local scaffold regressions. |
| rtifacts/ | Stores generated runtime artifacts. | Preserves run-local state, evidence, reports, visuals, and ledgers. |
| outputs/ | Stores OMN-style mirrored generated artifacts. | Gives a stable evidence surface for humans and agents. |
| eports/rcc_nexus/ | Stores RCC-N checker reports. | Makes navigation health inspectable. |
| isuals/tau_scaling/ | Stores classification/dashboard visuals. | Supports public metrics and explanation. |

## Structure Reading Route

For humans:

1. Read the Human Director Box.
2. Read Project Structure Director.
3. Open docs/context/rcc_nexus_index.json.
4. Run python -m unittest discover -s tests.
5. Run python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json.

For AI agents:

1. Read AGENTS.md.
2. Read this README.
3. Read docs/context/repository_context_index.json.
4. Read docs/context/rcc_nexus_index.json.
5. Read cc/nexus/route_map.json.
6. Read the target folder README.
7. Inspect source/tests/evidence before patching.
8. Run declared validation.

Structure boundary: project structure improves navigation. It does not prove correctness, security, patch safety, AI understanding, benchmark validity, independent silicon validation, production readiness, product performance, or source-paper validation.

## Evidence Artifacts

Primary runtime artifacts are written under:

    artifacts/runs/latest/

OMN-style mirrored evidence surfaces are written under:

    outputs/state/
    outputs/evidence/
    outputs/reports/
    outputs/plots/
    outputs/logs/
    outputs/ledger/

RCC-N reports are written under:

    docs/context/drift/
    reports/rcc_nexus/

## Non-Claim Locks

Tau Scaling is:

- not independent silicon validation,
- not proof of Huawei product metrics,
- not process-node equivalence proof,
- not product endorsement,
- not investment advice,
- not semiconductor manufacturing disclosure,
- not proof that simulation equals validation,
- not proof that roadmap coherence equals truth,
- not proof that RCC-N navigation validates code correctness.

---

# PART II - RCC Nexus README

## RCC Nexus Identity

Tau Scaling includes a local RCC Nexus layer with RCC-N v1.7 adoption-profile governance.

RCC tells the agent what the repository means.

RCC-N tells the agent where it is.

Validation tells the agent whether reality agreed.

## Repository Sphere

| Shell | Name | Meaning |
|---|---|---|
| center | Invariant Core | Purpose, source boundary, non-claim locks, evidence boundaries, safety rules. |
| inner | Primitives | Claim cards, tau vectors, runtime objects, gate records, schemas. |
| middle | Processes | CLI flow, examples, tests, scripts, checker workflows, validation commands. |
| outer | Evidence / Reflection | Artifacts, outputs, ledgers, reports, visuals, public summaries, drift reports. |

## Nexus Meridians

- source
- validation
- evidence
- drift
- agent
- safety
- runtime
- tau
- release
- documentation

## Nexus Sectors

- core
- schemas
- tau
- runtime
- validation
- evidence
- rcc
- agent
- examples
- release

## Primary Nexus Files

- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- docs/context/validation_surface.md
- cc/nexus/README.md
- cc/nexus/rcc_nexus_protocol.md
- cc/nexus/route_map.json
- cc/nexus/task_routing_matrix.md
- cc/nexus/echo_location_template.md
- cc/nexus/agent_handoff_contract.md
- scripts/rcc/check_rcc_nexus.py
- eports/rcc_nexus/latest_rcc_nexus_check.md

## RCC Nexus Echo Location

Sphere Position:

- Shell: center
- Meridian(s): source, safety, agent, runtime, evidence
- Sector: rcc
- Version / TTL: RCC-N-v1.7 / 180 days
- Last Verified: 2026-05-26

Local Role:

- Root orientation surface for humans, RCC Nexus navigation, and AI agents.

Inbound Hooks:

- GitHub repository page
- local PowerShell build scripts
- TAU-SCALING-SA software architecture
- TSEK v1.3 extraction kernel

Outbound Hooks:

- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- docs/context/validation_surface.md
- rcc/nexus/route_map.json
- src/tau_scaling/core/runtime.py
- tests/
- artifacts/runs/latest/
- outputs/evidence/

Evidence Surface:

- artifacts/runs/latest/evidence_package.json
- outputs/evidence/latest_evidence_package.json
- outputs/reports/latest_tau_scaling_summary.md
- reports/rcc_nexus/latest_rcc_nexus_check.md

Validation Surface:

- python -m unittest discover -s tests
- python -m tau_scaling --help
- python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
- python scripts/rcc/check_rcc_nexus.py
- python scripts/validation/validate_architecture_contracts.py

Claim Boundary:

- README quality, RCC-N geometry, reports, charts, and NCI do not prove code correctness, security, patch safety, AI understanding, benchmark validity, independent silicon validation, production readiness, product performance, process-node equivalence, or physical truth.

Non-Claim Locks:

- roadmap_coherence_is_not_validation
- simulation_is_not_silicon_validation
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required
- tau_vector_is_not_silicon_measurement
- codex_tau_is_not_physical_equivalence

Agent Route:

- Read README.md, docs/context/repository_context_index.json, docs/context/rcc_nexus_index.json, rcc/nexus/route_map.json, then the target folder README before editing.

Update Obligation:

- Update README, RCC context, Nexus index, route maps, reports, charts, and Echo Location records when project identity, validation commands, evidence paths, claim boundaries, or repository geometry changes.

---

# PART III - AI Agent README

## AI Version Tracking Contract

Current repository context:

- Repository: tau-scaling
- Purpose: governed Tau Scaling claim-evaluation runtime and evidence-emitting workbench.
- Current runtime layer: Tau Scaling runtime scaffold.
- Current software architecture layer: TAU-SCALING-SA v0.1.0.
- Primary package: 	au_scaling.
- Current classification: runtime-validated locally only.
- Current seed: logicfolding_claim_card.
- Latest evidence class: $Class.
- Current non-claim boundary: local scaffold evidence only, not independent silicon validation.
- RCC mode: Repository Context Canon plus mini READMEs.
- RCC-N mode: local geometric repository navigation shell plus RCC-N v1.7 Full profile governance.
- No runtime behavior is changed by RCC or RCC-N documentation.

## AI Operating Contract

Any AI agent reading or modifying this repository must follow this order:

1. Read the Human Director Box.
2. Read PART I - Human README.
3. Read PART II - RCC Nexus README.
4. Read PART III - AI Agent README.
5. Read docs/context/repository_context_index.json.
6. Read docs/context/rcc_nexus_index.json.
7. Read docs/context/validation_surface.md.
8. Read cc/nexus/route_map.json.
9. Read the mini README in the target folder.
10. Inspect only relevant source, tests, docs, configs, scripts, reports, outputs, or visuals.
11. Patch the smallest necessary surface.
12. Run relevant validation commands before claiming behavior changed.
13. Update README, RCC, RCC-N, reports, charts, and Echo Location records if geometry or evidence changed.

## AI README Update Policy

When the repository versions, the AI agent must update the root README in all required zones. Do not update only the top dashboard.

Required root README update zones:

| Zone | Section | Required update |
|---|---|---|
| 1 | Human Director Box / Current health snapshot | Current software layer, latest patch, tests, tag or release reference, metric status. |
| 2 | Current visual/dashboard section | Add or update the current version section and chart. |
| 3 | PART III - AI Agent README / AI Version Tracking Contract | Current software architecture layer and runtime status. |
| 4 | Theory / Software Architecture / Injections Registry | Current file rows and documentation lanes. |
| 5 | Current Versioned Documentation Stack | Active architecture, prior architecture, benchmarks, release notes, reports. |
| 6 | Current Architecture Chain | Append the new version in sequence. |
| 7 | Bottom historical lineage | Add a full section for the completed version, not only a one-line extension. |
| 8 | Validation commands | Update commands if validation surface changed. |
| 9 | Boundary / non-claim locks | Preserve or strengthen boundaries; never weaken them. |

AI update rule:

    Top dashboard without bottom lineage is incomplete.
    Bottom lineage without current health is stale.
    Current version without documentation-stack update is drift.
    README completion requires all three: current state, registry state, historical lineage.

Before claiming README completion, run:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

## AI File Routing Guide

- src/tau_scaling/core: executable runtime orchestration.
- src/tau_scaling/claims: claim cards, classification, downgrade logic.
- src/tau_scaling/tau: tau vectors, workload profiles, gains.
- src/tau_scaling/gates: LogicFolding, edge/surface, gamma_tau_ETP, PVT, evidence gates.
- src/tau_scaling/simulation: Monte Carlo checker stress.
- src/tau_scaling/evidence: package writer and evidence artifacts.
- configs: runtime and seed configuration.
- examples: runnable seed entry points.
- 	ests: implementation-health validation.
- rtifacts/runs/latest: latest runtime evidence package.
- outputs/evidence: OMN-style mirrored evidence surface.
- docs/context: RCC context index, validation surface, Nexus index, and drift reports.
- docs/software_architecture: software architecture shell.
- docs/injections: RCC/RCC-N injection record.
- cc/nexus: RCC-N protocol, route map, task matrix, Echo template, and handoff contract.
- eports/rcc_nexus: RCC-N checker reports.
- isuals/tau_scaling: dashboard and benchmark visualization surface.

## AI Non-Claim Lock

Never claim or imply:

- Tau Scaling runtime independently validates silicon.
- Public roadmap metrics are product truth.
- Density equivalence is process-node equivalence.
- Simulation proves chip behavior.
- Local LogicFolding path wins prove full-chip wins.
- Runtime-validated status proves production readiness.
- RCC documentation proves source correctness.
- RCC-N navigation proves code correctness.
- Evidence packages prove beyond their declared task boundary.
- LLM fluency should be confused with source-grounded implementation accuracy.

## Required Local Verification

After README, RCC, or RCC-N changes, run:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

After source/runtime changes, also run:

    python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json

## Current Versioned Documentation Stack

| Layer | Path | Status |
|---|---|---|
| Software architecture | docs/software_architecture/tau_scaling_sa_v0_1.md | active |
| RCC-N injection | docs/injections/tau_scaling_rcc_n_injection_v0_2.md | active |
| RCC context index | docs/context/repository_context_index.json | active |
| RCC Nexus index | docs/context/rcc_nexus_index.json | active |
| Route map | rcc/nexus/route_map.json | active |
| Latest evidence | artifacts/runs/latest/evidence_package.json | active if demo has run |
| Mirrored evidence | outputs/evidence/latest_evidence_package.json | active if demo has run |

## Current Architecture Chain

    TSEK v1.3
      → TAU-SCALING-SA v0.1
      → Tau Scaling Runtime v0.1.0
      → RCC-N / OMN-style Repository Structure Injection v0.2
      → Evidence Surface Hardening v0.2 candidate

## Bottom Historical Lineage

### v0.1.0 — Minimal Runtime Genesis

Created the first local Tau Scaling package with runnable CLI, claim-card seed, gates, Monte Carlo stress, evidence package, and tests.

### v0.2 — RCC-N / OMN-Style Repository Structure Injection

Adds README trisection, AGENTS.md, README_90_SECONDS.md, docs/context, rcc/nexus, folder mini READMEs, route maps, validation surface, architecture placeholders, injection records, and RCC-N checker.

Boundary: v0.2 improves navigation and evidence readability. It does not loosen the classifier, validate semiconductor claims, or prove code correctness.
---

## Public Non-Claim Locks

These locks are visible in the root README so humans, AI agents, validators, and RCC-N route checks can see the claim boundary before editing or interpreting the repository.

- Roadmap coherence is not validation.
- Simulation is not silicon evidence.
- Documentation is not correctness.
- RCC-N navigation is not code correctness.
- Density equivalence is not node equivalence.
- Local path win is not full-chip win.
- Context reconstruction is not correctness proof.
- Validation remains required.
- Evidence packages are task-bounded artifacts, not universal proof.
- Tau Scaling runtime outputs do not independently validate silicon, product metrics, manufacturing capability, benchmark superiority, or process-node equivalence.
