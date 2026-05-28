from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "primary_source_gap_review"
BACKUP_DIR = REPORT_DIR / "v0_8_9" / "backups"

EXACT_AI_RULE = "## AI Rule — Directory Box and Mini README Synchronization"
REQUIRED_ANCHORS = [
    "PART I - Human README",
    "PART II - RCC Nexus README",
    "PART III - AI Agent README",
    "AI Operating Contract",
    "Patch Routing Matrix",
    "README + Mini Repo Audit Map",
    "AI Failure Learning Ledger",
    EXACT_AI_RULE,
    "Full Directory Box",
    "Public Non-Claim Locks",
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def backup(path: Path) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write(BACKUP_DIR / f"{path.name}_before_v0_8_9_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.9 - Primary Source Validation Gap Review**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.8 - Public Source Population Pass**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.9 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.9-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.9 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def insert_after(text: str, anchor_heading: str, section: str) -> str:
    if section.splitlines()[0] in text:
        return text
    pattern = rf"(^## {re.escape(anchor_heading)}\s*$.*?)(?=^## |\Z)"
    m = re.search(pattern, text, flags=re.S | re.M)
    if not m:
        return text + "\n\n" + section
    return text[:m.end()] + "\n\n" + section + text[m.end():]

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text = read(README)
    text = normalize_state(text)

    row = "| v0.8.9 Primary Source Gap Review | What primary and independent validation is still missing? | `reports/primary_source_gap_review/latest_primary_source_gap_review.md` |"
    if row not in text:
        text = text.replace("| v0.8.8 Public Source Population Pass | What public sources can populate the queue without claiming primary validation? | `reports/public_source_population/latest_public_source_population_pass.md` |",
                            "| v0.8.8 Public Source Population Pass | What public sources can populate the queue without claiming primary validation? | `reports/public_source_population/latest_public_source_population_pass.md` |\n" + row)

    section = """## Primary Source Validation Gap Review v0.8.9

This layer converts source population into a publishable validation-gap review. It asks what first-party, formal, or independent evidence is still missing before any public Tau claim can be reviewed for promotion.

Primary outputs:

- `reports/primary_source_gap_review/latest_primary_source_gap_review.md`
- `reports/primary_source_gap_review/latest_primary_source_gap_review.json`
- `reports/publishable_findings/latest_publishable_findings_brief.md`
- `visuals/primary_source_gap_review/v0_8_9/`

Publishable boundary: the current result is publishable as evidence-governance and source-provenance analysis. It is not silicon validation, product validation, benchmark superiority, or proof of a universal Tau Scaling law.
"""
    text = insert_after(text, "Public Source Population Pass v0.8.8", section)

    for metric_row in [
        "| Primary source gap review | `reports/primary_source_gap_review/latest_primary_source_gap_review.md` |",
        "| Publishable findings brief | `reports/publishable_findings/latest_publishable_findings_brief.md` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Public source population pass | `reports/public_source_population/latest_public_source_population_pass.md` |",
                                "| Public source population pass | `reports/public_source_population/latest_public_source_population_pass.md` |\n" + metric_row)

    cmd = "python scripts/benchmarks/generate_primary_source_gap_review_v0_8_9.py"
    if cmd not in text:
        text = text.replace("python scripts/benchmarks/populate_public_source_intake_v0_8_8.py", "python scripts/benchmarks/populate_public_source_intake_v0_8_8.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/primary_source_gap_review/` | Primary source validation gap reports |", "| `reports/public_source_population/` | Public source population reports |"),
        ("| `reports/publishable_findings/` | Evidence-bounded publishable findings briefs |", "| `reports/primary_source_gap_review/` | Primary source validation gap reports |"),
        ("| `visuals/primary_source_gap_review/` | Primary source validation gap charts |", "| `visuals/public_source_population/` | Public source population charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_rows = [
        "| `reports/primary_source_gap_review/latest_primary_source_gap_review.md` | Primary source validation gap review |",
        "| `reports/publishable_findings/latest_publishable_findings_brief.md` | Evidence-bounded publishable findings brief |",
    ]
    for archive_row in archive_rows:
        if archive_row not in text:
            text = text.replace("| `reports/public_source_population/latest_public_source_population_pass.md` | Public source population report |",
                                "| `reports/public_source_population/latest_public_source_population_pass.md` | Public source population report |\n" + archive_row)

    if "| v0.8.9 |" not in text:
        text = text.replace("| v0.8.8 | Public Source Population Pass; populates source queue with bounded public secondary-source records while preserving primary-validation locks. |",
                            "| v0.8.8 | Public Source Population Pass; populates source queue with bounded public secondary-source records while preserving primary-validation locks. |\n| v0.8.9 | Primary Source Validation Gap Review; converts public source population into publishable validation-gap findings. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.9.0 - Public Research Milestone Package**

Recommended goals:

- Package the v0.8 public Tau research spine into a release-quality research artifact.
- Include claim ledger, source ledger, source population, validation-gap matrix, visuals, and publishable findings brief.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-077 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-077 | v0.8.8 source-populated all public Tau claims, but primary and independent validation remain absent. | A publishable result can be a bounded gap map, not a validation claim. | Publish source-provenance and validation-gap findings without upgrading technical claims beyond the available evidence. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.9 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.8.9-readme-primary-source-gap-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.9 - Primary Source Validation Gap Review",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/gap patch is publication routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_primary_source_gap_patch_v0_8_9.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_primary_source_gap_patch_v0_8_9.md", "# README Primary Source Gap Patch v0.8.9\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/primary_source_gap_review/readme_primary_source_gap_patch_v0_8_9.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()