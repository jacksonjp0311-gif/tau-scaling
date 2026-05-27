# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T17:35:38.269263+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.584` |
| `import_runtime` | `true` | `0` | `109.853` |
| `rcc_nexus_check` | `true` | `0` | `95.227` |
| `readme_mini_repo_audit` | `true` | `0` | `94.01` |
| `architecture_contract_validation` | `true` | `0` | `65.331` |
| `unit_tests` | `true` | `0` | `220.755` |
| `benchmark_harness` | `true` | `0` | `556.513` |
| `baseline_claim` | `true` | `0` | `168.053` |
| `promotion_path_claim` | `true` | `0` | `164.17` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T173538021038Z-1553b3",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T173538021038Z-1553b3\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T173538021038Z-1553b3"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T173538185078Z-e21d31",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T173538185078Z-e21d31\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T173538185078Z-e21d31"
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
      "max_elapsed_ms": 40.7195,
      "mean_elapsed_ms": 36.3847,
      "min_elapsed_ms": 34.2515,
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
      "max_elapsed_ms": 37.9419,
      "mean_elapsed_ms": 37.0791,
      "min_elapsed_ms": 36.6511,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T17:35:37.445164+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.7195,
  "mean_elapsed_ms": 36.7319,
  "median_elapsed_ms": 36.7223,
  "min_elapsed_ms": 34.2515,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.7195,
      "evidence_path": "artifacts/runs/claim-20260527T173537445164Z-43f825/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T173537445164Z-43f825",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.3503,
      "evidence_path": "artifacts/runs/claim-20260527T173537486224Z-a85a75/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T173537486224Z-a85a75",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3505,
      "evidence_path": "artifacts/runs/claim-20260527T173537520709Z-ccd3db/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T173537520709Z-ccd3db",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3021,
      "evidence_path": "artifacts/runs/claim-20260527T173537556770Z-49f35c/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T173537556770Z-49f35c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3344,
      "evidence_path": "artifacts/runs/claim-20260527T173537594154Z-8156cd/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T173537594154Z-8156cd",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.2515,
      "evidence_path": "artifacts/runs/claim-20260527T173537630712Z-a64216/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T173537630712Z-a64216",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.1907,
      "evidence_path": "artifacts/runs/claim-20260527T173537665536Z-0d5f2c/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T173537665536Z-0d5f2c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.6511,
      "evidence_path": "artifacts/runs/claim-20260527T173537702293Z-dd3d16/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T173537702293Z-dd3d16",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.9419,
      "evidence_path": "artifacts/runs/claim-20260527T173537739015Z-a863d6/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T173537739015Z-a863d6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8922,
      "evidence_path": "artifacts/runs/claim-20260527T173537777046Z-22fc34/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T173537777046Z-22fc34",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.0053,
      "evidence_path": "artifacts/runs/claim-20260527T173537814171Z-93aa7f/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T173537814171Z-93aa7f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7935,
      "evidence_path": "artifacts/runs/claim-20260527T173537851738Z-4e2ae1/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T173537851738Z-4e2ae1",
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
