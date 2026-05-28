from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "manuscript_draft"
BACKUP_DIR = REPORT_DIR / "v0_9_1" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_9_1_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.9.1 - Manuscript Draft Scaffold**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.9.0 - Public Research Milestone Package**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v0.9.1 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.9.1-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.9.1 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v0.9.1 Manuscript Draft Scaffold | What paper-style draft is generated from the public research package? | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md` |"
    if row not in text:
        text = text.replace("| v0.9.0 Public Research Milestone Package | What publishable package summarizes the v0.8 public Tau research spine? | `reports/public_research_milestone/latest_public_research_milestone.md` |",
                            "| v0.9.0 Public Research Milestone Package | What publishable package summarizes the v0.8 public Tau research spine? | `reports/public_research_milestone/latest_public_research_milestone.md` |\n" + row)

    section = """## Manuscript Draft Scaffold v0.9.1

This layer converts the v0.9.0 public research milestone package into a paper-style manuscript scaffold.

Primary outputs:

- `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md`
- `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.tex`
- `reports/manuscript_draft/latest_manuscript_draft_scaffold.md`
- `visuals/manuscript_draft/v0_9_1/manuscript_draft_scaffold.svg`

Publishable boundary: the manuscript is a source-provenance and evidence-governance draft. It is not silicon validation, product validation, benchmark superiority, process-node equivalence, or proof of a universal Tau Scaling law.
"""
    text = insert_after(text, "Public Research Milestone Package v0.9.0", section)

    for metric_row in [
        "| Manuscript draft scaffold | `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` |",
        "| Manuscript Markdown | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md` |",
        "| Manuscript LaTeX | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.tex` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Public research milestone package | `reports/public_research_milestone/latest_public_research_milestone.md` |",
                                "| Public research milestone package | `reports/public_research_milestone/latest_public_research_milestone.md` |\n" + metric_row)

    cmd = "python scripts/release/build_manuscript_draft_scaffold_v0_9_1.py"
    if cmd not in text:
        text = text.replace("python scripts/release/build_public_research_milestone_v0_9_0.py", "python scripts/release/build_public_research_milestone_v0_9_0.py\n" + cmd)

    for new_row, anchor in [
        ("| `docs/manuscript/` | Manuscript draft Markdown and LaTeX outputs |", "| `docs/` | Documentation, methods, context, and release notes |"),
        ("| `reports/manuscript_draft/` | Manuscript draft scaffold reports |", "| `reports/public_research_milestone/` | Public research milestone package reports |"),
        ("| `visuals/manuscript_draft/` | Manuscript draft charts |", "| `visuals/public_research_milestone/` | Public research milestone charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` | Manuscript draft scaffold report |"
    if archive_row not in text:
        text = text.replace("| `reports/public_research_milestone/latest_public_research_milestone.md` | Public research milestone package summary |",
                            "| `reports/public_research_milestone/latest_public_research_milestone.md` | Public research milestone package summary |\n" + archive_row)

    if "| v0.9.1 |" not in text:
        text = text.replace("| v0.9.0 | Public Research Milestone Package; packages the full v0.8 public Tau research spine into a release-quality artifact. |",
                            "| v0.9.0 | Public Research Milestone Package; packages the full v0.8 public Tau research spine into a release-quality artifact. |\n| v0.9.1 | Manuscript Draft Scaffold; converts the public research milestone package into Markdown and LaTeX manuscript drafts. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.9.2 - Manuscript Evidence Table and Figure Pack**

Recommended goals:

- Add manuscript-ready tables and figure captions.
- Generate a compact evidence table for the paper body.
- Generate figure index, caption list, and limitations table.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-079 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-079 | v0.9.1 converts the package into a manuscript scaffold. | A manuscript can publish the evidence machine without turning the evidence machine into a validation claim. | Paper drafts must keep abstract, results, limitations, reproducibility, and non-claim locks aligned. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.9.1 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.9.1-readme-manuscript-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.9.1 - Manuscript Draft Scaffold",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/manuscript patch is draft routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_manuscript_patch_v0_9_1.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_manuscript_patch_v0_9_1.md", "# README Manuscript Patch v0.9.1\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/manuscript_draft/readme_manuscript_patch_v0_9_1.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()