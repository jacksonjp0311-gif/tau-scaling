# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T17:51:15.096160+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `88.53` |
| `import_runtime` | `true` | `0` | `126.893` |
| `rcc_nexus_check` | `true` | `0` | `108.325` |
| `readme_mini_repo_audit` | `true` | `0` | `99.044` |
| `architecture_contract_validation` | `true` | `0` | `67.963` |
| `unit_tests` | `true` | `0` | `228.783` |
| `benchmark_harness` | `true` | `0` | `571.24` |
| `baseline_claim` | `true` | `0` | `170.098` |
| `promotion_path_claim` | `true` | `0` | `176.763` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175114820250Z-dbd5c7",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175114820250Z-dbd5c7\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T175114820250Z-dbd5c7"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175114996723Z-c039f0",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T175114996723Z-c039f0\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T175114996723Z-c039f0"
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
      "max_elapsed_ms": 46.2872,
      "mean_elapsed_ms": 38.7051,
      "min_elapsed_ms": 35.4432,
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
      "max_elapsed_ms": 38.9592,
      "mean_elapsed_ms": 36.146,
      "min_elapsed_ms": 34.7855,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T17:51:14.234103+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 46.2872,
  "mean_elapsed_ms": 37.4256,
  "median_elapsed_ms": 36.4817,
  "min_elapsed_ms": 34.7855,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.2872,
      "evidence_path": "artifacts/runs/claim-20260527T175114234103Z-574964/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T175114234103Z-574964",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.0774,
      "evidence_path": "artifacts/runs/claim-20260527T175114281176Z-a497c8/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T175114281176Z-a497c8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.0462,
      "evidence_path": "artifacts/runs/claim-20260527T175114317291Z-9cf98a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T175114317291Z-9cf98a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.9229,
      "evidence_path": "artifacts/runs/claim-20260527T175114357027Z-2ac41b/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T175114357027Z-2ac41b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.4536,
      "evidence_path": "artifacts/runs/claim-20260527T175114394110Z-68e933/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T175114394110Z-68e933",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.4432,
      "evidence_path": "artifacts/runs/claim-20260527T175114432260Z-91f783/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T175114432260Z-91f783",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.9592,
      "evidence_path": "artifacts/runs/claim-20260527T175114468190Z-542894/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T175114468190Z-542894",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0662,
      "evidence_path": "artifacts/runs/claim-20260527T175114507587Z-ebaf74/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T175114507587Z-ebaf74",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1333,
      "evidence_path": "artifacts/runs/claim-20260527T175114542896Z-f62abd/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T175114542896Z-f62abd",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7855,
      "evidence_path": "artifacts/runs/claim-20260527T175114579419Z-805c98/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T175114579419Z-805c98",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8302,
      "evidence_path": "artifacts/runs/claim-20260527T175114613645Z-515a46/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T175114613645Z-515a46",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.1018,
      "evidence_path": "artifacts/runs/claim-20260527T175114651081Z-2cef56/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T175114651081Z-2cef56",
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
