from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

REQUIRED_ROOT_README_SECTIONS = [
    "# Tau Scaling",
    "PART I - Human README",
    "PART II - RCC Nexus README",
    "PART III - AI Agent README",
    "AI Operating Contract",
    "Patch Routing Matrix",
    "README + Mini Repo Audit Map",
    "AI Failure Learning Ledger",
    "AI Rule — Directory Box and Mini README Synchronization",
    "Full Directory Box",
    "Public Non-Claim Locks",
]

REQUIRED_VALIDATION_COMMANDS = [
    "python -m py_compile src/tau_scaling/core/runtime.py",
    "python scripts/rcc/check_rcc_nexus.py",
    "python scripts/rcc/audit_readme_surface.py",
    "python scripts/validation/validate_architecture_contracts.py",
    "python -m unittest discover -s tests",
    "python scripts/benchmarks/run_tau_scaling_benchmarks.py",
]

DURABLE_DIRS_REQUIRING_MINI_README = [
    "artifacts",
    "configs",
    "configs/seeds",
    "docs",
    "docs/architecture",
    "docs/benchmarks",
    "docs/context",
    "docs/injections",
    "docs/protocols",
    "docs/release_notes",
    "docs/software_architecture",
    "docs/theory",
    "examples",
    "outputs",
    "rcc",
    "rcc/nexus",
    "reports",
    "reports/architecture",
    "reports/benchmarks",
    "reports/rcc_nexus",
    "reports/readme",
    "scripts",
    "scripts/benchmarks",
    "scripts/rcc",
    "scripts/validation",
    "src",
    "src/tau_scaling",
    "src/tau_scaling/claims",
    "src/tau_scaling/core",
    "src/tau_scaling/evidence",
    "src/tau_scaling/gates",
    "src/tau_scaling/schemas",
    "src/tau_scaling/simulation",
    "src/tau_scaling/tau",
    "src/tau_scaling/utils",
    "tests",
    "visuals",
    "visuals/tau_scaling",
]

@dataclass
class Finding:
    severity: str
    code: str
    path: str
    detail: str

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def add(findings: list[Finding], severity: str, code: str, path: str, detail: str) -> None:
    findings.append(Finding(severity, code, path, detail))

def check_root_readme(findings: list[Finding]) -> None:
    path = REPO_ROOT / "README.md"
    text = read_text(path)
    if not text:
        add(findings, "error", "root_readme_missing", "README.md", "Root README is missing or unreadable.")
        return

    for section in REQUIRED_ROOT_README_SECTIONS:
        if section not in text:
            add(findings, "error", "root_readme_section_missing", "README.md", f"Missing section/token: {section}")

    for command in REQUIRED_VALIDATION_COMMANDS:
        if command not in text:
            add(findings, "warning", "validation_command_missing", "README.md", f"Missing validation command: {command}")

    if "simulation_is_not_silicon_validation" not in text:
        add(findings, "error", "non_claim_lock_missing", "README.md", "Missing simulation_is_not_silicon_validation lock ID.")

    if not any(v in text for v in ("v0.3.2b", "v0.3.2c", "v0.3.2d")):
        add(findings, "warning", "checkpoint_may_be_stale", "README.md", "README does not mention latest v0.3.2 lineage.")

def check_mini_readmes(findings: list[Finding]) -> None:
    for rel in DURABLE_DIRS_REQUIRING_MINI_README:
        path = REPO_ROOT / rel
        if not path.exists():
            add(findings, "warning", "expected_directory_missing", rel, "Expected durable directory does not exist.")
            continue
        readme = path / "README.md"
        if not readme.exists():
            add(findings, "error", "mini_readme_missing", str(readme.relative_to(REPO_ROOT)), "Durable directory lacks README.md.")
            continue

        text = read_text(readme)
        if len(text.strip()) < 40:
            add(findings, "warning", "mini_readme_too_thin", str(readme.relative_to(REPO_ROOT)), "Mini README is very short.")
        if not any(token in text for token in (
            "README / Mini Repo Audit Rule",
            "Mini README Update Rule",
            "README Update Rule",
            "AI Failure Learning Note",
            "RCC Nexus Echo Location",
        )):
            add(findings, "warning", "mini_readme_lacks_ai_update_rule", str(readme.relative_to(REPO_ROOT)), "Mini README lacks explicit AI/RCC update guidance.")

def check_route_files(findings: list[Finding]) -> None:
    required = [
        "docs/context/repository_context_index.json",
        "docs/context/rcc_nexus_index.json",
        "rcc/nexus/route_map.json",
        "rcc/nexus/task_routing_matrix.md",
        "docs/protocols/readme_mini_repo_audit_protocol.md",
    ]
    for rel in required:
        path = REPO_ROOT / rel
        if not path.exists():
            add(findings, "error", "route_surface_missing", rel, "Required route/context surface is missing.")
            continue
        if path.suffix == ".json":
            try:
                json.loads(read_text(path))
            except Exception as exc:
                add(findings, "error", "route_json_invalid", rel, f"JSON is invalid: {exc}")

def main() -> int:
    findings: list[Finding] = []
    check_root_readme(findings)
    check_mini_readmes(findings)
    check_route_files(findings)

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    report = {
        "schema": "tau-scaling-readme-mini-repo-audit-v0.3.2d",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": "tau-scaling",
        "passed": len(errors) == 0,
        "errors": len(errors),
        "warnings": len(warnings),
        "required_root_sections": REQUIRED_ROOT_README_SECTIONS,
        "durable_dirs_checked": len(DURABLE_DIRS_REQUIRING_MINI_README),
        "findings": [asdict(f) for f in findings],
        "non_claim_lock": "README/mini-repo audit is context alignment, not code correctness or silicon validation.",
    }

    out_dir = REPO_ROOT / "reports" / "readme"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "latest_readme_mini_repo_audit.json"
    md_path = out_dir / "latest_readme_mini_repo_audit.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# README + Mini Repo Audit",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"Passed: `{str(report['passed']).lower()}`",
        f"Errors: `{report['errors']}`",
        f"Warnings: `{report['warnings']}`",
        f"Durable dirs checked: `{report['durable_dirs_checked']}`",
        "",
        "## Findings",
        "",
    ]
    if findings:
        lines.append("| Severity | Code | Path | Detail |")
        lines.append("|---|---|---|---|")
        for f in findings:
            detail = f.detail.replace("|", "\\|")
            lines.append(f"| {f.severity} | `{f.code}` | `{f.path}` | {detail} |")
    else:
        lines.append("No findings.")
    lines.extend([
        "",
        "## Non-Claim Lock",
        "",
        report["non_claim_lock"],
        "",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())