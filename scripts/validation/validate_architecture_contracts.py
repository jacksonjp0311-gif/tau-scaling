from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]

REQUIRED = [
    "docs/software_architecture/tau_scaling_sa_v0_1.md",
    "docs/injections/tau_scaling_rcc_n_injection_v0_2.md",
    "docs/release_notes/tau_scaling_v0_2_rcc_n_structure_injection.md",
    "docs/context/repository_context_index.json",
    "docs/context/rcc_nexus_index.json",
    "rcc/nexus/route_map.json",
    "README.md",
    "AGENTS.md",
]

REQUIRED_PHRASES = {
    "README.md": [
        "PART I - Human README",
        "PART II - RCC Nexus README",
        "PART III - AI Agent README",
        "Roadmap coherence is not validation",
        "Simulation is not silicon evidence",
    ],
    "docs/software_architecture/tau_scaling_sa_v0_1.md": [
        "claim",
        "tau vector",
        "evidence package",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def main() -> int:
    findings = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            findings.append({"severity": "error", "code": "missing_required_architecture_surface", "path": rel})

    for rel, phrases in REQUIRED_PHRASES.items():
        p = ROOT / rel
        if p.exists():
            text = read(p)
            for phrase in phrases:
                if phrase not in text:
                    findings.append({"severity": "warning", "code": "required_phrase_missing", "path": rel, "phrase": phrase})

    errors = sum(1 for f in findings if f["severity"] == "error")
    report = {
        "schema": "tau-scaling-architecture-contract-validation-v0.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "passed": errors == 0,
        "errors": errors,
        "warnings": sum(1 for f in findings if f["severity"] == "warning"),
        "findings": findings,
        "boundary": "Architecture validation is not code correctness or silicon validation."
    }

    out_dir = ROOT / "reports" / "architecture"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "latest_architecture_contract_validation.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    md = [
        "# Latest Architecture Contract Validation",
        "",
        f"- Generated: {report['generated_at']}",
        f"- Passed: {report['passed']}",
        f"- Errors: {report['errors']}",
        f"- Warnings: {report['warnings']}",
        "",
        "Boundary: architecture validation is not code correctness or silicon validation.",
        "",
        "## Findings",
        "",
    ]
    if findings:
        for f in findings:
            md.append(f"- `{f['severity']}` `{f['code']}`: `{json.dumps(f, ensure_ascii=False)}`")
    else:
        md.append("- No findings.")
    (out_dir / "latest_architecture_contract_validation.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())