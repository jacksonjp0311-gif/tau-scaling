from pathlib import Path
from datetime import datetime, timezone

root = Path(r"C:\Users\jacks\OneDrive\Desktop\tau-scaling")
readme = root / "README.md"
text = readme.read_text(encoding="utf-8", errors="replace")

required_heading = "## AI Rule \u2014 Directory Box and Mini README Synchronization"
required_token = "AI Rule \u2014 Directory Box and Mini README Synchronization"

# Remove common mojibake/ASCII variants to prevent duplicated-but-invisible drift.
variants = [
    "## AI Rule â€” Directory Box and Mini README Synchronization",
    "## AI Rule - Directory Box and Mini README Synchronization",
    "## AI Rule -- Directory Box and Mini README Synchronization",
    "## AI Rule – Directory Box and Mini README Synchronization",
]
for v in variants:
    text = text.replace(v, required_heading)

section = f"""
{required_heading}

This exact heading uses a Unicode em dash (U+2014) because `scripts/rcc/audit_readme_surface.py` checks this anchor literally.

This repository uses RCC-N style navigation. Repository structure is part of the public interface.

Any AI or human patch that adds, removes, renames, or repurposes a folder must update these surfaces in the same commit:

1. The root README Full Directory Box.
2. The affected folder-level mini `README.md`.
3. `docs/context/repository_context_index.json` if route meaning changes.
4. `docs/context/rcc_nexus_index.json` if Nexus position changes.
5. `rcc/nexus/route_map.json` if task routing changes.
6. Relevant validation reports after rerunning checks.

Non-claim lock: directory navigation is not correctness, but stale navigation is repository drift.
""".strip() + "\n"

if required_token not in text:
    marker = "## Full Directory Box"
    if marker in text:
        text = text.replace(marker, section + "\n" + marker, 1)
    else:
        text = text.rstrip() + "\n\n" + section

# Add an explicit machine-visible ASCII note too, without replacing the required Unicode anchor.
note = "Required Unicode audit anchor: AI Rule \u2014 Directory Box and Mini README Synchronization"
if note not in text:
    text = text.rstrip() + "\n\n<!-- " + note + " -->\n"

readme.write_text(text, encoding="utf-8")

release = root / "docs" / "release_notes" / "tau_scaling_v0_3_2g_exact_unicode_readme_anchor_repair.md"
release.parent.mkdir(parents=True, exist_ok=True)
release.write_text(f"""# TAU-SCALING-SA v0.3.2g — Exact Unicode README Anchor Repair

Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}

## Purpose

This patch repairs the final README mini repo audit failure by writing the exact required heading:

```text
AI Rule — Directory Box and Mini README Synchronization
```

The failure was not runtime, RCC-N, architecture, test, benchmark, or claim logic. It was exact Unicode anchor visibility.

## Lesson Encoded

When audit scripts check literal Unicode anchors, the patch layer must write the exact Unicode character rather than relying on PowerShell console paste or visually similar dash characters.

## Non-Claim Lock

This is context-surface repair only. It is not runtime correctness proof, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.
""", encoding="utf-8")

status = root / "reports" / "readme" / "latest_v0_3_2g_exact_unicode_readme_anchor_repair_status.md"
status.parent.mkdir(parents=True, exist_ok=True)
status.write_text(f"""# Tau Scaling v0.3.2g Exact Unicode README Anchor Repair Status

Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}

Status: complete

Fix:
- Wrote exact U+2014 README audit anchor with Python.
- Preserved AI Rule / Directory Box / Mini README Synchronization semantics.
- Added release note and status report.

Boundary:
- Context-surface repair only.
- Non-claim locks preserved.
""", encoding="utf-8")