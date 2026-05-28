# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T15:08:06.279599+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `119.102` |
| `import_runtime` | `true` | `0` | `140.886` |
| `rcc_nexus_check` | `true` | `0` | `100.549` |
| `readme_mini_repo_audit` | `true` | `0` | `114.564` |
| `architecture_contract_validation` | `true` | `0` | `81.48` |
| `unit_tests` | `true` | `0` | `253.552` |
| `benchmark_harness` | `true` | `0` | `760.275` |
| `baseline_claim` | `true` | `0` | `265.005` |
| `promotion_path_claim` | `true` | `0` | `274.818` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150805883936Z-3ba16f",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150805883936Z-3ba16f\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T150805883936Z-3ba16f"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150806164853Z-097d62",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150806164853Z-097d62\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T150806164853Z-097d62"
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
      "max_elapsed_ms": 65.8594,
      "mean_elapsed_ms": 49.256,
      "min_elapsed_ms": 39.3051,
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
      "max_elapsed_ms": 75.6769,
      "mean_elapsed_ms": 52.9523,
      "min_elapsed_ms": 44.7743,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T15:08:05.047339+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 75.6769,
  "mean_elapsed_ms": 51.1041,
  "median_elapsed_ms": 48.5619,
  "min_elapsed_ms": 39.3051,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.6774,
      "evidence_path": "artifacts/runs/claim-20260528T150805048339Z-2a3d78/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T150805048339Z-2a3d78",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.2939,
      "evidence_path": "artifacts/runs/claim-20260528T150805095459Z-d2c5cc/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T150805095459Z-d2c5cc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.3051,
      "evidence_path": "artifacts/runs/claim-20260528T150805138794Z-34192f/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T150805138794Z-34192f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.4553,
      "evidence_path": "artifacts/runs/claim-20260528T150805178452Z-85ca22/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T150805178452Z-85ca22",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 65.8594,
      "evidence_path": "artifacts/runs/claim-20260528T150805223372Z-9add48/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T150805223372Z-9add48",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 54.9448,
      "evidence_path": "artifacts/runs/claim-20260528T150805288893Z-f1df85/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T150805288893Z-f1df85",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 50.408,
      "evidence_path": "artifacts/runs/claim-20260528T150805345015Z-87e832/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T150805345015Z-87e832",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.9034,
      "evidence_path": "artifacts/runs/claim-20260528T150805395019Z-7a4a50/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T150805395019Z-7a4a50",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 75.6769,
      "evidence_path": "artifacts/runs/claim-20260528T150805442655Z-d9c312/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T150805442655Z-d9c312",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 50.5047,
      "evidence_path": "artifacts/runs/claim-20260528T150805518463Z-65822e/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T150805518463Z-65822e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 49.4465,
      "evidence_path": "artifacts/runs/claim-20260528T150805569030Z-875a79/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T150805569030Z-875a79",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.7743,
      "evidence_path": "artifacts/runs/claim-20260528T150805618668Z-400e7f/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T150805618668Z-400e7f",
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
