# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T10:11:44.807816+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `3`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.907` |
| `import_runtime` | `true` | `0` | `138.829` |
| `rcc_nexus_check` | `true` | `0` | `78.341` |
| `readme_mini_repo_audit` | `true` | `0` | `91.022` |
| `architecture_contract_validation` | `true` | `0` | `65.048` |
| `unit_tests` | `true` | `0` | `215.839` |
| `benchmark_harness` | `true` | `0` | `548.483` |
| `baseline_claim` | `true` | `0` | `162.959` |
| `promotion_path_claim` | `true` | `0` | `159.687` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T101144557614Z-3325e4",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T101144557614Z-3325e4\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T101144557614Z-3325e4"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T101144718977Z-d44d98",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T101144718977Z-d44d98\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T101144718977Z-d44d98"
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
      "max_elapsed_ms": 42.1384,
      "mean_elapsed_ms": 36.8416,
      "min_elapsed_ms": 33.4214,
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
      "max_elapsed_ms": 40.7973,
      "mean_elapsed_ms": 34.6578,
      "min_elapsed_ms": 32.4327,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T10:11:43.998563+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 42.1384,
  "mean_elapsed_ms": 35.7497,
  "median_elapsed_ms": 33.9234,
  "min_elapsed_ms": 32.4327,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.1384,
      "evidence_path": "artifacts/runs/claim-20260528T101143999563Z-a1b2ff/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T101143999563Z-a1b2ff",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.0013,
      "evidence_path": "artifacts/runs/claim-20260528T101144041807Z-d0a148/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T101144041807Z-d0a148",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5467,
      "evidence_path": "artifacts/runs/claim-20260528T101144075718Z-4fab10/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T101144075718Z-4fab10",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.4214,
      "evidence_path": "artifacts/runs/claim-20260528T101144111556Z-48c9c5/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T101144111556Z-48c9c5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0854,
      "evidence_path": "artifacts/runs/claim-20260528T101144145271Z-bc09b2/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T101144145271Z-bc09b2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.8564,
      "evidence_path": "artifacts/runs/claim-20260528T101144181090Z-593470/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T101144181090Z-593470",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7469,
      "evidence_path": "artifacts/runs/claim-20260528T101144221227Z-99784e/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T101144221227Z-99784e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7077,
      "evidence_path": "artifacts/runs/claim-20260528T101144254894Z-e1e610/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T101144254894Z-e1e610",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.4327,
      "evidence_path": "artifacts/runs/claim-20260528T101144289550Z-7f67c8/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T101144289550Z-7f67c8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.8455,
      "evidence_path": "artifacts/runs/claim-20260528T101144321579Z-f4e2e7/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T101144321579Z-f4e2e7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.4164,
      "evidence_path": "artifacts/runs/claim-20260528T101144355964Z-14284f/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T101144355964Z-14284f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.7973,
      "evidence_path": "artifacts/runs/claim-20260528T101144389661Z-30bea4/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T101144389661Z-30bea4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

| Severity | Code | Path | Detail |
|---|---|---|---|
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_tilde: \xc3 |
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_circumflex: \xc2 |
| warning | `possible_mojibake` | `README.md` | utf8_quote_dash_mojibake: \xe2\u20ac |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
