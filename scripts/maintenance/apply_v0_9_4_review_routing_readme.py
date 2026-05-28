from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "external_review_publication_routing"
BACKUP_DIR = REPORT_DIR / "v0_9_4" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_9_4_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.9.3 - Manuscript Polish and Submission Package**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v0.9.4 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.9.4-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.9.4 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v0.9.4 External Review Checklist and Publication Routing | Which publication route is appropriate and what review gates remain? | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |"
    if row not in text:
        text = text.replace("| v0.9.3 Manuscript Polish and Submission Package | What submission-facing manuscript bundle is ready for review? | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |",
                            "| v0.9.3 Manuscript Polish and Submission Package | What submission-facing manuscript bundle is ready for review? | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |\n" + row)

    section = """## External Review Checklist and Publication Routing v0.9.4

This layer adds external-review and publication-routing surfaces around the submission package.

Primary outputs:

- `docs/review/external_review_checklist_v0_9_4.md`
- `docs/review/reviewer_questions_v0_9_4.md`
- `docs/review/reviewer_response_template_v0_9_4.md`
- `docs/review/publication_routing_v0_9_4.md`
- `docs/review/github_release_checklist_v0_9_4.md`
- `docs/review/gist_technical_note_summary_v0_9_4.md`
- `releases/publication_routing_v0_9_4/`
- `reports/external_review_publication_routing/latest_external_review_publication_routing.md`

Routing decision: GitHub release, Gist summary, and bounded technical note are ready. Preprint is held for external review because primary and independent confirmations remain zero. Claim promotion remains blocked.
"""
    text = insert_after(text, "Manuscript Polish and Submission Package v0.9.3", section)

    for metric_row in [
        "| External review routing | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |",
        "| External review checklist | `docs/review/external_review_checklist_v0_9_4.md` |",
        "| Publication routing | `docs/review/publication_routing_v0_9_4.md` |",
        "| Reviewer response template | `docs/review/reviewer_response_template_v0_9_4.md` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Manuscript submission package | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |",
                                "| Manuscript submission package | `reports/manuscript_submission_package/latest_manuscript_submission_package.md` |\n" + metric_row)

    cmd = "python scripts/release/build_external_review_publication_routing_v0_9_4.py"
    if cmd not in text:
        text = text.replace("python scripts/release/build_manuscript_submission_package_v0_9_3.py", "python scripts/release/build_manuscript_submission_package_v0_9_3.py\n" + cmd)

    for new_row, anchor in [
        ("| `docs/review/` | External review checklist, questions, routing, and response templates |", "| `docs/manuscript/` | Manuscript draft Markdown and LaTeX outputs |"),
        ("| `reports/external_review_publication_routing/` | External review and publication routing reports |", "| `reports/manuscript_submission_package/` | Manuscript polish and submission package reports |"),
        ("| `releases/publication_routing_v0_9_4/` | Publication routing package |", "| `releases/manuscript_submission_package_v0_9_3/` | Submission-facing manuscript package |"),
        ("| `visuals/external_review_publication_routing/` | External review and publication routing charts |", "| `visuals/manuscript_submission_package/` | Manuscript submission-package charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/external_review_publication_routing/latest_external_review_publication_routing.md` | External review checklist and publication routing report |"
    if archive_row not in text:
        text = text.replace("| `reports/manuscript_submission_package/latest_manuscript_submission_package.md` | Manuscript polish and submission package report |",
                            "| `reports/manuscript_submission_package/latest_manuscript_submission_package.md` | Manuscript polish and submission package report |\n" + archive_row)

    if "| v0.9.4 |" not in text:
        text = text.replace("| v0.9.3 | Manuscript Polish and Submission Package; integrates the manuscript, evidence pack, data availability, ethics/non-claim statement, and submission release folder. |",
                            "| v0.9.3 | Manuscript Polish and Submission Package; integrates the manuscript, evidence pack, data availability, ethics/non-claim statement, and submission release folder. |\n| v0.9.4 | External Review Checklist and Publication Routing; adds review gates, reviewer questions, response template, GitHub/Gist/technical-note routing, and preprint hold logic. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v1.0.0 - Public Release Candidate**

Recommended goals:

- Freeze the evidence-governance public release candidate.
- Generate final changelog, version tag notes, and release announcement.
- Confirm all non-claim locks.
- Preserve source-fidelity and no-promotion discipline.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-082 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-082 | v0.9.4 routes publication while blocking claim promotion. | A publication route is not a validation route. | Route GitHub/Gist/technical-note publication before preprint, and keep preprint held until external review confirms the claim boundary. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.9.4 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.9.4-readme-review-routing-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/review-routing patch is publication routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_review_routing_patch_v0_9_4.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_review_routing_patch_v0_9_4.md", "# README Review Routing Patch v0.9.4\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/external_review_publication_routing/readme_review_routing_patch_v0_9_4.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()