# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:31:43.130663+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `98.274` |
| `import_runtime` | `true` | `0` | `128.069` |
| `rcc_nexus_check` | `true` | `0` | `76.554` |
| `readme_mini_repo_audit` | `true` | `0` | `97.712` |
| `architecture_contract_validation` | `true` | `0` | `65.444` |
| `unit_tests` | `true` | `0` | `221.699` |
| `benchmark_harness` | `true` | `0` | `564.072` |
| `baseline_claim` | `true` | `0` | `172.593` |
| `promotion_path_claim` | `true` | `0` | `173.911` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T153142870056Z-82eecf",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T153142870056Z-82eecf\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T153142870056Z-82eecf"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T153143044593Z-950121",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T153143044593Z-950121\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T153143044593Z-950121"
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
      "max_elapsed_ms": 38.6788,
      "mean_elapsed_ms": 37.0931,
      "min_elapsed_ms": 34.7355,
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
      "max_elapsed_ms": 40.8301,
      "mean_elapsed_ms": 37.0702,
      "min_elapsed_ms": 35.0318,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:31:42.284525+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.8301,
  "mean_elapsed_ms": 37.0817,
  "median_elapsed_ms": 37.1461,
  "min_elapsed_ms": 34.7355,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6788,
      "evidence_path": "artifacts/runs/claim-20260526T153142285768Z-4f8c23/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T153142285768Z-4f8c23",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7355,
      "evidence_path": "artifacts/runs/claim-20260526T153142324090Z-f13ec9/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T153142324090Z-f13ec9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2672,
      "evidence_path": "artifacts/runs/claim-20260526T153142358765Z-737f40/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T153142358765Z-737f40",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.3559,
      "evidence_path": "artifacts/runs/claim-20260526T153142397870Z-4b962a/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T153142397870Z-4b962a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1429,
      "evidence_path": "artifacts/runs/claim-20260526T153142434551Z-f36104/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T153142434551Z-f36104",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.3785,
      "evidence_path": "artifacts/runs/claim-20260526T153142470458Z-9b7b52/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T153142470458Z-9b7b52",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1414,
      "evidence_path": "artifacts/runs/claim-20260526T153142509117Z-0f84d7/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T153142509117Z-0f84d7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.9363,
      "evidence_path": "artifacts/runs/claim-20260526T153142545318Z-71163e/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T153142545318Z-71163e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.1882,
      "evidence_path": "artifacts/runs/claim-20260526T153142582877Z-e360ac/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T153142582877Z-e360ac",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.8301,
      "evidence_path": "artifacts/runs/claim-20260526T153142620816Z-242993/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T153142620816Z-242993",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.2935,
      "evidence_path": "artifacts/runs/claim-20260526T153142662060Z-545530/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T153142662060Z-545530",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0318,
      "evidence_path": "artifacts/runs/claim-20260526T153142697262Z-553d61/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T153142697262Z-553d61",
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
