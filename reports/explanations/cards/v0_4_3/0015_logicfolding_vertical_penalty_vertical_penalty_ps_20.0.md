# Explanation Card — logicfolding_vertical_penalty:vertical_penalty_ps=20.0

Generated: `2026-05-26T15:26:55.366928+00:00`

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

- `TSEK_B_LF_MISSING`

## Minimum Repair For Promotion

- Restore positive LogicFolding survivability margin.

## Evidence Path

```text
artifacts/runs/claim-20260526T152645358233Z-11ee97/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
