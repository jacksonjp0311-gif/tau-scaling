
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXECUTOR = ROOT / "reports" / "replay_executor" / "latest_approval_gated_replay_executor.json"
HANDOFF = ROOT / "reports" / "live_approval_handoff" / "latest_live_approval_handoff_check.json"
OUT = ROOT / "reports" / "blocked_continuity"
VIS = ROOT / "visuals" / "blocked_continuity" / "v0_6_8"
LEDGER = OUT / "blocked_state_continuity_ledger.jsonl"

def rjson(p):
    return json.loads(p.read_text(encoding="utf-8"))

def wjson(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def wtext(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def append_jsonl(p, x):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(x, sort_keys=True) + "\n")

def rel(p):
    return str(p.relative_to(ROOT)).replace("\\", "/")

def read_ledger(p):
    if not p.exists():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows

def charts(summary):
    paths = []
    try:
        import matplotlib.pyplot as plt
    except Exception as e:
        wtext(OUT / "chart_generation_skipped.txt", str(e))
        return paths
    VIS.mkdir(parents=True, exist_ok=True)

    def save(name):
        p = VIS / name
        plt.tight_layout()
        plt.savefig(p, dpi=180, bbox_inches="tight")
        plt.close()
        paths.append(rel(p))

    gates = {
        "executor_blocked": int(summary["executor_blocked"]),
        "handoff_blocked": int(summary["handoff_blocked"]),
        "live_approval_present": int(summary["live_approval_present"]),
        "mutation_allowed": int(summary["mutation_allowed"]),
        "application_allowed": int(summary["application_allowed"]),
    }
    plt.figure(figsize=(9, 4))
    plt.bar(list(gates.keys()), list(gates.values()))
    plt.xticks(rotation=25, ha="right")
    plt.ylabel("Boolean state")
    plt.title("Blocked-State Continuity Snapshot")
    save("blocked_continuity_snapshot.png")

    ledger_counts = summary["ledger_status_counts"]
    plt.figure(figsize=(8, 4))
    plt.bar(list(ledger_counts.keys()), list(ledger_counts.values()))
    plt.xticks(rotation=20, ha="right")
    plt.ylabel("Ledger entries")
    plt.title("Blocked-State Continuity Ledger")
    save("blocked_continuity_ledger_counts.png")

    timeline = summary["ledger_tail"]
    labels = [f"entry_{i+1}" for i, _ in enumerate(timeline)]
    vals = [1 for _ in timeline]
    plt.figure(figsize=(9, 4))
    plt.bar(labels, vals)
    plt.ylabel("Recorded")
    plt.title("Blocked-State Ledger Tail")
    save("blocked_continuity_tail.png")
    return paths

def report(s):
    lines = [
        "# Tau Scaling v0.6.8 Blocked-State Continuity Ledger",
        "",
        f"Generated: `{s['generated_at']}`",
        "",
        "## Continuity Result",
        "",
        f"- Continuity status: `{s['continuity_status']}`",
        f"- Executor status: `{s['executor_status']}`",
        f"- Handoff status: `{s['handoff_status']}`",
        f"- Ledger path: `{s['ledger_path']}`",
        f"- Ledger entries: `{s['ledger_entry_count']}`",
        f"- Executor blocked: `{s['executor_blocked']}`",
        f"- Handoff blocked: `{s['handoff_blocked']}`",
        f"- Mutation allowed: `{s['mutation_allowed']}`",
        f"- Application allowed: `{s['application_allowed']}`",
        "",
        "## Current Block Reason",
        "",
        s["block_reason"],
        "",
        "## Ledger Tail",
        "",
        "| Index | Version | Executor status | Handoff status | Replay allowed |",
        "|---:|---|---|---|---|",
    ]
    for i, row in enumerate(s["ledger_tail"], 1):
        lines.append(
            f"| {i} | `{row.get('version')}` | `{row.get('executor_status')}` | `{row.get('handoff_status')}` | `{row.get('replay_allowed')}` |"
        )
    lines += ["", "## Charts", ""]
    for p in s["chart_paths"]:
        lines.append(f"![{Path(p).stem}]({os.path.relpath(ROOT / p, OUT).replace('\\', '/')})")
        lines.append("")
    lines += ["## Boundary", "", s["boundary"], ""]
    return "\n".join(lines)

def main():
    executor = rjson(EXECUTOR)
    handoff = rjson(HANDOFF)

    executor_blocked = executor.get("executor_status") == "EXECUTOR_BLOCKED__LIVE_APPROVAL_HANDOFF_NOT_VALID"
    handoff_blocked = str(handoff.get("handoff_status", "")).startswith("HANDOFF_BLOCKED")
    replay_allowed = bool(executor.get("executor_allowed") and handoff.get("replay_allowed"))

    entry = {
        "schema": "tau-scaling-blocked-state-continuity-ledger-entry-v0.6.8",
        "version": "v0.6.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "executor_status": executor.get("executor_status"),
        "handoff_status": handoff.get("handoff_status"),
        "executor_blocked": bool(executor_blocked),
        "handoff_blocked": bool(handoff_blocked),
        "live_approval_present": bool(handoff.get("live_approval_present")),
        "live_approval_valid": bool(handoff.get("live_approval_valid")),
        "replay_allowed": bool(replay_allowed),
        "executor_ran": bool(executor.get("executor_ran")),
        "branch_created": False,
        "mutation_allowed": False,
        "application_allowed": False,
        "calibration_applied": False,
        "block_reason": executor.get("block_reason", "Live approval handoff is not valid for replay."),
    }
    append_jsonl(LEDGER, entry)
    rows = read_ledger(LEDGER)

    status_counts = {}
    for row in rows:
        key = row.get("executor_status", "UNKNOWN")
        status_counts[key] = status_counts.get(key, 0) + 1

    summary = {
        "schema": "tau-scaling-blocked-state-continuity-ledger-v0.6.8",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_replay_executor": rel(EXECUTOR),
        "input_live_approval_handoff": rel(HANDOFF),
        "continuity_status": "BLOCKED_STATE_RECORDED__NO_EXECUTION",
        "ledger_path": rel(LEDGER),
        "ledger_entry_count": len(rows),
        "ledger_status_counts": status_counts,
        "ledger_tail": rows[-5:],
        "executor_status": executor.get("executor_status"),
        "handoff_status": handoff.get("handoff_status"),
        "executor_blocked": bool(executor_blocked),
        "handoff_blocked": bool(handoff_blocked),
        "live_approval_present": bool(handoff.get("live_approval_present")),
        "live_approval_valid": bool(handoff.get("live_approval_valid")),
        "replay_allowed": bool(replay_allowed),
        "executor_ran": False,
        "branch_created": False,
        "branch_creation_allowed": False,
        "application_allowed": False,
        "mutation_allowed": False,
        "policy_enforced": False,
        "calibration_applied": False,
        "runtime_behavior_changed": False,
        "block_reason": entry["block_reason"],
        "final_recommendation": "Preserve blocked state as evidence. Do not replay, create branches, or mutate behavior without a valid live approval handoff.",
        "boundary": "Blocked-state continuity ledgers are local classifier-governance memory artifacts. They preserve why execution was blocked. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.",
        "next_recommendation": "v0.6.9 should add blocked-state trend review and retirement criteria before continuing toward any live approval pathway.",
    }
    summary["chart_paths"] = charts(summary)

    wjson(OUT / "blocked_state_continuity_v0_6_8.json", summary)
    wjson(OUT / "latest_blocked_state_continuity.json", summary)
    wtext(OUT / "blocked_state_continuity_v0_6_8.md", report(summary))
    wtext(OUT / "latest_blocked_state_continuity.md", report(summary))

    print(json.dumps({
        "schema": summary["schema"],
        "continuity_status": summary["continuity_status"],
        "ledger_entry_count": summary["ledger_entry_count"],
        "executor_status": summary["executor_status"],
        "handoff_status": summary["handoff_status"],
        "executor_blocked": summary["executor_blocked"],
        "handoff_blocked": summary["handoff_blocked"],
        "replay_allowed": summary["replay_allowed"],
        "executor_ran": summary["executor_ran"],
        "mutation_allowed": summary["mutation_allowed"],
        "application_allowed": summary["application_allowed"],
        "calibration_applied": summary["calibration_applied"],
        "chart_count": len(summary["chart_paths"]),
        "report": "reports/blocked_continuity/latest_blocked_state_continuity.md",
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
