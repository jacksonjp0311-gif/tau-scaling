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
        dest = ROOT / "reports" / "policy" / "v0_4_4" / "backups" / f"{path.name}_before_v0_4_4_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhbm5vdGF0aW9ucwoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KRVhQTEFJTl9QQVRIID0gUkVQT19ST09UIC8gInJlcG9ydHMiIC8gImV4cGxhbmF0aW9ucyIgLyAibGF0ZXN0X3RocmVzaG9sZF9leHBsYW5hdGlvbl9jYXJkcy5qc29uIgpJTlRFUkFDVElPTl9QQVRIID0gUkVQT19ST09UIC8gInJlcG9ydHMiIC8gImludGVyYWN0aW9ucyIgLyAibGF0ZXN0X2dhdGVfaW50ZXJhY3Rpb25fbWF0cml4Lmpzb24iCk9VVF9ESVIgPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicG9saWN5IgpWSVNfRElSID0gUkVQT19ST09UIC8gInZpc3VhbHMiIC8gInBvbGljeSIgLyAidjBfNF80IgoKR0FURV9PUkRFUiA9IFsKICAgICJCX3NvdXJjZSIsCiAgICAiQl9tZXRyaWMiLAogICAgIkJfYmFzZWxpbmUiLAogICAgIkJfbWV0aG9kIiwKICAgICJCX3dvcmtsb2FkIiwKICAgICJCX3RhdSIsCiAgICAiQl9MRiIsCiAgICAiQl9FVFAiLAogICAgIkJfUFZUIiwKICAgICJCX3lpZWxkIiwKICAgICJCX2V2aWRlbmNlIiwKXQoKU0VWRVJJVFlfU0NPUkUgPSB7CiAgICAiVFNFSy1DX1JFVEFJTiI6IDEsCiAgICAiVFNFSy1EX0NBTkRJREFURSI6IDIsCiAgICAiVFNFSy1FX0NBTkRJREFURSI6IDMsCiAgICAiSFVNQU5fUkVWSUVXIjogNCwKfQoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmV0dXJuIHt9CgpkZWYgd3JpdGVfanNvbihwYXRoOiBQYXRoLCBwYXlsb2FkOiBBbnkpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhwYXlsb2FkLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3cml0ZV90ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cikgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHBhaXJfcG9saWN5KGdhdGVfYTogc3RyLCBnYXRlX2I6IHN0ciwgcmVzdWx0OiBkaWN0W3N0ciwgQW55XSkgLT4gZGljdFtzdHIsIEFueV06CiAgICBwYWlyID0ge2dhdGVfYSwgZ2F0ZV9ifQogICAgY2xhc3NpZmljYXRpb24gPSByZXN1bHQuZ2V0KCJjbGFzc2lmaWNhdGlvbiIpCiAgICBmaW5kaW5ncyA9IHJlc3VsdC5nZXQoImZpbmRpbmdfY29kZXMiLCBbXSkKCiAgICBpZiAiQl9zb3VyY2UiIGluIHBhaXIgYW5kICgiQl9ldmlkZW5jZSIgaW4gcGFpciBvciAiQl9iYXNlbGluZSIgaW4gcGFpciBvciAiQl9tZXRyaWMiIGluIHBhaXIpOgogICAgICAgIHJldHVybiB7CiAgICAgICAgICAgICJwb2xpY3lfY2xhc3MiOiAiSFVNQU5fUkVWSUVXIiwKICAgICAgICAgICAgInJlY29tbWVuZGVkX2FjdGlvbiI6ICJSZXF1aXJlIGh1bWFuIHJldmlldyBiZWZvcmUgcHJvbW90aW9uIGJlY2F1c2Ugc291cmNlIGJvdW5kYXJ5IGlzIHBhaXJlZCB3aXRoIG1ldHJpYy9iYXNlbGluZS9ldmlkZW5jZSBmYWlsdXJlLiIsCiAgICAgICAgICAgICJyZWFzb24iOiAiU291cmNlLWJvdW5kYXJ5IGZhaWx1cmVzIGFmZmVjdCBpbnRlcnByZXRhYmlsaXR5IG9mIHRoZSBlbnRpcmUgY2xhaW0uIiwKICAgICAgICB9CgogICAgaWYgIkJfZXZpZGVuY2UiIGluIHBhaXIgYW5kICgiQl95aWVsZCIgaW4gcGFpciBvciAiQl9QVlQiIGluIHBhaXIgb3IgIkJfbWV0aG9kIiBpbiBwYWlyKToKICAgICAgICByZXR1cm4gewogICAgICAgICAgICAicG9saWN5X2NsYXNzIjogIlRTRUstRF9DQU5ESURBVEUiLAogICAgICAgICAgICAicmVjb21tZW5kZWRfYWN0aW9uIjogIkNhbmRpZGF0ZSBkb3duZ3JhZGUgYmVsb3cgVFNFSy1DIHVubGVzcyBldmlkZW5jZSBwYWNrYWdlLCB5aWVsZC9tZXRob2QsIGFuZCBjbG9zdXJlIGRpc2Nsb3N1cmVzIGFyZSByZXBhaXJlZC4iLAogICAgICAgICAgICAicmVhc29uIjogIkV2aWRlbmNlIHBsdXMgcGh5c2ljYWwtZGlzY2xvc3VyZSBmYWlsdXJlIHdlYWtlbnMgYXVkaXRhYmlsaXR5IGJleW9uZCBvcmRpbmFyeSBzaW5nbGUtZ2F0ZSBkb3duZ3JhZGUuIiwKICAgICAgICB9CgogICAgaWYgIkJfTEYiIGluIHBhaXIgYW5kICJCX0VUUCIgaW4gcGFpcjoKICAgICAgICByZXR1cm4gewogICAgICAgICAgICAicG9saWN5X2NsYXNzIjogIlRTRUstRF9DQU5ESURBVEUiLAogICAgICAgICAgICAicmVjb21tZW5kZWRfYWN0aW9uIjogIkNhbmRpZGF0ZSBkb3duZ3JhZGUgYmVsb3cgVFNFSy1DIGJlY2F1c2Ugc3Vydml2YWJpbGl0eSBhbmQgZW5lcmd5L3RoZXJtYWwvUEROIGdhaW4gZmFpbCB0b2dldGhlci4iLAogICAgICAgICAgICAicmVhc29uIjogIkxvZ2ljRm9sZGluZyB2aWFiaWxpdHkgYW5kIG5vcm1hbGl6ZWQgdGF1IGdhaW4gYXJlIGJvdGggY2VudHJhbCB0byB0aGUgcnVudGltZSBjbGFpbSBwYXRoLiIsCiAgICAgICAgfQoKICAgIGlmICJCX3RhdSIgaW4gcGFpciBhbmQgKCJCX3dvcmtsb2FkIiBpbiBwYWlyIG9yICJCX2Jhc2VsaW5lIiBpbiBwYWlyKToKICAgICAgICByZXR1cm4gewogICAgICAgICAgICAicG9saWN5X2NsYXNzIjogIlRTRUstRF9DQU5ESURBVEUiLAogICAgICAgICAgICAicmVjb21tZW5kZWRfYWN0aW9uIjogIkNhbmRpZGF0ZSBkb3duZ3JhZGUgYmVsb3cgVFNFSy1DIHVudGlsIHRhdSB2ZWN0b3IsIHdvcmtsb2FkLCBhbmQgYmFzZWxpbmUgYXJlIHNpbXVsdGFuZW91c2x5IHJlcGFpcmVkLiIsCiAgICAgICAgICAgICJyZWFzb24iOiAiVGF1IGltcHJvdmVtZW50cyBhcmUgbm90IGludGVycHJldGFibGUgd2l0aG91dCB3b3JrbG9hZCBhbmQgYmFzZWxpbmUgY29udGV4dC4iLAogICAgICAgIH0KCiAgICBpZiBjbGFzc2lmaWNhdGlvbiA9PSAiVFNFSy1DIiBhbmQgbGVuKGZpbmRpbmdzKSA+PSAyOgogICAgICAgIHJldHVybiB7CiAgICAgICAgICAgICJwb2xpY3lfY2xhc3MiOiAiVFNFSy1DX1JFVEFJTiIsCiAgICAgICAgICAgICJyZWNvbW1lbmRlZF9hY3Rpb24iOiAiUmV0YWluIFRTRUstQyB1bmRlciBjdXJyZW50IHBvbGljeSwgYnV0IGtlZXAgcGFpciB2aXNpYmxlIGluIGV4cGxhbmF0aW9uIGNhcmRzLiIsCiAgICAgICAgICAgICJyZWFzb24iOiAiUGFpcmVkIGZhaWx1cmUgaXMgY29udHJvbGxlZCBhbmQgaW50ZXJwcmV0YWJsZTsgbm8gb3ZlcmNsYWltIG9yIGhhcmQgcmVqZWN0aW9uIGNvbmRpdGlvbiBkZXRlY3RlZC4iLAogICAgICAgIH0KCiAgICByZXR1cm4gewogICAgICAgICJwb2xpY3lfY2xhc3MiOiAiVFNFSy1DX1JFVEFJTiIsCiAgICAgICAgInJlY29tbWVuZGVkX2FjdGlvbiI6ICJSZXRhaW4gY3VycmVudCBjbGFzc2lmaWVyIGJlaGF2aW9yLiIsCiAgICAgICAgInJlYXNvbiI6ICJObyBwb2xpY3kgZXNjYWxhdGlvbiBydWxlIG1hdGNoZWQuIiwKICAgIH0KCmRlZiBpbnRlcmFjdGlvbl9yZWNvcmRzKCkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICBwYXlsb2FkID0gcmVhZF9qc29uKElOVEVSQUNUSU9OX1BBVEgpCiAgICByZXR1cm4gcGF5bG9hZC5nZXQoInJlc3VsdHMiLCBbXSkKCmRlZiBidWlsZF9wb2xpY3lfcm93cygpIC0+IGxpc3RbZGljdFtzdHIsIEFueV1dOgogICAgcm93cyA9IFtdCiAgICBmb3IgcmVzdWx0IGluIGludGVyYWN0aW9uX3JlY29yZHMoKToKICAgICAgICBnYXRlX2EgPSByZXN1bHQuZ2V0KCJnYXRlX2EiKQogICAgICAgIGdhdGVfYiA9IHJlc3VsdC5nZXQoImdhdGVfYiIpCiAgICAgICAgcG9saWN5ID0gcGFpcl9wb2xpY3koZ2F0ZV9hLCBnYXRlX2IsIHJlc3VsdCkKICAgICAgICByb3dzLmFwcGVuZCh7CiAgICAgICAgICAgICJnYXRlX2EiOiBnYXRlX2EsCiAgICAgICAgICAgICJnYXRlX2IiOiBnYXRlX2IsCiAgICAgICAgICAgICJjdXJyZW50X2NsYXNzaWZpY2F0aW9uIjogcmVzdWx0LmdldCgiY2xhc3NpZmljYXRpb24iKSwKICAgICAgICAgICAgImN1cnJlbnRfQV9UU0VLIjogcmVzdWx0LmdldCgiQV9UU0VLIiksCiAgICAgICAgICAgICJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSI6IHJlc3VsdC5nZXQoImRpYWdub3N0aWNfYXZlcmFnZSIpLAogICAgICAgICAgICAiZmluZGluZ3NfY291bnQiOiByZXN1bHQuZ2V0KCJmaW5kaW5nc19jb3VudCIpLAogICAgICAgICAgICAiZmluZGluZ19jb2RlcyI6IHJlc3VsdC5nZXQoImZpbmRpbmdfY29kZXMiLCBbXSksCiAgICAgICAgICAgICJwb2xpY3lfY2xhc3MiOiBwb2xpY3lbInBvbGljeV9jbGFzcyJdLAogICAgICAgICAgICAicmVjb21tZW5kZWRfYWN0aW9uIjogcG9saWN5WyJyZWNvbW1lbmRlZF9hY3Rpb24iXSwKICAgICAgICAgICAgInJlYXNvbiI6IHBvbGljeVsicmVhc29uIl0sCiAgICAgICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAgICAgIm5vbl9jbGFpbV9sb2NrIjogIlBhaXIgcG9saWN5IHJldmlldyBpcyBjbGFzc2lmaWVyIGdvdmVybmFuY2Ugb25seTsgaXQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiBvciBwcm9kdWN0IGNsYWltcy4iLAogICAgICAgIH0pCiAgICByZXR1cm4gcm93cwoKZGVmIGdlbmVyYXRlX2NoYXJ0cyhyb3dzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSkgLT4gbGlzdFtzdHJdOgogICAgY2hhcnRfcGF0aHM6IGxpc3Rbc3RyXSA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgd3JpdGVfdGV4dChPVVRfRElSIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBmIm1hdHBsb3RsaWIgdW5hdmFpbGFibGU6IHtleGN9XG4iKQogICAgICAgIHJldHVybiBjaGFydF9wYXRocwoKICAgIFZJU19ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlZmlnKHBhdGg6IFBhdGgpIC0+IE5vbmU6CiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocGF0aCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIGNoYXJ0X3BhdGhzLmFwcGVuZChzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikpCgogICAgIyBQb2xpY3kgY2xhc3MgY291bnRzLgogICAgY291bnRzOiBkaWN0W3N0ciwgaW50XSA9IHt9CiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgY291bnRzW3Jvd1sicG9saWN5X2NsYXNzIl1dID0gY291bnRzLmdldChyb3dbInBvbGljeV9jbGFzcyJdLCAwKSArIDEKICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoY291bnRzLmtleXMoKSksIGxpc3QoY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC50aXRsZSgiUGFpciBQb2xpY3kgUmV2aWV3IENsYXNzZXMiKQogICAgcGx0LnlsYWJlbCgiUGFpciBjb3VudCIpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgc2F2ZWZpZyhWSVNfRElSIC8gInBhaXJfcG9saWN5X2NsYXNzX2NvdW50cy5wbmciKQoKICAgICMgTWF0cml4LgogICAgaWR4ID0ge2c6IGkgZm9yIGksIGcgaW4gZW51bWVyYXRlKEdBVEVfT1JERVIpfQogICAgbWF0cml4ID0gW1swIGZvciBfIGluIEdBVEVfT1JERVJdIGZvciBfIGluIEdBVEVfT1JERVJdCiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgaSA9IGlkeFtyb3dbImdhdGVfYSJdXQogICAgICAgIGogPSBpZHhbcm93WyJnYXRlX2IiXV0KICAgICAgICBzY29yZSA9IFNFVkVSSVRZX1NDT1JFW3Jvd1sicG9saWN5X2NsYXNzIl1dCiAgICAgICAgbWF0cml4W2ldW2pdID0gc2NvcmUKICAgICAgICBtYXRyaXhbal1baV0gPSBzY29yZQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA4KSkKICAgIGltZyA9IHBsdC5pbXNob3cobWF0cml4LCBhc3BlY3Q9ImF1dG8iLCB2bWluPTAsIHZtYXg9NCkKICAgIHBsdC50aXRsZSgiUGFpciBQb2xpY3kgU2V2ZXJpdHkgTWF0cml4IikKICAgIHBsdC54dGlja3MocmFuZ2UobGVuKEdBVEVfT1JERVIpKSwgR0FURV9PUkRFUiwgcm90YXRpb249NDUsIGhhPSJyaWdodCIpCiAgICBwbHQueXRpY2tzKHJhbmdlKGxlbihHQVRFX09SREVSKSksIEdBVEVfT1JERVIpCiAgICBwbHQuY29sb3JiYXIoaW1nLCBsYWJlbD0icG9saWN5IHNldmVyaXR5IikKICAgIHNhdmVmaWcoVklTX0RJUiAvICJwYWlyX3BvbGljeV9zZXZlcml0eV9tYXRyaXgucG5nIikKCiAgICAjIENhbmRpZGF0ZSBlc2NhbGF0aW9uIGJ5IGdhdGUuCiAgICBnYXRlX2NvdW50cyA9IHtnOiAwIGZvciBnIGluIEdBVEVfT1JERVJ9CiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgaWYgcm93WyJwb2xpY3lfY2xhc3MiXSAhPSAiVFNFSy1DX1JFVEFJTiI6CiAgICAgICAgICAgIGdhdGVfY291bnRzW3Jvd1siZ2F0ZV9hIl1dICs9IDEKICAgICAgICAgICAgZ2F0ZV9jb3VudHNbcm93WyJnYXRlX2IiXV0gKz0gMQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChnYXRlX2NvdW50cy5rZXlzKCkpLCBsaXN0KGdhdGVfY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC50aXRsZSgiRXNjYWxhdGlvbiBDYW5kaWRhdGUgRnJlcXVlbmN5IGJ5IEdhdGUiKQogICAgcGx0LnlsYWJlbCgiRXNjYWxhdGlvbiBjYW5kaWRhdGUgY291bnQiKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj00NSwgaGE9InJpZ2h0IikKICAgIHNhdmVmaWcoVklTX0RJUiAvICJlc2NhbGF0aW9uX2NhbmRpZGF0ZV9mcmVxdWVuY3lfYnlfZ2F0ZS5wbmciKQoKICAgIHJldHVybiBjaGFydF9wYXRocwoKZGVmIHN1bW1hcml6ZShyb3dzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSwgY2hhcnRzOiBsaXN0W3N0cl0pIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgcG9saWN5X2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgZ2F0ZV9lc2NhbGF0aW9uX2NvdW50cyA9IHtnOiAwIGZvciBnIGluIEdBVEVfT1JERVJ9CiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgcG9saWN5X2NvdW50c1tyb3dbInBvbGljeV9jbGFzcyJdXSA9IHBvbGljeV9jb3VudHMuZ2V0KHJvd1sicG9saWN5X2NsYXNzIl0sIDApICsgMQogICAgICAgIGlmIHJvd1sicG9saWN5X2NsYXNzIl0gIT0gIlRTRUstQ19SRVRBSU4iOgogICAgICAgICAgICBnYXRlX2VzY2FsYXRpb25fY291bnRzW3Jvd1siZ2F0ZV9hIl1dICs9IDEKICAgICAgICAgICAgZ2F0ZV9lc2NhbGF0aW9uX2NvdW50c1tyb3dbImdhdGVfYiJdXSArPSAxCgogICAgcmV2aWV3ID0gcmVhZF9qc29uKEVYUExBSU5fUEFUSCkKICAgIHJldHVybiB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1wYWlyLXBvbGljeS1yZXZpZXctZ2F0ZS12MC40LjQiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAicGFpcl9jb3VudCI6IGxlbihyb3dzKSwKICAgICAgICAicG9saWN5X2NvdW50cyI6IHBvbGljeV9jb3VudHMsCiAgICAgICAgImdhdGVfZXNjYWxhdGlvbl9jb3VudHMiOiBnYXRlX2VzY2FsYXRpb25fY291bnRzLAogICAgICAgICJwb2xpY3lfcm93cyI6IHJvd3MsCiAgICAgICAgImNoYXJ0X3BhdGhzIjogY2hhcnRzLAogICAgICAgICJpbnB1dHMiOiB7CiAgICAgICAgICAgICJleHBsYW5hdGlvbl9jYXJkX2NvdW50IjogcmV2aWV3LmdldCgiY2FyZF9jb3VudCIpLAogICAgICAgICAgICAicmV2aWV3X2NvdW50cyI6IHJldmlldy5nZXQoInJldmlld19jb3VudHMiKSwKICAgICAgICAgICAgImludGVyYWN0aW9uX21hdHJpeCI6IHN0cihJTlRFUkFDVElPTl9QQVRILnJlbGF0aXZlX3RvKFJFUE9fUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSwKICAgICAgICAgICAgImV4cGxhbmF0aW9uX2NhcmRzIjogc3RyKEVYUExBSU5fUEFUSC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIiksCiAgICAgICAgfSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNC41IHNob3VsZCBhZGQgYSBkcnktcnVuIHBvbGljeSBzaW11bGF0b3IgYmVmb3JlIGNoYW5naW5nIGNsYXNzaWZpZXIgb3V0cHV0LiIsCiAgICAgICAgImJvdW5kYXJ5IjogIlBhaXIgcG9saWN5IHJldmlldyBwcm9wb3NlcyBjbGFzc2lmaWVyLWdvdmVybmFuY2UgY2FuZGlkYXRlcyBvbmx5LiBJdCBkb2VzIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciBhbmQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQoKZGVmIHJlbmRlcl9tZChzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gc3RyOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNC40IFBhaXIgUG9saWN5IFJldmlldyBHYXRlIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gUGFpciBjb3VudDogYHtzdW1tYXJ5WydwYWlyX2NvdW50J119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzdW1tYXJ5Wydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICBmIi0gQ2hhcnQgY291bnQ6IGB7bGVuKHN1bW1hcnlbJ2NoYXJ0X3BhdGhzJ10pfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBQb2xpY3kgQ291bnRzIiwKICAgICAgICAiIiwKICAgICAgICAifCBQb2xpY3kgY2xhc3MgfCBDb3VudCB8IE1lYW5pbmcgfCIsCiAgICAgICAgInwtLS18LS0tOnwtLS18IiwKICAgIF0KICAgIG1lYW5pbmdzID0gewogICAgICAgICJUU0VLLUNfUkVUQUlOIjogIktlZXAgY3VycmVudCBjb250cm9sbGVkIGRvd25ncmFkZSBwb2xpY3kuIiwKICAgICAgICAiVFNFSy1EX0NBTkRJREFURSI6ICJDYW5kaWRhdGUgZm9yIGxvd2VyIGNsYXNzIGluIGZ1dHVyZSBwb2xpY3kgc2ltdWxhdG9yLiIsCiAgICAgICAgIlRTRUstRV9DQU5ESURBVEUiOiAiQ2FuZGlkYXRlIGhhcmQgcmVqZWN0aW9uOyBub25lIHNob3VsZCBiZSBlbmZvcmNlZCB3aXRob3V0IGRyeS1ydW4gZXZpZGVuY2UuIiwKICAgICAgICAiSFVNQU5fUkVWSUVXIjogIlJlcXVpcmUgZXhwbGljaXQgaHVtYW4gcmV2aWV3IGJlZm9yZSBwcm9tb3Rpb24uIiwKICAgIH0KICAgIGZvciBrLCB2IGluIHNvcnRlZChzdW1tYXJ5WyJwb2xpY3lfY291bnRzIl0uaXRlbXMoKSk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2t9YCB8IHt2fSB8IHttZWFuaW5ncy5nZXQoaywgJycpfSB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEdhdGUgRXNjYWxhdGlvbiBDYW5kaWRhdGUgRnJlcXVlbmN5IiwKICAgICAgICAiIiwKICAgICAgICAifCBHYXRlIHwgQ2FuZGlkYXRlIGNvdW50IHwiLAogICAgICAgICJ8LS0tfC0tLTp8IiwKICAgIF0KICAgIGZvciBnYXRlLCBjb3VudCBpbiBzb3J0ZWQoc3VtbWFyeVsiZ2F0ZV9lc2NhbGF0aW9uX2NvdW50cyJdLml0ZW1zKCksIGtleT1sYW1iZGEga3Y6ICgta3ZbMV0sIGt2WzBdKSk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2dhdGV9YCB8IHtjb3VudH0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBQb2xpY3kgUm93cyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgR2F0ZSBBIHwgR2F0ZSBCIHwgQ3VycmVudCBjbGFzcyB8IFBvbGljeSBjbGFzcyB8IEFjdGlvbiB8IFJlYXNvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwtLS18LS0tfCIsCiAgICBdCiAgICBmb3Igcm93IGluIHN1bW1hcnlbInBvbGljeV9yb3dzIl06CiAgICAgICAgYWN0aW9uID0gcm93WyJyZWNvbW1lbmRlZF9hY3Rpb24iXS5yZXBsYWNlKCJ8IiwgIlxcfCIpCiAgICAgICAgcmVhc29uID0gcm93WyJyZWFzb24iXS5yZXBsYWNlKCJ8IiwgIlxcfCIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3Jvd1snZ2F0ZV9hJ119YCB8IGB7cm93WydnYXRlX2InXX1gIHwgYHtyb3dbJ2N1cnJlbnRfY2xhc3NpZmljYXRpb24nXX1gIHwgYHtyb3dbJ3BvbGljeV9jbGFzcyddfWAgfCB7YWN0aW9ufSB8IHtyZWFzb259IHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIGNoYXJ0IGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJFUE9fUk9PVCAvIGNoYXJ0LCBPVVRfRElSKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcyArPSBbZiIhW3tQYXRoKGNoYXJ0KS5zdGVtfV0oe3JlbH0pIiwgIiJdCgogICAgbGluZXMgKz0gWwogICAgICAgICIjIyBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc3VtbWFyeVsiYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgIF0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpIC0+IE5vbmU6CiAgICByb3dzID0gYnVpbGRfcG9saWN5X3Jvd3MoKQogICAgY2hhcnRzID0gZ2VuZXJhdGVfY2hhcnRzKHJvd3MpCiAgICBzdW1tYXJ5ID0gc3VtbWFyaXplKHJvd3MsIGNoYXJ0cykKICAgIHdyaXRlX2pzb24oT1VUX0RJUiAvICJwYWlyX3BvbGljeV9yZXZpZXdfdjBfNF80Lmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfanNvbihPVVRfRElSIC8gImxhdGVzdF9wYWlyX3BvbGljeV9yZXZpZXcuanNvbiIsIHN1bW1hcnkpCiAgICBtZCA9IHJlbmRlcl9tZChzdW1tYXJ5KQogICAgd3JpdGVfdGV4dChPVVRfRElSIC8gInBhaXJfcG9saWN5X3Jldmlld192MF80XzQubWQiLCBtZCkKICAgIHdyaXRlX3RleHQoT1VUX0RJUiAvICJsYXRlc3RfcGFpcl9wb2xpY3lfcmV2aWV3Lm1kIiwgbWQpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJwYWlyX2NvdW50Ijogc3VtbWFyeVsicGFpcl9jb3VudCJdLAogICAgICAgICJwb2xpY3lfY291bnRzIjogc3VtbWFyeVsicG9saWN5X2NvdW50cyJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogc3VtbWFyeVsicG9saWN5X2VuZm9yY2VkIl0sCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3BvbGljeS9sYXRlc3RfcGFpcl9wb2xpY3lfcmV2aWV3Lm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
runner_text = base64.b64decode(runner_b64.encode("ascii")).decode("utf-8")
write(ROOT / "scripts" / "benchmarks" / "run_pair_policy_review.py", runner_text)

write(ROOT / "reports" / "policy" / "README.md", """# Pair Policy Reports

Current layer: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**

## Purpose

This folder stores classifier pair-policy review reports. These reports do not alter classifier behavior; they propose governance candidates.

## Primary command

```powershell
python scripts/benchmarks/run_pair_policy_review.py
```

## README Update Rule

Update this mini README whenever pair-policy schemas, reports, or policy interpretation rules change.

Boundary: pair policy review is local classifier governance only.
""")

write(ROOT / "visuals" / "policy" / "README.md", """# Pair Policy Visuals

Current layer: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**

## Purpose

This folder stores pair-policy severity matrices and escalation candidate charts.

## README Update Rule

Update this mini README whenever policy chart folders or chart meanings change.

Boundary: policy visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "policy" / "v0_4_4" / "README.md", """# v0.4.4 Pair Policy Charts

## Expected Charts

- `pair_policy_class_counts.png`
- `pair_policy_severity_matrix.png`
- `escalation_candidate_frequency_by_gate.png`

## README Update Rule

Update this mini README whenever chart names or chart meanings change.

Boundary: local classifier-governance diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.3[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.2[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.3 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.4 |", r)

if "| Pair policy review | `reports/policy/latest_pair_policy_review.md` |" not in r:
    r = r.replace(
        "| Explanation charts | `visuals/explanations/v0_4_3/` |\n",
        "| Explanation charts | `visuals/explanations/v0_4_3/` |\n| Pair policy review | `reports/policy/latest_pair_policy_review.md` |\n| Pair policy charts | `visuals/policy/v0_4_4/` |\n",
    )

if "python scripts/benchmarks/run_pair_policy_review.py" not in r:
    r = r.replace(
        "python scripts/benchmarks/generate_threshold_explanation_cards.py\npython scripts/release/validate_release.py",
        "python scripts/benchmarks/generate_threshold_explanation_cards.py\npython scripts/benchmarks/run_pair_policy_review.py\npython scripts/release/validate_release.py",
    )

section = """## Pair Policy Review Gate v0.4.4

v0.4.4 converts `review_pair_policy` findings into an explicit non-enforcing policy table.

Primary command:

```powershell
python scripts/benchmarks/run_pair_policy_review.py
```

Primary outputs:

```text
reports/policy/latest_pair_policy_review.json
reports/policy/latest_pair_policy_review.md
visuals/policy/v0_4_4/
```

The purpose is to answer:

```text
Which paired failures should remain TSEK-C?
Which paired failures are TSEK-D candidates?
Which paired failures require human review?
Should any pair become a TSEK-E candidate?
```

This layer does **not** change classifier output. It creates a governed decision surface for a future dry-run policy simulator.

Boundary: pair policy review is classifier governance only. It is not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Pair Policy Review Gate v0.4.4" not in r:
    r = r.replace("## Threshold Explanation Cards v0.4.3", section + "## Threshold Explanation Cards v0.4.3", 1)

if "    policy/" not in r:
    r = r.replace("  reports/\n    explanations/", "  reports/\n    policy/\n    explanations/")
    r = r.replace("  visuals/\n    explanations/", "  visuals/\n    policy/\n    explanations/")

lesson = "| L-022 | v0.4.3 produced 55 `review_pair_policy` cards and 1 `hard_reject_without_finding` card. | Explanation cards successfully exposed classifier-policy questions without mutating classifier behavior. | Pair-policy changes must pass through a non-enforcing policy review layer and then a dry-run simulator before classifier enforcement. |"
if lesson not in r:
    r = r.replace(
        "| L-021 | v0.4.2 showed every paired hard-gate failure classified as TSEK-C. | The current classifier treats paired missing gates as controlled downgrade unless overclaim or severe collapse forces TSEK-E. | Do not harden classifier thresholds until explanation cards classify whether pair-policy behavior is expected, suspicious, or promotion-repairable. |\n",
        "| L-021 | v0.4.2 showed every paired hard-gate failure classified as TSEK-C. | The current classifier treats paired missing gates as controlled downgrade unless overclaim or severe collapse forces TSEK-E. | Do not harden classifier thresholds until explanation cards classify whether pair-policy behavior is expected, suspicious, or promotion-repairable. |\n" + lesson + "\n",
    )

if "| v0.4.4 | Pair policy review gate for non-enforcing classifier-governance candidates. |" not in r:
    r = r.replace(
        "| v0.4.3 | Threshold explanation cards and promotion-repair hints. |\n",
        "| v0.4.3 | Threshold explanation cards and promotion-repair hints. |\n| v0.4.4 | Pair policy review gate for non-enforcing classifier-governance candidates. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.5 - Pair Policy Dry-Run Simulator**

Recommended goals:

- Simulate policy-class changes without mutating the classifier.
- Compare current class vs proposed policy class.
- Emit drift impact charts.
- Decide whether policy enforcement is safe.
- Preserve non-claim locks: dry-run policy simulation is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS and routing.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.3[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**",
    a,
)
if "python scripts/benchmarks/run_pair_policy_review.py" not in a:
    a = a.replace(
        "python scripts/benchmarks/generate_threshold_explanation_cards.py\npython -m unittest discover -s tests",
        "python scripts/benchmarks/generate_threshold_explanation_cards.py\npython scripts/benchmarks/run_pair_policy_review.py\npython -m unittest discover -s tests",
    )
if "Pair policy patch" not in a:
    a = a.replace(
        "| Explanation card patch | `reports/explanations/`, `visuals/explanations/`, classifier reports | release validator + explanation card report |\n",
        "| Explanation card patch | `reports/explanations/`, `visuals/explanations/`, classifier reports | release validator + explanation card report |\n| Pair policy patch | `reports/policy/`, `visuals/policy/`, explanation cards | release validator + policy review report; no classifier mutation |\n",
    )
write(agents, a)

matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.3[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate**",
    m,
)
if "| Pair policy patch |" not in m:
    m = m.replace(
        "| Explanation card patch | outer | evidence | validation | `reports/explanations/`, interaction/sensitivity reports, classifier | release validator + explanation report | `reports/explanations/latest_threshold_explanation_cards.md` |\n",
        "| Explanation card patch | outer | evidence | validation | `reports/explanations/`, interaction/sensitivity reports, classifier | release validator + explanation report | `reports/explanations/latest_threshold_explanation_cards.md` |\n| Pair policy patch | outer | validation | governance | `reports/policy/`, explanation cards, interaction matrix | release validator + policy review report | `reports/policy/latest_pair_policy_review.md` |\n",
    )
write(matrix, m)

route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.4"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["pair_policy_review"] = {
    "read_first": ["reports/explanations/latest_threshold_explanation_cards.json", "reports/interactions/latest_gate_interaction_matrix.json"],
    "validate": ["python scripts/benchmarks/run_pair_policy_review.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/policy/latest_pair_policy_review.md", "visuals/policy/v0_4_4/"],
    "mutation_lock": "Does not change classifier behavior.",
}
write_json(route_path, route)

atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.4 | Pair policy review gate |" not in t:
    t = t.replace(
        "| v0.4.3 | Threshold explanation cards | `python scripts/benchmarks/generate_threshold_explanation_cards.py` | Class explanations, repair hints, and review labels across synthetic/sensitivity/interaction results | `reports/explanations/latest_threshold_explanation_cards.md` | `visuals/explanations/v0_4_3/` |\n",
        "| v0.4.3 | Threshold explanation cards | `python scripts/benchmarks/generate_threshold_explanation_cards.py` | Class explanations, repair hints, and review labels across synthetic/sensitivity/interaction results | `reports/explanations/latest_threshold_explanation_cards.md` | `visuals/explanations/v0_4_3/` |\n| v0.4.4 | Pair policy review gate | `python scripts/benchmarks/run_pair_policy_review.py` | Non-enforcing pair-policy table based on explanation-card review labels | `reports/policy/latest_pair_policy_review.md` | `visuals/policy/v0_4_4/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_4_pair_policy_review_gate.md", f"""# TAU-SCALING-SA v0.4.4 - Pair Policy Review Gate

Generated: {GENERATED_AT}

## Purpose

Convert v0.4.3 `review_pair_policy` cards into a non-enforcing policy review table.

## Additions

- `scripts/benchmarks/run_pair_policy_review.py`
- `reports/policy/`
- `visuals/policy/v0_4_4/`
- README/AGENTS/route-map/task-matrix/benchmark-atlas updates.

## Mutation Lock

This version does not alter classifier behavior.

## Boundary

Pair policy review is local classifier governance only. It does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "policy" / "v0_4_4" / "latest_v0_4_4_status.md", f"""# Tau Scaling v0.4.4 Pair Policy Review Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary command:

```powershell
python scripts/benchmarks/run_pair_policy_review.py
```
""")

print("v0.4.4 pair policy review gate patch written")
