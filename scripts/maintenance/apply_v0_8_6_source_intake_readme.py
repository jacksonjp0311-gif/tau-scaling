from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "source_evidence_intake"
BACKUP_DIR = REPORT_DIR / "v0_8_6" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_8_6_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.6 - Source Evidence Intake Cards**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.5 - Public Source Ledger / Claim Provenance Map**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.6 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.6-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.6 |", text)
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

def update_research_snapshot(text: str) -> str:
    row = "| v0.8.6 Source Evidence Intake Cards | What exact source fields must be filled before claims can be reviewed? | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |"
    if row not in text:
        text = text.replace(
            "| v0.8.5 Public Source Ledger | Which source category produced each claim, and how far can it carry the claim? | `reports/public_source_ledger/latest_public_source_ledger.md` |",
            "| v0.8.5 Public Source Ledger | Which source category produced each claim, and how far can it carry the claim? | `reports/public_source_ledger/latest_public_source_ledger.md` |\n" + row
        )
    return text

def add_source_intake_section(text: str) -> str:
    section = """## Source Evidence Intake Cards v0.8.6

This layer converts source provenance into concrete source-intake cards. Every public Tau claim receives a card requiring source URL/citation, source type, publication/disclosure metadata, extracted claim or bounded paraphrase, allowed carry, blocked carry, and independent-evidence requirements.

Primary outputs:

- `reports/source_evidence_intake/latest_source_evidence_intake_cards.md`
- `reports/source_evidence_intake/latest_source_evidence_intake_cards.json`
- `reports/source_evidence_intake/cards/`
- `visuals/source_evidence_intake/v0_8_6/`

Boundary: source evidence intake cards are templates for source discipline. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.
"""
    return insert_after(text, "Public Source Ledger / Claim Provenance Map v0.8.5", section)

def update_metrics(text: str) -> str:
    rows = [
        "| Source evidence intake cards | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |",
        "| Source evidence intake visual | `visuals/source_evidence_intake/v0_8_6/source_evidence_intake_cards.svg` |",
    ]
    for row in rows:
        if row not in text:
            text = text.replace("| Public source ledger | `reports/public_source_ledger/latest_public_source_ledger.md` |", "| Public source ledger | `reports/public_source_ledger/latest_public_source_ledger.md` |\n" + row)
    return text

def update_quick_start(text: str) -> str:
    cmd = "python scripts/benchmarks/generate_source_evidence_intake_cards.py"
    if cmd not in text:
        text = text.replace("python scripts/benchmarks/generate_public_source_ledger.py", "python scripts/benchmarks/generate_public_source_ledger.py\n" + cmd)
    return text

def update_directory_box(text: str) -> str:
    rows = [
        "| `reports/source_evidence_intake/` | Source evidence intake card reports |",
        "| `visuals/source_evidence_intake/` | Source evidence intake charts |",
    ]
    for row in rows:
        if row not in text:
            if "reports/source_evidence_intake" in row:
                text = text.replace("| `reports/public_source_ledger/` | Public source provenance and source-carry boundary reports |", "| `reports/public_source_ledger/` | Public source provenance and source-carry boundary reports |\n" + row)
            else:
                text = text.replace("| `visuals/public_source_ledger/` | Public source ledger charts |", "| `visuals/public_source_ledger/` | Public source ledger charts |\n" + row)
    return text

def update_archive(text: str) -> str:
    row = "| `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` | Source evidence intake card report |"
    if row not in text:
        text = text.replace("| `reports/public_source_ledger/latest_public_source_ledger.md` | Public source ledger and claim provenance map |", "| `reports/public_source_ledger/latest_public_source_ledger.md` | Public source ledger and claim provenance map |\n" + row)
    return text

def update_lineage(text: str) -> str:
    if "| v0.8.6 |" not in text and "| v0.8.5 |" in text:
        text = text.replace(
            "| v0.8.5 | Public Source Ledger / Claim Provenance Map; maps source categories, source-carry boundaries, and reflection law into the public Tau claim spine. |",
            "| v0.8.5 | Public Source Ledger / Claim Provenance Map; maps source categories, source-carry boundaries, and reflection law into the public Tau claim spine. |\n| v0.8.6 | Source Evidence Intake Cards; creates per-claim source-intake cards with required source fields and promotion blockers. |"
        )
    return text

def update_next(text: str) -> str:
    return re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.7 - Source Intake Population / Primary Source Pass**

Recommended goals:

- Fill intake cards with actual primary-source URLs, titles, dates, and bounded paraphrases.
- Separate primary-source claims from media interpretation.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

def ensure_lesson(text: str) -> str:
    if "| L-073 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    lesson = "| L-073 | v0.8.5 mapped source provenance, but provenance categories still needed concrete source-intake fields. | A source category is not yet a citation, quote, date, author, or measurement package. | Source provenance must be followed by intake cards before any source-backed claim review or promotion discussion. |"
    block = text[start:end].rstrip() + "\n" + lesson + "\n\n"
    return text[:start] + block + text[end:]

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text = read(README)
    text = normalize_state(text)
    text = update_research_snapshot(text)
    text = add_source_intake_section(text)
    text = update_metrics(text)
    text = update_quick_start(text)
    text = update_directory_box(text)
    text = update_archive(text)
    text = update_lineage(text)
    text = update_next(text)
    text = ensure_lesson(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.6 README patch would remove required anchors: {missing}")

    write(README, text)

    report = {
        "schema": "tau-scaling-v0.8.6-readme-source-intake-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.6 - Source Evidence Intake Cards",
        "repairs": [
            "added Source Evidence Intake Cards section",
            "updated current research snapshot",
            "updated metrics and quick start",
            "updated directory box and archive pointers",
            "updated release lineage and next-version target",
            "added L-073 source-intake lesson",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "boundary": "README/source-intake patch is source discipline only. It does not validate silicon or promote claims.",
    }
    write(REPORT_DIR / "readme_source_intake_patch_v0_8_6.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_source_intake_patch_v0_8_6.md", "# README Source Intake Patch v0.8.6\n\n" + "\n".join(f"- {x}" for x in report["repairs"]) + "\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "report": "reports/source_evidence_intake/readme_source_intake_patch_v0_8_6.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()