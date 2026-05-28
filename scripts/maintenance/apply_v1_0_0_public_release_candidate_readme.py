from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "public_release_candidate"
BACKUP_DIR = REPORT_DIR / "v1_0_0" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v1_0_0_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v1.0.0 - Public Release Candidate**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.9.4 - External Review Checklist and Publication Routing**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v1.0.0 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v1.0.0-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v1.0.0 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v1.0.0 Public Release Candidate | What release candidate freezes the public evidence-governance artifact? | `reports/public_release_candidate/latest_public_release_candidate.md` |"
    if row not in text:
        text = text.replace("| v0.9.4 External Review Checklist and Publication Routing | Which publication route is appropriate and what review gates remain? | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |",
                            "| v0.9.4 External Review Checklist and Publication Routing | Which publication route is appropriate and what review gates remain? | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |\n" + row)

    section = """## Public Release Candidate v1.0.0

This layer freezes the public evidence-governance release candidate.

Primary outputs:

- `releases/public_release_candidate_v1_0_0/README.md`
- `releases/public_release_candidate_v1_0_0/CHANGELOG_v1_0_0.md`
- `releases/public_release_candidate_v1_0_0/GITHUB_RELEASE_BODY_v1_0_0.md`
- `releases/public_release_candidate_v1_0_0/TECHNICAL_NOTE_COPY_v1_0_0.md`
- `releases/public_release_candidate_v1_0_0/PUBLIC_ABSTRACT_v1_0_0.md`
- `releases/public_release_candidate_v1_0_0/VERSION_TAG_NOTES_v1_0_0.md`
- `releases/public_release_candidate_v1_0_0/FINAL_NON_CLAIM_LOCK_AUDIT_v1_0_0.json`
- `reports/public_release_candidate/latest_public_release_candidate.md`

Release boundary: v1.0.0 is a public evidence-governance release candidate. It does not validate sources, promote claims, validate silicon, validate products, or prove a universal Tau Scaling law.
"""
    text = insert_after(text, "External Review Checklist and Publication Routing v0.9.4", section)

    for metric_row in [
        "| Public release candidate | `reports/public_release_candidate/latest_public_release_candidate.md` |",
        "| Release candidate package | `releases/public_release_candidate_v1_0_0/README.md` |",
        "| GitHub release body | `releases/public_release_candidate_v1_0_0/GITHUB_RELEASE_BODY_v1_0_0.md` |",
        "| Public abstract | `releases/public_release_candidate_v1_0_0/PUBLIC_ABSTRACT_v1_0_0.md` |",
    ]:
        if metric_row not in text:
            text = text.replace("| External review routing | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |",
                                "| External review routing | `reports/external_review_publication_routing/latest_external_review_publication_routing.md` |\n" + metric_row)

    cmd = "python scripts/release/build_public_release_candidate_v1_0_0.py"
    if cmd not in text:
        text = text.replace("python scripts/release/build_external_review_publication_routing_v0_9_4.py", "python scripts/release/build_external_review_publication_routing_v0_9_4.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/public_release_candidate/` | Public release candidate reports |", "| `reports/external_review_publication_routing/` | External review and publication routing reports |"),
        ("| `releases/public_release_candidate_v1_0_0/` | Public release candidate package |", "| `releases/publication_routing_v0_9_4/` | Publication routing package |"),
        ("| `visuals/public_release_candidate/` | Public release candidate charts |", "| `visuals/external_review_publication_routing/` | External review and publication routing charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/public_release_candidate/latest_public_release_candidate.md` | Public release candidate report |"
    if archive_row not in text:
        text = text.replace("| `reports/external_review_publication_routing/latest_external_review_publication_routing.md` | External review checklist and publication routing report |",
                            "| `reports/external_review_publication_routing/latest_external_review_publication_routing.md` | External review checklist and publication routing report |\n" + archive_row)

    if "| v1.0.0 |" not in text:
        text = text.replace("| v0.9.4 | External Review Checklist and Publication Routing; adds review gates, reviewer questions, response template, GitHub/Gist/technical-note routing, and preprint hold logic. |",
                            "| v0.9.4 | External Review Checklist and Publication Routing; adds review gates, reviewer questions, response template, GitHub/Gist/technical-note routing, and preprint hold logic. |\n| v1.0.0 | Public Release Candidate; freezes the public evidence-governance artifact with changelog, release body, tag notes, technical-note copy, public abstract, and final non-claim lock audit. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v1.0.1 - Post-Release Review and External Feedback Intake**

Recommended goals:

- Collect external review feedback.
- Record reviewer comments and responses.
- Patch manuscript only if feedback improves clarity without weakening non-claim locks.
- Preserve source-fidelity and no-promotion discipline.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-083 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-083 | v1.0.0 freezes a public release candidate. | A release candidate can be public when its evidence boundaries are stronger than its claims. | Tag and publish only as evidence-governance/source-provenance analysis, not as semiconductor validation. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v1.0.0 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v1.0.0-readme-public-release-candidate-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v1.0.0 - Public Release Candidate",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/public-release-candidate patch is release routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_public_release_candidate_patch_v1_0_0.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_public_release_candidate_patch_v1_0_0.md", "# README Public Release Candidate Patch v1.0.0\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/public_release_candidate/readme_public_release_candidate_patch_v1_0_0.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()