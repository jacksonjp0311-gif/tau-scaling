# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:54:49.641046+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `70.215` |
| `import_runtime` | `true` | `0` | `109.672` |
| `rcc_nexus_check` | `true` | `0` | `89.955` |
| `readme_mini_repo_audit` | `true` | `0` | `85.97` |
| `architecture_contract_validation` | `true` | `0` | `65.824` |
| `unit_tests` | `true` | `0` | `241.108` |
| `benchmark_harness` | `true` | `0` | `598.517` |
| `baseline_claim` | `true` | `0` | `181.928` |
| `promotion_path_claim` | `true` | `0` | `164.047` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085449386156Z-b05880",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085449386156Z-b05880\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T085449386156Z-b05880"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085449558355Z-81f605",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085449558355Z-81f605\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T085449558355Z-81f605"
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
      "max_elapsed_ms": 46.7166,
      "mean_elapsed_ms": 39.7858,
      "min_elapsed_ms": 35.3111,
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
      "max_elapsed_ms": 40.3071,
      "mean_elapsed_ms": 38.5903,
      "min_elapsed_ms": 37.1979,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:54:48.769292+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 46.7166,
  "mean_elapsed_ms": 39.1881,
  "median_elapsed_ms": 38.8603,
  "min_elapsed_ms": 35.3111,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.7166,
      "evidence_path": "artifacts/runs/claim-20260528T085448770292Z-75d53e/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T085448770292Z-75d53e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.3111,
      "evidence_path": "artifacts/runs/claim-20260528T085448816923Z-d82974/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T085448816923Z-d82974",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.8552,
      "evidence_path": "artifacts/runs/claim-20260528T085448852640Z-516471/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T085448852640Z-516471",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.477,
      "evidence_path": "artifacts/runs/claim-20260528T085448890984Z-e9ecd2/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T085448890984Z-e9ecd2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.8756,
      "evidence_path": "artifacts/runs/claim-20260528T085448930843Z-696815/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T085448930843Z-696815",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.4796,
      "evidence_path": "artifacts/runs/claim-20260528T085448970385Z-ad1033/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T085448970385Z-ad1033",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8653,
      "evidence_path": "artifacts/runs/claim-20260528T085449009614Z-087f7a/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T085449009614Z-087f7a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.1281,
      "evidence_path": "artifacts/runs/claim-20260528T085449048973Z-ee06ed/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T085449048973Z-ee06ed",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.3071,
      "evidence_path": "artifacts/runs/claim-20260528T085449087037Z-7f8af8/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T085449087037Z-7f8af8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.1979,
      "evidence_path": "artifacts/runs/claim-20260528T085449127813Z-460ff4/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T085449127813Z-460ff4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.2257,
      "evidence_path": "artifacts/runs/claim-20260528T085449164624Z-8e5de0/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T085449164624Z-8e5de0",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.8176,
      "evidence_path": "artifacts/runs/claim-20260528T085449203872Z-ae5ce6/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T085449203872Z-ae5ce6",
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
