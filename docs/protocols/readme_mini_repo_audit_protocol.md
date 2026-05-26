# README + Mini Repo Audit Protocol

Generated: 2026-05-26T10:08:12Z
Version: TAU-SCALING-SA v0.3.2d

## Purpose

This protocol tells human maintainers and AI agents where to scan for repository gaps before claiming a patch is complete.

A patch is incomplete if it changes repository structure, runtime behavior, benchmarks, reports, claim seeds, release state, or documentation meaning without updating the relevant root README, mini README, route map, context index, validation report, or release note.

## Required Scan Order

1. README.md
2. AGENTS.md
3. README_90_SECONDS.md
4. docs/context/repository_context_index.json
5. docs/context/rcc_nexus_index.json
6. cc/nexus/route_map.json
7. cc/nexus/task_routing_matrix.md
8. Target folder README.md
9. Sibling folder README.md files if routing changed
10. Relevant tests, reports, benchmark outputs, and release notes

## Gap Classes

| Gap class | Meaning | Required repair |
|---|---|---|
| README drift | Root README claims do not match current repo state. | Patch README metrics, lineage, commands, and directory box. |
| Mini README drift | Folder README does not explain current folder role. | Patch the affected folder README. |
| Route drift | RCC-N route map/context index is stale. | Patch context JSON and route matrix. |
| Validation drift | README says passing, but latest reports are missing/stale. | Rerun validators and refresh reports. |
| Runtime drift | Code changed without compile/import/test evidence. | Run compile, import, unit tests, claims, and benchmarks if relevant. |
| Benchmark drift | Benchmarks changed without report updates. | Rerun benchmark harness and refresh benchmark report. |
| Evidence drift | Runtime output overwrites or lacks unique identity. | Verify collision-proof run IDs and latest evidence package. |
| Claim drift | Documentation implies stronger validation than evidence supports. | Restore non-claim locks and downgrade wording. |

## Required Audit Command

`powershell
python scripts/rcc/audit_readme_surface.py
`

## Full Validation After README/Repo-Audit Changes

`powershell
python -m py_compile src/tau_scaling/core/runtime.py
python -c "from tau_scaling.core.runtime import TauScalingRuntime; print('TauScalingRuntime import OK')"
python scripts/rcc/check_rcc_nexus.py
python scripts/rcc/audit_readme_surface.py
python scripts/validation/validate_architecture_contracts.py
python -m unittest discover -s tests
python scripts/benchmarks/run_tau_scaling_benchmarks.py
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_claim_card.json
python -m tau_scaling run-claim --seed configs/seeds/logicfolding_promotion_path_claim_card.json
`

## Non-Claim Lock

A README audit proves context alignment, not runtime correctness, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling law.