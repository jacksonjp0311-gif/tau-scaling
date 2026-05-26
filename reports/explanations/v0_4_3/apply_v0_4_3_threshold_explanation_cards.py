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
        dest = ROOT / "reports" / "explanations" / "v0_4_3" / "backups" / f"{path.name}_before_v0_4_3_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhbm5vdGF0aW9ucwoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KT1VUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJleHBsYW5hdGlvbnMiCkNBUkRfRElSID0gT1VUX0RJUiAvICJjYXJkcyIgLyAidjBfNF8zIgpWSVNfRElSID0gUkVQT19ST09UIC8gInZpc3VhbHMiIC8gImV4cGxhbmF0aW9ucyIgLyAidjBfNF8zIgoKU09VUkNFUyA9IHsKICAgICJzeW50aGV0aWNfZ2F0ZV9zdWl0ZSI6IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJiZW5jaG1hcmtzIiAvICJsYXRlc3Rfc3ludGhldGljX2dhdGVfc3VpdGUuanNvbiIsCiAgICAic2Vuc2l0aXZpdHlfc3dlZXAiOiBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAic2Vuc2l0aXZpdHkiIC8gImxhdGVzdF9zZW5zaXRpdml0eV9zd2VlcC5qc29uIiwKICAgICJnYXRlX2ludGVyYWN0aW9uX21hdHJpeCI6IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJpbnRlcmFjdGlvbnMiIC8gImxhdGVzdF9nYXRlX2ludGVyYWN0aW9uX21hdHJpeC5qc29uIiwKfQoKQ0xBU1NfUkFOSyA9IHsiVFNFSy1FIjogMCwgIlRTRUstRCI6IDEsICJUU0VLLUMiOiAyLCAiVFNFSy1CIjogMywgIlRTRUstQSI6IDR9CgpHQVRFX1JFUEFJUlMgPSB7CiAgICAiVFNFS19CX3NvdXJjZV9NSVNTSU5HIjogIkRlY2xhcmUgc291cmNlIGJvdW5kYXJ5IGFuZCBzZXBhcmF0ZSByZXBvcnRlZCBjbGFpbXMgZnJvbSB2YWxpZGF0aW9uLiIsCiAgICAiVFNFS19CX21ldHJpY19NSVNTSU5HIjogIkFkZCBhIG1lYXN1cmFibGUgY2xhaW0gdGV4dC90eXBlIGFuZCBtZXRyaWMgZGVmaW5pdGlvbi4iLAogICAgIlRTRUtfQl9iYXNlbGluZV9NSVNTSU5HIjogIkFkZCBleHBsaWNpdCBiYXNlbGluZSBtYW5pZmVzdCBhbmQgYmFzZWxpbmUgdGF1IHZlY3Rvci4iLAogICAgIlRTRUtfQl9tZXRob2RfTUlTU0lORyI6ICJEaXNjbG9zZSBtZXRob2QgYW5kIHlpZWxkIG1ldGhvZG9sb2d5LiIsCiAgICAiVFNFS19CX3dvcmtsb2FkX01JU1NJTkciOiAiRGVjbGFyZSB3b3JrbG9hZCBjbGFzcyBhbmQgZG9taW5hbnQgdGF1IHRlcm0uIiwKICAgICJUU0VLX0JfdGF1X01JU1NJTkciOiAiRGVjbGFyZSB0YXUgd2VpZ2h0cyBhbmQgZG9taW5hbnQgdGF1IGltcHJvdmVtZW50LiIsCiAgICAiVFNFS19CX0xGX01JU1NJTkciOiAiUmVzdG9yZSBwb3NpdGl2ZSBMb2dpY0ZvbGRpbmcgc3Vydml2YWJpbGl0eSBtYXJnaW4uIiwKICAgICJUU0VLX0JfRVRQX01JU1NJTkciOiAiSW1wcm92ZSBlbmVyZ3kvdGhlcm1hbC9QRE4tbm9ybWFsaXplZCB0YXUgZ2FpbiBhYm92ZSB0aHJlc2hvbGQuIiwKICAgICJUU0VLX0JfUFZUX01JU1NJTkciOiAiUHJvdmlkZSBjbG9zdXJlLCBQVlQsIGFuZCBQRE4gZXZpZGVuY2UuIiwKICAgICJUU0VLX0JfeWllbGRfTUlTU0lORyI6ICJSZXBvcnQgeWllbGQgb3IgZG93bmdyYWRlIHRoZSBjbGFpbS4iLAogICAgIlRTRUtfQl9ldmlkZW5jZV9NSVNTSU5HIjogIkNvbXBsZXRlIHRoZSBldmlkZW5jZSBwYWNrYWdlLiIsCiAgICAiVFNFS19PVkVSQ0xBSU1fSU5ERVBFTkRFTlRfVkFMSURBVElPTiI6ICJSZW1vdmUgaW5kZXBlbmRlbnQtdmFsaWRhdGlvbiBjbGFpbSBvciBwcm92aWRlIGluZGVwZW5kZW50IHZhbGlkYXRpb24gZXZpZGVuY2UuIiwKfQoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuIHt9CgpkZWYgd3JpdGVfanNvbihwYXRoOiBQYXRoLCBwYXlsb2FkOiBBbnkpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhwYXlsb2FkLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3cml0ZV90ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cikgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIG5vcm1hbGl6ZV9jb2RlKGNvZGU6IHN0cikgLT4gc3RyOgogICAgcmV0dXJuIGNvZGUucmVwbGFjZSgiX2Jhc2VsaW5lXyIsICJfYmFzZWxpbmVfIikuc3RyaXAoKQoKZGVmIG1pbmltdW1fcmVwYWlyKGZpbmRpbmdfY29kZXM6IGxpc3Rbc3RyXSwgY2xhc3NpZmljYXRpb246IHN0cikgLT4gbGlzdFtzdHJdOgogICAgaWYgbm90IGZpbmRpbmdfY29kZXM6CiAgICAgICAgaWYgY2xhc3NpZmljYXRpb24gPT0gIlRTRUstQiI6CiAgICAgICAgICAgIHJldHVybiBbIkluZGVwZW5kZW50IHZhbGlkYXRpb24gd291bGQgYmUgcmVxdWlyZWQgZm9yIFRTRUstQSBwcm9tb3Rpb24uIl0KICAgICAgICByZXR1cm4gWyJObyBleHBsaWNpdCBmaW5kaW5nIGNvZGVzIHdlcmUgZW1pdHRlZDsgaW5zcGVjdCBnYXRlIHZhbHVlcyBhbmQgY2xhc3NpZmllciB0aHJlc2hvbGRzLiJdCiAgICByZXBhaXJzID0gW10KICAgIGZvciBjb2RlIGluIGZpbmRpbmdfY29kZXM6CiAgICAgICAgcmVwYWlycy5hcHBlbmQoR0FURV9SRVBBSVJTLmdldChjb2RlLCBmIlJlcGFpciBmaW5kaW5nIGB7Y29kZX1gLiIpKQogICAgcmV0dXJuIHJlcGFpcnMKCmRlZiBleHBsYWluX2NsYXNzKHJlY29yZDogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGNscyA9IHJlY29yZC5nZXQoImNsYXNzaWZpY2F0aW9uIiwgInVua25vd24iKQogICAgZmluZGluZ3MgPSByZWNvcmQuZ2V0KCJmaW5kaW5nX2NvZGVzIiwgW10pCiAgICBhX3RzZWsgPSByZWNvcmQuZ2V0KCJBX1RTRUsiKQogICAgZGlhZyA9IHJlY29yZC5nZXQoImRpYWdub3N0aWNfYXZlcmFnZSIpCiAgICBpZiBjbHMgPT0gIlRTRUstQiIgYW5kIG5vdCBmaW5kaW5nczoKICAgICAgICByZXR1cm4gIlByb21vdGVkIHRvIFRTRUstQiBiZWNhdXNlIGFsbCBsb2NhbCBoYXJkIGdhdGVzIGFyZSBkaXNjbG9zZWQgYW5kIG5vIGluZGVwZW5kZW50LXZhbGlkYXRpb24gY2xhaW0gaXMgbWFkZS4gVFNFSy1BIHJlbWFpbnMgYmxvY2tlZCB3aXRob3V0IGluZGVwZW5kZW50IHZhbGlkYXRpb24uIgogICAgaWYgY2xzID09ICJUU0VLLUMiOgogICAgICAgIHJldHVybiBmIkRvd25ncmFkZWQgdG8gVFNFSy1DIGJlY2F1c2Ugb25lIG9yIG1vcmUgcmVxdWlyZWQgZXZpZGVuY2UgZ2F0ZXMgYXJlIG1pc3Npbmcgd2hpbGUgdGhlIGNsYWltIHJlbWFpbnMgaW50ZXJwcmV0YWJsZS4gQV9UU0VLPXthX3RzZWt9LCBkaWFnbm9zdGljX2F2ZXJhZ2U9e2RpYWd9LiIKICAgIGlmIGNscyA9PSAiVFNFSy1EIjoKICAgICAgICByZXR1cm4gZiJEb3duZ3JhZGVkIHRvIFRTRUstRCBiZWNhdXNlIGRpYWdub3N0aWMgc3VwcG9ydCBpcyB3ZWFrIGJ1dCBub3QgZnVsbHkgcmVqZWN0ZWQuIEFfVFNFSz17YV90c2VrfSwgZGlhZ25vc3RpY19hdmVyYWdlPXtkaWFnfS4iCiAgICBpZiBjbHMgPT0gIlRTRUstRSI6CiAgICAgICAgaWYgIlRTRUtfT1ZFUkNMQUlNX0lOREVQRU5ERU5UX1ZBTElEQVRJT04iIGluIGZpbmRpbmdzOgogICAgICAgICAgICByZXR1cm4gIlJlamVjdGVkIHRvIFRTRUstRSBiZWNhdXNlIGFuIGluZGVwZW5kZW50LXZhbGlkYXRpb24gY2xhaW0gd2FzIG1hZGUgd2l0aG91dCBjb3JyZXNwb25kaW5nIGluZGVwZW5kZW50LXZhbGlkYXRpb24gZXZpZGVuY2UuIgogICAgICAgIHJldHVybiBmIlJlamVjdGVkIG9yIHNldmVyZSBkb3duZ3JhZGUgdG8gVFNFSy1FIGJlY2F1c2UgY2xhc3NpZmllciBzdXBwb3J0IGNvbGxhcHNlZC4gQV9UU0VLPXthX3RzZWt9LCBkaWFnbm9zdGljX2F2ZXJhZ2U9e2RpYWd9LiIKICAgIHJldHVybiAiQ2xhc3MgZXhwbGFuYXRpb24gdW5hdmFpbGFibGUuIgoKZGVmIHN1c3BpY2lvbl9sYWJlbChyZWNvcmQ6IGRpY3Rbc3RyLCBBbnldLCBzb3VyY2U6IHN0cikgLT4gc3RyOgogICAgY2xzID0gcmVjb3JkLmdldCgiY2xhc3NpZmljYXRpb24iKQogICAgZmluZGluZ3MgPSByZWNvcmQuZ2V0KCJmaW5kaW5nX2NvZGVzIiwgW10pCiAgICBpZiBzb3VyY2UgPT0gImdhdGVfaW50ZXJhY3Rpb25fbWF0cml4IiBhbmQgY2xzID09ICJUU0VLLUMiIGFuZCBsZW4oZmluZGluZ3MpID49IDI6CiAgICAgICAgcmV0dXJuICJyZXZpZXdfcGFpcl9wb2xpY3kiCiAgICBpZiBjbHMgPT0gIlRTRUstQiIgYW5kIGZpbmRpbmdzOgogICAgICAgIHJldHVybiAidW5leHBlY3RlZF9wcm9tb3Rpb25fd2l0aF9maW5kaW5ncyIKICAgIGlmIGNscyA9PSAiVFNFSy1FIiBhbmQgbm90IGZpbmRpbmdzOgogICAgICAgIHJldHVybiAiaGFyZF9yZWplY3Rfd2l0aG91dF9maW5kaW5nIgogICAgcmV0dXJuICJleHBlY3RlZCIKCmRlZiBtYWtlX2NhcmQoc291cmNlOiBzdHIsIHJlY29yZDogZGljdFtzdHIsIEFueV0sIGlkeDogaW50KSAtPiBkaWN0W3N0ciwgQW55XToKICAgIGZpbmRpbmdfY29kZXMgPSByZWNvcmQuZ2V0KCJmaW5kaW5nX2NvZGVzIiwgW10pCiAgICBpZiAiaWQiIGluIHJlY29yZDoKICAgICAgICBzdWJqZWN0X2lkID0gcmVjb3JkWyJpZCJdCiAgICBlbGlmICJzd2VlcCIgaW4gcmVjb3JkOgogICAgICAgIHN1YmplY3RfaWQgPSBmIntyZWNvcmQuZ2V0KCdzd2VlcCcpfTp7cmVjb3JkLmdldCgneF9uYW1lJyl9PXtyZWNvcmQuZ2V0KCd4X3ZhbHVlJyl9IgogICAgZWxpZiAiZ2F0ZV9hIiBpbiByZWNvcmQ6CiAgICAgICAgc3ViamVjdF9pZCA9IGYie3JlY29yZC5nZXQoJ2dhdGVfYScpfSt7cmVjb3JkLmdldCgnZ2F0ZV9iJyl9IgogICAgZWxzZToKICAgICAgICBzdWJqZWN0X2lkID0gZiJ7c291cmNlfS17aWR4OjA0ZH0iCiAgICBjYXJkID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctdGhyZXNob2xkLWV4cGxhbmF0aW9uLWNhcmQtdjAuNC4zIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgInNvdXJjZSI6IHNvdXJjZSwKICAgICAgICAic3ViamVjdF9pZCI6IHN1YmplY3RfaWQsCiAgICAgICAgImNsYXNzaWZpY2F0aW9uIjogcmVjb3JkLmdldCgiY2xhc3NpZmljYXRpb24iKSwKICAgICAgICAiQV9UU0VLIjogcmVjb3JkLmdldCgiQV9UU0VLIiksCiAgICAgICAgImRpYWdub3N0aWNfYXZlcmFnZSI6IHJlY29yZC5nZXQoImRpYWdub3N0aWNfYXZlcmFnZSIpLAogICAgICAgICJmaW5kaW5nc19jb3VudCI6IHJlY29yZC5nZXQoImZpbmRpbmdzX2NvdW50IiwgbGVuKGZpbmRpbmdfY29kZXMpKSwKICAgICAgICAiZmluZGluZ19jb2RlcyI6IGZpbmRpbmdfY29kZXMsCiAgICAgICAgIndoeV90aGlzX2NsYXNzIjogZXhwbGFpbl9jbGFzcyhyZWNvcmQpLAogICAgICAgICJtaW5pbXVtX3JlcGFpcl9mb3JfcHJvbW90aW9uIjogbWluaW11bV9yZXBhaXIoZmluZGluZ19jb2RlcywgcmVjb3JkLmdldCgiY2xhc3NpZmljYXRpb24iLCAiIikpLAogICAgICAgICJyZXZpZXdfbGFiZWwiOiBzdXNwaWNpb25fbGFiZWwocmVjb3JkLCBzb3VyY2UpLAogICAgICAgICJldmlkZW5jZV9wYXRoIjogcmVjb3JkLmdldCgiZXZpZGVuY2VfcGF0aCIpLAogICAgICAgICJub25fY2xhaW1fbG9jayI6ICJFeHBsYW5hdGlvbiBjYXJkcyBleHBsYWluIGxvY2FsIGNsYXNzaWZpZXIgYmVoYXZpb3Igb25seS4gVGhleSBhcmUgbm90IHNpbGljb24gdmFsaWRhdGlvbiwgcHJvZHVjdCB2YWxpZGF0aW9uLCBtYW51ZmFjdHVyaW5nIHZhbGlkYXRpb24sIHByb2Nlc3Mtbm9kZSBlcXVpdmFsZW5jZSwgYmVuY2htYXJrIHN1cGVyaW9yaXR5IHByb29mLCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgcHJvb2YuIiwKICAgIH0KICAgIGlmICJzd2VlcCIgaW4gcmVjb3JkOgogICAgICAgIGNhcmRbInRocmVzaG9sZF9jb250ZXh0Il0gPSB7CiAgICAgICAgICAgICJzd2VlcCI6IHJlY29yZC5nZXQoInN3ZWVwIiksCiAgICAgICAgICAgICJ4X25hbWUiOiByZWNvcmQuZ2V0KCJ4X25hbWUiKSwKICAgICAgICAgICAgInhfdmFsdWUiOiByZWNvcmQuZ2V0KCJ4X3ZhbHVlIiksCiAgICAgICAgICAgICJsb2dpY2ZvbGRpbmdfbWFyZ2luIjogcmVjb3JkLmdldCgibG9naWNmb2xkaW5nX21hcmdpbiIpLAogICAgICAgICAgICAiZ2FtbWFfdGF1X0VUUCI6IHJlY29yZC5nZXQoImdhbW1hX3RhdV9FVFAiKSwKICAgICAgICB9CiAgICBpZiAiZ2F0ZV9hIiBpbiByZWNvcmQ6CiAgICAgICAgY2FyZFsiaW50ZXJhY3Rpb25fY29udGV4dCJdID0gewogICAgICAgICAgICAiZ2F0ZV9hIjogcmVjb3JkLmdldCgiZ2F0ZV9hIiksCiAgICAgICAgICAgICJnYXRlX2IiOiByZWNvcmQuZ2V0KCJnYXRlX2IiKSwKICAgICAgICAgICAgImdhdGVfdmFsdWVzIjogcmVjb3JkLmdldCgiZ2F0ZV92YWx1ZXMiKSwKICAgICAgICAgICAgImxvZ2ljZm9sZGluZ19tYXJnaW4iOiByZWNvcmQuZ2V0KCJsb2dpY2ZvbGRpbmdfbWFyZ2luIiksCiAgICAgICAgICAgICJnYW1tYV90YXVfRVRQIjogcmVjb3JkLmdldCgiZ2FtbWFfdGF1X0VUUCIpLAogICAgICAgIH0KICAgIHJldHVybiBjYXJkCgpkZWYgY29sbGVjdF9yZWNvcmRzKCkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICBjYXJkczogbGlzdFtkaWN0W3N0ciwgQW55XV0gPSBbXQogICAgZm9yIHNvdXJjZSwgcGF0aCBpbiBTT1VSQ0VTLml0ZW1zKCk6CiAgICAgICAgcGF5bG9hZCA9IHJlYWRfanNvbihwYXRoKQogICAgICAgIHJlc3VsdHMgPSBwYXlsb2FkLmdldCgicmVzdWx0cyIsIFtdKQogICAgICAgIGZvciBpZHgsIHJlYyBpbiBlbnVtZXJhdGUocmVzdWx0cyk6CiAgICAgICAgICAgIGNhcmRzLmFwcGVuZChtYWtlX2NhcmQoc291cmNlLCByZWMsIGlkeCkpCiAgICByZXR1cm4gY2FyZHMKCmRlZiBzdW1tYXJpemUoY2FyZHM6IGxpc3RbZGljdFtzdHIsIEFueV1dLCBjaGFydF9wYXRoczogbGlzdFtzdHJdKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIGNsYXNzX2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgcmV2aWV3X2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgc291cmNlX2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgZmluZGluZ19jb3VudHM6IGRpY3Rbc3RyLCBpbnRdID0ge30KICAgIGZvciBjIGluIGNhcmRzOgogICAgICAgIGNsYXNzX2NvdW50c1tjWyJjbGFzc2lmaWNhdGlvbiJdXSA9IGNsYXNzX2NvdW50cy5nZXQoY1siY2xhc3NpZmljYXRpb24iXSwgMCkgKyAxCiAgICAgICAgcmV2aWV3X2NvdW50c1tjWyJyZXZpZXdfbGFiZWwiXV0gPSByZXZpZXdfY291bnRzLmdldChjWyJyZXZpZXdfbGFiZWwiXSwgMCkgKyAxCiAgICAgICAgc291cmNlX2NvdW50c1tjWyJzb3VyY2UiXV0gPSBzb3VyY2VfY291bnRzLmdldChjWyJzb3VyY2UiXSwgMCkgKyAxCiAgICAgICAgZm9yIGNvZGUgaW4gY1siZmluZGluZ19jb2RlcyJdOgogICAgICAgICAgICBmaW5kaW5nX2NvdW50c1tjb2RlXSA9IGZpbmRpbmdfY291bnRzLmdldChjb2RlLCAwKSArIDEKCiAgICByZXZpZXdfZXhhbXBsZXMgPSBbYyBmb3IgYyBpbiBjYXJkcyBpZiBjWyJyZXZpZXdfbGFiZWwiXSAhPSAiZXhwZWN0ZWQiXVs6MjVdCiAgICByZXR1cm4gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctdGhyZXNob2xkLWV4cGxhbmF0aW9uLWNhcmRzLXYwLjQuMyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJjYXJkX2NvdW50IjogbGVuKGNhcmRzKSwKICAgICAgICAiY2xhc3NfY291bnRzIjogY2xhc3NfY291bnRzLAogICAgICAgICJzb3VyY2VfY291bnRzIjogc291cmNlX2NvdW50cywKICAgICAgICAicmV2aWV3X2NvdW50cyI6IHJldmlld19jb3VudHMsCiAgICAgICAgImZpbmRpbmdfY291bnRzIjogZmluZGluZ19jb3VudHMsCiAgICAgICAgInJldmlld19leGFtcGxlcyI6IHJldmlld19leGFtcGxlcywKICAgICAgICAiY2hhcnRfcGF0aHMiOiBjaGFydF9wYXRocywKICAgICAgICAiY2FyZF9kaXJlY3RvcnkiOiBzdHIoQ0FSRF9ESVIucmVsYXRpdmVfdG8oUkVQT19ST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpLAogICAgICAgICJib3VuZGFyeSI6ICJFeHBsYW5hdGlvbiBjYXJkcyBleHBsYWluIGxvY2FsIGNsYXNzaWZpZXIgYmVoYXZpb3Igb25seS4gVGhleSBhcmUgbm90IHNpbGljb24gdmFsaWRhdGlvbiwgcHJvZHVjdCB2YWxpZGF0aW9uLCBtYW51ZmFjdHVyaW5nIHZhbGlkYXRpb24sIHByb2Nlc3Mtbm9kZSBlcXVpdmFsZW5jZSwgYmVuY2htYXJrIHN1cGVyaW9yaXR5IHByb29mLCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgcHJvb2YuIiwKICAgIH0KCmRlZiBnZW5lcmF0ZV9jaGFydHMoY2FyZHM6IGxpc3RbZGljdFtzdHIsIEFueV1dKSAtPiBsaXN0W3N0cl06CiAgICBjaGFydF9wYXRoczogbGlzdFtzdHJdID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIGYibWF0cGxvdGxpYiB1bmF2YWlsYWJsZToge2V4Y31cbiIpCiAgICAgICAgcmV0dXJuIGNoYXJ0X3BhdGhzCgogICAgVklTX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmVmaWcocGF0aDogUGF0aCkgLT4gTm9uZToKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwYXRoLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgY2hhcnRfcGF0aHMuYXBwZW5kKHN0cihwYXRoLnJlbGF0aXZlX3RvKFJFUE9fUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSkKCiAgICBkZWYgY291bnRzX2ZvcihrZXk6IHN0cikgLT4gZGljdFtzdHIsIGludF06CiAgICAgICAgZDogZGljdFtzdHIsIGludF0gPSB7fQogICAgICAgIGZvciBjIGluIGNhcmRzOgogICAgICAgICAgICBkW3N0cihjLmdldChrZXkpKV0gPSBkLmdldChzdHIoYy5nZXQoa2V5KSksIDApICsgMQogICAgICAgIHJldHVybiBkCgogICAgZm9yIGtleSwgdGl0bGUsIGZuYW1lIGluIFsKICAgICAgICAoImNsYXNzaWZpY2F0aW9uIiwgIkV4cGxhbmF0aW9uIENhcmQgQ2xhc3MgQ291bnRzIiwgImV4cGxhbmF0aW9uX2NsYXNzX2NvdW50cy5wbmciKSwKICAgICAgICAoInJldmlld19sYWJlbCIsICJFeHBsYW5hdGlvbiBDYXJkIFJldmlldyBMYWJlbHMiLCAiZXhwbGFuYXRpb25fcmV2aWV3X2xhYmVscy5wbmciKSwKICAgICAgICAoInNvdXJjZSIsICJFeHBsYW5hdGlvbiBDYXJkIFNvdXJjZSBDb3VudHMiLCAiZXhwbGFuYXRpb25fc291cmNlX2NvdW50cy5wbmciKSwKICAgIF06CiAgICAgICAgZGF0YSA9IGNvdW50c19mb3Ioa2V5KQogICAgICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICAgICAgcGx0LmJhcihsaXN0KGRhdGEua2V5cygpKSwgbGlzdChkYXRhLnZhbHVlcygpKSkKICAgICAgICBwbHQudGl0bGUodGl0bGUpCiAgICAgICAgcGx0LnlsYWJlbCgiQ2FyZCBjb3VudCIpCiAgICAgICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zMCwgaGE9InJpZ2h0IikKICAgICAgICBzYXZlZmlnKFZJU19ESVIgLyBmbmFtZSkKCiAgICBmaW5kaW5nX2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgZm9yIGMgaW4gY2FyZHM6CiAgICAgICAgZm9yIGNvZGUgaW4gY1siZmluZGluZ19jb2RlcyJdOgogICAgICAgICAgICBmaW5kaW5nX2NvdW50c1tjb2RlXSA9IGZpbmRpbmdfY291bnRzLmdldChjb2RlLCAwKSArIDEKICAgIGlmIGZpbmRpbmdfY291bnRzOgogICAgICAgIGxhYmVscyA9IGxpc3QoZmluZGluZ19jb3VudHMua2V5cygpKQogICAgICAgIHZhbHVlcyA9IFtmaW5kaW5nX2NvdW50c1trXSBmb3IgayBpbiBsYWJlbHNdCiAgICAgICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMiwgNSkpCiAgICAgICAgcGx0LmJhcihsYWJlbHMsIHZhbHVlcykKICAgICAgICBwbHQudGl0bGUoIkZpbmRpbmcgRnJlcXVlbmN5IEFjcm9zcyBFeHBsYW5hdGlvbiBDYXJkcyIpCiAgICAgICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgICAgIHBsdC54dGlja3Mocm90YXRpb249NjUsIGhhPSJyaWdodCIsIGZvbnRzaXplPTcpCiAgICAgICAgc2F2ZWZpZyhWSVNfRElSIC8gImV4cGxhbmF0aW9uX2ZpbmRpbmdfZnJlcXVlbmN5LnBuZyIpCgogICAgcmV0dXJuIGNoYXJ0X3BhdGhzCgpkZWYgcmVuZGVyX2NhcmRfbWQoY2FyZDogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIHJlcGFpcnMgPSAiXG4iLmpvaW4oZiItIHtyfSIgZm9yIHIgaW4gY2FyZFsibWluaW11bV9yZXBhaXJfZm9yX3Byb21vdGlvbiJdKQogICAgZmluZGluZ3MgPSAiXG4iLmpvaW4oZiItIGB7Y31gIiBmb3IgYyBpbiBjYXJkWyJmaW5kaW5nX2NvZGVzIl0pIG9yICJOb25lIgogICAgcmV0dXJuIGYiIiIjIEV4cGxhbmF0aW9uIENhcmQg4oCUIHtjYXJkWydzdWJqZWN0X2lkJ119CgpHZW5lcmF0ZWQ6IGB7Y2FyZFsnZ2VuZXJhdGVkX2F0J119YAoKfCBGaWVsZCB8IFZhbHVlIHwKfC0tLXwtLS18CnwgU291cmNlIHwgYHtjYXJkWydzb3VyY2UnXX1gIHwKfCBDbGFzc2lmaWNhdGlvbiB8IGB7Y2FyZFsnY2xhc3NpZmljYXRpb24nXX1gIHwKfCBBX1RTRUsgfCBge2NhcmRbJ0FfVFNFSyddfWAgfAp8IERpYWdub3N0aWMgYXZlcmFnZSB8IGB7Y2FyZFsnZGlhZ25vc3RpY19hdmVyYWdlJ119YCB8CnwgRmluZGluZ3MgY291bnQgfCBge2NhcmRbJ2ZpbmRpbmdzX2NvdW50J119YCB8CnwgUmV2aWV3IGxhYmVsIHwgYHtjYXJkWydyZXZpZXdfbGFiZWwnXX1gIHwKCiMjIFdoeSBUaGlzIENsYXNzCgp7Y2FyZFsnd2h5X3RoaXNfY2xhc3MnXX0KCiMjIEZpbmRpbmcgQ29kZXMKCntmaW5kaW5nc30KCiMjIE1pbmltdW0gUmVwYWlyIEZvciBQcm9tb3Rpb24KCntyZXBhaXJzfQoKIyMgRXZpZGVuY2UgUGF0aAoKYGBgdGV4dAp7Y2FyZC5nZXQoJ2V2aWRlbmNlX3BhdGgnKX0KYGBgCgojIyBCb3VuZGFyeQoKe2NhcmRbJ25vbl9jbGFpbV9sb2NrJ119CiIiIgoKZGVmIHJlbmRlcl9zdW1tYXJ5X21kKHN1bW1hcnk6IGRpY3Rbc3RyLCBBbnldKSAtPiBzdHI6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC40LjMgVGhyZXNob2xkIEV4cGxhbmF0aW9uIENhcmRzIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gQ2FyZCBjb3VudDogYHtzdW1tYXJ5WydjYXJkX2NvdW50J119YCIsCiAgICAgICAgZiItIENhcmQgZGlyZWN0b3J5OiBge3N1bW1hcnlbJ2NhcmRfZGlyZWN0b3J5J119YCIsCiAgICAgICAgZiItIENoYXJ0IGNvdW50OiBge2xlbihzdW1tYXJ5WydjaGFydF9wYXRocyddKX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgU291cmNlIENvdW50cyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU291cmNlIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc29ydGVkKHN1bW1hcnlbInNvdXJjZV9jb3VudHMiXS5pdGVtcygpKToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7a31gIHwge3Z9IHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENsYXNzIENvdW50cyIsICIiLCAifCBDbGFzcyB8IENvdW50IHwiLCAifC0tLXwtLS06fCJdCiAgICBmb3IgaywgdiBpbiBzb3J0ZWQoc3VtbWFyeVsiY2xhc3NfY291bnRzIl0uaXRlbXMoKSk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2t9YCB8IHt2fSB8IikKCiAgICBsaW5lcyArPSBbIiIsICIjIyBSZXZpZXcgTGFiZWxzIiwgIiIsICJ8IExhYmVsIHwgQ291bnQgfCBNZWFuaW5nIHwiLCAifC0tLXwtLS06fC0tLXwiXQogICAgbWVhbmluZ3MgPSB7CiAgICAgICAgImV4cGVjdGVkIjogIkNsYXNzaWZpZXIgYmVoYXZpb3IgbWF0Y2hlcyBjdXJyZW50IHBvbGljeS4iLAogICAgICAgICJyZXZpZXdfcGFpcl9wb2xpY3kiOiAiUGFpcmVkIGZhaWx1cmVzIHJlbWFpbmVkIGNvbnRyb2xsZWQgZG93bmdyYWRlOyByZXZpZXcgd2hldGhlciB0aGlzIHNob3VsZCBiZWNvbWUgc3RyaWN0ZXIuIiwKICAgICAgICAidW5leHBlY3RlZF9wcm9tb3Rpb25fd2l0aF9maW5kaW5ncyI6ICJQcm9tb3Rpb24gb2NjdXJyZWQgZGVzcGl0ZSBmaW5kaW5nczsgaW5zcGVjdCBpbW1lZGlhdGVseS4iLAogICAgICAgICJoYXJkX3JlamVjdF93aXRob3V0X2ZpbmRpbmciOiAiSGFyZCByZWplY3Qgb2NjdXJyZWQgd2l0aG91dCBjbGVhciBmaW5kaW5nOyBpbnNwZWN0IGltbWVkaWF0ZWx5LiIsCiAgICB9CiAgICBmb3IgaywgdiBpbiBzb3J0ZWQoc3VtbWFyeVsicmV2aWV3X2NvdW50cyJdLml0ZW1zKCkpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCB7bWVhbmluZ3MuZ2V0KGssICcnKX0gfCIpCgogICAgbGluZXMgKz0gWyIiLCAiIyMgUmV2aWV3IEV4YW1wbGVzIiwgIiIsICJ8IFNvdXJjZSB8IFN1YmplY3QgfCBDbGFzcyB8IFJldmlldyBsYWJlbCB8IFdoeSB8IiwgInwtLS18LS0tfC0tLXwtLS18LS0tfCJdCiAgICBmb3IgYyBpbiBzdW1tYXJ5WyJyZXZpZXdfZXhhbXBsZXMiXToKICAgICAgICB3aHkgPSBjWyJ3aHlfdGhpc19jbGFzcyJdLnJlcGxhY2UoInwiLCAiXFx8IikKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7Y1snc291cmNlJ119YCB8IGB7Y1snc3ViamVjdF9pZCddfWAgfCBge2NbJ2NsYXNzaWZpY2F0aW9uJ119YCB8IGB7Y1sncmV2aWV3X2xhYmVsJ119YCB8IHt3aHl9IHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIGNoYXJ0IGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJFUE9fUk9PVCAvIGNoYXJ0LCBPVVRfRElSKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcyArPSBbZiIhW3tQYXRoKGNoYXJ0KS5zdGVtfV0oe3JlbH0pIiwgIiJdCgogICAgbGluZXMgKz0gWwogICAgICAgICIjIyBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc3VtbWFyeVsiYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgIF0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpIC0+IE5vbmU6CiAgICBjYXJkcyA9IGNvbGxlY3RfcmVjb3JkcygpCiAgICBDQVJEX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBmb3IgaWR4LCBjYXJkIGluIGVudW1lcmF0ZShjYXJkcyk6CiAgICAgICAgc2FmZV9pZCA9ICIiLmpvaW4oY2ggaWYgY2guaXNhbG51bSgpIG9yIGNoIGluICItXy4iIGVsc2UgIl8iIGZvciBjaCBpbiBjYXJkWyJzdWJqZWN0X2lkIl0pLnN0cmlwKCJfIilbOjE0MF0KICAgICAgICBqc29uX3BhdGggPSBDQVJEX0RJUiAvIGYie2lkeDowNGR9X3tzYWZlX2lkfS5qc29uIgogICAgICAgIG1kX3BhdGggPSBDQVJEX0RJUiAvIGYie2lkeDowNGR9X3tzYWZlX2lkfS5tZCIKICAgICAgICB3cml0ZV9qc29uKGpzb25fcGF0aCwgY2FyZCkKICAgICAgICB3cml0ZV90ZXh0KG1kX3BhdGgsIHJlbmRlcl9jYXJkX21kKGNhcmQpKQoKICAgIGNoYXJ0X3BhdGhzID0gZ2VuZXJhdGVfY2hhcnRzKGNhcmRzKQogICAgc3VtbWFyeSA9IHN1bW1hcml6ZShjYXJkcywgY2hhcnRfcGF0aHMpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAidGhyZXNob2xkX2V4cGxhbmF0aW9uX2NhcmRzX3YwXzRfMy5qc29uIiwgc3VtbWFyeSkKICAgIHdyaXRlX2pzb24oT1VUX0RJUiAvICJsYXRlc3RfdGhyZXNob2xkX2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gInRocmVzaG9sZF9leHBsYW5hdGlvbl9jYXJkc192MF80XzMubWQiLCByZW5kZXJfc3VtbWFyeV9tZChzdW1tYXJ5KSkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJsYXRlc3RfdGhyZXNob2xkX2V4cGxhbmF0aW9uX2NhcmRzLm1kIiwgcmVuZGVyX3N1bW1hcnlfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJjYXJkX2NvdW50Ijogc3VtbWFyeVsiY2FyZF9jb3VudCJdLAogICAgICAgICJjbGFzc19jb3VudHMiOiBzdW1tYXJ5WyJjbGFzc19jb3VudHMiXSwKICAgICAgICAic291cmNlX2NvdW50cyI6IHN1bW1hcnlbInNvdXJjZV9jb3VudHMiXSwKICAgICAgICAicmV2aWV3X2NvdW50cyI6IHN1bW1hcnlbInJldmlld19jb3VudHMiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL2V4cGxhbmF0aW9ucy9sYXRlc3RfdGhyZXNob2xkX2V4cGxhbmF0aW9uX2NhcmRzLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
runner_text = base64.b64decode(runner_b64.encode("ascii")).decode("utf-8")
write(ROOT / "scripts" / "benchmarks" / "generate_threshold_explanation_cards.py", runner_text)

write(ROOT / "reports" / "explanations" / "README.md", """# Explanation Reports

Current layer: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**

## Purpose

This folder stores classifier explanation cards, promotion-repair hints, and review labels.

## Primary command

```powershell
python scripts/benchmarks/generate_threshold_explanation_cards.py
```

## README Update Rule

Update this mini README whenever explanation-card schemas, reports, or interpretation rules change.

Boundary: explanation reports explain local classifier behavior only.
""")

write(ROOT / "visuals" / "explanations" / "README.md", """# Explanation Visuals

Current layer: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**

## Purpose

This folder stores visual summaries for threshold explanation cards.

## README Update Rule

Update this mini README whenever explanation chart folders or meanings change.

Boundary: explanation visuals are local classifier diagnostics only.
""")

write(ROOT / "visuals" / "explanations" / "v0_4_3" / "README.md", """# v0.4.3 Explanation Charts

## Expected Charts

- `explanation_class_counts.png`
- `explanation_review_labels.png`
- `explanation_source_counts.png`
- `explanation_finding_frequency.png`

## README Update Rule

Update this mini README whenever chart names or chart meanings change.

Boundary: local classifier explanation diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.2[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.1[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.2 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.3 |", r)

if "| Threshold explanation cards | `reports/explanations/latest_threshold_explanation_cards.md` |" not in r:
    r = r.replace(
        "| Interaction charts | `visuals/interactions/v0_4_2/` |\n",
        "| Interaction charts | `visuals/interactions/v0_4_2/` |\n| Threshold explanation cards | `reports/explanations/latest_threshold_explanation_cards.md` |\n| Explanation charts | `visuals/explanations/v0_4_3/` |\n",
    )

if "python scripts/benchmarks/generate_threshold_explanation_cards.py" not in r:
    r = r.replace(
        "python scripts/benchmarks/run_gate_interaction_matrix.py\npython scripts/release/validate_release.py",
        "python scripts/benchmarks/run_gate_interaction_matrix.py\npython scripts/benchmarks/generate_threshold_explanation_cards.py\npython scripts/release/validate_release.py",
    )

section = """## Threshold Explanation Cards v0.4.3

v0.4.3 turns classifier outputs into explanation cards.

Primary command:

```powershell
python scripts/benchmarks/generate_threshold_explanation_cards.py
```

Primary outputs:

```text
reports/explanations/latest_threshold_explanation_cards.json
reports/explanations/latest_threshold_explanation_cards.md
reports/explanations/cards/v0_4_3/
visuals/explanations/v0_4_3/
```

The purpose is to answer:

```text
Why did this claim receive its class?
Which gates caused downgrade?
What minimum repair would promote it?
Which classifier behaviors should be reviewed before hardening?
```

Current design question:

```text
v0.4.2 showed all paired gate failures remained TSEK-C.
v0.4.3 marks those cases as review_pair_policy instead of changing classifier rules prematurely.
```

Boundary: explanation cards explain local classifier behavior only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Threshold Explanation Cards v0.4.3" not in r:
    r = r.replace("## Gate Interaction Matrix v0.4.2", section + "## Gate Interaction Matrix v0.4.2", 1)

if "    explanations/" not in r:
    r = r.replace("  reports/\n    interactions/", "  reports/\n    explanations/\n    interactions/")
    r = r.replace("  visuals/\n    interactions/", "  visuals/\n    explanations/\n    interactions/")

lesson = "| L-021 | v0.4.2 showed every paired hard-gate failure classified as TSEK-C. | The current classifier treats paired missing gates as controlled downgrade unless overclaim or severe collapse forces TSEK-E. | Do not harden classifier thresholds until explanation cards classify whether pair-policy behavior is expected, suspicious, or promotion-repairable. |"
if lesson not in r:
    r = r.replace(
        "| L-020 | After v0.4.0e, README checkpoint advanced while AGENTS.md and task_routing_matrix.md still identified v0.3.3e. | Fast benchmark/readme repair layers advanced human-facing state faster than agent-facing contracts. | Every release-like change must re-sync AGENTS.md, task_routing_matrix.md, and route surfaces to the current checkpoint before the next experiment. |\n",
        "| L-020 | After v0.4.0e, README checkpoint advanced while AGENTS.md and task_routing_matrix.md still identified v0.3.3e. | Fast benchmark/readme repair layers advanced human-facing state faster than agent-facing contracts. | Every release-like change must re-sync AGENTS.md, task_routing_matrix.md, and route surfaces to the current checkpoint before the next experiment. |\n" + lesson + "\n",
    )

if "| v0.4.3 | Threshold explanation cards and promotion-repair hints. |" not in r:
    r = r.replace(
        "| v0.4.2 | Gate interaction matrix and paired gate-failure heatmaps. |\n",
        "| v0.4.2 | Gate interaction matrix and paired gate-failure heatmaps. |\n| v0.4.3 | Threshold explanation cards and promotion-repair hints. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**

Recommended goals:

- Convert explanation-card review labels into explicit policy checks.
- Decide whether some paired failures should become TSEK-D or TSEK-E.
- Add a policy table for gate-pair severity.
- Preserve non-claim locks: pair policy is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS and routing.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.2[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**",
    a,
)
if "python scripts/benchmarks/generate_threshold_explanation_cards.py" not in a:
    a = a.replace(
        "python scripts/benchmarks/run_gate_interaction_matrix.py\npython -m unittest discover -s tests",
        "python scripts/benchmarks/run_gate_interaction_matrix.py\npython scripts/benchmarks/generate_threshold_explanation_cards.py\npython -m unittest discover -s tests",
    )
if "Explanation card patch" not in a:
    a = a.replace(
        "| Gate interaction patch | `configs/seeds/interactions/`, `reports/interactions/`, `visuals/interactions/` | release validator + interaction matrix report + benchmark atlas update |\n",
        "| Gate interaction patch | `configs/seeds/interactions/`, `reports/interactions/`, `visuals/interactions/` | release validator + interaction matrix report + benchmark atlas update |\n| Explanation card patch | `reports/explanations/`, `visuals/explanations/`, classifier reports | release validator + explanation card report |\n",
    )
write(agents, a)

matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.2[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**",
    m,
)
if "| Explanation card patch |" not in m:
    m = m.replace(
        "| Gate interaction patch | inner | validation | tau | `configs/seeds/interactions/`, gate formulas, classifier, benchmark atlas | release validator + interaction matrix report | `reports/interactions/latest_gate_interaction_matrix.md` |\n",
        "| Gate interaction patch | inner | validation | tau | `configs/seeds/interactions/`, gate formulas, classifier, benchmark atlas | release validator + interaction matrix report | `reports/interactions/latest_gate_interaction_matrix.md` |\n| Explanation card patch | outer | evidence | validation | `reports/explanations/`, interaction/sensitivity reports, classifier | release validator + explanation report | `reports/explanations/latest_threshold_explanation_cards.md` |\n",
    )
write(matrix, m)

route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.3"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["threshold_explanation_cards"] = {
    "read_first": ["reports/benchmarks/latest_synthetic_gate_suite.json", "reports/sensitivity/latest_sensitivity_sweep.json", "reports/interactions/latest_gate_interaction_matrix.json"],
    "validate": ["python scripts/benchmarks/generate_threshold_explanation_cards.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/explanations/latest_threshold_explanation_cards.md", "reports/explanations/cards/v0_4_3/", "visuals/explanations/v0_4_3/"],
}
write_json(route_path, route)

atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.3 | Threshold explanation cards |" not in t:
    t = t.replace(
        "| v0.4.2 | Gate interaction matrix | `python scripts/benchmarks/run_gate_interaction_matrix.py` | Pairwise gate-failure interaction matrix across hard gates | `reports/interactions/latest_gate_interaction_matrix.md` | `visuals/interactions/v0_4_2/` |\n",
        "| v0.4.2 | Gate interaction matrix | `python scripts/benchmarks/run_gate_interaction_matrix.py` | Pairwise gate-failure interaction matrix across hard gates | `reports/interactions/latest_gate_interaction_matrix.md` | `visuals/interactions/v0_4_2/` |\n| v0.4.3 | Threshold explanation cards | `python scripts/benchmarks/generate_threshold_explanation_cards.py` | Class explanations, repair hints, and review labels across synthetic/sensitivity/interaction results | `reports/explanations/latest_threshold_explanation_cards.md` | `visuals/explanations/v0_4_3/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_3_threshold_explanation_cards.md", f"""# TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards

Generated: {GENERATED_AT}

## Purpose

Generate explanation cards for classifier outcomes across synthetic scenarios, sensitivity sweeps, and gate interaction matrices.

## Additions

- `scripts/benchmarks/generate_threshold_explanation_cards.py`
- `reports/explanations/`
- `reports/explanations/cards/v0_4_3/`
- `visuals/explanations/v0_4_3/`
- README/AGENTS/route-map/task-matrix/benchmark-atlas updates.

## Boundary

Explanation cards explain local classifier behavior only. They do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "explanations" / "v0_4_3" / "latest_v0_4_3_status.md", f"""# Tau Scaling v0.4.3 Explanation Card Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary command:

```powershell
python scripts/benchmarks/generate_threshold_explanation_cards.py
```
""")

print("v0.4.3 threshold explanation cards patch written")
