# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T13:39:30.993658+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.262` |
| `import_runtime` | `true` | `0` | `110.555` |
| `rcc_nexus_check` | `true` | `0` | `82.402` |
| `readme_mini_repo_audit` | `true` | `0` | `92.742` |
| `architecture_contract_validation` | `true` | `0` | `84.969` |
| `unit_tests` | `true` | `0` | `223.586` |
| `benchmark_harness` | `true` | `0` | `570.351` |
| `baseline_claim` | `true` | `0` | `169.594` |
| `promotion_path_claim` | `true` | `0` | `163.095` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T133930747710Z-055e69",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T133930747710Z-055e69\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T133930747710Z-055e69"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T133930915835Z-c57181",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T133930915835Z-c57181\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T133930915835Z-c57181"
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
      "max_elapsed_ms": 40.8511,
      "mean_elapsed_ms": 37.4374,
      "min_elapsed_ms": 35.8745,
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
      "max_elapsed_ms": 38.2626,
      "mean_elapsed_ms": 36.3043,
      "min_elapsed_ms": 35.0749,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T13:39:30.168801+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.8511,
  "mean_elapsed_ms": 36.8709,
  "median_elapsed_ms": 36.4553,
  "min_elapsed_ms": 35.0749,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.8511,
      "evidence_path": "artifacts/runs/claim-20260528T133930168801Z-97eb73/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T133930168801Z-97eb73",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.0594,
      "evidence_path": "artifacts/runs/claim-20260528T133930209526Z-7c0e11/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T133930209526Z-7c0e11",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.692,
      "evidence_path": "artifacts/runs/claim-20260528T133930248344Z-3d8001/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T133930248344Z-3d8001",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.749,
      "evidence_path": "artifacts/runs/claim-20260528T133930284784Z-bb23b6/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T133930284784Z-bb23b6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3984,
      "evidence_path": "artifacts/runs/claim-20260528T133930322042Z-d93136/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T133930322042Z-d93136",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.8745,
      "evidence_path": "artifacts/runs/claim-20260528T133930358757Z-01565d/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T133930358757Z-01565d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.749,
      "evidence_path": "artifacts/runs/claim-20260528T133930394600Z-0cbb26/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T133930394600Z-0cbb26",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3124,
      "evidence_path": "artifacts/runs/claim-20260528T133930430346Z-bd9537/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T133930430346Z-bd9537",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.2626,
      "evidence_path": "artifacts/runs/claim-20260528T133930466769Z-54ef65/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T133930466769Z-54ef65",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.5122,
      "evidence_path": "artifacts/runs/claim-20260528T133930505170Z-89899a/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T133930505170Z-89899a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9149,
      "evidence_path": "artifacts/runs/claim-20260528T133930542519Z-fb73b7/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T133930542519Z-fb73b7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0749,
      "evidence_path": "artifacts/runs/claim-20260528T133930577930Z-e91375/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T133930577930Z-e91375",
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
