# Explanation Card — pvt_closure_fail_downgrade

Generated: `2026-05-27T14:56:11.495261+00:00`

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

- `TSEK_B_PVT_MISSING`

## Minimum Repair For Promotion

- Provide closure, PVT, and PDN evidence.

## Evidence Path

```text
artifacts/runs/claim-20260527T145604456372Z-f52b3e/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
