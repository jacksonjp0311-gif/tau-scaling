from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "readme_render_alignment"
BACKUP_DIR = REPORT_DIR / "v0_8_3b" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_3b_{stamp}.bak", read(path))

def normalize_mojibake(text: str) -> str:
    text = re.sub(r"^# Tau Scaling .+ Evidence-Gated Tau-Claim Runtime", "# Tau Scaling - Evidence-Gated Tau-Claim Runtime", text, flags=re.M)
    replacements = {
        "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â": "-",
        "Ã¢â‚¬â€": "-",
        "Ã¢â‚¬â€œ": "-",
        "Ã¢â‚¬Ëœ": "'",
        "Ã¢â‚¬â„¢": "'",
        "Ã¢â‚¬Å“": '"',
        "Ã¢â‚¬Â": '"',
        "Ãƒ": "",
        "Â": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"cont``\s*ext", "context", text)
    text = re.sub(r"n``\s*ext", "next", text)
    text = re.sub(r"t``\s*ext", "text", text)
    text = re.sub(r"T``\s*ext", "Text", text)

    text = re.sub(r"```t``\s*ext", "```text", text)
    text = re.sub(r"`\s*``\s*ext", "```text", text)
    text = re.sub(r"`\s*ext", "```text", text)
    text = re.sub(r"`text", "```text", text)
    text = re.sub(r"(?m)^`$", "```", text)

    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    if EXACT_AI_RULE not in text:
        anchor_block = f"""

{EXACT_AI_RULE}

This exact heading uses a Unicode em dash (U+2014) because `scripts/rcc/audit_readme_surface.py` checks this anchor literally.

This repository uses RCC-N style navigation. Repository structure is part of the public interface.

Any AI or human patch that adds, removes, renames, or repurposes a folder must update these surfaces in the same commit:

1. The root README Full Directory Box.
2. The affected folder-level mini `README.md`.
3. `docs/context/repository_context_index.json` if route meaning changes.
4. `docs/context/rcc_nexus_index.json` if Nexus position changes.
5. `rcc/nexus/route_map.json` if task routing changes.
6. Relevant validation reports after rerunning checks.

Non-claim lock: directory navigation is not correctness, but stale navigation is repository drift.

"""
        text = text.replace("## Full Directory Box", anchor_block + "## Full Directory Box")
    return text

def ensure_showcase(text: str) -> str:
    showcase = """## Showcase Tau Findings

This repository has moved from governance construction into **Tau Scaling research instrumentation**.

Current public finding:

```text
Tau Scaling can be studied as an evidence-gated claim system.
Public claims can be separated into methodology, reported metrics, roadmap projections, topology arguments, and independent evidence.
The current public claim set is mostly TSEK-C, with roadmap/system claims in TSEK-D.
No public claim currently reaches TSEK-A or TSEK-B without additional disclosed evidence.
```

Current public Tau claim ledger:

```text
TSEK-A: 0
TSEK-B: 0
TSEK-C: 6
TSEK-D: 2
TSEK-E: 0
Average missing evidence gates: 6.375
```

LogicFolding sweep result:

```text
Aggressive best-case prior: 100.0% joint pass.
Conservative public prior: 0.0% joint pass.
Interpretation: LogicFolding is conditionally plausible, not automatically validated.
```

Research boundary:

```text
The current repo can test plausibility and evidence sufficiency.
It does not validate Huawei silicon, products, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
```

Primary evidence surfaces:

```text
claims/public_tau/
reports/tau_claim_ledger/latest_tau_public_claim_ledger.md
reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md
visuals/logicfolding_plausibility/v0_8_3/
```

"""
    if "## Showcase Tau Findings" not in text:
        if "## Tau Doctrine Alignment" in text:
            text = text.replace("## Tau Doctrine Alignment", showcase + "## Tau Doctrine Alignment", 1)
        elif "## Human Director Box" in text:
            text = text.replace("## Human Director Box", showcase + "## Human Director Box", 1)
        else:
            text = text + "\n\n" + showcase
    return text

def ensure_logicfolding_section(text: str) -> str:
    section = """## LogicFolding Plausibility Sweep v0.8.3

This layer begins proof/falsification work on the core LogicFolding claim by testing the TSEK survivability inequality under synthetic priors.

```text
rho_c * E[delta_tau_wire] >
E[tau_vertical] + tau_route + tau_sync + tau_variation + tau_closure

gamma_tau_ETP > 1
```

Primary outputs:

```text
reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md
reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.json
visuals/logicfolding_plausibility/v0_8_3/
```

Research interpretation:

```text
LogicFolding is conditionally plausible when critical-path coverage and wire-delay savings are high enough to dominate vertical, routing, synchronization, variation, and closure costs, and when energy/thermal/PDN-normalized tau gain remains above one.
```

Boundary: synthetic plausibility testing only. It does not validate Huawei silicon, products, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.

"""
    if "## LogicFolding Plausibility Sweep v0.8.3" not in text:
        if "## Showcase Tau Findings" in text:
            text = text.replace("## Showcase Tau Findings", section + "## Showcase Tau Findings", 1)
        else:
            text = text + "\n\n" + section
    return text

def normalize_metrics(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.3b - README Render and Alignment Repair**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.3a - README UTF-8 Anchor Repair after LogicFolding Sweep**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.3b |", text)
    text = re.sub(r"\| Release warning findings \| .*?\|", "| Release warning findings | non-blocking / tracked by release readiness report |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.3b-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.3b |", text)

    rows = [
        "| Public Tau claim ledger | `reports/tau_claim_ledger/latest_tau_public_claim_ledger.md` |",
        "| LogicFolding plausibility sweep | `reports/logicfolding_plausibility/latest_logicfolding_plausibility_sweep.md` |",
        "| LogicFolding plausibility charts | `visuals/logicfolding_plausibility/v0_8_3/` |",
        "| README render alignment repair | `reports/readme_render_alignment/latest_readme_render_alignment_repair.md` |",
    ]
    for row in rows:
        if row not in text and "| Current Public Metrics" in text:
            text = text.replace("| Claim status | local runtime evidence + benchmark observability only |", row + "\n| Claim status | local runtime evidence + benchmark observability only |")
    return text

def normalize_lessons(text: str) -> str:
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text

    block = text[start:end]
    full_rows = re.findall(r"^(\| L-(\d{3}) \|.*?\|)$", block, flags=re.M)
    seen = {}
    for row, num in full_rows:
        seen[int(num)] = row

    seen[64] = "| L-064 | v0.8.2 created the public Tau claim ledger, but README audit failed because the AI Rule em-dash anchor was mojibake-corrupted. | Encoding drift can make a semantically correct README fail exact audit anchors. | Audit-visible headings must be repaired with exact Unicode anchors, and high-value findings should be showcased near the top of the README. |"
    seen[65] = "| L-065 | v0.8.3 LogicFolding sweep succeeded, but README audit failed again on the em-dash AI Rule anchor. | Windows PowerShell read/write paths can reintroduce mojibake into UTF-8 README surfaces. | README repairs that must preserve Unicode audit anchors must use explicit UTF-8 patchers, then rerun release validator before commit. |"
    seen[66] = "| L-066 | v0.8.3a passed all validators but README rendering still showed mojibake and broken code fences. | Passing exact anchors is not the same as human-readable public rendering. | After validator repair, inspect rendered README for mojibake, broken fences, duplicate lesson headers, stale metrics, and directory-box drift. |"

    sorted_rows = [seen[k] for k in sorted(seen)]
    new_block = "### Current Lessons\n\n| Lesson ID | Failure observed | Root cause | Permanent rule |\n|---|---|---|---|\n" + "\n".join(sorted_rows) + "\n\n"
    return text[:start] + new_block + text[end:]

def normalize_directory_box(text: str) -> str:
    canonical = """## Full Directory Box

This box is a durable public repository map. Update it in the same commit whenever top-level folders or durable subfolders are added, removed, renamed, or repurposed. Generated timestamped runtime folders under `artifacts/runs/` are intentionally excluded.

```text
tau-scaling/
  .github/
    workflows/
  AGENTS.md
  LICENSE
  pyproject.toml
  README.md
  README_5_MINUTES.md
  README_90_SECONDS.md
  artifacts/
    dashboards/
    evidence_packages/
    ledgers/
    reports/
    runs/
      latest/
    visuals/
  claims/
    public_tau/
  configs/
    seeds/
  docs/
    architecture/
    architecture_changes/
    benchmarks/
    context/
      drift/
    feedback/
    future_architecture/
    injected_theory/
    injections/
    protocols/
    public_release/
    reflection/
    release_notes/
    software_architecture/
    theory/
  examples/
  outputs/
    evidence/
    ledger/
    logs/
    plots/
    reports/
    state/
  rcc/
    nexus/
  releases/
  reports/
    architecture/
    benchmarks/
    logicfolding_plausibility/
    readme_anchor_repair/
    readme_render_alignment/
    readme_showcase/
    release/
    tau_claim_ledger/
    stable_tau_threshold_governance/
    threshold_governance_summary/
    threshold_decision_record/
    threshold_sensitivity_dry_run/
    penalty_controls/
    tsek_boundary_cards/
    tsek_threshold_review/
    gate_algebra/
    tau_vector_semantics/
    tau_mechanics_review/
    approval_corridor/
    blocked_trend_review/
    blocked_continuity/
    replay_executor/
    live_approval_handoff/
    approval_fixtures/
    approval_gated_replay/
    approval_validator/
    human_approval/
    candidate_replay/
    candidate_branch/
    review_signoff/
    review_package/
    counterfactual_decision/
    calibration_counterfactuals/
    calibration_plan/
    negative_controls/
    remediation_plan/
    over_penalty_causes/
    nexus_target_refresh/
    enforcement_readiness/
    regression_review/
    policy_dry_run/
    policy_impact/
    policy_decision/
    policy/
    explanations/
    interactions/
    rcc_nexus/
    reflection/
    runtime/
    status/
  scripts/
    benchmarks/
    feedback/
    maintenance/
    rcc/
    reflection/
    release/
    validation/
  src/
    tau_scaling/
      claims/
      core/
      evidence/
      gates/
      schemas/
      simulation/
      tau/
      utils/
  tests/
  visuals/
    logicfolding_plausibility/
    tau_claim_ledger/
    stable_tau_threshold_governance/
    threshold_governance_summary/
    threshold_decision_record/
    threshold_sensitivity_dry_run/
    penalty_controls/
    tsek_boundary_cards/
    tsek_threshold_review/
    gate_algebra/
    tau_vector_semantics/
    tau_mechanics_review/
    approval_corridor/
    blocked_trend_review/
    blocked_continuity/
    replay_executor/
    live_approval_handoff/
    approval_fixtures/
    approval_gated_replay/
    approval_validator/
    human_approval/
    candidate_replay/
    candidate_branch/
    review_signoff/
    review_package/
    counterfactual_decision/
    calibration_counterfactuals/
    calibration_plan/
    negative_controls/
    remediation_plan/
    over_penalty_causes/
    nexus_target_refresh/
    enforcement_readiness/
    regression_review/
    policy_dry_run/
    policy_impact/
    policy_decision/
    policy/
    explanations/
    interactions/
    reflection/
    rcc_nexus/
    tau_scaling/
```

"""
    pattern = r"## Full Directory Box.*?```(?:text)?\s*tau-scaling/.*?```\s*\n"
    if re.search(pattern, text, flags=re.S):
        text = re.sub(pattern, canonical, text, count=1, flags=re.S)
    else:
        text = text.replace("## Unified Release Readiness Layer", canonical + "## Unified Release Readiness Layer", 1)
    return text

def ensure_next(text: str) -> str:
    next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**

Recommended goals:

- Convert public Tau claim classes into explicit evidence sufficiency requirements.
- Define what evidence would promote TSEK-C to TSEK-B and TSEK-B to TSEK-A.
- Preserve downgrade discipline and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
"""
    if "## Next Recommended Version" in text:
        text = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + next_section
    return text

def main() -> None:
    backup(README)
    text = read(README)

    text = normalize_mojibake(text)
    text = ensure_showcase(text)
    text = ensure_logicfolding_section(text)
    text = normalize_metrics(text)
    text = normalize_lessons(text)
    text = normalize_directory_box(text)
    text = ensure_next(text)

    text = text.replace("docs/cont``\text", "docs/context")
    text = text.replace("cont``\text", "context")
    text = text.replace("n``\text", "next")
    text = text.replace("t``\text", "text")
    text = re.sub(r"\n{3,}", "\n\n", text)

    write(README, text)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "tau-scaling-readme-render-alignment-repair-v0.8.3b",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.3b - README Render and Alignment Repair",
        "repairs": [
            "repaired mojibake in title and text",
            "repaired broken fenced code blocks",
            "normalized context/next/text corruption",
            "deduplicated AI Failure Learning Ledger headers",
            "added L-066 render-inspection lesson",
            "normalized Full Directory Box",
            "surfaced LogicFolding and Tau findings near top",
            "preserved exact audited AI Rule em-dash heading",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "README render/alignment repair improves public readability and repository navigation only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    write(REPORT_DIR / "readme_render_alignment_repair_v0_8_3b.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_readme_render_alignment_repair.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# README Render and Alignment Repair v0.8.3b\n\n"
    md += "## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "readme_render_alignment_repair_v0_8_3b.md", md)
    write(REPORT_DIR / "latest_readme_render_alignment_repair.md", md)

    readme_report = "# README Render Alignment Reports\n\n"
    readme_report += "Current layer: **TAU-SCALING-SA v0.8.3b - README Render and Alignment Repair**\n\n"
    readme_report += "## Purpose\n\nThis folder stores reports for public README rendering, mojibake cleanup, code-fence repair, directory-box normalization, and alignment repair.\n\n"
    readme_report += "## README Update Rule\n\nUpdate this mini README whenever public README rendering, code fences, directory boxes, or high-level findings are repaired.\n\n"
    readme_report += "Boundary: README render alignment is repository hygiene only.\n"
    write(REPORT_DIR / "README.md", readme_report)

    release_note = "# TAU-SCALING-SA v0.8.3b - README Render and Alignment Repair\n\n"
    release_note += "## Purpose\n\nClean remaining README rendering and alignment drift after the v0.8.3 LogicFolding sweep and v0.8.3a UTF-8 anchor repair.\n\n"
    release_note += "## Repairs\n\n- Cleans mojibake in README title and prose.\n- Repairs broken fenced code blocks.\n- Restores `context`, `next`, and `text` where code-fence drift corrupted words.\n- Deduplicates the AI Failure Learning Ledger header.\n- Normalizes the Full Directory Box.\n- Keeps Tau findings and LogicFolding sweep visible near the top.\n- Preserves exact audited heading: `AI Rule — Directory Box and Mini README Synchronization`.\n\n"
    release_note += "## Boundary\n\nThis is README/release-surface repair only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_3b_readme_render_alignment_repair.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "repairs": len(report["repairs"]),
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/readme_render_alignment/latest_readme_render_alignment_repair.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()