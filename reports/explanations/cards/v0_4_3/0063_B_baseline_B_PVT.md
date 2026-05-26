# Explanation Card — B_baseline+B_PVT

Generated: `2026-05-26T15:26:55.378730+00:00`

| Field | Value |
|---|---|
| Source | `gate_interaction_matrix` |
| Classification | `TSEK-C` |
| A_TSEK | `0.0` |
| Diagnostic average | `0.8182` |
| Findings count | `2` |
| Review label | `review_pair_policy` |

## Why This Class

Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK=0.0, diagnostic_average=0.8182.

## Finding Codes

- `TSEK_B_baseline_MISSING`
- `TSEK_B_PVT_MISSING`

## Minimum Repair For Promotion

- Add explicit baseline manifest and baseline tau vector.
- Provide closure, PVT, and PDN evidence.

## Evidence Path

```text
artifacts/runs/claim-20260526T152640485001Z-3f74bd/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
