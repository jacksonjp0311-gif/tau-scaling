from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "README.md",
    "README_90_SECONDS.md",
    "AGENTS.md",
    "docs/context/repository_context_index.json",
    "docs/context/rcc_nexus_index.json",
    "docs/context/validation_surface.md",
    "rcc/nexus/route_map.json",
    "rcc/nexus/rcc_nexus_protocol.md",
    "rcc/nexus/task_routing_matrix.md",
    "rcc/nexus/echo_location_template.md",
    "rcc/nexus/agent_handoff_contract.md",
]

MAJOR_DIRS = [
    "configs",
    "docs",
    "docs/context",
    "docs/software_architecture",
    "docs/injections",
    "rcc",
    "rcc/nexus",
    "src",
    "src/tau_scaling",
    "src/tau_scaling/core",
    "src/tau_scaling/claims",
    "src/tau_scaling/gates",
    "src/tau_scaling/simulation",
    "src/tau_scaling/evidence",
    "examples",
    "tests",
    "artifacts",
    "outputs",
    "reports",
    "reports/rcc_nexus",
    "scripts",
    "scripts/rcc",
    "scripts/validation",
    "visuals",
    "visuals/tau_scaling",
]

LOCKS = [
    "navigation_is_not_validation",
    "documentation_is_not_correctness",
    "simulation_is_not_silicon_validation",
    "density_equivalence_is_not_node_equivalence",
    "local_path_win_is_not_full_chip_win",
    "validation_remains_required",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def main() -> int:
    findings = []

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if not p.exists():
            findings.append({"severity": "error", "code": "missing_required_file", "path": rel})

    missing_readmes = []
    weak_readmes = []
    for rel in MAJOR_DIRS:
        p = ROOT / rel / "README.md"
        if not p.exists():
            missing_readmes.append(rel)
        else:
            text = read_text(p)
            needed = ["Folder Purpose", "RCC Nexus Echo Location", "Non-Claim Locks", "Validation Surface"]
            missing_sections = [s for s in needed if s not in text]
            if missing_sections:
                weak_readmes.append({"path": rel, "missing_sections": missing_sections})

    if missing_readmes:
        findings.append({"severity": "error", "code": "missing_mini_readmes", "paths": missing_readmes})

    if weak_readmes:
        findings.append({"severity": "warning", "code": "weak_mini_readmes", "items": weak_readmes})

    root = ROOT / "README.md"
    if root.exists():
        text = read_text(root)
        for section in ["PART I - Human README", "PART II - RCC Nexus README", "PART III - AI Agent README"]:
            if section not in text:
                findings.append({"severity": "error", "code": "readme_trisection_missing", "section": section})
        for lock in LOCKS:
            if lock not in text and lock.replace("_", " ") not in text.lower():
                findings.append({"severity": "warning", "code": "lock_not_visible_in_root_readme", "lock": lock})

    for rel in ["docs/context/repository_context_index.json", "docs/context/rcc_nexus_index.json", "rcc/nexus/route_map.json"]:
        p = ROOT / rel
        if p.exists():
            try:
                json.loads(read_text(p))
            except Exception as exc:
                findings.append({"severity": "error", "code": "invalid_json", "path": rel, "error": str(exc)})

    error_count = sum(1 for f in findings if f["severity"] == "error")
    warning_count = sum(1 for f in findings if f["severity"] == "warning")

    report = {
        "schema": "tau-scaling-rcc-nexus-check-v0.2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": "tau-scaling",
        "profile": "Full",
        "major_dirs_checked": len(MAJOR_DIRS),
        "mini_readme_coverage": (len(MAJOR_DIRS) - len(missing_readmes)) / len(MAJOR_DIRS),
        "errors": error_count,
        "warnings": warning_count,
        "passed": error_count == 0,
        "findings": findings,
        "non_claim_lock": "RCC-N navigation is not code correctness or silicon validation."
    }

    out_dir = ROOT / "reports" / "rcc_nexus"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "latest_rcc_nexus_check.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = [
        "# Latest RCC Nexus Check",
        "",
        f"- Generated: {report['generated_at']}",
        f"- Profile: {report['profile']}",
        f"- Mini README coverage: {report['mini_readme_coverage']:.3f}",
        f"- Errors: {error_count}",
        f"- Warnings: {warning_count}",
        f"- Passed: {report['passed']}",
        "",
        "## Boundary",
        "",
        "RCC-N checks repository navigation and context integrity. They do not prove code correctness or independent silicon validation.",
        "",
        "## Findings",
        "",
    ]
    if findings:
        for f in findings:
            md.append(f"- `{f['severity']}` `{f['code']}`: `{json.dumps(f, ensure_ascii=False)}`")
    else:
        md.append("- No findings.")
    (out_dir / "latest_rcc_nexus_check.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    drift_dir = ROOT / "docs" / "context" / "drift"
    drift_dir.mkdir(parents=True, exist_ok=True)
    (drift_dir / "latest_rcc_nexus_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())