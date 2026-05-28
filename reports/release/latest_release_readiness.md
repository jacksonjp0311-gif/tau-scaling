# Tau Scaling Unified Release Readiness

Generated: `2026-05-28T09:50:54.100959+00:00`

Passed: `false`
Step count: `9`
Step failures: `1`
Findings: `3`

## Step Summary

| Step | Passed | Exit | Elapsed ms |
|---|---:|---:|---:|
| `compile_runtime` | `true` | `0` | `79.974` |
| `import_runtime` | `true` | `0` | `159.333` |
| `rcc_nexus_check` | `true` | `0` | `93.752` |
| `readme_mini_repo_audit` | `false` | `1` | `113.132` |
| `architecture_contract_validation` | `true` | `0` | `110.683` |
| `unit_tests` | `true` | `0` | `519.914` |
| `benchmark_harness` | `true` | `0` | `823.892` |
| `baseline_claim` | `true` | `0` | `190.481` |
| `promotion_path_claim` | `true` | `0` | `334.104` |

## Claim Summary

### baseline_claim

```json
{
  "A_TSEK": 0.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T095053624283Z-1d4bed",
  "class": "TSEK-C",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T095053624283Z-1d4bed\\evidence_package.json",
  "findings": 1,
  "run_id": "claim-20260528T095053624283Z-1d4bed"
}
```

### promotion_path_claim

```json
{
  "A_TSEK": 1.0,
  "artifacts": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T095053824460Z-d9a8a8",
  "class": "TSEK-B",
  "evidence": "C:\\Users\\jacks\\OneDrive\\Desktop\\tau-scaling\\artifacts\\runs\\claim-20260528T095053824460Z-d9a8a8\\evidence_package.json",
  "findings": 0,
  "run_id": "claim-20260528T095053824460Z-d9a8a8"
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
      "max_elapsed_ms": 53.3634,
      "mean_elapsed_ms": 45.3826,
      "min_elapsed_ms": 42.271,
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
      "max_elapsed_ms": 179.1206,
      "mean_elapsed_ms": 67.5139,
      "min_elapsed_ms": 40.5182,
      "runs": 6
    }
  },
  "class_counts": {
    "TSEK-B": 6,
    "TSEK-C": 6
  },
  "collision_proof_run_identity_passed": true,
  "duplicate_run_ids": [],
  "generated_at": "2026-05-28T09:50:52.790186+00:00",
  "iterations_per_seed": 6,
  "max_elapsed_ms": 179.1206,
  "mean_elapsed_ms": 56.4482,
  "median_elapsed_ms": 43.4829,
  "min_elapsed_ms": 40.5182,
  "results": [
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 53.3634,
      "evidence_path": "artifacts/runs/claim-20260528T095052790186Z-6d01f5/evidence_package.json",
      "findings_count": 1,
      "iteration": 1,
      "run_id": "claim-20260528T095052790186Z-6d01f5",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 43.2563,
      "evidence_path": "artifacts/runs/claim-20260528T095052844220Z-93cabf/evidence_package.json",
      "findings_count": 1,
      "iteration": 2,
      "run_id": "claim-20260528T095052844220Z-93cabf",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.5813,
      "evidence_path": "artifacts/runs/claim-20260528T095052887666Z-176243/evidence_package.json",
      "findings_count": 1,
      "iteration": 3,
      "run_id": "claim-20260528T095052887666Z-176243",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.271,
      "evidence_path": "artifacts/runs/claim-20260528T095052930525Z-1722da/evidence_package.json",
      "findings_count": 1,
      "iteration": 4,
      "run_id": "claim-20260528T095052930525Z-1722da",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 42.8396,
      "evidence_path": "artifacts/runs/claim-20260528T095052973025Z-7a58d0/evidence_package.json",
      "findings_count": 1,
      "iteration": 5,
      "run_id": "claim-20260528T095052973025Z-7a58d0",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 0.0,
      "classification": "TSEK-C",
      "elapsed_ms": 47.9837,
      "evidence_path": "artifacts/runs/claim-20260528T095053015771Z-d35c81/evidence_package.json",
      "findings_count": 1,
      "iteration": 6,
      "run_id": "claim-20260528T095053015771Z-d35c81",
      "seed": "configs/seeds/logicfolding_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 51.7302,
      "evidence_path": "artifacts/runs/claim-20260528T095053064614Z-60c967/evidence_package.json",
      "findings_count": 0,
      "iteration": 1,
      "run_id": "claim-20260528T095053064614Z-60c967",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 47.8845,
      "evidence_path": "artifacts/runs/claim-20260528T095053117230Z-1af226/evidence_package.json",
      "findings_count": 0,
      "iteration": 2,
      "run_id": "claim-20260528T095053117230Z-1af226",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 43.7095,
      "evidence_path": "artifacts/runs/claim-20260528T095053165050Z-44bf80/evidence_package.json",
      "findings_count": 0,
      "iteration": 3,
      "run_id": "claim-20260528T095053165050Z-44bf80",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 42.1203,
      "evidence_path": "artifacts/runs/claim-20260528T095053208937Z-7386af/evidence_package.json",
      "findings_count": 0,
      "iteration": 4,
      "run_id": "claim-20260528T095053208937Z-7386af",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 40.5182,
      "evidence_path": "artifacts/runs/claim-20260528T095053251420Z-0b2875/evidence_package.json",
      "findings_count": 0,
      "iteration": 5,
      "run_id": "claim-20260528T095053251420Z-0b2875",
      "seed": "configs/seeds/logicfolding_promotion_path_claim_card.json"
    },
    {
      "A_TSEK": 1.0,
      "classification": "TSEK-B",
      "elapsed_ms": 179.1206,
      "evidence_path": "artifacts/runs/claim-20260528T095053291905Z-3804c3/evidence_package.json",
      "findings_count": 0,
      "iteration": 6,
      "run_id": "claim-20260528T095053291905Z-3804c3",
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
| warning | `possible_mojibake` | `README.md` | utf8_quote_dash_mojibake: \xe2\u20ac |
| error | `readme_audit_reported_failed` | `reports/readme/latest_readme_mini_repo_audit.json` |  |

## Non-Claim Lock

Release readiness validates repository/runtime hygiene only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.
