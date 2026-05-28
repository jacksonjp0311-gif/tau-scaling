# Evidence Sufficiency Matrix v0.8.4

## Purpose

Define the evidence required to preserve, promote, downgrade, or reject each public Tau claim.

## Summary

- Claim count: `8`
- Average evidence sufficiency score: `0.375`
- Average missing gates: `5`
- Classifier changed: `false`
- Thresholds changed: `false`
- Mutation allowed: `false`

## Claim Matrix

| Claim | Current class | Family | Score | Missing gates | Recommended action |
|---|---|---|---:|---:|---|
| `tau-public-001-methodology` | TSEK-C | methodology | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-002-logicfolding` | TSEK-C | mechanism | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-003-density-equivalent` | TSEK-C | mechanism | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-004-roadmap-1p4nm-class` | TSEK-C | metric | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-005-unified-bus` | TSEK-C | architecture | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-006-hione-optical-io` | TSEK-C | io | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-007-3d-folding` | TSEK-C | topology | 0.375 | 5 | remain_current_class_pending_evidence |
| `tau-public-008-ai-gap-closure` | TSEK-C | roadmap | 0.375 | 5 | remain_current_class_pending_evidence |

## Promotion Rules

A claim may be considered for TSEK-B review only when workload, baseline, method, and companion gate evidence are disclosed.

A claim may be considered for TSEK-A review only when independent reproduction, measurement protocol, uncertainty bounds, and negative controls are available.

## Downgrade Rules

- Roadmap language treated as achieved result forces downgrade pressure.
- Density equivalence treated as node equivalence forces downgrade pressure.
- Timing gain without energy/thermal/PDN/yield companion evidence remains bounded.
- LogicFolding fails if wire savings are erased by vertical, routing, sync, variation, closure, thermal, or yield burden.

## Visual

![Evidence sufficiency matrix](../../visuals/evidence_sufficiency/v0_8_4/evidence_sufficiency_matrix.svg)

## Boundary

Evidence sufficiency matrices are promotion-condition artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
