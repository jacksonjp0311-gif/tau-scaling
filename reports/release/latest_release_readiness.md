# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T08:04:56.628109+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `68.43` |
| `import_runtime` | `true` | `0` | `100.369` |
| `rcc_nexus_check` | `true` | `0` | `106.407` |
| `readme_mini_repo_audit` | `true` | `0` | `120.257` |
| `architecture_contract_validation` | `true` | `0` | `80.997` |
| `unit_tests` | `true` | `0` | `236.313` |
| `benchmark_harness` | `true` | `0` | `567.421` |
| `baseline_claim` | `true` | `0` | `160.978` |
| `promotion_path_claim` | `true` | `0` | `147.737` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080456397296Z-776df8",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080456397296Z-776df8\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T080456397296Z-776df8"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080456548661Z-318aeb",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T080456548661Z-318aeb\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T080456548661Z-318aeb"
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
      "max_elapsed_ms": 41.4367,
      "mean_elapsed_ms": 37.9747,
      "min_elapsed_ms": 36.3225,
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
      "max_elapsed_ms": 38.6676,
      "mean_elapsed_ms": 36.754,
      "min_elapsed_ms": 34.6476,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T08:04:55.817857+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 41.4367,
  "mean_elapsed_ms": 37.3644,
  "median_elapsed_ms": 37.2903,
  "min_elapsed_ms": 34.6476,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.4367,
      "evidence_path": "artifacts/runs/claim-20260528T080455817857Z-528a58/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T080455817857Z-528a58",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.7172,
      "evidence_path": "artifacts/runs/claim-20260528T080455859124Z-7b15a7/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T080455859124Z-7b15a7",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8545,
      "evidence_path": "artifacts/runs/claim-20260528T080455897852Z-2a6b0a/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T080455897852Z-2a6b0a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3225,
      "evidence_path": "artifacts/runs/claim-20260528T080455935072Z-d77cea/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T080455935072Z-d77cea",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.7261,
      "evidence_path": "artifacts/runs/claim-20260528T080455971455Z-a837f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T080455971455Z-a837f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.7912,
      "evidence_path": "artifacts/runs/claim-20260528T080456009602Z-c85187/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T080456009602Z-c85187",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.6676,
      "evidence_path": "artifacts/runs/claim-20260528T080456046291Z-8946bb/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T080456046291Z-8946bb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.2873,
      "evidence_path": "artifacts/runs/claim-20260528T080456085805Z-fef858/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T080456085805Z-fef858",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6476,
      "evidence_path": "artifacts/runs/claim-20260528T080456124516Z-9e6ff1/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T080456124516Z-9e6ff1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.9015,
      "evidence_path": "artifacts/runs/claim-20260528T080456159122Z-a1cddc/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T080456159122Z-a1cddc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.2514,
      "evidence_path": "artifacts/runs/claim-20260528T080456193577Z-b53156/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T080456193577Z-b53156",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.7688,
      "evidence_path": "artifacts/runs/claim-20260528T080456229918Z-4f4cd6/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T080456229918Z-4f4cd6",
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
