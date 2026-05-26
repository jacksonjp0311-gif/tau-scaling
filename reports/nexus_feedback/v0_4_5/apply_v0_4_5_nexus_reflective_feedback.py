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
        dest = ROOT / "reports" / "nexus_feedback" / "v0_4_5" / "backups" / f"{path.name}_before_v0_4_5_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhbm5vdGF0aW9ucwoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KT1VUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJuZXh1c19mZWVkYmFjayIKVklTX0RJUiA9IFJFUE9fUk9PVCAvICJ2aXN1YWxzIiAvICJuZXh1c19mZWVkYmFjayIgLyAidjBfNF81IgoKSU5QVVRTID0gewogICAgInJlbGVhc2VfcmVhZGluZXNzIjogUkVQT19ST09UIC8gInJlcG9ydHMiIC8gInJlbGVhc2UiIC8gImxhdGVzdF9yZWxlYXNlX3JlYWRpbmVzcy5qc29uIiwKICAgICJyZWFkbWVfYXVkaXQiOiBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicmVhZG1lIiAvICJsYXRlc3RfcmVhZG1lX21pbmlfcmVwb19hdWRpdC5qc29uIiwKICAgICJyY2NfbmV4dXMiOiBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicmNjX25leHVzIiAvICJsYXRlc3RfcmNjX25leHVzX2NoZWNrLmpzb24iLAogICAgInN5bnRoZXRpY19nYXRlX3N1aXRlIjogUkVQT19ST09UIC8gInJlcG9ydHMiIC8gImJlbmNobWFya3MiIC8gImxhdGVzdF9zeW50aGV0aWNfZ2F0ZV9zdWl0ZS5qc29uIiwKICAgICJzZW5zaXRpdml0eV9zd2VlcCI6IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJzZW5zaXRpdml0eSIgLyAibGF0ZXN0X3NlbnNpdGl2aXR5X3N3ZWVwLmpzb24iLAogICAgImdhdGVfaW50ZXJhY3Rpb25fbWF0cml4IjogUkVQT19ST09UIC8gInJlcG9ydHMiIC8gImludGVyYWN0aW9ucyIgLyAibGF0ZXN0X2dhdGVfaW50ZXJhY3Rpb25fbWF0cml4Lmpzb24iLAogICAgInRocmVzaG9sZF9leHBsYW5hdGlvbnMiOiBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAiZXhwbGFuYXRpb25zIiAvICJsYXRlc3RfdGhyZXNob2xkX2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iLAogICAgInBhaXJfcG9saWN5X3JldmlldyI6IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3kiIC8gImxhdGVzdF9wYWlyX3BvbGljeV9yZXZpZXcuanNvbiIsCn0KCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCkgLT4gZGljdFtzdHIsIEFueV06CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJfbWlzc2luZ19vcl9pbnZhbGlkIjogVHJ1ZSwgIl9wYXRoIjogc3RyKHBhdGgpLCAiX2Vycm9yIjogc3RyKGV4Yyl9CgpkZWYgcmVhZF90ZXh0KHBhdGg6IFBhdGgpIC0+IHN0cjoKICAgIHJldHVybiBwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiLCBlcnJvcnM9InJlcGxhY2UiKSBpZiBwYXRoLmV4aXN0cygpIGVsc2UgIiIKCmRlZiB3cml0ZV9qc29uKHBhdGg6IFBhdGgsIHBheWxvYWQ6IEFueSkgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKHBheWxvYWQsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHdyaXRlX3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKSAtPiBOb25lOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KHRleHQsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgYm9vbF9wYXNzKHBheWxvYWQ6IGRpY3Rbc3RyLCBBbnldKSAtPiBib29sOgogICAgcmV0dXJuIGJvb2wocGF5bG9hZC5nZXQoInBhc3NlZCIpIGlzIFRydWUpIGFuZCBub3QgcGF5bG9hZC5nZXQoIl9taXNzaW5nX29yX2ludmFsaWQiKQoKZGVmIGhlYWx0aF9zY29yZShpbnB1dHM6IGRpY3Rbc3RyLCBkaWN0W3N0ciwgQW55XV0pIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgcmVsZWFzZSA9IGlucHV0c1sicmVsZWFzZV9yZWFkaW5lc3MiXQogICAgcmVhZG1lID0gaW5wdXRzWyJyZWFkbWVfYXVkaXQiXQogICAgcmNjID0gaW5wdXRzWyJyY2NfbmV4dXMiXQogICAgc3ludGhldGljID0gaW5wdXRzWyJzeW50aGV0aWNfZ2F0ZV9zdWl0ZSJdCiAgICBzZW5zaXRpdml0eSA9IGlucHV0c1sic2Vuc2l0aXZpdHlfc3dlZXAiXQogICAgaW50ZXJhY3Rpb25zID0gaW5wdXRzWyJnYXRlX2ludGVyYWN0aW9uX21hdHJpeCJdCiAgICBleHBsYW5hdGlvbnMgPSBpbnB1dHNbInRocmVzaG9sZF9leHBsYW5hdGlvbnMiXQogICAgcG9saWN5ID0gaW5wdXRzWyJwYWlyX3BvbGljeV9yZXZpZXciXQoKICAgIHZhbGlkYXRpb25zID0gewogICAgICAgICJyZWxlYXNlX3JlYWRpbmVzcyI6IGJvb2xfcGFzcyhyZWxlYXNlKSBhbmQgcmVsZWFzZS5nZXQoInN0ZXBfZmFpbHVyZXMiLCAwKSA9PSAwIGFuZCByZWxlYXNlLmdldCgiZmluZGluZ3MiLCAwKSA9PSAwLAogICAgICAgICJyZWFkbWVfYXVkaXQiOiBib29sX3Bhc3MocmVhZG1lKSBhbmQgcmVhZG1lLmdldCgid2FybmluZ3MiLCAwKSA9PSAwIGFuZCByZWFkbWUuZ2V0KCJlcnJvcnMiLCAwKSA9PSAwLAogICAgICAgICJyY2NfbmV4dXMiOiBib29sX3Bhc3MocmNjKSBhbmQgcmNjLmdldCgid2FybmluZ3MiLCAwKSA9PSAwIGFuZCByY2MuZ2V0KCJlcnJvcnMiLCAwKSA9PSAwLAogICAgICAgICJzeW50aGV0aWNfc3VpdGUiOiBzeW50aGV0aWMuZ2V0KCJhbGxfc2NlbmFyaW9zX3Bhc3NlZCIpIGlzIFRydWUgYW5kIHN5bnRoZXRpYy5nZXQoImZhaWxlZF9zY2VuYXJpb3MiLCAxKSA9PSAwLAogICAgICAgICJzZW5zaXRpdml0eV9zd2VlcCI6IHNlbnNpdGl2aXR5LmdldCgidG90YWxfcG9pbnRzIiwgMCkgPj0gMjkgYW5kIHNlbnNpdGl2aXR5LmdldCgiY2hhcnRfY291bnQiLCAwKSA+PSAxMCwKICAgICAgICAiZ2F0ZV9pbnRlcmFjdGlvbnMiOiBpbnRlcmFjdGlvbnMuZ2V0KCJhbGxfcGFpcnNfZXhlY3V0ZWQiKSBpcyBUcnVlIGFuZCBpbnRlcmFjdGlvbnMuZ2V0KCJwYWlyX2NvdW50IiwgMCkgPT0gNTUsCiAgICAgICAgImV4cGxhbmF0aW9uX2NhcmRzIjogZXhwbGFuYXRpb25zLmdldCgiY2FyZF9jb3VudCIsIDApID49IDk0LAogICAgICAgICJwb2xpY3lfcmV2aWV3IjogcG9saWN5LmdldCgicGFpcl9jb3VudCIsIDApID09IDU1IGFuZCBwb2xpY3kuZ2V0KCJwb2xpY3lfZW5mb3JjZWQiKSBpcyBGYWxzZSwKICAgIH0KCiAgICBzY29yZSA9IHN1bSgxIGZvciB2IGluIHZhbGlkYXRpb25zLnZhbHVlcygpIGlmIHYpIC8gbGVuKHZhbGlkYXRpb25zKQogICAgcmV0dXJuIHsic2NvcmUiOiByb3VuZChzY29yZSwgNCksICJjaGVja3MiOiB2YWxpZGF0aW9ucywgInBhc3NlZCI6IHNjb3JlID09IDEuMH0KCmRlZiBmZWVkYmFja19zaWduYWxzKGlucHV0czogZGljdFtzdHIsIGRpY3Rbc3RyLCBBbnldXSkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICBzaWduYWxzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSA9IFtdCiAgICBwb2xpY3kgPSBpbnB1dHNbInBhaXJfcG9saWN5X3JldmlldyJdCiAgICBleHBsYW5hdGlvbnMgPSBpbnB1dHNbInRocmVzaG9sZF9leHBsYW5hdGlvbnMiXQogICAgcm91dGVfbWFwID0gcmVhZF9qc29uKFJFUE9fUk9PVCAvICJyY2MiIC8gIm5leHVzIiAvICJyb3V0ZV9tYXAuanNvbiIpCiAgICBhZ2VudHMgPSByZWFkX3RleHQoUkVQT19ST09UIC8gIkFHRU5UUy5tZCIpCiAgICByZWFkbWUgPSByZWFkX3RleHQoUkVQT19ST09UIC8gIlJFQURNRS5tZCIpCgogICAgcG9saWN5X2NvdW50cyA9IHBvbGljeS5nZXQoInBvbGljeV9jb3VudHMiLCB7fSkKICAgIHBhaXJfY291bnQgPSBtYXgoMSwgaW50KHBvbGljeS5nZXQoInBhaXJfY291bnQiLCAxKSkpCiAgICBlc2NhbGF0aW9uID0gaW50KHBvbGljeV9jb3VudHMuZ2V0KCJUU0VLLURfQ0FORElEQVRFIiwgMCkpICsgaW50KHBvbGljeV9jb3VudHMuZ2V0KCJIVU1BTl9SRVZJRVciLCAwKSkgKyBpbnQocG9saWN5X2NvdW50cy5nZXQoIlRTRUstRV9DQU5ESURBVEUiLCAwKSkKICAgIGVzY2FsYXRpb25fcmF0aW8gPSBlc2NhbGF0aW9uIC8gcGFpcl9jb3VudAoKICAgIHNpZ25hbHMuYXBwZW5kKHsKICAgICAgICAiaWQiOiAiTkYtMDAxIiwKICAgICAgICAic3VyZmFjZSI6ICJwYWlyX3BvbGljeSIsCiAgICAgICAgInNldmVyaXR5IjogImhpZ2giIGlmIGVzY2FsYXRpb25fcmF0aW8gPj0gMC4xNSBlbHNlICJtZWRpdW0iIGlmIGVzY2FsYXRpb25fcmF0aW8gPiAwIGVsc2UgImxvdyIsCiAgICAgICAgInNpZ25hbCI6ICJwYWlyX3BvbGljeV9lc2NhbGF0aW9uX3ByZXNzdXJlIiwKICAgICAgICAiZXZpZGVuY2UiOiB7CiAgICAgICAgICAgICJwYWlyX2NvdW50IjogcGFpcl9jb3VudCwKICAgICAgICAgICAgInBvbGljeV9jb3VudHMiOiBwb2xpY3lfY291bnRzLAogICAgICAgICAgICAiZXNjYWxhdGlvbl9yYXRpbyI6IHJvdW5kKGVzY2FsYXRpb25fcmF0aW8sIDQpLAogICAgICAgIH0sCiAgICAgICAgInJlY29tbWVuZGF0aW9uIjogIlJ1biBhIGRyeS1ydW4gc2ltdWxhdG9yIGJlZm9yZSBlbmZvcmNpbmcgcGFpci1wb2xpY3kgY2hhbmdlcy4iLAogICAgICAgICJ0YXJnZXRfbmV4dCI6ICJUQVUtU0NBTElORy1TQSB2MC40LjYgLSBQYWlyIFBvbGljeSBEcnktUnVuIFNpbXVsYXRvciIsCiAgICB9KQoKICAgIHJldmlld19jb3VudHMgPSBleHBsYW5hdGlvbnMuZ2V0KCJyZXZpZXdfY291bnRzIiwge30pCiAgICBoYXJkX3JlamVjdF93aXRob3V0X2ZpbmRpbmcgPSBpbnQocmV2aWV3X2NvdW50cy5nZXQoImhhcmRfcmVqZWN0X3dpdGhvdXRfZmluZGluZyIsIDApKQogICAgc2lnbmFscy5hcHBlbmQoewogICAgICAgICJpZCI6ICJORi0wMDIiLAogICAgICAgICJzdXJmYWNlIjogImV4cGxhbmF0aW9ucyIsCiAgICAgICAgInNldmVyaXR5IjogIm1lZGl1bSIgaWYgaGFyZF9yZWplY3Rfd2l0aG91dF9maW5kaW5nIGVsc2UgImxvdyIsCiAgICAgICAgInNpZ25hbCI6ICJoYXJkX3JlamVjdF93aXRob3V0X2ZpbmRpbmciLAogICAgICAgICJldmlkZW5jZSI6IHsiY291bnQiOiBoYXJkX3JlamVjdF93aXRob3V0X2ZpbmRpbmcsICJyZXZpZXdfY291bnRzIjogcmV2aWV3X2NvdW50c30sCiAgICAgICAgInJlY29tbWVuZGF0aW9uIjogIkFkZCBleHBsaWNpdCBmaW5kaW5nIHByb3ZlbmFuY2UgZm9yIGFueSBUU0VLLUUgY29sbGFwc2UgcGF0aCB0aGF0IGN1cnJlbnRseSBlbWl0cyBubyBmaW5kaW5nIGNvZGUuIiwKICAgICAgICAidGFyZ2V0X25leHQiOiAiRGlhZ25vc3RpYyBmaW5kaW5nIHByb3ZlbmFuY2UgcmVwYWlyIiwKICAgIH0pCgogICAgc3RhbGVfYWdlbnRzX3J1bGUgPSAiIyMgdjAuNC4xIFNlbnNpdGl2aXR5LVN3ZWVwIFN0YXJ0IFJ1bGUiIGluIGFnZW50cwogICAgc2lnbmFscy5hcHBlbmQoewogICAgICAgICJpZCI6ICJORi0wMDMiLAogICAgICAgICJzdXJmYWNlIjogImFnZW50X2NvbnRyYWN0IiwKICAgICAgICAic2V2ZXJpdHkiOiAibWVkaXVtIiBpZiBzdGFsZV9hZ2VudHNfcnVsZSBlbHNlICJsb3ciLAogICAgICAgICJzaWduYWwiOiAic3RhbGVfc3BlY2lmaWNfc3RhcnRfcnVsZSIgaWYgc3RhbGVfYWdlbnRzX3J1bGUgZWxzZSAiYWdlbnRfY29udHJhY3RfY3VycmVudCIsCiAgICAgICAgImV2aWRlbmNlIjogeyJmb3VuZF92MF80XzFfc3BlY2lmaWNfcnVsZSI6IHN0YWxlX2FnZW50c19ydWxlfSwKICAgICAgICAicmVjb21tZW5kYXRpb24iOiAiR2VuZXJhbGl6ZSB0aGUgQUdFTlRTIGV4cGVyaW1lbnQtc3RhcnQgcnVsZSBzbyBmdXR1cmUgbGF5ZXJzIGRvIG5vdCBjYXJyeSBzdGFsZSB2ZXJzaW9uLXNwZWNpZmljIGxhbmd1YWdlLiIsCiAgICAgICAgInRhcmdldF9uZXh0IjogIkFnZW50IGNvbnRyYWN0IGZlZWRiYWNrIHN5bmMiLAogICAgfSkKCiAgICBmZWVkYmFja19yb3V0ZV9leGlzdHMgPSAibmV4dXNfZmVlZGJhY2siIGluIHJvdXRlX21hcC5nZXQoInYwXzRfcm91dGVzIiwge30pCiAgICBzaWduYWxzLmFwcGVuZCh7CiAgICAgICAgImlkIjogIk5GLTAwNCIsCiAgICAgICAgInN1cmZhY2UiOiAicmNjX25leHVzIiwKICAgICAgICAic2V2ZXJpdHkiOiAibG93IiBpZiBmZWVkYmFja19yb3V0ZV9leGlzdHMgZWxzZSAibWVkaXVtIiwKICAgICAgICAic2lnbmFsIjogImZlZWRiYWNrX3JvdXRlX3ByZXNlbnQiIGlmIGZlZWRiYWNrX3JvdXRlX2V4aXN0cyBlbHNlICJmZWVkYmFja19yb3V0ZV9taXNzaW5nIiwKICAgICAgICAiZXZpZGVuY2UiOiB7InJvdXRlX2V4aXN0cyI6IGZlZWRiYWNrX3JvdXRlX2V4aXN0c30sCiAgICAgICAgInJlY29tbWVuZGF0aW9uIjogIktlZXAgYSByb3V0ZS1tYXAgZW50cnkgZm9yIE5leHVzIGZlZWRiYWNrIHNvIGFnZW50cyBrbm93IHdoZXJlIHJlZmxlY3RpdmUgcmVwb3J0cyBsaXZlLiIsCiAgICAgICAgInRhcmdldF9uZXh0IjogIlJvdXRlLW1hcCBmZWVkYmFjayBjb250aW51aXR5IiwKICAgIH0pCgogICAgZmVlZGJhY2tfY29tbWFuZF9pbl9yZWFkbWUgPSAicHl0aG9uIHNjcmlwdHMvZmVlZGJhY2svcnVuX25leHVzX2ZlZWRiYWNrLnB5IiBpbiByZWFkbWUKICAgIHNpZ25hbHMuYXBwZW5kKHsKICAgICAgICAiaWQiOiAiTkYtMDA1IiwKICAgICAgICAic3VyZmFjZSI6ICJyZWFkbWUiLAogICAgICAgICJzZXZlcml0eSI6ICJsb3ciIGlmIGZlZWRiYWNrX2NvbW1hbmRfaW5fcmVhZG1lIGVsc2UgIm1lZGl1bSIsCiAgICAgICAgInNpZ25hbCI6ICJmZWVkYmFja19jb21tYW5kX3ByZXNlbnQiIGlmIGZlZWRiYWNrX2NvbW1hbmRfaW5fcmVhZG1lIGVsc2UgImZlZWRiYWNrX2NvbW1hbmRfbWlzc2luZyIsCiAgICAgICAgImV2aWRlbmNlIjogeyJjb21tYW5kX3ByZXNlbnQiOiBmZWVkYmFja19jb21tYW5kX2luX3JlYWRtZX0sCiAgICAgICAgInJlY29tbWVuZGF0aW9uIjogIkV4cG9zZSBOZXh1cyBmZWVkYmFjayBhcyBhIGZpcnN0LWNsYXNzIFJFQURNRSBjb21tYW5kLiIsCiAgICAgICAgInRhcmdldF9uZXh0IjogIlJFQURNRSBmZWVkYmFjayBjb21tYW5kIHN5bmMiLAogICAgfSkKCiAgICByZXR1cm4gc2lnbmFscwoKZGVmIHByaW9yaXRpZXMoc2lnbmFsczogbGlzdFtkaWN0W3N0ciwgQW55XV0pIC0+IGxpc3RbZGljdFtzdHIsIEFueV1dOgogICAgd2VpZ2h0ID0geyJoaWdoIjogMywgIm1lZGl1bSI6IDIsICJsb3ciOiAxfQogICAgb3JkZXJlZCA9IHNvcnRlZChzaWduYWxzLCBrZXk9bGFtYmRhIHM6ICgtd2VpZ2h0LmdldChzWyJzZXZlcml0eSJdLCAwKSwgc1siaWQiXSkpCiAgICByZXR1cm4gWwogICAgICAgIHsKICAgICAgICAgICAgInJhbmsiOiBpICsgMSwKICAgICAgICAgICAgImlkIjogc1siaWQiXSwKICAgICAgICAgICAgInN1cmZhY2UiOiBzWyJzdXJmYWNlIl0sCiAgICAgICAgICAgICJzZXZlcml0eSI6IHNbInNldmVyaXR5Il0sCiAgICAgICAgICAgICJzaWduYWwiOiBzWyJzaWduYWwiXSwKICAgICAgICAgICAgInJlY29tbWVuZGF0aW9uIjogc1sicmVjb21tZW5kYXRpb24iXSwKICAgICAgICAgICAgInRhcmdldF9uZXh0Ijogc1sidGFyZ2V0X25leHQiXSwKICAgICAgICB9CiAgICAgICAgZm9yIGksIHMgaW4gZW51bWVyYXRlKG9yZGVyZWQpCiAgICBdCgpkZWYgZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnk6IGRpY3Rbc3RyLCBBbnldKSAtPiBsaXN0W3N0cl06CiAgICBwYXRoczogbGlzdFtzdHJdID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIGYibWF0cGxvdGxpYiB1bmF2YWlsYWJsZToge2V4Y31cbiIpCiAgICAgICAgcmV0dXJuIHBhdGhzCgogICAgVklTX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmVmaWcocGF0aDogUGF0aCkgLT4gTm9uZToKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwYXRoLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHN0cihwYXRoLnJlbGF0aXZlX3RvKFJFUE9fUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSkKCiAgICAjIFZhbGlkYXRpb24gaGVhbHRoIGJhcnMuCiAgICBjaGVja3MgPSBzdW1tYXJ5WyJoZWFsdGgiXVsiY2hlY2tzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKQogICAgcGx0LmJhcihsaXN0KGNoZWNrcy5rZXlzKCkpLCBbMSBpZiB2IGVsc2UgMCBmb3IgdiBpbiBjaGVja3MudmFsdWVzKCldKQogICAgcGx0LnlsaW0oMCwgMS4xKQogICAgcGx0LnlsYWJlbCgiUGFzcyA9IDEiKQogICAgcGx0LnRpdGxlKCJOZXh1cyBWYWxpZGF0aW9uIEhlYWx0aCBTdXJmYWNlIikKICAgIHBsdC54dGlja3Mocm90YXRpb249NDUsIGhhPSJyaWdodCIsIGZvbnRzaXplPTgpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAibmV4dXNfdmFsaWRhdGlvbl9oZWFsdGgucG5nIikKCiAgICAjIEZlZWRiYWNrIHNldmVyaXR5IGNvdW50cy4KICAgIHNldl9jb3VudHM6IGRpY3Rbc3RyLCBpbnRdID0ge30KICAgIGZvciBzIGluIHN1bW1hcnlbInNpZ25hbHMiXToKICAgICAgICBzZXZfY291bnRzW3NbInNldmVyaXR5Il1dID0gc2V2X2NvdW50cy5nZXQoc1sic2V2ZXJpdHkiXSwgMCkgKyAxCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDYsIDQpKQogICAgcGx0LmJhcihsaXN0KHNldl9jb3VudHMua2V5cygpKSwgbGlzdChzZXZfY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC50aXRsZSgiTmV4dXMgRmVlZGJhY2sgU2V2ZXJpdHkgQ291bnRzIikKICAgIHBsdC55bGFiZWwoIlNpZ25hbCBjb3VudCIpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAibmV4dXNfZmVlZGJhY2tfc2V2ZXJpdHlfY291bnRzLnBuZyIpCgogICAgIyBQcmlvcml0eSByYW5rIGNoYXJ0LgogICAgcHIgPSBzdW1tYXJ5WyJwcmlvcml0aWVzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKQogICAgcGx0LmJhcihbcFsiaWQiXSBmb3IgcCBpbiBwcl0sIGxpc3QocmFuZ2UobGVuKHByKSwgMCwgLTEpKSkKICAgIHBsdC50aXRsZSgiTmV4dXMgSW1wcm92ZW1lbnQgUHJpb3JpdHkgU3RhY2siKQogICAgcGx0LnlsYWJlbCgiUmVsYXRpdmUgcHJpb3JpdHkiKQogICAgc2F2ZWZpZyhWSVNfRElSIC8gIm5leHVzX3ByaW9yaXR5X3N0YWNrLnBuZyIpCgogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVuZGVyX21hcmtkb3duKHN1bW1hcnk6IGRpY3Rbc3RyLCBBbnldKSAtPiBzdHI6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC40LjUgTmV4dXMgUmVmbGVjdGl2ZSBGZWVkYmFjayBMb29wIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSGVhbHRoIHNjb3JlOiBge3N1bW1hcnlbJ2hlYWx0aCddWydzY29yZSddfWAiLAogICAgICAgIGYiLSBIZWFsdGggcGFzc2VkOiBge3N1bW1hcnlbJ2hlYWx0aCddWydwYXNzZWQnXX1gIiwKICAgICAgICBmIi0gRmVlZGJhY2sgc2lnbmFsIGNvdW50OiBge2xlbihzdW1tYXJ5WydzaWduYWxzJ10pfWAiLAogICAgICAgIGYiLSBDaGFydCBjb3VudDogYHtsZW4oc3VtbWFyeVsnY2hhcnRfcGF0aHMnXSl9YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEhlYWx0aCBDaGVja3MiLAogICAgICAgICIiLAogICAgICAgICJ8IENoZWNrIHwgUGFzc2VkIHwiLAogICAgICAgICJ8LS0tfC0tLTp8IiwKICAgIF0KICAgIGZvciBrLCB2IGluIHN1bW1hcnlbImhlYWx0aCJdWyJjaGVja3MiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCBge3Z9YCB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEltcHJvdmVtZW50IFByaW9yaXRpZXMiLAogICAgICAgICIiLAogICAgICAgICJ8IFJhbmsgfCBTaWduYWwgfCBTZXZlcml0eSB8IFN1cmZhY2UgfCBSZWNvbW1lbmRhdGlvbiB8IFRhcmdldCBuZXh0IHwiLAogICAgICAgICJ8LS0tOnwtLS18LS0tfC0tLXwtLS18LS0tfCIsCiAgICBdCiAgICBmb3IgcCBpbiBzdW1tYXJ5WyJwcmlvcml0aWVzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCB7cFsncmFuayddfSB8IGB7cFsnc2lnbmFsJ119YCB8IGB7cFsnc2V2ZXJpdHknXX1gIHwgYHtwWydzdXJmYWNlJ119YCB8IHtwWydyZWNvbW1lbmRhdGlvbiddfSB8IHtwWyd0YXJnZXRfbmV4dCddfSB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEZlZWRiYWNrIFNpZ25hbHMiLAogICAgICAgICIiLAogICAgICAgICJ8IElEIHwgU3VyZmFjZSB8IFNldmVyaXR5IHwgU2lnbmFsIHwgRXZpZGVuY2UgfCBSZWNvbW1lbmRhdGlvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwtLS18LS0tfCIsCiAgICBdCiAgICBmb3IgcyBpbiBzdW1tYXJ5WyJzaWduYWxzIl06CiAgICAgICAgZXYgPSBqc29uLmR1bXBzKHNbImV2aWRlbmNlIl0sIHNvcnRfa2V5cz1UcnVlKS5yZXBsYWNlKCJ8IiwgIlxcfCIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3NbJ2lkJ119YCB8IGB7c1snc3VyZmFjZSddfWAgfCBge3NbJ3NldmVyaXR5J119YCB8IGB7c1snc2lnbmFsJ119YCB8IGB7ZXZ9YCB8IHtzWydyZWNvbW1lbmRhdGlvbiddfSB8IikKCiAgICBsaW5lcyArPSBbIiIsICIjIyBDaGFydHMiLCAiIl0KICAgIGZvciBjaGFydCBpbiBzdW1tYXJ5WyJjaGFydF9wYXRocyJdOgogICAgICAgIHJlbCA9IG9zLnBhdGgucmVscGF0aChSRVBPX1JPT1QgLyBjaGFydCwgT1VUX0RJUikucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgbGluZXMgKz0gW2YiIVt7UGF0aChjaGFydCkuc3RlbX1dKHtyZWx9KSIsICIiXQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIyMgQm91bmRhcnkiLAogICAgICAgICIiLAogICAgICAgIHN1bW1hcnlbImJvdW5kYXJ5Il0sCiAgICAgICAgIiIsCiAgICBdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKSAtPiBOb25lOgogICAgaW5wdXRzID0ge25hbWU6IHJlYWRfanNvbihwYXRoKSBmb3IgbmFtZSwgcGF0aCBpbiBJTlBVVFMuaXRlbXMoKX0KICAgIGhlYWx0aCA9IGhlYWx0aF9zY29yZShpbnB1dHMpCiAgICBzaWduYWxzID0gZmVlZGJhY2tfc2lnbmFscyhpbnB1dHMpCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctbmV4dXMtcmVmbGVjdGl2ZS1mZWVkYmFjay12MC40LjUiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRzIjoge2s6IHN0cih2LnJlbGF0aXZlX3RvKFJFUE9fUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSBmb3IgaywgdiBpbiBJTlBVVFMuaXRlbXMoKX0sCiAgICAgICAgImhlYWx0aCI6IGhlYWx0aCwKICAgICAgICAic2lnbmFscyI6IHNpZ25hbHMsCiAgICAgICAgInByaW9yaXRpZXMiOiBwcmlvcml0aWVzKHNpZ25hbHMpLAogICAgICAgICJib3VuZGFyeSI6ICJOZXh1cyBmZWVkYmFjayBpcyByZXBvc2l0b3J5IHNlbGYtb2JzZXJ2YXRpb24gYW5kIGltcHJvdmVtZW50IHByaW9yaXRpemF0aW9uIG9ubHkuIEl0IGRvZXMgbm90IG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yIGFuZCBkb2VzIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBBSSB1bmRlcnN0YW5kaW5nLCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICB9CiAgICBjaGFydHMgPSBnZW5lcmF0ZV9jaGFydHMoc3VtbWFyeSkKICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMKCiAgICBPVVRfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHdyaXRlX2pzb24oT1VUX0RJUiAvICJuZXh1c19mZWVkYmFja192MF80XzUuanNvbiIsIHN1bW1hcnkpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAibGF0ZXN0X25leHVzX2ZlZWRiYWNrLmpzb24iLCBzdW1tYXJ5KQogICAgbWQgPSByZW5kZXJfbWFya2Rvd24oc3VtbWFyeSkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJuZXh1c19mZWVkYmFja192MF80XzUubWQiLCBtZCkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJsYXRlc3RfbmV4dXNfZmVlZGJhY2subWQiLCBtZCkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImhlYWx0aF9zY29yZSI6IHN1bW1hcnlbImhlYWx0aCJdWyJzY29yZSJdLAogICAgICAgICJoZWFsdGhfcGFzc2VkIjogc3VtbWFyeVsiaGVhbHRoIl1bInBhc3NlZCJdLAogICAgICAgICJzaWduYWxfY291bnQiOiBsZW4oc3VtbWFyeVsic2lnbmFscyJdKSwKICAgICAgICAicHJpb3JpdGllcyI6IHN1bW1hcnlbInByaW9yaXRpZXMiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL25leHVzX2ZlZWRiYWNrL2xhdGVzdF9uZXh1c19mZWVkYmFjay5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo="
runner_text = base64.b64decode(runner_b64.encode("ascii")).decode("utf-8")
write(ROOT / "scripts" / "feedback" / "run_nexus_feedback.py", runner_text)

write(ROOT / "docs" / "feedback" / "README.md", """# Nexus Feedback Documentation

Current layer: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**

## Purpose

This folder documents the reflective feedback loop: the repository reads its latest validation, benchmark, explanation, and policy outputs, then emits improvement priorities.

## README Update Rule

Update this mini README whenever feedback logic, feedback surfaces, or reflection boundaries change.

Boundary: Nexus feedback is repository self-observation only. It is not AI understanding or external validation.
""")

write(ROOT / "reports" / "nexus_feedback" / "README.md", """# Nexus Feedback Reports

Current layer: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**

## Purpose

This folder stores self-observation reports generated from the latest release, RCC, README, benchmark, explanation, and pair-policy surfaces.

## Primary command

```powershell
python scripts/feedback/run_nexus_feedback.py
```

## README Update Rule

Update this mini README whenever feedback report schemas, inputs, or priority rules change.

Boundary: feedback reports prioritize local repo improvements only.
""")

write(ROOT / "visuals" / "nexus_feedback" / "README.md", """# Nexus Feedback Visuals

Current layer: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**

## Purpose

This folder stores charts generated by the Nexus feedback loop.

## README Update Rule

Update this mini README whenever feedback charts or chart meanings change.

Boundary: feedback visuals are local repository self-observation only.
""")

write(ROOT / "visuals" / "nexus_feedback" / "v0_4_5" / "README.md", """# v0.4.5 Nexus Feedback Charts

## Expected Charts

- `nexus_validation_health.png`
- `nexus_feedback_severity_counts.png`
- `nexus_priority_stack.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local repository feedback diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.4[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.3[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.4 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.5 |", r)

if "| Nexus feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |" not in r:
    r = r.replace(
        "| Pair policy charts | `visuals/policy/v0_4_4/` |\n",
        "| Pair policy charts | `visuals/policy/v0_4_4/` |\n| Nexus feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |\n| Nexus feedback charts | `visuals/nexus_feedback/v0_4_5/` |\n",
    )

if "python scripts/feedback/run_nexus_feedback.py" not in r:
    r = r.replace(
        "python scripts/benchmarks/run_pair_policy_review.py\npython scripts/release/validate_release.py",
        "python scripts/benchmarks/run_pair_policy_review.py\npython scripts/feedback/run_nexus_feedback.py\npython scripts/release/validate_release.py",
    )

section = """## Nexus Reflective Feedback Loop v0.4.5

v0.4.5 lets the repository read its own latest outputs and emit improvement priorities.

Primary command:

```powershell
python scripts/feedback/run_nexus_feedback.py
```

Primary outputs:

```text
reports/nexus_feedback/latest_nexus_feedback.json
reports/nexus_feedback/latest_nexus_feedback.md
visuals/nexus_feedback/v0_4_5/
```

The feedback loop reads:

```text
release readiness
README audit
RCC-N checker
synthetic gate suite
sensitivity sweep
gate interaction matrix
threshold explanation cards
pair policy review
```

The purpose is to answer:

```text
What is healthy?
What is producing policy pressure?
What should be improved next?
What should not be mutated yet?
```

This creates a reflective Nexus surface: the system does not merely generate reports; it turns its reports into ranked improvement signals.

Boundary: Nexus feedback is repository self-observation and improvement prioritization only. It does not mutate classifier behavior and does not validate silicon, products, manufacturing, process nodes, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Nexus Reflective Feedback Loop v0.4.5" not in r:
    r = r.replace("## Pair Policy Review Gate v0.4.4", section + "## Pair Policy Review Gate v0.4.4", 1)

if "    feedback/" not in r:
    r = r.replace("  docs/\n    architecture/", "  docs/\n    feedback/\n    architecture/")
    r = r.replace("  reports/\n    policy/", "  reports/\n    nexus_feedback/\n    policy/")
    r = r.replace("  scripts/\n    benchmarks/", "  scripts/\n    feedback/\n    benchmarks/")
    r = r.replace("  visuals/\n    policy/", "  visuals/\n    nexus_feedback/\n    policy/")

lesson = "| L-023 | v0.4.4 created policy candidates but the repo still needed a way to turn outputs into improvement priorities. | Validation, benchmark, explanation, and policy reports were readable, but not yet synthesized into a feedback surface for the next agent. | Every mature runtime should emit a Nexus feedback report that ranks improvement targets without mutating classifier behavior. |"
if lesson not in r:
    r = r.replace(
        "| L-022 | v0.4.3 produced 55 `review_pair_policy` cards and 1 `hard_reject_without_finding` card. | Explanation cards successfully exposed classifier-policy questions without mutating classifier behavior. | Pair-policy changes must pass through a non-enforcing policy review layer and then a dry-run simulator before classifier enforcement. |\n",
        "| L-022 | v0.4.3 produced 55 `review_pair_policy` cards and 1 `hard_reject_without_finding` card. | Explanation cards successfully exposed classifier-policy questions without mutating classifier behavior. | Pair-policy changes must pass through a non-enforcing policy review layer and then a dry-run simulator before classifier enforcement. |\n" + lesson + "\n",
    )

if "| v0.4.5 | Nexus reflective feedback loop for ranked improvement signals. |" not in r:
    r = r.replace(
        "| v0.4.4 | Pair policy review gate for non-enforcing classifier-governance candidates. |\n",
        "| v0.4.4 | Pair policy review gate for non-enforcing classifier-governance candidates. |\n| v0.4.5 | Nexus reflective feedback loop for ranked improvement signals. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.6 - Pair Policy Dry-Run Simulator**

Recommended goals:

- Simulate policy-class changes without mutating the classifier.
- Compare current class vs proposed policy class.
- Emit drift impact charts.
- Decide whether policy enforcement is safe.
- Preserve non-claim locks: dry-run policy simulation is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS update.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.4[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**",
    a,
)
if "python scripts/feedback/run_nexus_feedback.py" not in a:
    a = a.replace(
        "python scripts/benchmarks/run_pair_policy_review.py\npython -m unittest discover -s tests",
        "python scripts/benchmarks/run_pair_policy_review.py\npython scripts/feedback/run_nexus_feedback.py\npython -m unittest discover -s tests",
    )
a = a.replace("## v0.4.1 Sensitivity-Sweep Start Rule", "## v0.4+ Experiment Start Rule")
a = a.replace("Do not begin or promote v0.4.1 Synthetic Gate Sensitivity Sweep work unless:", "Do not begin or promote any v0.4+ experimental layer unless:")
if "Nexus feedback patch" not in a:
    a = a.replace(
        "| Pair policy patch | `reports/policy/`, `visuals/policy/`, explanation cards | release validator + policy review report; no classifier mutation |\n",
        "| Pair policy patch | `reports/policy/`, `visuals/policy/`, explanation cards | release validator + policy review report; no classifier mutation |\n| Nexus feedback patch | `scripts/feedback/`, `reports/nexus_feedback/`, `visuals/nexus_feedback/` | release validator + Nexus feedback report; no classifier mutation |\n",
    )
write(agents, a)

# task matrix update.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.4[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop**",
    m,
)
if "| Nexus feedback patch |" not in m:
    m = m.replace(
        "| Pair policy patch | outer | validation | governance | `reports/policy/`, explanation cards, interaction matrix | release validator + policy review report | `reports/policy/latest_pair_policy_review.md` |\n",
        "| Pair policy patch | outer | validation | governance | `reports/policy/`, explanation cards, interaction matrix | release validator + policy review report | `reports/policy/latest_pair_policy_review.md` |\n| Nexus feedback patch | outer | drift | agent | `scripts/feedback/`, `reports/nexus_feedback/`, latest reports | release validator + feedback report | `reports/nexus_feedback/latest_nexus_feedback.md` |\n",
    )
write(matrix, m)

# route map update.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.5"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["nexus_feedback"] = {
    "read_first": [
        "reports/release/latest_release_readiness.json",
        "reports/readme/latest_readme_mini_repo_audit.json",
        "reports/rcc_nexus/latest_rcc_nexus_check.json",
        "reports/benchmarks/latest_synthetic_gate_suite.json",
        "reports/sensitivity/latest_sensitivity_sweep.json",
        "reports/interactions/latest_gate_interaction_matrix.json",
        "reports/explanations/latest_threshold_explanation_cards.json",
        "reports/policy/latest_pair_policy_review.json"
    ],
    "validate": [
        "python scripts/feedback/run_nexus_feedback.py",
        "python scripts/release/validate_release.py"
    ],
    "evidence": [
        "reports/nexus_feedback/latest_nexus_feedback.md",
        "visuals/nexus_feedback/v0_4_5/"
    ],
    "mutation_lock": "Does not change classifier behavior; emits improvement priorities only."
}
write_json(route_path, route)

# benchmark atlas / docs index update.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.5 | Nexus reflective feedback |" not in t:
    t = t.replace(
        "| v0.4.4 | Pair policy review gate | `python scripts/benchmarks/run_pair_policy_review.py` | Non-enforcing pair-policy table based on explanation-card review labels | `reports/policy/latest_pair_policy_review.md` | `visuals/policy/v0_4_4/` |\n",
        "| v0.4.4 | Pair policy review gate | `python scripts/benchmarks/run_pair_policy_review.py` | Non-enforcing pair-policy table based on explanation-card review labels | `reports/policy/latest_pair_policy_review.md` | `visuals/policy/v0_4_4/` |\n| v0.4.5 | Nexus reflective feedback | `python scripts/feedback/run_nexus_feedback.py` | Synthesizes latest reports into ranked improvement signals | `reports/nexus_feedback/latest_nexus_feedback.md` | `visuals/nexus_feedback/v0_4_5/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_5_nexus_reflective_feedback_loop.md", f"""# TAU-SCALING-SA v0.4.5 - Nexus Reflective Feedback Loop

Generated: {GENERATED_AT}

## Purpose

Let the repository synthesize its own latest reports into ranked improvement signals.

## Additions

- `scripts/feedback/run_nexus_feedback.py`
- `docs/feedback/`
- `reports/nexus_feedback/`
- `visuals/nexus_feedback/v0_4_5/`
- README/AGENTS/route-map/task-matrix/benchmark-atlas updates.

## Mutation Lock

This version does not alter classifier behavior.

## Boundary

Nexus feedback is repository self-observation and improvement prioritization only. It does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "nexus_feedback" / "v0_4_5" / "latest_v0_4_5_status.md", f"""# Tau Scaling v0.4.5 Nexus Feedback Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary command:

```powershell
python scripts/feedback/run_nexus_feedback.py
```
""")

print("v0.4.5 Nexus reflective feedback loop patch written")
