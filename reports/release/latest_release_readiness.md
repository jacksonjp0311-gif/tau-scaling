# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T16:06:36.253307+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `0`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `76.391` |
| `import_runtime` | `true` | `0` | `118.568` |
| `rcc_nexus_check` | `true` | `0` | `85.229` |
| `readme_mini_repo_audit` | `true` | `0` | `95.218` |
| `architecture_contract_validation` | `true` | `0` | `72.579` |
| `unit_tests` | `true` | `0` | `232.046` |
| `benchmark_harness` | `true` | `0` | `603.239` |
| `baseline_claim` | `true` | `0` | `182.03` |
| `promotion_path_claim` | `true` | `0` | `168.78` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T160635996119Z-15198d",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T160635996119Z-15198d\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T160635996119Z-15198d"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T160636167955Z-a82d95",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T160636167955Z-a82d95\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T160636167955Z-a82d95"
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
      "max_elapsed_ms": 45.4461,
      "mean_elapsed_ms": 39.8574,
      "min_elapsed_ms": 36.8223,
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
      "max_elapsed_ms": 46.8136,
      "mean_elapsed_ms": 39.6307,
      "min_elapsed_ms": 36.6087,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T16:06:35.367664+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 46.8136,
  "mean_elapsed_ms": 39.7441,
  "median_elapsed_ms": 39.3683,
  "min_elapsed_ms": 36.6087,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 45.4461,
      "evidence_path": "artifacts/runs/claim-20260528T160635368670Z-0183cc/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T160635368670Z-0183cc",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.5478,
      "evidence_path": "artifacts/runs/claim-20260528T160635413320Z-4bdee3/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T160635413320Z-4bdee3",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.3045,
      "evidence_path": "artifacts/runs/claim-20260528T160635454345Z-5a5f27/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T160635454345Z-5a5f27",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 39.7947,
      "evidence_path": "artifacts/runs/claim-20260528T160635493956Z-b169f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T160635493956Z-b169f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 36.8223,
      "evidence_path": "artifacts/runs/claim-20260528T160635533891Z-702b58/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T160635533891Z-702b58",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 37.229,
      "evidence_path": "artifacts/runs/claim-20260528T160635570773Z-d43c34/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T160635570773Z-d43c34",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 39.4321,
      "evidence_path": "artifacts/runs/claim-20260528T160635608812Z-4119d4/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T160635608812Z-4119d4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.6087,
      "evidence_path": "artifacts/runs/claim-20260528T160635648121Z-d3e2b4/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T160635648121Z-d3e2b4",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.825,
      "evidence_path": "artifacts/runs/claim-20260528T160635685243Z-1c1a43/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T160635685243Z-1c1a43",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 36.6842,
      "evidence_path": "artifacts/runs/claim-20260528T160635722215Z-c4bd9b/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T160635722215Z-c4bd9b",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.4208,
      "evidence_path": "artifacts/runs/claim-20260528T160635759780Z-e8e91d/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T160635759780Z-e8e91d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 46.8136,
      "evidence_path": "artifacts/runs/claim-20260528T160635800127Z-5a1013/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T160635800127Z-5a1013",
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
