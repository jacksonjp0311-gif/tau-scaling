from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from secrets import token_hex
from typing import Iterable


def utc_run_stamp() -> str:
    """Return a UTC timestamp with microsecond precision."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def generate_run_id(prefix: str = "") -> str:
    """Generate a collision-resistant, filesystem-safe run identifier.

    Format:
        YYYYMMDDTHHMMSSffffffZ-abcdef
        or <prefix>-YYYYMMDDTHHMMSSffffffZ-abcdef

    This fixes second-level run_id collisions when two Tau Scaling runs are
    launched in the same second.
    """
    suffix = token_hex(3)
    stamp = utc_run_stamp()
    if prefix:
        safe = "".join(ch if ch.isalnum() or ch in ("-", "_") else "-" for ch in prefix).strip("-_")
        if safe:
            return f"{safe}-{stamp}-{suffix}"
    return f"{stamp}-{suffix}"


def claim_seed_slug(seed_path: str | Path | None) -> str:
    """Create a short safe slug from a seed path for benchmark-readable IDs."""
    if not seed_path:
        return "claim"
    stem = Path(seed_path).stem
    slug = "".join(ch if ch.isalnum() or ch in ("-", "_") else "-" for ch in stem).strip("-_").lower()
    return slug or "claim"


def ensure_unique_run_dir(base_dir: Path, run_id: str) -> tuple[str, Path]:
    """Return a run id and directory path that do not already exist.

    The tokenized microsecond ID should already avoid collisions. This final
    filesystem guard makes the contract explicit and testable.
    """
    candidate = base_dir / run_id
    if not candidate.exists():
        return run_id, candidate

    for _ in range(100):
        new_id = generate_run_id("rerun")
        candidate = base_dir / new_id
        if not candidate.exists():
            return new_id, candidate

    raise RuntimeError("Could not allocate a unique Tau Scaling run directory after 100 attempts.")