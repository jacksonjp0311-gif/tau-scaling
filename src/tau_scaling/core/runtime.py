from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tau_scaling.claims.classifier import classify_tsek
from tau_scaling.gates.logicfolding_survivability import logicfolding_margin
from tau_scaling.gates.gamma_tau_etp import gamma_tau_etp
from tau_scaling.gates.edge_surface import edge_surface_ratio
from tau_scaling.simulation.monte_carlo import run_monte_carlo
from tau_scaling.evidence.package import emit_evidence_package


@dataclass
class TauScalingRunResult:
    run_id: str
    run_dir: str
    evidence_path: str
    classification: str
    admissible_score: float
    findings_count: int


class TauScalingRuntime:
    def __init__(self, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root).resolve()

    def run(self, seed: dict[str, Any]) -> TauScalingRunResult:
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_dir = self.repo_root / "artifacts" / "runs" / run_id

        logicfolding = seed.get("logicfolding_survivability", {})
        normalization = seed.get("energy_thermal_pdn_pvt", {})

        lf_margin = logicfolding_margin(logicfolding)
        gamma = gamma_tau_etp(normalization)
        beta = edge_surface_ratio(seed.get("edge_surface_boundary", {}))
        stress = run_monte_carlo(seed.get("monte_carlo_stress", {}))

        gate_record = {
            "source_boundary": seed.get("source_boundary", {}),
            "claim_card": seed.get("claim_card", {}),
            "workload_profile": seed.get("workload_profile", {}),
            "tau_vector": seed.get("tau_vector", {}),
            "logicfolding_margin": lf_margin,
            "gamma_tau_ETP": gamma,
            "edge_surface": beta,
            "pvt_closure": seed.get("pvt_closure", {}),
            "yield_method_disclosure": seed.get("yield_method_disclosure", {}),
            "evidence_disclosure": seed.get("evidence_disclosure", {}),
            "overclaim": seed.get("overclaim", 0.0),
            "monte_carlo_stress": stress,
        }

        classification = classify_tsek(gate_record)

        evidence = {
            "schema": "TAU-SCALING-SA-v0.1-evidence-package",
            "run_id": run_id,
            "source_boundary": seed.get("source_boundary", {}),
            "claim_card": seed.get("claim_card", {}),
            "workload_profile": seed.get("workload_profile", {}),
            "tau_vector": seed.get("tau_vector", {}),
            "baseline_manifest": seed.get("baseline_manifest", {}),
            "candidate_manifest": seed.get("candidate_manifest", {}),
            "logicfolding_survivability": {
                **logicfolding,
                "logicfolding_margin": lf_margin,
                "passed": lf_margin > 0,
            },
            "edge_surface_boundary": beta,
            "energy_thermal_pdn_pvt": {
                **normalization,
                "gamma_tau_ETP": gamma,
                "passed": gamma > 1,
            },
            "pvt_closure": seed.get("pvt_closure", {}),
            "yield_method_disclosure": seed.get("yield_method_disclosure", {}),
            "monte_carlo_stress": stress,
            "admissible_claim": classification["admissible_claim"],
            "classification": classification,
            "non_claim_locks": seed.get("non_claim_locks", {}),
        }

        evidence_path = emit_evidence_package(run_dir, evidence)

        latest = self.repo_root / "artifacts" / "runs" / "latest"
        if latest.exists() and latest.is_dir():
            import shutil
            shutil.rmtree(latest)
        latest.mkdir(parents=True, exist_ok=True)

        import shutil
        for item in run_dir.iterdir():
            dest = latest / item.name
            if item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest)

        return TauScalingRunResult(
            run_id=run_id,
            run_dir=str(run_dir),
            evidence_path=str(evidence_path),
            classification=classification["class"],
            admissible_score=classification["admissible_claim"]["A_TSEK"],
            findings_count=len(classification["findings"]),
        )
