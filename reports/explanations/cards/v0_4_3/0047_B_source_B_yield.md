# Explanation Card — B_source+B_yield

Generated: `2026-05-27T14:39:56.314511+00:00`

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

- `TSEK_B_source_MISSING`
- `TSEK_B_yield_MISSING`

## Minimum Repair For Promotion

- Declare source boundary and separate reported claims from validation.
- Report yield or downgrade the claim.

## Evidence Path

```text
artifacts/runs/claim-20260527T143938863580Z-29f709/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
