
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
        dest = ROOT / "reports" / "policy_impact" / "v0_4_7" / "backups" / f"{path.name}_before_v0_4_7_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KRFJZX1JVTiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3lfZHJ5X3J1biIgLyAibGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4uanNvbiIKT1VUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3lfaW1wYWN0IgpDQVJEX0RJUiA9IE9VVF9ESVIgLyAiY2FyZHMiIC8gInYwXzRfNyIKVklTX0RJUiA9IFJFUE9fUk9PVCAvICJ2aXN1YWxzIiAvICJwb2xpY3lfaW1wYWN0IiAvICJ2MF80XzciCgpkZWYgcmVhZF9qc29uKHBhdGg6IFBhdGgpIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd3JpdGVfanNvbihwYXRoOiBQYXRoLCBwYXlsb2FkOiBBbnkpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhwYXlsb2FkLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3cml0ZV90ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cikgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIGNsYXNzaWZ5X2ltcGFjdChyb3c6IGRpY3Rbc3RyLCBBbnldKSAtPiBzdHI6CiAgICBzaW0gPSByb3cuZ2V0KCJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIikKICAgIGlmIHNpbSA9PSAiSFVNQU5fUkVWSUVXIjoKICAgICAgICByZXR1cm4gIm1hbnVhbF9yZXZpZXdfcmVxdWlyZWQiCiAgICBpZiBzaW0gPT0gIlRTRUstRCI6CiAgICAgICAgcmV0dXJuICJjb250cm9sbGVkX3BvbGljeV9kb3duZ3JhZGUiCiAgICBpZiBzaW0gPT0gIlRTRUstRSI6CiAgICAgICAgcmV0dXJuICJoYXJkX3JlamVjdF9jYW5kaWRhdGUiCiAgICByZXR1cm4gIm5vX3BvbGljeV9kcmlmdCIKCmRlZiByaXNrX2xhYmVsKHJvdzogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGFjdGlvbiA9IHJvdy5nZXQoInNpbXVsYXRpb25fYWN0aW9uIikKICAgIGlmIGFjdGlvbiA9PSAiaHVtYW5fcmV2aWV3X3JlcXVpcmVkIjoKICAgICAgICByZXR1cm4gInJldmlld19yaXNrIgogICAgaWYgYWN0aW9uID09ICJjYW5kaWRhdGVfZG93bmdyYWRlIjoKICAgICAgICByZXR1cm4gImRvd25ncmFkZV9yaXNrIgogICAgaWYgYWN0aW9uID09ICJjYW5kaWRhdGVfaGFyZF9yZWplY3QiOgogICAgICAgIHJldHVybiAiaGFyZF9yZWplY3RfcmlzayIKICAgIHJldHVybiAibG93IgoKZGVmIGNhcmRfZm9yKHJvdzogZGljdFtzdHIsIEFueV0sIGluZGV4OiBpbnQpIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgY3VycmVudCA9IHJvdy5nZXQoImN1cnJlbnRfY2xhc3NpZmljYXRpb24iKQogICAgc2ltdWxhdGVkID0gcm93LmdldCgic2ltdWxhdGVkX3BvbGljeV9jbGFzc2lmaWNhdGlvbiIpCiAgICBpbXBhY3RfY2xhc3MgPSBjbGFzc2lmeV9pbXBhY3Qocm93KQogICAgcmlzayA9IHJpc2tfbGFiZWwocm93KQogICAgZ2F0ZV9wYWlyID0gZiJ7cm93LmdldCgnZ2F0ZV9hJyl9K3tyb3cuZ2V0KCdnYXRlX2InKX0iCiAgICBleHBsYW5hdGlvbiA9ICgKICAgICAgICBmIlBhaXIge2dhdGVfcGFpcn0gcmVtYWlucyB7Y3VycmVudH07IG5vIHNpbXVsYXRlZCBwb2xpY3kgZHJpZnQuIgogICAgICAgIGlmIG5vdCByb3cuZ2V0KCJkcmlmdGVkIikKICAgICAgICBlbHNlIGYiUGFpciB7Z2F0ZV9wYWlyfSB3b3VsZCBtb3ZlIGZyb20ge2N1cnJlbnR9IHRvIHtzaW11bGF0ZWR9IHVuZGVyIGRyeS1ydW4gcG9saWN5LiIKICAgICkKICAgIGlmIHNpbXVsYXRlZCA9PSAiSFVNQU5fUkVWSUVXIjoKICAgICAgICBkZWNpc2lvbiA9ICJEbyBub3QgZW5mb3JjZSBhdXRvbWF0aWNhbGx5OyByb3V0ZSB0byBodW1hbiBwb2xpY3kgcmV2aWV3LiIKICAgIGVsaWYgc2ltdWxhdGVkID09ICJUU0VLLUQiOgogICAgICAgIGRlY2lzaW9uID0gIkNhbmRpZGF0ZSBjb250cm9sbGVkIGRvd25ncmFkZTsgZXhwbGFpbiBhbmQgcmVncmVzc2lvbi10ZXN0IGJlZm9yZSBlbmZvcmNlbWVudC4iCiAgICBlbGlmIHNpbXVsYXRlZCA9PSAiVFNFSy1FIjoKICAgICAgICBkZWNpc2lvbiA9ICJIYXJkIHJlamVjdCBjYW5kaWRhdGU7IGJsb2NrIGVuZm9yY2VtZW50IHVudGlsIGV4cGxpY2l0IHByb3ZlbmFuY2UgYW5kIHJlZ3Jlc3Npb24gcmV2aWV3LiIKICAgIGVsc2U6CiAgICAgICAgZGVjaXNpb24gPSAiUmV0YWluIGN1cnJlbnQgYmVoYXZpb3IuIgoKICAgIHJldHVybiB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1wb2xpY3ktaW1wYWN0LWNhcmQtdjAuNC43IiwKICAgICAgICAiY2FyZF9pZCI6IGYicG9saWN5LWltcGFjdC12MC00LTcte2luZGV4OjAzZH0iLAogICAgICAgICJnYXRlX2EiOiByb3cuZ2V0KCJnYXRlX2EiKSwKICAgICAgICAiZ2F0ZV9iIjogcm93LmdldCgiZ2F0ZV9iIiksCiAgICAgICAgImdhdGVfcGFpciI6IGdhdGVfcGFpciwKICAgICAgICAiY3VycmVudF9jbGFzc2lmaWNhdGlvbiI6IGN1cnJlbnQsCiAgICAgICAgInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iOiBzaW11bGF0ZWQsCiAgICAgICAgInBvbGljeV9jbGFzcyI6IHJvdy5nZXQoInBvbGljeV9jbGFzcyIpLAogICAgICAgICJzaW11bGF0aW9uX2FjdGlvbiI6IHJvdy5nZXQoInNpbXVsYXRpb25fYWN0aW9uIiksCiAgICAgICAgImltcGFjdF9jbGFzcyI6IGltcGFjdF9jbGFzcywKICAgICAgICAicmlza19sYWJlbCI6IHJpc2ssCiAgICAgICAgImRyaWZ0ZWQiOiByb3cuZ2V0KCJkcmlmdGVkIiksCiAgICAgICAgImRyaWZ0X3NldmVyaXR5Ijogcm93LmdldCgiZHJpZnRfc2V2ZXJpdHkiKSwKICAgICAgICAiZmluZGluZ19jb2RlcyI6IHJvdy5nZXQoImZpbmRpbmdfY29kZXMiLCBbXSksCiAgICAgICAgImZpbmRpbmdzX2NvdW50Ijogcm93LmdldCgiZmluZGluZ3NfY291bnQiLCAwKSwKICAgICAgICAiY3VycmVudF9BX1RTRUsiOiByb3cuZ2V0KCJjdXJyZW50X0FfVFNFSyIpLAogICAgICAgICJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSI6IHJvdy5nZXQoImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIiksCiAgICAgICAgInJlYXNvbiI6IHJvdy5nZXQoInJlYXNvbiIpLAogICAgICAgICJyZWNvbW1lbmRlZF9hY3Rpb25fZnJvbV9wb2xpY3kiOiByb3cuZ2V0KCJyZWNvbW1lbmRlZF9hY3Rpb24iKSwKICAgICAgICAiaW1wYWN0X2V4cGxhbmF0aW9uIjogZXhwbGFuYXRpb24sCiAgICAgICAgImRlY2lzaW9uX2hpbnQiOiBkZWNpc2lvbiwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgIm5vbl9jbGFpbV9sb2NrIjogIlBvbGljeSBpbXBhY3QgY2FyZHMgZXhwbGFpbiBzaW11bGF0ZWQgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGVmZmVjdHMgb25seTsgdGhleSBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiBvciBwcm9kdWN0IGNsYWltcy4iLAogICAgfQoKZGVmIGdlbmVyYXRlX2NoYXJ0cyhzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gbGlzdFtzdHJdOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0IiwgZiJtYXRwbG90bGliIHVuYXZhaWxhYmxlOiB7ZXhjfVxuIikKICAgICAgICByZXR1cm4gcGF0aHMKCiAgICBWSVNfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShwYXRoOiBQYXRoKSAtPiBOb25lOgogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHBhdGgsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQoc3RyKHBhdGgucmVsYXRpdmVfdG8oUkVQT19ST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQoKICAgIGltcGFjdF9jb3VudHMgPSBzdW1tYXJ5WyJpbXBhY3RfY2xhc3NfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoaW1wYWN0X2NvdW50cy5rZXlzKCkpLCBsaXN0KGltcGFjdF9jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNhcmQgY291bnQiKQogICAgcGx0LnRpdGxlKCJQb2xpY3kgSW1wYWN0IENsYXNzIENvdW50cyIpCiAgICBzYXZlKFZJU19ESVIgLyAicG9saWN5X2ltcGFjdF9jbGFzc19jb3VudHMucG5nIikKCiAgICByaXNrX2NvdW50cyA9IHN1bW1hcnlbInJpc2tfbGFiZWxfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3Qocmlza19jb3VudHMua2V5cygpKSwgbGlzdChyaXNrX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ2FyZCBjb3VudCIpCiAgICBwbHQudGl0bGUoIlBvbGljeSBJbXBhY3QgUmlzayBMYWJlbHMiKQogICAgc2F2ZShWSVNfRElSIC8gInBvbGljeV9pbXBhY3Rfcmlza19sYWJlbHMucG5nIikKCiAgICBnYXRlX2NvdW50cyA9IHN1bW1hcnlbImRyaWZ0X2dhdGVfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZV9jb3VudHMua2V5cygpKSwgbGlzdChnYXRlX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTQ1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiRHJpZnQtY2FyZCBpbnZvbHZlbWVudCIpCiAgICBwbHQudGl0bGUoIlBvbGljeSBJbXBhY3QgRHJpZnQgYnkgR2F0ZSIpCiAgICBzYXZlKFZJU19ESVIgLyAicG9saWN5X2ltcGFjdF9kcmlmdF9ieV9nYXRlLnBuZyIpCgogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVuZGVyX2NhcmRfbWQoY2FyZDogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIHJldHVybiAiXG4iLmpvaW4oWwogICAgICAgIGYiIyB7Y2FyZFsnY2FyZF9pZCddfSIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIEdhdGUgcGFpcjogYHtjYXJkWydnYXRlX3BhaXInXX1gIiwKICAgICAgICBmIi0gQ3VycmVudCBjbGFzczogYHtjYXJkWydjdXJyZW50X2NsYXNzaWZpY2F0aW9uJ119YCIsCiAgICAgICAgZiItIFNpbXVsYXRlZCBjbGFzczogYHtjYXJkWydzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uJ119YCIsCiAgICAgICAgZiItIEltcGFjdCBjbGFzczogYHtjYXJkWydpbXBhY3RfY2xhc3MnXX1gIiwKICAgICAgICBmIi0gUmlzayBsYWJlbDogYHtjYXJkWydyaXNrX2xhYmVsJ119YCIsCiAgICAgICAgZiItIERyaWZ0ZWQ6IGB7Y2FyZFsnZHJpZnRlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBFeHBsYW5hdGlvbiIsCiAgICAgICAgIiIsCiAgICAgICAgY2FyZFsiaW1wYWN0X2V4cGxhbmF0aW9uIl0sCiAgICAgICAgIiIsCiAgICAgICAgIiMjIERlY2lzaW9uIEhpbnQiLAogICAgICAgICIiLAogICAgICAgIGNhcmRbImRlY2lzaW9uX2hpbnQiXSwKICAgICAgICAiIiwKICAgICAgICAiIyMgQm91bmRhcnkiLAogICAgICAgICIiLAogICAgICAgIGNhcmRbIm5vbl9jbGFpbV9sb2NrIl0sCiAgICAgICAgIiIsCiAgICBdKQoKZGVmIHJlbmRlcl9yZXBvcnQoc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjQuNyBQb2xpY3kgSW1wYWN0IEV4cGxhbmF0aW9uIENhcmRzIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSW5wdXQgZHJ5LXJ1biByb3dzOiBge3N1bW1hcnlbJ2lucHV0X3Jvd3MnXX1gIiwKICAgICAgICBmIi0gRHJpZnQgY2FyZHM6IGB7c3VtbWFyeVsnZHJpZnRfY2FyZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBDb250cm9sbGVkIGRvd25ncmFkZSBjYXJkczogYHtzdW1tYXJ5Wydjb250cm9sbGVkX2Rvd25ncmFkZV9jb3VudCddfWAiLAogICAgICAgIGYiLSBNYW51YWwgcmV2aWV3IGNhcmRzOiBge3N1bW1hcnlbJ21hbnVhbF9yZXZpZXdfY291bnQnXX1gIiwKICAgICAgICBmIi0gSGFyZCByZWplY3QgY2FuZGlkYXRlIGNhcmRzOiBge3N1bW1hcnlbJ2hhcmRfcmVqZWN0X2NhbmRpZGF0ZV9jb3VudCddfWAiLAogICAgICAgIGYiLSBQb2xpY3kgZW5mb3JjZWQ6IGB7c3VtbWFyeVsncG9saWN5X2VuZm9yY2VkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEltcGFjdCBDbGFzc2VzIiwKICAgICAgICAiIiwKICAgICAgICAifCBJbXBhY3QgY2xhc3MgfCBDb3VudCB8IiwKICAgICAgICAifC0tLXwtLS06fCIsCiAgICBdCiAgICBmb3IgaywgdiBpbiBzdW1tYXJ5WyJpbXBhY3RfY2xhc3NfY291bnRzIl0uaXRlbXMoKToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7a31gIHwge3Z9IHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgUmlzayBMYWJlbHMiLAogICAgICAgICIiLAogICAgICAgICJ8IFJpc2sgbGFiZWwgfCBDb3VudCB8IiwKICAgICAgICAifC0tLXwtLS06fCIsCiAgICBdCiAgICBmb3IgaywgdiBpbiBzdW1tYXJ5WyJyaXNrX2xhYmVsX2NvdW50cyJdLml0ZW1zKCk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2t9YCB8IHt2fSB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENhcmRzIiwKICAgICAgICAiIiwKICAgICAgICAifCBDYXJkIHwgR2F0ZSBwYWlyIHwgQ3VycmVudCB8IFNpbXVsYXRlZCB8IEltcGFjdCB8IERlY2lzaW9uIGhpbnQgfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIGMgaW4gc3VtbWFyeVsiY2FyZHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoQ0FSRF9ESVIgLyBmIntjWydjYXJkX2lkJ119Lm1kIiwgT1VUX0RJUikucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgaGludCA9IGNbImRlY2lzaW9uX2hpbnQiXS5yZXBsYWNlKCJ8IiwgIlxcfCIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBbYHtjWydjYXJkX2lkJ119YF0oe3JlbH0pIHwgYHtjWydnYXRlX3BhaXInXX1gIHwgYHtjWydjdXJyZW50X2NsYXNzaWZpY2F0aW9uJ119YCB8IGB7Y1snc2ltdWxhdGVkX3BvbGljeV9jbGFzc2lmaWNhdGlvbiddfWAgfCBge2NbJ2ltcGFjdF9jbGFzcyddfWAgfCB7aGludH0gfCIpCgogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgY2hhcnQgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUkVQT19ST09UIC8gY2hhcnQsIE9VVF9ESVIpLnJlcGxhY2UoIlxcIiwgIi8iKQogICAgICAgIGxpbmVzICs9IFtmIiFbe1BhdGgoY2hhcnQpLnN0ZW19XSh7cmVsfSkiLCAiIl0KCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIGRyeSA9IHJlYWRfanNvbihEUllfUlVOKQogICAgcm93cyA9IGRyeS5nZXQoImRyeV9ydW5fcm93cyIsIFtdKQogICAgZHJpZnRfcm93cyA9IFtyIGZvciByIGluIHJvd3MgaWYgci5nZXQoImRyaWZ0ZWQiKV0KICAgIGNhcmRzID0gW2NhcmRfZm9yKHJvdywgaSArIDEpIGZvciBpLCByb3cgaW4gZW51bWVyYXRlKGRyaWZ0X3Jvd3MpXQoKICAgIENBUkRfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIGZvciBjYXJkIGluIGNhcmRzOgogICAgICAgIHdyaXRlX2pzb24oQ0FSRF9ESVIgLyBmIntjYXJkWydjYXJkX2lkJ119Lmpzb24iLCBjYXJkKQogICAgICAgIHdyaXRlX3RleHQoQ0FSRF9ESVIgLyBmIntjYXJkWydjYXJkX2lkJ119Lm1kIiwgcmVuZGVyX2NhcmRfbWQoY2FyZCkpCgogICAgaW1wYWN0X2NvdW50cyA9IENvdW50ZXIoY1siaW1wYWN0X2NsYXNzIl0gZm9yIGMgaW4gY2FyZHMpCiAgICByaXNrX2NvdW50cyA9IENvdW50ZXIoY1sicmlza19sYWJlbCJdIGZvciBjIGluIGNhcmRzKQogICAgZ2F0ZV9jb3VudHMgPSBDb3VudGVyKCkKICAgIGZvciBjIGluIGNhcmRzOgogICAgICAgIGdhdGVfY291bnRzW2NbImdhdGVfYSJdXSArPSAxCiAgICAgICAgZ2F0ZV9jb3VudHNbY1siZ2F0ZV9iIl1dICs9IDEKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctcG9saWN5LWltcGFjdC1leHBsYW5hdGlvbi1jYXJkcy12MC40LjciLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXQiOiAicmVwb3J0cy9wb2xpY3lfZHJ5X3J1bi9sYXRlc3RfcGFpcl9wb2xpY3lfZHJ5X3J1bi5qc29uIiwKICAgICAgICAiaW5wdXRfcm93cyI6IGxlbihyb3dzKSwKICAgICAgICAiZHJpZnRfY2FyZF9jb3VudCI6IGxlbihjYXJkcyksCiAgICAgICAgImNvbnRyb2xsZWRfZG93bmdyYWRlX2NvdW50IjogaW1wYWN0X2NvdW50cy5nZXQoImNvbnRyb2xsZWRfcG9saWN5X2Rvd25ncmFkZSIsIDApLAogICAgICAgICJtYW51YWxfcmV2aWV3X2NvdW50IjogaW1wYWN0X2NvdW50cy5nZXQoIm1hbnVhbF9yZXZpZXdfcmVxdWlyZWQiLCAwKSwKICAgICAgICAiaGFyZF9yZWplY3RfY2FuZGlkYXRlX2NvdW50IjogaW1wYWN0X2NvdW50cy5nZXQoImhhcmRfcmVqZWN0X2NhbmRpZGF0ZSIsIDApLAogICAgICAgICJpbXBhY3RfY2xhc3NfY291bnRzIjogZGljdChpbXBhY3RfY291bnRzKSwKICAgICAgICAicmlza19sYWJlbF9jb3VudHMiOiBkaWN0KHJpc2tfY291bnRzKSwKICAgICAgICAiZHJpZnRfZ2F0ZV9jb3VudHMiOiBkaWN0KGdhdGVfY291bnRzKSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhcmRzIjogY2FyZHMsCiAgICAgICAgImJvdW5kYXJ5IjogIlBvbGljeSBpbXBhY3QgZXhwbGFuYXRpb24gY2FyZHMgZXhwbGFpbiBkcnktcnVuIGNsYXNzaWZpZXItcG9saWN5IGVmZmVjdHMgb25seS4gVGhleSBkbyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNC44IHNob3VsZCBjcmVhdGUgYSBwb2xpY3kgZGVjaXNpb24gcmVjb3JkIGJlZm9yZSBhbnkgZW5mb3JjZW1lbnQgY2FuZGlkYXRlLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnkpCgogICAgd3JpdGVfanNvbihPVVRfRElSIC8gInBvbGljeV9pbXBhY3RfY2FyZHNfdjBfNF83Lmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfanNvbihPVVRfRElSIC8gImxhdGVzdF9wb2xpY3lfaW1wYWN0X2NhcmRzLmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gInBvbGljeV9pbXBhY3RfY2FyZHNfdjBfNF83Lm1kIiwgcmVuZGVyX3JlcG9ydChzdW1tYXJ5KSkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJsYXRlc3RfcG9saWN5X2ltcGFjdF9jYXJkcy5tZCIsIHJlbmRlcl9yZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJpbnB1dF9yb3dzIjogc3VtbWFyeVsiaW5wdXRfcm93cyJdLAogICAgICAgICJkcmlmdF9jYXJkX2NvdW50Ijogc3VtbWFyeVsiZHJpZnRfY2FyZF9jb3VudCJdLAogICAgICAgICJjb250cm9sbGVkX2Rvd25ncmFkZV9jb3VudCI6IHN1bW1hcnlbImNvbnRyb2xsZWRfZG93bmdyYWRlX2NvdW50Il0sCiAgICAgICAgIm1hbnVhbF9yZXZpZXdfY291bnQiOiBzdW1tYXJ5WyJtYW51YWxfcmV2aWV3X2NvdW50Il0sCiAgICAgICAgImhhcmRfcmVqZWN0X2NhbmRpZGF0ZV9jb3VudCI6IHN1bW1hcnlbImhhcmRfcmVqZWN0X2NhbmRpZGF0ZV9jb3VudCJdLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBzdW1tYXJ5WyJwb2xpY3lfZW5mb3JjZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3BvbGljeV9pbXBhY3QvbGF0ZXN0X3BvbGljeV9pbXBhY3RfY2FyZHMubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK"
write(ROOT / "scripts" / "benchmarks" / "generate_policy_impact_cards.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "policy_impact" / "README.md", """# Policy Impact Reports

Current layer: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**

## Purpose

This folder stores explanation cards for pair-policy dry-run drift cases.

## Primary command

```powershell
python scripts/benchmarks/generate_policy_impact_cards.py
```

## README Update Rule

Update this mini README whenever policy impact schemas, cards, report paths, or interpretation rules change.

Boundary: policy impact reports explain local classifier-governance simulations only.
""")

write(ROOT / "visuals" / "policy_impact" / "README.md", """# Policy Impact Visuals

Current layer: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**

## Purpose

This folder stores charts summarizing policy impact cards.

## README Update Rule

Update this mini README whenever policy impact chart names or chart meanings change.

Boundary: policy impact visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "policy_impact" / "v0_4_7" / "README.md", """# v0.4.7 Policy Impact Charts

## Expected Charts

- `policy_impact_class_counts.png`
- `policy_impact_risk_labels.png`
- `policy_impact_drift_by_gate.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local policy-impact diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.6[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.5d[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.6 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.7 |", r)

if "| Policy impact cards | `reports/policy_impact/latest_policy_impact_cards.md` |" not in r:
    r = r.replace("| Pair policy dry-run charts | `visuals/policy_dry_run/v0_4_6/` |\n",
                  "| Pair policy dry-run charts | `visuals/policy_dry_run/v0_4_6/` |\n| Policy impact cards | `reports/policy_impact/latest_policy_impact_cards.md` |\n| Policy impact charts | `visuals/policy_impact/v0_4_7/` |\n")

if "python scripts/benchmarks/generate_policy_impact_cards.py" not in r:
    r = r.replace("python scripts/benchmarks/run_pair_policy_dry_run.py\npython scripts/feedback/run_nexus_feedback.py",
                  "python scripts/benchmarks/run_pair_policy_dry_run.py\npython scripts/benchmarks/generate_policy_impact_cards.py\npython scripts/feedback/run_nexus_feedback.py")

section = """## Policy Impact Explanation Cards v0.4.7

v0.4.7 explains the drift cases produced by the v0.4.6 dry-run simulator.

Primary command:

```powershell
python scripts/benchmarks/generate_policy_impact_cards.py
```

Primary outputs:

```text
reports/policy_impact/latest_policy_impact_cards.json
reports/policy_impact/latest_policy_impact_cards.md
reports/policy_impact/cards/v0_4_7/
visuals/policy_impact/v0_4_7/
```

This layer explains:

```text
which dry-run pairs drifted
why each drift happened
whether the drift is a controlled downgrade or human-review case
which gates are most involved in policy impact
```

Boundary: impact cards explain simulated classifier-governance effects only. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Policy Impact Explanation Cards v0.4.7" not in r:
    r = r.replace("## Pair Policy Dry-Run Simulator v0.4.6", section + "## Pair Policy Dry-Run Simulator v0.4.6", 1)

lesson = "| L-029 | v0.4.6 produced 9 drift cases but drift alone is not an enforcement decision. | A dry-run simulator can show impact without explaining whether each impact is justified. | Any simulated classifier drift must receive an impact explanation card before enforcement is considered. |"
if lesson not in r:
    r = r.replace("| L-028 | Nexus feedback v0.4.5d reached health 1.0 and ranked pair-policy pressure as the top next target. | Policy review pressure should not mutate the classifier directly. | Any classifier-policy change must first pass a dry-run simulator comparing current class vs simulated policy class. |\n",
                  "| L-028 | Nexus feedback v0.4.5d reached health 1.0 and ranked pair-policy pressure as the top next target. | Policy review pressure should not mutate the classifier directly. | Any classifier-policy change must first pass a dry-run simulator comparing current class vs simulated policy class. |\n" + lesson + "\n")

if "| v0.4.7 | Policy impact explanation cards for dry-run drift cases. |" not in r:
    r = r.replace("| v0.4.6 | Pair policy dry-run simulator for non-mutating classifier-policy impact analysis. |\n",
                  "| v0.4.6 | Pair policy dry-run simulator for non-mutating classifier-policy impact analysis. |\n| v0.4.7 | Policy impact explanation cards for dry-run drift cases. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.8 - Policy Decision Record**

Recommended goals:

- Convert policy impact cards into a decision record.
- Approve, reject, or defer each simulated drift class.
- Preserve classifier non-mutation until decision record passes.
- Preserve non-claim locks: policy decisions are local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS update.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**", a)
if "Policy impact patch" not in a:
    a = a.replace("| Pair policy dry-run patch | `reports/policy_dry_run/`, `visuals/policy_dry_run/`, policy review report | dry-run report + Nexus feedback + release validator; no classifier mutation |\n",
                  "| Pair policy dry-run patch | `reports/policy_dry_run/`, `visuals/policy_dry_run/`, policy review report | dry-run report + Nexus feedback + release validator; no classifier mutation |\n| Policy impact patch | `reports/policy_impact/`, `visuals/policy_impact/`, dry-run report | impact cards + release validator; no classifier mutation |\n")
write(agents, a)

# route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.7"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["policy_impact_cards"] = {
    "read_first": ["reports/policy_dry_run/latest_pair_policy_dry_run.json", "reports/policy/latest_pair_policy_review.json"],
    "validate": ["python scripts/benchmarks/generate_policy_impact_cards.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/policy_impact/latest_policy_impact_cards.md", "reports/policy_impact/cards/v0_4_7/", "visuals/policy_impact/v0_4_7/"],
    "mutation_lock": "Does not change classifier behavior; explains dry-run impact only."
}
write_json(route_path, route)

# task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**", m)
if "| Policy impact patch |" not in m:
    m = m.replace("| Pair policy dry-run patch | outer | validation | governance | pair policy review + dry-run report | dry-run report + charts + release validator | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |\n",
                  "| Pair policy dry-run patch | outer | validation | governance | pair policy review + dry-run report | dry-run report + charts + release validator | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |\n| Policy impact patch | outer | validation | governance | dry-run report + impact cards | impact report + charts + release validator | `reports/policy_impact/latest_policy_impact_cards.md` |\n")
write(matrix, m)

# atlas.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.7 | Policy impact explanation cards |" not in t:
    t = t.replace("| v0.4.6 | Pair policy dry-run simulator | `python scripts/benchmarks/run_pair_policy_dry_run.py` | Simulates policy impact without classifier mutation | `reports/policy_dry_run/latest_pair_policy_dry_run.md` | `visuals/policy_dry_run/v0_4_6/` |\n",
                  "| v0.4.6 | Pair policy dry-run simulator | `python scripts/benchmarks/run_pair_policy_dry_run.py` | Simulates policy impact without classifier mutation | `reports/policy_dry_run/latest_pair_policy_dry_run.md` | `visuals/policy_dry_run/v0_4_6/` |\n| v0.4.7 | Policy impact explanation cards | `python scripts/benchmarks/generate_policy_impact_cards.py` | Explains each dry-run drift case before policy decision | `reports/policy_impact/latest_policy_impact_cards.md` | `visuals/policy_impact/v0_4_7/` |\n")
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_7_policy_impact_explanation_cards.md", f"""# TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards

Generated: {GENERATED_AT}

## Purpose

Explain the dry-run drift cases produced by v0.4.6 before any policy decision or enforcement candidate.

## Adds

- `scripts/benchmarks/generate_policy_impact_cards.py`
- `reports/policy_impact/`
- `reports/policy_impact/cards/v0_4_7/`
- `visuals/policy_impact/v0_4_7/`

## Boundary

Policy impact cards are local classifier-governance explanation artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.4.7 policy impact explanation card patch written")
