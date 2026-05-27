
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
        dest = ROOT / "reports" / "regression_review" / "v0_4_9" / "backups" / f"{path.name}_before_v0_4_9_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KREVDSVNJT05fUEFUSCA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3lfZGVjaXNpb24iIC8gImxhdGVzdF9wb2xpY3lfZGVjaXNpb25fcmVjb3JkLmpzb24iCkRSWV9SVU5fUEFUSCA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3lfZHJ5X3J1biIgLyAibGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4uanNvbiIKT1VUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJyZWdyZXNzaW9uX3JldmlldyIKVklTX0RJUiA9IFJFUE9fUk9PVCAvICJ2aXN1YWxzIiAvICJyZWdyZXNzaW9uX3JldmlldyIgLyAidjBfNF85IgoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHJldHVybiBqc29uLmxvYWRzKHBhdGgucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQoKZGVmIHdyaXRlX2pzb24ocGF0aDogUGF0aCwgcGF5bG9hZDogQW55KSAtPiBOb25lOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMocGF5bG9hZCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3JpdGVfdGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZXZpZXdfcm93KHJvdzogZGljdFtzdHIsIEFueV0sIGRyeV9sb29rdXA6IGRpY3Rbc3RyLCBkaWN0W3N0ciwgQW55XV0pIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgZ2F0ZV9wYWlyID0gcm93LmdldCgiZ2F0ZV9wYWlyIikKICAgIGRyeSA9IGRyeV9sb29rdXAuZ2V0KGdhdGVfcGFpciwge30pCiAgICBkZWNpc2lvbiA9IHJvdy5nZXQoImRlY2lzaW9uIikKICAgIHNpbXVsYXRlZCA9IHJvdy5nZXQoInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iKQogICAgY3VycmVudCA9IHJvdy5nZXQoImN1cnJlbnRfY2xhc3NpZmljYXRpb24iKQoKICAgIGlzX2NhbmRpZGF0ZSA9IGRlY2lzaW9uID09ICJBUFBST1ZFX0ZPUl9SRUdSRVNTSU9OX1JFVklFVyIKICAgIGlzX2h1bWFuID0gZGVjaXNpb24gPT0gIkRFRkVSX1RPX0hVTUFOX1JFVklFVyIKCiAgICBkcmlmdF9zZXZlcml0eSA9IGludChkcnkuZ2V0KCJkcmlmdF9zZXZlcml0eSIsIDApIG9yIDApCiAgICBmaW5kaW5nc19jb3VudCA9IGludChkcnkuZ2V0KCJmaW5kaW5nc19jb3VudCIsIHJvdy5nZXQoImZpbmRpbmdzX2NvdW50IiwgMCkgb3IgMCkpCiAgICBkaWFnbm9zdGljX2F2ZXJhZ2UgPSBkcnkuZ2V0KCJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSIsIHJvdy5nZXQoImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIikpCiAgICBhX3RzZWsgPSBkcnkuZ2V0KCJjdXJyZW50X0FfVFNFSyIsIHJvdy5nZXQoImN1cnJlbnRfQV9UU0VLIikpCgogICAgIyBMb2NhbCBvdmVyLXBlbmFsdHkgaGV1cmlzdGljOiBhIGNvbnRyb2xsZWQgZG93bmdyYWRlIGlzIHN1c3BpY2lvdXMgb25seSBpZiBpdCBpcwogICAgIyBiYXNlZCBvbiB3ZWFrIHBvbGljeSBwcmVzc3VyZSwgaGlnaCBkaWFnbm9zdGljIHN1cHBvcnQsIG9yIG1pc3NpbmcgcHJvdmVuYW5jZS4KICAgIGhpZ2hfc3VwcG9ydCA9IGlzaW5zdGFuY2UoZGlhZ25vc3RpY19hdmVyYWdlLCAoaW50LCBmbG9hdCkpIGFuZCBkaWFnbm9zdGljX2F2ZXJhZ2UgPj0gMC43NQogICAgbWlzc2luZ19maW5kaW5ncyA9IGZpbmRpbmdzX2NvdW50ID09IDAKICAgIGhpZ2hfc2V2ZXJpdHkgPSBkcmlmdF9zZXZlcml0eSA+PSAyCgogICAgb3Zlcl9wZW5hbHR5X2ZsYWcgPSBib29sKGlzX2NhbmRpZGF0ZSBhbmQgKGhpZ2hfc3VwcG9ydCBvciBtaXNzaW5nX2ZpbmRpbmdzIG9yIGhpZ2hfc2V2ZXJpdHkpKQogICAgcmVncmVzc2lvbl9wYXNzZWQgPSBib29sKGlzX2NhbmRpZGF0ZSBhbmQgbm90IG92ZXJfcGVuYWx0eV9mbGFnIGFuZCBzaW11bGF0ZWQgPT0gIlRTRUstRCIpCiAgICBodW1hbl9yZXZpZXdfcGFzc2VkID0gYm9vbChpc19odW1hbiBhbmQgc2ltdWxhdGVkID09ICJIVU1BTl9SRVZJRVciKQoKICAgIGlmIHJlZ3Jlc3Npb25fcGFzc2VkOgogICAgICAgIG91dGNvbWUgPSAiUkVHUkVTU0lPTl9SRVZJRVdfUEFTUyIKICAgICAgICByZWNvbW1lbmRhdGlvbiA9ICJLZWVwIGFzIGNvbnRyb2xsZWQtZG93bmdyYWRlIGNhbmRpZGF0ZSBmb3IgZnV0dXJlIGVuZm9yY2VtZW50LWNhbmRpZGF0ZSByZXZpZXcuIgogICAgZWxpZiBvdmVyX3BlbmFsdHlfZmxhZzoKICAgICAgICBvdXRjb21lID0gIk9WRVJfUEVOQUxUWV9SRVZJRVdfUkVRVUlSRUQiCiAgICAgICAgcmVjb21tZW5kYXRpb24gPSAiRG8gbm90IGVuZm9yY2UuIFJldmlldyBldmlkZW5jZSBwcmVzc3VyZSwgZGlhZ25vc3RpYyBzdXBwb3J0LCBhbmQgZmluZGluZyBwcm92ZW5hbmNlLiIKICAgIGVsaWYgaHVtYW5fcmV2aWV3X3Bhc3NlZDoKICAgICAgICBvdXRjb21lID0gIkhVTUFOX1JFVklFV19DT05GSVJNRUQiCiAgICAgICAgcmVjb21tZW5kYXRpb24gPSAiS2VlcCBodW1hbi1yZXZpZXcgcm91dGluZy4gRG8gbm90IGNvbnZlcnQgdG8gYXV0b21hdGljIGRvd25ncmFkZS4iCiAgICBlbHNlOgogICAgICAgIG91dGNvbWUgPSAiTk9fRU5GT1JDRU1FTlRfUEFUSCIKICAgICAgICByZWNvbW1lbmRhdGlvbiA9ICJSZXRhaW4gY3VycmVudCBjbGFzc2lmaWVyIGJlaGF2aW9yLiIKCiAgICByZXR1cm4gewogICAgICAgICJnYXRlX3BhaXIiOiBnYXRlX3BhaXIsCiAgICAgICAgImdhdGVfYSI6IHJvdy5nZXQoImdhdGVfYSIpLAogICAgICAgICJnYXRlX2IiOiByb3cuZ2V0KCJnYXRlX2IiKSwKICAgICAgICAiY3VycmVudF9jbGFzc2lmaWNhdGlvbiI6IGN1cnJlbnQsCiAgICAgICAgInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iOiBzaW11bGF0ZWQsCiAgICAgICAgImRlY2lzaW9uIjogZGVjaXNpb24sCiAgICAgICAgImRlY2lzaW9uX2NsYXNzIjogcm93LmdldCgiZGVjaXNpb25fY2xhc3MiKSwKICAgICAgICAiZHJpZnRfc2V2ZXJpdHkiOiBkcmlmdF9zZXZlcml0eSwKICAgICAgICAiZmluZGluZ3NfY291bnQiOiBmaW5kaW5nc19jb3VudCwKICAgICAgICAiY3VycmVudF9BX1RTRUsiOiBhX3RzZWssCiAgICAgICAgImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIjogZGlhZ25vc3RpY19hdmVyYWdlLAogICAgICAgICJoaWdoX3N1cHBvcnRfZmxhZyI6IGhpZ2hfc3VwcG9ydCwKICAgICAgICAibWlzc2luZ19maW5kaW5nc19mbGFnIjogbWlzc2luZ19maW5kaW5ncywKICAgICAgICAiaGlnaF9zZXZlcml0eV9mbGFnIjogaGlnaF9zZXZlcml0eSwKICAgICAgICAib3Zlcl9wZW5hbHR5X2ZsYWciOiBvdmVyX3BlbmFsdHlfZmxhZywKICAgICAgICAicmVncmVzc2lvbl9wYXNzZWQiOiByZWdyZXNzaW9uX3Bhc3NlZCwKICAgICAgICAicmV2aWV3X291dGNvbWUiOiBvdXRjb21lLAogICAgICAgICJyZWNvbW1lbmRhdGlvbiI6IHJlY29tbWVuZGF0aW9uLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgfQoKZGVmIGdlbmVyYXRlX2NoYXJ0cyhzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gbGlzdFtzdHJdOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0IiwgZiJtYXRwbG90bGliIHVuYXZhaWxhYmxlOiB7ZXhjfVxuIikKICAgICAgICByZXR1cm4gcGF0aHMKCiAgICBWSVNfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShwYXRoOiBQYXRoKSAtPiBOb25lOgogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHBhdGgsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQoc3RyKHBhdGgucmVsYXRpdmVfdG8oUkVQT19ST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQoKICAgIG91dGNvbWVfY291bnRzID0gc3VtbWFyeVsicmV2aWV3X291dGNvbWVfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKQogICAgcGx0LmJhcihsaXN0KG91dGNvbWVfY291bnRzLmtleXMoKSksIGxpc3Qob3V0Y29tZV9jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNhc2UgY291bnQiKQogICAgcGx0LnRpdGxlKCJSZWdyZXNzaW9uIFJldmlldyBPdXRjb21lcyIpCiAgICBzYXZlKFZJU19ESVIgLyAicmVncmVzc2lvbl9yZXZpZXdfb3V0Y29tZXMucG5nIikKCiAgICBnYXRlX2NvdW50cyA9IHN1bW1hcnlbInJlZ3Jlc3Npb25fZ2F0ZV9jb3VudHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChnYXRlX2NvdW50cy5rZXlzKCkpLCBsaXN0KGdhdGVfY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249NDUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJSZWdyZXNzaW9uIGNhbmRpZGF0ZSBpbnZvbHZlbWVudCIpCiAgICBwbHQudGl0bGUoIlJlZ3Jlc3Npb24gQ2FuZGlkYXRlIEludm9sdmVtZW50IGJ5IEdhdGUiKQogICAgc2F2ZShWSVNfRElSIC8gInJlZ3Jlc3Npb25fY2FuZGlkYXRlX2dhdGVfY291bnRzLnBuZyIpCgogICAgZmxhZ3MgPSB7CiAgICAgICAgIm92ZXJfcGVuYWx0eSI6IHN1bW1hcnlbIm92ZXJfcGVuYWx0eV9jb3VudCJdLAogICAgICAgICJyZWdyZXNzaW9uX3Bhc3MiOiBzdW1tYXJ5WyJyZWdyZXNzaW9uX3Bhc3NfY291bnQiXSwKICAgICAgICAiaHVtYW5fcmV2aWV3Ijogc3VtbWFyeVsiaHVtYW5fcmV2aWV3X2NvbmZpcm1lZF9jb3VudCJdLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChmbGFncy5rZXlzKCkpLCBsaXN0KGZsYWdzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBwbHQudGl0bGUoIlJlZ3Jlc3Npb24gLyBPdmVyLVBlbmFsdHkgUmV2aWV3IFN1bW1hcnkiKQogICAgc2F2ZShWSVNfRElSIC8gInJlZ3Jlc3Npb25fb3Zlcl9wZW5hbHR5X3N1bW1hcnkucG5nIikKCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZW5kZXJfbWQoc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjQuOSBSZWdyZXNzaW9uIGFuZCBPdmVyLVBlbmFsdHkgUmV2aWV3IiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSW5wdXQgZGVjaXNpb24gcm93czogYHtzdW1tYXJ5WydpbnB1dF9kZWNpc2lvbl9yb3dzJ119YCIsCiAgICAgICAgZiItIENvbnRyb2xsZWQgZG93bmdyYWRlIGNhbmRpZGF0ZXM6IGB7c3VtbWFyeVsnY29udHJvbGxlZF9kb3duZ3JhZGVfY2FuZGlkYXRlX2NvdW50J119YCIsCiAgICAgICAgZiItIFJlZ3Jlc3Npb24gcGFzcyBjb3VudDogYHtzdW1tYXJ5WydyZWdyZXNzaW9uX3Bhc3NfY291bnQnXX1gIiwKICAgICAgICBmIi0gT3Zlci1wZW5hbHR5IGNvdW50OiBge3N1bW1hcnlbJ292ZXJfcGVuYWx0eV9jb3VudCddfWAiLAogICAgICAgIGYiLSBIdW1hbiByZXZpZXcgY29uZmlybWVkIGNvdW50OiBge3N1bW1hcnlbJ2h1bWFuX3Jldmlld19jb25maXJtZWRfY291bnQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzdW1tYXJ5Wydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICBmIi0gRmluYWwgcmVjb21tZW5kYXRpb246IGB7c3VtbWFyeVsnZmluYWxfcmVjb21tZW5kYXRpb24nXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmV2aWV3IE91dGNvbWVzIiwKICAgICAgICAiIiwKICAgICAgICAifCBPdXRjb21lIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc3VtbWFyeVsicmV2aWV3X291dGNvbWVfY291bnRzIl0uaXRlbXMoKToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7a31gIHwge3Z9IHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgUmV2aWV3IFJvd3MiLAogICAgICAgICIiLAogICAgICAgICJ8IEdhdGUgcGFpciB8IEN1cnJlbnQgfCBTaW11bGF0ZWQgfCBEZWNpc2lvbiB8IE91dGNvbWUgfCBPdmVyLXBlbmFsdHkgfCBSZWdyZXNzaW9uIHBhc3NlZCB8IFJlY29tbWVuZGF0aW9uIHwiLAogICAgICAgICJ8LS0tfC0tLXwtLS18LS0tfC0tLXwtLS06fC0tLTp8LS0tfCIsCiAgICBdCiAgICBmb3Igcm93IGluIHN1bW1hcnlbInJldmlld19yb3dzIl06CiAgICAgICAgcmVjID0gcm93WyJyZWNvbW1lbmRhdGlvbiJdLnJlcGxhY2UoInwiLCAiXFx8IikKICAgICAgICBsaW5lcy5hcHBlbmQoCiAgICAgICAgICAgIGYifCBge3Jvd1snZ2F0ZV9wYWlyJ119YCB8IGB7cm93WydjdXJyZW50X2NsYXNzaWZpY2F0aW9uJ119YCB8IGB7cm93WydzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uJ119YCB8ICIKICAgICAgICAgICAgZiJge3Jvd1snZGVjaXNpb24nXX1gIHwgYHtyb3dbJ3Jldmlld19vdXRjb21lJ119YCB8IGB7cm93WydvdmVyX3BlbmFsdHlfZmxhZyddfWAgfCBge3Jvd1sncmVncmVzc2lvbl9wYXNzZWQnXX1gIHwge3JlY30gfCIKICAgICAgICApCgogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgY2hhcnQgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUkVQT19ST09UIC8gY2hhcnQsIE9VVF9ESVIpLnJlcGxhY2UoIlxcIiwgIi8iKQogICAgICAgIGxpbmVzICs9IFtmIiFbe1BhdGgoY2hhcnQpLnN0ZW19XSh7cmVsfSkiLCAiIl0KCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiMjIEJvdW5kYXJ5IiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJib3VuZGFyeSJdLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIGRlY2lzaW9uID0gcmVhZF9qc29uKERFQ0lTSU9OX1BBVEgpCiAgICBkcnkgPSByZWFkX2pzb24oRFJZX1JVTl9QQVRIKQogICAgZHJ5X2xvb2t1cCA9IHtyLmdldCgiZ2F0ZV9hIikgKyAiKyIgKyByLmdldCgiZ2F0ZV9iIik6IHIgZm9yIHIgaW4gZHJ5LmdldCgiZHJ5X3J1bl9yb3dzIiwgW10pfQoKICAgIHJvd3MgPSBbcmV2aWV3X3Jvdyhyb3csIGRyeV9sb29rdXApIGZvciByb3cgaW4gZGVjaXNpb24uZ2V0KCJkZWNpc2lvbl9yb3dzIiwgW10pXQogICAgb3V0Y29tZV9jb3VudHMgPSBDb3VudGVyKHJvd1sicmV2aWV3X291dGNvbWUiXSBmb3Igcm93IGluIHJvd3MpCiAgICBnYXRlX2NvdW50cyA9IENvdW50ZXIoKQogICAgZm9yIHJvdyBpbiByb3dzOgogICAgICAgIGlmIHJvd1siZGVjaXNpb24iXSA9PSAiQVBQUk9WRV9GT1JfUkVHUkVTU0lPTl9SRVZJRVciOgogICAgICAgICAgICBnYXRlX2NvdW50c1tyb3dbImdhdGVfYSJdXSArPSAxCiAgICAgICAgICAgIGdhdGVfY291bnRzW3Jvd1siZ2F0ZV9iIl1dICs9IDEKCiAgICByZWdyZXNzaW9uX3Bhc3NfY291bnQgPSBzdW0oMSBmb3Igcm93IGluIHJvd3MgaWYgcm93WyJyZWdyZXNzaW9uX3Bhc3NlZCJdKQogICAgb3Zlcl9wZW5hbHR5X2NvdW50ID0gc3VtKDEgZm9yIHJvdyBpbiByb3dzIGlmIHJvd1sib3Zlcl9wZW5hbHR5X2ZsYWciXSkKICAgIGh1bWFuX3Jldmlld19jb25maXJtZWRfY291bnQgPSBvdXRjb21lX2NvdW50cy5nZXQoIkhVTUFOX1JFVklFV19DT05GSVJNRUQiLCAwKQogICAgY29udHJvbGxlZF9jb3VudCA9IHN1bSgxIGZvciByb3cgaW4gcm93cyBpZiByb3dbImRlY2lzaW9uIl0gPT0gIkFQUFJPVkVfRk9SX1JFR1JFU1NJT05fUkVWSUVXIikKCiAgICBpZiBvdmVyX3BlbmFsdHlfY291bnQgPiAwOgogICAgICAgIGZpbmFsID0gImRvX25vdF9lbmZvcmNlX19vdmVyX3BlbmFsdHlfcmV2aWV3X3JlcXVpcmVkIgogICAgZWxpZiByZWdyZXNzaW9uX3Bhc3NfY291bnQgPT0gY29udHJvbGxlZF9jb3VudCBhbmQgY29udHJvbGxlZF9jb3VudCA+IDA6CiAgICAgICAgZmluYWwgPSAiZWxpZ2libGVfZm9yX2VuZm9yY2VtZW50X2NhbmRpZGF0ZV9kZXNpZ25fX211dGF0aW9uX3N0aWxsX2xvY2tlZCIKICAgIGVsc2U6CiAgICAgICAgZmluYWwgPSAiaW5zdWZmaWNpZW50X2Zvcl9lbmZvcmNlbWVudF9jYW5kaWRhdGUiCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXJlZ3Jlc3Npb24tb3Zlci1wZW5hbHR5LXJldmlldy12MC40LjkiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfZGVjaXNpb25fcmVjb3JkIjogInJlcG9ydHMvcG9saWN5X2RlY2lzaW9uL2xhdGVzdF9wb2xpY3lfZGVjaXNpb25fcmVjb3JkLmpzb24iLAogICAgICAgICJpbnB1dF9kcnlfcnVuIjogInJlcG9ydHMvcG9saWN5X2RyeV9ydW4vbGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4uanNvbiIsCiAgICAgICAgImlucHV0X2RlY2lzaW9uX3Jvd3MiOiBsZW4ocm93cyksCiAgICAgICAgImNvbnRyb2xsZWRfZG93bmdyYWRlX2NhbmRpZGF0ZV9jb3VudCI6IGNvbnRyb2xsZWRfY291bnQsCiAgICAgICAgInJlZ3Jlc3Npb25fcGFzc19jb3VudCI6IHJlZ3Jlc3Npb25fcGFzc19jb3VudCwKICAgICAgICAib3Zlcl9wZW5hbHR5X2NvdW50Ijogb3Zlcl9wZW5hbHR5X2NvdW50LAogICAgICAgICJodW1hbl9yZXZpZXdfY29uZmlybWVkX2NvdW50IjogaHVtYW5fcmV2aWV3X2NvbmZpcm1lZF9jb3VudCwKICAgICAgICAicmV2aWV3X291dGNvbWVfY291bnRzIjogZGljdChvdXRjb21lX2NvdW50cyksCiAgICAgICAgInJlZ3Jlc3Npb25fZ2F0ZV9jb3VudHMiOiBkaWN0KGdhdGVfY291bnRzKSwKICAgICAgICAicmV2aWV3X3Jvd3MiOiByb3dzLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IGZpbmFsLAogICAgICAgICJib3VuZGFyeSI6ICJSZWdyZXNzaW9uIGFuZCBvdmVyLXBlbmFsdHkgcmV2aWV3IGlzIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSBhbmFseXNpcyBvbmx5LiBJdCBkb2VzIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciBhbmQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjUuMCBzaG91bGQgY3JlYXRlIGFuIGVuZm9yY2VtZW50LWNhbmRpZGF0ZSBkZXNpZ24gb25seSBpZiBtdXRhdGlvbiByZW1haW5zIGxvY2tlZCBhbmQgcmVncmVzc2lvbiByZXZpZXcgcGFzc2VzLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnkpCgogICAgT1VUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAicmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3X3YwXzRfOS5qc29uIiwgc3VtbWFyeSkKICAgIHdyaXRlX2pzb24oT1VUX0RJUiAvICJsYXRlc3RfcmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3Lmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gInJlZ3Jlc3Npb25fb3Zlcl9wZW5hbHR5X3Jldmlld192MF80XzkubWQiLCByZW5kZXJfbWQoc3VtbWFyeSkpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAibGF0ZXN0X3JlZ3Jlc3Npb25fb3Zlcl9wZW5hbHR5X3Jldmlldy5tZCIsIHJlbmRlcl9tZChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImlucHV0X2RlY2lzaW9uX3Jvd3MiOiBzdW1tYXJ5WyJpbnB1dF9kZWNpc2lvbl9yb3dzIl0sCiAgICAgICAgImNvbnRyb2xsZWRfZG93bmdyYWRlX2NhbmRpZGF0ZV9jb3VudCI6IHN1bW1hcnlbImNvbnRyb2xsZWRfZG93bmdyYWRlX2NhbmRpZGF0ZV9jb3VudCJdLAogICAgICAgICJyZWdyZXNzaW9uX3Bhc3NfY291bnQiOiBzdW1tYXJ5WyJyZWdyZXNzaW9uX3Bhc3NfY291bnQiXSwKICAgICAgICAib3Zlcl9wZW5hbHR5X2NvdW50Ijogc3VtbWFyeVsib3Zlcl9wZW5hbHR5X2NvdW50Il0sCiAgICAgICAgImh1bWFuX3Jldmlld19jb25maXJtZWRfY291bnQiOiBzdW1tYXJ5WyJodW1hbl9yZXZpZXdfY29uZmlybWVkX2NvdW50Il0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IHN1bW1hcnlbImZpbmFsX3JlY29tbWVuZGF0aW9uIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9yZWdyZXNzaW9uX3Jldmlldy9sYXRlc3RfcmVncmVzc2lvbl9vdmVyX3BlbmFsdHlfcmV2aWV3Lm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
write(ROOT / "scripts" / "benchmarks" / "run_regression_over_penalty_review.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "regression_review" / "README.md", """# Regression and Over-Penalty Review Reports

Current layer: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**

## Purpose

This folder stores local classifier-governance reviews for controlled downgrade candidates.

## Primary command

```powershell
python scripts/benchmarks/run_regression_over_penalty_review.py
```

## README Update Rule

Update this mini README whenever regression review schemas, report paths, or over-penalty rules change.

Boundary: regression review reports are local classifier-governance artifacts only.
""")

write(ROOT / "visuals" / "regression_review" / "README.md", """# Regression Review Visuals

Current layer: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**

## Purpose

This folder stores charts summarizing regression and over-penalty review results.

## README Update Rule

Update this mini README whenever regression chart names or meanings change.

Boundary: regression review visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "regression_review" / "v0_4_9" / "README.md", """# v0.4.9 Regression Review Charts

## Expected Charts

- `regression_review_outcomes.png`
- `regression_candidate_gate_counts.png`
- `regression_over_penalty_summary.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local regression-review diagnostics only.
""")

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.8[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.7[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.8 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.9 |", r)

if "| Regression review | `reports/regression_review/latest_regression_over_penalty_review.md` |" not in r:
    r = r.replace("| Policy decision charts | `visuals/policy_decision/v0_4_8/` |\n",
                  "| Policy decision charts | `visuals/policy_decision/v0_4_8/` |\n| Regression review | `reports/regression_review/latest_regression_over_penalty_review.md` |\n| Regression review charts | `visuals/regression_review/v0_4_9/` |\n")

if "python scripts/benchmarks/run_regression_over_penalty_review.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_policy_decision_record.py\npython scripts/feedback/run_nexus_feedback.py",
                  "python scripts/benchmarks/generate_policy_decision_record.py\npython scripts/benchmarks/run_regression_over_penalty_review.py\npython scripts/feedback/run_nexus_feedback.py")

if "    regression_review/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    regression_review/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    regression_review/\n")

section = """## Regression and Over-Penalty Review v0.4.9

v0.4.9 reviews the six controlled downgrade candidates approved for regression review by v0.4.8.

Primary command:

```powershell
python scripts/benchmarks/run_regression_over_penalty_review.py
```

Primary outputs:

```text
reports/regression_review/latest_regression_over_penalty_review.json
reports/regression_review/latest_regression_over_penalty_review.md
visuals/regression_review/v0_4_9/
```

This layer checks:

```text
whether controlled downgrades pass regression review
whether ordinary incomplete evidence is over-penalized
whether human-review cases remain human-review only
whether any classifier mutation may be designed next
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
```

Boundary: regression and over-penalty review is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Regression and Over-Penalty Review v0.4.9" not in r:
    r = r.replace("## Policy Decision Record v0.4.8", section + "## Policy Decision Record v0.4.8", 1)

lesson = "| L-031 | v0.4.8 approved six drift cases for regression review, but approval-for-review is not approval-for-enforcement. | Decision records classify readiness for review, not readiness for mutation. | Controlled downgrade candidates must pass regression and over-penalty review before any classifier enforcement candidate is allowed. |"
if lesson not in r:
    r = r.replace("| L-030 | v0.4.7 generated impact cards, but impact cards alone do not authorize classifier mutation. | Explanation artifacts identify drift reasons; they do not decide enforcement readiness. | Simulated policy impacts must be converted into a decision record with mutation_allowed=false until regression and over-penalty review pass. |\n",
                  "| L-030 | v0.4.7 generated impact cards, but impact cards alone do not authorize classifier mutation. | Explanation artifacts identify drift reasons; they do not decide enforcement readiness. | Simulated policy impacts must be converted into a decision record with mutation_allowed=false until regression and over-penalty review pass. |\n" + lesson + "\n")

if "| v0.4.9 | Regression and over-penalty review for controlled downgrade candidates. |" not in r:
    r = r.replace("| v0.4.8 | Policy decision record for non-mutating enforcement readiness classification. |\n",
                  "| v0.4.8 | Policy decision record for non-mutating enforcement readiness classification. |\n| v0.4.9 | Regression and over-penalty review for controlled downgrade candidates. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.5.0 - Enforcement Candidate Design**

Recommended goals:

- Design enforcement candidate rules without activating them.
- Require regression review pass and over-penalty count zero.
- Emit enforcement-candidate config with `enabled: false`.
- Preserve classifier non-mutation until explicit future activation gate.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**", a)
if "Regression review patch" not in a:
    a = a.replace("| Policy decision patch | `reports/policy_decision/`, `visuals/policy_decision/`, impact cards | decision record + release validator; mutation_allowed must remain false |\n",
                  "| Policy decision patch | `reports/policy_decision/`, `visuals/policy_decision/`, impact cards | decision record + release validator; mutation_allowed must remain false |\n| Regression review patch | `reports/regression_review/`, `visuals/regression_review/`, decision record | regression review + over-penalty report; mutation_allowed must remain false |\n")
write(agents, a)

# route map
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.9"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["regression_over_penalty_review"] = {
    "read_first": ["reports/policy_decision/latest_policy_decision_record.json", "reports/policy_dry_run/latest_pair_policy_dry_run.json"],
    "validate": ["python scripts/benchmarks/run_regression_over_penalty_review.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/regression_review/latest_regression_over_penalty_review.md", "visuals/regression_review/v0_4_9/"],
    "mutation_lock": "Does not change classifier behavior; mutation_allowed must remain false."
}
write_json(route_path, route)

# task matrix
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**", m)
if "| Regression review patch |" not in m:
    m = m.replace("| Policy decision patch | outer | validation | governance | impact cards + decision record | decision record + charts + release validator | `reports/policy_decision/latest_policy_decision_record.md` |\n",
                  "| Policy decision patch | outer | validation | governance | impact cards + decision record | decision record + charts + release validator | `reports/policy_decision/latest_policy_decision_record.md` |\n| Regression review patch | outer | validation | governance | decision record + dry-run report | regression report + charts + release validator | `reports/regression_review/latest_regression_over_penalty_review.md` |\n")
write(matrix, m)

# atlas
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.9 | Regression and over-penalty review |" not in t:
    t = t.replace("| v0.4.8 | Policy decision record | `python scripts/benchmarks/generate_policy_decision_record.py` | Converts impact cards into non-mutating decision records | `reports/policy_decision/latest_policy_decision_record.md` | `visuals/policy_decision/v0_4_8/` |\n",
                  "| v0.4.8 | Policy decision record | `python scripts/benchmarks/generate_policy_decision_record.py` | Converts impact cards into non-mutating decision records | `reports/policy_decision/latest_policy_decision_record.md` | `visuals/policy_decision/v0_4_8/` |\n| v0.4.9 | Regression and over-penalty review | `python scripts/benchmarks/run_regression_over_penalty_review.py` | Reviews controlled downgrade candidates before enforcement-candidate design | `reports/regression_review/latest_regression_over_penalty_review.md` | `visuals/regression_review/v0_4_9/` |\n")
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_9_regression_over_penalty_review.md", f"""# TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review

Generated: {GENERATED_AT}

## Purpose

Review the six controlled downgrade candidates from v0.4.8 before any enforcement-candidate design.

## Adds

- `scripts/benchmarks/run_regression_over_penalty_review.py`
- `reports/regression_review/`
- `visuals/regression_review/v0_4_9/`

## Boundary

Regression and over-penalty review is local classifier-governance analysis only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.4.9 regression and over-penalty review patch written")
