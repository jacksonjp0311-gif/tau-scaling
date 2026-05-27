
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
        dest = ROOT / "reports" / "enforcement_readiness" / "v0_5_0" / "backups" / f"{path.name}_before_v0_5_0_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KUkVHUkVTU0lPTl9QQVRIID0gUkVQT19ST09UIC8gInJlcG9ydHMiIC8gInJlZ3Jlc3Npb25fcmV2aWV3IiAvICJsYXRlc3RfcmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3Lmpzb24iCk9VVF9ESVIgPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAiZW5mb3JjZW1lbnRfcmVhZGluZXNzIgpWSVNfRElSID0gUkVQT19ST09UIC8gInZpc3VhbHMiIC8gImVuZm9yY2VtZW50X3JlYWRpbmVzcyIgLyAidjBfNV8wIgoKVEhSRVNIT0xEUyA9IFswLjcwLCAwLjc1LCAwLjgwLCAwLjg1LCAwLjkwLCAwLjk1XQoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHJldHVybiBqc29uLmxvYWRzKHBhdGgucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQoKZGVmIHdyaXRlX2pzb24ocGF0aDogUGF0aCwgcGF5bG9hZDogQW55KSAtPiBOb25lOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMocGF5bG9hZCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3JpdGVfdGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB0aHJlc2hvbGRfZmxhZ3Mocm93OiBkaWN0W3N0ciwgQW55XSwgdGhyZXNob2xkOiBmbG9hdCkgLT4gZGljdFtzdHIsIEFueV06CiAgICBkaWFnID0gcm93LmdldCgiY3VycmVudF9kaWFnbm9zdGljX2F2ZXJhZ2UiKQogICAgZmluZGluZ3NfY291bnQgPSBpbnQocm93LmdldCgiZmluZGluZ3NfY291bnQiLCAwKSBvciAwKQogICAgc2V2ZXJpdHkgPSBpbnQocm93LmdldCgiZHJpZnRfc2V2ZXJpdHkiLCAwKSBvciAwKQoKICAgIGhpZ2hfc3VwcG9ydCA9IGlzaW5zdGFuY2UoZGlhZywgKGludCwgZmxvYXQpKSBhbmQgZGlhZyA+PSB0aHJlc2hvbGQKICAgIG1pc3NpbmdfZmluZGluZ3MgPSBmaW5kaW5nc19jb3VudCA9PSAwCiAgICBoaWdoX3NldmVyaXR5ID0gc2V2ZXJpdHkgPj0gMgoKICAgIHJlYXNvbnMgPSBbXQogICAgaWYgaGlnaF9zdXBwb3J0OgogICAgICAgIHJlYXNvbnMuYXBwZW5kKCJoaWdoX2RpYWdub3N0aWNfc3VwcG9ydCIpCiAgICBpZiBtaXNzaW5nX2ZpbmRpbmdzOgogICAgICAgIHJlYXNvbnMuYXBwZW5kKCJtaXNzaW5nX2ZpbmRpbmdfcHJvdmVuYW5jZSIpCiAgICBpZiBoaWdoX3NldmVyaXR5OgogICAgICAgIHJlYXNvbnMuYXBwZW5kKCJoaWdoX2RyaWZ0X3NldmVyaXR5IikKCiAgICByZXR1cm4gewogICAgICAgICJ0aHJlc2hvbGQiOiB0aHJlc2hvbGQsCiAgICAgICAgImhpZ2hfc3VwcG9ydF9mbGFnIjogaGlnaF9zdXBwb3J0LAogICAgICAgICJtaXNzaW5nX2ZpbmRpbmdzX2ZsYWciOiBtaXNzaW5nX2ZpbmRpbmdzLAogICAgICAgICJoaWdoX3NldmVyaXR5X2ZsYWciOiBoaWdoX3NldmVyaXR5LAogICAgICAgICJhY3RpdmVfcmVhc29ucyI6IHJlYXNvbnMsCiAgICAgICAgIm92ZXJfcGVuYWx0eV9mbGFnIjogYm9vbChyZWFzb25zKSwKICAgIH0KCmRlZiByZWFkaW5lc3Nfcm93KHJvdzogZGljdFtzdHIsIEFueV0pIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgY2FuZGlkYXRlID0gcm93LmdldCgiZGVjaXNpb24iKSA9PSAiQVBQUk9WRV9GT1JfUkVHUkVTU0lPTl9SRVZJRVciCiAgICBodW1hbl9yZXZpZXcgPSByb3cuZ2V0KCJkZWNpc2lvbiIpID09ICJERUZFUl9UT19IVU1BTl9SRVZJRVciCiAgICBiYXNlbGluZSA9IHRocmVzaG9sZF9mbGFncyhyb3csIDAuNzUpCgogICAgaWYgaHVtYW5fcmV2aWV3OgogICAgICAgIHN0YXR1cyA9ICJIVU1BTl9SRVZJRVdfT05MWSIKICAgICAgICBhY3Rpb24gPSAiUHJlc2VydmUgaHVtYW4tcmV2aWV3IHJvdXRpbmcuIERvIG5vdCBjb252ZXJ0IHRvIGF1dG9tYXRpYyBkb3duZ3JhZGUuIgogICAgZWxpZiBjYW5kaWRhdGUgYW5kIGJhc2VsaW5lWyJvdmVyX3BlbmFsdHlfZmxhZyJdOgogICAgICAgIHN0YXR1cyA9ICJCTE9DS0VEX0JZX09WRVJfUEVOQUxUWSIKICAgICAgICBhY3Rpb24gPSAiRG8gbm90IGVuZm9yY2UuIENhbmRpZGF0ZSBtdXN0IGJlIGNhbGlicmF0ZWQgb3IgbmFycm93ZWQgYmVmb3JlIGFueSBlbmZvcmNlbWVudCBkZXNpZ24uIgogICAgZWxpZiBjYW5kaWRhdGU6CiAgICAgICAgc3RhdHVzID0gIkVMSUdJQkxFX0ZPUl9DQU5ESURBVEVfREVTSUdOIgogICAgICAgIGFjdGlvbiA9ICJFbGlnaWJsZSBmb3IgZGlzYWJsZWQgZW5mb3JjZW1lbnQtY2FuZGlkYXRlIGRlc2lnbiBvbmx5LiIKICAgIGVsc2U6CiAgICAgICAgc3RhdHVzID0gIlJFVEFJTl9DVVJSRU5UX0JFSEFWSU9SIgogICAgICAgIGFjdGlvbiA9ICJObyBlbmZvcmNlbWVudCBwYXRoLiIKCiAgICByZXR1cm4gewogICAgICAgICJnYXRlX3BhaXIiOiByb3cuZ2V0KCJnYXRlX3BhaXIiKSwKICAgICAgICAiZ2F0ZV9hIjogcm93LmdldCgiZ2F0ZV9hIiksCiAgICAgICAgImdhdGVfYiI6IHJvdy5nZXQoImdhdGVfYiIpLAogICAgICAgICJkZWNpc2lvbiI6IHJvdy5nZXQoImRlY2lzaW9uIiksCiAgICAgICAgImN1cnJlbnRfY2xhc3NpZmljYXRpb24iOiByb3cuZ2V0KCJjdXJyZW50X2NsYXNzaWZpY2F0aW9uIiksCiAgICAgICAgInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iOiByb3cuZ2V0KCJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIiksCiAgICAgICAgImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIjogcm93LmdldCgiY3VycmVudF9kaWFnbm9zdGljX2F2ZXJhZ2UiKSwKICAgICAgICAiZmluZGluZ3NfY291bnQiOiByb3cuZ2V0KCJmaW5kaW5nc19jb3VudCIpLAogICAgICAgICJkcmlmdF9zZXZlcml0eSI6IHJvdy5nZXQoImRyaWZ0X3NldmVyaXR5IiksCiAgICAgICAgImJhc2VsaW5lX292ZXJfcGVuYWx0eV9yZWFzb25zIjogYmFzZWxpbmVbImFjdGl2ZV9yZWFzb25zIl0sCiAgICAgICAgInJlYWRpbmVzc19zdGF0dXMiOiBzdGF0dXMsCiAgICAgICAgInJlY29tbWVuZGVkX2FjdGlvbiI6IGFjdGlvbiwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgIH0KCmRlZiBjYWxpYnJhdGlvbl9zd2VlcChyb3dzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICBjYW5kaWRhdGVzID0gW3IgZm9yIHIgaW4gcm93cyBpZiByLmdldCgiZGVjaXNpb24iKSA9PSAiQVBQUk9WRV9GT1JfUkVHUkVTU0lPTl9SRVZJRVciXQogICAgc3dlZXAgPSBbXQogICAgZm9yIHRocmVzaG9sZCBpbiBUSFJFU0hPTERTOgogICAgICAgIGZsYWdzID0gW3RocmVzaG9sZF9mbGFncyhyLCB0aHJlc2hvbGQpIGZvciByIGluIGNhbmRpZGF0ZXNdCiAgICAgICAgb3Zlcl9jb3VudCA9IHN1bSgxIGZvciBmIGluIGZsYWdzIGlmIGZbIm92ZXJfcGVuYWx0eV9mbGFnIl0pCiAgICAgICAgcGFzc19jb3VudCA9IGxlbihjYW5kaWRhdGVzKSAtIG92ZXJfY291bnQKICAgICAgICBzd2VlcC5hcHBlbmQoewogICAgICAgICAgICAidGhyZXNob2xkIjogdGhyZXNob2xkLAogICAgICAgICAgICAiY2FuZGlkYXRlX2NvdW50IjogbGVuKGNhbmRpZGF0ZXMpLAogICAgICAgICAgICAib3Zlcl9wZW5hbHR5X2NvdW50Ijogb3Zlcl9jb3VudCwKICAgICAgICAgICAgInBhc3NfY291bnQiOiBwYXNzX2NvdW50LAogICAgICAgICAgICAiaGlnaF9zdXBwb3J0X2NvdW50Ijogc3VtKDEgZm9yIGYgaW4gZmxhZ3MgaWYgZlsiaGlnaF9zdXBwb3J0X2ZsYWciXSksCiAgICAgICAgICAgICJtaXNzaW5nX2ZpbmRpbmdzX2NvdW50Ijogc3VtKDEgZm9yIGYgaW4gZmxhZ3MgaWYgZlsibWlzc2luZ19maW5kaW5nc19mbGFnIl0pLAogICAgICAgICAgICAiaGlnaF9zZXZlcml0eV9jb3VudCI6IHN1bSgxIGZvciBmIGluIGZsYWdzIGlmIGZbImhpZ2hfc2V2ZXJpdHlfZmxhZyJdKSwKICAgICAgICB9KQogICAgcmV0dXJuIHN3ZWVwCgpkZWYgZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnk6IGRpY3Rbc3RyLCBBbnldKSAtPiBsaXN0W3N0cl06CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgd3JpdGVfdGV4dChPVVRfRElSIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBmIm1hdHBsb3RsaWIgdW5hdmFpbGFibGU6IHtleGN9XG4iKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJU19ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKHBhdGg6IFBhdGgpIC0+IE5vbmU6CiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocGF0aCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikpCgogICAgcmVhZGluZXNzX2NvdW50cyA9IHN1bW1hcnlbInJlYWRpbmVzc19zdGF0dXNfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QocmVhZGluZXNzX2NvdW50cy5rZXlzKCkpLCBsaXN0KHJlYWRpbmVzc19jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNhc2UgY291bnQiKQogICAgcGx0LnRpdGxlKCJ2MC41LjAgRW5mb3JjZW1lbnQgUmVhZGluZXNzIFN0YXR1cyIpCiAgICBzYXZlKFZJU19ESVIgLyAiZW5mb3JjZW1lbnRfcmVhZGluZXNzX3N0YXR1c19jb3VudHMucG5nIikKCiAgICBzd2VlcCA9IHN1bW1hcnlbImNhbGlicmF0aW9uX3N3ZWVwIl0KICAgIHggPSBbclsidGhyZXNob2xkIl0gZm9yIHIgaW4gc3dlZXBdCiAgICBvdmVyID0gW3JbIm92ZXJfcGVuYWx0eV9jb3VudCJdIGZvciByIGluIHN3ZWVwXQogICAgcGFzc2VkID0gW3JbInBhc3NfY291bnQiXSBmb3IgciBpbiBzd2VlcF0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQucGxvdCh4LCBvdmVyLCBtYXJrZXI9Im8iLCBsYWJlbD0ib3Zlci1wZW5hbHR5IGNvdW50IikKICAgIHBsdC5wbG90KHgsIHBhc3NlZCwgbWFya2VyPSJvIiwgbGFiZWw9InBhc3MgY291bnQiKQogICAgcGx0LnhsYWJlbCgiRGlhZ25vc3RpYyBzdXBwb3J0IHRocmVzaG9sZCIpCiAgICBwbHQueWxhYmVsKCJDYW5kaWRhdGUgY291bnQiKQogICAgcGx0LnRpdGxlKCJ2MC41LjAgQ2FsaWJyYXRpb24gU3dlZXAiKQogICAgcGx0LmxlZ2VuZCgpCiAgICBzYXZlKFZJU19ESVIgLyAiZW5mb3JjZW1lbnRfcmVhZGluZXNzX2NhbGlicmF0aW9uX3N3ZWVwLnBuZyIpCgogICAgZ2F0ZV9jb3VudHMgPSBzdW1tYXJ5WyJibG9ja2VkX2dhdGVfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZV9jb3VudHMua2V5cygpKSwgbGlzdChnYXRlX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTQ1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQmxvY2tlZCBjYW5kaWRhdGUgaW52b2x2ZW1lbnQiKQogICAgcGx0LnRpdGxlKCJCbG9ja2VkIENhbmRpZGF0ZSBJbnZvbHZlbWVudCBieSBHYXRlIikKICAgIHNhdmUoVklTX0RJUiAvICJibG9ja2VkX2NhbmRpZGF0ZV9nYXRlX2NvdW50cy5wbmciKQoKICAgIHJldHVybiBwYXRocwoKZGVmIHJlbmRlcl9tZChzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gc3RyOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNS4wIEVuZm9yY2VtZW50IFJlYWRpbmVzcyBHYXRlIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSW5wdXQgcmV2aWV3IHJvd3M6IGB7c3VtbWFyeVsnaW5wdXRfcmV2aWV3X3Jvd3MnXX1gIiwKICAgICAgICBmIi0gQ29udHJvbGxlZCBkb3duZ3JhZGUgY2FuZGlkYXRlczogYHtzdW1tYXJ5Wydjb250cm9sbGVkX2Rvd25ncmFkZV9jYW5kaWRhdGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gQmxvY2tlZCBieSBvdmVyLXBlbmFsdHk6IGB7c3VtbWFyeVsnYmxvY2tlZF9ieV9vdmVyX3BlbmFsdHlfY291bnQnXX1gIiwKICAgICAgICBmIi0gSHVtYW4gcmV2aWV3IG9ubHk6IGB7c3VtbWFyeVsnaHVtYW5fcmV2aWV3X29ubHlfY291bnQnXX1gIiwKICAgICAgICBmIi0gRWxpZ2libGUgZm9yIGRpc2FibGVkIGNhbmRpZGF0ZSBkZXNpZ246IGB7c3VtbWFyeVsnZWxpZ2libGVfY2FuZGlkYXRlX2Rlc2lnbl9jb3VudCddfWAiLAogICAgICAgIGYiLSBFbmZvcmNlbWVudCBjYW5kaWRhdGUgZW5hYmxlZDogYHtzdW1tYXJ5WydlbmZvcmNlbWVudF9jYW5kaWRhdGVfZW5hYmxlZCddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3N1bW1hcnlbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gUG9saWN5IGVuZm9yY2VkOiBge3N1bW1hcnlbJ3BvbGljeV9lbmZvcmNlZCddfWAiLAogICAgICAgIGYiLSBGaW5hbCByZWNvbW1lbmRhdGlvbjogYHtzdW1tYXJ5WydmaW5hbF9yZWNvbW1lbmRhdGlvbiddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBSZWFkaW5lc3MgU3RhdHVzIENvdW50cyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU3RhdHVzIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc3VtbWFyeVsicmVhZGluZXNzX3N0YXR1c19jb3VudHMiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBSZWFkaW5lc3MgUm93cyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgR2F0ZSBwYWlyIHwgRGVjaXNpb24gfCBTdGF0dXMgfCBSZWFzb25zIHwgQWN0aW9uIHwiLAogICAgICAgICJ8LS0tfC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHJvdyBpbiBzdW1tYXJ5WyJyZWFkaW5lc3Nfcm93cyJdOgogICAgICAgIHJlYXNvbnMgPSAiLCAiLmpvaW4ocm93WyJiYXNlbGluZV9vdmVyX3BlbmFsdHlfcmVhc29ucyJdKSBvciAibm9uZSIKICAgICAgICBhY3Rpb24gPSByb3dbInJlY29tbWVuZGVkX2FjdGlvbiJdLnJlcGxhY2UoInwiLCAiXFx8IikKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7cm93WydnYXRlX3BhaXInXX1gIHwgYHtyb3dbJ2RlY2lzaW9uJ119YCB8IGB7cm93WydyZWFkaW5lc3Nfc3RhdHVzJ119YCB8IGB7cmVhc29uc31gIHwge2FjdGlvbn0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBDYWxpYnJhdGlvbiBTd2VlcCIsCiAgICAgICAgIiIsCiAgICAgICAgInwgVGhyZXNob2xkIHwgT3Zlci1wZW5hbHR5IHwgUGFzcyBjb3VudCB8IEhpZ2ggc3VwcG9ydCB8IE1pc3NpbmcgZmluZGluZ3MgfCBIaWdoIHNldmVyaXR5IHwiLAogICAgICAgICJ8LS0tOnwtLS06fC0tLTp8LS0tOnwtLS06fC0tLTp8IiwKICAgIF0KICAgIGZvciByb3cgaW4gc3VtbWFyeVsiY2FsaWJyYXRpb25fc3dlZXAiXToKICAgICAgICBsaW5lcy5hcHBlbmQoCiAgICAgICAgICAgIGYifCB7cm93Wyd0aHJlc2hvbGQnXTouMmZ9IHwge3Jvd1snb3Zlcl9wZW5hbHR5X2NvdW50J119IHwge3Jvd1sncGFzc19jb3VudCddfSB8ICIKICAgICAgICAgICAgZiJ7cm93WydoaWdoX3N1cHBvcnRfY291bnQnXX0gfCB7cm93WydtaXNzaW5nX2ZpbmRpbmdzX2NvdW50J119IHwge3Jvd1snaGlnaF9zZXZlcml0eV9jb3VudCddfSB8IgogICAgICAgICkKCiAgICBsaW5lcyArPSBbIiIsICIjIyBDaGFydHMiLCAiIl0KICAgIGZvciBjaGFydCBpbiBzdW1tYXJ5WyJjaGFydF9wYXRocyJdOgogICAgICAgIHJlbCA9IG9zLnBhdGgucmVscGF0aChSRVBPX1JPT1QgLyBjaGFydCwgT1VUX0RJUikucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgbGluZXMgKz0gW2YiIVt7UGF0aChjaGFydCkuc3RlbX1dKHtyZWx9KSIsICIiXQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIyMgdjAuNS4wIExvY2siLAogICAgICAgICIiLAogICAgICAgICJ2MC41LjAgaXMgYSBtYWpvciBnb3Zlcm5hbmNlIGNoZWNrcG9pbnQsIG5vdCBjbGFzc2lmaWVyIGFjdGl2YXRpb24uIiwKICAgICAgICAiIiwKICAgICAgICAiYGBgdGV4dCIsCiAgICAgICAgImVuZm9yY2VtZW50X2NhbmRpZGF0ZV9lbmFibGVkOiBmYWxzZSIsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQ6IGZhbHNlIiwKICAgICAgICAicG9saWN5X2VuZm9yY2VkOiBmYWxzZSIsCiAgICAgICAgImBgYCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEJvdW5kYXJ5IiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJib3VuZGFyeSJdLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIHJlZ3Jlc3Npb24gPSByZWFkX2pzb24oUkVHUkVTU0lPTl9QQVRIKQogICAgcmV2aWV3X3Jvd3MgPSByZWdyZXNzaW9uLmdldCgicmV2aWV3X3Jvd3MiLCBbXSkKICAgIHJvd3MgPSBbcmVhZGluZXNzX3Jvdyhyb3cpIGZvciByb3cgaW4gcmV2aWV3X3Jvd3NdCiAgICBzdGF0dXNfY291bnRzID0gQ291bnRlcihyb3dbInJlYWRpbmVzc19zdGF0dXMiXSBmb3Igcm93IGluIHJvd3MpCiAgICBjb250cm9sbGVkID0gW3IgZm9yIHIgaW4gcm93cyBpZiByWyJkZWNpc2lvbiJdID09ICJBUFBST1ZFX0ZPUl9SRUdSRVNTSU9OX1JFVklFVyJdCiAgICBibG9ja2VkID0gW3IgZm9yIHIgaW4gcm93cyBpZiByWyJyZWFkaW5lc3Nfc3RhdHVzIl0gPT0gIkJMT0NLRURfQllfT1ZFUl9QRU5BTFRZIl0KCiAgICBnYXRlX2NvdW50cyA9IENvdW50ZXIoKQogICAgZm9yIHJvdyBpbiBibG9ja2VkOgogICAgICAgIGdhdGVfY291bnRzW3Jvd1siZ2F0ZV9hIl1dICs9IDEKICAgICAgICBnYXRlX2NvdW50c1tyb3dbImdhdGVfYiJdXSArPSAxCgogICAgZWxpZ2libGUgPSBzdGF0dXNfY291bnRzLmdldCgiRUxJR0lCTEVfRk9SX0NBTkRJREFURV9ERVNJR04iLCAwKQogICAgZmluYWwgPSAoCiAgICAgICAgImRvX25vdF9kZXNpZ25fZW5mb3JjZW1lbnRfY2FuZGlkYXRlX19hbGxfY29udHJvbGxlZF9kb3duZ3JhZGVzX2Jsb2NrZWQiCiAgICAgICAgaWYgZWxpZ2libGUgPT0gMCBhbmQgbGVuKGNvbnRyb2xsZWQpID4gMAogICAgICAgIGVsc2UgImRpc2FibGVkX2VuZm9yY2VtZW50X2NhbmRpZGF0ZV9kZXNpZ25fYWxsb3dlZF9hZnRlcl9tYW51YWxfcmV2aWV3IgogICAgICAgIGlmIGVsaWdpYmxlID4gMAogICAgICAgIGVsc2UgIm5vX2VuZm9yY2VtZW50X2NhbmRpZGF0ZV9wYXRoIgogICAgKQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1lbmZvcmNlbWVudC1yZWFkaW5lc3MtZ2F0ZS12MC41LjAiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXQiOiAicmVwb3J0cy9yZWdyZXNzaW9uX3Jldmlldy9sYXRlc3RfcmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3Lmpzb24iLAogICAgICAgICJpbnB1dF9yZXZpZXdfcm93cyI6IGxlbihyZXZpZXdfcm93cyksCiAgICAgICAgImNvbnRyb2xsZWRfZG93bmdyYWRlX2NhbmRpZGF0ZV9jb3VudCI6IGxlbihjb250cm9sbGVkKSwKICAgICAgICAiYmxvY2tlZF9ieV9vdmVyX3BlbmFsdHlfY291bnQiOiBsZW4oYmxvY2tlZCksCiAgICAgICAgImh1bWFuX3Jldmlld19vbmx5X2NvdW50Ijogc3RhdHVzX2NvdW50cy5nZXQoIkhVTUFOX1JFVklFV19PTkxZIiwgMCksCiAgICAgICAgImVsaWdpYmxlX2NhbmRpZGF0ZV9kZXNpZ25fY291bnQiOiBlbGlnaWJsZSwKICAgICAgICAicmVhZGluZXNzX3N0YXR1c19jb3VudHMiOiBkaWN0KHN0YXR1c19jb3VudHMpLAogICAgICAgICJibG9ja2VkX2dhdGVfY291bnRzIjogZGljdChnYXRlX2NvdW50cyksCiAgICAgICAgImNhbGlicmF0aW9uX3N3ZWVwIjogY2FsaWJyYXRpb25fc3dlZXAocmV2aWV3X3Jvd3MpLAogICAgICAgICJyZWFkaW5lc3Nfcm93cyI6IHJvd3MsCiAgICAgICAgImVuZm9yY2VtZW50X2NhbmRpZGF0ZV9lbmFibGVkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogZmluYWwsCiAgICAgICAgImJvdW5kYXJ5IjogIkVuZm9yY2VtZW50IHJlYWRpbmVzcyBpcyBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYW5hbHlzaXMgb25seS4gSXQgZG9lcyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvZXMgbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC41LjEgc2hvdWxkIHJlcGFpciB0aGUgTmV4dXMgZmVlZGJhY2sgdGFyZ2V0IHNvIGNvbXBsZXRlZCB2MC40Lnggc3VyZmFjZXMgYXJlIHJlY29nbml6ZWQgYW5kIHN0YWxlIHJlY29tbWVuZGF0aW9ucyBhcmUgcmV0aXJlZC4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGdlbmVyYXRlX2NoYXJ0cyhzdW1tYXJ5KQoKICAgIE9VVF9ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgd3JpdGVfanNvbihPVVRfRElSIC8gImVuZm9yY2VtZW50X3JlYWRpbmVzc19nYXRlX3YwXzVfMC5qc29uIiwgc3VtbWFyeSkKICAgIHdyaXRlX2pzb24oT1VUX0RJUiAvICJsYXRlc3RfZW5mb3JjZW1lbnRfcmVhZGluZXNzX2dhdGUuanNvbiIsIHN1bW1hcnkpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAiZW5mb3JjZW1lbnRfcmVhZGluZXNzX2dhdGVfdjBfNV8wLm1kIiwgcmVuZGVyX21kKHN1bW1hcnkpKQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gImxhdGVzdF9lbmZvcmNlbWVudF9yZWFkaW5lc3NfZ2F0ZS5tZCIsIHJlbmRlcl9tZChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImlucHV0X3Jldmlld19yb3dzIjogc3VtbWFyeVsiaW5wdXRfcmV2aWV3X3Jvd3MiXSwKICAgICAgICAiY29udHJvbGxlZF9kb3duZ3JhZGVfY2FuZGlkYXRlX2NvdW50Ijogc3VtbWFyeVsiY29udHJvbGxlZF9kb3duZ3JhZGVfY2FuZGlkYXRlX2NvdW50Il0sCiAgICAgICAgImJsb2NrZWRfYnlfb3Zlcl9wZW5hbHR5X2NvdW50Ijogc3VtbWFyeVsiYmxvY2tlZF9ieV9vdmVyX3BlbmFsdHlfY291bnQiXSwKICAgICAgICAiaHVtYW5fcmV2aWV3X29ubHlfY291bnQiOiBzdW1tYXJ5WyJodW1hbl9yZXZpZXdfb25seV9jb3VudCJdLAogICAgICAgICJlbGlnaWJsZV9jYW5kaWRhdGVfZGVzaWduX2NvdW50Ijogc3VtbWFyeVsiZWxpZ2libGVfY2FuZGlkYXRlX2Rlc2lnbl9jb3VudCJdLAogICAgICAgICJlbmZvcmNlbWVudF9jYW5kaWRhdGVfZW5hYmxlZCI6IHN1bW1hcnlbImVuZm9yY2VtZW50X2NhbmRpZGF0ZV9lbmFibGVkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IHN1bW1hcnlbImZpbmFsX3JlY29tbWVuZGF0aW9uIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9lbmZvcmNlbWVudF9yZWFkaW5lc3MvbGF0ZXN0X2VuZm9yY2VtZW50X3JlYWRpbmVzc19nYXRlLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
write(ROOT / "scripts" / "benchmarks" / "run_enforcement_readiness_gate.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "enforcement_readiness" / "README.md", """# Enforcement Readiness Reports

Current layer: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**

## Purpose

This folder stores major-checkpoint readiness reports for classifier-policy enforcement candidates.

## Primary command

```powershell
python scripts/benchmarks/run_enforcement_readiness_gate.py
```

## README Update Rule

Update this mini README whenever enforcement-readiness schemas, report paths, or readiness rules change.

Boundary: enforcement readiness reports are local classifier-governance artifacts only.
""")

write(ROOT / "visuals" / "enforcement_readiness" / "README.md", """# Enforcement Readiness Visuals

Current layer: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**

## Purpose

This folder stores charts summarizing enforcement-readiness status.

## README Update Rule

Update this mini README whenever readiness chart names or chart meanings change.

Boundary: readiness visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "enforcement_readiness" / "v0_5_0" / "README.md", """# v0.5.0 Enforcement Readiness Charts

## Expected Charts

- `enforcement_readiness_status_counts.png`
- `enforcement_readiness_calibration_sweep.png`
- `blocked_candidate_gate_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local enforcement-readiness diagnostics only.
""")

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

# Accept either planned v0.4.10 or existing v0.4.9 as previous state.
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.(?:9|10)[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.(?:8|9)[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.(?:9|10) \|", "| Current checkpoint | TAU-SCALING-SA v0.5.0 |", r)

if "| Enforcement readiness gate | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |" not in r:
    marker = "| Regression review charts | `visuals/regression_review/v0_4_9/` |\n"
    insert = marker + "| Enforcement readiness gate | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n| Enforcement readiness charts | `visuals/enforcement_readiness/v0_5_0/` |\n"
    if marker in r:
        r = r.replace(marker, insert)
    else:
        r = r.replace("| Policy decision charts | `visuals/policy_decision/v0_4_8/` |\n",
                      "| Policy decision charts | `visuals/policy_decision/v0_4_8/` |\n| Enforcement readiness gate | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n| Enforcement readiness charts | `visuals/enforcement_readiness/v0_5_0/` |\n")

if "python scripts/benchmarks/run_enforcement_readiness_gate.py" not in r:
    r = r.replace("python scripts/benchmarks/run_regression_over_penalty_review.py\npython scripts/feedback/run_nexus_feedback.py",
                  "python scripts/benchmarks/run_regression_over_penalty_review.py\npython scripts/benchmarks/run_enforcement_readiness_gate.py\npython scripts/feedback/run_nexus_feedback.py")
    r = r.replace("python scripts/benchmarks/run_over_penalty_calibration.py\npython scripts/feedback/run_nexus_feedback.py",
                  "python scripts/benchmarks/run_over_penalty_calibration.py\npython scripts/benchmarks/run_enforcement_readiness_gate.py\npython scripts/feedback/run_nexus_feedback.py")

if "    enforcement_readiness/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    enforcement_readiness/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    enforcement_readiness/\n")

section = """## Enforcement Readiness Gate v0.5.0

v0.5.0 is the major governance checkpoint after v0.4.9 blocked all controlled downgrade candidates.

Primary command:

```powershell
python scripts/benchmarks/run_enforcement_readiness_gate.py
```

Primary outputs:

```text
reports/enforcement_readiness/latest_enforcement_readiness_gate.json
reports/enforcement_readiness/latest_enforcement_readiness_gate.md
visuals/enforcement_readiness/v0_5_0/
```

This layer answers:

```text
which policy candidates remain blocked
which cases stay human-review only
whether disabled enforcement-candidate design is allowed
whether any classifier mutation is permitted
```

Current lock:

```text
enforcement_candidate_enabled: false
mutation_allowed: false
policy_enforced: false
```

Boundary: enforcement readiness is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Enforcement Readiness Gate v0.5.0" not in r:
    # Put before v0.4.9 or before policy decision if older.
    if "## Regression and Over-Penalty Review v0.4.9" in r:
        r = r.replace("## Regression and Over-Penalty Review v0.4.9", section + "## Regression and Over-Penalty Review v0.4.9", 1)
    else:
        r = r.replace("## Policy Decision Record v0.4.8", section + "## Policy Decision Record v0.4.8", 1)

lesson = "| L-032 | v0.4.9 showed that all six controlled downgrade candidates triggered over-penalty review. | A review gate that blocks every candidate may indicate true policy harshness or heuristic over-sensitivity. | When regression review blocks every candidate, do not proceed to enforcement design; first promote the blocked state into a major enforcement-readiness gate with all mutation disabled. |"
if "L-032" not in r:
    r = r.replace("| L-031 | v0.4.8 approved six drift cases for regression review, but approval-for-review is not approval-for-enforcement. | Decision records classify readiness for review, not readiness for mutation. | Controlled downgrade candidates must pass regression and over-penalty review before any classifier enforcement candidate is allowed. |\n",
                  "| L-031 | v0.4.8 approved six drift cases for regression review, but approval-for-review is not approval-for-enforcement. | Decision records classify readiness for review, not readiness for mutation. | Controlled downgrade candidates must pass regression and over-penalty review before any classifier enforcement candidate is allowed. |\n" + lesson + "\n")
else:
    r = re.sub(r"\| L-032 \|.*?\|\n", lesson + "\n", r)

if "| v0.5.0 | Enforcement readiness gate for blocked policy candidates with classifier mutation disabled. |" not in r:
    if "| v0.4.10 |" in r:
        r = r.replace("| v0.4.10 | Over-penalty diagnosis and threshold calibration after regression review blocked all candidates. |\n",
                      "| v0.4.10 | Over-penalty diagnosis and threshold calibration after regression review blocked all candidates. |\n| v0.5.0 | Enforcement readiness gate for blocked policy candidates with classifier mutation disabled. |\n")
    else:
        r = r.replace("| v0.4.9 | Regression and over-penalty review for controlled downgrade candidates. |\n",
                      "| v0.4.9 | Regression and over-penalty review for controlled downgrade candidates. |\n| v0.5.0 | Enforcement readiness gate for blocked policy candidates with classifier mutation disabled. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**

Recommended goals:

- Update Nexus feedback so completed v0.4.6-v0.5.0 targets are recognized as completed.
- Retire stale NF-001 dry-run recommendation.
- Promote the current blocker as the next active signal.
- Preserve non-claim locks: Nexus target refresh is repository self-observation only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.(?:9|10)[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**", a)
if "Enforcement readiness patch" not in a:
    # Robust insert after regression or decision.
    if "| Regression review patch |" in a:
        a = a.replace("| Regression review patch | `reports/regression_review/`, `visuals/regression_review/`, decision record | regression review + over-penalty report; mutation_allowed must remain false |\n",
                      "| Regression review patch | `reports/regression_review/`, `visuals/regression_review/`, decision record | regression review + over-penalty report; mutation_allowed must remain false |\n| Enforcement readiness patch | `reports/enforcement_readiness/`, `visuals/enforcement_readiness/`, regression review | readiness gate + release validator; enforcement_candidate_enabled must remain false |\n")
    else:
        a += "\n| Enforcement readiness patch | `reports/enforcement_readiness/`, `visuals/enforcement_readiness/`, regression review | readiness gate + release validator; enforcement_candidate_enabled must remain false |\n"
write(agents, a)

# route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.5.0"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_5_routes", {})
route["v0_5_routes"]["enforcement_readiness_gate"] = {
    "read_first": ["reports/regression_review/latest_regression_over_penalty_review.json"],
    "validate": ["python scripts/benchmarks/run_enforcement_readiness_gate.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/enforcement_readiness/latest_enforcement_readiness_gate.md", "visuals/enforcement_readiness/v0_5_0/"],
    "mutation_lock": "Does not change classifier behavior; enforcement_candidate_enabled, mutation_allowed, and policy_enforced must remain false."
}
write_json(route_path, route)

# task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.(?:9|10)[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate**", m)
if "| Enforcement readiness patch |" not in m:
    if "| Regression review patch |" in m:
        m = m.replace("| Regression review patch | outer | validation | governance | decision record + dry-run report | regression report + charts + release validator | `reports/regression_review/latest_regression_over_penalty_review.md` |\n",
                      "| Regression review patch | outer | validation | governance | decision record + dry-run report | regression report + charts + release validator | `reports/regression_review/latest_regression_over_penalty_review.md` |\n| Enforcement readiness patch | outer | validation | governance | regression review + readiness gate | readiness report + charts + release validator | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n")
    else:
        m += "\n| Enforcement readiness patch | outer | validation | governance | regression review + readiness gate | readiness report + charts + release validator | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` |\n"
write(matrix, m)

# atlas
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.5.0 | Enforcement readiness gate |" not in t:
    if "| v0.4.9 |" in t:
        t = t.replace("| v0.4.9 | Regression and over-penalty review | `python scripts/benchmarks/run_regression_over_penalty_review.py` | Reviews controlled downgrade candidates before enforcement-candidate design | `reports/regression_review/latest_regression_over_penalty_review.md` | `visuals/regression_review/v0_4_9/` |\n",
                      "| v0.4.9 | Regression and over-penalty review | `python scripts/benchmarks/run_regression_over_penalty_review.py` | Reviews controlled downgrade candidates before enforcement-candidate design | `reports/regression_review/latest_regression_over_penalty_review.md` | `visuals/regression_review/v0_4_9/` |\n| v0.5.0 | Enforcement readiness gate | `python scripts/benchmarks/run_enforcement_readiness_gate.py` | Major checkpoint that blocks enforcement when over-penalty review fails | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` | `visuals/enforcement_readiness/v0_5_0/` |\n")
    else:
        t += "\n| v0.5.0 | Enforcement readiness gate | `python scripts/benchmarks/run_enforcement_readiness_gate.py` | Major checkpoint that blocks enforcement when over-penalty review fails | `reports/enforcement_readiness/latest_enforcement_readiness_gate.md` | `visuals/enforcement_readiness/v0_5_0/` |\n"
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_5_0_enforcement_readiness_gate.md", f"""# TAU-SCALING-SA v0.5.0 - Enforcement Readiness Gate

Generated: {GENERATED_AT}

## Purpose

Promote the blocked v0.4.9 state into a clear v0.5.0 major checkpoint to prevent version confusion.

## Adds

- `scripts/benchmarks/run_enforcement_readiness_gate.py`
- `reports/enforcement_readiness/`
- `visuals/enforcement_readiness/v0_5_0/`

## Lock

```text
enforcement_candidate_enabled: false
mutation_allowed: false
policy_enforced: false
```

## Boundary

Enforcement readiness is local classifier-governance analysis only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.5.0 enforcement readiness gate patch written")
