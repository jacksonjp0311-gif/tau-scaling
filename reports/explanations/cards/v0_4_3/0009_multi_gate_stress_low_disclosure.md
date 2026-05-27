# Explanation Card — multi_gate_stress_low_disclosure

Generated: `2026-05-27T14:39:56.295004+00:00`

| Field | Value |
|---|---|
| Source | `synthetic_gate_suite` |
| Classification | `TSEK-E` |
| A_TSEK | `0.0` |
| Diagnostic average | `0.0909` |
| Findings count | `10` |
| Review label | `expected` |

## Why This Class

Rejected or severe downgrade to TSEK-E because classifier support collapsed. A_TSEK=0.0, diagnostic_average=0.0909.

## Finding Codes

- `TSEK_B_metric_MISSING`
- `TSEK_B_baseline_MISSING`
- `TSEK_B_method_MISSING`
- `TSEK_B_workload_MISSING`
- `TSEK_B_tau_MISSING`
- `TSEK_B_LF_MISSING`
- `TSEK_B_ETP_MISSING`
- `TSEK_B_PVT_MISSING`
- `TSEK_B_yield_MISSING`
- `TSEK_B_evidence_MISSING`

## Minimum Repair For Promotion

- Add a measurable claim text/type and metric definition.
- Add explicit baseline manifest and baseline tau vector.
- Disclose method and yield methodology.
- Declare workload class and dominant tau term.
- Declare tau weights and dominant tau improvement.
- Restore positive LogicFolding survivability margin.
- Improve energy/thermal/PDN-normalized tau gain above threshold.
- Provide closure, PVT, and PDN evidence.
- Report yield or downgrade the claim.
- Complete the evidence package.

## Evidence Path

```text
artifacts/runs/claim-20260527T143950496692Z-40123f/evidence_package.json
```

## Boundary

Explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
