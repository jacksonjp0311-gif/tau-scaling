# Explanation Card — gamma_tau_etp_tau_gain:tau_gain=0.85

Generated: `2026-05-26T15:02:32.015878+00:00`

| Field | Value |
|---|---|
| Source | `sensitivity_sweep` |
| Classification | `TSEK-C` |
| A_TSEK | `0.0` |
| Diagnostic average | `0.9091` |
| Findings count | `1` |
| Review label | `expected` |

## Why This Class

Downgraded to TSEK-C because one or more required evidence gates are missing while the claim remains interpretable. A_TSEK=0.0, diagnostic_average=0.9091.

## Finding Codes

- `TSEK_B_ETP_MISSING`

## Minimum Repair For Promotion

- Improve energy/thermal/PDN-normalized tau gain above threshold.

## Evidence Path

```text
artifacts/runs/claim-20260526T150222604091Z-693411/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
