from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "readme_publication_surface"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main() -> None:
    readme = read(ROOT / "README.md")
    graphic = ROOT / "visuals" / "stable_tau_threshold_governance" / "v0_8_0" / "tau_scaling_benchmark_findings_dashboard.svg"
    required = [
        "Current checkpoint: **TAU-SCALING-SA v0.8.1 - Benchmark Finding Publication Surface**",
        "## Tau Doctrine Alignment",
        "Time is the shared metric, not automatic proof.",
        "Topology helps only when overheads are dominated.",
        "Industrial roadmap coherence is not independent validation.",
        "Energy, thermal, yield, PDN/PVT, workload, and method data are required.",
        "## Benchmark Finding - Stable Tau Threshold Governance v0.8.0",
        "The publishable result is **not** that Tau Scaling is independently validated.",
        "defer threshold change pending more evidence",
        "visuals/stable_tau_threshold_governance/v0_8_0/tau_scaling_benchmark_findings_dashboard.svg",
    ]
    missing = [item for item in required if item not in readme]
    passed = len(missing) == 0 and graphic.exists()
    data = {
        "schema": "tau-scaling-readme-benchmark-publication-surface-v0.8.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "publication_status": "README_BENCHMARK_PUBLICATION_SURFACE_READY" if passed else "README_BENCHMARK_PUBLICATION_SURFACE_NEEDS_REPAIR",
        "passed": passed,
        "missing_required_items": missing,
        "graphic_exists": graphic.exists(),
        "graphic_path": "visuals/stable_tau_threshold_governance/v0_8_0/tau_scaling_benchmark_findings_dashboard.svg",
        "thresholds_changed": False,
        "classifier_changed": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "boundary": "README benchmark publication surfaces summarize local runtime governance only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
    }
    md = "# README Benchmark Publication Surface v0.8.1\n\n"
    md += f"Generated: `{data['generated_at']}`\n\n"
    md += "## Status\n\n"
    md += f"- Publication status: `{data['publication_status']}`\n"
    md += f"- Passed: `{data['passed']}`\n"
    md += f"- Graphic exists: `{data['graphic_exists']}`\n"
    md += f"- Graphic path: `{data['graphic_path']}`\n\n"
    md += "## Public Result\n\nTau Scaling can be operationalized as an evidence-gated claim-governance runtime. The v0.8.0 milestone deferred threshold changes pending more evidence; no threshold or classifier mutation occurred.\n\n"
    md += "## Boundary\n\n" + data["boundary"] + "\n"
    write_json(OUT / "readme_benchmark_publication_surface_v0_8_1.json", data)
    write_json(OUT / "latest_readme_benchmark_publication_surface.json", data)
    write(OUT / "readme_benchmark_publication_surface_v0_8_1.md", md)
    write(OUT / "latest_readme_benchmark_publication_surface.md", md)
    print(json.dumps({
        "schema": data["schema"],
        "publication_status": data["publication_status"],
        "passed": data["passed"],
        "graphic_exists": data["graphic_exists"],
        "thresholds_changed": data["thresholds_changed"],
        "classifier_changed": data["classifier_changed"],
        "mutation_allowed": data["mutation_allowed"],
        "application_allowed": data["application_allowed"],
        "calibration_applied": data["calibration_applied"],
        "report": "reports/readme_publication_surface/latest_readme_benchmark_publication_surface.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()