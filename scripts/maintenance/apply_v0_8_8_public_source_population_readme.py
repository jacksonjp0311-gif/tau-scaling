from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "public_source_population"
BACKUP_DIR = REPORT_DIR / "v0_8_8" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_8_8_{stamp}.bak", read(path))

def normalize_state(text: str) -> str:
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.8 - Public Source Population Pass**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.8\.[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.7 - Primary Source Intake Queue / Source Population Scaffold**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.8\.[0-9A-Za-z.]* \|", "| Current checkpoint | TAU-SCALING-SA v0.8.8 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.8.8-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.8.8 |", text)
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

    row = "| v0.8.8 Public Source Population Pass | What public sources can populate the queue without claiming primary validation? | `reports/public_source_population/latest_public_source_population_pass.md` |"
    if row not in text:
        text = text.replace("| v0.8.7 Primary Source Intake Queue | Which source records are ready to be manually populated and confirmed? | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |",
                            "| v0.8.7 Primary Source Intake Queue | Which source records are ready to be manually populated and confirmed? | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |\n" + row)

    section = """## Public Source Population Pass v0.8.8

This layer populates the v0.8.7 intake queue with bounded public source records. The initial source pool is treated as public secondary-source evidence unless a record explicitly marks `primary_source_confirmed: true`.

Primary outputs:

- `sources/primary_source_intake/source_population_manifest_v0_8_8.json`
- `reports/public_source_population/latest_public_source_population_pass.md`
- `reports/public_source_population/latest_public_source_population_pass.json`
- `visuals/public_source_population/v0_8_8/`

Boundary: source population is not source validation. Source validation is not claim promotion. Claim promotion requires evidence gates, independent support, and explicit review.
"""
    text = insert_after(text, "Primary Source Intake Queue v0.8.7", section)

    for metric_row in [
        "| Public source population pass | `reports/public_source_population/latest_public_source_population_pass.md` |",
        "| Public source population manifest | `sources/primary_source_intake/source_population_manifest_v0_8_8.json` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Primary source intake queue | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |",
                                "| Primary source intake queue | `reports/primary_source_intake/latest_primary_source_intake_queue.md` |\n" + metric_row)

    cmd = "python scripts/benchmarks/populate_public_source_intake_v0_8_8.py"
    if cmd not in text:
        text = text.replace("python scripts/benchmarks/run_primary_source_intake_queue.py", "python scripts/benchmarks/run_primary_source_intake_queue.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/public_source_population/` | Public source population reports |", "| `reports/primary_source_intake/` | Primary source intake queue reports |"),
        ("| `visuals/public_source_population/` | Public source population charts |", "| `visuals/primary_source_intake/` | Primary source intake charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/public_source_population/latest_public_source_population_pass.md` | Public source population report |"
    if archive_row not in text:
        text = text.replace("| `reports/primary_source_intake/latest_primary_source_intake_queue.md` | Primary source intake queue report |",
                            "| `reports/primary_source_intake/latest_primary_source_intake_queue.md` | Primary source intake queue report |\n" + archive_row)

    if "| v0.8.8 |" not in text:
        text = text.replace("| v0.8.7 | Primary Source Intake Queue; creates manual source-population manifest without inventing or validating sources. |",
                            "| v0.8.7 | Primary Source Intake Queue; creates manual source-population manifest without inventing or validating sources. |\n| v0.8.8 | Public Source Population Pass; populates source queue with bounded public secondary-source records while preserving primary-validation locks. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.8.9 - Primary Source Validation Gap Review**

Recommended goals:

- Identify which populated source records still need first-party Huawei/HiSilicon/IEEE material.
- Separate secondary-source confidence from primary-source confirmation.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-076 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-076 | v0.8.8 can populate claims from public reporting, but public secondary reporting is not primary validation. | Source population, source validation, and claim promotion are three separate gates. | Always mark public media/source records as secondary unless first-party or independently reproduced evidence is present. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.8.8 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.8.8-readme-public-source-population-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.8.8 - Public Source Population Pass",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/source population patch is source-population scaffold only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_public_source_population_patch_v0_8_8.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_public_source_population_patch_v0_8_8.md", "# README Public Source Population Patch v0.8.8\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/public_source_population/readme_public_source_population_patch_v0_8_8.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()