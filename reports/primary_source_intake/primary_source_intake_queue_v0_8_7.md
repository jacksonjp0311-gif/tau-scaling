# Primary Source Intake Queue v0.8.7

## Purpose

Create a governed manual queue for filling source-intake cards with primary-source details.

## Summary

- Claim count: `8`
- Source-populated count: `0`
- Ready for claim review: `0`
- Average filled fields: `2`
- Average source confidence: `0.0`
- Manifest: `sources\primary_source_intake\source_seed_manifest_v0_8_7.json`

## Queue Table

| Claim | Source category | Filled fields | Missing fields | Primary confirmed | Source populated |
|---|---|---:|---|---:|---:|
| `tau-public-001-methodology` | methodology_claim | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-002-logicfolding` | architecture_interpretation | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-003-density-equivalent` | reported_metric | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-004-roadmap-1p4nm-class` | roadmap_projection | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-005-unified-bus` | architecture_interpretation | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-006-hione-optical-io` | reported_metric | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-007-3d-folding` | architecture_interpretation | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |
| `tau-public-008-ai-gap-closure` | media_interpretation | 2 | source_url, source_title, source_date, source_author_or_org, claim_excerpt_or_paraphrase | False | False |

## Required Manual Population Fields

- `source_url`
- `source_title`
- `source_type`
- `source_date`
- `source_author_or_org`
- `claim_excerpt_or_paraphrase`
- `paraphrase_boundary`

## Visual

![Primary source intake queue](../../visuals/primary_source_intake/v0_8_7/primary_source_intake_queue.svg)

## Boundary

Primary source intake queue prepares manual source population only. It does not invent sources, validate sources, promote claims, validate silicon, validate products, or establish a universal Tau Scaling law.
