# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T14:21:36.165931+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.224` |
| `import_runtime` | `true` | `0` | `114.111` |
| `rcc_nexus_check` | `true` | `0` | `80.269` |
| `readme_mini_repo_audit` | `true` | `0` | `104.426` |
| `architecture_contract_validation` | `true` | `0` | `63.832` |
| `unit_tests` | `true` | `0` | `209.604` |
| `benchmark_harness` | `true` | `0` | `537.283` |
| `baseline_claim` | `true` | `0` | `167.668` |
| `promotion_path_claim` | `true` | `0` | `157.986` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T142135924609Z-f2ca47",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T142135924609Z-f2ca47\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T142135924609Z-f2ca47"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T142136087336Z-4b06c7",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T142136087336Z-4b06c7\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T142136087336Z-4b06c7"
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
      "max_elapsed_ms": 39.0355,
      "mean_elapsed_ms": 35.816,
      "min_elapsed_ms": 33.1256,
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
      "max_elapsed_ms": 36.7423,
      "mean_elapsed_ms": 34.2319,
      "min_elapsed_ms": 32.0846,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T14:21:35.368085+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 39.0355,
  "mean_elapsed_ms": 35.024,
  "median_elapsed_ms": 34.5917,
  "min_elapsed_ms": 32.0846,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.0355,
      "evidence_path": "artifacts/runs/claim-20260526T142135368085Z-353b8f/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T142135368085Z-353b8f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.2398,
      "evidence_path": "artifacts/runs/claim-20260526T142135407396Z-d62dea/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T142135407396Z-d62dea",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.2565,
      "evidence_path": "artifacts/runs/claim-20260526T142135442856Z-92cd65/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T142135442856Z-92cd65",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7484,
      "evidence_path": "artifacts/runs/claim-20260526T142135481105Z-4c4492/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T142135481105Z-4c4492",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.4905,
      "evidence_path": "artifacts/runs/claim-20260526T142135516238Z-f3eaa2/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T142135516238Z-f3eaa2",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.1256,
      "evidence_path": "artifacts/runs/claim-20260526T142135550700Z-8707b9/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T142135550700Z-8707b9",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7423,
      "evidence_path": "artifacts/runs/claim-20260526T142135583966Z-c7d10d/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T142135583966Z-c7d10d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.2894,
      "evidence_path": "artifacts/runs/claim-20260526T142135620915Z-d60bd8/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T142135620915Z-d60bd8",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 32.0846,
      "evidence_path": "artifacts/runs/claim-20260526T142135656037Z-83705a/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T142135656037Z-83705a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.0339,
      "evidence_path": "artifacts/runs/claim-20260526T142135688378Z-c8f1e1/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T142135688378Z-c8f1e1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.5482,
      "evidence_path": "artifacts/runs/claim-20260526T142135722320Z-95dbc1/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T142135722320Z-95dbc1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6928,
      "evidence_path": "artifacts/runs/claim-20260526T142135755627Z-8807e8/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T142135755627Z-8807e8",
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
