from __future__ import annotations

from typing import Any


def _f(x: Any, default: float = 0.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def logicfolding_margin(record: dict[str, Any]) -> float:
    rho = max(0.0, min(1.0, _f(record.get("rho_critical_paths"))))
    wire = _f(record.get("expected_wire_savings_ps"))
    penalties = sum(_f(record.get(k)) for k in [
        "expected_vertical_penalty_ps",
        "routing_penalty_ps",
        "sync_penalty_ps",
        "variation_penalty_ps",
        "closure_penalty_ps",
    ])
    return round((rho * wire) - penalties, 6)
