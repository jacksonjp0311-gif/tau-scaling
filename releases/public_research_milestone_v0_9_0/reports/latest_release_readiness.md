# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T15:21:24.130051+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `92.977` |
| `import_runtime` | `true` | `0` | `139.573` |
| `rcc_nexus_check` | `true` | `0` | `105.421` |
| `readme_mini_repo_audit` | `true` | `0` | `110.092` |
| `architecture_contract_validation` | `true` | `0` | `85.799` |
| `unit_tests` | `true` | `0` | `279.997` |
| `benchmark_harness` | `true` | `0` | `801.973` |
| `baseline_claim` | `true` | `0` | `281.717` |
| `promotion_path_claim` | `true` | `0` | `217.166` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T152123812736Z-7a9bb3",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T152123812736Z-7a9bb3\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T152123812736Z-7a9bb3"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T152124021675Z-2513e1",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T152124021675Z-2513e1\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T152124021675Z-2513e1"
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
      "max_elapsed_ms": 53.0744,
      "mean_elapsed_ms": 45.36,
      "min_elapsed_ms": 39.9733,
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
      "max_elapsed_ms": 77.1454,
      "mean_elapsed_ms": 62.3144,
      "min_elapsed_ms": 44.6754,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T15:21:22.910607+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 77.1454,
  "mean_elapsed_ms": 53.8372,
  "median_elapsed_ms": 46.6442,
  "min_elapsed_ms": 39.9733,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 53.0744,
      "evidence_path": "artifacts/runs/claim-20260528T152122910607Z-963247/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T152122910607Z-963247",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.8806,
      "evidence_path": "artifacts/runs/claim-20260528T152122963937Z-9483f0/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T152122963937Z-9483f0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.1894,
      "evidence_path": "artifacts/runs/claim-20260528T152123006118Z-2b19df/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T152123006118Z-2b19df",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.9733,
      "evidence_path": "artifacts/runs/claim-20260528T152123051033Z-232ce7/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T152123051033Z-232ce7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 46.8719,
      "evidence_path": "artifacts/runs/claim-20260528T152123091161Z-c68d4f/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T152123091161Z-c68d4f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.1705,
      "evidence_path": "artifacts/runs/claim-20260528T152123138916Z-63bdaa/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T152123138916Z-63bdaa",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 76.8477,
      "evidence_path": "artifacts/runs/claim-20260528T152123185099Z-3df62b/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T152123185099Z-3df62b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 64.3597,
      "evidence_path": "artifacts/runs/claim-20260528T152123261857Z-7c774d/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T152123261857Z-7c774d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 64.4414,
      "evidence_path": "artifacts/runs/claim-20260528T152123325871Z-7551aa/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T152123325871Z-7551aa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 44.6754,
      "evidence_path": "artifacts/runs/claim-20260528T152123390734Z-83b413/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T152123390734Z-83b413",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.4166,
      "evidence_path": "artifacts/runs/claim-20260528T152123435161Z-21e253/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T152123435161Z-21e253",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 77.1454,
      "evidence_path": "artifacts/runs/claim-20260528T152123482318Z-bc7dd0/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T152123482318Z-bc7dd0",
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
