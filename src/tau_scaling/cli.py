from __future__ import annotations

import argparse
from pathlib import Path

from tau_scaling.core.runtime import TauScalingRuntime
from tau_scaling.claims.classifier import classify_tsek
from tau_scaling.gates.logicfolding_survivability import logicfolding_margin
from tau_scaling.gates.gamma_tau_etp import gamma_tau_etp
from tau_scaling.gates.edge_surface import edge_surface_ratio
from tau_scaling.simulation.monte_carlo import run_monte_carlo
from tau_scaling.utils.safe_json import read_json


def cmd_init(args: argparse.Namespace) -> None:
    Path("artifacts/runs").mkdir(parents=True, exist_ok=True)
    print("Tau Scaling runtime initialized.")


def cmd_run_claim(args: argparse.Namespace) -> None:
    seed = read_json(args.seed)
    result = TauScalingRuntime(".").run(seed)
    print("TAU-SCALING-SA run complete")
    print(f"run_id: {result.run_id}")
    print(f"class: {result.classification}")
    print(f"A_TSEK: {result.admissible_score:.4f}")
    print(f"findings: {result.findings_count}")
    print(f"artifacts: {result.run_dir}")
    print(f"evidence: {result.evidence_path}")


def cmd_classify(args: argparse.Namespace) -> None:
    evidence = read_json(args.evidence)
    record = {
        "source_boundary": evidence.get("source_boundary", {}),
        "claim_card": evidence.get("claim_card", {}),
        "workload_profile": evidence.get("workload_profile", {}),
        "tau_vector": evidence.get("tau_vector", {}),
        "logicfolding_margin": evidence.get("logicfolding_survivability", {}).get("logicfolding_margin", 0.0),
        "gamma_tau_ETP": evidence.get("energy_thermal_pdn_pvt", {}).get("gamma_tau_ETP", 0.0),
        "pvt_closure": evidence.get("pvt_closure", {}),
        "yield_method_disclosure": evidence.get("yield_method_disclosure", {}),
        "evidence_disclosure": {"evidence_package_complete": True},
        "overclaim": 0.0,
    }
    print(classify_tsek(record))


def cmd_check_logicfolding(args: argparse.Namespace) -> None:
    print({"logicfolding_margin": logicfolding_margin(read_json(args.record))})


def cmd_gamma_etp(args: argparse.Namespace) -> None:
    print({"gamma_tau_ETP": gamma_tau_etp(read_json(args.record))})


def cmd_edge_surface(args: argparse.Namespace) -> None:
    print(edge_surface_ratio(read_json(args.record)))


def cmd_monte_carlo(args: argparse.Namespace) -> None:
    seed = read_json(args.seed)
    config = seed.get("monte_carlo_stress", seed)
    print(run_monte_carlo(config))


def main() -> None:
    parser = argparse.ArgumentParser(prog="tau_scaling")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("run-claim")
    p.add_argument("--seed", required=True)
    p.set_defaults(func=cmd_run_claim)

    p = sub.add_parser("classify")
    p.add_argument("--evidence", required=True)
    p.set_defaults(func=cmd_classify)

    p = sub.add_parser("check-logicfolding")
    p.add_argument("--record", required=True)
    p.set_defaults(func=cmd_check_logicfolding)

    p = sub.add_parser("gamma-etp")
    p.add_argument("--record", required=True)
    p.set_defaults(func=cmd_gamma_etp)

    p = sub.add_parser("edge-surface")
    p.add_argument("--record", required=True)
    p.set_defaults(func=cmd_edge_surface)

    p = sub.add_parser("monte-carlo")
    p.add_argument("--seed", required=True)
    p.set_defaults(func=cmd_monte_carlo)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
