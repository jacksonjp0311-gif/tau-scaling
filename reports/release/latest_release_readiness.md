# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T09:01:47.603535+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `71.881` |
| `import_runtime` | `true` | `0` | `105.144` |
| `rcc_nexus_check` | `true` | `0` | `94.429` |
| `readme_mini_repo_audit` | `true` | `0` | `84.23` |
| `architecture_contract_validation` | `true` | `0` | `65.338` |
| `unit_tests` | `true` | `0` | `242.367` |
| `benchmark_harness` | `true` | `0` | `550.961` |
| `baseline_claim` | `true` | `0` | `157.882` |
| `promotion_path_claim` | `true` | `0` | `153.723` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090147369649Z-f6cb8e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090147369649Z-f6cb8e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T090147369649Z-f6cb8e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090147523295Z-b27ba7",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T090147523295Z-b27ba7\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T090147523295Z-b27ba7"
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
      "max_elapsed_ms": 41.462,
      "mean_elapsed_ms": 36.656,
      "min_elapsed_ms": 34.9495,
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
      "max_elapsed_ms": 37.3871,
      "mean_elapsed_ms": 35.5566,
      "min_elapsed_ms": 34.596,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T09:01:46.806639+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 41.462,
  "mean_elapsed_ms": 36.1063,
  "median_elapsed_ms": 35.4569,
  "min_elapsed_ms": 34.596,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.462,
      "evidence_path": "artifacts/runs/claim-20260528T090146806639Z-7a1033/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T090146806639Z-7a1033",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9495,
      "evidence_path": "artifacts/runs/claim-20260528T090146849231Z-5d3a11/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T090146849231Z-5d3a11",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5997,
      "evidence_path": "artifacts/runs/claim-20260528T090146883501Z-73c315/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T090146883501Z-73c315",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.6963,
      "evidence_path": "artifacts/runs/claim-20260528T090146920018Z-69fecc/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T090146920018Z-69fecc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.045,
      "evidence_path": "artifacts/runs/claim-20260528T090146955423Z-f67436/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T090146955423Z-f67436",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.1833,
      "evidence_path": "artifacts/runs/claim-20260528T090146990284Z-d47bc9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T090146990284Z-d47bc9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1621,
      "evidence_path": "artifacts/runs/claim-20260528T090147027981Z-a9ca32/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T090147027981Z-a9ca32",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3871,
      "evidence_path": "artifacts/runs/claim-20260528T090147065023Z-7b0db4/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T090147065023Z-7b0db4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.314,
      "evidence_path": "artifacts/runs/claim-20260528T090147102220Z-22b38f/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T090147102220Z-22b38f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.596,
      "evidence_path": "artifacts/runs/claim-20260528T090147137591Z-895c82/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T090147137591Z-895c82",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0207,
      "evidence_path": "artifacts/runs/claim-20260528T090147172542Z-4d4b9d/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T090147172542Z-4d4b9d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.8599,
      "evidence_path": "artifacts/runs/claim-20260528T090147207628Z-9a0ee8/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T090147207628Z-9a0ee8",
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
