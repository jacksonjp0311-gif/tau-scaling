# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T15:03:45.413289+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `86.471` |
| `import_runtime` | `true` | `0` | `143.759` |
| `rcc_nexus_check` | `true` | `0` | `91.085` |
| `readme_mini_repo_audit` | `true` | `0` | `102.51` |
| `architecture_contract_validation` | `true` | `0` | `78.654` |
| `unit_tests` | `true` | `0` | `261.372` |
| `benchmark_harness` | `true` | `0` | `633.226` |
| `baseline_claim` | `true` | `0` | `187.046` |
| `promotion_path_claim` | `true` | `0` | `197.012` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150345120460Z-e5a7f5",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150345120460Z-e5a7f5\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T150345120460Z-e5a7f5"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150345318286Z-178e01",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T150345318286Z-178e01\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T150345318286Z-178e01"
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
      "max_elapsed_ms": 47.2714,
      "mean_elapsed_ms": 42.9064,
      "min_elapsed_ms": 41.0899,
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
      "max_elapsed_ms": 42.6039,
      "mean_elapsed_ms": 40.2997,
      "min_elapsed_ms": 38.4931,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T15:03:44.471717+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.2714,
  "mean_elapsed_ms": 41.6031,
  "median_elapsed_ms": 41.3964,
  "min_elapsed_ms": 38.4931,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.2714,
      "evidence_path": "artifacts/runs/claim-20260528T150344471717Z-9e0c68/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T150344471717Z-9e0c68",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 44.2512,
      "evidence_path": "artifacts/runs/claim-20260528T150344518937Z-183c3a/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T150344518937Z-183c3a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.3858,
      "evidence_path": "artifacts/runs/claim-20260528T150344563531Z-d748ac/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T150344563531Z-d748ac",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.0899,
      "evidence_path": "artifacts/runs/claim-20260528T150344605746Z-43b144/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T150344605746Z-43b144",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.407,
      "evidence_path": "artifacts/runs/claim-20260528T150344646916Z-aea9d2/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T150344646916Z-aea9d2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.0332,
      "evidence_path": "artifacts/runs/claim-20260528T150344687753Z-119f60/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T150344687753Z-119f60",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.2001,
      "evidence_path": "artifacts/runs/claim-20260528T150344731212Z-9ed52d/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T150344731212Z-9ed52d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.3893,
      "evidence_path": "artifacts/runs/claim-20260528T150344771576Z-848973/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T150344771576Z-848973",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.4931,
      "evidence_path": "artifacts/runs/claim-20260528T150344809980Z-d1b36c/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T150344809980Z-d1b36c",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.6039,
      "evidence_path": "artifacts/runs/claim-20260528T150344848399Z-86e4aa/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T150344848399Z-86e4aa",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.6645,
      "evidence_path": "artifacts/runs/claim-20260528T150344892567Z-a7abd5/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T150344892567Z-a7abd5",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 41.4473,
      "evidence_path": "artifacts/runs/claim-20260528T150344931950Z-fb7092/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T150344931950Z-fb7092",
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
