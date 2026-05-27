# Explanation Card — overclaim_pressure:overclaim=1.0

Generated: `2026-05-27T14:39:56.305006+00:00`

| Field | Value |
|---|---|
| Source | `sensitivity_sweep` |
| Classification | `TSEK-E` |
| A_TSEK | `0.0` |
| Diagnostic average | `1.0` |
| Findings count | `0` |
| Review label | `hard_reject_without_finding` |

## Why This Class

Rejected or severe downgrade to TSEK-E because classifier support collapsed. A_TSEK=0.0, diagnostic_average=1.0.

## Finding Codes

None

## Minimum Repair For Promotion

- No explicit finding codes were emitted; inspect gate values and classifier thresholds.

## Evidence Path

```text
artifacts/runs/claim-20260527T143946707194Z-3b0a69/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
