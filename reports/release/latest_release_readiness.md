# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:32:56.877108+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.282` |
| `import_runtime` | `true` | `0` | `121.429` |
| `rcc_nexus_check` | `true` | `0` | `88.046` |
| `readme_mini_repo_audit` | `true` | `0` | `81.417` |
| `architecture_contract_validation` | `true` | `0` | `60.577` |
| `unit_tests` | `true` | `0` | `208.519` |
| `benchmark_harness` | `true` | `0` | `516.676` |
| `baseline_claim` | `true` | `0` | `153.756` |
| `promotion_path_claim` | `true` | `0` | `155.555` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073256637035Z-11c887",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073256637035Z-11c887\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T073256637035Z-11c887"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073256794729Z-8da073",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073256794729Z-8da073\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T073256794729Z-8da073"
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
      "max_elapsed_ms": 38.9955,
      "mean_elapsed_ms": 34.0097,
      "min_elapsed_ms": 31.9883,
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
      "max_elapsed_ms": 35.4479,
      "mean_elapsed_ms": 33.1365,
      "min_elapsed_ms": 31.0801,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:32:56.111687+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 38.9955,
  "mean_elapsed_ms": 33.5731,
  "median_elapsed_ms": 33.0393,
  "min_elapsed_ms": 31.0801,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.9955,
      "evidence_path": "artifacts/runs/claim-20260528T073256111687Z-ff22c4/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T073256111687Z-ff22c4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.066,
      "evidence_path": "artifacts/runs/claim-20260528T073256150821Z-e20b23/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T073256150821Z-e20b23",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 32.0539,
      "evidence_path": "artifacts/runs/claim-20260528T073256185844Z-a96238/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T073256185844Z-a96238",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.3521,
      "evidence_path": "artifacts/runs/claim-20260528T073256218777Z-7a882c/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T073256218777Z-7a882c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 32.6024,
      "evidence_path": "artifacts/runs/claim-20260528T073256251580Z-503362/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T073256251580Z-503362",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 31.9883,
      "evidence_path": "artifacts/runs/claim-20260528T073256284229Z-afa4a9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T073256284229Z-afa4a9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 31.0801,
      "evidence_path": "artifacts/runs/claim-20260528T073256317136Z-b945e0/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T073256317136Z-b945e0",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.3564,
      "evidence_path": "artifacts/runs/claim-20260528T073256348095Z-5717ec/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T073256348095Z-5717ec",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.7266,
      "evidence_path": "artifacts/runs/claim-20260528T073256380881Z-0c9f53/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T073256380881Z-0c9f53",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7536,
      "evidence_path": "artifacts/runs/claim-20260528T073256413585Z-702b24/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T073256413585Z-702b24",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4479,
      "evidence_path": "artifacts/runs/claim-20260528T073256447281Z-0228f8/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T073256447281Z-0228f8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.4547,
      "evidence_path": "artifacts/runs/claim-20260528T073256482721Z-57b820/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T073256482721Z-57b820",
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
