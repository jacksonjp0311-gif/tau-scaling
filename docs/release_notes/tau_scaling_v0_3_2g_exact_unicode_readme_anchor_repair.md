# TAU-SCALING-SA v0.3.2g — Exact Unicode README Anchor Repair

Generated: 2026-05-26T10:12:59Z

## Purpose

This patch repairs the final README mini repo audit failure by writing the exact required heading:

```text
AI Rule — Directory Box and Mini README Synchronization
```

The failure was not runtime, RCC-N, architecture, test, benchmark, or claim logic. It was exact Unicode anchor visibility.

## Lesson Encoded

When audit scripts check literal Unicode anchors, the patch layer must write the exact Unicode character rather than relying on PowerShell console paste or visually similar dash characters.

## Non-Claim Lock

This is context-surface repair only. It is not runtime correctness proof, silicon validation, product validation, manufacturing validation, process-node equivalence, or universal Tau Scaling proof.
