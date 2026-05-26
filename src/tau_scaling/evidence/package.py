from __future__ import annotations

from pathlib import Path
from typing import Any

from tau_scaling.utils.safe_json import write_json, write_text


def _dashboard_svg(class_name: str, score: float, margin: float, gamma: float) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="980" height="420" viewBox="0 0 980 420">
  <rect width="980" height="420" fill="#071018"/>
  <text x="40" y="55" fill="#e7f6ff" font-size="30" font-family="Arial">Tau Scaling Classification Dashboard</text>
  <text x="40" y="105" fill="#8bdcff" font-size="20" font-family="Arial">Class: {class_name}</text>
  <text x="40" y="145" fill="#8bdcff" font-size="20" font-family="Arial">A_TSEK: {score:.4f}</text>
  <text x="40" y="185" fill="#8bdcff" font-size="20" font-family="Arial">LogicFolding margin: {margin:.4f} ps</text>
  <text x="40" y="225" fill="#8bdcff" font-size="20" font-family="Arial">Gamma_tau_ETP: {gamma:.4f}</text>
  <rect x="40" y="270" width="900" height="70" rx="14" fill="#102436" stroke="#2aa8d8"/>
  <text x="70" y="313" fill="#ffffff" font-size="20" font-family="Arial">Roadmap coherence is not validation. Simulation is not silicon evidence.</text>
</svg>
"""


def emit_evidence_package(run_dir: str | Path, evidence: dict[str, Any]) -> Path:
    run_dir = Path(run_dir)
    state_dir = run_dir / "state"
    validation_dir = run_dir / "validation"
    simulation_dir = run_dir / "simulation"
    scoring_dir = run_dir / "scoring"
    reports_dir = run_dir / "reports"
    visuals_dir = run_dir / "visuals"
    ledgers_dir = run_dir / "ledger"

    for d in [state_dir, validation_dir, simulation_dir, scoring_dir, reports_dir, visuals_dir, ledgers_dir]:
        d.mkdir(parents=True, exist_ok=True)

    write_json(state_dir / "source_boundary.json", evidence.get("source_boundary", {}))
    write_json(state_dir / "claim_card.json", evidence.get("claim_card", {}))
    write_json(state_dir / "workload_profile.json", evidence.get("workload_profile", {}))
    write_json(state_dir / "tau_vector.json", evidence.get("tau_vector", {}))

    write_json(validation_dir / "logicfolding_survivability.json", evidence.get("logicfolding_survivability", {}))
    write_json(validation_dir / "edge_surface_boundary.json", evidence.get("edge_surface_boundary", {}))
    write_json(validation_dir / "gamma_tau_etp.json", evidence.get("energy_thermal_pdn_pvt", {}))
    write_json(validation_dir / "pvt_closure.json", evidence.get("pvt_closure", {}))
    write_json(validation_dir / "yield_method_disclosure.json", evidence.get("yield_method_disclosure", {}))

    write_json(simulation_dir / "monte_carlo_summary.json", evidence.get("monte_carlo_stress", {}))
    write_json(scoring_dir / "admissible_claim.json", evidence.get("admissible_claim", {}))
    write_json(scoring_dir / "classifier_result.json", evidence.get("classification", {}))

    findings = evidence.get("classification", {}).get("findings", [])
    import json
    ledger_lines = "\n".join(json.dumps(f, ensure_ascii=False) for f in findings)
    write_text(ledgers_dir / "downgrade_ledger.jsonl", ledger_lines + ("\n" if ledger_lines else ""))

    class_name = evidence.get("classification", {}).get("class", "UNKNOWN")
    score = float(evidence.get("admissible_claim", {}).get("A_TSEK", 0.0))
    margin = float(evidence.get("logicfolding_survivability", {}).get("logicfolding_margin", 0.0))
    gamma = float(evidence.get("energy_thermal_pdn_pvt", {}).get("gamma_tau_ETP", 0.0))

    report = f"""# Tau Scaling Run Summary

## Classification

- Class: `{class_name}`
- A_TSEK: `{score:.4f}`
- LogicFolding margin: `{margin:.4f} ps`
- Gamma_tau_ETP: `{gamma:.4f}`

## Non-claim locks

- Roadmap coherence is not validation.
- Simulation is not silicon evidence.
- Density equivalence is not node equivalence.
- Local path win is not full-chip win.
"""
    write_text(reports_dir / "tau_scaling_summary.md", report)
    write_text(reports_dir / "non_claim_locks.md", "# Non-Claim Locks\n\nRoadmap coherence is not validation.\nSimulation is not silicon evidence.\n")
    write_text(visuals_dir / "classification_dashboard.svg", _dashboard_svg(class_name, score, margin, gamma))

    evidence_path = run_dir / "evidence_package.json"
    write_json(evidence_path, evidence)
    return evidence_path
