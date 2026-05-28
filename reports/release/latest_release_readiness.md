# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:57:21.350601+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.402` |
| `import_runtime` | `true` | `0` | `107.88` |
| `rcc_nexus_check` | `true` | `0` | `91.473` |
| `readme_mini_repo_audit` | `true` | `0` | `90.77` |
| `architecture_contract_validation` | `true` | `0` | `63.135` |
| `unit_tests` | `true` | `0` | `217.39` |
| `benchmark_harness` | `true` | `0` | `563.843` |
| `baseline_claim` | `true` | `0` | `172.277` |
| `promotion_path_claim` | `true` | `0` | `161.666` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085721095400Z-d9bc04",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085721095400Z-d9bc04\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T085721095400Z-d9bc04"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085721268133Z-8e242c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085721268133Z-8e242c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T085721268133Z-8e242c"
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
      "max_elapsed_ms": 38.7101,
      "mean_elapsed_ms": 36.6274,
      "min_elapsed_ms": 34.5514,
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
      "max_elapsed_ms": 38.4165,
      "mean_elapsed_ms": 35.2576,
      "min_elapsed_ms": 33.896,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:57:20.532686+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 38.7101,
  "mean_elapsed_ms": 35.9425,
  "median_elapsed_ms": 35.8419,
  "min_elapsed_ms": 33.896,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.7101,
      "evidence_path": "artifacts/runs/claim-20260528T085720532686Z-7bb475/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T085720532686Z-7bb475",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0343,
      "evidence_path": "artifacts/runs/claim-20260528T085720571373Z-c99f52/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T085720571373Z-c99f52",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.5514,
      "evidence_path": "artifacts/runs/claim-20260528T085720607312Z-eebc35/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T085720607312Z-eebc35",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.5941,
      "evidence_path": "artifacts/runs/claim-20260528T085720642864Z-b12403/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T085720642864Z-b12403",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.4622,
      "evidence_path": "artifacts/runs/claim-20260528T085720680223Z-9eb03a/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T085720680223Z-9eb03a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.4123,
      "evidence_path": "artifacts/runs/claim-20260528T085720716987Z-51cce5/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T085720716987Z-51cce5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.4468,
      "evidence_path": "artifacts/runs/claim-20260528T085720753875Z-5c2a37/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T085720753875Z-5c2a37",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.4165,
      "evidence_path": "artifacts/runs/claim-20260528T085720788245Z-af83c8/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T085720788245Z-af83c8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.827,
      "evidence_path": "artifacts/runs/claim-20260528T085720826470Z-08bd75/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T085720826470Z-08bd75",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.896,
      "evidence_path": "artifacts/runs/claim-20260528T085720861931Z-d78d0f/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T085720861931Z-d78d0f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.6496,
      "evidence_path": "artifacts/runs/claim-20260528T085720895383Z-057b97/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T085720895383Z-057b97",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3098,
      "evidence_path": "artifacts/runs/claim-20260528T085720931668Z-7efd1d/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T085720931668Z-7efd1d",
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
