# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:06:58.196297+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `83.644` |
| `import_runtime` | `true` | `0` | `124.12` |
| `rcc_nexus_check` | `true` | `0` | `104.415` |
| `readme_mini_repo_audit` | `true` | `0` | `102.637` |
| `architecture_contract_validation` | `true` | `0` | `66.938` |
| `unit_tests` | `true` | `0` | `224.327` |
| `benchmark_harness` | `true` | `0` | `543.759` |
| `baseline_claim` | `true` | `0` | `167.73` |
| `promotion_path_claim` | `true` | `0` | `162.72` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150657951010Z-68c659",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150657951010Z-68c659\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T150657951010Z-68c659"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150658114477Z-4e4957",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T150658114477Z-4e4957\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T150658114477Z-4e4957"
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
      "max_elapsed_ms": 39.3954,
      "mean_elapsed_ms": 35.5722,
      "min_elapsed_ms": 33.5137,
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
      "max_elapsed_ms": 36.8457,
      "mean_elapsed_ms": 34.9206,
      "min_elapsed_ms": 33.5029,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:06:57.393929+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.3954,
  "mean_elapsed_ms": 35.2464,
  "median_elapsed_ms": 34.8199,
  "min_elapsed_ms": 33.5029,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.3954,
      "evidence_path": "artifacts/runs/claim-20260526T150657393929Z-d0a5f0/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T150657393929Z-d0a5f0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.2371,
      "evidence_path": "artifacts/runs/claim-20260526T150657433406Z-edcce1/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T150657433406Z-edcce1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6125,
      "evidence_path": "artifacts/runs/claim-20260526T150657471087Z-f49de4/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T150657471087Z-f49de4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.5885,
      "evidence_path": "artifacts/runs/claim-20260526T150657506755Z-ed558b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T150657506755Z-ed558b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.5137,
      "evidence_path": "artifacts/runs/claim-20260526T150657540295Z-2c3c94/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T150657540295Z-2c3c94",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.0863,
      "evidence_path": "artifacts/runs/claim-20260526T150657573999Z-db1230/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T150657573999Z-db1230",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.5029,
      "evidence_path": "artifacts/runs/claim-20260526T150657608586Z-4cc3aa/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T150657608586Z-4cc3aa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.2183,
      "evidence_path": "artifacts/runs/claim-20260526T150657642337Z-335c44/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T150657642337Z-335c44",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8457,
      "evidence_path": "artifacts/runs/claim-20260526T150657677441Z-2c2133/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T150657677441Z-2c2133",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4287,
      "evidence_path": "artifacts/runs/claim-20260526T150657714787Z-46ba50/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T150657714787Z-46ba50",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.4214,
      "evidence_path": "artifacts/runs/claim-20260526T150657750012Z-109326/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T150657750012Z-109326",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.1064,
      "evidence_path": "artifacts/runs/claim-20260526T150657784632Z-780b46/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T150657784632Z-780b46",
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
