# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:35:39.760394+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `108.532` |
| `import_runtime` | `true` | `0` | `103.036` |
| `rcc_nexus_check` | `true` | `0` | `87.904` |
| `readme_mini_repo_audit` | `true` | `0` | `106.693` |
| `architecture_contract_validation` | `true` | `0` | `64.264` |
| `unit_tests` | `true` | `0` | `214.102` |
| `benchmark_harness` | `true` | `0` | `566.747` |
| `baseline_claim` | `true` | `0` | `169.017` |
| `promotion_path_claim` | `true` | `0` | `153.399` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073539521247Z-529dd6",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073539521247Z-529dd6\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T073539521247Z-529dd6"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073539679939Z-30aad7",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073539679939Z-30aad7\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T073539679939Z-30aad7"
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
      "max_elapsed_ms": 40.611,
      "mean_elapsed_ms": 37.836,
      "min_elapsed_ms": 35.2096,
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
      "max_elapsed_ms": 39.9513,
      "mean_elapsed_ms": 37.1013,
      "min_elapsed_ms": 35.193,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:35:38.933798+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.611,
  "mean_elapsed_ms": 37.4687,
  "median_elapsed_ms": 37.3398,
  "min_elapsed_ms": 35.193,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.611,
      "evidence_path": "artifacts/runs/claim-20260528T073538933798Z-b30815/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T073538933798Z-b30815",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.3506,
      "evidence_path": "artifacts/runs/claim-20260528T073538974750Z-f03c91/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T073538974750Z-f03c91",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.4688,
      "evidence_path": "artifacts/runs/claim-20260528T073539013612Z-7cc1cd/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T073539013612Z-7cc1cd",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8264,
      "evidence_path": "artifacts/runs/claim-20260528T073539050997Z-e1700e/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T073539050997Z-e1700e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.5498,
      "evidence_path": "artifacts/runs/claim-20260528T073539088369Z-bc1039/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T073539088369Z-bc1039",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.2096,
      "evidence_path": "artifacts/runs/claim-20260528T073539127107Z-bfaacb/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T073539127107Z-bfaacb",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3161,
      "evidence_path": "artifacts/runs/claim-20260528T073539162646Z-06ddc2/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T073539162646Z-06ddc2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3891,
      "evidence_path": "artifacts/runs/claim-20260528T073539200597Z-606954/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T073539200597Z-606954",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.3636,
      "evidence_path": "artifacts/runs/claim-20260528T073539236607Z-c17495/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T073539236607Z-c17495",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.9513,
      "evidence_path": "artifacts/runs/claim-20260528T073539274413Z-38c6c3/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T073539274413Z-38c6c3",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.3948,
      "evidence_path": "artifacts/runs/claim-20260528T073539314942Z-ec3619/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T073539314942Z-ec3619",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.193,
      "evidence_path": "artifacts/runs/claim-20260528T073539351299Z-d39980/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T073539351299Z-d39980",
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
