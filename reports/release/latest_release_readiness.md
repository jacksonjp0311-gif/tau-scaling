# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T13:09:10.141767+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `86.366` |
| `import_runtime` | `true` | `0` | `120.447` |
| `rcc_nexus_check` | `true` | `0` | `97.472` |
| `readme_mini_repo_audit` | `true` | `0` | `89.45` |
| `architecture_contract_validation` | `true` | `0` | `66.625` |
| `unit_tests` | `true` | `0` | `215.995` |
| `benchmark_harness` | `true` | `0` | `562.02` |
| `baseline_claim` | `true` | `0` | `162.038` |
| `promotion_path_claim` | `true` | `0` | `155.903` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130909901066Z-55ba9e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130909901066Z-55ba9e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T130909901066Z-55ba9e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130910060240Z-0478c6",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T130910060240Z-0478c6\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T130910060240Z-0478c6"
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
      "max_elapsed_ms": 39.8154,
      "mean_elapsed_ms": 37.3036,
      "min_elapsed_ms": 35.188,
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
      "max_elapsed_ms": 38.6729,
      "mean_elapsed_ms": 36.4315,
      "min_elapsed_ms": 33.7425,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T13:09:09.328498+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.8154,
  "mean_elapsed_ms": 36.8676,
  "median_elapsed_ms": 36.819,
  "min_elapsed_ms": 33.7425,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.3572,
      "evidence_path": "artifacts/runs/claim-20260526T130909328498Z-fa2707/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T130909328498Z-fa2707",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6939,
      "evidence_path": "artifacts/runs/claim-20260526T130909368103Z-162c7c/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T130909368103Z-162c7c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.188,
      "evidence_path": "artifacts/runs/claim-20260526T130909404613Z-e07f4a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T130909404613Z-e07f4a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.6445,
      "evidence_path": "artifacts/runs/claim-20260526T130909439107Z-d6340b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T130909439107Z-d6340b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.1225,
      "evidence_path": "artifacts/runs/claim-20260526T130909476655Z-ef376c/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T130909476655Z-ef376c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.8154,
      "evidence_path": "artifacts/runs/claim-20260526T130909513262Z-30c5b9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T130909513262Z-30c5b9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.9934,
      "evidence_path": "artifacts/runs/claim-20260526T130909554127Z-7dfded/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T130909554127Z-7dfded",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.6729,
      "evidence_path": "artifacts/runs/claim-20260526T130909591586Z-cbcdaa/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T130909591586Z-cbcdaa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2935,
      "evidence_path": "artifacts/runs/claim-20260526T130909629867Z-ad6a09/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T130909629867Z-ad6a09",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7425,
      "evidence_path": "artifacts/runs/claim-20260526T130909665985Z-4e312c/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T130909665985Z-4e312c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.478,
      "evidence_path": "artifacts/runs/claim-20260526T130909700514Z-c672f3/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T130909700514Z-c672f3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4088,
      "evidence_path": "artifacts/runs/claim-20260526T130909737867Z-796e01/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T130909737867Z-796e01",
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
