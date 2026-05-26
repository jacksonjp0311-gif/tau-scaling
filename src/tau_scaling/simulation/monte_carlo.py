from __future__ import annotations

import random
from statistics import mean
from typing import Any


def _uniform_pair(bounds: list[float] | tuple[float, float], default=(0.0, 1.0)) -> tuple[float, float]:
    try:
        lo, hi = float(bounds[0]), float(bounds[1])
        return lo, hi
    except Exception:
        return default


def run_monte_carlo(config: dict[str, Any]) -> dict[str, Any]:
    n = int(config.get("runs", 1000))
    if n < 1:
        n = 1
    seed = int(config.get("seed", 777))
    random.seed(seed)

    rho_b = _uniform_pair(config.get("rho_critical_paths", [0.40, 0.80]))
    wire_b = _uniform_pair(config.get("wire_savings_ps", [20.0, 45.0]))
    vertical_b = _uniform_pair(config.get("vertical_penalty_ps", [5.0, 15.0]))
    route_b = _uniform_pair(config.get("routing_penalty_ps", [2.0, 10.0]))
    sync_b = _uniform_pair(config.get("sync_penalty_ps", [1.0, 5.0]))
    variation_b = _uniform_pair(config.get("variation_penalty_ps", [1.0, 5.0]))
    closure_b = _uniform_pair(config.get("closure_penalty_ps", [2.0, 10.0]))

    tau_gain_b = _uniform_pair(config.get("tau_gain", [1.0, 1.5]))
    energy_b = _uniform_pair(config.get("energy_ratio", [0.9, 1.2]))
    thermal_b = _uniform_pair(config.get("thermal_ratio", [0.9, 1.2]))
    pdn_b = _uniform_pair(config.get("pdn_ratio", [0.9, 1.2]))
    closure_probability = float(config.get("post_route_closure_probability", 0.75))

    margins = []
    gammas = []
    b_candidates = 0
    margin_pass = 0
    gamma_pass = 0
    closure_pass_count = 0

    for _ in range(n):
        rho = random.uniform(*rho_b)
        wire = random.uniform(*wire_b)
        penalties = (
            random.uniform(*vertical_b)
            + random.uniform(*route_b)
            + random.uniform(*sync_b)
            + random.uniform(*variation_b)
            + random.uniform(*closure_b)
        )
        margin = (rho * wire) - penalties
        tau_gain = random.uniform(*tau_gain_b)
        energy = random.uniform(*energy_b)
        thermal = random.uniform(*thermal_b)
        pdn = random.uniform(*pdn_b)
        gamma = tau_gain / (energy * thermal * pdn) if energy > 0 and thermal > 0 and pdn > 0 else 0.0
        closure_pass = random.random() <= closure_probability

        margins.append(margin)
        gammas.append(gamma)

        if margin > 0:
            margin_pass += 1
        if gamma > 1:
            gamma_pass += 1
        if closure_pass:
            closure_pass_count += 1
        if margin > 0 and gamma > 1 and closure_pass:
            b_candidates += 1

    return {
        "schema": "TAU-SCALING-SA-v0.1-monte-carlo-summary",
        "simulation_not_validation": True,
        "runs": n,
        "seed": seed,
        "mean_margin_ps": round(mean(margins), 6),
        "mean_gamma_tau_ETP": round(mean(gammas), 6),
        "p_margin_pass": round(margin_pass / n, 6),
        "p_gamma_pass": round(gamma_pass / n, 6),
        "p_post_route_closure_pass": round(closure_pass_count / n, 6),
        "p_tsek_b_candidate": round(b_candidates / n, 6),
    }
