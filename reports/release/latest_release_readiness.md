# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:36:03.960122+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `70.671` |
| `import_runtime` | `true` | `0` | `105.513` |
| `rcc_nexus_check` | `true` | `0` | `85.404` |
| `readme_mini_repo_audit` | `true` | `0` | `84.479` |
| `architecture_contract_validation` | `true` | `0` | `62.043` |
| `unit_tests` | `true` | `0` | `222.086` |
| `benchmark_harness` | `true` | `0` | `555.716` |
| `baseline_claim` | `true` | `0` | `191.845` |
| `promotion_path_claim` | `true` | `0` | `188.155` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T083603677819Z-4330f3",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T083603677819Z-4330f3\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T083603677819Z-4330f3"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T083603848446Z-f57ee1",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T083603848446Z-f57ee1\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T083603848446Z-f57ee1"
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
      "max_elapsed_ms": 38.7331,
      "mean_elapsed_ms": 36.0807,
      "min_elapsed_ms": 34.6958,
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
      "max_elapsed_ms": 39.0034,
      "mean_elapsed_ms": 36.9634,
      "min_elapsed_ms": 35.0896,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:36:03.083513+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.0034,
  "mean_elapsed_ms": 36.5221,
  "median_elapsed_ms": 35.9455,
  "min_elapsed_ms": 34.6958,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.7331,
      "evidence_path": "artifacts/runs/claim-20260528T083603083513Z-bde1aa/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T083603083513Z-bde1aa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1011,
      "evidence_path": "artifacts/runs/claim-20260528T083603122230Z-b3aef1/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T083603122230Z-b3aef1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.6958,
      "evidence_path": "artifacts/runs/claim-20260528T083603157823Z-436636/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T083603157823Z-436636",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.0077,
      "evidence_path": "artifacts/runs/claim-20260528T083603192881Z-4f928b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T083603192881Z-4f928b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0527,
      "evidence_path": "artifacts/runs/claim-20260528T083603227783Z-7072d7/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T083603227783Z-7072d7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8939,
      "evidence_path": "artifacts/runs/claim-20260528T083603263569Z-59c875/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T083603263569Z-59c875",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.9922,
      "evidence_path": "artifacts/runs/claim-20260528T083603301467Z-d28904/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T083603301467Z-d28904",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.2023,
      "evidence_path": "artifacts/runs/claim-20260528T083603339995Z-68bb61/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T083603339995Z-68bb61",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.6546,
      "evidence_path": "artifacts/runs/claim-20260528T083603374708Z-b88a7f/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T083603374708Z-b88a7f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0896,
      "evidence_path": "artifacts/runs/claim-20260528T083603414218Z-da5942/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T083603414218Z-da5942",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8384,
      "evidence_path": "artifacts/runs/claim-20260528T083603448699Z-e2b73a/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T083603448699Z-e2b73a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.0034,
      "evidence_path": "artifacts/runs/claim-20260528T083603484834Z-026c1c/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T083603484834Z-026c1c",
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
