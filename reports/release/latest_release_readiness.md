# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:27:03.892041+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `78.772` |
| `import_runtime` | `true` | `0` | `140.31` |
| `rcc_nexus_check` | `true` | `0` | `69.142` |
| `readme_mini_repo_audit` | `true` | `0` | `101.701` |
| `architecture_contract_validation` | `true` | `0` | `68.765` |
| `unit_tests` | `true` | `0` | `222.243` |
| `benchmark_harness` | `true` | `0` | `550.69` |
| `baseline_claim` | `true` | `0` | `176.714` |
| `promotion_path_claim` | `true` | `0` | `153.01` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152703655589Z-d68b2d",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152703655589Z-d68b2d\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T152703655589Z-d68b2d"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152703809601Z-f18313",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152703809601Z-f18313\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T152703809601Z-f18313"
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
      "max_elapsed_ms": 39.6874,
      "mean_elapsed_ms": 36.5193,
      "min_elapsed_ms": 33.045,
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
      "max_elapsed_ms": 36.7084,
      "mean_elapsed_ms": 34.3248,
      "min_elapsed_ms": 32.6577,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:27:03.084507+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.6874,
  "mean_elapsed_ms": 35.422,
  "median_elapsed_ms": 34.9012,
  "min_elapsed_ms": 32.6577,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.2158,
      "evidence_path": "artifacts/runs/claim-20260526T152703084507Z-947a24/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T152703084507Z-947a24",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.4171,
      "evidence_path": "artifacts/runs/claim-20260526T152703123487Z-d49123/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T152703123487Z-d49123",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.3852,
      "evidence_path": "artifacts/runs/claim-20260526T152703159040Z-32895b/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T152703159040Z-32895b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.045,
      "evidence_path": "artifacts/runs/claim-20260526T152703193348Z-e8adbc/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T152703193348Z-e8adbc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.3651,
      "evidence_path": "artifacts/runs/claim-20260526T152703226824Z-0cd311/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T152703226824Z-0cd311",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.6874,
      "evidence_path": "artifacts/runs/claim-20260526T152703264451Z-50ed4a/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T152703264451Z-50ed4a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7084,
      "evidence_path": "artifacts/runs/claim-20260526T152703304699Z-066479/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T152703304699Z-066479",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.568,
      "evidence_path": "artifacts/runs/claim-20260526T152703341719Z-7e4a71/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T152703341719Z-7e4a71",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0129,
      "evidence_path": "artifacts/runs/claim-20260526T152703375884Z-392453/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T152703375884Z-392453",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.6601,
      "evidence_path": "artifacts/runs/claim-20260526T152703409816Z-1a4979/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T152703409816Z-1a4979",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3417,
      "evidence_path": "artifacts/runs/claim-20260526T152703442408Z-1efd87/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T152703442408Z-1efd87",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.6577,
      "evidence_path": "artifacts/runs/claim-20260526T152703479366Z-105b2c/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T152703479366Z-105b2c",
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
