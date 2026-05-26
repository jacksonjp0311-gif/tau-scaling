# Architecture Reports

This folder stores latest architecture-contract validation outputs and architecture health reports.

## README / Mini Repo Audit Rule

This folder participates in the repository-wide README + mini repo audit.

When this folder changes, an AI or human maintainer must check:

- root `README.md`
- this folder `README.md`
- nearest parent folder `README.md`
- `docs/context/repository_context_index.json` if route meaning changes
- `docs/context/rcc_nexus_index.json` if Nexus position changes
- `rcc/nexus/route_map.json` if task routing changes

Audit command:

```powershell
python scripts/rcc/audit_readme_surface.py
```

Non-claim lock: README audit alignment is not runtime correctness or silicon validation.
