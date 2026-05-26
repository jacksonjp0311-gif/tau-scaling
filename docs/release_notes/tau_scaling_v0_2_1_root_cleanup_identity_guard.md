# Tau Scaling v0.2.1 - Root Cleanup and Identity Guard

## Summary

This patch cleans loose root status files, repairs root package identity, checks root README identity, preserves RCC-N / OMN-style repository geometry, and reruns validation.

## Actions

- Root status files moved to reports/status/legacy_root_status/.
- pyproject.toml repaired to tau-scaling v0.2.0 package identity.
- README identity checked and repaired if OMN drift was detected.
- README_90_SECONDS identity checked and repaired if OMN drift was detected.

## Boundary

This patch is repository hygiene and identity alignment only. It does not loosen TSEK gates, upgrade claim class, validate silicon, validate product metrics, prove node equivalence, or change runtime claim strength.