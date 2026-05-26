# Task Routing Matrix

Current contract: **TAU-SCALING-SA v0.3.3e — Agent Contract Geometry Sync**

## Geometry Route

```text
intent -> shell -> meridian -> sector -> files -> validation -> evidence -> lesson
```

| Task | Shell | Meridian | Sector | Read first | Validate | Evidence output |
|---|---|---|---|---|---|---|
| Runtime patch | middle | runtime | core | `src/tau_scaling/README.md`, `tests/` | `python scripts/release/validate_release.py` | `reports/release/latest_release_readiness.md` |
| Claim classifier patch | inner | validation | runtime | `src/tau_scaling/claims/README.md`, claim cards, evidence | release validator + baseline/promotion claims | `artifacts/runs/latest/evidence_package.json` |
| Gate logic patch | inner | validation | tau | `src/tau_scaling/gates/README.md`, synthetic seeds | release validator + gate-specific tests | `reports/gates/` |
| RCC docs patch | center | agent | rcc | `README.md`, `docs/context/`, `rcc/nexus/` | `python scripts/rcc/check_rcc_nexus.py` + release validator | `reports/rcc_nexus/latest_rcc_nexus_check.md` |
| README / mini README patch | center | documentation | agent | root README, target mini README, route map | `python scripts/rcc/audit_readme_surface.py` + release validator | `reports/readme/latest_readme_mini_repo_audit.md` |
| Architecture docs patch | center | source | architecture | `docs/software_architecture/`, `docs/architecture/` | architecture validator + release validator | `reports/architecture/latest_architecture_contract_validation.md` |
| Directory structure patch | center | drift | rcc | Full Directory Box, context indexes, affected mini READMEs | README audit + RCC-N + release validator | README + context index diffs |
| Release / benchmark patch | outer | release | evidence | `releases/`, `docs/benchmarks/`, `reports/benchmarks/`, `reports/release/` | `python scripts/release/validate_release.py` | `reports/release/latest_release_readiness.md` |
| Synthetic gate test patch | inner | validation | tau | `configs/seeds/tests/`, `src/tau_scaling/gates/`, `tests/` | release validator + synthetic gate report | `reports/gates/latest_synthetic_gate_report.md` |
| Public claim replay patch | outer | evidence | release | source boundary docs, `configs/seeds/public_claims/` | release validator + claim replay report | `reports/public_claims/latest_claim_replay_report.md` |
| Agent contract patch | center | agent | rcc | `AGENTS.md`, route map, task matrix, README | README audit + release validator | `reports/agent/latest_agent_contract_sync.md` |

## Non-Claim Lock

Task routing improves repository orientation. It does not prove code correctness, patch safety, AI understanding, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling truth.
