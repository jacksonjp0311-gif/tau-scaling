
from __future__ import annotations

import base64
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
GENERATED_AT = datetime.now(timezone.utc).isoformat()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def backup(path: Path, label: str) -> None:
    if path.exists():
        dest = ROOT / "reports" / "nexus_target_refresh" / "v0_5_1" / "backups" / f"{path.name}_before_v0_5_1_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KTkVYVVNfUEFUSCA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJuZXh1c19mZWVkYmFjayIgLyAibGF0ZXN0X25leHVzX2ZlZWRiYWNrLmpzb24iClJFQURJTkVTU19QQVRIID0gUkVQT19ST09UIC8gInJlcG9ydHMiIC8gImVuZm9yY2VtZW50X3JlYWRpbmVzcyIgLyAibGF0ZXN0X2VuZm9yY2VtZW50X3JlYWRpbmVzc19nYXRlLmpzb24iCk9VVF9ESVIgPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAibmV4dXNfdGFyZ2V0X3JlZnJlc2giClZJU19ESVIgPSBSRVBPX1JPT1QgLyAidmlzdWFscyIgLyAibmV4dXNfdGFyZ2V0X3JlZnJlc2giIC8gInYwXzVfMSIKCkNPTVBMRVRJT05fRVZJREVOQ0UgPSB7CiAgICAiVEFVLVNDQUxJTkctU0EgdjAuNC42IC0gUGFpciBQb2xpY3kgRHJ5LVJ1biBTaW11bGF0b3IiOiBbCiAgICAgICAgInJlcG9ydHMvcG9saWN5X2RyeV9ydW4vbGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4uanNvbiIsCiAgICAgICAgInJlcG9ydHMvcG9saWN5X2RyeV9ydW4vbGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4ubWQiLAogICAgXSwKICAgICJUQVUtU0NBTElORy1TQSB2MC40LjcgLSBQb2xpY3kgSW1wYWN0IEV4cGxhbmF0aW9uIENhcmRzIjogWwogICAgICAgICJyZXBvcnRzL3BvbGljeV9pbXBhY3QvbGF0ZXN0X3BvbGljeV9pbXBhY3RfY2FyZHMuanNvbiIsCiAgICAgICAgInJlcG9ydHMvcG9saWN5X2ltcGFjdC9sYXRlc3RfcG9saWN5X2ltcGFjdF9jYXJkcy5tZCIsCiAgICBdLAogICAgIlRBVS1TQ0FMSU5HLVNBIHYwLjQuOCAtIFBvbGljeSBEZWNpc2lvbiBSZWNvcmQiOiBbCiAgICAgICAgInJlcG9ydHMvcG9saWN5X2RlY2lzaW9uL2xhdGVzdF9wb2xpY3lfZGVjaXNpb25fcmVjb3JkLmpzb24iLAogICAgICAgICJyZXBvcnRzL3BvbGljeV9kZWNpc2lvbi9sYXRlc3RfcG9saWN5X2RlY2lzaW9uX3JlY29yZC5tZCIsCiAgICBdLAogICAgIlRBVS1TQ0FMSU5HLVNBIHYwLjQuOSAtIFJlZ3Jlc3Npb24gYW5kIE92ZXItUGVuYWx0eSBSZXZpZXciOiBbCiAgICAgICAgInJlcG9ydHMvcmVncmVzc2lvbl9yZXZpZXcvbGF0ZXN0X3JlZ3Jlc3Npb25fb3Zlcl9wZW5hbHR5X3Jldmlldy5qc29uIiwKICAgICAgICAicmVwb3J0cy9yZWdyZXNzaW9uX3Jldmlldy9sYXRlc3RfcmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3Lm1kIiwKICAgIF0sCiAgICAiVEFVLVNDQUxJTkctU0EgdjAuNS4wIC0gRW5mb3JjZW1lbnQgUmVhZGluZXNzIEdhdGUiOiBbCiAgICAgICAgInJlcG9ydHMvZW5mb3JjZW1lbnRfcmVhZGluZXNzL2xhdGVzdF9lbmZvcmNlbWVudF9yZWFkaW5lc3NfZ2F0ZS5qc29uIiwKICAgICAgICAicmVwb3J0cy9lbmZvcmNlbWVudF9yZWFkaW5lc3MvbGF0ZXN0X2VuZm9yY2VtZW50X3JlYWRpbmVzc19nYXRlLm1kIiwKICAgIF0sCn0KCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCkgLT4gZGljdFtzdHIsIEFueV06CiAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3cml0ZV9qc29uKHBhdGg6IFBhdGgsIHBheWxvYWQ6IEFueSkgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKHBheWxvYWQsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHdyaXRlX3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKSAtPiBOb25lOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KHRleHQsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgZXZpZGVuY2VfY29tcGxldGUocGF0aHM6IGxpc3Rbc3RyXSkgLT4gYm9vbDoKICAgIHJldHVybiBhbGwoKFJFUE9fUk9PVCAvIHApLmV4aXN0cygpIGZvciBwIGluIHBhdGhzKQoKZGVmIGNsYXNzaWZ5X3ByaW9yaXR5KHByaW9yaXR5OiBkaWN0W3N0ciwgQW55XSkgLT4gZGljdFtzdHIsIEFueV06CiAgICB0YXJnZXQgPSBwcmlvcml0eS5nZXQoInRhcmdldF9uZXh0IiwgIiIpCiAgICBldmlkZW5jZSA9IENPTVBMRVRJT05fRVZJREVOQ0UuZ2V0KHRhcmdldCkKICAgIGlmIGV2aWRlbmNlIGFuZCBldmlkZW5jZV9jb21wbGV0ZShldmlkZW5jZSk6CiAgICAgICAgc3RhdHVzID0gIkNPTVBMRVRFRF9SRVRJUkVEIgogICAgICAgIHJlYXNvbiA9ICJUYXJnZXQgZXZpZGVuY2UgZXhpc3RzOyByZWNvbW1lbmRhdGlvbiBzaG91bGQgYmUgcmV0aXJlZCBmcm9tIGFjdGl2ZSBOZXh1cyBxdWV1ZS4iCiAgICBlbHNlOgogICAgICAgIHN0YXR1cyA9ICJBQ1RJVkUiCiAgICAgICAgcmVhc29uID0gIk5vIGNvbXBsZXRpb24gZXZpZGVuY2UgZm91bmQgZm9yIHRhcmdldC4iCgogICAgcmV0dXJuIHsKICAgICAgICAiaWQiOiBwcmlvcml0eS5nZXQoImlkIiksCiAgICAgICAgInJhbmsiOiBwcmlvcml0eS5nZXQoInJhbmsiKSwKICAgICAgICAic3VyZmFjZSI6IHByaW9yaXR5LmdldCgic3VyZmFjZSIpLAogICAgICAgICJzaWduYWwiOiBwcmlvcml0eS5nZXQoInNpZ25hbCIpLAogICAgICAgICJzZXZlcml0eSI6IHByaW9yaXR5LmdldCgic2V2ZXJpdHkiKSwKICAgICAgICAicmVjb21tZW5kYXRpb24iOiBwcmlvcml0eS5nZXQoInJlY29tbWVuZGF0aW9uIiksCiAgICAgICAgInRhcmdldF9uZXh0IjogdGFyZ2V0LAogICAgICAgICJjb21wbGV0aW9uX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAiY29tcGxldGlvbl9yZWFzb24iOiByZWFzb24sCiAgICB9CgpkZWYgYnVpbGRfYWN0aXZlX2Jsb2NrZXIocmVhZGluZXNzOiBkaWN0W3N0ciwgQW55XSkgLT4gZGljdFtzdHIsIEFueV06CiAgICBibG9ja2VkID0gaW50KHJlYWRpbmVzcy5nZXQoImJsb2NrZWRfYnlfb3Zlcl9wZW5hbHR5X2NvdW50IiwgMCkgb3IgMCkKICAgIGVsaWdpYmxlID0gaW50KHJlYWRpbmVzcy5nZXQoImVsaWdpYmxlX2NhbmRpZGF0ZV9kZXNpZ25fY291bnQiLCAwKSBvciAwKQogICAgZW5mb3JjZW1lbnQgPSBib29sKHJlYWRpbmVzcy5nZXQoImVuZm9yY2VtZW50X2NhbmRpZGF0ZV9lbmFibGVkIiwgRmFsc2UpKQogICAgbXV0YXRpb24gPSBib29sKHJlYWRpbmVzcy5nZXQoIm11dGF0aW9uX2FsbG93ZWQiLCBGYWxzZSkpCgogICAgaWYgYmxvY2tlZCA+IDAgYW5kIGVsaWdpYmxlID09IDAgYW5kIG5vdCBlbmZvcmNlbWVudCBhbmQgbm90IG11dGF0aW9uOgogICAgICAgIHJldHVybiB7CiAgICAgICAgICAgICJpZCI6ICJORi1BQ1RJVkUtMDAxIiwKICAgICAgICAgICAgInJhbmsiOiAxLAogICAgICAgICAgICAic3VyZmFjZSI6ICJlbmZvcmNlbWVudF9yZWFkaW5lc3MiLAogICAgICAgICAgICAic2lnbmFsIjogImFsbF9jb250cm9sbGVkX2Rvd25ncmFkZXNfYmxvY2tlZCIsCiAgICAgICAgICAgICJzZXZlcml0eSI6ICJoaWdoIiwKICAgICAgICAgICAgInRhcmdldF9uZXh0IjogIlRBVS1TQ0FMSU5HLVNBIHYwLjUuMiAtIE92ZXItUGVuYWx0eSBDYXVzZSBEZWNvbXBvc2l0aW9uIiwKICAgICAgICAgICAgInJlY29tbWVuZGF0aW9uIjogIkRlY29tcG9zZSB3aHkgYWxsIGNvbnRyb2xsZWQgZG93bmdyYWRlcyBhcmUgYmxvY2tlZCBiZWZvcmUgYW55IGVuZm9yY2VtZW50LWNhbmRpZGF0ZSBkZXNpZ24uIiwKICAgICAgICAgICAgImV2aWRlbmNlIjogewogICAgICAgICAgICAgICAgImJsb2NrZWRfYnlfb3Zlcl9wZW5hbHR5X2NvdW50IjogYmxvY2tlZCwKICAgICAgICAgICAgICAgICJlbGlnaWJsZV9jYW5kaWRhdGVfZGVzaWduX2NvdW50IjogZWxpZ2libGUsCiAgICAgICAgICAgICAgICAiZW5mb3JjZW1lbnRfY2FuZGlkYXRlX2VuYWJsZWQiOiBlbmZvcmNlbWVudCwKICAgICAgICAgICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogbXV0YXRpb24sCiAgICAgICAgICAgICAgICAic291cmNlIjogInJlcG9ydHMvZW5mb3JjZW1lbnRfcmVhZGluZXNzL2xhdGVzdF9lbmZvcmNlbWVudF9yZWFkaW5lc3NfZ2F0ZS5qc29uIiwKICAgICAgICAgICAgfSwKICAgICAgICB9CgogICAgcmV0dXJuIHsKICAgICAgICAiaWQiOiAiTkYtQUNUSVZFLTAwMSIsCiAgICAgICAgInJhbmsiOiAxLAogICAgICAgICJzdXJmYWNlIjogIm5leHVzX2ZlZWRiYWNrIiwKICAgICAgICAic2lnbmFsIjogIm5vX2FjdGl2ZV9ibG9ja2VyX2RldGVjdGVkIiwKICAgICAgICAic2V2ZXJpdHkiOiAibG93IiwKICAgICAgICAidGFyZ2V0X25leHQiOiAiVEFVLVNDQUxJTkctU0EgdjAuNS4yIC0gTmV4dXMgTWFpbnRlbmFuY2UiLAogICAgICAgICJyZWNvbW1lbmRhdGlvbiI6ICJObyBhY3RpdmUgZW5mb3JjZW1lbnQgYmxvY2tlciBkZXRlY3RlZDsgbWFpbnRhaW4gTmV4dXMgdGFyZ2V0IHRyYWNraW5nLiIsCiAgICAgICAgImV2aWRlbmNlIjogewogICAgICAgICAgICAic291cmNlIjogInJlcG9ydHMvZW5mb3JjZW1lbnRfcmVhZGluZXNzL2xhdGVzdF9lbmZvcmNlbWVudF9yZWFkaW5lc3NfZ2F0ZS5qc29uIiwKICAgICAgICB9LAogICAgfQoKZGVmIGdlbmVyYXRlX2NoYXJ0cyhzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gbGlzdFtzdHJdOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0IiwgZiJtYXRwbG90bGliIHVuYXZhaWxhYmxlOiB7ZXhjfVxuIikKICAgICAgICByZXR1cm4gcGF0aHMKCiAgICBWSVNfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShwYXRoOiBQYXRoKSAtPiBOb25lOgogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHBhdGgsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQoc3RyKHBhdGgucmVsYXRpdmVfdG8oUkVQT19ST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQoKICAgIHN0YXR1c19jb3VudHMgPSBzdW1tYXJ5WyJzdGF0dXNfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3Qoc3RhdHVzX2NvdW50cy5rZXlzKCkpLCBsaXN0KHN0YXR1c19jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlByaW9yaXR5IGNvdW50IikKICAgIHBsdC50aXRsZSgiTmV4dXMgUHJpb3JpdHkgQ29tcGxldGlvbiBTdGF0dXMiKQogICAgc2F2ZShWSVNfRElSIC8gIm5leHVzX3ByaW9yaXR5X2NvbXBsZXRpb25fc3RhdHVzLnBuZyIpCgogICAgYWN0aXZlID0gc3VtbWFyeVsiYWN0aXZlX2Jsb2NrZXIiXVsiZXZpZGVuY2UiXQogICAga2V5cyA9IFsiYmxvY2tlZF9ieV9vdmVyX3BlbmFsdHlfY291bnQiLCAiZWxpZ2libGVfY2FuZGlkYXRlX2Rlc2lnbl9jb3VudCJdCiAgICB2YWxzID0gW2FjdGl2ZS5nZXQoaywgMCkgZm9yIGsgaW4ga2V5c10KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGtleXMsIHZhbHMpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJDdXJyZW50IEFjdGl2ZSBFbmZvcmNlbWVudCBCbG9ja2VyIikKICAgIHNhdmUoVklTX0RJUiAvICJhY3RpdmVfZW5mb3JjZW1lbnRfYmxvY2tlcl9jb3VudHMucG5nIikKCiAgICBzZXZlcml0eV9jb3VudHMgPSBzdW1tYXJ5WyJyZXRpcmVkX3NldmVyaXR5X2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KHNldmVyaXR5X2NvdW50cy5rZXlzKCkpLCBsaXN0KHNldmVyaXR5X2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiUmV0aXJlZCBwcmlvcml0eSBjb3VudCIpCiAgICBwbHQudGl0bGUoIlJldGlyZWQgUHJpb3JpdGllcyBieSBTZXZlcml0eSIpCiAgICBzYXZlKFZJU19ESVIgLyAicmV0aXJlZF9wcmlvcml0eV9zZXZlcml0eV9jb3VudHMucG5nIikKCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZW5kZXJfbWQoc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjUuMSBOZXh1cyBUYXJnZXQgUmVmcmVzaCBhbmQgQ29tcGxldGVkLVNpZ25hbCBSZXRpcmVtZW50IiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSW5wdXQgTmV4dXMgcHJpb3JpdGllczogYHtzdW1tYXJ5WydpbnB1dF9wcmlvcml0eV9jb3VudCddfWAiLAogICAgICAgIGYiLSBDb21wbGV0ZWQvcmV0aXJlZCBwcmlvcml0aWVzOiBge3N1bW1hcnlbJ2NvbXBsZXRlZF9zaWduYWxfY291bnQnXX1gIiwKICAgICAgICBmIi0gQWN0aXZlIHByaW9yaXRpZXMgcmV0YWluZWQgZnJvbSBvbGQgTmV4dXM6IGB7c3VtbWFyeVsnYWN0aXZlX29sZF9zaWduYWxfY291bnQnXX1gIiwKICAgICAgICBmIi0gQ3VycmVudCBhY3RpdmUgYmxvY2tlcjogYHtzdW1tYXJ5WydhY3RpdmVfYmxvY2tlciddWydzaWduYWwnXX1gIiwKICAgICAgICBmIi0gTmV4dCBjdXJyZW50IHRhcmdldDogYHtzdW1tYXJ5WyduZXh0X2N1cnJlbnRfdGFyZ2V0J119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c3VtbWFyeVsnbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBQb2xpY3kgZW5mb3JjZWQ6IGB7c3VtbWFyeVsncG9saWN5X2VuZm9yY2VkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJldGlyZWQgLyBBY3RpdmUgT2xkIFByaW9yaXRpZXMiLAogICAgICAgICIiLAogICAgICAgICJ8IElEIHwgT2xkIHRhcmdldCB8IFN0YXR1cyB8IFJlYXNvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHJvdyBpbiBzdW1tYXJ5WyJwcmlvcml0eV9yZWZyZXNoX3Jvd3MiXToKICAgICAgICByZWFzb24gPSByb3dbImNvbXBsZXRpb25fcmVhc29uIl0ucmVwbGFjZSgifCIsICJcXHwiKQogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtyb3dbJ2lkJ119YCB8IGB7cm93Wyd0YXJnZXRfbmV4dCddfWAgfCBge3Jvd1snY29tcGxldGlvbl9zdGF0dXMnXX1gIHwge3JlYXNvbn0gfCIpCgogICAgYWN0aXZlID0gc3VtbWFyeVsiYWN0aXZlX2Jsb2NrZXIiXQogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBOZXcgQWN0aXZlIEJsb2NrZXIiLAogICAgICAgICIiLAogICAgICAgIGYiLSBJRDogYHthY3RpdmVbJ2lkJ119YCIsCiAgICAgICAgZiItIFN1cmZhY2U6IGB7YWN0aXZlWydzdXJmYWNlJ119YCIsCiAgICAgICAgZiItIFNpZ25hbDogYHthY3RpdmVbJ3NpZ25hbCddfWAiLAogICAgICAgIGYiLSBTZXZlcml0eTogYHthY3RpdmVbJ3NldmVyaXR5J119YCIsCiAgICAgICAgZiItIFJlY29tbWVuZGF0aW9uOiB7YWN0aXZlWydyZWNvbW1lbmRhdGlvbiddfSIsCiAgICAgICAgZiItIFRhcmdldCBuZXh0OiBge2FjdGl2ZVsndGFyZ2V0X25leHQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KCiAgICBmb3IgY2hhcnQgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUkVQT19ST09UIC8gY2hhcnQsIE9VVF9ESVIpLnJlcGxhY2UoIlxcIiwgIi8iKQogICAgICAgIGxpbmVzICs9IFtmIiFbe1BhdGgoY2hhcnQpLnN0ZW19XSh7cmVsfSkiLCAiIl0KCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiMjIEJvdW5kYXJ5IiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJib3VuZGFyeSJdLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIG5leHVzID0gcmVhZF9qc29uKE5FWFVTX1BBVEgpCiAgICByZWFkaW5lc3MgPSByZWFkX2pzb24oUkVBRElORVNTX1BBVEgpCgogICAgcHJpb3JpdGllcyA9IG5leHVzLmdldCgicHJpb3JpdGllcyIsIFtdKQogICAgcm93cyA9IFtjbGFzc2lmeV9wcmlvcml0eShwKSBmb3IgcCBpbiBwcmlvcml0aWVzXQogICAgc3RhdHVzX2NvdW50cyA9IENvdW50ZXIoclsiY29tcGxldGlvbl9zdGF0dXMiXSBmb3IgciBpbiByb3dzKQogICAgcmV0aXJlZCA9IFtyIGZvciByIGluIHJvd3MgaWYgclsiY29tcGxldGlvbl9zdGF0dXMiXSA9PSAiQ09NUExFVEVEX1JFVElSRUQiXQogICAgYWN0aXZlX29sZCA9IFtyIGZvciByIGluIHJvd3MgaWYgclsiY29tcGxldGlvbl9zdGF0dXMiXSA9PSAiQUNUSVZFIl0KICAgIHJldGlyZWRfc2V2ZXJpdHlfY291bnRzID0gQ291bnRlcihyLmdldCgic2V2ZXJpdHkiLCAidW5rbm93biIpIGZvciByIGluIHJldGlyZWQpCiAgICBhY3RpdmVfYmxvY2tlciA9IGJ1aWxkX2FjdGl2ZV9ibG9ja2VyKHJlYWRpbmVzcykKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctbmV4dXMtdGFyZ2V0LXJlZnJlc2gtdjAuNS4xIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgImlucHV0X25leHVzX2ZlZWRiYWNrIjogInJlcG9ydHMvbmV4dXNfZmVlZGJhY2svbGF0ZXN0X25leHVzX2ZlZWRiYWNrLmpzb24iLAogICAgICAgICJpbnB1dF9lbmZvcmNlbWVudF9yZWFkaW5lc3MiOiAicmVwb3J0cy9lbmZvcmNlbWVudF9yZWFkaW5lc3MvbGF0ZXN0X2VuZm9yY2VtZW50X3JlYWRpbmVzc19nYXRlLmpzb24iLAogICAgICAgICJpbnB1dF9wcmlvcml0eV9jb3VudCI6IGxlbihwcmlvcml0aWVzKSwKICAgICAgICAiY29tcGxldGVkX3NpZ25hbF9jb3VudCI6IGxlbihyZXRpcmVkKSwKICAgICAgICAiYWN0aXZlX29sZF9zaWduYWxfY291bnQiOiBsZW4oYWN0aXZlX29sZCksCiAgICAgICAgInN0YXR1c19jb3VudHMiOiBkaWN0KHN0YXR1c19jb3VudHMpLAogICAgICAgICJyZXRpcmVkX3NldmVyaXR5X2NvdW50cyI6IGRpY3QocmV0aXJlZF9zZXZlcml0eV9jb3VudHMpLAogICAgICAgICJwcmlvcml0eV9yZWZyZXNoX3Jvd3MiOiByb3dzLAogICAgICAgICJhY3RpdmVfYmxvY2tlciI6IGFjdGl2ZV9ibG9ja2VyLAogICAgICAgICJuZXh0X2N1cnJlbnRfdGFyZ2V0IjogYWN0aXZlX2Jsb2NrZXJbInRhcmdldF9uZXh0Il0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImJvdW5kYXJ5IjogIk5leHVzIHRhcmdldCByZWZyZXNoIGlzIHJlcG9zaXRvcnkgc2VsZi1vYnNlcnZhdGlvbiBhbmQgcXVldWUgaHlnaWVuZSBvbmx5LiBJdCBkb2VzIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciBhbmQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogYWN0aXZlX2Jsb2NrZXJbInRhcmdldF9uZXh0Il0sCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnkpCgogICAgT1VUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAibmV4dXNfdGFyZ2V0X3JlZnJlc2hfdjBfNV8xLmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfanNvbihPVVRfRElSIC8gImxhdGVzdF9uZXh1c190YXJnZXRfcmVmcmVzaC5qc29uIiwgc3VtbWFyeSkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJuZXh1c190YXJnZXRfcmVmcmVzaF92MF81XzEubWQiLCByZW5kZXJfbWQoc3VtbWFyeSkpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAibGF0ZXN0X25leHVzX3RhcmdldF9yZWZyZXNoLm1kIiwgcmVuZGVyX21kKHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiaW5wdXRfcHJpb3JpdHlfY291bnQiOiBzdW1tYXJ5WyJpbnB1dF9wcmlvcml0eV9jb3VudCJdLAogICAgICAgICJjb21wbGV0ZWRfc2lnbmFsX2NvdW50Ijogc3VtbWFyeVsiY29tcGxldGVkX3NpZ25hbF9jb3VudCJdLAogICAgICAgICJhY3RpdmVfb2xkX3NpZ25hbF9jb3VudCI6IHN1bW1hcnlbImFjdGl2ZV9vbGRfc2lnbmFsX2NvdW50Il0sCiAgICAgICAgIm5leHRfY3VycmVudF90YXJnZXQiOiBzdW1tYXJ5WyJuZXh0X2N1cnJlbnRfdGFyZ2V0Il0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvbmV4dXNfdGFyZ2V0X3JlZnJlc2gvbGF0ZXN0X25leHVzX3RhcmdldF9yZWZyZXNoLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
write(ROOT / "scripts" / "feedback" / "run_nexus_target_refresh.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "nexus_target_refresh" / "README.md", """# Nexus Target Refresh Reports

Current layer: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**

## Purpose

This folder stores reports that retire completed Nexus targets and promote the current active blocker.

## Primary command

```powershell
python scripts/feedback/run_nexus_target_refresh.py
```

## README Update Rule

Update this mini README whenever Nexus target-refresh schemas, report paths, or signal-retirement rules change.

Boundary: target refresh is repository self-observation only.
""")

write(ROOT / "visuals" / "nexus_target_refresh" / "README.md", """# Nexus Target Refresh Visuals

Current layer: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**

## Purpose

This folder stores charts summarizing Nexus target completion and active blocker promotion.

## README Update Rule

Update this mini README whenever target-refresh chart names or meanings change.

Boundary: target-refresh visuals are repository self-observation diagnostics only.
""")

write(ROOT / "visuals" / "nexus_target_refresh" / "v0_5_1" / "README.md", """# v0.5.1 Nexus Target Refresh Charts

## Expected Charts

- `nexus_priority_completion_status.png`
- `active_enforcement_blocker_counts.png`
- `retired_priority_severity_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local Nexus queue diagnostics only.
""")

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.0[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.9[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.0 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.1 |", r)

if "| Nexus target refresh | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |" not in r:
    r = r.replace("| Enforcement readiness charts | `visuals/enforcement_readiness/v0_5_0/` |\n",
                  "| Enforcement readiness charts | `visuals/enforcement_readiness/v0_5_0/` |\n| Nexus target refresh | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |\n| Nexus target refresh charts | `visuals/nexus_target_refresh/v0_5_1/` |\n")

if "python scripts/feedback/run_nexus_target_refresh.py" not in r:
    r = r.replace("python scripts/feedback/run_nexus_feedback.py\npython scripts/release/validate_release.py",
                  "python scripts/feedback/run_nexus_feedback.py\npython scripts/feedback/run_nexus_target_refresh.py\npython scripts/release/validate_release.py")

if "    nexus_target_refresh/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    nexus_target_refresh/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    nexus_target_refresh/\n")

section = """## Nexus Target Refresh and Completed-Signal Retirement v0.5.1

v0.5.1 repairs stale reflective routing after v0.5.0 enforcement readiness.

Primary command:

```powershell
python scripts/feedback/run_nexus_target_refresh.py
```

Primary outputs:

```text
reports/nexus_target_refresh/latest_nexus_target_refresh.json
reports/nexus_target_refresh/latest_nexus_target_refresh.md
visuals/nexus_target_refresh/v0_5_1/
```

This layer answers:

```text
which old Nexus priorities are completed
which stale recommendations should retire
what the current active blocker is
what the next current target should be
```

Current active blocker:

```text
all_controlled_downgrades_blocked
```

Boundary: Nexus target refresh is repository self-observation and queue hygiene only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Nexus Target Refresh and Completed-Signal Retirement v0.5.1" not in r:
    r = r.replace("## Enforcement Readiness Gate v0.5.0", section + "## Enforcement Readiness Gate v0.5.0", 1)

lesson = "| L-033 | v0.5.0 completed the dry-run through enforcement-readiness chain, but Nexus still ranked the old v0.4.6 dry-run target as active. | A healthy feedback score can still carry stale priorities if completed targets are not retired. | Reflective feedback must retire completed targets and promote the current active blocker, or the repo will keep recommending already-completed work. |"
if "L-033" not in r:
    r = r.replace("| L-032 | v0.4.9 showed that all six controlled downgrade candidates triggered over-penalty review. | A review gate that blocks every candidate may indicate true policy harshness or heuristic over-sensitivity. | When regression review blocks every candidate, do not proceed to enforcement design; first promote the blocked state into a major enforcement-readiness gate with all mutation disabled. |\n",
                  "| L-032 | v0.4.9 showed that all six controlled downgrade candidates triggered over-penalty review. | A review gate that blocks every candidate may indicate true policy harshness or heuristic over-sensitivity. | When regression review blocks every candidate, do not proceed to enforcement design; first promote the blocked state into a major enforcement-readiness gate with all mutation disabled. |\n" + lesson + "\n")

if "| v0.5.1 | Nexus target refresh and completed-signal retirement after v0.5.0. |" not in r:
    r = r.replace("| v0.5.0 | Enforcement readiness gate for blocked policy candidates with classifier mutation disabled. |\n",
                  "| v0.5.0 | Enforcement readiness gate for blocked policy candidates with classifier mutation disabled. |\n| v0.5.1 | Nexus target refresh and completed-signal retirement after v0.5.0. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**

Recommended goals:

- Decompose why all six controlled downgrades are blocked.
- Separate diagnostic-support over-sensitivity from missing provenance and high drift severity.
- Emit cause-specific remediation cards.
- Preserve non-claim locks: cause decomposition is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**", a)
if "Nexus target refresh patch" not in a:
    a = a.replace("| Enforcement readiness patch | `reports/enforcement_readiness/`, `visuals/enforcement_readiness/`, regression review | readiness gate + release validator; enforcement_candidate_enabled must remain false |\n",
                  "| Enforcement readiness patch | `reports/enforcement_readiness/`, `visuals/enforcement_readiness/`, regression review | readiness gate + release validator; enforcement_candidate_enabled must remain false |\n| Nexus target refresh patch | `reports/nexus_target_refresh/`, `visuals/nexus_target_refresh/`, Nexus feedback + readiness gate | target-refresh report + release validator; no classifier mutation |\n")
write(agents, a)

# route map
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.5.1"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_5_routes", {})
route["v0_5_routes"]["nexus_target_refresh"] = {
    "read_first": ["reports/nexus_feedback/latest_nexus_feedback.json", "reports/enforcement_readiness/latest_enforcement_readiness_gate.json"],
    "validate": ["python scripts/feedback/run_nexus_target_refresh.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/nexus_target_refresh/latest_nexus_target_refresh.md", "visuals/nexus_target_refresh/v0_5_1/"],
    "mutation_lock": "Does not change classifier behavior; refreshes reflective queue only."
}
write_json(route_path, route)

# task matrix
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**", m)
if "| Nexus target refresh patch |" not in m:
    m = m.replace("| Enforcement readiness patch | outer | validation | governance | regression review + readiness gate | readiness report + charts + release validator | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n",
                  "| Enforcement readiness patch | outer | validation | governance | regression review + readiness gate | readiness report + charts + release validator | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n| Nexus target refresh patch | outer | drift | feedback | Nexus feedback + readiness gate | target-refresh report + charts + release validator | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |\n")
write(matrix, m)

# atlas
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.5.1 | Nexus target refresh |" not in t:
    t = t.replace("| v0.5.0 | Enforcement readiness gate | `python scripts/benchmarks/run_enforcement_readiness_gate.py` | Major checkpoint that blocks enforcement when over-penalty review fails | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` | `visuals/enforcement_readiness/v0_5_0/` |\n",
                  "| v0.5.0 | Enforcement readiness gate | `python scripts/benchmarks/run_enforcement_readiness_gate.py` | Major checkpoint that blocks enforcement when over-penalty review fails | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` | `visuals/enforcement_readiness/v0_5_0/` |\n| v0.5.1 | Nexus target refresh | `python scripts/feedback/run_nexus_target_refresh.py` | Retires completed Nexus targets and promotes the current active blocker | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` | `visuals/nexus_target_refresh/v0_5_1/` |\n")
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_5_1_nexus_target_refresh.md", f"""# TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement

Generated: {GENERATED_AT}

## Purpose

Retire stale Nexus targets that were completed by v0.4.6-v0.5.0 and promote the current active blocker.

## Adds

- `scripts/feedback/run_nexus_target_refresh.py`
- `reports/nexus_target_refresh/`
- `visuals/nexus_target_refresh/v0_5_1/`

## Boundary

Nexus target refresh is repository self-observation and queue hygiene only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.5.1 Nexus target refresh patch written")
