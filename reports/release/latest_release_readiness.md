# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T15:22:49.537712+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `80.779` |
| `import_runtime` | `true` | `0` | `145.776` |
| `rcc_nexus_check` | `true` | `0` | `79.385` |
| `readme_mini_repo_audit` | `true` | `0` | `99.168` |
| `architecture_contract_validation` | `true` | `0` | `73.065` |
| `unit_tests` | `true` | `0` | `216.255` |
| `benchmark_harness` | `true` | `0` | `534.081` |
| `baseline_claim` | `true` | `0` | `157.883` |
| `promotion_path_claim` | `true` | `0` | `168.048` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152249289338Z-06023e",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152249289338Z-06023e\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T152249289338Z-06023e"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152249458125Z-f56ffe",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T152249458125Z-f56ffe\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T152249458125Z-f56ffe"
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
      "max_elapsed_ms": 39.4503,
      "mean_elapsed_ms": 35.2494,
      "min_elapsed_ms": 33.2792,
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
      "max_elapsed_ms": 35.6467,
      "mean_elapsed_ms": 33.7572,
      "min_elapsed_ms": 32.6628,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T15:22:48.747936+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.4503,
  "mean_elapsed_ms": 34.5033,
  "median_elapsed_ms": 33.9828,
  "min_elapsed_ms": 32.6628,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.4503,
      "evidence_path": "artifacts/runs/claim-20260526T152248747936Z-94514e/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T152248747936Z-94514e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.0805,
      "evidence_path": "artifacts/runs/claim-20260526T152248787336Z-29eef3/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T152248787336Z-29eef3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1503,
      "evidence_path": "artifacts/runs/claim-20260526T152248821853Z-0c0a09/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T152248821853Z-0c0a09",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.9378,
      "evidence_path": "artifacts/runs/claim-20260526T152248857512Z-f8afc2/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T152248857512Z-f8afc2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5985,
      "evidence_path": "artifacts/runs/claim-20260526T152248891193Z-cd82e1/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T152248891193Z-cd82e1",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.2792,
      "evidence_path": "artifacts/runs/claim-20260526T152248927637Z-555453/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T152248927637Z-555453",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.8883,
      "evidence_path": "artifacts/runs/claim-20260526T152248961061Z-49e57f/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T152248961061Z-49e57f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.6628,
      "evidence_path": "artifacts/runs/claim-20260526T152248994811Z-e6758b/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T152248994811Z-e6758b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.6467,
      "evidence_path": "artifacts/runs/claim-20260526T152249027855Z-f7ac58/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T152249027855Z-f7ac58",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0279,
      "evidence_path": "artifacts/runs/claim-20260526T152249064058Z-0dff6e/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T152249064058Z-0dff6e",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.3302,
      "evidence_path": "artifacts/runs/claim-20260526T152249097990Z-1df6bc/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T152249097990Z-1df6bc",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.9876,
      "evidence_path": "artifacts/runs/claim-20260526T152249130903Z-ec1c12/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T152249130903Z-ec1c12",
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
