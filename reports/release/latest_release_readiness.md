# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:55:01.270238+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `78.749` |
| `import_runtime` | `true` | `0` | `107.264` |
| `rcc_nexus_check` | `true` | `0` | `90.235` |
| `readme_mini_repo_audit` | `true` | `0` | `100.742` |
| `architecture_contract_validation` | `true` | `0` | `77.077` |
| `unit_tests` | `true` | `0` | `225.089` |
| `benchmark_harness` | `true` | `0` | `549.463` |
| `baseline_claim` | `true` | `0` | `169.0` |
| `promotion_path_claim` | `true` | `0` | `154.984` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075501031182Z-08149d",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075501031182Z-08149d\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T075501031182Z-08149d"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075501187479Z-53ea6c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T075501187479Z-53ea6c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T075501187479Z-53ea6c"
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
      "max_elapsed_ms": 39.6873,
      "mean_elapsed_ms": 37.1195,
      "min_elapsed_ms": 34.6313,
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
      "max_elapsed_ms": 37.538,
      "mean_elapsed_ms": 35.5374,
      "min_elapsed_ms": 33.1226,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:55:00.458020+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.6873,
  "mean_elapsed_ms": 36.3284,
  "median_elapsed_ms": 36.3701,
  "min_elapsed_ms": 33.1226,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2565,
      "evidence_path": "artifacts/runs/claim-20260528T075500458020Z-e2e1a8/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T075500458020Z-e2e1a8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.4017,
      "evidence_path": "artifacts/runs/claim-20260528T075500497323Z-c499fc/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T075500497323Z-c499fc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3927,
      "evidence_path": "artifacts/runs/claim-20260528T075500534364Z-05f42a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T075500534364Z-05f42a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.6313,
      "evidence_path": "artifacts/runs/claim-20260528T075500570743Z-88958b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T075500570743Z-88958b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.6873,
      "evidence_path": "artifacts/runs/claim-20260528T075500606056Z-0a847e/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T075500606056Z-0a847e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3475,
      "evidence_path": "artifacts/runs/claim-20260528T075500645670Z-280ec9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T075500645670Z-280ec9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.538,
      "evidence_path": "artifacts/runs/claim-20260528T075500682214Z-8a1c36/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T075500682214Z-8a1c36",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.24,
      "evidence_path": "artifacts/runs/claim-20260528T075500720664Z-64c44c/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T075500720664Z-64c44c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3415,
      "evidence_path": "artifacts/runs/claim-20260528T075500758141Z-ba1805/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T075500758141Z-ba1805",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1804,
      "evidence_path": "artifacts/runs/claim-20260528T075500794077Z-e82532/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T075500794077Z-e82532",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.1226,
      "evidence_path": "artifacts/runs/claim-20260528T075500829093Z-e8394c/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T075500829093Z-e8394c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.8016,
      "evidence_path": "artifacts/runs/claim-20260528T075500862929Z-0d8f44/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T075500862929Z-0d8f44",
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
