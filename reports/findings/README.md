# Finding Reports

Current layer: **TAU-SCALING-SA v0.4.0c - Benchmark Atlas and Chart Index**

## Purpose

This folder stores finding-level summaries and chart reports.

## Current Surfaces

| Surface | Role |
|---|---|
| `latest_finding_charts.md` | Markdown chart report for finding presence and benchmark charts. |
| `latest_finding_summary.json` | Machine-readable finding count summary. |

## Finding Count Snapshot

```json
{
  "TSEK_B_ETP_MISSING": 2,
  "TSEK_B_LF_MISSING": 2,
  "TSEK_B_PVT_MISSING": 2,
  "TSEK_B_baseline_MISSING": 2,
  "TSEK_B_evidence_MISSING": 2,
  "TSEK_B_method_MISSING": 1,
  "TSEK_B_metric_MISSING": 1,
  "TSEK_B_tau_MISSING": 1,
  "TSEK_B_workload_MISSING": 2,
  "TSEK_B_yield_MISSING": 2,
  "TSEK_OVERCLAIM_INDEPENDENT_VALIDATION": 1
}
```

## Boundary

Findings explain local runtime downgrade behavior only. They are not external validation.
