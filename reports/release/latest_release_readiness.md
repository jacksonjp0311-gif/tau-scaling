# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T13:54:11.930863+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.037` |
| `import_runtime` | `true` | `0` | `110.969` |
| `rcc_nexus_check` | `true` | `0` | `85.644` |
| `readme_mini_repo_audit` | `true` | `0` | `88.659` |
| `architecture_contract_validation` | `true` | `0` | `64.517` |
| `unit_tests` | `true` | `0` | `216.985` |
| `benchmark_harness` | `true` | `0` | `567.21` |
| `baseline_claim` | `true` | `0` | `163.956` |
| `promotion_path_claim` | `true` | `0` | `164.738` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T135411684816Z-384f31",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T135411684816Z-384f31\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T135411684816Z-384f31"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T135411850118Z-6b067e",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T135411850118Z-6b067e\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T135411850118Z-6b067e"
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
      "max_elapsed_ms": 40.6904,
      "mean_elapsed_ms": 37.694,
      "min_elapsed_ms": 33.414,
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
      "max_elapsed_ms": 41.9051,
      "mean_elapsed_ms": 37.0498,
      "min_elapsed_ms": 35.0335,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T13:54:11.102115+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 41.9051,
  "mean_elapsed_ms": 37.3719,
  "median_elapsed_ms": 36.8757,
  "min_elapsed_ms": 33.414,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.6904,
      "evidence_path": "artifacts/runs/claim-20260528T135411102115Z-5b4494/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T135411102115Z-5b4494",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.4808,
      "evidence_path": "artifacts/runs/claim-20260528T135411142677Z-c15cbf/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T135411142677Z-c15cbf",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.0151,
      "evidence_path": "artifacts/runs/claim-20260528T135411183964Z-3e2f9e/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T135411183964Z-3e2f9e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.0455,
      "evidence_path": "artifacts/runs/claim-20260528T135411221306Z-67c146/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T135411221306Z-67c146",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.414,
      "evidence_path": "artifacts/runs/claim-20260528T135411261368Z-67a32c/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T135411261368Z-67a32c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.5185,
      "evidence_path": "artifacts/runs/claim-20260528T135411295539Z-2aa314/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T135411295539Z-2aa314",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.6488,
      "evidence_path": "artifacts/runs/claim-20260528T135411329481Z-e6abf1/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T135411329481Z-e6abf1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9113,
      "evidence_path": "artifacts/runs/claim-20260528T135411365702Z-7ba684/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T135411365702Z-7ba684",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.7364,
      "evidence_path": "artifacts/runs/claim-20260528T135411404721Z-e877a9/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T135411404721Z-e877a9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0639,
      "evidence_path": "artifacts/runs/claim-20260528T135411440395Z-c23016/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T135411440395Z-c23016",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0335,
      "evidence_path": "artifacts/runs/claim-20260528T135411475937Z-fa05eb/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T135411475937Z-fa05eb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 41.9051,
      "evidence_path": "artifacts/runs/claim-20260528T135411510579Z-7c1c34/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T135411510579Z-7c1c34",
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
