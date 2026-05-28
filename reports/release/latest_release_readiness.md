# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T10:01:51.915560+00:00`

Passed: `true`
Step count: `9`
Step failures: `0`
Findings: `3`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `79.153` |
| `import_runtime` | `true` | `0` | `107.746` |
| `rcc_nexus_check` | `true` | `0` | `70.467` |
| `readme_mini_repo_audit` | `true` | `0` | `94.576` |
| `architecture_contract_validation` | `true` | `0` | `68.415` |
| `unit_tests` | `true` | `0` | `227.35` |
| `benchmark_harness` | `true` | `0` | `554.137` |
| `baseline_claim` | `true` | `0` | `157.308` |
| `promotion_path_claim` | `true` | `0` | `167.106` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100151664187Z-7a599b",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100151664187Z-7a599b\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T100151664187Z-7a599b"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100151827983Z-4c92dc",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T100151827983Z-4c92dc\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T100151827983Z-4c92dc"
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
      "max_elapsed_ms": 40.9074,
      "mean_elapsed_ms": 35.7065,
      "min_elapsed_ms": 33.5018,
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
      "max_elapsed_ms": 38.7156,
      "mean_elapsed_ms": 36.0292,
      "min_elapsed_ms": 33.7031,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T10:01:51.106863+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 40.9074,
  "mean_elapsed_ms": 35.8679,
  "median_elapsed_ms": 35.228,
  "min_elapsed_ms": 33.5018,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 40.9074,
      "evidence_path": "artifacts/runs/claim-20260528T100151106863Z-6bc998/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T100151106863Z-6bc998",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 33.5018,
      "evidence_path": "artifacts/runs/claim-20260528T100151148670Z-812c83/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T100151148670Z-812c83",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.6077,
      "evidence_path": "artifacts/runs/claim-20260528T100151181432Z-4b8b88/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T100151181432Z-4b8b88",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.3943,
      "evidence_path": "artifacts/runs/claim-20260528T100151216561Z-71d610/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T100151216561Z-71d610",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 34.7659,
      "evidence_path": "artifacts/runs/claim-20260528T100151252493Z-d6d86b/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T100151252493Z-d6d86b",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 35.0617,
      "evidence_path": "artifacts/runs/claim-20260528T100151287382Z-c424c4/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T100151287382Z-c424c4",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 38.7156,
      "evidence_path": "artifacts/runs/claim-20260528T100151322467Z-779af1/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T100151322467Z-779af1",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 33.7031,
      "evidence_path": "artifacts/runs/claim-20260528T100151361800Z-799139/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T100151361800Z-799139",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.9175,
      "evidence_path": "artifacts/runs/claim-20260528T100151395254Z-5bfecb/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T100151395254Z-5bfecb",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 37.6117,
      "evidence_path": "artifacts/runs/claim-20260528T100151431147Z-8a585d/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T100151431147Z-8a585d",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 35.8676,
      "evidence_path": "artifacts/runs/claim-20260528T100151469515Z-518ac7/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T100151469515Z-518ac7",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 34.36,
      "evidence_path": "artifacts/runs/claim-20260528T100151505223Z-5016c9/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T100151505223Z-5016c9",
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
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_tilde: \xc3 |
| warning | `possible_mojibake` | `README.md` | latin1_mojibake_A_circumflex: \xc2 |
| warning | `possible_mojibake` | `README.md` | utf8_quote_dash_mojibake: \xe2\u20ac |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
