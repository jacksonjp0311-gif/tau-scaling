# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T17:53:50.427502+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `108.224` |
| `import_runtime` | `true` | `0` | `121.404` |
| `rcc_nexus_check` | `true` | `0` | `99.351` |
| `readme_mini_repo_audit` | `true` | `0` | `168.499` |
| `architecture_contract_validation` | `true` | `0` | `100.73` |
| `unit_tests` | `true` | `0` | `273.834` |
| `benchmark_harness` | `true` | `0` | `561.651` |
| `baseline_claim` | `true` | `0` | `175.634` |
| `promotion_path_claim` | `true` | `0` | `194.68` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175350139128Z-7045f3",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175350139128Z-7045f3\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T175350139128Z-7045f3"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175350335477Z-7a8b54",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175350335477Z-7a8b54\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T175350335477Z-7a8b54"
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
      "max_elapsed_ms": 41.2488,
      "mean_elapsed_ms": 35.927,
      "min_elapsed_ms": 33.8857,
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
      "max_elapsed_ms": 41.6503,
      "mean_elapsed_ms": 36.2721,
      "min_elapsed_ms": 34.9267,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T17:53:49.568338+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 41.6503,
  "mean_elapsed_ms": 36.0996,
  "median_elapsed_ms": 35.0802,
  "min_elapsed_ms": 33.8857,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.2488,
      "evidence_path": "artifacts/runs/claim-20260527T175349569339Z-f19de4/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T175349569339Z-f19de4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.7254,
      "evidence_path": "artifacts/runs/claim-20260527T175349610349Z-8aa96d/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T175349610349Z-8aa96d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6879,
      "evidence_path": "artifacts/runs/claim-20260527T175349646787Z-3bc4d3/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T175349646787Z-3bc4d3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1096,
      "evidence_path": "artifacts/runs/claim-20260527T175349682378Z-0e7259/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T175349682378Z-0e7259",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.8857,
      "evidence_path": "artifacts/runs/claim-20260527T175349717317Z-c57587/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T175349717317Z-c57587",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.9048,
      "evidence_path": "artifacts/runs/claim-20260527T175349751800Z-5f2775/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T175349751800Z-5f2775",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0507,
      "evidence_path": "artifacts/runs/claim-20260527T175349785843Z-d99147/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T175349785843Z-d99147",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9267,
      "evidence_path": "artifacts/runs/claim-20260527T175349821276Z-2a5c04/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T175349821276Z-2a5c04",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 41.6503,
      "evidence_path": "artifacts/runs/claim-20260527T175349855670Z-22b570/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T175349855670Z-22b570",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0158,
      "evidence_path": "artifacts/runs/claim-20260527T175349898349Z-1b135d/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T175349898349Z-1b135d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9753,
      "evidence_path": "artifacts/runs/claim-20260527T175349932653Z-872125/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T175349932653Z-872125",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0138,
      "evidence_path": "artifacts/runs/claim-20260527T175349969133Z-e30b39/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T175349969133Z-e30b39",
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
