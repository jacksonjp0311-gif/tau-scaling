# src\tau_scaling\gates

## Folder Purpose

LogicFolding, edge/surface, gamma_tau_ETP, PVT, PDN, yield, and evidence gates.

## S — Specification

This folder participates in the Tau Scaling runtime, documentation, evidence, or RCC-N navigation surface according to its local role.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- artifacts/runs/latest/validation
- validation reports when this folder participates in runtime, documentation, release, or RCC checks

## A — Artifacts

This folder may contain source files, docs, reports, schemas, scripts, visuals, generated state, or validation records depending on its role.

## T — Theory / Basis

Governed by TAU-SCALING-SA v0.1, TSEK v1.3, RCC-N v1.7, and the repository non-claim locks.

## I — Invariants

- Preserve source attribution.
- Preserve non-claim boundaries.
- Do not treat navigation as validation.
- Do not treat documentation as correctness.
- Do not claim independent silicon validation.
- Do not claim product performance validation.
- Keep evidence and validation surfaces inspectable.

## E — Examples

Read this file before editing this folder.

Run relevant validation after changes:

    python -m unittest discover -s tests
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py

## RCC Nexus Echo Location

Sphere Position:

- Shell: inner
- Meridian(s): runtime, validation
- Sector: validation
- Version / TTL: RCC-N-v1.7 / 180 days
- Last Verified: 2026-05-26

Local Role:

- LogicFolding, edge/surface, gamma_tau_ETP, PVT, PDN, yield, and evidence gates.

Evidence Surface:

- artifacts/runs/latest/validation

Validation Surface:

    python -m unittest discover -s tests

Claim Boundary:

- This mini README improves local navigation and agent orientation. It does not prove code correctness, patch safety, empirical validation, independent silicon validation, product performance, process-node equivalence, AI understanding, or production readiness.

Non-Claim Locks:

- navigation_is_not_validation
- documentation_is_not_correctness
- context_reconstruction_is_not_code_quality
- validation_remains_required
- simulation_is_not_silicon_validation
- density_equivalence_is_not_node_equivalence
- local_path_win_is_not_full_chip_win

Agent Route:

- Read root README, docs/context indexes, route map, then this README before editing.

Update Obligation:

- Update this README and RCC/Nexus records if folder purpose, hooks, evidence surfaces, validation commands, or claim boundaries change.