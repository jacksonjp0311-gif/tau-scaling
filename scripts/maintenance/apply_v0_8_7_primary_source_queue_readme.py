from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "primary_source_intake"
BACKUP_DIR = REPORT_DIR / "v0_8_7" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_8_7_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.7 - Primary Source Intake Queue / Source Population Scaffold**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.6a - README Render Spacing Polish**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.7 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.7-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.7 |", text)
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

    row = "| v0.8.7 Primary Source Intake Queue | Which source records are ready to be manually populated and confirmed? | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |"
    if row not in text:
        text = text.replace("| v0.8.6a README Render Spacing Polish | Did the public README render cleanly after source-intake insertion? | `reports/readme_render_spacing/latest_readme_render_spacing_polish.md` |",
                            "| v0.8.6a README Render Spacing Polish | Did the public README render cleanly after source-intake insertion? | `reports/readme_render_spacing/latest_readme_render_spacing_polish.md` |\n" + row)

    section = """## Primary Source Intake Queue v0.8.7

This layer creates a governed manual queue for filling v0.8.6 source-intake cards with actual primary-source details. It intentionally does not invent URLs, scrape sources, or promote claims.

Primary outputs:

- `sources/primary_source_intake/source_seed_manifest_v0_8_7.json`
- `reports/primary_source_intake/latest_primary_source_intake_queue.md`
- `reports/primary_source_intake/latest_primary_source_intake_queue.json`
- `visuals/primary_source_intake/v0_8_7/`

Boundary: primary source intake queueing prepares source population only. It does not validate sources, promote claims, validate silicon, validate products, prove benchmark superiority, or establish a universal Tau Scaling law.
"""
    text = insert_after(text, "Source Evidence Intake Cards v0.8.6", section)

    for metric_row in [
        "| Primary source intake queue | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |",
        "| Primary source intake manifest | `sources/primary_source_intake/source_seed_manifest_v0_8_7.json` |",
        "| Primary source intake visual | `visuals/primary_source_intake/v0_8_7/primary_source_intake_queue.svg` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Source evidence intake cards | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |",
                                "| Source evidence intake cards | `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` |\n" + metric_row)

    cmd = "python scripts/benchmarks/run_primary_source_intake_queue.py"
    if cmd not in text:
        text = text.replace("python scripts/benchmarks/generate_source_evidence_intake_cards.py", "python scripts/benchmarks/generate_source_evidence_intake_cards.py\n" + cmd)

    dir_rows = [
        ("| `sources/primary_source_intake/` | Manual primary-source intake manifest |", "| `claims/public_tau/` | Public Tau claim cards created in v0.8.2 |"),
        ("| `reports/primary_source_intake/` | Primary source intake queue reports |", "| `reports/source_evidence_intake/` | Source evidence intake card reports |"),
        ("| `visuals/primary_source_intake/` | Primary source intake charts |", "| `visuals/source_evidence_intake/` | Source evidence intake charts |"),
    ]
    for new_row, anchor in dir_rows:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/primary_source_intake/latest_primary_source_intake_queue.md` | Primary source intake queue report |"
    if archive_row not in text:
        text = text.replace("| `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` | Source evidence intake card report |",
                            "| `reports/source_evidence_intake/latest_source_evidence_intake_cards.md` | Source evidence intake card report |\n" + archive_row)

    if "| v0.8.7 |" not in text:
        text = text.replace("| v0.8.6a | README Render Spacing Polish; repairs GitHub-rendering spacing after v0.8.6 section insertion. |",
                            "| v0.8.6a | README Render Spacing Polish; repairs GitHub-rendering spacing after v0.8.6 section insertion. |\n| v0.8.7 | Primary Source Intake Queue; creates manual source-population manifest without inventing or validating sources. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.8 - Primary Source Population Pass**

Recommended goals:

- Populate source manifest entries with actual source URLs, titles, dates, authors/orgs, and bounded paraphrases.
- Keep primary source and media interpretation separate.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-075 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-075 | v0.8.6 created source-intake cards, but actual source population should not be invented by automation. | A card scaffold is not a source; a TODO field is not evidence. | Create a manual primary-source intake queue before source population, and keep claim promotion disabled until source details are filled and reviewed. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.7 README patch would remove required anchors: {missing}")

    write(README, text)

    report = {
        "schema": "tau-scaling-v0.8.7-readme-primary-source-queue-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.7 - Primary Source Intake Queue / Source Population Scaffold",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "boundary": "README/queue patch is source-population scaffold only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_primary_source_queue_patch_v0_8_7.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_primary_source_queue_patch_v0_8_7.md", "# README Primary Source Queue Patch v0.8.7\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "report": "reports/primary_source_intake/readme_primary_source_queue_patch_v0_8_7.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()