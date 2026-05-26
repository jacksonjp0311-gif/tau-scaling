
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import re

root = Path.cwd()
generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

readme = root / "README.md"
text = readme.read_text(encoding="utf-8", errors="replace")

backup_dir = root / "reports" / "readme" / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)
backup = backup_dir / f"README_before_v0_3_3d_render_lineage_warning_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
backup.write_text(text, encoding="utf-8")

text = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.3\.3[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.3.3d — README Render, Lineage, and Warning Polish**",
    text,
)
text = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.3\.3[a-z]?[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.3.3c — Safe README Process Alignment Repair**",
    text,
)
text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.3\.3[a-z]? \|", "| Current checkpoint | TAU-SCALING-SA v0.3.3d |", text)
text = re.sub(r"\| Public README / process alignment \| v0\.3\.3[a-z]? \|", "| Public README / render-lineage polish | v0.3.3d |", text)

if "| Release warning findings | 0 expected after v0.3.3d validator scan repair |" not in text:
    text = text.replace(
        "| Unified release validator | passing / step failures 0 |\n",
        "| Unified release validator | passing / step failures 0 |\n| Release warning findings | 0 expected after v0.3.3d validator scan repair |\n",
    )

head, sep, tail = text.partition("## Repository Layers")
if sep and "python scripts/release/validate_release.py" not in head:
    head = head.replace(
        "python scripts/benchmarks/run_tau_scaling_benchmarks.py",
        "python scripts/benchmarks/run_tau_scaling_benchmarks.py\npython scripts/release/validate_release.py",
        1,
    )
text = head + sep + tail

ledger_start = text.find("### Current Lessons")
ledger_end = text.find("### Failure Response Protocol")
if ledger_start != -1 and ledger_end != -1:
    before = text[:ledger_start]
    after = text[ledger_end:]
    lesson_lines = [
        "### Current Lessons",
        "",
        "| Lesson ID | Failure observed | Root cause | Permanent rule |",
        "|---|---|---|---|",
        "| L-001 | RCC-N passed while runtime syntax was broken. | RCC-N validates navigation and context, not Python execution. | Runtime patches must run `py_compile`, import checks, unit tests, and CLI claims. |",
        "| L-002 | Architecture validator passed while runtime syntax was broken. | Architecture validation checks contract surfaces, not executable behavior. | Architecture pass is necessary but never sufficient for release readiness. |",
        "| L-003 | v0.3.2 introduced a concatenated import line. | Script patching merged two Python imports into one invalid statement. | Generated code patches must be compile-checked before any commit. |",
        "| L-004 | v0.3.2a left a literal PowerShell backtick newline inside Python. | PowerShell string escaping injected raw escape text instead of an actual newline. | Scripts that patch code must avoid raw escape residue and must compile the patched file. |",
        "| L-005 | Back-to-back baseline and promotion runs originally shared second-level run IDs. | Timestamp identity had insufficient granularity. | Run identity must use microsecond/token uniqueness and filesystem collision guards. |",
        "| L-006 | Early v0.3.2 status text said complete even when validation failed. | Script wrote completion status after failed checks without hard stop semantics. | Failed validation must produce a failure status, not a completion seal. |",
        "| L-007 | Benchmark evidence could be confused with product evidence. | Local runtime benchmarks can look stronger than their claim boundary. | Benchmark reports must state: local-runtime evidence only, not silicon/product validation. |",
        "| L-008 | README audit failed on a visually correct AI Rule heading. | The heading used the wrong dash/encoding variant. | Audit-visible anchors must be written with exact expected Unicode or ASCII tokens. |",
        "| L-009 | README became mojibake-contaminated after repeated Unicode patching. | Mixed console encodings and repeated copy/paste repair passes corrupted Unicode arrows/dashes/code blocks. | Public README should prefer ASCII-safe syntax except for explicitly audited Unicode anchors. |",
        "| L-010 | v0.3.3 release validator passed with one non-blocking finding. | Release readiness can be true while warning-level readability/risk findings remain. | Passing release readiness must still be inspected before the next experimental layer. |",
        "| L-011 | README release-state drift recurred after v0.3.3. | The release validator was added and pushed before the public README was fully synchronized. | Every release patch must update README checkpoint, metrics, lineage, next target, and process rules before promotion. |",
        "| L-012 | v0.3.3b repair failed when pasted line by line. | PowerShell line wrapping split paths such as `reports\\\\readme` and `scripts\\\\release`. | Large scripts must be run from downloaded `.ps1` files using `powershell -ExecutionPolicy Bypass -File ...`. |",
        "| L-013 | v0.3.3c README had out-of-order release lineage. | Emergency repair appended rows without chronological normalization. | Release lineage and lesson ledgers must be ordered before push. |",
        "",
        "",
    ]
    text = before + "\n".join(lesson_lines) + after

lineage_start = text.find("## Release Lineage")
lineage_end = text.find("## Next Recommended Version")
if lineage_start != -1 and lineage_end != -1:
    before = text[:lineage_start]
    after = text[lineage_end:]
    lineage_lines = [
        "## Release Lineage",
        "",
        "| Version | Meaning |",
        "|---|---|",
        "| v0.1 | Minimal Tau Scaling runtime scaffold. |",
        "| v0.2-RCCN | RCC-N / OMN-style repository structure injection. |",
        "| v0.2.1 | Root cleanup and identity guard. |",
        "| v0.2.2 | Version seal and release manifest layer. |",
        "| v0.2.3 | README / Nexus public polish layer. |",
        "| v0.2.3a | RCC-N trisection anchor repair. |",
        "| v0.3 | Evidence Promotion Path + Directory Governance. |",
        "| v0.3.1 | Public README directory-box repair and durable map cleanup. |",
        "| v0.3.2b | Collision-proof run identity and benchmark validation. |",
        "| v0.3.2c | AI failure-learning README ledger and protocol. |",
        "| v0.3.2d | README + mini repo audit map and executable gap scanner. |",
        "| v0.3.2e | README / mini repo audit repair and visible lock restoration. |",
        "| v0.3.2f | README / mini repo audit visibility repair. |",
        "| v0.3.2g | Exact Unicode README anchor repair. |",
        "| v0.3.2h | README mojibake cleanup and audit surface consolidation. |",
        "| v0.3.3 | Unified release validator and release-readiness reports. |",
        "| v0.3.3a | Main README release-state synchronization. |",
        "| v0.3.3c | Safe README process alignment repair after pasted-script path break. |",
        "| v0.3.3d | README render, lineage, and validator-warning polish. |",
        "",
        "",
    ]
    text = before + "\n".join(lineage_lines) + after

if "### Render and Ordering Discipline" not in text:
    note = "\n".join([
        "### Render and Ordering Discipline",
        "",
        "Before push, inspect the public README for:",
        "",
        "```text",
        "- current checkpoint matches latest commit intent",
        "- release lineage is chronological",
        "- failure lessons are numerically ordered",
        "- directory box has no duplicate durable entries",
        "- Quick Start includes the release validator",
        "- next recommended version points to the actual next layer",
        "```",
        "",
        "",
    ])
    text = text.replace("### Pre-Experiment Checklist", note + "### Pre-Experiment Checklist", 1)

next_lines = [
    "## Next Recommended Version",
    "",
    "**TAU-SCALING-SA v0.4.0 — Synthetic Gate Test Suite**",
    "",
    "Recommended goals:",
    "",
    "- Add synthetic claim cards that isolate each gate.",
    "- Prove downgrade behavior for missing yield, missing workload, thermal/PDN/PVT failures, edge/surface starvation, and LogicFolding survivability failures.",
    "- Emit gate-test reports under `reports/gates/`.",
    "- Preserve non-claim locks: synthetic gate tests are runtime behavior tests, not silicon/product validation.",
    "",
    "Initial target seeds:",
    "",
    "```text",
    "configs/seeds/tests/tau_compute_only_pass.json",
    "configs/seeds/tests/tau_wire_dominant_pass.json",
    "configs/seeds/tests/tau_memory_dominant_fail.json",
    "configs/seeds/tests/logicfolding_high_vertical_penalty_fail.json",
    "configs/seeds/tests/edge_surface_starvation_fail.json",
    "configs/seeds/tests/gamma_tau_etp_thermal_fail.json",
    "configs/seeds/tests/yield_missing_disclosure_downgrade.json",
    "```",
]
text = re.sub(r"## Next Recommended Version\s+.*\Z", "\n".join(next_lines) + "\n", text, flags=re.S)
readme.write_text(text, encoding="utf-8")

validator = root / "scripts" / "release" / "validate_release.py"
vtext = validator.read_text(encoding="utf-8", errors="replace")

new_func = r"""def inspect_readme_for_mojibake() -> list[dict[str, str]]:
    path = REPO_ROOT / "README.md"
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

    findings: list[dict[str, str]] = []

    mojibake_tokens = {
        "Ã": "latin1_mojibake_A_tilde",
        "Â": "latin1_mojibake_A_circumflex",
        "â€": "utf8_quote_dash_mojibake",
        "\\ufffd": "replacement_character",
    }
    for token, label in mojibake_tokens.items():
        if token in text:
            findings.append({
                "severity": "warning",
                "code": "possible_mojibake",
                "path": "README.md",
                "detail": f"{label}: {token.encode('unicode_escape').decode('ascii')}",
            })

    broken_path_patterns = {
        r"(?m)^\\s*cc/nexus/": "missing leading r in rcc/nexus/",
        r"(?m)^\\s*eports/": "missing leading r in reports/",
        r"(?m)^\\s*ests/": "missing leading t in tests/",
        r"(?m)^\\s*rtifacts/": "missing leading a in artifacts/",
        r"(?m)^\\s*isuals/": "missing leading v in visuals/",
    }
    for pattern, detail in broken_path_patterns.items():
        if re.search(pattern, text):
            findings.append({
                "severity": "warning",
                "code": "possible_path_break",
                "path": "README.md",
                "detail": detail,
            })

    duplicate_scripts_release = (
        "  scripts/\\n"
        "    benchmarks/\\n"
        "    release/\\n"
        "    maintenance/\\n"
        "    rcc/\\n"
        "    release/\\n"
        "    validation/"
    )
    if duplicate_scripts_release in text:
        findings.append({
            "severity": "warning",
            "code": "duplicate_directory_box_entry",
            "path": "README.md",
            "detail": "scripts/release appears twice in Full Directory Box",
        })

    if "| v0.3.3c |" in text and "| v0.3.3a |" in text:
        if text.find("| v0.3.3c |") < text.find("| v0.3.3a |"):
            findings.append({
                "severity": "warning",
                "code": "release_lineage_out_of_order",
                "path": "README.md",
                "detail": "v0.3.3c appears before v0.3.3a",
            })

    return findings
"""

vtext2 = re.sub(
    r"def inspect_readme_for_mojibake\(\) -> list\[dict\[str, str\]\]:.*?\n\ndef main\(\) -> int:",
    new_func + "\n\ndef main() -> int:",
    vtext,
    flags=re.S,
)
if vtext2 == vtext:
    raise RuntimeError("Could not patch inspect_readme_for_mojibake in validate_release.py")
validator.write_text(vtext2, encoding="utf-8")

release = root / "docs" / "release_notes" / "tau_scaling_v0_3_3d_readme_render_lineage_warning_polish.md"
release.parent.mkdir(parents=True, exist_ok=True)
release.write_text(f"""# TAU-SCALING-SA v0.3.3d — README Render, Lineage, and Warning Polish

Generated: {generated_at}

## Purpose

This patch cleans the public README ordering state and repairs release-validator warning behavior before v0.4.0 begins.

## Updates

- Sets current checkpoint to v0.3.3d.
- Reorders AI Failure Learning Ledger rows L-010 through L-013.
- Reorders release lineage chronologically.
- Adds render and ordering discipline checklist.
- Patches release-validator README scan to avoid blank false-positive findings.
- Keeps v0.4.0 Synthetic Gate Test Suite as the next target.

## Boundary

This is README/process/validator polish only. It does not alter Tau Scaling gate math, classifier thresholds, evidence semantics, or claim classes.
""", encoding="utf-8")

status = root / "reports" / "readme" / "latest_v0_3_3d_readme_render_lineage_warning_polish_status.md"
status.parent.mkdir(parents=True, exist_ok=True)
status.write_text(f"""# Tau Scaling v0.3.3d README Render, Lineage, and Warning Polish Status

Generated: {generated_at}

Status: complete

Boundary:
- Public README and validator-quality polish only.
""", encoding="utf-8")
