# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:26:05.438248+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `84.404` |
| `import_runtime` | `true` | `0` | `145.693` |
| `rcc_nexus_check` | `true` | `0` | `387.655` |
| `readme_mini_repo_audit` | `true` | `0` | `204.506` |
| `architecture_contract_validation` | `true` | `0` | `83.625` |
| `unit_tests` | `true` | `0` | `222.486` |
| `benchmark_harness` | `true` | `0` | `579.659` |
| `baseline_claim` | `true` | `0` | `164.912` |
| `promotion_path_claim` | `true` | `0` | `164.056` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T072605194559Z-b23be5",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T072605194559Z-b23be5\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T072605194559Z-b23be5"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T072605362619Z-af3165",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T072605362619Z-af3165\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T072605362619Z-af3165"
}
```

## Benchmark Summary

```json
{
  "boundary": "Benchmark timing and class stability are local-runtime diagnostics only. They are not silicon validation, product validation, or universal Tau Scaling proof.",
  "by_seed": {
    "configs/seeds/logicfolding_claim_card.json": {
      "A_TSEK_values": [
        0.0
      ],
      "classes": {
        "TSEK-C": 6
      },
      "findings_values": [
        1
      ],
      "max_elapsed_ms": 47.5018,
      "mean_elapsed_ms": 38.0795,
      "min_elapsed_ms": 34.9805,
      "runs": 6
    },
    "configs/seeds/logicfolding_promotion_path_claim_card.json": {
      "A_TSEK_values": [
        1.0
      ],
      "classes": {
        "TSEK-B": 6
      },
      "findings_values": [
        0
      ],
      "max_elapsed_ms": 37.4846,
      "mean_elapsed_ms": 36.2592,
      "min_elapsed_ms": 33.3913,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:26:04.604083+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.5018,
  "mean_elapsed_ms": 37.1694,
  "median_elapsed_ms": 36.2329,
  "min_elapsed_ms": 33.3913,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.5018,
      "evidence_path": "artifacts/runs/claim-20260528T072604604083Z-771c01/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T072604604083Z-771c01",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2625,
      "evidence_path": "artifacts/runs/claim-20260528T072604651993Z-50de60/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T072604651993Z-50de60",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.425,
      "evidence_path": "artifacts/runs/claim-20260528T072604689768Z-b5ef1e/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T072604689768Z-b5ef1e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0495,
      "evidence_path": "artifacts/runs/claim-20260528T072604726186Z-bd1c85/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T072604726186Z-bd1c85",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9805,
      "evidence_path": "artifacts/runs/claim-20260528T072604762474Z-37e1f3/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T072604762474Z-37e1f3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.2579,
      "evidence_path": "artifacts/runs/claim-20260528T072604797370Z-b43f7a/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T072604797370Z-b43f7a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.794,
      "evidence_path": "artifacts/runs/claim-20260528T072604842256Z-8438db/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T072604842256Z-8438db",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.4846,
      "evidence_path": "artifacts/runs/claim-20260528T072604878404Z-efdd6e/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T072604878404Z-efdd6e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2079,
      "evidence_path": "artifacts/runs/claim-20260528T072604916632Z-0dae2b/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T072604916632Z-0dae2b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.3913,
      "evidence_path": "artifacts/runs/claim-20260528T072604952592Z-4e1e12/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T072604952592Z-4e1e12",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3672,
      "evidence_path": "artifacts/runs/claim-20260528T072604986469Z-89ee39/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T072604986469Z-89ee39",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.31,
      "evidence_path": "artifacts/runs/claim-20260528T072605023579Z-230064/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T072605023579Z-230064",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

No findings.

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
