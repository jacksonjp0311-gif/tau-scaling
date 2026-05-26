from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
REPORT_DIR = REPO_ROOT / "reports" / "release"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class StepResult:
    name: str
    command: list[str]
    passed: bool
    exit_code: int
    elapsed_ms: float
    stdout_tail: str
    stderr_tail: str
    parsed: dict[str, Any] | None = None


def tail(text: str, limit: int = 5000) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    return text[-limit:]


def run_step(name: str, command: list[str]) -> StepResult:
    start = time.perf_counter()
    proc = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
    )
    elapsed = (time.perf_counter() - start) * 1000.0
    parsed = parse_stdout_json(proc.stdout)
    return StepResult(
        name=name,
        command=command,
        passed=proc.returncode == 0,
        exit_code=proc.returncode,
        elapsed_ms=round(elapsed, 3),
        stdout_tail=tail(proc.stdout),
        stderr_tail=tail(proc.stderr),
        parsed=parsed,
    )


def parse_stdout_json(stdout: str) -> dict[str, Any] | None:
    if not stdout:
        return None
    text = stdout.strip()
    # First try whole stdout.
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    # Then try last JSON object-looking block.
    start = text.rfind("{")
    if start >= 0:
        candidate = text[start:]
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except Exception:
            pass
    return None


def extract_claim_summary(stdout: str) -> dict[str, Any]:
    summary: dict[str, Any] = {}
    for line in stdout.splitlines():
        line = line.strip()
        if line.startswith("run_id:"):
            summary["run_id"] = line.split(":", 1)[1].strip()
        elif line.startswith("class:"):
            summary["class"] = line.split(":", 1)[1].strip()
        elif line.startswith("A_TSEK:"):
            value = line.split(":", 1)[1].strip()
            try:
                summary["A_TSEK"] = float(value)
            except ValueError:
                summary["A_TSEK"] = value
        elif line.startswith("findings:"):
            value = line.split(":", 1)[1].strip()
            try:
                summary["findings"] = int(value)
            except ValueError:
                summary["findings"] = value
        elif line.startswith("artifacts:"):
            summary["artifacts"] = line.split(":", 1)[1].strip()
        elif line.startswith("evidence:"):
            summary["evidence"] = line.split(":", 1)[1].strip()
    return summary


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def check_expected_artifacts() -> list[dict[str, str]]:
    required = [
        "reports/rcc_nexus/latest_rcc_nexus_check.json",
        "reports/rcc_nexus/latest_rcc_nexus_check.md",
        "reports/readme/latest_readme_mini_repo_audit.json",
        "reports/readme/latest_readme_mini_repo_audit.md",
        "reports/architecture/latest_architecture_contract_validation.json",
        "reports/architecture/latest_architecture_contract_validation.md",
        "reports/benchmarks/latest_benchmark_summary.json",
        "reports/benchmarks/latest_benchmark_summary.md",
    ]
    findings: list[dict[str, str]] = []
    for rel in required:
        path = REPO_ROOT / rel
        if not path.exists():
            findings.append({"severity": "error", "code": "expected_artifact_missing", "path": rel})
    return findings


def inspect_readme_for_mojibake() -> list[dict[str, str]]:
    path = REPO_ROOT / "README.md"
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    bad_tokens = ["Ã", "Â", "â€", " ", "\ncc/nexus", "\neports/", "\nests/"]
    findings: list[dict[str, str]] = []
    for token in bad_tokens:
        if token in text:
            display = token.encode("unicode_escape").decode("ascii")
            findings.append({
                "severity": "warning",
                "code": "possible_mojibake_or_path_break",
                "path": "README.md",
                "detail": f"Found token: {display}",
            })
    return findings


def main() -> int:
    python = sys.executable
    steps: list[StepResult] = []

    commands: list[tuple[str, list[str]]] = [
        ("compile_runtime", [python, "-m", "py_compile", "src/tau_scaling/core/runtime.py"]),
        ("import_runtime", [python, "-c", "from tau_scaling.core.runtime import TauScalingRuntime; print('TauScalingRuntime import OK')"]),
        ("rcc_nexus_check", [python, "scripts/rcc/check_rcc_nexus.py"]),
        ("readme_mini_repo_audit", [python, "scripts/rcc/audit_readme_surface.py"]),
        ("architecture_contract_validation", [python, "scripts/validation/validate_architecture_contracts.py"]),
        ("unit_tests", [python, "-m", "unittest", "discover", "-s", "tests"]),
        ("benchmark_harness", [python, "scripts/benchmarks/run_tau_scaling_benchmarks.py"]),
        ("baseline_claim", [python, "-m", "tau_scaling", "run-claim", "--seed", "configs/seeds/logicfolding_claim_card.json"]),
        ("promotion_path_claim", [python, "-m", "tau_scaling", "run-claim", "--seed", "configs/seeds/logicfolding_promotion_path_claim_card.json"]),
    ]

    for name, command in commands:
        result = run_step(name, command)
        if name.endswith("_claim"):
            result.parsed = extract_claim_summary(result.stdout_tail)
        steps.append(result)

    benchmark_json = read_json(REPO_ROOT / "reports/benchmarks/latest_benchmark_summary.json")
    rcc_json = read_json(REPO_ROOT / "reports/rcc_nexus/latest_rcc_nexus_check.json")
    readme_audit_json = read_json(REPO_ROOT / "reports/readme/latest_readme_mini_repo_audit.json")
    architecture_json = read_json(REPO_ROOT / "reports/architecture/latest_architecture_contract_validation.json")

    findings: list[dict[str, Any]] = []
    findings.extend(check_expected_artifacts())
    findings.extend(inspect_readme_for_mojibake())

    if benchmark_json:
        if not benchmark_json.get("collision_proof_run_identity_passed", False):
            findings.append({"severity": "error", "code": "benchmark_collision_identity_failed", "path": "reports/benchmarks/latest_benchmark_summary.json"})
        if benchmark_json.get("duplicate_run_ids"):
            findings.append({"severity": "error", "code": "duplicate_run_ids_present", "path": "reports/benchmarks/latest_benchmark_summary.json"})
    else:
        findings.append({"severity": "error", "code": "benchmark_summary_unreadable", "path": "reports/benchmarks/latest_benchmark_summary.json"})

    for label, obj, path in [
        ("rcc", rcc_json, "reports/rcc_nexus/latest_rcc_nexus_check.json"),
        ("readme_audit", readme_audit_json, "reports/readme/latest_readme_mini_repo_audit.json"),
        ("architecture", architecture_json, "reports/architecture/latest_architecture_contract_validation.json"),
    ]:
        if not obj:
            findings.append({"severity": "error", "code": f"{label}_json_unreadable", "path": path})
        elif not obj.get("passed", False):
            findings.append({"severity": "error", "code": f"{label}_reported_failed", "path": path})

    baseline = next((s for s in steps if s.name == "baseline_claim"), None)
    promotion = next((s for s in steps if s.name == "promotion_path_claim"), None)
    if baseline and baseline.parsed and baseline.parsed.get("class") != "TSEK-C":
        findings.append({"severity": "warning", "code": "baseline_class_changed", "path": "configs/seeds/logicfolding_claim_card.json", "detail": str(baseline.parsed)})
    if promotion and promotion.parsed and promotion.parsed.get("class") != "TSEK-B":
        findings.append({"severity": "warning", "code": "promotion_class_changed", "path": "configs/seeds/logicfolding_promotion_path_claim_card.json", "detail": str(promotion.parsed)})

    step_failures = [asdict(s) for s in steps if not s.passed]
    errors = [f for f in findings if f.get("severity") == "error"]

    report = {
        "schema": "tau-scaling-unified-release-readiness-v0.3.3",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": "tau-scaling",
        "checkpoint": "TAU-SCALING-SA v0.3.3 — Unified Release Validator",
        "passed": len(step_failures) == 0 and len(errors) == 0,
        "step_count": len(steps),
        "step_failures": step_failures,
        "findings": findings,
        "steps": [asdict(s) for s in steps],
        "summaries": {
            "rcc": rcc_json,
            "readme_audit": readme_audit_json,
            "architecture": architecture_json,
            "benchmark": benchmark_json,
            "baseline_claim": baseline.parsed if baseline else None,
            "promotion_path_claim": promotion.parsed if promotion else None,
        },
        "non_claim_lock": (
            "Release readiness validates repository/runtime hygiene only. "
            "It is not silicon validation, product validation, manufacturing validation, "
            "process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof."
        ),
    }

    json_path = REPORT_DIR / "latest_release_readiness.json"
    md_path = REPORT_DIR / "latest_release_readiness.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines: list[str] = []
    lines.append("# Tau Scaling Unified Release Readiness")
    lines.append("")
    lines.append(f"Generated: `{report['generated_at']}`")
    lines.append("")
    lines.append(f"Passed: `{str(report['passed']).lower()}`")
    lines.append(f"Step count: `{report['step_count']}`")
    lines.append(f"Step failures: `{len(step_failures)}`")
    lines.append(f"Findings: `{len(findings)}`")
    lines.append("")
    lines.append("## Step Summary")
    lines.append("")
    lines.append("| Step | Passed | Exit | Elapsed ms |")
    lines.append("|---|---:|---:|---:|")
    for step in steps:
        lines.append(f"| `{step.name}` | `{str(step.passed).lower()}` | `{step.exit_code}` | `{step.elapsed_ms}` |")
    lines.append("")
    lines.append("## Claim Summary")
    lines.append("")
    for key in ["baseline_claim", "promotion_path_claim"]:
        lines.append(f"### {key}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(report["summaries"].get(key), indent=2, sort_keys=True))
        lines.append("```")
        lines.append("")
    lines.append("## Benchmark Summary")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(benchmark_json, indent=2, sort_keys=True))
    lines.append("```")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    if findings:
        lines.append("| Severity | Code | Path | Detail |")
        lines.append("|---|---|---|---|")
        for f in findings:
            detail = str(f.get("detail", "")).replace("|", "\\|")
            lines.append(f"| {f.get('severity')} | `{f.get('code')}` | `{f.get('path', '')}` | {detail} |")
    else:
        lines.append("No findings.")
    lines.append("")
    lines.append("## Non-Claim Lock")
    lines.append("")
    lines.append(report["non_claim_lock"])
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({
        "schema": report["schema"],
        "passed": report["passed"],
        "step_failures": len(step_failures),
        "findings": len(findings),
        "json": str(json_path.relative_to(REPO_ROOT)),
        "markdown": str(md_path.relative_to(REPO_ROOT)),
        "non_claim_lock": report["non_claim_lock"],
    }, indent=2, sort_keys=True))

    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())