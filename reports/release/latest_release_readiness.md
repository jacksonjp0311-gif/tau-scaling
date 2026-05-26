# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T14:38:55.306420+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `78.548` |
| `import_runtime` | `true` | `0` | `116.052` |
| `rcc_nexus_check` | `true` | `0` | `94.821` |
| `readme_mini_repo_audit` | `true` | `0` | `90.052` |
| `architecture_contract_validation` | `true` | `0` | `64.826` |
| `unit_tests` | `true` | `0` | `220.135` |
| `benchmark_harness` | `true` | `0` | `586.959` |
| `baseline_claim` | `true` | `0` | `181.118` |
| `promotion_path_claim` | `true` | `0` | `179.059` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T143855037275Z-c49054",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T143855037275Z-c49054\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T143855037275Z-c49054"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T143855220413Z-44a95c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T143855220413Z-44a95c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T143855220413Z-44a95c"
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
      "max_elapsed_ms": 42.9671,
      "mean_elapsed_ms": 38.672,
      "min_elapsed_ms": 37.1294,
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
      "max_elapsed_ms": 42.951,
      "mean_elapsed_ms": 38.0722,
      "min_elapsed_ms": 36.0175,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T14:38:54.432582+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.9671,
  "mean_elapsed_ms": 38.3721,
  "median_elapsed_ms": 37.7899,
  "min_elapsed_ms": 36.0175,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.9671,
      "evidence_path": "artifacts/runs/claim-20260526T143854432582Z-4b2369/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T143854432582Z-4b2369",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6284,
      "evidence_path": "artifacts/runs/claim-20260526T143854475450Z-f40b8e/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T143854475450Z-f40b8e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.7099,
      "evidence_path": "artifacts/runs/claim-20260526T143854515135Z-3e8209/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T143854515135Z-3e8209",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.1294,
      "evidence_path": "artifacts/runs/claim-20260526T143854553138Z-b2845f/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T143854553138Z-b2845f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.5278,
      "evidence_path": "artifacts/runs/claim-20260526T143854590173Z-643399/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T143854590173Z-643399",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.0692,
      "evidence_path": "artifacts/runs/claim-20260526T143854627664Z-bffff9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T143854627664Z-bffff9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.4192,
      "evidence_path": "artifacts/runs/claim-20260526T143854666854Z-347d77/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T143854666854Z-347d77",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1175,
      "evidence_path": "artifacts/runs/claim-20260526T143854703051Z-d18b1b/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T143854703051Z-d18b1b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.951,
      "evidence_path": "artifacts/runs/claim-20260526T143854739282Z-822286/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T143854739282Z-822286",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0175,
      "evidence_path": "artifacts/runs/claim-20260526T143854782699Z-f01786/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T143854782699Z-f01786",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0579,
      "evidence_path": "artifacts/runs/claim-20260526T143854818214Z-ac1eff/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T143854818214Z-ac1eff",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.87,
      "evidence_path": "artifacts/runs/claim-20260526T143854858045Z-74f683/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T143854858045Z-74f683",
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
