# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T15:00:58.718396+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.92` |
| `import_runtime` | `true` | `0` | `124.587` |
| `rcc_nexus_check` | `true` | `0` | `87.57` |
| `readme_mini_repo_audit` | `true` | `0` | `99.434` |
| `architecture_contract_validation` | `true` | `0` | `70.853` |
| `unit_tests` | `true` | `0` | `254.384` |
| `benchmark_harness` | `true` | `0` | `698.734` |
| `baseline_claim` | `true` | `0` | `220.436` |
| `promotion_path_claim` | `true` | `0` | `190.513` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T150058430270Z-e8fd6c",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T150058430270Z-e8fd6c\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T150058430270Z-e8fd6c"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T150058622967Z-c3d731",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T150058622967Z-c3d731\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T150058622967Z-c3d731"
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
      "max_elapsed_ms": 47.4798,
      "mean_elapsed_ms": 40.2423,
      "min_elapsed_ms": 37.2365,
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
      "max_elapsed_ms": 65.4307,
      "mean_elapsed_ms": 52.9513,
      "min_elapsed_ms": 40.8391,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T15:00:57.682334+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 65.4307,
  "mean_elapsed_ms": 46.5968,
  "median_elapsed_ms": 42.2236,
  "min_elapsed_ms": 37.2365,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.4798,
      "evidence_path": "artifacts/runs/claim-20260527T150057682334Z-290362/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T150057682334Z-290362",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.74,
      "evidence_path": "artifacts/runs/claim-20260527T150057729713Z-e8b7f8/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T150057729713Z-e8b7f8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2065,
      "evidence_path": "artifacts/runs/claim-20260527T150057772122Z-2c6003/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T150057772122Z-2c6003",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.6759,
      "evidence_path": "artifacts/runs/claim-20260527T150057809636Z-017802/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T150057809636Z-017802",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.2365,
      "evidence_path": "artifacts/runs/claim-20260527T150057849019Z-a30e09/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T150057849019Z-a30e09",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.1151,
      "evidence_path": "artifacts/runs/claim-20260527T150057886354Z-810e0c/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T150057886354Z-810e0c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.8391,
      "evidence_path": "artifacts/runs/claim-20260527T150057925886Z-9d301c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T150057925886Z-9d301c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 62.3807,
      "evidence_path": "artifacts/runs/claim-20260527T150057966388Z-4b5b05/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T150057966388Z-4b5b05",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 61.817,
      "evidence_path": "artifacts/runs/claim-20260527T150058029205Z-887cec/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T150058029205Z-887cec",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.5331,
      "evidence_path": "artifacts/runs/claim-20260527T150058091623Z-801464/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T150058091623Z-801464",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 65.4307,
      "evidence_path": "artifacts/runs/claim-20260527T150058136633Z-6c34bb/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T150058136633Z-6c34bb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.7071,
      "evidence_path": "artifacts/runs/claim-20260527T150058201648Z-dd6c2f/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T150058201648Z-dd6c2f",
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
