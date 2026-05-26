# Release Scripts

This folder stores release-readiness and release-packaging scripts.

Primary script:

```text
validate_release.py
```

It runs compile, import, RCC-N, README audit, architecture validation, unit tests, benchmark harness, baseline claim, and promotion-path claim.

Non-claim lock: release readiness is repository/runtime hygiene evidence only.