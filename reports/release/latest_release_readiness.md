# Tau Scaling Unified Release Readiness

Generated: `2026-05-27T17:29:55.531005+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `73.457` |
| `import_runtime` | `true` | `0` | `110.361` |
| `rcc_nexus_check` | `true` | `0` | `98.786` |
| `readme_mini_repo_audit` | `true` | `0` | `87.964` |
| `architecture_contract_validation` | `true` | `0` | `64.62` |
| `unit_tests` | `true` | `0` | `220.205` |
| `benchmark_harness` | `true` | `0` | `601.72` |
| `baseline_claim` | `true` | `0` | `201.857` |
| `promotion_path_claim` | `true` | `0` | `189.725` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T172955244725Z-424808",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T172955244725Z-424808\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260527T172955244725Z-424808"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T172955448166Z-698fbd",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260527T172955448166Z-698fbd\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260527T172955448166Z-698fbd"
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
      "max_elapsed_ms": 42.8237,
      "mean_elapsed_ms": 38.7887,
      "min_elapsed_ms": 34.4669,
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
      "max_elapsed_ms": 47.3869,
      "mean_elapsed_ms": 38.2917,
      "min_elapsed_ms": 33.5563,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-27T17:29:54.615103+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.3869,
  "mean_elapsed_ms": 38.5402,
  "median_elapsed_ms": 37.1608,
  "min_elapsed_ms": 33.5563,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.3394,
      "evidence_path": "artifacts/runs/claim-20260527T172954616103Z-f51847/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260527T172954616103Z-f51847",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.5808,
      "evidence_path": "artifacts/runs/claim-20260527T172954658524Z-db6f7b/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260527T172954658524Z-db6f7b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.7805,
      "evidence_path": "artifacts/runs/claim-20260527T172954694513Z-d5f08d/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260527T172954694513Z-d5f08d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.8237,
      "evidence_path": "artifacts/runs/claim-20260527T172954734215Z-1789e6/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260527T172954734215Z-1789e6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.7408,
      "evidence_path": "artifacts/runs/claim-20260527T172954777234Z-43dca8/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260527T172954777234Z-43dca8",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.4669,
      "evidence_path": "artifacts/runs/claim-20260527T172954814716Z-40112f/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260527T172954814716Z-40112f",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.1416,
      "evidence_path": "artifacts/runs/claim-20260527T172954850036Z-71ea33/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260527T172954850036Z-71ea33",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.4953,
      "evidence_path": "artifacts/runs/claim-20260527T172954883791Z-43fe11/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260527T172954883791Z-43fe11",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.5563,
      "evidence_path": "artifacts/runs/claim-20260527T172954919447Z-13d282/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260527T172954919447Z-13d282",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.5125,
      "evidence_path": "artifacts/runs/claim-20260527T172954953503Z-4ad727/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260527T172954953503Z-4ad727",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.6575,
      "evidence_path": "artifacts/runs/claim-20260527T172954988700Z-b2c4ed/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260527T172954988700Z-b2c4ed",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 47.3869,
      "evidence_path": "artifacts/runs/claim-20260527T172955032653Z-2fc173/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260527T172955032653Z-2fc173",
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
