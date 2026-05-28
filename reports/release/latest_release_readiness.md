# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T11:20:06.278624+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `1`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `74.174` |
| `import_runtime` | `true` | `0` | `111.089` |
| `rcc_nexus_check` | `true` | `0` | `94.087` |
| `readme_mini_repo_audit` | `true` | `0` | `104.841` |
| `architecture_contract_validation` | `true` | `0` | `63.962` |
| `unit_tests` | `true` | `0` | `222.482` |
| `benchmark_harness` | `true` | `0` | `546.02` |
| `baseline_claim` | `true` | `0` | `160.839` |
| `promotion_path_claim` | `true` | `0` | `160.398` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T112006030660Z-b7315c",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T112006030660Z-b7315c\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T112006030660Z-b7315c"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T112006190845Z-b4a671",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T112006190845Z-b4a671\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T112006190845Z-b4a671"
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
      "max_elapsed_ms": 38.7461,
      "mean_elapsed_ms": 35.7465,
      "min_elapsed_ms": 34.2257,
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
      "max_elapsed_ms": 40.5683,
      "mean_elapsed_ms": 35.8947,
      "min_elapsed_ms": 33.306,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T11:20:05.472919+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.5683,
  "mean_elapsed_ms": 35.8206,
  "median_elapsed_ms": 35.0942,
  "min_elapsed_ms": 33.306,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.7461,
      "evidence_path": "artifacts/runs/claim-20260528T112005472919Z-9cca21/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T112005472919Z-9cca21",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.6568,
      "evidence_path": "artifacts/runs/claim-20260528T112005512163Z-245d8a/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T112005512163Z-245d8a",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.1538,
      "evidence_path": "artifacts/runs/claim-20260528T112005549079Z-ea45f4/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T112005549079Z-ea45f4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.0116,
      "evidence_path": "artifacts/runs/claim-20260528T112005584504Z-ccb168/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T112005584504Z-ccb168",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.685,
      "evidence_path": "artifacts/runs/claim-20260528T112005619156Z-879ec4/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T112005619156Z-879ec4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.2257,
      "evidence_path": "artifacts/runs/claim-20260528T112005654725Z-a972af/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T112005654725Z-a972af",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.7478,
      "evidence_path": "artifacts/runs/claim-20260528T112005689140Z-c8940a/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T112005689140Z-c8940a",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.963,
      "evidence_path": "artifacts/runs/claim-20260528T112005725882Z-85f46f/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T112005725882Z-85f46f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7484,
      "evidence_path": "artifacts/runs/claim-20260528T112005762086Z-ccc599/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T112005762086Z-ccc599",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.306,
      "evidence_path": "artifacts/runs/claim-20260528T112005796255Z-37587f/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T112005796255Z-37587f",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.0346,
      "evidence_path": "artifacts/runs/claim-20260528T112005829084Z-f32b9b/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T112005829084Z-f32b9b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.5683,
      "evidence_path": "artifacts/runs/claim-20260528T112005864473Z-204269/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T112005864473Z-204269",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    }
  ],
  "schema": "tau-scaling-benchmark-summary-v0.3.2",
  "total_runs": 12,
  "unique_run_ids": 12
}
```

## Findings

| Severity | Code | Path | Detail |
|---|---|---|---|
| warning | `possible_path_break` | `README.md` | missing leading r in reports/ |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
