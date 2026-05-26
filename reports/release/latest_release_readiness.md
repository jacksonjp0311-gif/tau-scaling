# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T11:25:47.514709+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `1`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `73.847` |
| `import_runtime` | `true` | `0` | `115.398` |
| `rcc_nexus_check` | `true` | `0` | `93.208` |
| `readme_mini_repo_audit` | `true` | `0` | `216.329` |
| `architecture_contract_validation` | `true` | `0` | `111.983` |
| `unit_tests` | `true` | `0` | `284.531` |
| `benchmark_harness` | `true` | `0` | `634.417` |
| `baseline_claim` | `true` | `0` | `167.147` |
| `promotion_path_claim` | `true` | `0` | `157.427` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T112547276346Z-5b14cb",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T112547276346Z-5b14cb\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T112547276346Z-5b14cb"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T112547435419Z-a8e29c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T112547435419Z-a8e29c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T112547435419Z-a8e29c"
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
      "max_elapsed_ms": 65.4238,
      "mean_elapsed_ms": 48.1385,
      "min_elapsed_ms": 39.4496,
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
      "max_elapsed_ms": 37.1694,
      "mean_elapsed_ms": 36.0557,
      "min_elapsed_ms": 34.0319,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T11:25:46.632533+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 65.4238,
  "mean_elapsed_ms": 42.0971,
  "median_elapsed_ms": 38.3095,
  "min_elapsed_ms": 34.0319,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 53.147,
      "evidence_path": "artifacts/runs/claim-20260526T112546632533Z-22061e/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T112546632533Z-22061e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 65.4238,
      "evidence_path": "artifacts/runs/claim-20260526T112546686348Z-d7954d/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T112546686348Z-d7954d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 51.2312,
      "evidence_path": "artifacts/runs/claim-20260526T112546751572Z-b4c910/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T112546751572Z-b4c910",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.4496,
      "evidence_path": "artifacts/runs/claim-20260526T112546803044Z-bbe105/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T112546803044Z-bbe105",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.5143,
      "evidence_path": "artifacts/runs/claim-20260526T112546842798Z-36a397/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T112546842798Z-36a397",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.0654,
      "evidence_path": "artifacts/runs/claim-20260526T112546882490Z-ef4f53/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T112546882490Z-ef4f53",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0319,
      "evidence_path": "artifacts/runs/claim-20260526T112546922876Z-1d061a/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T112546922876Z-1d061a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.678,
      "evidence_path": "artifacts/runs/claim-20260526T112546957062Z-922407/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T112546957062Z-922407",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3841,
      "evidence_path": "artifacts/runs/claim-20260526T112546993005Z-454024/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T112546993005Z-454024",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0663,
      "evidence_path": "artifacts/runs/claim-20260526T112547029251Z-2ab74b/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T112547029251Z-2ab74b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.1694,
      "evidence_path": "artifacts/runs/claim-20260526T112547066710Z-3bf76e/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T112547066710Z-3bf76e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0045,
      "evidence_path": "artifacts/runs/claim-20260526T112547104635Z-921c01/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T112547104635Z-921c01",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

| Severity | Code | Path | Detail |
|---|---|---|---|
| warning | `possible_mojibake_or_path_break` | `README.md` | Found token:   |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
