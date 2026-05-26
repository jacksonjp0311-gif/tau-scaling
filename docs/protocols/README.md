# docs/protocols/

Operational protocols, non-claim locks, claim cards, tau vectors, and evidence gates.

<!-- MINI_README_UPDATE_RULE_START -->
## AI Update Rule Ã¢â‚¬â€ Mini README and Directory Box Synchronization

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