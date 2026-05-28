# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T14:24:45.050339+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.316` |
| `import_runtime` | `true` | `0` | `114.095` |
| `rcc_nexus_check` | `true` | `0` | `92.022` |
| `readme_mini_repo_audit` | `true` | `0` | `92.425` |
| `architecture_contract_validation` | `true` | `0` | `66.225` |
| `unit_tests` | `true` | `0` | `214.27` |
| `benchmark_harness` | `true` | `0` | `561.285` |
| `baseline_claim` | `true` | `0` | `170.052` |
| `promotion_path_claim` | `true` | `0` | `185.564` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142444778833Z-bf30d5",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142444778833Z-bf30d5\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T142444778833Z-bf30d5"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142444950969Z-79683c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T142444950969Z-79683c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T142444950969Z-79683c"
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
      "max_elapsed_ms": 39.6829,
      "mean_elapsed_ms": 36.3743,
      "min_elapsed_ms": 33.9367,
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
      "max_elapsed_ms": 39.3372,
      "mean_elapsed_ms": 36.7208,
      "min_elapsed_ms": 35.303,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T14:24:44.204672+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.6829,
  "mean_elapsed_ms": 36.5476,
  "median_elapsed_ms": 36.4368,
  "min_elapsed_ms": 33.9367,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.6829,
      "evidence_path": "artifacts/runs/claim-20260528T142444204672Z-45a144/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T142444204672Z-45a144",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.9367,
      "evidence_path": "artifacts/runs/claim-20260528T142444244259Z-8924d8/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T142444244259Z-8924d8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.1819,
      "evidence_path": "artifacts/runs/claim-20260528T142444278770Z-6bad88/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T142444278770Z-6bad88",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.5631,
      "evidence_path": "artifacts/runs/claim-20260528T142444315884Z-ca14e8/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T142444315884Z-ca14e8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.2901,
      "evidence_path": "artifacts/runs/claim-20260528T142444350752Z-55be9a/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T142444350752Z-55be9a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.591,
      "evidence_path": "artifacts/runs/claim-20260528T142444387234Z-09b039/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T142444387234Z-09b039",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.4747,
      "evidence_path": "artifacts/runs/claim-20260528T142444423954Z-24d840/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T142444423954Z-24d840",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.303,
      "evidence_path": "artifacts/runs/claim-20260528T142444462237Z-ef0449/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T142444462237Z-ef0449",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.3367,
      "evidence_path": "artifacts/runs/claim-20260528T142444497065Z-dbea32/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T142444497065Z-dbea32",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.4445,
      "evidence_path": "artifacts/runs/claim-20260528T142444533368Z-cf5a08/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T142444533368Z-cf5a08",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.3372,
      "evidence_path": "artifacts/runs/claim-20260528T142444569854Z-514cbb/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T142444569854Z-514cbb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.429,
      "evidence_path": "artifacts/runs/claim-20260528T142444608803Z-336709/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T142444608803Z-336709",
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
