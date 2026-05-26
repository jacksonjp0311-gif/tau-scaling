# Tau Scaling Unified Release Readiness

Generated: `2026-05-26T14:19:41.869618+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `75.258` |
| `import_runtime` | `true` | `0` | `106.746` |
| `rcc_nexus_check` | `true` | `0` | `82.387` |
| `readme_mini_repo_audit` | `true` | `0` | `102.767` |
| `architecture_contract_validation` | `true` | `0` | `72.189` |
| `unit_tests` | `true` | `0` | `236.644` |
| `benchmark_harness` | `true` | `0` | `609.683` |
| `baseline_claim` | `true` | `0` | `181.288` |
| `promotion_path_claim` | `true` | `0` | `182.26` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T141941602647Z-26bd10",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T141941602647Z-26bd10\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260526T141941602647Z-26bd10"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T141941765206Z-1c3aee",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260526T141941765206Z-1c3aee\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260526T141941765206Z-1c3aee"
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
      "max_elapsed_ms": 47.1047,
      "mean_elapsed_ms": 38.9275,
      "min_elapsed_ms": 35.135,
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
      "max_elapsed_ms": 40.1373,
      "mean_elapsed_ms": 37.3677,
      "min_elapsed_ms": 34.6889,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-26T14:19:40.991122+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 47.1047,
  "mean_elapsed_ms": 38.1476,
  "median_elapsed_ms": 37.7103,
  "min_elapsed_ms": 34.6889,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.1047,
      "evidence_path": "artifacts/runs/claim-20260526T141940992122Z-9ace4c/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260526T141940992122Z-9ace4c",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.5726,
      "evidence_path": "artifacts/runs/claim-20260526T141941039337Z-4056ea/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260526T141941039337Z-4056ea",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.8603,
      "evidence_path": "artifacts/runs/claim-20260526T141941078556Z-69e08b/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260526T141941078556Z-69e08b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.135,
      "evidence_path": "artifacts/runs/claim-20260526T141941114828Z-8d5eb6/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260526T141941114828Z-8d5eb6",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.2814,
      "evidence_path": "artifacts/runs/claim-20260526T141941149762Z-424b86/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260526T141941149762Z-424b86",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 38.611,
      "evidence_path": "artifacts/runs/claim-20260526T141941187398Z-1fb73d/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260526T141941187398Z-1fb73d",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.3621,
      "evidence_path": "artifacts/runs/claim-20260526T141941226951Z-fa49d6/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260526T141941226951Z-fa49d6",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.1524,
      "evidence_path": "artifacts/runs/claim-20260526T141941265876Z-ea4aa2/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260526T141941265876Z-ea4aa2",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.1393,
      "evidence_path": "artifacts/runs/claim-20260526T141941302765Z-0e2816/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260526T141941302765Z-0e2816",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.7262,
      "evidence_path": "artifacts/runs/claim-20260526T141941341289Z-981cd7/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260526T141941341289Z-981cd7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.6889,
      "evidence_path": "artifacts/runs/claim-20260526T141941377107Z-dda662/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260526T141941377107Z-dda662",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.1373,
      "evidence_path": "artifacts/runs/claim-20260526T141941412021Z-33e180/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260526T141941412021Z-33e180",
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
