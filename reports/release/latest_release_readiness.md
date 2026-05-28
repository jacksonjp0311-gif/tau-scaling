# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:37:37.756545+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `163.46` |
| `import_runtime` | `true` | `0` | `141.754` |
| `rcc_nexus_check` | `true` | `0` | `89.293` |
| `readme_mini_repo_audit` | `true` | `0` | `89.658` |
| `architecture_contract_validation` | `true` | `0` | `75.067` |
| `unit_tests` | `true` | `0` | `212.007` |
| `benchmark_harness` | `true` | `0` | `528.699` |
| `baseline_claim` | `true` | `0` | `157.879` |
| `promotion_path_claim` | `true` | `0` | `147.603` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073737529675Z-a46752",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073737529675Z-a46752\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T073737529675Z-a46752"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073737680228Z-8e97f6",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073737680228Z-8e97f6\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T073737680228Z-8e97f6"
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
      "max_elapsed_ms": 39.3132,
      "mean_elapsed_ms": 35.9301,
      "min_elapsed_ms": 34.735,
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
      "max_elapsed_ms": 34.9098,
      "mean_elapsed_ms": 34.1282,
      "min_elapsed_ms": 32.9858,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:37:36.982275+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.3132,
  "mean_elapsed_ms": 35.0292,
  "median_elapsed_ms": 34.8224,
  "min_elapsed_ms": 32.9858,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.3132,
      "evidence_path": "artifacts/runs/claim-20260528T073736982275Z-02fd90/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T073736982275Z-02fd90",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.016,
      "evidence_path": "artifacts/runs/claim-20260528T073737021472Z-5f86a5/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T073737021472Z-5f86a5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9889,
      "evidence_path": "artifacts/runs/claim-20260528T073737057252Z-54ee5c/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T073737057252Z-54ee5c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1574,
      "evidence_path": "artifacts/runs/claim-20260528T073737092974Z-380b46/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T073737092974Z-380b46",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.3704,
      "evidence_path": "artifacts/runs/claim-20260528T073737127919Z-6ecc3f/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T073737127919Z-6ecc3f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.735,
      "evidence_path": "artifacts/runs/claim-20260528T073737163847Z-557518/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T073737163847Z-557518",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.1895,
      "evidence_path": "artifacts/runs/claim-20260528T073737198978Z-143a8b/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T073737198978Z-143a8b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9098,
      "evidence_path": "artifacts/runs/claim-20260528T073737233200Z-9411da/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T073737233200Z-9411da",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6508,
      "evidence_path": "artifacts/runs/claim-20260528T073737268231Z-0ca4fa/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T073737268231Z-0ca4fa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3276,
      "evidence_path": "artifacts/runs/claim-20260528T073737303590Z-c55568/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T073737303590Z-c55568",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7057,
      "evidence_path": "artifacts/runs/claim-20260528T073737337913Z-768ec2/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T073737337913Z-768ec2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.9858,
      "evidence_path": "artifacts/runs/claim-20260528T073737371134Z-5dc466/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T073737371134Z-5dc466",
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
