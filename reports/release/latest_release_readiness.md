# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T16:21:03.615172+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.374` |
| `import_runtime` | `true` | `0` | `119.601` |
| `rcc_nexus_check` | `true` | `0` | `76.863` |
| `readme_mini_repo_audit` | `true` | `0` | `98.753` |
| `architecture_contract_validation` | `true` | `0` | `80.25` |
| `unit_tests` | `true` | `0` | `223.347` |
| `benchmark_harness` | `true` | `0` | `577.119` |
| `baseline_claim` | `true` | `0` | `161.072` |
| `promotion_path_claim` | `true` | `0` | `163.617` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T162103369457Z-d7783e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T162103369457Z-d7783e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T162103369457Z-d7783e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T162103530809Z-fd25e5",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T162103530809Z-fd25e5\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T162103530809Z-fd25e5"
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
      "max_elapsed_ms": 43.656,
      "mean_elapsed_ms": 36.9703,
      "min_elapsed_ms": 33.8083,
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
      "max_elapsed_ms": 38.0331,
      "mean_elapsed_ms": 35.5375,
      "min_elapsed_ms": 32.7084,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T16:21:02.803953+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 43.656,
  "mean_elapsed_ms": 36.2539,
  "median_elapsed_ms": 35.6574,
  "min_elapsed_ms": 32.7084,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.656,
      "evidence_path": "artifacts/runs/claim-20260527T162102804953Z-a7772b/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T162102804953Z-a7772b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.0643,
      "evidence_path": "artifacts/runs/claim-20260527T162102848661Z-69ca11/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T162102848661Z-69ca11",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.6179,
      "evidence_path": "artifacts/runs/claim-20260527T162102885402Z-1fdbcf/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T162102885402Z-1fdbcf",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.8083,
      "evidence_path": "artifacts/runs/claim-20260527T162102919902Z-8d62be/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T162102919902Z-8d62be",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.52,
      "evidence_path": "artifacts/runs/claim-20260527T162102954722Z-5e2628/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T162102954722Z-5e2628",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.1554,
      "evidence_path": "artifacts/runs/claim-20260527T162102990543Z-f203c1/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T162102990543Z-f203c1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.7949,
      "evidence_path": "artifacts/runs/claim-20260527T162103027948Z-1dd883/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T162103027948Z-1dd883",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4847,
      "evidence_path": "artifacts/runs/claim-20260527T162103063285Z-b4f579/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T162103063285Z-b4f579",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.6847,
      "evidence_path": "artifacts/runs/claim-20260527T162103099560Z-12c494/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T162103099560Z-12c494",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.7084,
      "evidence_path": "artifacts/runs/claim-20260527T162103133497Z-8cf9b2/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T162103133497Z-8cf9b2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.0331,
      "evidence_path": "artifacts/runs/claim-20260527T162103165624Z-623fd2/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T162103165624Z-623fd2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.5192,
      "evidence_path": "artifacts/runs/claim-20260527T162103204083Z-265966/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T162103204083Z-265966",
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
