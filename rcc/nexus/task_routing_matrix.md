# Task Routing Matrix

Current contract: **TAU-SCALING-SA v0.8.6a - README Render Spacing Polish**

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
| Sensitivity sweep patch | inner | validation | tau | `configs/seeds/sweeps/`, gate formulas, benchmark atlas | release validator + sensitivity sweep report | `reports/sensitivity/latest_sensitivity_sweep.md` |
| Gate interaction patch | inner | validation | tau | `configs/seeds/interactions/`, gate formulas, classifier, benchmark atlas | release validator + interaction matrix report | `reports/interactions/latest_gate_interaction_matrix.md` |
| Explanation card patch | outer | evidence | validation | `reports/explanations/`, interaction/sensitivity reports, classifier | release validator + explanation report | `reports/explanations/latest_threshold_explanation_cards.md` |
| Pair policy patch | outer | validation | governance | `reports/policy/`, explanation cards, interaction matrix | release validator + policy review report | `reports/policy/latest_pair_policy_review.md` |
| Nexus feedback patch | outer | drift | agent | `scripts/feedback/`, `reports/nexus_feedback/`, latest reports | release validator + feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |
| Feedback health ordering repair | outer | drift | agent | validation reports, feedback report, AGENTS ordering rule | validators before feedback + feedback + validators after | `reports/nexus_feedback/latest_nexus_feedback.md` |
| Feedback health schema alignment | outer | drift | agent | feedback runner, release report, sensitivity report | feedback health score 1.0 + validators | `reports/nexus_feedback/latest_nexus_feedback.md` |
| Feedback function-block repair | outer | drift | agent | feedback runner function body | compile + function-body assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |
| Feedback chart-path health repair | outer | drift | agent | feedback runner + sensitivity chart_paths | compile + chart-path assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |
| Pair policy dry-run patch | outer | validation | governance | pair policy review + dry-run report | dry-run report + charts + release validator | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |
| Policy impact patch | outer | validation | governance | dry-run report + impact cards | impact report + charts + release validator | `reports/policy_impact/latest_policy_impact_cards.md` |
| Policy decision patch | outer | validation | governance | impact cards + decision record | decision record + charts + release validator | `reports/policy_decision/latest_policy_decision_record.md` |
| Regression review patch | outer | validation | governance | decision record + dry-run report | regression report + charts + release validator | `reports/regression_review/latest_regression_over_penalty_review.md` |
| Enforcement readiness patch | outer | validation | governance | regression review + readiness gate | readiness report + charts + release validator | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |
| Nexus target refresh patch | outer | drift | feedback | Nexus feedback + readiness gate | target-refresh report + charts + release validator | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |
| Over-penalty cause patch | outer | validation | governance | readiness gate + regression review | cause cards + charts + release validator | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` |
| Remediation plan patch | outer | validation | governance | cause cards + remediation tasks | remediation report + charts + release validator | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` |
| Support-aware negative-control patch | outer | validation | governance | remediation tasks + cause cards | negative-control report + charts + release validator | `reports/negative_controls/latest_support_aware_negative_controls.md` |
| Disabled calibration plan patch | outer | validation | governance | negative controls + candidate thresholds | calibration plan + charts + release validator | `reports/calibration_plan/latest_disabled_calibration_plan.md` |
| Calibration counterfactual patch | outer | validation | governance | calibration plan + negative controls | counterfactual report + charts + release validator | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` |
| Counterfactual decision patch | outer | validation | governance | calibration counterfactuals + decision criteria | decision record + charts + release validator | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` |
| Review package patch | outer | evidence | governance | v0.5.2-v0.5.7 evidence surfaces | review package + charts + release validator | `reports/review_package/latest_review_package.md` |
| Review signoff patch | outer | validation | governance | review package + signoff checks | signoff gate + charts + release validator | `reports/review_signoff/latest_review_signoff_gate.md` |
| Candidate branch gate patch | outer | governance | review | signoff gate + human approval requirement | candidate branch gate + charts + release validator | `reports/candidate_branch/latest_candidate_branch_gate.md` |
| Candidate replay harness patch | outer | validation | governance | candidate gate + signoff | replay harness + charts + release validator | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` |
| Human approval template patch | outer | governance | review | replay harness + candidate gate | approval template + charts + release validator | `reports/human_approval/latest_human_approval_template_report.md` |
| Human approval validator patch | outer | validation | governance | approval artifact + replay harness | approval validator + charts + release validator | `reports/approval_validator/latest_human_approval_validator.md` |
| Approval-gated replay patch | outer | validation | governance | approval validator + replay harness | blocked replay dry-run + charts + release validator | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` |
| Approval fixture patch | outer | validation | governance | approval template + approval validator | fixture validator + charts + release validator | `reports/approval_fixtures/latest_approval_fixture_validator.md` |
| Live approval handoff patch | outer | validation | governance | approval fixtures + live approval directory | handoff check + charts + release validator | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` |
| Replay executor patch | outer | execution-boundary | governance | live approval handoff | executor blocked report + charts + release validator | `reports/replay_executor/latest_approval_gated_replay_executor.md` |
| Blocked continuity patch | outer | evidence | governance | replay executor + live approval handoff | continuity ledger + charts + release validator | `reports/blocked_continuity/latest_blocked_state_continuity.md` |
| Blocked trend patch | outer | analysis | governance | blocked continuity ledger | trend review + charts + release validator | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` |
| Approval corridor patch | outer | milestone | governance | v0.6 approval reports | corridor manifest + charts + release validator | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` |
| Tau mechanics review patch | inner | analysis | runtime | core runtime + seeds + reports | mechanics scan + charts + release validator | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` |
| Tau vector semantics patch | inner | analysis | runtime | core runtime + seeds | semantics ledger + charts + release validator | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` |
| Gate algebra patch | inner | analysis | runtime | core gates + seeds + tau semantics | gate algebra map + charts + release validator | `reports/gate_algebra/latest_gate_algebra_map.md` |
| TSEK threshold review patch | inner | analysis | classifier | classifier + gate algebra + reports | threshold review + charts + release validator | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` |
| TSEK boundary card patch | inner | explanation | classifier | threshold review + TSEK classes | boundary cards + charts + release validator | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` |
| Penalty controls patch | inner | analysis | classifier | TSEK boundary cards + threshold review | report-only controls + charts + release validator | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` |
| Threshold sensitivity patch | inner | dry-run | classifier | penalty controls + threshold review | report-only threshold sensitivity + charts + release validator | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` |
| Threshold decision patch | inner | decision | classifier | threshold sensitivity dry-run | non-mutating decision record + charts + release validator | `reports/threshold_decision_record/latest_threshold_decision_record.md` |
| Threshold governance summary patch | inner | milestone | classifier | v0.7 Tau mechanics reports | milestone summary + charts + release validator | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` |
| Stable threshold governance patch | inner | milestone | classifier | v0.7 reports + threshold decision | stable milestone + charts + release validator | `reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md` |
| Public claim replay patch | outer | evidence | release | source boundary docs, `configs/seeds/public_claims/` | release validator + claim replay report | `reports/public_claims/latest_claim_replay_report.md` |
| Agent contract patch | center | agent | rcc | `AGENTS.md`, route map, task matrix, README | README audit + release validator | `reports/agent/latest_agent_contract_sync.md` |
| Reflection patch | center | drift | documentation | `docs/reflection/`, `reports/reflection/`, README, AGENTS | README audit + release validator | `reports/reflection/latest_system_reflection.md` |

## Non-Claim Lock

Task routing improves repository orientation. It does not prove code correctness, patch safety, AI understanding, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling truth.
