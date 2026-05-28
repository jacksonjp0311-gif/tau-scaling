# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T15:12:12.247640+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `89.894` |
| `import_runtime` | `true` | `0` | `124.567` |
| `rcc_nexus_check` | `true` | `0` | `90.979` |
| `readme_mini_repo_audit` | `true` | `0` | `101.298` |
| `architecture_contract_validation` | `true` | `0` | `70.478` |
| `unit_tests` | `true` | `0` | `235.158` |
| `benchmark_harness` | `true` | `0` | `620.696` |
| `baseline_claim` | `true` | `0` | `203.311` |
| `promotion_path_claim` | `true` | `0` | `186.266` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T151211956672Z-2ac6ec",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T151211956672Z-2ac6ec\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T151211956672Z-2ac6ec"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T151212158422Z-e73f6c",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T151212158422Z-e73f6c\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T151212158422Z-e73f6c"
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
      "max_elapsed_ms": 49.4778,
      "mean_elapsed_ms": 45.7955,
      "min_elapsed_ms": 40.826,
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
      "max_elapsed_ms": 37.5062,
      "mean_elapsed_ms": 36.3648,
      "min_elapsed_ms": 35.436,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T15:12:11.309409+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 49.4778,
  "mean_elapsed_ms": 41.0801,
  "median_elapsed_ms": 39.1661,
  "min_elapsed_ms": 35.436,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.0073,
      "evidence_path": "artifacts/runs/claim-20260528T151211309409Z-113a59/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T151211309409Z-113a59",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.826,
      "evidence_path": "artifacts/runs/claim-20260528T151211354184Z-b6ba0f/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T151211354184Z-b6ba0f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 49.4778,
      "evidence_path": "artifacts/runs/claim-20260528T151211394986Z-fb00f2/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T151211394986Z-fb00f2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 48.8619,
      "evidence_path": "artifacts/runs/claim-20260528T151211444487Z-b7397c/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T151211444487Z-b7397c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 49.1355,
      "evidence_path": "artifacts/runs/claim-20260528T151211493955Z-8f4572/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T151211493955Z-8f4572",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.4645,
      "evidence_path": "artifacts/runs/claim-20260528T151211542847Z-cc948b/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T151211542847Z-cc948b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0281,
      "evidence_path": "artifacts/runs/claim-20260528T151211584945Z-6651cc/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T151211584945Z-6651cc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.5062,
      "evidence_path": "artifacts/runs/claim-20260528T151211622890Z-cf3ee6/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T151211622890Z-cf3ee6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9376,
      "evidence_path": "artifacts/runs/claim-20260528T151211660670Z-fa2bb9/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T151211660670Z-fa2bb9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.5805,
      "evidence_path": "artifacts/runs/claim-20260528T151211697301Z-9cc2cf/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T151211697301Z-9cc2cf",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.436,
      "evidence_path": "artifacts/runs/claim-20260528T151211732190Z-e662fc/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T151211732190Z-e662fc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7003,
      "evidence_path": "artifacts/runs/claim-20260528T151211768634Z-17477d/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T151211768634Z-17477d",
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
