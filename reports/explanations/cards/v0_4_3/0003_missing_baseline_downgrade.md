# Explanation Card — missing_baseline_downgrade

Generated: `2026-05-26T15:06:53.036502+00:00`

| Field | Value |
|---|---|
| Source | `synthetic_gate_suite` |
| Classification | `TSEK-C` |
| A_TSEK | `0.0` |
| Diagnostic average | `0.9091` |
| Findings count | `1` |
| Review label | `expected` |

## Why This Class

Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK=0.0, diagnostic_average=0.9091.

## Finding Codes

- `TSEK_B_baseline_MISSING`

## Minimum Repair For Promotion

- Add explicit baseline manifest and baseline tau vector.

## Evidence Path

```text
artifacts/runs/claim-20260526T150647323141Z-76d48a/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
