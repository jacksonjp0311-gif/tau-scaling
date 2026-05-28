# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T16:17:20.448754+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `93.667` |
| `import_runtime` | `true` | `0` | `152.33` |
| `rcc_nexus_check` | `true` | `0` | `109.739` |
| `readme_mini_repo_audit` | `true` | `0` | `113.173` |
| `architecture_contract_validation` | `true` | `0` | `79.203` |
| `unit_tests` | `true` | `0` | `286.657` |
| `benchmark_harness` | `true` | `0` | `736.733` |
| `baseline_claim` | `true` | `0` | `222.371` |
| `promotion_path_claim` | `true` | `0` | `218.75` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T161720122578Z-f4c634",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T161720122578Z-f4c634\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T161720122578Z-f4c634"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T161720339699Z-995f15",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T161720339699Z-995f15\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T161720339699Z-995f15"
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
      "max_elapsed_ms": 55.5687,
      "mean_elapsed_ms": 46.8731,
      "min_elapsed_ms": 42.4103,
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
      "max_elapsed_ms": 67.5655,
      "mean_elapsed_ms": 49.0009,
      "min_elapsed_ms": 42.8539,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T16:17:19.362735+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 67.5655,
  "mean_elapsed_ms": 47.937,
  "median_elapsed_ms": 45.83,
  "min_elapsed_ms": 42.4103,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 55.5687,
      "evidence_path": "artifacts/runs/claim-20260528T161719363734Z-02dea7/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T161719363734Z-02dea7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.4103,
      "evidence_path": "artifacts/runs/claim-20260528T161719419458Z-5f9768/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T161719419458Z-5f9768",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.5877,
      "evidence_path": "artifacts/runs/claim-20260528T161719461151Z-4ab530/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T161719461151Z-4ab530",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.6189,
      "evidence_path": "artifacts/runs/claim-20260528T161719507838Z-820e42/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T161719507838Z-820e42",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.0724,
      "evidence_path": "artifacts/runs/claim-20260528T161719555107Z-3e765c/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T161719555107Z-3e765c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.9807,
      "evidence_path": "artifacts/runs/claim-20260528T161719601442Z-01d488/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T161719601442Z-01d488",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.7738,
      "evidence_path": "artifacts/runs/claim-20260528T161719645697Z-ddd22c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T161719645697Z-ddd22c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.5287,
      "evidence_path": "artifacts/runs/claim-20260528T161719691019Z-bb3777/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T161719691019Z-bb3777",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.8539,
      "evidence_path": "artifacts/runs/claim-20260528T161719735698Z-e83e62/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T161719735698Z-e83e62",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.9918,
      "evidence_path": "artifacts/runs/claim-20260528T161719778989Z-1a5d3c/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T161719778989Z-1a5d3c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 67.5655,
      "evidence_path": "artifacts/runs/claim-20260528T161719826230Z-05d2b5/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T161719826230Z-05d2b5",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 47.2915,
      "evidence_path": "artifacts/runs/claim-20260528T161719892892Z-b1fbd9/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T161719892892Z-b1fbd9",
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
