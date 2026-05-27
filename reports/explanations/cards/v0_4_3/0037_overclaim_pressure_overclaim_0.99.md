# Explanation Card — overclaim_pressure:overclaim=0.99

Generated: `2026-05-27T14:56:11.505512+00:00`

| Field | Value |
|---|---|
| Source | `sensitivity_sweep` |
| Classification | `TSEK-C` |
| A_TSEK | `0.01` |
| Diagnostic average | `1.0` |
| Findings count | `0` |
| Review label | `expected` |

## Why This Class

Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK=0.01, diagnostic_average=1.0.

## Finding Codes

None

## Minimum Repair For Promotion

- No explicit finding codes were emitted; inspect gate values and classifier thresholds.

## Evidence Path

```text
artifacts/runs/claim-20260527T145600177007Z-8380ea/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
