from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
README = ROOT / "README.md"
REPORT_DIR = ROOT / "reports" / "manuscript_evidence_pack"
BACKUP_DIR = REPORT_DIR / "v0_9_2" / "backups"

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
    write(BACKUP_DIR / f"{path.name}_before_v0_9_2_{stamp}.bak", read(path))

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
    text = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.9.2 - Manuscript Evidence Table and Figure Pack**", text)
    text = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v[0-9.]+[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.9.1 - Manuscript Draft Scaffold**", text)
    text = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v[0-9A-Za-z.]+ \|", "| Current checkpoint | TAU-SCALING-SA v0.9.2 |", text)
    text = re.sub(r"\| Task routing matrix \| .*?\|", "| Task routing matrix | geometry-aware / v0.9.2-ready |", text)
    text = re.sub(r"\| Agent contract version sync \| .*?\|", "| Agent contract version sync | current / v0.9.2 |", text)
    text = re.sub(r"## AI Rule .*? Directory Box and Mini README Synchronization", EXACT_AI_RULE, text)

    row = "| v0.9.2 Manuscript Evidence Table and Figure Pack | What tables, captions, limitations, and artifact maps support the manuscript? | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |"
    if row not in text:
        text = text.replace("| v0.9.1 Manuscript Draft Scaffold | What paper-style draft is generated from the public research package? | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md` |",
                            "| v0.9.1 Manuscript Draft Scaffold | What paper-style draft is generated from the public research package? | `docs/manuscript/tau_scaling_public_claim_system_v0_9_1.md` |\n" + row)

    section = """## Manuscript Evidence Table and Figure Pack v0.9.2

This layer adds manuscript-ready tables, figure captions, limitation tables, artifact maps, and a paper-ready result summary.

Primary outputs:

- `docs/manuscript/evidence_table_v0_9_2.md`
- `docs/manuscript/evidence_table_v0_9_2.tex`
- `docs/manuscript/figure_pack_v0_9_2.md`
- `docs/manuscript/limitations_table_v0_9_2.md`
- `docs/manuscript/artifact_map_v0_9_2.md`
- `docs/manuscript/paper_ready_results_summary_v0_9_2.md`
- `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md`
- `visuals/manuscript_evidence_pack/v0_9_2/manuscript_evidence_pack.svg`

Publishable boundary: these tables and captions improve manuscript readability. They do not validate sources, promote claims, validate silicon, validate products, or prove a universal Tau Scaling law.
"""
    text = insert_after(text, "Manuscript Draft Scaffold v0.9.1", section)

    for metric_row in [
        "| Manuscript evidence pack | `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` |",
        "| Manuscript evidence table | `docs/manuscript/evidence_table_v0_9_2.md` |",
        "| Manuscript figure pack | `docs/manuscript/figure_pack_v0_9_2.md` |",
        "| Paper-ready result summary | `docs/manuscript/paper_ready_results_summary_v0_9_2.md` |",
    ]:
        if metric_row not in text:
            text = text.replace("| Manuscript draft scaffold | `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` |",
                                "| Manuscript draft scaffold | `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` |\n" + metric_row)

    cmd = "python scripts/release/build_manuscript_evidence_pack_v0_9_2.py"
    if cmd not in text:
        text = text.replace("python scripts/release/build_manuscript_draft_scaffold_v0_9_1.py", "python scripts/release/build_manuscript_draft_scaffold_v0_9_1.py\n" + cmd)

    for new_row, anchor in [
        ("| `reports/manuscript_evidence_pack/` | Manuscript evidence table and figure-pack reports |", "| `reports/manuscript_draft/` | Manuscript draft scaffold reports |"),
        ("| `visuals/manuscript_evidence_pack/` | Manuscript evidence-pack charts |", "| `visuals/manuscript_draft/` | Manuscript draft charts |"),
    ]:
        if new_row not in text:
            text = text.replace(anchor, anchor + "\n" + new_row)

    archive_row = "| `reports/manuscript_evidence_pack/latest_manuscript_evidence_pack.md` | Manuscript evidence table and figure pack report |"
    if archive_row not in text:
        text = text.replace("| `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` | Manuscript draft scaffold report |",
                            "| `reports/manuscript_draft/latest_manuscript_draft_scaffold.md` | Manuscript draft scaffold report |\n" + archive_row)

    if "| v0.9.2 |" not in text:
        text = text.replace("| v0.9.1 | Manuscript Draft Scaffold; converts the public research milestone package into Markdown and LaTeX manuscript drafts. |",
                            "| v0.9.1 | Manuscript Draft Scaffold; converts the public research milestone package into Markdown and LaTeX manuscript drafts. |\n| v0.9.2 | Manuscript Evidence Table and Figure Pack; adds paper-ready evidence tables, captions, limitations, artifact map, and result summary. |")

    text = re.sub(
        r"## Next Recommended Version\s+.*\Z",
        """## Next Recommended Version

**TAU-SCALING-SA v0.9.3 - Manuscript Polish and Submission Package**

Recommended goals:

- Integrate evidence table and figure pack into the manuscript body.
- Add polished abstract, contribution statement, limitations paragraph, and data availability statement.
- Produce a submission-ready Markdown/LaTeX pair.
- Preserve source-fidelity and non-claim locks.
- Keep threshold and classifier mutation disabled.
- Preserve `mutation_allowed: false`.
""",
        text,
        flags=re.S,
    )

    if "| L-080 |" not in text:
        start = text.find("### Current Lessons")
        end = text.find("### Failure Response Protocol")
        if start != -1 and end != -1 and end > start:
            lesson = "| L-080 | v0.9.2 adds manuscript tables and captions. | Presentation can strengthen auditability without strengthening the claim itself. | Tables and figures must preserve the distinction between source-populated, source-validated, and claim-promoted. |"
            text = text[:end] + lesson + "\n\n" + text[end:]

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise RuntimeError(f"v0.9.2 README patch would remove required anchors: {missing}")

    write(README, text)
    report = {
        "schema": "tau-scaling-v0.9.2-readme-evidence-pack-patch",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checkpoint": "TAU-SCALING-SA v0.9.2 - Manuscript Evidence Table and Figure Pack",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "claim_promotion_allowed": False,
        "source_validation_claimed": False,
        "boundary": "README/evidence-pack patch is manuscript-support routing only. It does not validate or promote claims.",
    }
    write(REPORT_DIR / "readme_evidence_pack_patch_v0_9_2.json", json.dumps(report, indent=2, sort_keys=True) + "\n")
    write(REPORT_DIR / "readme_evidence_pack_patch_v0_9_2.md", "# README Evidence Pack Patch v0.9.2\n\nBoundary: " + report["boundary"] + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "thresholds_changed": report["thresholds_changed"],
        "classifier_changed": report["classifier_changed"],
        "mutation_allowed": report["mutation_allowed"],
        "application_allowed": report["application_allowed"],
        "claim_promotion_allowed": report["claim_promotion_allowed"],
        "source_validation_claimed": report["source_validation_claimed"],
        "report": "reports/manuscript_evidence_pack/readme_evidence_pack_patch_v0_9_2.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()