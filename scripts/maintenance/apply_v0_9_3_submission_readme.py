from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "manuscript_submission_package"
BACKUP_DIR = REPORT_DIR / "v0_9_3" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_9_3_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.9.3 - Manuscript Polish and Submission Package**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.9.2 - Manuscript Evidence Table and Figure Pack**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v0.9.3 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.9.3-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.9.3 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v0.9.3 Manuscript Polish and Submission Package | What submission-facing manuscript bundle is ready for review? | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |"
    if row not in text:
        text = text.replace("| v0.9.2 Manuscript Evidence Table and Figure Pack | What tables, captions, limitations, and artifact maps support the manuscript? | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |",
                            "| v0.9.2 Manuscript Evidence Table and Figure Pack | What tables, captions, limitations, and artifact maps support the manuscript? | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |\n" + row)

    section = """## Manuscript Polish and Submission Package v0.9.3

This layer integrates the manuscript draft and evidence pack into a submission-facing package.

Primary outputs:

- `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.md`
- `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.tex`
- `releases/manuscript_submission_package_v0_9_3/README.md`
- `releases/manuscript_submission_package_v0_9_3/DATA_AVAILABILITY.md`
- `releases/manuscript_submission_package_v0_9_3/ETHICS_AND_NON_CLAIM_STATEMENT.md`
- `reports/manuscript_submission_package/latest_manuscript_submission_package.md`
- `visuals/manuscript_submission_package/v0_9_3/manuscript_submission_package.svg`

Submission boundary: this is a manuscript communication package for evidence-governance findings. It does not validate sources, promote claims, validate silicon, validate products, or prove a universal Tau Scaling law.
"""
    text = insert_after(text, "Manuscript Evidence Table and Figure Pack v0.9.2", section)

    for metric_row in [
        "| Manuscript submission package | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |",
        "| Polished manuscript Markdown | `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.md` |",
        "| Polished manuscript LaTeX | `docs/manuscript/tau_scaling_public_claim_system_v0_9_3.tex` |",
        "| Submission package release | `releases/manuscript_submission_package_v0_9_3/README.md` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Manuscript evidence pack | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |",
                                "| Manuscript evidence pack | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |\n" + metric_row)

    cmd = "python scripts/release/build_manuscript_submission_package_v0_9_3.py"
    if cmd not in text:
        text = text.replace("python scripts/release/build_manuscript_evidence_pack_v0_9_2.py", "python scripts/release/build_manuscript_evidence_pack_v0_9_2.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/manuscript_submission_package/` | Manuscript polish and submission package reports |", "| `reports/manuscript_evidence_pack/` | Manuscript evidence table and figure-pack reports |"),
        ("| `releases/manuscript_submission_package_v0_9_3/` | Submission-facing manuscript package |", "| `releases/public_research_milestone_v0_9_0/` | v0.9.0 release-quality public research package |"),
        ("| `visuals/manuscript_submission_package/` | Manuscript submission-package charts |", "| `visuals/manuscript_evidence_pack/` | Manuscript evidence-pack charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/manuscript_submission_package/latest_manuscript_submission_package.md` | Manuscript polish and submission package report |"
    if archive_row not in text:
        text = text.replace("| `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` | Manuscript evidence table and figure pack report |",
                            "| `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` | Manuscript evidence table and figure pack report |\n" + archive_row)

    if "| v0.9.3 |" not in text:
        text = text.replace("| v0.9.2 | Manuscript Evidence Table and Figure Pack; adds paper-ready evidence tables, captions, limitations, artifact map, and result summary. |",
                            "| v0.9.2 | Manuscript Evidence Table and Figure Pack; adds paper-ready evidence tables, captions, limitations, artifact map, and result summary. |\n| v0.9.3 | Manuscript Polish and Submission Package; integrates the manuscript, evidence pack, data availability, ethics/non-claim statement, and submission release folder. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing**

Recommended goals:

- Add external review checklist.
- Add publication routing options: GitHub release, gist, preprint draft, technical note.
- Add reviewer questions and response template.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-081 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-081 | v0.9.3 creates a submission-facing manuscript package. | Submission packaging must make the claim boundary easier to see, not easier to bypass. | Keep data availability, ethics/non-claim statement, release checks, and evidence tables beside the manuscript. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.9.3 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.9.3-readme-submission-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.9.3 - Manuscript Polish and Submission Package",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/submission patch is manuscript-routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_submission_patch_v0_9_3.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_submission_patch_v0_9_3.md", "# README Submission Patch v0.9.3\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/manuscript_submission_package/readme_submission_patch_v0_9_3.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()