# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T13:27:22.848467+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.455` |
| `import_runtime` | `true` | `0` | `132.985` |
| `rcc_nexus_check` | `true` | `0` | `192.533` |
| `readme_mini_repo_audit` | `true` | `0` | `138.038` |
| `architecture_contract_validation` | `true` | `0` | `71.978` |
| `unit_tests` | `true` | `0` | `322.984` |
| `benchmark_harness` | `true` | `0` | `600.246` |
| `baseline_claim` | `true` | `0` | `164.004` |
| `promotion_path_claim` | `true` | `0` | `164.579` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T132722600056Z-f8263c",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T132722600056Z-f8263c\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T132722600056Z-f8263c"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T132722758740Z-2f4669",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T132722758740Z-2f4669\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T132722758740Z-2f4669"
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
      "max_elapsed_ms": 70.1904,
      "mean_elapsed_ms": 42.3935,
      "min_elapsed_ms": 33.9735,
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
      "max_elapsed_ms": 37.1833,
      "mean_elapsed_ms": 35.0587,
      "min_elapsed_ms": 33.0557,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T13:27:21.991957+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 70.1904,
  "mean_elapsed_ms": 38.7261,
  "median_elapsed_ms": 35.4073,
  "min_elapsed_ms": 33.0557,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.2701,
      "evidence_path": "artifacts/runs/claim-20260528T132721991957Z-d2a696/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T132721991957Z-d2a696",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.1121,
      "evidence_path": "artifacts/runs/claim-20260528T132722035662Z-b762f9/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T132722035662Z-b762f9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.2279,
      "evidence_path": "artifacts/runs/claim-20260528T132722072570Z-868107/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T132722072570Z-868107",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.9735,
      "evidence_path": "artifacts/runs/claim-20260528T132722107323Z-35d639/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T132722107323Z-35d639",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5868,
      "evidence_path": "artifacts/runs/claim-20260528T132722142043Z-8b404f/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T132722142043Z-8b404f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 70.1904,
      "evidence_path": "artifacts/runs/claim-20260528T132722177393Z-265735/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T132722177393Z-265735",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.5572,
      "evidence_path": "artifacts/runs/claim-20260528T132722257230Z-8b1b58/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T132722257230Z-8b1b58",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.5302,
      "evidence_path": "artifacts/runs/claim-20260528T132722291177Z-dd0280/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T132722291177Z-dd0280",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.1833,
      "evidence_path": "artifacts/runs/claim-20260528T132722328083Z-8af89a/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T132722328083Z-8af89a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.4521,
      "evidence_path": "artifacts/runs/claim-20260528T132722365601Z-662caa/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T132722365601Z-662caa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.5739,
      "evidence_path": "artifacts/runs/claim-20260528T132722400149Z-f321a4/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T132722400149Z-f321a4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.0557,
      "evidence_path": "artifacts/runs/claim-20260528T132722434446Z-c1d749/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T132722434446Z-c1d749",
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
