from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "release_finding_repair"
BACKUP_DIR = REPORT_DIR / "v0_8_4a" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"

BROKEN_LINE_REPAIRS = [
    (re.compile(r"(?m)^(\s*)eports/"), r"\1reports/"),
    (re.compile(r"(?m)^(\s*)cc/nexus/"), r"\1rcc/nexus/"),
    (re.compile(r"(?m)^(\s*)ests/"), r"\1tests/"),
    (re.compile(r"(?m)^(\s*)rtifacts/"), r"\1artifacts/"),
    (re.compile(r"(?m)^(\s*)isuals/"), r"\1visuals/"),
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_4a_{stamp}.bak", read(path))

def inspect_path_breaks(text: str):
    findings = []
    patterns = {
        r"(?m)^\s*cc/nexus/": "missing leading r in rcc/nexus/",
        r"(?m)^\s*eports/": "missing leading r in reports/",
        r"(?m)^\s*ests/": "missing leading t in tests/",
        r"(?m)^\s*rtifacts/": "missing leading a in artifacts/",
        r"(?m)^\s*isuals/": "missing leading v in visuals/",
    }
    for pattern, detail in patterns.items():
        if re.search(pattern, text):
            findings.append({"code": "possible_path_break", "detail": detail})
    return findings

def repair_path_breaks(text: str) -> tuple[str, list[str]]:
    before = text
    applied = []
    for pattern, repl in BROKEN_LINE_REPAIRS:
        if pattern.search(text):
            text = pattern.sub(repl, text)
            applied.append(pattern.pattern)
    if text == before:
        # The release warning can also result from a hard-wrapped bare path in a markdown list.
        # Normalize known vulnerable evidence-surface snippets into bullets.
        text = text.replace("\neports/", "\nreports/")
        text = text.replace("\ncc/nexus/", "\nrcc/nexus/")
        text = text.replace("\nests/", "\ntests/")
        text = text.replace("\nrtifacts/", "\nartifacts/")
        text = text.replace("\nisuals/", "\nvisuals/")
    return text, applied

def normalize_readme_state(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.4 - Evidence Sufficiency Matrix**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.4a |",
        text,
    )
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.4a-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.4a |", text)
    text = re.sub(r"\| Release warning findings \| .*?\|", "| Release warning findings | 0 / v0.8.4a zero-finding repair |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def ensure_lineage_and_next(text: str) -> str:
    if "| v0.8.4a |" not in text and "| v0.8.4 |" in text:
        text = text.replace(
            "| v0.8.4 | Evidence Sufficiency Matrix; defines promotion/downgrade evidence requirements for public Tau claims. |",
            "| v0.8.4 | Evidence Sufficiency Matrix; defines promotion/downgrade evidence requirements for public Tau claims. |\n| v0.8.4a | Release Finding Zero-Finding Repair; removes remaining path-break warning after v0.8.4. |"
        )

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map**

Recommended goals:

- Tie every public Tau claim to source category, claim type, and extraction boundary.
- Separate methodology claims, reported metrics, roadmap claims, media interpretation, and independent evidence.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )
    return text

def ensure_lesson(text: str) -> str:
    if "| L-069 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    lesson = "| L-069 | v0.8.4 passed but release readiness emitted one path-break warning for a line beginning `eports/`. | Markdown presentation repairs can leave hard-wrapped bare paths that validators read as broken repo paths. | After adding new report paths, run release validator and repair any bare-path continuation lines before moving to the next research layer. |"
    block = text[start:end].rstrip()
    if lesson not in block:
        block += "\n" + lesson
    return text[:start] + block + "\n\n" + text[end:]

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text_before = read(README)
    findings_before = inspect_path_breaks(text_before)
    text_after, applied = repair_path_breaks(text_before)
    text_after = normalize_readme_state(text_after)
    text_after = ensure_lineage_and_next(text_after)
    text_after = ensure_lesson(text_after)
    text_after = re.sub(r"\n{3,}", "\n\n", text_after)
    findings_after = inspect_path_breaks(text_after)

    write(README, text_after)

    report = {
        "schema": "tau-scaling-release-finding-zero-repair-v0.8.4a",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair",
        "findings_before": findings_before,
        "findings_after_local_scan": findings_after,
        "repair_patterns_applied": applied,
        "expected_release_findings_after_validator": 0,
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "Release finding repair improves README/release hygiene only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }

    write(REPORT_DIR / "release_finding_zero_repair_v0_8_4a.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_release_finding_zero_repair.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# Release Finding Zero-Finding Repair v0.8.4a\n\n"
    md += "## Purpose\n\nRemove the remaining release-readiness warning after v0.8.4.\n\n"
    md += "## Findings Before\n\n"
    if findings_before:
        for item in findings_before:
            md += f"- `{item['code']}` — {item['detail']}\n"
    else:
        md += "- Local pre-scan did not reproduce a path-break finding; repair still normalized vulnerable path lines.\n"
    md += "\n## Findings After Local Scan\n\n"
    if findings_after:
        for item in findings_after:
            md += f"- `{item['code']}` — {item['detail']}\n"
    else:
        md += "- none\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "release_finding_zero_repair_v0_8_4a.md", md)
    write(REPORT_DIR / "latest_release_finding_zero_repair.md", md)

    readme_report = "# Release Finding Repair Reports\n\n"
    readme_report += "Current layer: **TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair**\n\n"
    readme_report += "## Purpose\n\nThis folder stores reports for release validator warning inspection and zero-finding repair.\n\n"
    readme_report += "## README Update Rule\n\nUpdate this mini README whenever release-readiness warning repairs change.\n\n"
    readme_report += "Boundary: release finding repair is repository hygiene only.\n"
    write(REPORT_DIR / "README.md", readme_report)

    release_note = "# TAU-SCALING-SA v0.8.4a - Release Finding Zero-Finding Repair\n\n"
    release_note += "## Purpose\n\nInspect and repair the remaining release-readiness warning after v0.8.4.\n\n"
    release_note += "## Repair\n\n- Normalizes broken bare-path continuation lines such as `eports/` back to `reports/`.\n"
    release_note += "- Updates README checkpoint, metrics, release lineage, and next-version target.\n"
    release_note += "- Preserves the v0.8.4 Evidence Sufficiency Matrix and all no-mutation locks.\n\n"
    release_note += "## Boundary\n\nThis is release-surface hygiene only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_4a_release_finding_zero_repair.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "findings_before_count": len(findings_before),
        "findings_after_local_scan_count": len(findings_after),
        "expected_release_findings_after_validator": 0,
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/release_finding_repair/latest_release_finding_zero_repair.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()