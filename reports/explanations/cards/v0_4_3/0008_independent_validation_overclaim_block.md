# Explanation Card — independent_validation_overclaim_block

Generated: `2026-05-26T15:31:34.566767+00:00`

| Field | Value |
|---|---|
| Source | `synthetic_gate_suite` |
| Classification | `TSEK-E` |
| A_TSEK | `0.0` |
| Diagnostic average | `1.0` |
| Findings count | `1` |
| Review label | `expected` |

## Why This Class

Rejected to TSEK-E because an independent-validation claim was made without corresponding independent-validation evidence.

## Finding Codes

- `TSEK_OVERCLAIM_INDEPENDENT_VALIDATION`

## Minimum Repair For Promotion

- Remove independent-validation claim or provide independent validation evidence.

## Evidence Path

```text
artifacts/runs/claim-20260526T153129169957Z-5b0a94/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
