# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T15:15:13.352653+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `86.531` |
| `import_runtime` | `true` | `0` | `149.897` |
| `rcc_nexus_check` | `true` | `0` | `147.387` |
| `readme_mini_repo_audit` | `true` | `0` | `122.606` |
| `architecture_contract_validation` | `true` | `0` | `91.166` |
| `unit_tests` | `true` | `0` | `251.336` |
| `benchmark_harness` | `true` | `0` | `629.246` |
| `baseline_claim` | `true` | `0` | `209.216` |
| `promotion_path_claim` | `true` | `0` | `206.477` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T151513056105Z-48b552",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T151513056105Z-48b552\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T151513056105Z-48b552"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T151513226617Z-b8dc23",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T151513226617Z-b8dc23\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T151513226617Z-b8dc23"
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
      "max_elapsed_ms": 47.727,
      "mean_elapsed_ms": 41.4964,
      "min_elapsed_ms": 38.6813,
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
      "max_elapsed_ms": 39.6504,
      "mean_elapsed_ms": 39.1343,
      "min_elapsed_ms": 38.7013,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T15:15:12.393166+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.727,
  "mean_elapsed_ms": 40.3154,
  "median_elapsed_ms": 39.3102,
  "min_elapsed_ms": 38.6813,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.727,
      "evidence_path": "artifacts/runs/claim-20260527T151512393166Z-d573fa/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T151512393166Z-d573fa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.7264,
      "evidence_path": "artifacts/runs/claim-20260527T151512440397Z-3ecd09/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T151512440397Z-3ecd09",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.6466,
      "evidence_path": "artifacts/runs/claim-20260527T151512483147Z-7eb971/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T151512483147Z-7eb971",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.1986,
      "evidence_path": "artifacts/runs/claim-20260527T151512524911Z-7b7a0b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T151512524911Z-7b7a0b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.9987,
      "evidence_path": "artifacts/runs/claim-20260527T151512565443Z-345b13/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T151512565443Z-345b13",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6813,
      "evidence_path": "artifacts/runs/claim-20260527T151512604053Z-8beecf/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T151512604053Z-8beecf",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.1925,
      "evidence_path": "artifacts/runs/claim-20260527T151512645097Z-12b8be/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T151512645097Z-12b8be",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9521,
      "evidence_path": "artifacts/runs/claim-20260527T151512684614Z-ff18ff/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T151512684614Z-ff18ff",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.4278,
      "evidence_path": "artifacts/runs/claim-20260527T151512723758Z-c3f75d/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T151512723758Z-c3f75d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.7013,
      "evidence_path": "artifacts/runs/claim-20260527T151512762574Z-8fc11b/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T151512762574Z-8fc11b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8818,
      "evidence_path": "artifacts/runs/claim-20260527T151512801729Z-147abd/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T151512801729Z-147abd",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.6504,
      "evidence_path": "artifacts/runs/claim-20260527T151512841187Z-833a6b/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T151512841187Z-833a6b",
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
