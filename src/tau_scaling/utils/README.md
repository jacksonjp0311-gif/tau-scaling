# utils/

Mini README for RCC/AI context. Preserve non-claim locks and evidence gates.

<!-- MINI_README_UPDATE_RULE_START -->
## AI Update Rule â€” Mini README and Directory Box Synchronization

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
