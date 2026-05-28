# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T15:54:01.822804+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `77.522` |
| `import_runtime` | `true` | `0` | `124.891` |
| `rcc_nexus_check` | `true` | `0` | `100.333` |
| `readme_mini_repo_audit` | `true` | `0` | `115.193` |
| `architecture_contract_validation` | `true` | `0` | `165.968` |
| `unit_tests` | `true` | `0` | `264.909` |
| `benchmark_harness` | `true` | `0` | `677.582` |
| `baseline_claim` | `true` | `0` | `185.495` |
| `promotion_path_claim` | `true` | `0` | `176.06` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T155401557789Z-bbe2dd",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T155401557789Z-bbe2dd\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T155401557789Z-bbe2dd"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T155401734675Z-54c9a0",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T155401734675Z-54c9a0\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T155401734675Z-54c9a0"
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
      "max_elapsed_ms": 48.3945,
      "mean_elapsed_ms": 43.2626,
      "min_elapsed_ms": 41.8663,
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
      "max_elapsed_ms": 48.5759,
      "mean_elapsed_ms": 42.3275,
      "min_elapsed_ms": 39.568,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T15:54:00.892102+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 48.5759,
  "mean_elapsed_ms": 42.795,
  "median_elapsed_ms": 42.1895,
  "min_elapsed_ms": 39.568,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 48.3945,
      "evidence_path": "artifacts/runs/claim-20260528T155400892102Z-52b0b5/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T155400892102Z-52b0b5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.2056,
      "evidence_path": "artifacts/runs/claim-20260528T155400940578Z-68f2ea/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T155400940578Z-68f2ea",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 41.8663,
      "evidence_path": "artifacts/runs/claim-20260528T155400982963Z-562d68/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T155400982963Z-562d68",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.1735,
      "evidence_path": "artifacts/runs/claim-20260528T155401025105Z-473ebd/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T155401025105Z-473ebd",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.6849,
      "evidence_path": "artifacts/runs/claim-20260528T155401067335Z-97db30/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T155401067335Z-97db30",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.251,
      "evidence_path": "artifacts/runs/claim-20260528T155401110453Z-06d140/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T155401110453Z-06d140",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.6967,
      "evidence_path": "artifacts/runs/claim-20260528T155401153799Z-28b009/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T155401153799Z-28b009",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.568,
      "evidence_path": "artifacts/runs/claim-20260528T155401194178Z-65b976/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T155401194178Z-65b976",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.7907,
      "evidence_path": "artifacts/runs/claim-20260528T155401233931Z-37bcb4/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T155401233931Z-37bcb4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.1496,
      "evidence_path": "artifacts/runs/claim-20260528T155401278176Z-d211fb/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T155401278176Z-d211fb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 41.1839,
      "evidence_path": "artifacts/runs/claim-20260528T155401318386Z-f29a50/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T155401318386Z-f29a50",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 48.5759,
      "evidence_path": "artifacts/runs/claim-20260528T155401359480Z-a10d51/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T155401359480Z-a10d51",
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
