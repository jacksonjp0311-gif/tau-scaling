
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
        dest = ROOT / "reports" / "policy_dry_run" / "v0_4_6" / "backups" / f"{path.name}_before_v0_4_6_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KUE9MSUNZX1BBVEggPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicG9saWN5IiAvICJsYXRlc3RfcGFpcl9wb2xpY3lfcmV2aWV3Lmpzb24iCk9VVF9ESVIgPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicG9saWN5X2RyeV9ydW4iClZJU19ESVIgPSBSRVBPX1JPT1QgLyAidmlzdWFscyIgLyAicG9saWN5X2RyeV9ydW4iIC8gInYwXzRfNiIKCkNMQVNTX09SREVSID0gWyJUU0VLLUIiLCAiVFNFSy1DIiwgIlRTRUstRCIsICJUU0VLLUUiLCAiSFVNQU5fUkVWSUVXIl0KQ0xBU1NfUkFOSyA9IHtjOiBpIGZvciBpLCBjIGluIGVudW1lcmF0ZShDTEFTU19PUkRFUil9CgpkZWYgcmVhZF9qc29uKHBhdGg6IFBhdGgpIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd3JpdGVfanNvbihwYXRoOiBQYXRoLCBwYXlsb2FkOiBBbnkpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhwYXlsb2FkLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3cml0ZV90ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cikgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHNpbXVsYXRlX2NsYXNzKHJvdzogZGljdFtzdHIsIEFueV0pIC0+IHR1cGxlW3N0ciwgc3RyXToKICAgIHBvbGljeV9jbGFzcyA9IHJvdy5nZXQoInBvbGljeV9jbGFzcyIsICIiKQogICAgY3VycmVudCA9IHJvdy5nZXQoImN1cnJlbnRfY2xhc3NpZmljYXRpb24iLCAiVU5LTk9XTiIpCgogICAgaWYgcG9saWN5X2NsYXNzID09ICJUU0VLLUNfUkVUQUlOIjoKICAgICAgICByZXR1cm4gY3VycmVudCwgInJldGFpbiIKICAgIGlmIHBvbGljeV9jbGFzcyA9PSAiVFNFSy1EX0NBTkRJREFURSI6CiAgICAgICAgcmV0dXJuICJUU0VLLUQiLCAiY2FuZGlkYXRlX2Rvd25ncmFkZSIKICAgIGlmIHBvbGljeV9jbGFzcyA9PSAiVFNFSy1FX0NBTkRJREFURSI6CiAgICAgICAgcmV0dXJuICJUU0VLLUUiLCAiY2FuZGlkYXRlX2hhcmRfcmVqZWN0IgogICAgaWYgcG9saWN5X2NsYXNzID09ICJIVU1BTl9SRVZJRVciOgogICAgICAgIHJldHVybiAiSFVNQU5fUkVWSUVXIiwgImh1bWFuX3Jldmlld19yZXF1aXJlZCIKICAgIHJldHVybiBjdXJyZW50LCAidW5rbm93bl9wb2xpY3lfcmV0YWluIgoKZGVmIGRyaWZ0X3NldmVyaXR5KGN1cnJlbnQ6IHN0ciwgc2ltdWxhdGVkOiBzdHIpIC0+IGludDoKICAgIGlmIGN1cnJlbnQgPT0gc2ltdWxhdGVkOgogICAgICAgIHJldHVybiAwCiAgICByZXR1cm4gbWF4KDEsIENMQVNTX1JBTksuZ2V0KHNpbXVsYXRlZCwgOTkpIC0gQ0xBU1NfUkFOSy5nZXQoY3VycmVudCwgOTkpKQoKZGVmIGJ1aWxkX3Jvd3MocG9saWN5OiBkaWN0W3N0ciwgQW55XSkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICByb3dzID0gW10KICAgIGZvciByb3cgaW4gcG9saWN5LmdldCgicG9saWN5X3Jvd3MiLCBbXSk6CiAgICAgICAgc2ltdWxhdGVkLCBhY3Rpb24gPSBzaW11bGF0ZV9jbGFzcyhyb3cpCiAgICAgICAgY3VycmVudCA9IHJvdy5nZXQoImN1cnJlbnRfY2xhc3NpZmljYXRpb24iLCAiVU5LTk9XTiIpCiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAiZ2F0ZV9hIjogcm93LmdldCgiZ2F0ZV9hIiksCiAgICAgICAgICAgICJnYXRlX2IiOiByb3cuZ2V0KCJnYXRlX2IiKSwKICAgICAgICAgICAgImN1cnJlbnRfY2xhc3NpZmljYXRpb24iOiBjdXJyZW50LAogICAgICAgICAgICAicG9saWN5X2NsYXNzIjogcm93LmdldCgicG9saWN5X2NsYXNzIiksCiAgICAgICAgICAgICJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIjogc2ltdWxhdGVkLAogICAgICAgICAgICAic2ltdWxhdGlvbl9hY3Rpb24iOiBhY3Rpb24sCiAgICAgICAgICAgICJkcmlmdGVkIjogY3VycmVudCAhPSBzaW11bGF0ZWQsCiAgICAgICAgICAgICJkcmlmdF9zZXZlcml0eSI6IGRyaWZ0X3NldmVyaXR5KGN1cnJlbnQsIHNpbXVsYXRlZCksCiAgICAgICAgICAgICJmaW5kaW5nX2NvZGVzIjogcm93LmdldCgiZmluZGluZ19jb2RlcyIsIFtdKSwKICAgICAgICAgICAgImZpbmRpbmdzX2NvdW50Ijogcm93LmdldCgiZmluZGluZ3NfY291bnQiLCAwKSwKICAgICAgICAgICAgImN1cnJlbnRfQV9UU0VLIjogcm93LmdldCgiY3VycmVudF9BX1RTRUsiKSwKICAgICAgICAgICAgImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIjogcm93LmdldCgiY3VycmVudF9kaWFnbm9zdGljX2F2ZXJhZ2UiKSwKICAgICAgICAgICAgInJlY29tbWVuZGVkX2FjdGlvbiI6IHJvdy5nZXQoInJlY29tbWVuZGVkX2FjdGlvbiIpLAogICAgICAgICAgICAicmVhc29uIjogcm93LmdldCgicmVhc29uIiksCiAgICAgICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICB9KQogICAgcmV0dXJuIHJvd3MKCmRlZiBnZW5lcmF0ZV9jaGFydHMoc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IGxpc3Rbc3RyXToKICAgIGNoYXJ0X3BhdGhzOiBsaXN0W3N0cl0gPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0IiwgZiJtYXRwbG90bGliIHVuYXZhaWxhYmxlOiB7ZXhjfVxuIikKICAgICAgICByZXR1cm4gY2hhcnRfcGF0aHMKCiAgICBWSVNfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZWZpZyhwYXRoOiBQYXRoKSAtPiBOb25lOgogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHBhdGgsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBjaGFydF9wYXRocy5hcHBlbmQoc3RyKHBhdGgucmVsYXRpdmVfdG8oUkVQT19ST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQoKICAgIGN1cnJlbnRfY291bnRzID0gc3VtbWFyeVsiY3VycmVudF9jbGFzc19jb3VudHMiXQogICAgc2ltdWxhdGVkX2NvdW50cyA9IHN1bW1hcnlbInNpbXVsYXRlZF9jbGFzc19jb3VudHMiXQogICAgbGFiZWxzID0gc29ydGVkKHNldChjdXJyZW50X2NvdW50cykgfCBzZXQoc2ltdWxhdGVkX2NvdW50cyksIGtleT1sYW1iZGEgeDogQ0xBU1NfUkFOSy5nZXQoeCwgOTkpKQoKICAgIHggPSBsaXN0KHJhbmdlKGxlbihsYWJlbHMpKSkKICAgIHdpZHRoID0gMC4zNQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIoW2kgLSB3aWR0aC8yIGZvciBpIGluIHhdLCBbY3VycmVudF9jb3VudHMuZ2V0KGssIDApIGZvciBrIGluIGxhYmVsc10sIHdpZHRoPXdpZHRoLCBsYWJlbD0iY3VycmVudCIpCiAgICBwbHQuYmFyKFtpICsgd2lkdGgvMiBmb3IgaSBpbiB4XSwgW3NpbXVsYXRlZF9jb3VudHMuZ2V0KGssIDApIGZvciBrIGluIGxhYmVsc10sIHdpZHRoPXdpZHRoLCBsYWJlbD0ic2ltdWxhdGVkIikKICAgIHBsdC54dGlja3MoeCwgbGFiZWxzLCByb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlBhaXIgY291bnQiKQogICAgcGx0LnRpdGxlKCJDdXJyZW50IHZzIFNpbXVsYXRlZCBQb2xpY3kgQ2xhc3NpZmljYXRpb24iKQogICAgcGx0LmxlZ2VuZCgpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAiY3VycmVudF92c19zaW11bGF0ZWRfY2xhc3NfY291bnRzLnBuZyIpCgogICAgYWN0aW9uX2NvdW50cyA9IHN1bW1hcnlbInNpbXVsYXRpb25fYWN0aW9uX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGFjdGlvbl9jb3VudHMua2V5cygpKSwgbGlzdChhY3Rpb25fY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJQYWlyIGNvdW50IikKICAgIHBsdC50aXRsZSgiUG9saWN5IERyeS1SdW4gQWN0aW9uIENvdW50cyIpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAicG9saWN5X2RyeV9ydW5fYWN0aW9uX2NvdW50cy5wbmciKQoKICAgIGdhdGVfY291bnRzID0gc3VtbWFyeVsiZHJpZnRfYnlfZ2F0ZSJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVfY291bnRzLmtleXMoKSksIGxpc3QoZ2F0ZV9jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj00NSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkRyaWZ0IGludm9sdmVtZW50IGNvdW50IikKICAgIHBsdC50aXRsZSgiQ2xhc3MgRHJpZnQgSW52b2x2ZW1lbnQgYnkgR2F0ZSIpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAiY2xhc3NfZHJpZnRfYnlfZ2F0ZS5wbmciKQoKICAgIHJldHVybiBjaGFydF9wYXRocwoKZGVmIHN1bW1hcml6ZShyb3dzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSwgcG9saWN5OiBkaWN0W3N0ciwgQW55XSkgLT4gZGljdFtzdHIsIEFueV06CiAgICBjdXJyZW50X2NvdW50cyA9IENvdW50ZXIoclsiY3VycmVudF9jbGFzc2lmaWNhdGlvbiJdIGZvciByIGluIHJvd3MpCiAgICBzaW11bGF0ZWRfY291bnRzID0gQ291bnRlcihyWyJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIl0gZm9yIHIgaW4gcm93cykKICAgIGFjdGlvbl9jb3VudHMgPSBDb3VudGVyKHJbInNpbXVsYXRpb25fYWN0aW9uIl0gZm9yIHIgaW4gcm93cykKICAgIGRyaWZ0X3Jvd3MgPSBbciBmb3IgciBpbiByb3dzIGlmIHJbImRyaWZ0ZWQiXV0KICAgIGRyaWZ0X2J5X2dhdGUgPSBDb3VudGVyKCkKICAgIGZvciByIGluIGRyaWZ0X3Jvd3M6CiAgICAgICAgZHJpZnRfYnlfZ2F0ZVtyWyJnYXRlX2EiXV0gKz0gMQogICAgICAgIGRyaWZ0X2J5X2dhdGVbclsiZ2F0ZV9iIl1dICs9IDEKCiAgICBwYWlyX2NvdW50ID0gbGVuKHJvd3MpCiAgICBkcmlmdF9jb3VudCA9IGxlbihkcmlmdF9yb3dzKQogICAgaHVtYW5fcmV2aWV3X2NvdW50ID0gc2ltdWxhdGVkX2NvdW50cy5nZXQoIkhVTUFOX1JFVklFVyIsIDApCiAgICBkb3duZ3JhZGVfY291bnQgPSBzdW0oMSBmb3IgciBpbiBkcmlmdF9yb3dzIGlmIHJbInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iXSA9PSAiVFNFSy1EIikKICAgIGhhcmRfcmVqZWN0X2NvdW50ID0gc3VtKDEgZm9yIHIgaW4gZHJpZnRfcm93cyBpZiByWyJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIl0gPT0gIlRTRUstRSIpCgogICAgb3Zlcl9wZW5hbHR5X2ZsYWcgPSBkcmlmdF9jb3VudCAvIG1heCgxLCBwYWlyX2NvdW50KSA+IDAuMzUgb3IgaGFyZF9yZWplY3RfY291bnQgPiAwCiAgICBzaW11bGF0b3JfcmVjb21tZW5kYXRpb24gPSAoCiAgICAgICAgImRvX25vdF9lbmZvcmNlX3lldF9vdmVyX3BlbmFsdHlfcmV2aWV3X3JlcXVpcmVkIgogICAgICAgIGlmIG92ZXJfcGVuYWx0eV9mbGFnCiAgICAgICAgZWxzZSAic2FmZV9mb3JfaHVtYW5fcmV2aWV3X25vdF9lbmZvcmNlbWVudCIKICAgICAgICBpZiBodW1hbl9yZXZpZXdfY291bnQgPiAwCiAgICAgICAgZWxzZSAiY2FuZGlkYXRlX3NhZmVfZm9yX2xpbWl0ZWRfZW5mb3JjZW1lbnQiCiAgICApCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXBhaXItcG9saWN5LWRyeS1ydW4tdjAuNC42IiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgInBvbGljeV9zb3VyY2UiOiAicmVwb3J0cy9wb2xpY3kvbGF0ZXN0X3BhaXJfcG9saWN5X3Jldmlldy5qc29uIiwKICAgICAgICAicGFpcl9jb3VudCI6IHBhaXJfY291bnQsCiAgICAgICAgImRyaWZ0X2NvdW50IjogZHJpZnRfY291bnQsCiAgICAgICAgImRyaWZ0X3JhdGlvIjogcm91bmQoZHJpZnRfY291bnQgLyBtYXgoMSwgcGFpcl9jb3VudCksIDQpLAogICAgICAgICJodW1hbl9yZXZpZXdfY291bnQiOiBodW1hbl9yZXZpZXdfY291bnQsCiAgICAgICAgImRvd25ncmFkZV9jb3VudCI6IGRvd25ncmFkZV9jb3VudCwKICAgICAgICAiaGFyZF9yZWplY3RfY291bnQiOiBoYXJkX3JlamVjdF9jb3VudCwKICAgICAgICAiY3VycmVudF9jbGFzc19jb3VudHMiOiBkaWN0KGN1cnJlbnRfY291bnRzKSwKICAgICAgICAic2ltdWxhdGVkX2NsYXNzX2NvdW50cyI6IGRpY3Qoc2ltdWxhdGVkX2NvdW50cyksCiAgICAgICAgInNpbXVsYXRpb25fYWN0aW9uX2NvdW50cyI6IGRpY3QoYWN0aW9uX2NvdW50cyksCiAgICAgICAgImRyaWZ0X2J5X2dhdGUiOiBkaWN0KGRyaWZ0X2J5X2dhdGUpLAogICAgICAgICJvdmVyX3BlbmFsdHlfZmxhZyI6IG92ZXJfcGVuYWx0eV9mbGFnLAogICAgICAgICJzaW11bGF0b3JfcmVjb21tZW5kYXRpb24iOiBzaW11bGF0b3JfcmVjb21tZW5kYXRpb24sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJkcnlfcnVuX3Jvd3MiOiByb3dzLAogICAgICAgICJib3VuZGFyeSI6ICJQYWlyIHBvbGljeSBkcnktcnVuIHNpbXVsYXRlcyBjbGFzc2lmaWVyLXBvbGljeSBpbXBhY3Qgb25seS4gSXQgZG9lcyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvZXMgbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC40Ljcgc2hvdWxkIGdlbmVyYXRlIHBvbGljeSBpbXBhY3QgZXhwbGFuYXRpb24gY2FyZHMgYmVmb3JlIGFueSBjbGFzc2lmaWVyIGVuZm9yY2VtZW50IGNhbmRpZGF0ZS4iLAogICAgfQogICAgY2hhcnRzID0gZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnkpCiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzCiAgICByZXR1cm4gc3VtbWFyeQoKZGVmIHJlbmRlcl9tZChzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gc3RyOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNC42IFBhaXIgUG9saWN5IERyeS1SdW4gU2ltdWxhdG9yIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gUGFpciBjb3VudDogYHtzdW1tYXJ5WydwYWlyX2NvdW50J119YCIsCiAgICAgICAgZiItIERyaWZ0IGNvdW50OiBge3N1bW1hcnlbJ2RyaWZ0X2NvdW50J119YCIsCiAgICAgICAgZiItIERyaWZ0IHJhdGlvOiBge3N1bW1hcnlbJ2RyaWZ0X3JhdGlvJ119YCIsCiAgICAgICAgZiItIERvd25ncmFkZSBjb3VudDogYHtzdW1tYXJ5Wydkb3duZ3JhZGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gSHVtYW4gcmV2aWV3IGNvdW50OiBge3N1bW1hcnlbJ2h1bWFuX3Jldmlld19jb3VudCddfWAiLAogICAgICAgIGYiLSBIYXJkIHJlamVjdCBjb3VudDogYHtzdW1tYXJ5WydoYXJkX3JlamVjdF9jb3VudCddfWAiLAogICAgICAgIGYiLSBPdmVyLXBlbmFsdHkgZmxhZzogYHtzdW1tYXJ5WydvdmVyX3BlbmFsdHlfZmxhZyddfWAiLAogICAgICAgIGYiLSBSZWNvbW1lbmRhdGlvbjogYHtzdW1tYXJ5WydzaW11bGF0b3JfcmVjb21tZW5kYXRpb24nXX1gIiwKICAgICAgICBmIi0gUG9saWN5IGVuZm9yY2VkOiBge3N1bW1hcnlbJ3BvbGljeV9lbmZvcmNlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDdXJyZW50IHZzIFNpbXVsYXRlZCBDbGFzcyBDb3VudHMiLAogICAgICAgICIiLAogICAgICAgICJ8IENsYXNzIHwgQ3VycmVudCB8IFNpbXVsYXRlZCB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLTp8IiwKICAgIF0KICAgIGxhYmVscyA9IHNvcnRlZChzZXQoc3VtbWFyeVsiY3VycmVudF9jbGFzc19jb3VudHMiXSkgfCBzZXQoc3VtbWFyeVsic2ltdWxhdGVkX2NsYXNzX2NvdW50cyJdKSwga2V5PWxhbWJkYSB4OiBDTEFTU19SQU5LLmdldCh4LCA5OSkpCiAgICBmb3IgbGFiZWwgaW4gbGFiZWxzOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtsYWJlbH1gIHwge3N1bW1hcnlbJ2N1cnJlbnRfY2xhc3NfY291bnRzJ10uZ2V0KGxhYmVsLCAwKX0gfCB7c3VtbWFyeVsnc2ltdWxhdGVkX2NsYXNzX2NvdW50cyddLmdldChsYWJlbCwgMCl9IHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgU2ltdWxhdGlvbiBBY3Rpb25zIiwKICAgICAgICAiIiwKICAgICAgICAifCBBY3Rpb24gfCBDb3VudCB8IiwKICAgICAgICAifC0tLXwtLS06fCIsCiAgICBdCiAgICBmb3IgaywgdiBpbiBzdW1tYXJ5WyJzaW11bGF0aW9uX2FjdGlvbl9jb3VudHMiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBEcmlmdCBieSBHYXRlIiwKICAgICAgICAiIiwKICAgICAgICAifCBHYXRlIHwgRHJpZnQgaW52b2x2ZW1lbnQgY291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc29ydGVkKHN1bW1hcnlbImRyaWZ0X2J5X2dhdGUiXS5pdGVtcygpLCBrZXk9bGFtYmRhIGt2OiAoLWt2WzFdLCBrdlswXSkpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBEcnktUnVuIFJvd3MiLAogICAgICAgICIiLAogICAgICAgICJ8IEdhdGUgQSB8IEdhdGUgQiB8IEN1cnJlbnQgfCBTaW11bGF0ZWQgfCBBY3Rpb24gfCBEcmlmdGVkIHwgUmVhc29uIHwiLAogICAgICAgICJ8LS0tfC0tLXwtLS18LS0tfC0tLXwtLS06fC0tLXwiLAogICAgXQogICAgZm9yIHIgaW4gc3VtbWFyeVsiZHJ5X3J1bl9yb3dzIl06CiAgICAgICAgcmVhc29uID0gc3RyKHIuZ2V0KCJyZWFzb24iLCAiIikpLnJlcGxhY2UoInwiLCAiXFx8IikKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7clsnZ2F0ZV9hJ119YCB8IGB7clsnZ2F0ZV9iJ119YCB8IGB7clsnY3VycmVudF9jbGFzc2lmaWNhdGlvbiddfWAgfCBge3JbJ3NpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24nXX1gIHwgYHtyWydzaW11bGF0aW9uX2FjdGlvbiddfWAgfCBge3JbJ2RyaWZ0ZWQnXX1gIHwge3JlYXNvbn0gfCIpCgogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgY2hhcnQgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUkVQT19ST09UIC8gY2hhcnQsIE9VVF9ESVIpLnJlcGxhY2UoIlxcIiwgIi8iKQogICAgICAgIGxpbmVzICs9IFtmIiFbe1BhdGgoY2hhcnQpLnN0ZW19XSh7cmVsfSkiLCAiIl0KCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIHBvbGljeSA9IHJlYWRfanNvbihQT0xJQ1lfUEFUSCkKICAgIHJvd3MgPSBidWlsZF9yb3dzKHBvbGljeSkKICAgIHN1bW1hcnkgPSBzdW1tYXJpemUocm93cywgcG9saWN5KQogICAgT1VUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAicGFpcl9wb2xpY3lfZHJ5X3J1bl92MF80XzYuanNvbiIsIHN1bW1hcnkpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAibGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4uanNvbiIsIHN1bW1hcnkpCiAgICBtZCA9IHJlbmRlcl9tZChzdW1tYXJ5KQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gInBhaXJfcG9saWN5X2RyeV9ydW5fdjBfNF82Lm1kIiwgbWQpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAibGF0ZXN0X3BhaXJfcG9saWN5X2RyeV9ydW4ubWQiLCBtZCkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInBhaXJfY291bnQiOiBzdW1tYXJ5WyJwYWlyX2NvdW50Il0sCiAgICAgICAgImRyaWZ0X2NvdW50Ijogc3VtbWFyeVsiZHJpZnRfY291bnQiXSwKICAgICAgICAiZHJpZnRfcmF0aW8iOiBzdW1tYXJ5WyJkcmlmdF9yYXRpbyJdLAogICAgICAgICJkb3duZ3JhZGVfY291bnQiOiBzdW1tYXJ5WyJkb3duZ3JhZGVfY291bnQiXSwKICAgICAgICAiaHVtYW5fcmV2aWV3X2NvdW50Ijogc3VtbWFyeVsiaHVtYW5fcmV2aWV3X2NvdW50Il0sCiAgICAgICAgImhhcmRfcmVqZWN0X2NvdW50Ijogc3VtbWFyeVsiaGFyZF9yZWplY3RfY291bnQiXSwKICAgICAgICAib3Zlcl9wZW5hbHR5X2ZsYWciOiBzdW1tYXJ5WyJvdmVyX3BlbmFsdHlfZmxhZyJdLAogICAgICAgICJzaW11bGF0b3JfcmVjb21tZW5kYXRpb24iOiBzdW1tYXJ5WyJzaW11bGF0b3JfcmVjb21tZW5kYXRpb24iXSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogc3VtbWFyeVsicG9saWN5X2VuZm9yY2VkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9wb2xpY3lfZHJ5X3J1bi9sYXRlc3RfcGFpcl9wb2xpY3lfZHJ5X3J1bi5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo="
write(ROOT / "scripts" / "benchmarks" / "run_pair_policy_dry_run.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "policy_dry_run" / "README.md", """# Pair Policy Dry-Run Reports

Current layer: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**

## Purpose

This folder stores non-enforcing dry-run simulations of pair-policy enforcement.

## Primary command

```powershell
python scripts/benchmarks/run_pair_policy_dry_run.py
```

## README Update Rule

Update this mini README whenever dry-run schemas, simulator rules, or policy interpretation changes.

Boundary: dry-run reports simulate classifier governance only.
""")

write(ROOT / "visuals" / "policy_dry_run" / "README.md", """# Pair Policy Dry-Run Visuals

Current layer: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**

## Purpose

This folder stores charts comparing current classifier output against simulated policy output.

## README Update Rule

Update this mini README whenever dry-run chart names or chart meanings change.

Boundary: dry-run visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "policy_dry_run" / "v0_4_6" / "README.md", """# v0.4.6 Pair Policy Dry-Run Charts

## Expected Charts

- `current_vs_simulated_class_counts.png`
- `policy_dry_run_action_counts.png`
- `class_drift_by_gate.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local policy simulation diagnostics only.
""")

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.5d[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.5c[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.5d - Nexus Feedback Chart-Path Health Repair**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.5d \|", "| Current checkpoint | TAU-SCALING-SA v0.4.6 |", r)

if "| Pair policy dry-run | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |" not in r:
    r = r.replace("| Nexus feedback charts | `visuals/nexus_feedback/v0_4_5/` |\n", "| Nexus feedback charts | `visuals/nexus_feedback/v0_4_5/` |\n| Pair policy dry-run | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |\n| Pair policy dry-run charts | `visuals/policy_dry_run/v0_4_6/` |\n")

if "python scripts/benchmarks/run_pair_policy_dry_run.py" not in r:
    r = r.replace("python scripts/benchmarks/run_pair_policy_review.py\npython scripts/feedback/run_nexus_feedback.py", "python scripts/benchmarks/run_pair_policy_review.py\npython scripts/benchmarks/run_pair_policy_dry_run.py\npython scripts/feedback/run_nexus_feedback.py")

section = """## Pair Policy Dry-Run Simulator v0.4.6

v0.4.6 simulates v0.4.4 pair-policy enforcement without mutating the classifier.

Primary command:

```powershell
python scripts/benchmarks/run_pair_policy_dry_run.py
```

Primary outputs:

```text
reports/policy_dry_run/latest_pair_policy_dry_run.json
reports/policy_dry_run/latest_pair_policy_dry_run.md
visuals/policy_dry_run/v0_4_6/
```

The simulator compares:

```text
current_classification
vs
simulated_policy_classification
```

It answers:

```text
How many pairs drift if policy is enforced?
How many TSEK-C cases become TSEK-D?
How many require human review?
Would enforcement over-penalize local synthetic evidence?
```

Boundary: dry-run simulation is classifier governance only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Pair Policy Dry-Run Simulator v0.4.6" not in r:
    r = r.replace("## Nexus Feedback Chart-Path Health Repair v0.4.5d", section + "## Nexus Feedback Chart-Path Health Repair v0.4.5d", 1)

lesson = "| L-028 | Nexus feedback v0.4.5d reached health 1.0 and ranked pair-policy pressure as the top next target. | Policy review pressure should not mutate the classifier directly. | Any classifier-policy change must first pass a dry-run simulator comparing current class vs simulated policy class. |"
if lesson not in r:
    r = r.replace("| L-027 | v0.4.5c repaired list counters but `sensitivity_sweep` still failed health scoring. | The persisted sensitivity JSON used `chart_paths` while the feedback health scorer checked only `chart_count`. | Feedback health scoring must normalize both count fields and evidence-list fields such as chart_paths. |\n",
                  "| L-027 | v0.4.5c repaired list counters but `sensitivity_sweep` still failed health scoring. | The persisted sensitivity JSON used `chart_paths` while the feedback health scorer checked only `chart_count`. | Feedback health scoring must normalize both count fields and evidence-list fields such as chart_paths. |\n" + lesson + "\n")

if "| v0.4.6 | Pair policy dry-run simulator for non-mutating classifier-policy impact analysis. |" not in r:
    r = r.replace("| v0.4.5d | Nexus feedback chart-path health repair for sensitivity sweep chart evidence. |\n",
                  "| v0.4.5d | Nexus feedback chart-path health repair for sensitivity sweep chart evidence. |\n| v0.4.6 | Pair policy dry-run simulator for non-mutating classifier-policy impact analysis. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**

Recommended goals:

- Explain each simulated class drift.
- Identify over-penalty risks.
- Separate justified downgrades from policy-review-only cases.
- Preserve non-claim locks: impact explanations are local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5d[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**", a)
if "Pair policy dry-run patch" not in a:
    a = a.replace("| Nexus feedback patch | `scripts/feedback/`, `reports/nexus_feedback/`, `visuals/nexus_feedback/` | release validator + Nexus feedback report; no classifier mutation |\n",
                  "| Nexus feedback patch | `scripts/feedback/`, `reports/nexus_feedback/`, `visuals/nexus_feedback/` | release validator + Nexus feedback report; no classifier mutation |\n| Pair policy dry-run patch | `reports/policy_dry_run/`, `visuals/policy_dry_run/`, policy review report | dry-run report + Nexus feedback + release validator; no classifier mutation |\n")
write(agents, a)

route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.6"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["pair_policy_dry_run"] = {
    "read_first": ["reports/policy/latest_pair_policy_review.json", "reports/nexus_feedback/latest_nexus_feedback.json"],
    "validate": ["python scripts/benchmarks/run_pair_policy_dry_run.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/policy_dry_run/latest_pair_policy_dry_run.md", "visuals/policy_dry_run/v0_4_6/"],
    "mutation_lock": "Does not change classifier behavior; simulates policy impact only."
}
write_json(route_path, route)

matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.5d[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**", m)
if "| Pair policy dry-run patch |" not in m:
    m = m.replace("| Feedback chart-path health repair | outer | drift | agent | feedback runner + sensitivity chart_paths | compile + chart-path assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
                  "| Feedback chart-path health repair | outer | drift | agent | feedback runner + sensitivity chart_paths | compile + chart-path assertion + feedback health score 1.0 | `reports/nexus_feedback/latest_nexus_feedback.md` |\n| Pair policy dry-run patch | outer | validation | governance | pair policy review + dry-run report | dry-run report + charts + release validator | `reports/policy_dry_run/latest_pair_policy_dry_run.md` |\n")
write(matrix, m)

atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.6 | Pair policy dry-run simulator |" not in t:
    t = t.replace("| v0.4.5d | Nexus feedback chart-path health repair | chart-path assertion + feedback health assertion | Normalizes sensitivity chart evidence from `chart_paths` | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5d/` |\n",
                  "| v0.4.5d | Nexus feedback chart-path health repair | chart-path assertion + feedback health assertion | Normalizes sensitivity chart evidence from `chart_paths` | `reports/nexus_feedback/latest_nexus_feedback.md` | `reports/nexus_feedback/v0_4_5d/` |\n| v0.4.6 | Pair policy dry-run simulator | `python scripts/benchmarks/run_pair_policy_dry_run.py` | Simulates policy impact without classifier mutation | `reports/policy_dry_run/latest_pair_policy_dry_run.md` | `visuals/policy_dry_run/v0_4_6/` |\n")
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_6_pair_policy_dry_run_simulator.md", f"""# TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator

Generated: {GENERATED_AT}

## Purpose

Simulate pair-policy enforcement without changing classifier behavior.

## Adds

- `scripts/benchmarks/run_pair_policy_dry_run.py`
- `reports/policy_dry_run/`
- `visuals/policy_dry_run/v0_4_6/`

## Boundary

Dry-run simulation is local classifier governance only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.4.6 pair policy dry-run patch written")
