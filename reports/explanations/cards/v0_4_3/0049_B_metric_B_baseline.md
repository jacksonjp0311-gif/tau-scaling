# Explanation Card — B_metric+B_baseline

Generated: `2026-05-27T14:56:11.516616+00:00`

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

- `TSEK_B_metric_MISSING`
- `TSEK_B_baseline_MISSING`

## Minimum Repair For Promotion

- Add a measurable claim text/type and metric definition.
- Add explicit baseline manifest and baseline tau vector.

## Evidence Path

```text
artifacts/runs/claim-20260527T145551916199Z-e32dc3/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
