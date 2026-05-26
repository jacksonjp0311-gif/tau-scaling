from __future__ import annotations

import json
import statistics
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tau_scaling.core.runtime import TauScalingRuntime


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SEEDS = [
    REPO_ROOT / "configs" / "seeds" / "logicfolding_claim_card.json",
    REPO_ROOT / "configs" / "seeds" / "logicfolding_promotion_path_claim_card.json",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_benchmarks(iterations: int = 6) -> dict[str, Any]:
    runtime = TauScalingRuntime(REPO_ROOT)
    generated_at = datetime.now(timezone.utc).isoformat()
    results: list[dict[str, Any]] = []

    for seed_path in DEFAULT_SEEDS:
        if not seed_path.exists():
            raise FileNotFoundError(f"Missing benchmark seed: {seed_path}")

        seed = load_json(seed_path)
        for i in range(iterations):
            t0 = time.perf_counter()
            result = runtime.run(seed)
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            results.append(
                {
                    "seed": str(seed_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                    "iteration": i + 1,
                    "run_id": result.run_id,
                    "classification": result.classification,
                    "A_TSEK": result.admissible_score,
                    "findings_count": result.findings_count,
                    "elapsed_ms": round(elapsed_ms, 4),
                    "evidence_path": str(Path(result.evidence_path).relative_to(REPO_ROOT)).replace("\\", "/"),
                }
            )

    run_ids = [row["run_id"] for row in results]
    duplicate_run_ids = sorted([rid for rid, count in Counter(run_ids).items() if count > 1])
    elapsed = [row["elapsed_ms"] for row in results]

    by_seed: dict[str, Any] = {}
    for seed in sorted({row["seed"] for row in results}):
        rows = [row for row in results if row["seed"] == seed]
        by_seed[seed] = {
            "runs": len(rows),
            "classes": dict(Counter(row["classification"] for row in rows)),
            "A_TSEK_values": sorted({row["A_TSEK"] for row in rows}),
            "findings_values": sorted({row["findings_count"] for row in rows}),
            "mean_elapsed_ms": round(statistics.mean(row["elapsed_ms"] for row in rows), 4),
            "min_elapsed_ms": round(min(row["elapsed_ms"] for row in rows), 4),
            "max_elapsed_ms": round(max(row["elapsed_ms"] for row in rows), 4),
        }

    summary = {
        "schema": "tau-scaling-benchmark-summary-v0.3.2",
        "generated_at": generated_at,
        "iterations_per_seed": iterations,
        "total_runs": len(results),
        "unique_run_ids": len(set(run_ids)),
        "duplicate_run_ids": duplicate_run_ids,
        "collision_proof_run_identity_passed": len(duplicate_run_ids) == 0,
        "mean_elapsed_ms": round(statistics.mean(elapsed), 4),
        "median_elapsed_ms": round(statistics.median(elapsed), 4),
        "min_elapsed_ms": round(min(elapsed), 4),
        "max_elapsed_ms": round(max(elapsed), 4),
        "class_counts": dict(Counter(row["classification"] for row in results)),
        "by_seed": by_seed,
        "results": results,
        "boundary": "Benchmark timing and class stability are local-runtime diagnostics only. They are not silicon validation, product validation, or universal Tau Scaling proof.",
    }

    return summary


def render_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Tau Scaling v0.3.2 Benchmark Summary",
        "",
        f"Generated: `{summary['generated_at']}`",
        "",
        "## Result",
        "",
        f"- Total runs: `{summary['total_runs']}`",
        f"- Unique run IDs: `{summary['unique_run_ids']}`",
        f"- Duplicate run IDs: `{len(summary['duplicate_run_ids'])}`",
        f"- Collision-proof identity passed: `{summary['collision_proof_run_identity_passed']}`",
        f"- Mean elapsed ms: `{summary['mean_elapsed_ms']}`",
        f"- Median elapsed ms: `{summary['median_elapsed_ms']}`",
        f"- Min elapsed ms: `{summary['min_elapsed_ms']}`",
        f"- Max elapsed ms: `{summary['max_elapsed_ms']}`",
        "",
        "## Class Counts",
        "",
        "| Class | Count |",
        "|---|---:|",
    ]
    for cls, count in sorted(summary["class_counts"].items()):
        lines.append(f"| {cls} | {count} |")

    lines += [
        "",
        "## Seed Breakdown",
        "",
        "| Seed | Runs | Classes | A_TSEK values | Findings values | Mean ms |",
        "|---|---:|---|---|---|---:|",
    ]
    for seed, data in summary["by_seed"].items():
        classes = ", ".join(f"{k}:{v}" for k, v in sorted(data["classes"].items()))
        lines.append(
            f"| `{seed}` | {data['runs']} | {classes} | {data['A_TSEK_values']} | {data['findings_values']} | {data['mean_elapsed_ms']} |"
        )

    lines += [
        "",
        "## Boundary",
        "",
        summary["boundary"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    summary = run_benchmarks()
    json_path = REPO_ROOT / "reports" / "benchmarks" / "tau_scaling_v0_3_2_benchmark_summary.json"
    md_path = REPO_ROOT / "reports" / "benchmarks" / "tau_scaling_v0_3_2_benchmark_summary.md"
    latest_json = REPO_ROOT / "reports" / "benchmarks" / "latest_benchmark_summary.json"
    latest_md = REPO_ROOT / "reports" / "benchmarks" / "latest_benchmark_summary.md"

    write_json(json_path, summary)
    write_json(latest_json, summary)
    md = render_markdown(summary)
    write_text(md_path, md)
    write_text(latest_md, md)

    print(json.dumps({k: summary[k] for k in [
        "schema",
        "total_runs",
        "unique_run_ids",
        "duplicate_run_ids",
        "collision_proof_run_identity_passed",
        "mean_elapsed_ms",
        "class_counts",
    ]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()