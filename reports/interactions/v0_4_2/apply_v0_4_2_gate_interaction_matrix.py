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
        dest = ROOT / "reports" / "interactions" / "v0_4_2" / "backups" / f"{path.name}_before_v0_4_2_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhbm5vdGF0aW9ucwoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmltcG9ydCBzdGF0aXN0aWNzCmltcG9ydCB0aW1lCmZyb20gY29weSBpbXBvcnQgZGVlcGNvcHkKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gaXRlcnRvb2xzIGltcG9ydCBjb21iaW5hdGlvbnMKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCmZyb20gdHlwaW5nIGltcG9ydCBBbnkKCmZyb20gdGF1X3NjYWxpbmcuY29yZS5ydW50aW1lIGltcG9ydCBUYXVTY2FsaW5nUnVudGltZQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KU0VFRF9ESVIgPSBSRVBPX1JPT1QgLyAiY29uZmlncyIgLyAic2VlZHMiIC8gImludGVyYWN0aW9ucyIKUkVQT1JUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJpbnRlcmFjdGlvbnMiClZJU19ESVIgPSBSRVBPX1JPT1QgLyAidmlzdWFscyIgLyAiaW50ZXJhY3Rpb25zIiAvICJ2MF80XzIiCgpHQVRFX09SREVSID0gWwogICAgIkJfc291cmNlIiwKICAgICJCX21ldHJpYyIsCiAgICAiQl9iYXNlbGluZSIsCiAgICAiQl9tZXRob2QiLAogICAgIkJfd29ya2xvYWQiLAogICAgIkJfdGF1IiwKICAgICJCX0xGIiwKICAgICJCX0VUUCIsCiAgICAiQl9QVlQiLAogICAgIkJfeWllbGQiLAogICAgIkJfZXZpZGVuY2UiLApdCgpDTEFTU19UT19ZID0geyJUU0VLLUUiOiAwLCAiVFNFSy1EIjogMSwgIlRTRUstQyI6IDIsICJUU0VLLUIiOiAzLCAiVFNFSy1BIjogNH0KCmRlZiBsb2FkX2pzb24ocGF0aDogUGF0aCkgLT4gZGljdFtzdHIsIEFueV06CiAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3cml0ZV9qc29uKHBhdGg6IFBhdGgsIHBheWxvYWQ6IEFueSkgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKHBheWxvYWQsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSksIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3JpdGVfdGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiBiYXNlX3NlZWQoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHJldHVybiBsb2FkX2pzb24oUkVQT19ST09UIC8gImNvbmZpZ3MiIC8gInNlZWRzIiAvICJsb2dpY2ZvbGRpbmdfcHJvbW90aW9uX3BhdGhfY2xhaW1fY2FyZC5qc29uIikKCmRlZiBmYWlsX2dhdGUoc2VlZDogZGljdFtzdHIsIEFueV0sIGdhdGU6IHN0cikgLT4gZGljdFtzdHIsIEFueV06CiAgICBzZWVkID0gZGVlcGNvcHkoc2VlZCkKICAgIGlmIGdhdGUgPT0gIkJfc291cmNlIjoKICAgICAgICBzZWVkLnNldGRlZmF1bHQoInNvdXJjZV9ib3VuZGFyeSIsIHt9KVsic291cmNlX2RlY2xhcmVkIl0gPSBGYWxzZQogICAgICAgIHNlZWRbInNvdXJjZV9ib3VuZGFyeSJdWyJyZXBvcnRlZF9jbGFpbXNfc2VwYXJhdGVkX2Zyb21fdmFsaWRhdGlvbiJdID0gRmFsc2UKICAgIGVsaWYgZ2F0ZSA9PSAiQl9tZXRyaWMiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgiY2xhaW1fY2FyZCIsIHt9KVsiY2xhaW1fdGV4dCJdID0gIiIKICAgICAgICBzZWVkWyJjbGFpbV9jYXJkIl1bImNsYWltX3R5cGUiXSA9ICIiCiAgICBlbGlmIGdhdGUgPT0gIkJfYmFzZWxpbmUiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgidGF1X3ZlY3RvciIsIHt9KS5wb3AoImJhc2VsaW5lIiwgTm9uZSkKICAgIGVsaWYgZ2F0ZSA9PSAiQl9tZXRob2QiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgieWllbGRfbWV0aG9kX2Rpc2Nsb3N1cmUiLCB7fSlbIm1ldGhvZF9kaXNjbG9zZWQiXSA9IEZhbHNlCiAgICBlbGlmIGdhdGUgPT0gIkJfd29ya2xvYWQiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgid29ya2xvYWRfcHJvZmlsZSIsIHt9KVsid29ya2xvYWRfY2xhc3MiXSA9ICIiCiAgICAgICAgc2VlZFsid29ya2xvYWRfcHJvZmlsZSJdWyJkb21pbmFudF90YXVfdGVybSJdID0gIiIKICAgIGVsaWYgZ2F0ZSA9PSAiQl90YXUiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgidGF1X3ZlY3RvciIsIHt9KVsid2VpZ2h0c19kZWNsYXJlZCJdID0gRmFsc2UKICAgICAgICBzZWVkWyJ0YXVfdmVjdG9yIl1bImRvbWluYW50X3RhdV9pbXByb3ZlZCJdID0gRmFsc2UKICAgIGVsaWYgZ2F0ZSA9PSAiQl9MRiI6CiAgICAgICAgc2VlZC5zZXRkZWZhdWx0KCJsb2dpY2ZvbGRpbmdfc3Vydml2YWJpbGl0eSIsIHt9KVsiZXhwZWN0ZWRfdmVydGljYWxfcGVuYWx0eV9wcyJdID0gOTAuMAogICAgICAgIHNlZWRbImxvZ2ljZm9sZGluZ19zdXJ2aXZhYmlsaXR5Il1bInJvdXRpbmdfcGVuYWx0eV9wcyJdID0gMjUuMAogICAgICAgIHNlZWRbImxvZ2ljZm9sZGluZ19zdXJ2aXZhYmlsaXR5Il1bInN5bmNfcGVuYWx0eV9wcyJdID0gMTUuMAogICAgICAgIHNlZWRbImxvZ2ljZm9sZGluZ19zdXJ2aXZhYmlsaXR5Il1bInZhcmlhdGlvbl9wZW5hbHR5X3BzIl0gPSAxNS4wCiAgICAgICAgc2VlZFsibG9naWNmb2xkaW5nX3N1cnZpdmFiaWxpdHkiXVsiY2xvc3VyZV9wZW5hbHR5X3BzIl0gPSAyMC4wCiAgICBlbGlmIGdhdGUgPT0gIkJfRVRQIjoKICAgICAgICBzZWVkLnNldGRlZmF1bHQoImVuZXJneV90aGVybWFsX3Bkbl9wdnQiLCB7fSlbInRhdV9nYWluIl0gPSAwLjg1CiAgICAgICAgc2VlZFsiZW5lcmd5X3RoZXJtYWxfcGRuX3B2dCJdWyJlbmVyZ3lfcmF0aW9fbmV3X292ZXJfb2xkIl0gPSAxLjQwCiAgICAgICAgc2VlZFsiZW5lcmd5X3RoZXJtYWxfcGRuX3B2dCJdWyJ0aGVybWFsX3JhdGlvX25ld19vdmVyX29sZCJdID0gMS40MAogICAgICAgIHNlZWRbImVuZXJneV90aGVybWFsX3Bkbl9wdnQiXVsicGRuX2Ryb29wX3JhdGlvX25ld19vdmVyX29sZCJdID0gMS40MAogICAgZWxpZiBnYXRlID09ICJCX1BWVCI6CiAgICAgICAgc2VlZC5zZXRkZWZhdWx0KCJwdnRfY2xvc3VyZSIsIHt9KVsicG9zdF9yb3V0ZV9jbG9zdXJlX3Bhc3NlZCJdID0gRmFsc2UKICAgICAgICBzZWVkWyJwdnRfY2xvc3VyZSJdWyJwdnRfdmFyaWF0aW9uX3Bhc3NlZCJdID0gRmFsc2UKICAgICAgICBzZWVkWyJwdnRfY2xvc3VyZSJdWyJwZG5fcmVwb3J0ZWQiXSA9IEZhbHNlCiAgICBlbGlmIGdhdGUgPT0gIkJfeWllbGQiOgogICAgICAgIHNlZWQuc2V0ZGVmYXVsdCgieWllbGRfbWV0aG9kX2Rpc2Nsb3N1cmUiLCB7fSlbInlpZWxkX3JlcG9ydGVkIl0gPSBGYWxzZQogICAgZWxpZiBnYXRlID09ICJCX2V2aWRlbmNlIjoKICAgICAgICBzZWVkLnNldGRlZmF1bHQoImV2aWRlbmNlX2Rpc2Nsb3N1cmUiLCB7fSlbImV2aWRlbmNlX3BhY2thZ2VfY29tcGxldGUiXSA9IEZhbHNlCiAgICBlbHNlOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZiJ1bmtub3duIGdhdGU6IHtnYXRlfSIpCiAgICByZXR1cm4gc2VlZAoKZGVmIHNjZW5hcmlvX3NlZWQoZ2F0ZV9hOiBzdHIsIGdhdGVfYjogc3RyKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHNlZWQgPSBiYXNlX3NlZWQoKQogICAgc2VlZCA9IGZhaWxfZ2F0ZShzZWVkLCBnYXRlX2EpCiAgICBzZWVkID0gZmFpbF9nYXRlKHNlZWQsIGdhdGVfYikKICAgIHNlZWQuc2V0ZGVmYXVsdCgiY2xhaW1fY2FyZCIsIHt9KVsiY2xhaW1faWQiXSA9IGYiaW50ZXJhY3Rpb24te2dhdGVfYX0te2dhdGVfYn0iLnJlcGxhY2UoIl8iLCAiLSIpCiAgICBzZWVkWyJjbGFpbV9jYXJkIl1bImNsYWltX3RleHQiXSA9IGYiR2F0ZSBpbnRlcmFjdGlvbiBtYXRyaXggc2NlbmFyaW86IHtnYXRlX2F9ICsge2dhdGVfYn0uIgogICAgc2VlZC5zZXRkZWZhdWx0KCJtZXRhZGF0YSIsIHt9KVsiaW50ZXJhY3Rpb25fZ2F0ZXMiXSA9IFtnYXRlX2EsIGdhdGVfYl0KICAgIHNlZWRbIm1ldGFkYXRhIl1bIm5vbl9jbGFpbV9sb2NrIl0gPSAiU3ludGhldGljIGludGVyYWN0aW9uIHNjZW5hcmlvOyBsb2NhbCBydW50aW1lIGRpYWdub3N0aWMgb25seS4iCiAgICByZXR1cm4gc2VlZAoKZGVmIHdyaXRlX3NlZWRzKCkgLT4gbGlzdFtkaWN0W3N0ciwgQW55XV06CiAgICBTRUVEX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBzY2VuYXJpb3M6IGxpc3RbZGljdFtzdHIsIEFueV1dID0gW10KICAgIGZvciBnYXRlX2EsIGdhdGVfYiBpbiBjb21iaW5hdGlvbnMoR0FURV9PUkRFUiwgMik6CiAgICAgICAgc2VlZCA9IHNjZW5hcmlvX3NlZWQoZ2F0ZV9hLCBnYXRlX2IpCiAgICAgICAgZm5hbWUgPSBmIntnYXRlX2EubG93ZXIoKX1fX3tnYXRlX2IubG93ZXIoKX0uanNvbiIKICAgICAgICBwYXRoID0gU0VFRF9ESVIgLyBmbmFtZQogICAgICAgIHdyaXRlX2pzb24ocGF0aCwgc2VlZCkKICAgICAgICBzY2VuYXJpb3MuYXBwZW5kKHsKICAgICAgICAgICAgImdhdGVfYSI6IGdhdGVfYSwKICAgICAgICAgICAgImdhdGVfYiI6IGdhdGVfYiwKICAgICAgICAgICAgInBhdGgiOiBzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIiksCiAgICAgICAgICAgICJzZWVkIjogc2VlZCwKICAgICAgICB9KQogICAgd3JpdGVfanNvbihTRUVEX0RJUiAvICJnYXRlX2ludGVyYWN0aW9uX21hbmlmZXN0X3YwXzRfMi5qc29uIiwgewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctZ2F0ZS1pbnRlcmFjdGlvbi1tYW5pZmVzdC12MC40LjIiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiZ2F0ZXMiOiBHQVRFX09SREVSLAogICAgICAgICJzY2VuYXJpb19jb3VudCI6IGxlbihzY2VuYXJpb3MpLAogICAgICAgICJzY2VuYXJpb3MiOiBbe2s6IHNba10gZm9yIGsgaW4gKCJnYXRlX2EiLCAiZ2F0ZV9iIiwgInBhdGgiKX0gZm9yIHMgaW4gc2NlbmFyaW9zXSwKICAgICAgICAibm9uX2NsYWltX2xvY2siOiAiR2F0ZSBpbnRlcmFjdGlvbiBzZWVkcyBhcmUgc3ludGhldGljIGxvY2FsIHJ1bnRpbWUgZGlhZ25vc3RpY3Mgb25seS4iLAogICAgfSkKICAgIHJldHVybiBzY2VuYXJpb3MKCmRlZiBydW5fc2NlbmFyaW8ocnVudGltZTogVGF1U2NhbGluZ1J1bnRpbWUsIHNjZW5hcmlvOiBkaWN0W3N0ciwgQW55XSkgLT4gZGljdFtzdHIsIEFueV06CiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKCkKICAgIHJlc3VsdCA9IHJ1bnRpbWUucnVuKHNjZW5hcmlvWyJzZWVkIl0pCiAgICBlbGFwc2VkX21zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgKiAxMDAwLjAKICAgIGV2aWRlbmNlID0gbG9hZF9qc29uKFBhdGgocmVzdWx0LmV2aWRlbmNlX3BhdGgpKQogICAgY2xhc3NpZmljYXRpb24gPSBldmlkZW5jZVsiY2xhc3NpZmljYXRpb24iXQogICAgYWRtaXNzaWJsZSA9IGNsYXNzaWZpY2F0aW9uWyJhZG1pc3NpYmxlX2NsYWltIl0KICAgIGZpbmRpbmdfY29kZXMgPSBbZlsiY29kZSJdIGZvciBmIGluIGNsYXNzaWZpY2F0aW9uLmdldCgiZmluZGluZ3MiLCBbXSldCiAgICByZXR1cm4gewogICAgICAgICJnYXRlX2EiOiBzY2VuYXJpb1siZ2F0ZV9hIl0sCiAgICAgICAgImdhdGVfYiI6IHNjZW5hcmlvWyJnYXRlX2IiXSwKICAgICAgICAiY2xhc3NpZmljYXRpb24iOiByZXN1bHQuY2xhc3NpZmljYXRpb24sCiAgICAgICAgImNsYXNzX2luZGV4IjogQ0xBU1NfVE9fWS5nZXQocmVzdWx0LmNsYXNzaWZpY2F0aW9uLCAtMSksCiAgICAgICAgIkFfVFNFSyI6IHJlc3VsdC5hZG1pc3NpYmxlX3Njb3JlLAogICAgICAgICJkaWFnbm9zdGljX2F2ZXJhZ2UiOiBhZG1pc3NpYmxlLmdldCgiZGlhZ25vc3RpY19hdmVyYWdlIiwgMC4wKSwKICAgICAgICAiZmluZGluZ3NfY291bnQiOiByZXN1bHQuZmluZGluZ3NfY291bnQsCiAgICAgICAgImZpbmRpbmdfY29kZXMiOiBmaW5kaW5nX2NvZGVzLAogICAgICAgICJnYXRlX3ZhbHVlcyI6IHtnOiBhZG1pc3NpYmxlLmdldChnLCAwLjApIGZvciBnIGluIEdBVEVfT1JERVJ9LAogICAgICAgICJsb2dpY2ZvbGRpbmdfbWFyZ2luIjogZXZpZGVuY2UuZ2V0KCJsb2dpY2ZvbGRpbmdfc3Vydml2YWJpbGl0eSIsIHt9KS5nZXQoImxvZ2ljZm9sZGluZ19tYXJnaW4iKSwKICAgICAgICAiZ2FtbWFfdGF1X0VUUCI6IGV2aWRlbmNlLmdldCgiZW5lcmd5X3RoZXJtYWxfcGRuX3B2dCIsIHt9KS5nZXQoImdhbW1hX3RhdV9FVFAiKSwKICAgICAgICAiZWxhcHNlZF9tcyI6IHJvdW5kKGVsYXBzZWRfbXMsIDQpLAogICAgICAgICJydW5faWQiOiByZXN1bHQucnVuX2lkLAogICAgICAgICJldmlkZW5jZV9wYXRoIjogc3RyKFBhdGgocmVzdWx0LmV2aWRlbmNlX3BhdGgpLnJlbGF0aXZlX3RvKFJFUE9fUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSwKICAgICAgICAic2NlbmFyaW9fcGFzc2VkIjogc2NlbmFyaW9bImdhdGVfYSJdIGluIEdBVEVfT1JERVIgYW5kIHNjZW5hcmlvWyJnYXRlX2IiXSBpbiBHQVRFX09SREVSLAogICAgfQoKZGVmIGJ1aWxkX21hdHJpeChyZXN1bHRzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSwgdmFsdWVfa2V5OiBzdHIpIC0+IGxpc3RbbGlzdFtmbG9hdF1dOgogICAgaWR4ID0ge2c6IGkgZm9yIGksIGcgaW4gZW51bWVyYXRlKEdBVEVfT1JERVIpfQogICAgbiA9IGxlbihHQVRFX09SREVSKQogICAgbWF0cml4ID0gW1tmbG9hdCgibmFuIikgZm9yIF8gaW4gcmFuZ2UobildIGZvciBfIGluIHJhbmdlKG4pXQogICAgZm9yIHIgaW4gcmVzdWx0czoKICAgICAgICBpLCBqID0gaWR4W3JbImdhdGVfYSJdXSwgaWR4W3JbImdhdGVfYiJdXQogICAgICAgIG1hdHJpeFtpXVtqXSA9IHJbdmFsdWVfa2V5XQogICAgICAgIG1hdHJpeFtqXVtpXSA9IHJbdmFsdWVfa2V5XQogICAgcmV0dXJuIG1hdHJpeAoKZGVmIGdlbmVyYXRlX2NoYXJ0cyhyZXN1bHRzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSkgLT4gbGlzdFtzdHJdOgogICAgY2hhcnRfcGF0aHM6IGxpc3Rbc3RyXSA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgd3JpdGVfdGV4dChSRVBPUlRfRElSIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBmIm1hdHBsb3RsaWIgdW5hdmFpbGFibGU6IHtleGN9XG4iKQogICAgICAgIHJldHVybiBjaGFydF9wYXRocwoKICAgIFZJU19ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlZmlnKHBhdGg6IFBhdGgpIC0+IE5vbmU6CiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocGF0aCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIGNoYXJ0X3BhdGhzLmFwcGVuZChzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikpCgogICAgZm9yIGtleSwgdGl0bGUsIGZpbGVuYW1lLCB2bWluLCB2bWF4LCBjYmFyIGluIFsKICAgICAgICAoImNsYXNzX2luZGV4IiwgIkdhdGUgUGFpciBDbGFzcyBUcmFuc2l0aW9uIE1hdHJpeCIsICJnYXRlX3BhaXJfY2xhc3NfbWF0cml4LnBuZyIsIDAsIDQsICJUU0VLIGNsYXNzIGluZGV4IiksCiAgICAgICAgKCJBX1RTRUsiLCAiR2F0ZSBQYWlyIEFfVFNFSyBNYXRyaXgiLCAiZ2F0ZV9wYWlyX2FfdHNla19tYXRyaXgucG5nIiwgMCwgMSwgIkFfVFNFSyIpLAogICAgICAgICgiZGlhZ25vc3RpY19hdmVyYWdlIiwgIkdhdGUgUGFpciBEaWFnbm9zdGljIEF2ZXJhZ2UgTWF0cml4IiwgImdhdGVfcGFpcl9kaWFnbm9zdGljX2F2ZXJhZ2VfbWF0cml4LnBuZyIsIDAsIDEsICJEaWFnbm9zdGljIGF2ZXJhZ2UiKSwKICAgICAgICAoImZpbmRpbmdzX2NvdW50IiwgIkdhdGUgUGFpciBGaW5kaW5nIENvdW50IE1hdHJpeCIsICJnYXRlX3BhaXJfZmluZGluZ19jb3VudF9tYXRyaXgucG5nIiwgMCwgTm9uZSwgIkZpbmRpbmdzIGNvdW50IiksCiAgICBdOgogICAgICAgIG1hdHJpeCA9IGJ1aWxkX21hdHJpeChyZXN1bHRzLCBrZXkpCiAgICAgICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA4KSkKICAgICAgICBpZiB2bWF4IGlzIE5vbmU6CiAgICAgICAgICAgIGltZyA9IHBsdC5pbXNob3cobWF0cml4LCBhc3BlY3Q9ImF1dG8iLCB2bWluPXZtaW4pCiAgICAgICAgZWxzZToKICAgICAgICAgICAgaW1nID0gcGx0Lmltc2hvdyhtYXRyaXgsIGFzcGVjdD0iYXV0byIsIHZtaW49dm1pbiwgdm1heD12bWF4KQogICAgICAgIHBsdC50aXRsZSh0aXRsZSkKICAgICAgICBwbHQueHRpY2tzKHJhbmdlKGxlbihHQVRFX09SREVSKSksIEdBVEVfT1JERVIsIHJvdGF0aW9uPTQ1LCBoYT0icmlnaHQiKQogICAgICAgIHBsdC55dGlja3MocmFuZ2UobGVuKEdBVEVfT1JERVIpKSwgR0FURV9PUkRFUikKICAgICAgICBwbHQuY29sb3JiYXIoaW1nLCBsYWJlbD1jYmFyKQogICAgICAgIHNhdmVmaWcoVklTX0RJUiAvIGZpbGVuYW1lKQoKICAgIGNsYXNzX2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgZm9yIHIgaW4gcmVzdWx0czoKICAgICAgICBjbGFzc19jb3VudHNbclsiY2xhc3NpZmljYXRpb24iXV0gPSBjbGFzc19jb3VudHMuZ2V0KHJbImNsYXNzaWZpY2F0aW9uIl0sIDApICsgMQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg3LCA0KSkKICAgIHBsdC5iYXIobGlzdChjbGFzc19jb3VudHMua2V5cygpKSwgbGlzdChjbGFzc19jb3VudHMudmFsdWVzKCkpKQogICAgcGx0LnRpdGxlKCJHYXRlIEludGVyYWN0aW9uIENsYXNzIERpc3RyaWJ1dGlvbiIpCiAgICBwbHQueWxhYmVsKCJQYWlyIGNvdW50IikKICAgIHNhdmVmaWcoVklTX0RJUiAvICJpbnRlcmFjdGlvbl9jbGFzc19kaXN0cmlidXRpb24ucG5nIikKCiAgICBzb3J0ZWRfcmVzdWx0cyA9IHNvcnRlZChyZXN1bHRzLCBrZXk9bGFtYmRhIHI6IChyWyJjbGFzc19pbmRleCJdLCByWyJBX1RTRUsiXSwgclsiZGlhZ25vc3RpY19hdmVyYWdlIl0pKQogICAgbGFiZWxzID0gW2Yie3JbJ2dhdGVfYSddfSt7clsnZ2F0ZV9iJ119IiBmb3IgciBpbiBzb3J0ZWRfcmVzdWx0c10KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTMsIDUpKQogICAgcGx0LmJhcihsYWJlbHMsIFtyWyJkaWFnbm9zdGljX2F2ZXJhZ2UiXSBmb3IgciBpbiBzb3J0ZWRfcmVzdWx0c10pCiAgICBwbHQudGl0bGUoIkRpYWdub3N0aWMgQXZlcmFnZSBieSBHYXRlIFBhaXIiKQogICAgcGx0LnlsYWJlbCgiRGlhZ25vc3RpYyBhdmVyYWdlIikKICAgIHBsdC54dGlja3Mocm90YXRpb249NzUsIGhhPSJyaWdodCIsIGZvbnRzaXplPTYpCiAgICBzYXZlZmlnKFZJU19ESVIgLyAiZGlhZ25vc3RpY19hdmVyYWdlX2J5X3BhaXIucG5nIikKCiAgICByZXR1cm4gY2hhcnRfcGF0aHMKCmRlZiBzdW1tYXJpemUocmVzdWx0czogbGlzdFtkaWN0W3N0ciwgQW55XV0sIGNoYXJ0czogbGlzdFtzdHJdKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIGNsYXNzX2NvdW50czogZGljdFtzdHIsIGludF0gPSB7fQogICAgZm9yIHIgaW4gcmVzdWx0czoKICAgICAgICBjbGFzc19jb3VudHNbclsiY2xhc3NpZmljYXRpb24iXV0gPSBjbGFzc19jb3VudHMuZ2V0KHJbImNsYXNzaWZpY2F0aW9uIl0sIDApICsgMQoKICAgIHN0cm9uZ2VzdF9wYWlycyA9IHNvcnRlZChyZXN1bHRzLCBrZXk9bGFtYmRhIHI6IChyWyJjbGFzc19pbmRleCJdLCByWyJkaWFnbm9zdGljX2F2ZXJhZ2UiXSwgclsiQV9UU0VLIl0pKVs6MTBdCiAgICBsZWFzdF9zZXZlcmVfcGFpcnMgPSBzb3J0ZWQocmVzdWx0cywga2V5PWxhbWJkYSByOiAoLXJbImNsYXNzX2luZGV4Il0sIC1yWyJkaWFnbm9zdGljX2F2ZXJhZ2UiXSwgLXJbIkFfVFNFSyJdKSlbOjEwXQoKICAgIHJldHVybiB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1nYXRlLWludGVyYWN0aW9uLW1hdHJpeC12MC40LjIiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiZ2F0ZV9jb3VudCI6IGxlbihHQVRFX09SREVSKSwKICAgICAgICAicGFpcl9jb3VudCI6IGxlbihyZXN1bHRzKSwKICAgICAgICAiYWxsX3BhaXJzX2V4ZWN1dGVkIjogbGVuKHJlc3VsdHMpID09IChsZW4oR0FURV9PUkRFUikgKiAobGVuKEdBVEVfT1JERVIpIC0gMSkgLy8gMiksCiAgICAgICAgImNsYXNzX2NvdW50cyI6IGNsYXNzX2NvdW50cywKICAgICAgICAibWVhbl9BX1RTRUsiOiByb3VuZChzdGF0aXN0aWNzLm1lYW4oclsiQV9UU0VLIl0gZm9yIHIgaW4gcmVzdWx0cyksIDQpLAogICAgICAgICJtZWFuX2RpYWdub3N0aWNfYXZlcmFnZSI6IHJvdW5kKHN0YXRpc3RpY3MubWVhbihyWyJkaWFnbm9zdGljX2F2ZXJhZ2UiXSBmb3IgciBpbiByZXN1bHRzKSwgNCksCiAgICAgICAgIm1lYW5fZWxhcHNlZF9tcyI6IHJvdW5kKHN0YXRpc3RpY3MubWVhbihyWyJlbGFwc2VkX21zIl0gZm9yIHIgaW4gcmVzdWx0cyksIDQpLAogICAgICAgICJzdHJvbmdlc3RfZG93bmdyYWRlX3BhaXJzIjogc3Ryb25nZXN0X3BhaXJzLAogICAgICAgICJsZWFzdF9zZXZlcmVfcGFpcnMiOiBsZWFzdF9zZXZlcmVfcGFpcnMsCiAgICAgICAgInJlc3VsdHMiOiByZXN1bHRzLAogICAgICAgICJjaGFydF9wYXRocyI6IGNoYXJ0cywKICAgICAgICAiYm91bmRhcnkiOiAiR2F0ZSBpbnRlcmFjdGlvbiBtYXRyaWNlcyBhcmUgc3ludGhldGljIGxvY2FsIHJ1bnRpbWUgZGlhZ25vc3RpY3Mgb25seS4gVGhleSBhcmUgbm90IHNpbGljb24gdmFsaWRhdGlvbiwgcHJvZHVjdCB2YWxpZGF0aW9uLCBtYW51ZmFjdHVyaW5nIHZhbGlkYXRpb24sIHByb2Nlc3Mtbm9kZSBlcXVpdmFsZW5jZSwgYmVuY2htYXJrIHN1cGVyaW9yaXR5IHByb29mLCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgcHJvb2YuIiwKICAgIH0KCmRlZiByZW5kZXJfbWFya2Rvd24oc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjQuMiBHYXRlIEludGVyYWN0aW9uIE1hdHJpeCIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIEdhdGVzOiBge3N1bW1hcnlbJ2dhdGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gR2F0ZSBwYWlyczogYHtzdW1tYXJ5WydwYWlyX2NvdW50J119YCIsCiAgICAgICAgZiItIEFsbCBwYWlycyBleGVjdXRlZDogYHtzdW1tYXJ5WydhbGxfcGFpcnNfZXhlY3V0ZWQnXX1gIiwKICAgICAgICBmIi0gTWVhbiBBX1RTRUs6IGB7c3VtbWFyeVsnbWVhbl9BX1RTRUsnXX1gIiwKICAgICAgICBmIi0gTWVhbiBkaWFnbm9zdGljIGF2ZXJhZ2U6IGB7c3VtbWFyeVsnbWVhbl9kaWFnbm9zdGljX2F2ZXJhZ2UnXX1gIiwKICAgICAgICBmIi0gQ2hhcnQgY291bnQ6IGB7bGVuKHN1bW1hcnlbJ2NoYXJ0X3BhdGhzJ10pfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDbGFzcyBDb3VudHMiLAogICAgICAgICIiLAogICAgICAgICJ8IENsYXNzIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGNscywgY291bnQgaW4gc29ydGVkKHN1bW1hcnlbImNsYXNzX2NvdW50cyJdLml0ZW1zKCkpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtjbHN9YCB8IHtjb3VudH0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBTdHJvbmdlc3QgRG93bmdyYWRlIFBhaXJzIiwKICAgICAgICAiIiwKICAgICAgICAifCBHYXRlIEEgfCBHYXRlIEIgfCBDbGFzcyB8IEFfVFNFSyB8IERpYWdub3N0aWMgYXZnIHwgRmluZGluZ3MgfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS06fC0tLTp8LS0tOnwiLAogICAgXQogICAgZm9yIHIgaW4gc3VtbWFyeVsic3Ryb25nZXN0X2Rvd25ncmFkZV9wYWlycyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtyWydnYXRlX2EnXX1gIHwgYHtyWydnYXRlX2InXX1gIHwge3JbJ2NsYXNzaWZpY2F0aW9uJ119IHwge3JbJ0FfVFNFSyddfSB8IHtyWydkaWFnbm9zdGljX2F2ZXJhZ2UnXX0gfCB7clsnZmluZGluZ3NfY291bnQnXX0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBMZWFzdCBTZXZlcmUgUGFpcnMiLAogICAgICAgICIiLAogICAgICAgICJ8IEdhdGUgQSB8IEdhdGUgQiB8IENsYXNzIHwgQV9UU0VLIHwgRGlhZ25vc3RpYyBhdmcgfCBGaW5kaW5ncyB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLTp8LS0tOnwtLS06fCIsCiAgICBdCiAgICBmb3IgciBpbiBzdW1tYXJ5WyJsZWFzdF9zZXZlcmVfcGFpcnMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7clsnZ2F0ZV9hJ119YCB8IGB7clsnZ2F0ZV9iJ119YCB8IHtyWydjbGFzc2lmaWNhdGlvbiddfSB8IHtyWydBX1RTRUsnXX0gfCB7clsnZGlhZ25vc3RpY19hdmVyYWdlJ119IHwge3JbJ2ZpbmRpbmdzX2NvdW50J119IHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIGNoYXJ0IGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJFUE9fUk9PVCAvIGNoYXJ0LCBSRVBPUlRfRElSKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcy5leHRlbmQoW2YiIVt7UGF0aChjaGFydCkuc3RlbX1dKHtyZWx9KSIsICIiXSkKCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIHJ1bnRpbWUgPSBUYXVTY2FsaW5nUnVudGltZShSRVBPX1JPT1QpCiAgICBzY2VuYXJpb3MgPSB3cml0ZV9zZWVkcygpCiAgICByZXN1bHRzID0gW3J1bl9zY2VuYXJpbyhydW50aW1lLCBzKSBmb3IgcyBpbiBzY2VuYXJpb3NdCiAgICBjaGFydHMgPSBnZW5lcmF0ZV9jaGFydHMocmVzdWx0cykKICAgIHN1bW1hcnkgPSBzdW1tYXJpemUocmVzdWx0cywgY2hhcnRzKQogICAgUkVQT1JUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKFJFUE9SVF9ESVIgLyAiZ2F0ZV9pbnRlcmFjdGlvbl9tYXRyaXhfdjBfNF8yLmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfanNvbihSRVBPUlRfRElSIC8gImxhdGVzdF9nYXRlX2ludGVyYWN0aW9uX21hdHJpeC5qc29uIiwgc3VtbWFyeSkKICAgIG1kID0gcmVuZGVyX21hcmtkb3duKHN1bW1hcnkpCiAgICB3cml0ZV90ZXh0KFJFUE9SVF9ESVIgLyAiZ2F0ZV9pbnRlcmFjdGlvbl9tYXRyaXhfdjBfNF8yLm1kIiwgbWQpCiAgICB3cml0ZV90ZXh0KFJFUE9SVF9ESVIgLyAibGF0ZXN0X2dhdGVfaW50ZXJhY3Rpb25fbWF0cml4Lm1kIiwgbWQpCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImdhdGVfY291bnQiOiBzdW1tYXJ5WyJnYXRlX2NvdW50Il0sCiAgICAgICAgInBhaXJfY291bnQiOiBzdW1tYXJ5WyJwYWlyX2NvdW50Il0sCiAgICAgICAgImFsbF9wYWlyc19leGVjdXRlZCI6IHN1bW1hcnlbImFsbF9wYWlyc19leGVjdXRlZCJdLAogICAgICAgICJjbGFzc19jb3VudHMiOiBzdW1tYXJ5WyJjbGFzc19jb3VudHMiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL2ludGVyYWN0aW9ucy9sYXRlc3RfZ2F0ZV9pbnRlcmFjdGlvbl9tYXRyaXgubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKICAgIGlmIG5vdCBzdW1tYXJ5WyJhbGxfcGFpcnNfZXhlY3V0ZWQiXToKICAgICAgICByYWlzZSBTeXN0ZW1FeGl0KDEpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
runner_text = base64.b64decode(runner_b64.encode("ascii")).decode("utf-8")
write(ROOT / "scripts" / "benchmarks" / "run_gate_interaction_matrix.py", runner_text)

write(ROOT / "configs" / "seeds" / "interactions" / "README.md", """# Gate Interaction Seeds

Current layer: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**

## Purpose

This folder stores synthetic claim cards for paired gate-failure interactions.

## README Update Rule

Update this mini README whenever interaction seed generation, gate list, or interaction boundaries change.

Boundary: interaction seeds are synthetic local runtime diagnostics only.
""")

write(ROOT / "reports" / "interactions" / "README.md", """# Gate Interaction Reports

Current layer: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**

## Purpose

This folder stores paired gate-failure matrix reports.

## Primary command

```powershell
python scripts/benchmarks/run_gate_interaction_matrix.py
```

## README Update Rule

Update this mini README whenever interaction reports, schemas, or chart paths change.

Boundary: interaction reports are local runtime diagnostics only.
""")

write(ROOT / "visuals" / "interactions" / "README.md", """# Gate Interaction Visuals

Current layer: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**

## Purpose

This folder stores gate-pair heatmaps and interaction charts.

## README Update Rule

Update this mini README whenever interaction chart folders or interpretation surfaces change.

Boundary: interaction visuals are local runtime diagnostics only.
""")

write(ROOT / "visuals" / "interactions" / "v0_4_2" / "README.md", """# v0.4.2 Gate Interaction Charts

## Expected Charts

- `gate_pair_class_matrix.png`
- `gate_pair_a_tsek_matrix.png`
- `gate_pair_diagnostic_average_matrix.png`
- `gate_pair_finding_count_matrix.png`
- `interaction_class_distribution.png`
- `diagnostic_average_by_pair.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local runtime diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.1[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0f[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.1 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.2 |", r)

if "| Gate interaction matrix | `reports/interactions/latest_gate_interaction_matrix.md` |" not in r:
    r = r.replace(
        "| Sensitivity charts | `visuals/sensitivity/v0_4_1/` |\n",
        "| Sensitivity charts | `visuals/sensitivity/v0_4_1/` |\n| Gate interaction matrix | `reports/interactions/latest_gate_interaction_matrix.md` |\n| Interaction charts | `visuals/interactions/v0_4_2/` |\n",
    )

if "python scripts/benchmarks/run_gate_interaction_matrix.py" not in r:
    r = r.replace(
        "python scripts/benchmarks/run_sensitivity_sweep.py\npython scripts/release/validate_release.py",
        "python scripts/benchmarks/run_sensitivity_sweep.py\npython scripts/benchmarks/run_gate_interaction_matrix.py\npython scripts/release/validate_release.py",
    )

section = """## Gate Interaction Matrix v0.4.2

v0.4.2 moves from single-gate threshold curves to paired gate-failure interactions.

Primary command:

```powershell
python scripts/benchmarks/run_gate_interaction_matrix.py
```

Primary outputs:

```text
configs/seeds/interactions/gate_interaction_manifest_v0_4_2.json
reports/interactions/latest_gate_interaction_matrix.json
reports/interactions/latest_gate_interaction_matrix.md
visuals/interactions/v0_4_2/
```

The purpose is to answer:

```text
Which gates compound each other?
Which paired failures force hard downgrades?
Which pairs remain diagnostic rather than catastrophic?
Which pairings reveal classifier brittleness?
```

Boundary: interaction matrices are synthetic local runtime diagnostics only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Gate Interaction Matrix v0.4.2" not in r:
    r = r.replace("## Synthetic Gate Sensitivity Sweep v0.4.1", section + "## Synthetic Gate Sensitivity Sweep v0.4.1", 1)

if "    interactions/" not in r:
    r = r.replace("    sweeps/\n", "    sweeps/\n    interactions/\n") if "    sweeps/\n" in r else r
    r = r.replace("  reports/\n    architecture/", "  reports/\n    interactions/\n    architecture/")
    r = r.replace("  visuals/\n    reflection/", "  visuals/\n    interactions/\n    reflection/")

if "| v0.4.2 | Gate interaction matrix and paired gate-failure heatmaps. |" not in r:
    r = r.replace(
        "| v0.4.1 | Synthetic gate sensitivity sweep and threshold curves. |\n",
        "| v0.4.1 | Synthetic gate sensitivity sweep and threshold curves. |\n| v0.4.2 | Gate interaction matrix and paired gate-failure heatmaps. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.3 - Threshold Explanation Cards**

Recommended goals:

- Generate explanation cards for class transitions.
- Explain why each claim is TSEK-B/C/D/E.
- Identify the minimum evidence repair needed for promotion.
- Add benchmark atlas row and explanation reports.
- Preserve non-claim locks: explanation cards are local classifier explanations only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS and task routing.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.1[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**",
    a,
)
if "python scripts/benchmarks/run_gate_interaction_matrix.py" not in a:
    a = a.replace(
        "python scripts/benchmarks/run_sensitivity_sweep.py\npython -m unittest discover -s tests",
        "python scripts/benchmarks/run_sensitivity_sweep.py\npython scripts/benchmarks/run_gate_interaction_matrix.py\npython -m unittest discover -s tests",
    )
if "Gate interaction patch" not in a:
    a = a.replace(
        "| Sensitivity sweep patch | `configs/seeds/sweeps/`, `reports/sensitivity/`, `visuals/sensitivity/` | release validator + sensitivity report + benchmark atlas update |\n",
        "| Sensitivity sweep patch | `configs/seeds/sweeps/`, `reports/sensitivity/`, `visuals/sensitivity/` | release validator + sensitivity report + benchmark atlas update |\n| Gate interaction patch | `configs/seeds/interactions/`, `reports/interactions/`, `visuals/interactions/` | release validator + interaction matrix report + benchmark atlas update |\n",
    )
write(agents, a)

matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.1[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**",
    m,
)
if "| Gate interaction patch |" not in m:
    m = m.replace(
        "| Sensitivity sweep patch | inner | validation | tau | `configs/seeds/sweeps/`, gate formulas, benchmark atlas | release validator + sensitivity sweep report | `reports/sensitivity/latest_sensitivity_sweep.md` |\n",
        "| Sensitivity sweep patch | inner | validation | tau | `configs/seeds/sweeps/`, gate formulas, benchmark atlas | release validator + sensitivity sweep report | `reports/sensitivity/latest_sensitivity_sweep.md` |\n| Gate interaction patch | inner | validation | tau | `configs/seeds/interactions/`, gate formulas, classifier, benchmark atlas | release validator + interaction matrix report | `reports/interactions/latest_gate_interaction_matrix.md` |\n",
    )
write(matrix, m)

route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.2"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["gate_interaction_matrix"] = {
    "read_first": ["configs/seeds/interactions", "scripts/benchmarks/run_gate_interaction_matrix.py", "reports/sensitivity/latest_sensitivity_sweep.json", "docs/benchmarks/benchmark_atlas.md"],
    "validate": ["python scripts/benchmarks/run_gate_interaction_matrix.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/interactions/latest_gate_interaction_matrix.md", "visuals/interactions/v0_4_2/"],
}
write_json(route_path, route)

atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.2 | Gate interaction matrix |" not in t:
    t = t.replace(
        "| v0.4.1 | Sensitivity sweep | `python scripts/benchmarks/run_sensitivity_sweep.py` | Threshold curves for LogicFolding, gamma_tau_ETP, and overclaim pressure | `reports/sensitivity/latest_sensitivity_sweep.md` | `visuals/sensitivity/v0_4_1/` |\n",
        "| v0.4.1 | Sensitivity sweep | `python scripts/benchmarks/run_sensitivity_sweep.py` | Threshold curves for LogicFolding, gamma_tau_ETP, and overclaim pressure | `reports/sensitivity/latest_sensitivity_sweep.md` | `visuals/sensitivity/v0_4_1/` |\n| v0.4.2 | Gate interaction matrix | `python scripts/benchmarks/run_gate_interaction_matrix.py` | Pairwise gate-failure interaction matrix across hard gates | `reports/interactions/latest_gate_interaction_matrix.md` | `visuals/interactions/v0_4_2/` |\n",
    )
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_2_gate_interaction_matrix.md", f"""# TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix

Generated: {GENERATED_AT}

## Purpose

Move from single-gate sensitivity to paired gate-failure interactions.

## Additions

- `scripts/benchmarks/run_gate_interaction_matrix.py`
- `configs/seeds/interactions/`
- `reports/interactions/`
- `visuals/interactions/v0_4_2/`
- README/AGENTS/route-map/task-matrix/benchmark-atlas updates.

## Boundary

Gate interaction matrices are synthetic local runtime diagnostics only. They do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "interactions" / "v0_4_2" / "latest_v0_4_2_status.md", f"""# Tau Scaling v0.4.2 Gate Interaction Matrix Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary command:

```powershell
python scripts/benchmarks/run_gate_interaction_matrix.py
```
""")

print("v0.4.2 gate interaction matrix patch written")
