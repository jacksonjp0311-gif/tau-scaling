# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T13:22:38.247239+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.366` |
| `import_runtime` | `true` | `0` | `116.512` |
| `rcc_nexus_check` | `true` | `0` | `83.626` |
| `readme_mini_repo_audit` | `true` | `0` | `103.865` |
| `architecture_contract_validation` | `true` | `0` | `78.361` |
| `unit_tests` | `true` | `0` | `221.569` |
| `benchmark_harness` | `true` | `0` | `590.957` |
| `baseline_claim` | `true` | `0` | `210.425` |
| `promotion_path_claim` | `true` | `0` | `203.855` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T132237939592Z-c509a4",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T132237939592Z-c509a4\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T132237939592Z-c509a4"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T132238163546Z-07fbdb",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T132238163546Z-07fbdb\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T132238163546Z-07fbdb"
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
      "max_elapsed_ms": 40.6952,
      "mean_elapsed_ms": 37.0322,
      "min_elapsed_ms": 35.6032,
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
      "max_elapsed_ms": 67.6181,
      "mean_elapsed_ms": 41.7155,
      "min_elapsed_ms": 34.9227,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T13:22:37.308281+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 67.6181,
  "mean_elapsed_ms": 39.3738,
  "median_elapsed_ms": 36.5911,
  "min_elapsed_ms": 34.9227,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.6952,
      "evidence_path": "artifacts/runs/claim-20260526T132237308281Z-1b93ad/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T132237308281Z-1b93ad",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.0158,
      "evidence_path": "artifacts/runs/claim-20260526T132237349468Z-bde1d7/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T132237349468Z-bde1d7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.1508,
      "evidence_path": "artifacts/runs/claim-20260526T132237386094Z-255454/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T132237386094Z-255454",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.101,
      "evidence_path": "artifacts/runs/claim-20260526T132237423242Z-e3bc7a/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T132237423242Z-e3bc7a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6032,
      "evidence_path": "artifacts/runs/claim-20260526T132237460518Z-0667c5/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T132237460518Z-0667c5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6274,
      "evidence_path": "artifacts/runs/claim-20260526T132237496235Z-f0fe9c/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T132237496235Z-f0fe9c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9227,
      "evidence_path": "artifacts/runs/claim-20260526T132237532213Z-02a3d9/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T132237532213Z-02a3d9",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7431,
      "evidence_path": "artifacts/runs/claim-20260526T132237567417Z-9024da/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T132237567417Z-9024da",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2137,
      "evidence_path": "artifacts/runs/claim-20260526T132237603529Z-4cc26f/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T132237603529Z-4cc26f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.4391,
      "evidence_path": "artifacts/runs/claim-20260526T132237639662Z-522aae/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T132237639662Z-522aae",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 67.6181,
      "evidence_path": "artifacts/runs/claim-20260526T132237677015Z-2f35ab/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T132237677015Z-2f35ab",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.356,
      "evidence_path": "artifacts/runs/claim-20260526T132237744332Z-b4d03d/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T132237744332Z-b4d03d",
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
