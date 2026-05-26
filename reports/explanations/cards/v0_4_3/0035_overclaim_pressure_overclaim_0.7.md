# Explanation Card — overclaim_pressure:overclaim=0.7

Generated: `2026-05-26T15:31:34.577260+00:00`

| Field | Value |
|---|---|
| Source | `sensitivity_sweep` |
| Classification | `TSEK-C` |
| A_TSEK | `0.3` |
| Diagnostic average | `1.0` |
| Findings count | `0` |
| Review label | `expected` |

## Why This Class

Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK=0.3, diagnostic_average=1.0.

## Finding Codes

None

## Minimum Repair For Promotion

- No explicit finding codes were emitted; inspect gate values and classifier thresholds.

## Evidence Path

```text
artifacts/runs/claim-20260526T153125628140Z-788510/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
