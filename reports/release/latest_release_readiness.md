# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T10:42:36.493648+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `78.405` |
| `import_runtime` | `true` | `0` | `126.318` |
| `rcc_nexus_check` | `true` | `0` | `87.478` |
| `readme_mini_repo_audit` | `true` | `0` | `89.7` |
| `architecture_contract_validation` | `true` | `0` | `64.077` |
| `unit_tests` | `true` | `0` | `244.32` |
| `benchmark_harness` | `true` | `0` | `540.013` |
| `baseline_claim` | `true` | `0` | `169.585` |
| `promotion_path_claim` | `true` | `0` | `167.07` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104236241238Z-8da3df",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104236241238Z-8da3df\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T104236241238Z-8da3df"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104236409692Z-101b30",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T104236409692Z-101b30\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T104236409692Z-101b30"
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
      "max_elapsed_ms": 39.6354,
      "mean_elapsed_ms": 36.0175,
      "min_elapsed_ms": 34.3896,
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
      "max_elapsed_ms": 35.1583,
      "mean_elapsed_ms": 34.4106,
      "min_elapsed_ms": 33.7382,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T10:42:35.681912+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.6354,
  "mean_elapsed_ms": 35.214,
  "median_elapsed_ms": 34.6484,
  "min_elapsed_ms": 33.7382,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.6354,
      "evidence_path": "artifacts/runs/claim-20260528T104235681912Z-e2527a/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T104235681912Z-e2527a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8341,
      "evidence_path": "artifacts/runs/claim-20260528T104235721974Z-de6221/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T104235721974Z-de6221",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.7769,
      "evidence_path": "artifacts/runs/claim-20260528T104235758706Z-896fd7/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T104235758706Z-896fd7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.5788,
      "evidence_path": "artifacts/runs/claim-20260528T104235794793Z-4b22a3/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T104235794793Z-4b22a3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.8903,
      "evidence_path": "artifacts/runs/claim-20260528T104235828794Z-7ba23b/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T104235828794Z-7ba23b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.3896,
      "evidence_path": "artifacts/runs/claim-20260528T104235863990Z-3e78b7/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T104235863990Z-3e78b7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.4085,
      "evidence_path": "artifacts/runs/claim-20260528T104235898992Z-c9b721/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T104235898992Z-c9b721",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.1027,
      "evidence_path": "artifacts/runs/claim-20260528T104235933505Z-763890/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T104235933505Z-763890",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7179,
      "evidence_path": "artifacts/runs/claim-20260528T104235967906Z-a886f1/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T104235967906Z-a886f1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.3378,
      "evidence_path": "artifacts/runs/claim-20260528T104236003337Z-4275ba/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T104236003337Z-4275ba",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1583,
      "evidence_path": "artifacts/runs/claim-20260528T104236037296Z-724fa2/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T104236037296Z-724fa2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7382,
      "evidence_path": "artifacts/runs/claim-20260528T104236072901Z-2edb6d/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T104236072901Z-2edb6d",
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
