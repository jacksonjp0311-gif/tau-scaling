# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T10:47:14.586953+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.281` |
| `import_runtime` | `true` | `0` | `122.489` |
| `rcc_nexus_check` | `true` | `0` | `97.612` |
| `readme_mini_repo_audit` | `true` | `0` | `93.768` |
| `architecture_contract_validation` | `true` | `0` | `68.093` |
| `unit_tests` | `true` | `0` | `244.826` |
| `benchmark_harness` | `true` | `0` | `537.697` |
| `baseline_claim` | `true` | `0` | `158.954` |
| `promotion_path_claim` | `true` | `0` | `156.523` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104714345645Z-296c3c",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104714345645Z-296c3c\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T104714345645Z-296c3c"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104714504469Z-0f2acf",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104714504469Z-0f2acf\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T104714504469Z-0f2acf"
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
      "max_elapsed_ms": 38.056,
      "mean_elapsed_ms": 35.9218,
      "min_elapsed_ms": 34.7217,
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
      "max_elapsed_ms": 36.703,
      "mean_elapsed_ms": 33.97,
      "min_elapsed_ms": 32.5074,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T10:47:13.800067+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 38.056,
  "mean_elapsed_ms": 34.9459,
  "median_elapsed_ms": 34.8341,
  "min_elapsed_ms": 32.5074,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.056,
      "evidence_path": "artifacts/runs/claim-20260528T104713800067Z-981618/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T104713800067Z-981618",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8007,
      "evidence_path": "artifacts/runs/claim-20260528T104713838739Z-d13daa/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T104713838739Z-d13daa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9465,
      "evidence_path": "artifacts/runs/claim-20260528T104713875126Z-a700d9/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T104713875126Z-a700d9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.3627,
      "evidence_path": "artifacts/runs/claim-20260528T104713910847Z-d6d82c/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T104713910847Z-d6d82c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7217,
      "evidence_path": "artifacts/runs/claim-20260528T104713946326Z-acf534/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T104713946326Z-acf534",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6435,
      "evidence_path": "artifacts/runs/claim-20260528T104713980690Z-27919d/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T104713980690Z-27919d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3895,
      "evidence_path": "artifacts/runs/claim-20260528T104714016695Z-de0df3/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T104714016695Z-de0df3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6318,
      "evidence_path": "artifacts/runs/claim-20260528T104714051105Z-1c973f/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T104714051105Z-1c973f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.5074,
      "evidence_path": "artifacts/runs/claim-20260528T104714086722Z-32e79d/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T104714086722Z-32e79d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.8908,
      "evidence_path": "artifacts/runs/claim-20260528T104714119419Z-1dc5c1/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T104714119419Z-1dc5c1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.703,
      "evidence_path": "artifacts/runs/claim-20260528T104714151570Z-3b0a55/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T104714151570Z-3b0a55",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.6973,
      "evidence_path": "artifacts/runs/claim-20260528T104714189143Z-ccc626/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T104714189143Z-ccc626",
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
