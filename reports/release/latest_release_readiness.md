# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T14:09:11.488186+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.206` |
| `import_runtime` | `true` | `0` | `123.783` |
| `rcc_nexus_check` | `true` | `0` | `87.289` |
| `readme_mini_repo_audit` | `true` | `0` | `95.173` |
| `architecture_contract_validation` | `true` | `0` | `64.576` |
| `unit_tests` | `true` | `0` | `224.707` |
| `benchmark_harness` | `true` | `0` | `578.86` |
| `baseline_claim` | `true` | `0` | `165.144` |
| `promotion_path_claim` | `true` | `0` | `164.258` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T140911239012Z-f5db66",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T140911239012Z-f5db66\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T140911239012Z-f5db66"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T140911403933Z-ea03e7",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T140911403933Z-ea03e7\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T140911403933Z-ea03e7"
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
      "max_elapsed_ms": 46.1683,
      "mean_elapsed_ms": 38.18,
      "min_elapsed_ms": 34.086,
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
      "max_elapsed_ms": 39.4106,
      "mean_elapsed_ms": 37.1042,
      "min_elapsed_ms": 35.8012,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T14:09:10.654404+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 46.1683,
  "mean_elapsed_ms": 37.6421,
  "median_elapsed_ms": 36.4614,
  "min_elapsed_ms": 34.086,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.8196,
      "evidence_path": "artifacts/runs/claim-20260528T140910654404Z-0a5019/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T140910654404Z-0a5019",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.1683,
      "evidence_path": "artifacts/runs/claim-20260528T140910695873Z-df5462/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T140910695873Z-df5462",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.0779,
      "evidence_path": "artifacts/runs/claim-20260528T140910741651Z-f67ebe/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T140910741651Z-f67ebe",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1884,
      "evidence_path": "artifacts/runs/claim-20260528T140910780376Z-daf69d/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T140910780376Z-daf69d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.086,
      "evidence_path": "artifacts/runs/claim-20260528T140910815836Z-714a4e/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T140910815836Z-714a4e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7399,
      "evidence_path": "artifacts/runs/claim-20260528T140910850107Z-86f129/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T140910850107Z-86f129",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8012,
      "evidence_path": "artifacts/runs/claim-20260528T140910885121Z-e07a18/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T140910885121Z-e07a18",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2551,
      "evidence_path": "artifacts/runs/claim-20260528T140910920487Z-6041af/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T140910920487Z-6041af",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.6603,
      "evidence_path": "artifacts/runs/claim-20260528T140910957247Z-90d699/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T140910957247Z-90d699",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.4106,
      "evidence_path": "artifacts/runs/claim-20260528T140910995832Z-2acabe/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T140910995832Z-2acabe",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.6677,
      "evidence_path": "artifacts/runs/claim-20260528T140911035745Z-87a44d/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T140911035745Z-87a44d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.83,
      "evidence_path": "artifacts/runs/claim-20260528T140911072794Z-1ebec1/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T140911072794Z-1ebec1",
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
