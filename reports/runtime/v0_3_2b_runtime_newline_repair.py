from pathlib import Path
import re
from datetime import datetime, timezone

root = Path(r"C:\Users\jacks\OneDrive\Desktop\tau-scaling")
runtime = root / "src" / "tau_scaling" / "core" / "runtime.py"
backup_dir = root / "reports" / "runtime" / "backups"
backup_dir.mkdir(parents=True, exist_ok=True)
backup = backup_dir / f"runtime_before_v0_3_2b_newline_repair_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.py"
text = runtime.read_text(encoding="utf-8-sig")
backup.write_text(text, encoding="utf-8")

# Repair literal PowerShell escape residue: `n should have been a real newline.
text = text.replace("`r`n", "\n")
text = text.replace("`n", "\n")
text = text.replace("`r", "\n")

# Repair the earlier malformed import if it still exists.
text = text.replace(
    "from tau_scaling.evidence.package import emit_evidence_package from tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id",
    "from tau_scaling.evidence.package import emit_evidence_package\nfrom tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id",
)

# Normalize any line where two imports were accidentally collapsed with whitespace.
text = re.sub(
    r"from tau_scaling\.evidence\.package import emit_evidence_package\s+from tau_scaling\.utils\.run_identity import ensure_unique_run_dir, generate_run_id",
    "from tau_scaling.evidence.package import emit_evidence_package\nfrom tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id",
    text,
)

# Ensure run identity import exists once.
identity_import = "from tau_scaling.utils.run_identity import ensure_unique_run_dir, generate_run_id"
if identity_import not in text:
    marker = "from tau_scaling.evidence.package import emit_evidence_package"
    if marker in text:
        text = text.replace(marker, marker + "\n" + identity_import, 1)
    else:
        text = identity_import + "\n" + text

# De-duplicate consecutive duplicate imports.
lines = text.splitlines()
out = []
seen_imports = set()
for line in lines:
    if line.strip() in {
        "from tau_scaling.evidence.package import emit_evidence_package",
        identity_import,
    }:
        if line.strip() in seen_imports:
            continue
        seen_imports.add(line.strip())
    out.append(line.rstrip())
text = "\n".join(out) + "\n"

runtime.write_text(text, encoding="utf-8")
print(f"repaired: {runtime}")
print(f"backup:   {backup}")