from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "readme_render_spacing"
BACKUP_DIR = REPORT_DIR / "v0_8_6a" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_8_6a_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(
        r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Current checkpoint: **TAU-SCALING-SA v0.8.6a - README Render Spacing Polish**",
        text,
    )
    text = re.sub(
        r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*",
        "Previous seal: **TAU-SCALING-SA v0.8.6 - Source Evidence Intake Cards**",
        text,
    )
    text = re.sub(
        r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|",
        "| Current checkpoint | TAU-SCALING-SA v0.8.6a |",
        text,
    )
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.6a-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.6a |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)
    return text

def ensure_blank_before_headings(text: str) -> str:
    # Exactly target GitHub rendering risks introduced by generated adjacent sections.
    replacements = [
        (
            "Boundary: source evidence intake cards are templates for source discipline. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.\n## Tau Doctrine Alignment",
            "Boundary: source evidence intake cards are templates for source discipline. They do not promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.\n\n## Tau Doctrine Alignment",
        ),
        (
            "- `docs/reflection/law_of_sufficient_form_v0_8_5.md`\n## Human Director Box",
            "- `docs/reflection/law_of_sufficient_form_v0_8_5.md`\n\n## Human Director Box",
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)

    # General safety: ensure top-level headings are separated from prior non-blank text.
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.startswith("## ") and out and out[-1].strip() != "":
            out.append("")
        out.append(line)
    return "\n".join(out) + "\n"

def update_research_snapshot(text: str) -> str:
    row = "| v0.8.6a README Render Spacing Polish | Did the public README render cleanly after source-intake insertion? | `reports/readme_render_spacing/latest_readme_render_spacing_polish.md` |"
    if row not in text:
        text = text.replace(
            "| v0.8.6 Source Evidence Intake Cards | What exact source fields must be filled before claims can be reviewed? | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |",
            "| v0.8.6 Source Evidence Intake Cards | What exact source fields must be filled before claims can be reviewed? | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |\n" + row
        )
    return text

def update_metrics(text: str) -> str:
    row = "| README render spacing polish | `reports/readme_render_spacing/latest_readme_render_spacing_polish.md` |"
    if row not in text:
        text = text.replace(
            "| Source evidence intake cards | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |",
            "| Source evidence intake cards | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |\n" + row
        )
    return text

def update_directory_box(text: str) -> str:
    row = "| `reports/readme_render_spacing/` | README render-spacing polish reports |"
    if row not in text:
        text = text.replace(
            "| `reports/readme_information_architecture/` | README information architecture compression reports |",
            "| `reports/readme_information_architecture/` | README information architecture compression reports |\n" + row
        )
    return text

def update_archive(text: str) -> str:
    row = "| `reports/readme_render_spacing/latest_readme_render_spacing_polish.md` | README render spacing polish report |"
    if row not in text:
        text = text.replace(
            "| `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` | Source evidence intake card report |",
            "| `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` | Source evidence intake card report |\n" + row
        )
    return text

def update_lineage(text: str) -> str:
    if "| v0.8.6a |" not in text and "| v0.8.6 |" in text:
        text = text.replace(
            "| v0.8.6 | Source Evidence Intake Cards; creates per-claim source-intake cards with required source fields and promotion blockers. |",
            "| v0.8.6 | Source Evidence Intake Cards; creates per-claim source-intake cards with required source fields and promotion blockers. |\n| v0.8.6a | README Render Spacing Polish; repairs GitHub-rendering spacing after v0.8.6 section insertion. |"
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
    if "| L-074 |" in text:
        return text
    start = text.find("### Current Lessons")
    end = text.find("### Failure Response Protocol")
    if start == -1 or end == -1 or end <= start:
        return text
    lesson = "| L-074 | v0.8.6 passed all validators, but generated README sections had minor heading-adjacency render risk. | Markdown can pass audits while still needing visual spacing polish. | After inserting generated README sections, run a render-spacing polish pass before starting the next research layer. |"
    block = text[start:end].rstrip() + "\n" + lesson + "\n\n"
    return text[:start] + block + text[end:]

def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    backup(README)

    text = read(README)
    text = normalize_state(text)
    text = update_research_snapshot(text)
    text = update_metrics(text)
    text = update_directory_box(text)
    text = update_archive(text)
    text = update_lineage(text)
    text = update_next(text)
    text = ensure_lesson(text)
    text = ensure_blank_before_headings(text)
    text = re.sub(r"\n{4,}", "\n\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.6a render spacing polish would remove required anchors: {missing}")

    write(README, text)

    report = {
        "schema": "tau-scaling-readme-render-spacing-polish-v0.8.6a",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.6a - README Render Spacing Polish",
        "repairs": [
            "added blank line before Tau Doctrine Alignment after Source Evidence Intake section",
            "added blank line before Human Director Box after Reflection section",
            "added general top-level heading spacing guard",
            "added v0.8.6a to Current Research Snapshot and Release Lineage",
            "added README render spacing report surface",
            "preserved all RCC-N / README audit anchors",
        ],
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "boundary": "README render spacing polish improves GitHub readability only. It does not change research outputs, promote claims, validate silicon, validate products, or mutate classifier behavior.",
    }
    write(REPORT_DIR / "readme_render_spacing_polish_v0_8_6a.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "latest_readme_render_spacing_polish.json", json.dumps(report, indent=2, sort_keys=True) + "\n")

    md = "# README Render Spacing Polish v0.8.6a\n\n## Repairs\n\n"
    for item in report["repairs"]:
        md += f"- {item}\n"
    md += "\n## Boundary\n\n" + report["boundary"] + "\n"
    write(REPORT_DIR / "readme_render_spacing_polish_v0_8_6a.md", md)
    write(REPORT_DIR / "latest_readme_render_spacing_polish.md", md)

    write(REPORT_DIR / "README.md", "# README Render Spacing Reports\n\nCurrent layer: **TAU-SCALING-SA v0.8.6a - README Render Spacing Polish**\n\n## Purpose\n\nThis folder stores reports for GitHub README rendering and spacing polish.\n\n## README Update Rule\n\nUpdate this mini README whenever public README render polish changes.\n\nBoundary: render spacing is public documentation hygiene only.\n")

    release_note = "# TAU-SCALING-SA v0.8.6a - README Render Spacing Polish\n\n"
    release_note += "## Purpose\n\nRepair minor README heading-adjacency spacing after v0.8.6 while preserving all audit-visible anchors.\n\n"
    release_note += "## Boundary\n\nThis is public README rendering polish only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.\n"
    write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_6a_readme_render_spacing_polish.md", release_note)

    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "report": "reports/readme_render_spacing/latest_readme_render_spacing_polish.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()