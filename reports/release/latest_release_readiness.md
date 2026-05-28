# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:51:34.340932+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `68.552` |
| `import_runtime` | `true` | `0` | `106.219` |
| `rcc_nexus_check` | `true` | `0` | `87.349` |
| `readme_mini_repo_audit` | `true` | `0` | `81.157` |
| `architecture_contract_validation` | `true` | `0` | `64.082` |
| `unit_tests` | `true` | `0` | `211.996` |
| `benchmark_harness` | `true` | `0` | `574.234` |
| `baseline_claim` | `true` | `0` | `153.611` |
| `promotion_path_claim` | `true` | `0` | `185.009` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085134071936Z-c85aaa",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085134071936Z-c85aaa\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T085134071936Z-c85aaa"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085134249581Z-c60e30",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T085134249581Z-c60e30\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T085134249581Z-c60e30"
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
      "max_elapsed_ms": 47.9881,
      "mean_elapsed_ms": 40.8693,
      "min_elapsed_ms": 35.7214,
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
      "max_elapsed_ms": 36.8088,
      "mean_elapsed_ms": 35.7884,
      "min_elapsed_ms": 33.836,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:51:33.486558+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.9881,
  "mean_elapsed_ms": 38.3289,
  "median_elapsed_ms": 36.5053,
  "min_elapsed_ms": 33.836,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.9881,
      "evidence_path": "artifacts/runs/claim-20260528T085133487560Z-e8eca2/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T085133487560Z-e8eca2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.6079,
      "evidence_path": "artifacts/runs/claim-20260528T085133535725Z-04a3cf/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T085133535725Z-04a3cf",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.117,
      "evidence_path": "artifacts/runs/claim-20260528T085133582450Z-516c59/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T085133582450Z-516c59",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8814,
      "evidence_path": "artifacts/runs/claim-20260528T085133624026Z-cd0738/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T085133624026Z-cd0738",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.7214,
      "evidence_path": "artifacts/runs/claim-20260528T085133661322Z-41cab3/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T085133661322Z-41cab3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.9001,
      "evidence_path": "artifacts/runs/claim-20260528T085133697887Z-897159/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T085133697887Z-897159",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9808,
      "evidence_path": "artifacts/runs/claim-20260528T085133733625Z-1b8129/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T085133733625Z-1b8129",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.836,
      "evidence_path": "artifacts/runs/claim-20260528T085133768768Z-626da1/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T085133768768Z-626da1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2882,
      "evidence_path": "artifacts/runs/claim-20260528T085133803273Z-14f266/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T085133803273Z-14f266",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.8088,
      "evidence_path": "artifacts/runs/claim-20260528T085133839875Z-b09b55/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T085133839875Z-b09b55",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0945,
      "evidence_path": "artifacts/runs/claim-20260528T085133876298Z-6e6527/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T085133876298Z-6e6527",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7223,
      "evidence_path": "artifacts/runs/claim-20260528T085133912738Z-5c8f7b/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T085133912738Z-5c8f7b",
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
