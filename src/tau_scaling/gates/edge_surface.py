from __future__ import annotations

from typing import Any


def _f(x: Any, default: float = 1.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def edge_surface_ratio(record: dict[str, Any]) -> dict[str, float | str | bool]:
    n = max(1.0, _f(record.get("N"), 10.0))
    compute_coeff = _f(record.get("compute_coeff"), 1.0)
    edge_coeff = _f(record.get("edge_coeff"), 1.0)
    surface_coeff = _f(record.get("surface_coeff"), 1.0)

    compute = compute_coeff * (n ** 2)
    edge_resource = edge_coeff * n
    surface_resource = surface_coeff * (n ** 2)

    beta_edge = edge_resource / compute if compute else 0.0
    beta_surface = surface_resource / compute if compute else 0.0

    return {
        "N": n,
        "beta_edge": round(beta_edge, 6),
        "beta_surface": round(beta_surface, 6),
        "edge_starvation_detected": beta_edge < beta_surface,
        "model": "beta_edge ~ N^-1; beta_surface ~ O(1)"
    }
