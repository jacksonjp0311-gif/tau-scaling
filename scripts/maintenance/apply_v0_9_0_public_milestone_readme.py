from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "public_research_milestone"
BACKUP_DIR = REPORT_DIR / "v0_9_0" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_9_0_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.9.0 - Public Research Milestone Package**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.8.9 - Primary Source Validation Gap Review**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v0.9.0 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.9.0-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.9.0 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v0.9.0 Public Research Milestone Package | What publishable package summarizes the v0.8 public Tau research spine? | `reports/public_research_milestone/latest_public_research_milestone.md` |"
    if row not in text:
        text = text.replace("| v0.8.9 Primary Source Gap Review | What primary and independent validation is still missing? | `reports/primary_source_gap_review/latest_primary_source_gap_review.md` |",
                            "| v0.8.9 Primary Source Gap Review | What primary and independent validation is still missing? | `reports/primary_source_gap_review/latest_primary_source_gap_review.md` |\n" + row)

    section = """## Public Research Milestone Package v0.9.0

This layer packages the full v0.8 public Tau research spine into a release-quality research artifact.

Primary outputs:

- `releases/public_research_milestone_v0_9_0/README.md`
- `releases/public_research_milestone_v0_9_0/public_research_milestone_manifest_v0_9_0.json`
- `reports/public_research_milestone/latest_public_research_milestone.md`
- `reports/publishable_findings/latest_publishable_findings_brief.md`
- `visuals/public_research_milestone/v0_9_0/public_research_milestone.svg`

Publishable boundary: this is publishable as a repository-based evidence-governance and source-provenance artifact. It is not silicon validation, product validation, benchmark superiority, process-node equivalence, or proof of a universal Tau Scaling law.
"""
    text = insert_after(text, "Primary Source Validation Gap Review v0.8.9", section)

    for metric_row in [
        "| Public research milestone package | `reports/public_research_milestone/latest_public_research_milestone.md` |",
        "| Public research milestone release | `releases/public_research_milestone_v0_9_0/README.md` |",
        "| Public research milestone visual | `visuals/public_research_milestone/v0_9_0/public_research_milestone.svg` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Publishable findings brief | `reports/publishable_findings/latest_publishable_findings_brief.md` |",
                                "| Publishable findings brief | `reports/publishable_findings/latest_publishable_findings_brief.md` |\n" + metric_row)

    cmd = "python scripts/release/build_public_research_milestone_v0_9_0.py"
    if cmd not in text:
        text = text.replace("python scripts/benchmarks/generate_primary_source_gap_review_v0_8_9.py", "python scripts/benchmarks/generate_primary_source_gap_review_v0_8_9.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/public_research_milestone/` | Public research milestone package reports |", "| `reports/publishable_findings/` | Evidence-bounded publishable findings briefs |"),
        ("| `releases/public_research_milestone_v0_9_0/` | v0.9.0 release-quality public research package |", "| `releases/` | Versioned release outputs |"),
        ("| `visuals/public_research_milestone/` | Public research milestone charts |", "| `visuals/primary_source_gap_review/` | Primary source validation gap charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/public_research_milestone/latest_public_research_milestone.md` | Public research milestone package summary |"
    if archive_row not in text:
        text = text.replace("| `reports/publishable_findings/latest_publishable_findings_brief.md` | Evidence-bounded publishable findings brief |",
                            "| `reports/publishable_findings/latest_publishable_findings_brief.md` | Evidence-bounded publishable findings brief |\n" + archive_row)

    if "| v0.9.0 |" not in text:
        text = text.replace("| v0.8.9 | Primary Source Validation Gap Review; converts public source population into publishable validation-gap findings. |",
                            "| v0.8.9 | Primary Source Validation Gap Review; converts public source population into publishable validation-gap findings. |\n| v0.9.0 | Public Research Milestone Package; packages the full v0.8 public Tau research spine into a release-quality artifact. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.9.1 - Manuscript Draft Scaffold**

Recommended goals:

- Convert the v0.9.0 public research package into a manuscript-style draft.
- Include abstract, method, artifacts, results, limitations, reproducibility, and non-claim locks.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-078 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-078 | v0.9.0 packages the v0.8 spine as a public research artifact. | A package can be publishable when it publishes evidence boundaries, not overclaims. | Milestone packages should preserve claim ledgers, source ledgers, validation gaps, visuals, release checks, and explicit non-claim locks. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.9.0 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.9.0-readme-public-milestone-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.9.0 - Public Research Milestone Package",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/milestone patch is release packaging only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_public_milestone_patch_v0_9_0.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_public_milestone_patch_v0_9_0.md", "# README Public Milestone Patch v0.9.0\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/public_research_milestone/readme_public_milestone_patch_v0_9_0.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()