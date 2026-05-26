# tests

## Folder Purpose

Implementation-health tests.

## S Ã¢â‚¬â€ Specification

This folder participates in the Tau Scaling runtime, documentation, evidence, or RCC-N navigation surface according to its local role.

## H Ã¢â‚¬â€ Hooks

Inbound hooks:

- README.md
- AGENTS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- tests
- validation reports when this folder participates in runtime, documentation, release, or RCC checks

## A Ã¢â‚¬â€ Artifacts

This folder may contain source files, docs, reports, schemas, scripts, visuals, generated state, or validation records depending on its role.

## T Ã¢â‚¬â€ Theory / Basis

Governed by TAU-SCALING-SA v0.1, TSEK v1.3, RCC-N v1.7, and the repository non-claim locks.

## I Ã¢â‚¬â€ Invariants

- Preserve source attribution.
- Preserve non-claim boundaries.
- Do not treat navigation as validation.
- Do not treat documentation as correctness.
- Do not claim independent silicon validation.
- Do not claim product performance validation.
- Keep evidence and validation surfaces inspectable.

## E Ã¢â‚¬â€ Examples

Read this file before editing this folder.

Run relevant validation after changes:

    python -m unittest discover -s tests
    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py

## RCC Nexus Echo Location

Sphere Position:

- Shell: middle
- Meridian(s): validation
- Sector: validation
- Version / TTL: RCC-N-v1.7 / 180 days
- Last Verified: 2026-05-26

Local Role:

- Implementation-health tests.

Evidence Surface:

- tests

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

<!-- MINI_README_UPDATE_RULE_START -->
## AI Update Rule ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mini README and Directory Box Synchronization

This folder is part of the RCC-N navigable repository surface.

When this folder's purpose, files, routes, evidence surfaces, validation commands, or claim boundaries change, update this mini README in the same commit. Also update the root README Full Directory Box if any folder is added, removed, renamed, or repurposed.

Required after changes:

`powershell
python scripts/rcc/check_rcc_nexus.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
`

Non-claim lock: navigation is not validation, but stale navigation is repository drift.
<!-- MINI_README_UPDATE_RULE_END -->


## AI Failure Learning Note

If a patch touching this folder fails validation, record the reusable lesson in the root README `AI Failure Learning Ledger` and update this mini README when the local rule changes.

Minimum repair discipline:

```powershell
python -m py_compile src/tau_scaling/core/runtime.py
python -c "from tau_scaling.core.runtime import TauScalingRuntime; print('TauScalingRuntime import OK')"
python -m unittest discover -s tests
python scripts/benchmarks/run_tau_scaling_benchmarks.py
```

Boundary: passing local runtime checks improves repository confidence but does not validate silicon, product performance, manufacturing capability, process-node equivalence, or a universal Tau Scaling law.

## README / Mini Repo Audit Rule

This folder participates in the repository-wide README + mini repo audit.

When this folder changes, an AI or human maintainer must check:

- root README.md
- this folder README.md
- nearest parent folder README.md
- docs/context/repository_context_index.json if route meaning changes
- docs/context/rcc_nexus_index.json if Nexus position changes
- cc/nexus/route_map.json if task routing changes

Audit command:

`powershell
python scripts/rcc/audit_readme_surface.py
`

Non-claim lock: README audit alignment is not runtime correctness or silicon validation.