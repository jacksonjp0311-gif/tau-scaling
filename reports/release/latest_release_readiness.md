# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T07:30:09.532488+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `68.322` |
| `import_runtime` | `true` | `0` | `100.821` |
| `rcc_nexus_check` | `true` | `0` | `87.896` |
| `readme_mini_repo_audit` | `true` | `0` | `83.396` |
| `architecture_contract_validation` | `true` | `0` | `60.715` |
| `unit_tests` | `true` | `0` | `227.713` |
| `benchmark_harness` | `true` | `0` | `550.368` |
| `baseline_claim` | `true` | `0` | `162.126` |
| `promotion_path_claim` | `true` | `0` | `157.838` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073009284001Z-390e7d",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073009284001Z-390e7d\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T073009284001Z-390e7d"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073009446184Z-bfa3c8",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T073009446184Z-bfa3c8\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T073009446184Z-bfa3c8"
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
      "max_elapsed_ms": 43.3088,
      "mean_elapsed_ms": 37.0757,
      "min_elapsed_ms": 34.9711,
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
      "max_elapsed_ms": 36.779,
      "mean_elapsed_ms": 35.1093,
      "min_elapsed_ms": 33.4663,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T07:30:08.725159+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 43.3088,
  "mean_elapsed_ms": 36.0925,
  "median_elapsed_ms": 35.5626,
  "min_elapsed_ms": 33.4663,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.3088,
      "evidence_path": "artifacts/runs/claim-20260528T073008725159Z-357c80/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T073008725159Z-357c80",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.2039,
      "evidence_path": "artifacts/runs/claim-20260528T073008768511Z-1ffea0/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T073008768511Z-1ffea0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.3322,
      "evidence_path": "artifacts/runs/claim-20260528T073008806082Z-412311/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T073008806082Z-412311",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.0812,
      "evidence_path": "artifacts/runs/claim-20260528T073008843102Z-16b70e/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T073008843102Z-16b70e",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.5572,
      "evidence_path": "artifacts/runs/claim-20260528T073008877423Z-9c4368/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T073008877423Z-9c4368",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.9711,
      "evidence_path": "artifacts/runs/claim-20260528T073008914096Z-1a3d35/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T073008914096Z-1a3d35",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.4663,
      "evidence_path": "artifacts/runs/claim-20260528T073008949137Z-cfa483/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T073008949137Z-cfa483",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.019,
      "evidence_path": "artifacts/runs/claim-20260528T073008982562Z-ec8e54/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T073008982562Z-ec8e54",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.7319,
      "evidence_path": "artifacts/runs/claim-20260528T073009016422Z-b86c82/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T073009016422Z-b86c82",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.779,
      "evidence_path": "artifacts/runs/claim-20260528T073009051484Z-ca9f70/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T073009051484Z-ca9f70",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.568,
      "evidence_path": "artifacts/runs/claim-20260528T073009088815Z-37d74d/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T073009088815Z-37d74d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.0916,
      "evidence_path": "artifacts/runs/claim-20260528T073009124737Z-c53cb1/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T073009124737Z-c53cb1",
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
