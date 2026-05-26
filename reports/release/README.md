# Release Reports

This folder stores unified release-readiness reports.

Primary command:

```powershell
python scripts/release/validate_release.py
```

Primary outputs:

```text
reports/release/latest_release_readiness.json
reports/release/latest_release_readiness.md
```

The release validator is a repository/runtime readiness gate. It does not validate silicon, products, manufacturing, process-node equivalence, benchmark superiority, or universal Tau Scaling truth.