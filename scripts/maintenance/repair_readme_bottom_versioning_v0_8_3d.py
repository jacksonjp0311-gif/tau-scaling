from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "readme_bottom_versioning"
BACKUP_DIR = REPORT_DIR / "v0_8_3d" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"

LINEAGE_ROWS = [
    ("v0.1", "Minimal Tau Scaling runtime scaffold."),
    ("v0.2-RCCN", "RCC-N / OMN-style repository structure injection."),
    ("v0.2.1", "Root cleanup and identity guard."),
    ("v0.2.2", "Version seal and release manifest layer."),
    ("v0.2.3", "README / Nexus public polish layer."),
    ("v0.2.3a", "RCC-N trisection anchor repair."),
    ("v0.3", "Evidence Promotion Path + Directory Governance."),
    ("v0.3.1", "Public README directory-box repair and durable map cleanup."),
    ("v0.3.2b", "Collision-proof run identity and benchmark validation."),
    ("v0.3.2c", "AI failure-learning README ledger and protocol."),
    ("v0.3.2d", "README + mini repo audit map and executable gap scanner."),
    ("v0.3.2e", "README / mini repo audit repair and visible lock restoration."),
    ("v0.3.2f", "README / mini repo audit visibility repair."),
    ("v0.3.2g", "Exact Unicode README anchor repair."),
    ("v0.3.2h", "README mojibake cleanup and audit surface consolidation."),
    ("v0.3.3", "Unified release validator and release-readiness reports."),
    ("v0.3.3a", "Main README release-state synchronization."),
    ("v0.3.3c", "Safe README process alignment repair after pasted-script path break."),
    ("v0.3.3d", "README render, lineage, and validator-warning polish."),
    ("v0.3.3e", "Agent contract geometry sync and v0.4 routing readiness."),
    ("v0.4.0", "Synthetic gate suite with benchmark charts and finding charts."),
    ("v0.4.0a", "Synthetic gate report link repair and complete report regeneration."),
    ("v0.4.0b", "Synthetic gate expectation calibration and hard-fail incomplete suite semantics."),
    ("v0.4.0c", "Benchmark atlas and per-version chart/finding registry."),
    ("v0.4.0d", "Benchmark mini README AI/RCC warning repair."),
    ("v0.4.0e", "Exact mini README audit-anchor repair for benchmark docs."),
    ("v0.4.0f", "Coherence reflection and agent contract re-sync after benchmark atlas sequence."),
    ("v0.4.1", "Synthetic gate sensitivity sweep and threshold curves."),
    ("v0.4.2", "Gate interaction matrix and paired gate-failure heatmaps."),
    ("v0.4.3", "Threshold explanation cards and promotion-repair hints."),
    ("v0.4.4", "Pair policy review gate for non-enforcing classifier-governance candidates."),
    ("v0.4.5", "Nexus reflective feedback loop for ranked improvement signals."),
    ("v0.4.5a", "Feedback health ordering repair so Nexus feedback reads fresh validation surfaces."),
    ("v0.4.5b", "Nexus feedback health schema alignment for list-valued findings and derived sensitivity points."),
    ("v0.4.5c", "Nexus feedback function-block repair to ensure health scorer logic actually updates."),
    ("v0.4.5d", "Nexus feedback chart-path health repair for sensitivity sweep chart evidence."),
    ("v0.4.6", "Pair policy dry-run simulator for non-mutating classifier-policy impact analysis."),
    ("v0.4.7", "Policy impact explanation cards for dry-run drift cases."),
    ("v0.4.8", "Policy decision record for non-mutating enforcement readiness classification."),
    ("v0.4.9", "Regression and over-penalty review for controlled downgrade candidates."),
    ("v0.5.0", "Enforcement readiness gate for blocked policy candidates with classifier mutation disabled."),
    ("v0.5.1", "Nexus target refresh and completed-signal retirement after v0.5.0."),
    ("v0.5.1a", "Public alignment polish for README metrics and AGENTS validation chain."),
    ("v0.5.2", "Over-penalty cause decomposition and remediation cards for blocked controlled downgrades."),
    ("v0.5.3", "Cause-specific remediation plan for high-support blocked downgrade candidates."),
    ("v0.5.4", "Support-aware negative controls for high-support blocked downgrade candidates."),
    ("v0.5.5", "Disabled calibration plan preserving support-aware retention constraints."),
    ("v0.5.6", "Calibration counterfactuals for the selected report-only threshold."),
    ("v0.5.7", "Counterfactual decision record for safe-review classification without application."),
    ("v0.5.8", "Review package and evidence bundle for v0.5.2-v0.5.7."),
    ("v0.5.9", "Review checklist and signoff gate for the evidence bundle."),
    ("v0.6.0", "Human-approved candidate branch gate; proposal only, no branch by default."),
    ("v0.6.1", "Candidate branch replay harness; replay blocked until explicit approval artifact exists."),
    ("v0.6.2", "Human approval artifact template; template only, no approval by default."),
    ("v0.6.3", "Human approval artifact validator; rejects UNSET/template-only approval by default."),
    ("v0.6.4", "Approval-gated replay dry-run; emits blocked report unless approval validates."),
    ("v0.6.5", "Approval fixture and denial fixture validator; fixtures only, no live approval."),
    ("v0.6.6", "Live approval handoff check; refuses fixtures as live approval."),
    ("v0.6.7", "Approval-gated replay executor; refuses execution when handoff is invalid."),
    ("v0.6.8", "Blocked-state continuity ledger; records blocked execution as evidence."),
    ("v0.6.9", "Blocked-state trend review; classifies whether block remains valid or stale."),
    ("v0.7.0", "Approval-governance corridor milestone; packages v0.6.0-v0.6.9 and returns focus to Tau mechanics."),
    ("v0.7.1", "Tau mechanics return review; inspects tau vectors, gate algebra, thresholds, and evidence surfaces."),
    ("v0.7.2", "Tau vector semantics ledger; maps tau terms, seed coverage, and evidence surface gaps."),
    ("v0.7.3", "Gate algebra map; maps gate-family visibility before threshold changes."),
    ("v0.7.4", "TSEK threshold boundary review; reviews class-boundary visibility without mutation."),
    ("v0.7.5", "TSEK boundary explanation cards; explains each class boundary before penalty controls."),
    ("v0.7.6", "Over/under-penalty negative controls; defines report-only controls before threshold dry-runs."),
    ("v0.7.7", "Threshold sensitivity dry-run; models threshold pressure without changing classifier behavior."),
    ("v0.7.8", "Threshold decision record; converts dry-run pressure into a non-mutating decision."),
    ("v0.7.9", "Threshold governance summary; summarizes v0.7.x and freezes threshold mutation pending more evidence."),
    ("v0.8.0", "Stable Tau threshold governance milestone; packages v0.7.x and routes future work to evidence expansion."),
    ("v0.8.1", "README benchmark publication surface for stable Tau threshold findings."),
    ("v0.8.1a", "README benchmark publication lock repair with exact public anchors."),
    ("v0.8.2", "Public Tau claim ledger; source-bounded classification of company/public claims."),
    ("v0.8.2a", "README showcase and audit-anchor repair for public Tau findings."),
    ("v0.8.3", "LogicFolding plausibility sweep; synthetic proof/falsification regime test."),
    ("v0.8.3a", "README UTF-8 audit-anchor repair after LogicFolding sweep."),
    ("v0.8.3b", "README render/alignment repair after remaining mojibake and directory-box drift."),
    ("v0.8.3c", "README presentation restore; compact human-readable layout."),
    ("v0.8.3d", "README bottom versioning and final presentation tail repair."),
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_3d_{stamp}.bak", read(path))

def normalize_top(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.3d - README Bottom Versioning and Presentation Tail Repair**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.3c - README Presentation Restore**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.3d |",
        text,
    )
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.3d-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.3d |", text)

    if "| README presentation restore |" not in text:
        text = text.replace(
            "| Claim status | local runtime evidence + benchmark observability only |",
            "| README presentation restore | `reports/readme_presentation_restore/latest_readme_presentation_restore.md` |\n| Claim status | local runtime evidence + benchmark observability only |",
        )
    if "| README bottom versioning repair |" not in text:
        text = text.replace(
            "| Claim status | local runtime evidence + benchmark observability only |",
            "| README bottom versioning repair | `reports/readme_bottom_versioning/latest_readme_bottom_versioning_repair.md` |\n| Claim status | local runtime evidence + benchmark observability only |",
        )
    return text

def normalize_remaining_fences(text: str) -> str:
    text = text.replace("`````text", "```")
    text = text.replace("````text", "```")
    text = text.replace("## N```` Recommended Version", "## Next Recommended Version")
    text = text.replace("N```` Recommended", "Next Recommended")
    return text

def ensure_anchor(text: str) -> str:
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def rebuild_release_tail(text: str) -> str:
    start = text.find("## Release Lineage")
    if start == -1:
        start = len(text)

    before = text[:start].rstrip()
    lineage = ["## Release Lineage", "", "| Version | Meaning |", "|---|---|"]
    lineage += [f"| {version} | {meaning} |" for version, meaning in LINEAGE_ROWS]

    next_section = [
        "",
        "## Next Recommended Version",
        "",
        "**TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**",
        "",
        "Recommended goals:",
        "",
        "- Convert public Tau claim classes into explicit evidence sufficiency requirements.",
        "- Define what evidence would promote TSEK-C to TSEK-B and TSEK-B to TSEK-A.",
        "- Define what evidence would force downgrade to TSEK-D or TSEK-E.",
        "- Preserve downgrade discipline and non-claim locks.",
        "- Keep threshold and classifier mutation disabled.",
        "- Preserve `mutation_allowed: false`.",
        "",
    ]

    return before + "\n\n" + "\n".join(lineage + next_section)

def ensure_lesson(text: str) -> str:
    if "| L-068 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    block = text[start:end].rstrip()
    lesson = "| L-068 | v0.8.3c restored the top README presentation, but the release lineage tail still had stale v0.8.3 text and a corrupt Next Recommended heading. | Top and bottom README sections can drift independently after surgical repairs. | Presentation repairs must inspect the README tail: release lineage, next-version block, duplicate sections, and stale version labels. |"
    if lesson not in block:
        block += "\n" + lesson
    return text[:start] + block + "\n\n" + text[end:]

def main() -> None:
    backup(README)
    text = read(README)

    text = normalize_remaining_fences(text)
    text = ensure_anchor(text)
    text = normalize_top(text)
    text = ensure_lesson(text)
    text = rebuild_release_tail(text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    write(README, text)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "tau-scaling-readme-bottom-versioning-repair-v0.8.3d",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.3d - README Bottom Versioning and Presentation Tail Repair",
        "repairs": [
            "updated top checkpoint to v0.8.3d",
            "updated current public metrics to v0.8.3d",
            "replaced corrupt bottom Next Recommended heading",
            "removed stale duplicate LogicFolding section from the README tail",
            "rebuilt Release Lineage through v0.8.3d",
            "set next recommended version to v0.8.4 Evidence Sufficiency Matrix",
            "added L-068 tail-versioning lesson",
            "preserved exact audited AI Rule em-dash heading",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "README bottom versioning repair improves public readability and repository navigation only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    write(REPORT_DIR / "readme_bottom_versioning_repair_v0_8_3d.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_readme_bottom_versioning_repair.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# README Bottom Versioning Repair v0.8.3d\n\n## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "readme_bottom_versioning_repair_v0_8_3d.md", md)
    write(REPORT_DIR / "latest_readme_bottom_versioning_repair.md", md)

    readme_report = "# README Bottom Versioning Reports\n\n"
    readme_report += "Current layer: **TAU-SCALING-SA v0.8.3d - README Bottom Versioning and Presentation Tail Repair**\n\n"
    readme_report += "## Purpose\n\nThis folder stores reports for README release-lineage, next-version, and tail-presentation repairs.\n\n"
    readme_report += "## README Update Rule\n\nUpdate this mini README whenever the root README release lineage or next-version block changes.\n\n"
    readme_report += "Boundary: README bottom-versioning repair is repository hygiene only.\n"
    write(REPORT_DIR / "README.md", readme_report)

    release_note = "# TAU-SCALING-SA v0.8.3d - README Bottom Versioning and Presentation Tail Repair\n\n"
    release_note += "## Purpose\n\nRepair the README tail after v0.8.3c restored presentation but left the release-lineage bottom stale.\n\n"
    release_note += "## Repairs\n\n"
    for item in report["repairs"]:
        release_note += f"- {item}\n"
    release_note += "\n## Boundary\n\nThis is README/release-surface repair only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_3d_readme_bottom_versioning_repair.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "repairs": len(report["repairs"]),
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/readme_bottom_versioning/latest_readme_bottom_versioning_repair.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()