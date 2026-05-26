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
        dest = ROOT / "reports" / "sensitivity" / "v0_4_1" / "backups" / f"{path.name}_before_v0_4_1_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhbm5vdGF0aW9ucwoKaW1wb3J0IGpzb24KaW1wb3J0IG9zCmltcG9ydCBzdGF0aXN0aWNzCmltcG9ydCB0aW1lCmZyb20gY29weSBpbXBvcnQgZGVlcGNvcHkKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aApmcm9tIHR5cGluZyBpbXBvcnQgQW55Cgpmcm9tIHRhdV9zY2FsaW5nLmNvcmUucnVudGltZSBpbXBvcnQgVGF1U2NhbGluZ1J1bnRpbWUKClJFUE9fUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdClNFRURfRElSID0gUkVQT19ST09UIC8gImNvbmZpZ3MiIC8gInNlZWRzIiAvICJzd2VlcHMiClJFUE9SVF9ESVIgPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAic2Vuc2l0aXZpdHkiClZJU19ESVIgPSBSRVBPX1JPT1QgLyAidmlzdWFscyIgLyAic2Vuc2l0aXZpdHkiIC8gInYwXzRfMSIKCmRlZiBsb2FkX2pzb24ocGF0aDogUGF0aCkgLT4gZGljdFtzdHIsIEFueV06CiAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3cml0ZV9qc29uKHBhdGg6IFBhdGgsIHBheWxvYWQ6IEFueSkgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKHBheWxvYWQsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSksIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3JpdGVfdGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiBiYXNlX3NlZWQoKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIHJldHVybiBsb2FkX2pzb24oUkVQT19ST09UIC8gImNvbmZpZ3MiIC8gInNlZWRzIiAvICJsb2dpY2ZvbGRpbmdfcHJvbW90aW9uX3BhdGhfY2xhaW1fY2FyZC5qc29uIikKCmRlZiBydW5fc2VlZChydW50aW1lOiBUYXVTY2FsaW5nUnVudGltZSwgc2VlZDogZGljdFtzdHIsIEFueV0sIHN3ZWVwOiBzdHIsIHhfbmFtZTogc3RyLCB4X3ZhbHVlOiBmbG9hdCkgLT4gZGljdFtzdHIsIEFueV06CiAgICB0MCA9IHRpbWUucGVyZl9jb3VudGVyKCkKICAgIHJlc3VsdCA9IHJ1bnRpbWUucnVuKHNlZWQpCiAgICBlbGFwc2VkX21zID0gKHRpbWUucGVyZl9jb3VudGVyKCkgLSB0MCkgKiAxMDAwLjAKICAgIGV2aWRlbmNlID0gbG9hZF9qc29uKFBhdGgocmVzdWx0LmV2aWRlbmNlX3BhdGgpKQogICAgY2xhc3NpZmljYXRpb24gPSBldmlkZW5jZVsiY2xhc3NpZmljYXRpb24iXQogICAgYWRtaXNzaWJsZSA9IGNsYXNzaWZpY2F0aW9uWyJhZG1pc3NpYmxlX2NsYWltIl0KICAgIHJldHVybiB7CiAgICAgICAgInN3ZWVwIjogc3dlZXAsCiAgICAgICAgInhfbmFtZSI6IHhfbmFtZSwKICAgICAgICAieF92YWx1ZSI6IHhfdmFsdWUsCiAgICAgICAgInJ1bl9pZCI6IHJlc3VsdC5ydW5faWQsCiAgICAgICAgImNsYXNzaWZpY2F0aW9uIjogcmVzdWx0LmNsYXNzaWZpY2F0aW9uLAogICAgICAgICJBX1RTRUsiOiByZXN1bHQuYWRtaXNzaWJsZV9zY29yZSwKICAgICAgICAiZGlhZ25vc3RpY19hdmVyYWdlIjogYWRtaXNzaWJsZS5nZXQoImRpYWdub3N0aWNfYXZlcmFnZSIsIDAuMCksCiAgICAgICAgImZpbmRpbmdzX2NvdW50IjogcmVzdWx0LmZpbmRpbmdzX2NvdW50LAogICAgICAgICJmaW5kaW5nX2NvZGVzIjogW2ZbImNvZGUiXSBmb3IgZiBpbiBjbGFzc2lmaWNhdGlvbi5nZXQoImZpbmRpbmdzIiwgW10pXSwKICAgICAgICAibG9naWNmb2xkaW5nX21hcmdpbiI6IGV2aWRlbmNlLmdldCgibG9naWNmb2xkaW5nX3N1cnZpdmFiaWxpdHkiLCB7fSkuZ2V0KCJsb2dpY2ZvbGRpbmdfbWFyZ2luIiksCiAgICAgICAgImdhbW1hX3RhdV9FVFAiOiBldmlkZW5jZS5nZXQoImVuZXJneV90aGVybWFsX3Bkbl9wdnQiLCB7fSkuZ2V0KCJnYW1tYV90YXVfRVRQIiksCiAgICAgICAgImVsYXBzZWRfbXMiOiByb3VuZChlbGFwc2VkX21zLCA0KSwKICAgICAgICAiZXZpZGVuY2VfcGF0aCI6IHN0cihQYXRoKHJlc3VsdC5ldmlkZW5jZV9wYXRoKS5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIiksCiAgICB9CgpkZWYgbWFrZV9zd2VlcHMoKSAtPiBsaXN0W2RpY3Rbc3RyLCBBbnldXToKICAgIGJhc2UgPSBiYXNlX3NlZWQoKQogICAgc2NlbmFyaW9zOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSA9IFtdCgogICAgIyBMb2dpY0ZvbGRpbmcgbWFyZ2luIHN3ZWVwOiB2ZXJ0aWNhbCBwZW5hbHR5IG1vdmVzIG1hcmdpbiBhY3Jvc3MgemVyby4KICAgICMgQmFzZSBtYXJnaW4gPSByaG8qd2lyZSAtIHN1bSBwZW5hbHRpZXMgPSAuNzUqNDIgLSAoOCs1KzMrMis0KSA9IDkuNS4KICAgIGZvciB2ZXJ0aWNhbCBpbiBbMCwgNCwgOCwgMTIsIDE2LCAyMCwgMjQsIDI4LCAzMiwgNDBdOgogICAgICAgIHNlZWQgPSBkZWVwY29weShiYXNlKQogICAgICAgIHNlZWRbImNsYWltX2NhcmQiXVsiY2xhaW1faWQiXSA9IGYic3dlZXAtbGYtdmVydGljYWwte3ZlcnRpY2FsfSIKICAgICAgICBzZWVkWyJjbGFpbV9jYXJkIl1bImNsYWltX3RleHQiXSA9ICJTZW5zaXRpdml0eSBzd2VlcDogTG9naWNGb2xkaW5nIHZlcnRpY2FsIHBlbmFsdHkgdGhyZXNob2xkLiIKICAgICAgICBzZWVkWyJsb2dpY2ZvbGRpbmdfc3Vydml2YWJpbGl0eSJdWyJleHBlY3RlZF92ZXJ0aWNhbF9wZW5hbHR5X3BzIl0gPSBmbG9hdCh2ZXJ0aWNhbCkKICAgICAgICBzY2VuYXJpb3MuYXBwZW5kKHsic3dlZXAiOiAibG9naWNmb2xkaW5nX3ZlcnRpY2FsX3BlbmFsdHkiLCAieF9uYW1lIjogInZlcnRpY2FsX3BlbmFsdHlfcHMiLCAieF92YWx1ZSI6IGZsb2F0KHZlcnRpY2FsKSwgInNlZWQiOiBzZWVkfSkKCiAgICAjIGdhbW1hX3RhdV9FVFAgc3dlZXA6IHRhdV9nYWluIGNyb3NzZXMgRVRQIHRocmVzaG9sZCBuZWFyIGRlbm9taW5hdG9yIDAuOTUqMS4wNSoxLjAyIH49IDEuMDE3NDUuCiAgICBmb3IgdGF1X2dhaW4gaW4gWzAuNzAsIDAuODUsIDAuOTUsIDEuMDAsIDEuMDIsIDEuMDUsIDEuMTAsIDEuMjIsIDEuMzUsIDEuNTBdOgogICAgICAgIHNlZWQgPSBkZWVwY29weShiYXNlKQogICAgICAgIHNlZWRbImNsYWltX2NhcmQiXVsiY2xhaW1faWQiXSA9IGYic3dlZXAtZXRwLXRhdWdhaW4te3N0cih0YXVfZ2FpbikucmVwbGFjZSgnLicsICdfJyl9IgogICAgICAgIHNlZWRbImNsYWltX2NhcmQiXVsiY2xhaW1fdGV4dCJdID0gIlNlbnNpdGl2aXR5IHN3ZWVwOiBnYW1tYV90YXVfRVRQIHRhdSBnYWluIHRocmVzaG9sZC4iCiAgICAgICAgc2VlZFsiZW5lcmd5X3RoZXJtYWxfcGRuX3B2dCJdWyJ0YXVfZ2FpbiJdID0gZmxvYXQodGF1X2dhaW4pCiAgICAgICAgc2NlbmFyaW9zLmFwcGVuZCh7InN3ZWVwIjogImdhbW1hX3RhdV9ldHBfdGF1X2dhaW4iLCAieF9uYW1lIjogInRhdV9nYWluIiwgInhfdmFsdWUiOiBmbG9hdCh0YXVfZ2FpbiksICJzZWVkIjogc2VlZH0pCgogICAgIyBPdmVyY2xhaW0gcHJlc3N1cmU6IEFfVFNFSyBkZWNsaW5lcywgd2l0aCBoYXJkIGJsb2NrIGF0ID49MS4KICAgIGZvciBvdmVyY2xhaW0gaW4gWzAuMCwgMC4wNSwgMC4xMCwgMC4yNSwgMC41MCwgMC43MCwgMC45MCwgMC45OSwgMS4wXToKICAgICAgICBzZWVkID0gZGVlcGNvcHkoYmFzZSkKICAgICAgICBzZWVkWyJjbGFpbV9jYXJkIl1bImNsYWltX2lkIl0gPSBmInN3ZWVwLW92ZXJjbGFpbS17c3RyKG92ZXJjbGFpbSkucmVwbGFjZSgnLicsICdfJyl9IgogICAgICAgIHNlZWRbImNsYWltX2NhcmQiXVsiY2xhaW1fdGV4dCJdID0gIlNlbnNpdGl2aXR5IHN3ZWVwOiBvdmVyY2xhaW0gcHJlc3N1cmUuIgogICAgICAgIHNlZWRbIm92ZXJjbGFpbSJdID0gZmxvYXQob3ZlcmNsYWltKQogICAgICAgIHNjZW5hcmlvcy5hcHBlbmQoeyJzd2VlcCI6ICJvdmVyY2xhaW1fcHJlc3N1cmUiLCAieF9uYW1lIjogIm92ZXJjbGFpbSIsICJ4X3ZhbHVlIjogZmxvYXQob3ZlcmNsYWltKSwgInNlZWQiOiBzZWVkfSkKCiAgICByZXR1cm4gc2NlbmFyaW9zCgpkZWYgd3JpdGVfc2VlZF9tYW5pZmVzdChzY2VuYXJpb3M6IGxpc3RbZGljdFtzdHIsIEFueV1dKSAtPiBOb25lOgogICAgU0VFRF9ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgbWFuaWZlc3QgPSBbXQogICAgZm9yIHMgaW4gc2NlbmFyaW9zOgogICAgICAgIHBhdGggPSBTRUVEX0RJUiAvIGYie3NbJ3N3ZWVwJ119X197c1sneF9uYW1lJ119X197c3RyKHNbJ3hfdmFsdWUnXSkucmVwbGFjZSgnLicsICdfJyl9Lmpzb24iCiAgICAgICAgd3JpdGVfanNvbihwYXRoLCBzWyJzZWVkIl0pCiAgICAgICAgbWFuaWZlc3QuYXBwZW5kKHsKICAgICAgICAgICAgInN3ZWVwIjogc1sic3dlZXAiXSwKICAgICAgICAgICAgInhfbmFtZSI6IHNbInhfbmFtZSJdLAogICAgICAgICAgICAieF92YWx1ZSI6IHNbInhfdmFsdWUiXSwKICAgICAgICAgICAgInBhdGgiOiBzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIiksCiAgICAgICAgfSkKICAgIHdyaXRlX2pzb24oU0VFRF9ESVIgLyAic2Vuc2l0aXZpdHlfc3dlZXBfbWFuaWZlc3RfdjBfNF8xLmpzb24iLCB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1zZW5zaXRpdml0eS1zd2VlcC1tYW5pZmVzdC12MC40LjEiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAic2NlbmFyaW9zIjogbWFuaWZlc3QsCiAgICAgICAgIm5vbl9jbGFpbV9sb2NrIjogIlNlbnNpdGl2aXR5IHN3ZWVwIHNlZWRzIGFyZSBzeW50aGV0aWMgbG9jYWwgcnVudGltZSBkaWFnbm9zdGljcyBvbmx5LiIsCiAgICB9KQoKZGVmIHN1bW1hcml6ZShyZXN1bHRzOiBsaXN0W2RpY3Rbc3RyLCBBbnldXSwgY2hhcnRzOiBsaXN0W3N0cl0pIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgYnlfc3dlZXA6IGRpY3Rbc3RyLCBBbnldID0ge30KICAgIGZvciBzd2VlcCBpbiBzb3J0ZWQoe3JbInN3ZWVwIl0gZm9yIHIgaW4gcmVzdWx0c30pOgogICAgICAgIHJvd3MgPSBbciBmb3IgciBpbiByZXN1bHRzIGlmIHJbInN3ZWVwIl0gPT0gc3dlZXBdCiAgICAgICAgdHJhbnNpdGlvbnMgPSBbXQogICAgICAgIHByZXZpb3VzID0gTm9uZQogICAgICAgIGZvciByb3cgaW4gc29ydGVkKHJvd3MsIGtleT1sYW1iZGEgcjogclsieF92YWx1ZSJdKToKICAgICAgICAgICAgaWYgcHJldmlvdXMgYW5kIHByZXZpb3VzWyJjbGFzc2lmaWNhdGlvbiJdICE9IHJvd1siY2xhc3NpZmljYXRpb24iXToKICAgICAgICAgICAgICAgIHRyYW5zaXRpb25zLmFwcGVuZCh7CiAgICAgICAgICAgICAgICAgICAgImZyb21feCI6IHByZXZpb3VzWyJ4X3ZhbHVlIl0sCiAgICAgICAgICAgICAgICAgICAgInRvX3giOiByb3dbInhfdmFsdWUiXSwKICAgICAgICAgICAgICAgICAgICAiZnJvbV9jbGFzcyI6IHByZXZpb3VzWyJjbGFzc2lmaWNhdGlvbiJdLAogICAgICAgICAgICAgICAgICAgICJ0b19jbGFzcyI6IHJvd1siY2xhc3NpZmljYXRpb24iXSwKICAgICAgICAgICAgICAgIH0pCiAgICAgICAgICAgIHByZXZpb3VzID0gcm93CiAgICAgICAgYnlfc3dlZXBbc3dlZXBdID0gewogICAgICAgICAgICAicG9pbnRzIjogbGVuKHJvd3MpLAogICAgICAgICAgICAiY2xhc3NlcyI6IHtjOiBzdW0oMSBmb3IgciBpbiByb3dzIGlmIHJbImNsYXNzaWZpY2F0aW9uIl0gPT0gYykgZm9yIGMgaW4gc29ydGVkKHtyWyJjbGFzc2lmaWNhdGlvbiJdIGZvciByIGluIHJvd3N9KX0sCiAgICAgICAgICAgICJtaW5fQV9UU0VLIjogbWluKHJbIkFfVFNFSyJdIGZvciByIGluIHJvd3MpLAogICAgICAgICAgICAibWF4X0FfVFNFSyI6IG1heChyWyJBX1RTRUsiXSBmb3IgciBpbiByb3dzKSwKICAgICAgICAgICAgIm1pbl9kaWFnbm9zdGljX2F2ZXJhZ2UiOiBtaW4oclsiZGlhZ25vc3RpY19hdmVyYWdlIl0gZm9yIHIgaW4gcm93cyksCiAgICAgICAgICAgICJtYXhfZGlhZ25vc3RpY19hdmVyYWdlIjogbWF4KHJbImRpYWdub3N0aWNfYXZlcmFnZSJdIGZvciByIGluIHJvd3MpLAogICAgICAgICAgICAidHJhbnNpdGlvbnMiOiB0cmFuc2l0aW9ucywKICAgICAgICB9CiAgICByZXR1cm4gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctc2Vuc2l0aXZpdHktc3dlZXAtdjAuNC4xIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgInRvdGFsX3BvaW50cyI6IGxlbihyZXN1bHRzKSwKICAgICAgICAic3dlZXBzIjogYnlfc3dlZXAsCiAgICAgICAgIm1lYW5fZWxhcHNlZF9tcyI6IHJvdW5kKHN0YXRpc3RpY3MubWVhbihyWyJlbGFwc2VkX21zIl0gZm9yIHIgaW4gcmVzdWx0cyksIDQpLAogICAgICAgICJyZXN1bHRzIjogcmVzdWx0cywKICAgICAgICAiY2hhcnRfcGF0aHMiOiBjaGFydHMsCiAgICAgICAgImJvdW5kYXJ5IjogIlNlbnNpdGl2aXR5IHN3ZWVwcyBhcmUgc3ludGhldGljIGxvY2FsIHJ1bnRpbWUgZGlhZ25vc3RpY3Mgb25seS4gVGhleSBhcmUgbm90IHNpbGljb24gdmFsaWRhdGlvbiwgcHJvZHVjdCB2YWxpZGF0aW9uLCBtYW51ZmFjdHVyaW5nIHZhbGlkYXRpb24sIHByb2Nlc3Mtbm9kZSBlcXVpdmFsZW5jZSwgYmVuY2htYXJrIHN1cGVyaW9yaXR5IHByb29mLCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgcHJvb2YuIiwKICAgIH0KCmRlZiBnZW5lcmF0ZV9jaGFydHMocmVzdWx0czogbGlzdFtkaWN0W3N0ciwgQW55XV0pIC0+IGxpc3Rbc3RyXToKICAgIGNoYXJ0X3BhdGhzOiBsaXN0W3N0cl0gPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHdyaXRlX3RleHQoUkVQT1JUX0RJUiAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0IiwgZiJtYXRwbG90bGliIHVuYXZhaWxhYmxlOiB7ZXhjfVxuIikKICAgICAgICByZXR1cm4gY2hhcnRfcGF0aHMKCiAgICBWSVNfRElSLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIGNsYXNzX3RvX3kgPSB7IlRTRUstRSI6IDAsICJUU0VLLUQiOiAxLCAiVFNFSy1DIjogMiwgIlRTRUstQiI6IDMsICJUU0VLLUEiOiA0fQoKICAgIGRlZiBzYXZlZmlnKHBhdGg6IFBhdGgpIC0+IE5vbmU6CiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocGF0aCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIGNoYXJ0X3BhdGhzLmFwcGVuZChzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikpCgogICAgZm9yIHN3ZWVwIGluIHNvcnRlZCh7clsic3dlZXAiXSBmb3IgciBpbiByZXN1bHRzfSk6CiAgICAgICAgcm93cyA9IHNvcnRlZChbciBmb3IgciBpbiByZXN1bHRzIGlmIHJbInN3ZWVwIl0gPT0gc3dlZXBdLCBrZXk9bGFtYmRhIHI6IHJbInhfdmFsdWUiXSkKICAgICAgICB4cyA9IFtyWyJ4X3ZhbHVlIl0gZm9yIHIgaW4gcm93c10KCiAgICAgICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA1KSkKICAgICAgICBwbHQucGxvdCh4cywgW3JbIkFfVFNFSyJdIGZvciByIGluIHJvd3NdLCBtYXJrZXI9Im8iKQogICAgICAgIHBsdC50aXRsZShmIkFfVFNFSyBzZW5zaXRpdml0eSAtIHtzd2VlcH0iKQogICAgICAgIHBsdC54bGFiZWwocm93c1swXVsieF9uYW1lIl0pCiAgICAgICAgcGx0LnlsYWJlbCgiQV9UU0VLIikKICAgICAgICBzYXZlZmlnKFZJU19ESVIgLyBmIntzd2VlcH1fYV90c2VrX2N1cnZlLnBuZyIpCgogICAgICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNSkpCiAgICAgICAgcGx0LnBsb3QoeHMsIFtyWyJkaWFnbm9zdGljX2F2ZXJhZ2UiXSBmb3IgciBpbiByb3dzXSwgbWFya2VyPSJvIikKICAgICAgICBwbHQudGl0bGUoZiJEaWFnbm9zdGljIGF2ZXJhZ2Ugc2Vuc2l0aXZpdHkgLSB7c3dlZXB9IikKICAgICAgICBwbHQueGxhYmVsKHJvd3NbMF1bInhfbmFtZSJdKQogICAgICAgIHBsdC55bGFiZWwoImRpYWdub3N0aWNfYXZlcmFnZSIpCiAgICAgICAgc2F2ZWZpZyhWSVNfRElSIC8gZiJ7c3dlZXB9X2RpYWdub3N0aWNfYXZlcmFnZV9jdXJ2ZS5wbmciKQoKICAgICAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDUpKQogICAgICAgIHBsdC5zdGVwKHhzLCBbY2xhc3NfdG9feS5nZXQoclsiY2xhc3NpZmljYXRpb24iXSwgLTEpIGZvciByIGluIHJvd3NdLCB3aGVyZT0ibWlkIikKICAgICAgICBwbHQueXRpY2tzKGxpc3QoY2xhc3NfdG9feS52YWx1ZXMoKSksIGxpc3QoY2xhc3NfdG9feS5rZXlzKCkpKQogICAgICAgIHBsdC50aXRsZShmIkNsYXNzIHRyYW5zaXRpb24gY3VydmUgLSB7c3dlZXB9IikKICAgICAgICBwbHQueGxhYmVsKHJvd3NbMF1bInhfbmFtZSJdKQogICAgICAgIHBsdC55bGFiZWwoIlRTRUsgY2xhc3MiKQogICAgICAgIHNhdmVmaWcoVklTX0RJUiAvIGYie3N3ZWVwfV9jbGFzc190cmFuc2l0aW9uX2N1cnZlLnBuZyIpCgogICAgIyBDb21iaW5lZCBjbGFzcyB0cmFuc2l0aW9uIHN1cmZhY2UuCiAgICBzd2VlcHMgPSBzb3J0ZWQoe3JbInN3ZWVwIl0gZm9yIHIgaW4gcmVzdWx0c30pCiAgICBtYXhfbGVuID0gbWF4KHN1bSgxIGZvciByIGluIHJlc3VsdHMgaWYgclsic3dlZXAiXSA9PSBzKSBmb3IgcyBpbiBzd2VlcHMpCiAgICBtYXRyaXggPSBbXQogICAgZm9yIHN3ZWVwIGluIHN3ZWVwczoKICAgICAgICByb3cgPSBbY2xhc3NfdG9feS5nZXQoclsiY2xhc3NpZmljYXRpb24iXSwgLTEpIGZvciByIGluIHNvcnRlZChbciBmb3IgciBpbiByZXN1bHRzIGlmIHJbInN3ZWVwIl0gPT0gc3dlZXBdLCBrZXk9bGFtYmRhIHI6IHJbInhfdmFsdWUiXSldCiAgICAgICAgcm93ID0gcm93ICsgWy0xXSAqIChtYXhfbGVuIC0gbGVuKHJvdykpCiAgICAgICAgbWF0cml4LmFwcGVuZChyb3cpCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5pbXNob3cobWF0cml4LCBhc3BlY3Q9ImF1dG8iLCB2bWluPTAsIHZtYXg9NCkKICAgIHBsdC55dGlja3MocmFuZ2UobGVuKHN3ZWVwcykpLCBzd2VlcHMpCiAgICBwbHQueGxhYmVsKCJzd2VlcCBwb2ludCBpbmRleCIpCiAgICBwbHQudGl0bGUoIlNlbnNpdGl2aXR5IGNsYXNzIHRyYW5zaXRpb24gaGVhdG1hcCIpCiAgICBwbHQuY29sb3JiYXIobGFiZWw9IlRTRUsgY2xhc3MgaW5kZXgiKQogICAgc2F2ZWZpZyhWSVNfRElSIC8gInNlbnNpdGl2aXR5X2NsYXNzX3RyYW5zaXRpb25faGVhdG1hcC5wbmciKQoKICAgIHJldHVybiBjaGFydF9wYXRocwoKZGVmIHJlbmRlcl9tYXJrZG93bihzdW1tYXJ5OiBkaWN0W3N0ciwgQW55XSkgLT4gc3RyOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNC4xIFN5bnRoZXRpYyBHYXRlIFNlbnNpdGl2aXR5IFN3ZWVwIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gVG90YWwgc3dlZXAgcG9pbnRzOiBge3N1bW1hcnlbJ3RvdGFsX3BvaW50cyddfWAiLAogICAgICAgIGYiLSBNZWFuIGVsYXBzZWQgbXM6IGB7c3VtbWFyeVsnbWVhbl9lbGFwc2VkX21zJ119YCIsCiAgICAgICAgZiItIENoYXJ0IGNvdW50OiBge2xlbihzdW1tYXJ5WydjaGFydF9wYXRocyddKX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgU3dlZXAgU3VtbWFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU3dlZXAgfCBQb2ludHMgfCBDbGFzc2VzIHwgQV9UU0VLIHJhbmdlIHwgRGlhZ25vc3RpYyBhdmcgcmFuZ2UgfCBUcmFuc2l0aW9ucyB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHN3ZWVwLCBkYXRhIGluIHN1bW1hcnlbInN3ZWVwcyJdLml0ZW1zKCk6CiAgICAgICAgY2xhc3NlcyA9ICIsICIuam9pbihmIntrfTp7dn0iIGZvciBrLCB2IGluIHNvcnRlZChkYXRhWyJjbGFzc2VzIl0uaXRlbXMoKSkpCiAgICAgICAgdHJhbnNpdGlvbnMgPSAiOyAiLmpvaW4oZiJ7dFsnZnJvbV9jbGFzcyddfS0+e3RbJ3RvX2NsYXNzJ119IEAge3RbJ2Zyb21feCddfS4ue3RbJ3RvX3gnXX0iIGZvciB0IGluIGRhdGFbInRyYW5zaXRpb25zIl0pIG9yICJub25lIgogICAgICAgIGxpbmVzLmFwcGVuZCgKICAgICAgICAgICAgZiJ8IGB7c3dlZXB9YCB8IHtkYXRhWydwb2ludHMnXX0gfCB7Y2xhc3Nlc30gfCB7ZGF0YVsnbWluX0FfVFNFSyddfS4ue2RhdGFbJ21heF9BX1RTRUsnXX0gfCB7ZGF0YVsnbWluX2RpYWdub3N0aWNfYXZlcmFnZSddfS4ue2RhdGFbJ21heF9kaWFnbm9zdGljX2F2ZXJhZ2UnXX0gfCB7dHJhbnNpdGlvbnN9IHwiCiAgICAgICAgKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIGNoYXJ0IGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJFUE9fUk9PVCAvIGNoYXJ0LCBSRVBPUlRfRElSKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcy5leHRlbmQoW2YiIVt7UGF0aChjaGFydCkuc3RlbX1dKHtyZWx9KSIsICIiXSkKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiMjIEJvdW5kYXJ5IiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJib3VuZGFyeSJdLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIHJ1bnRpbWUgPSBUYXVTY2FsaW5nUnVudGltZShSRVBPX1JPT1QpCiAgICBzY2VuYXJpb3MgPSBtYWtlX3N3ZWVwcygpCiAgICB3cml0ZV9zZWVkX21hbmlmZXN0KHNjZW5hcmlvcykKICAgIHJlc3VsdHMgPSBbcnVuX3NlZWQocnVudGltZSwgc1sic2VlZCJdLCBzWyJzd2VlcCJdLCBzWyJ4X25hbWUiXSwgc1sieF92YWx1ZSJdKSBmb3IgcyBpbiBzY2VuYXJpb3NdCiAgICBjaGFydHMgPSBnZW5lcmF0ZV9jaGFydHMocmVzdWx0cykKICAgIHN1bW1hcnkgPSBzdW1tYXJpemUocmVzdWx0cywgY2hhcnRzKQogICAgUkVQT1JUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKFJFUE9SVF9ESVIgLyAic2Vuc2l0aXZpdHlfc3dlZXBfdjBfNF8xLmpzb24iLCBzdW1tYXJ5KQogICAgd3JpdGVfanNvbihSRVBPUlRfRElSIC8gImxhdGVzdF9zZW5zaXRpdml0eV9zd2VlcC5qc29uIiwgc3VtbWFyeSkKICAgIG1kID0gcmVuZGVyX21hcmtkb3duKHN1bW1hcnkpCiAgICB3cml0ZV90ZXh0KFJFUE9SVF9ESVIgLyAic2Vuc2l0aXZpdHlfc3dlZXBfdjBfNF8xLm1kIiwgbWQpCiAgICB3cml0ZV90ZXh0KFJFUE9SVF9ESVIgLyAibGF0ZXN0X3NlbnNpdGl2aXR5X3N3ZWVwLm1kIiwgbWQpCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInRvdGFsX3BvaW50cyI6IHN1bW1hcnlbInRvdGFsX3BvaW50cyJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAic3dlZXBzIjoge2s6IHsicG9pbnRzIjogdlsicG9pbnRzIl0sICJjbGFzc2VzIjogdlsiY2xhc3NlcyJdLCAidHJhbnNpdGlvbnMiOiB2WyJ0cmFuc2l0aW9ucyJdfSBmb3IgaywgdiBpbiBzdW1tYXJ5WyJzd2VlcHMiXS5pdGVtcygpfSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvc2Vuc2l0aXZpdHkvbGF0ZXN0X3NlbnNpdGl2aXR5X3N3ZWVwLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
runner_text = base64.b64decode(runner_b64.encode("ascii")).decode("utf-8")
write(ROOT / "scripts" / "benchmarks" / "run_sensitivity_sweep.py", runner_text)

# Mini READMEs.
write(ROOT / "configs" / "seeds" / "sweeps" / "README.md", """# Sensitivity Sweep Seeds

Current layer: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**

## Purpose

This folder stores synthetic claim cards generated for gate-threshold sweeps.

## README Update Rule

Update this mini README whenever sweep parameters, seed generation logic, or sensitivity boundaries change.

Boundary: sweep seeds are local runtime diagnostics only, not silicon/product validation.
""")

write(ROOT / "reports" / "sensitivity" / "README.md", """# Sensitivity Reports

Current layer: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**

## Purpose

This folder stores sensitivity sweep reports and machine-readable sweep summaries.

## Primary command

```powershell
python scripts/benchmarks/run_sensitivity_sweep.py
```

## README Update Rule

Update this mini README whenever sensitivity reports, sweep schemas, or chart paths change.

Boundary: sensitivity reports are local runtime diagnostics only.
""")

write(ROOT / "visuals" / "sensitivity" / "README.md", """# Sensitivity Visuals

Current layer: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**

## Purpose

This folder stores threshold curves and sensitivity charts.

## README Update Rule

Update this mini README whenever sensitivity chart folders or interpretation surfaces change.

Boundary: sensitivity visuals are local runtime diagnostics only.
""")

write(ROOT / "visuals" / "sensitivity" / "v0_4_1" / "README.md", """# v0.4.1 Sensitivity Charts

## Expected Charts

- LogicFolding A_TSEK curve
- LogicFolding diagnostic average curve
- LogicFolding class transition curve
- gamma_tau_ETP A_TSEK curve
- gamma_tau_ETP diagnostic average curve
- gamma_tau_ETP class transition curve
- overclaim pressure A_TSEK curve
- overclaim pressure diagnostic average curve
- overclaim pressure class transition curve
- combined class transition heatmap

## README Update Rule

Update this mini README whenever chart names or chart meanings change.

Boundary: local runtime diagnostics only.
""")

# README update.
readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)
r = re.sub(
    r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.0f[^*]*\*\*",
    "Current checkpoint: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**",
    r,
)
r = re.sub(
    r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.0e[^*]*\*\*",
    "Previous seal: **TAU-SCALING-SA v0.4.0f - Coherence Reflection and Agent Contract Re-Sync**",
    r,
)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.0f \|", "| Current checkpoint | TAU-SCALING-SA v0.4.1 |", r)

if "| Sensitivity sweep | `reports/sensitivity/latest_sensitivity_sweep.md` |" not in r:
    r = r.replace(
        "| Reflection layer | `docs/reflection/tau_scaling_reflection_v0_4_0f.md` |\n",
        "| Reflection layer | `docs/reflection/tau_scaling_reflection_v0_4_0f.md` |\n| Sensitivity sweep | `reports/sensitivity/latest_sensitivity_sweep.md` |\n| Sensitivity charts | `visuals/sensitivity/v0_4_1/` |\n",
    )

if "python scripts/benchmarks/run_sensitivity_sweep.py" not in r:
    r = r.replace(
        "python scripts/benchmarks/run_synthetic_gate_suite.py\npython scripts/release/validate_release.py",
        "python scripts/benchmarks/run_synthetic_gate_suite.py\npython scripts/benchmarks/run_sensitivity_sweep.py\npython scripts/release/validate_release.py",
    )

section = """## Synthetic Gate Sensitivity Sweep v0.4.1

v0.4.1 moves from discrete synthetic pass/fail scenarios to threshold curves.

Primary command:

```powershell
python scripts/benchmarks/run_sensitivity_sweep.py
```

Primary outputs:

```text
configs/seeds/sweeps/sensitivity_sweep_manifest_v0_4_1.json
reports/sensitivity/latest_sensitivity_sweep.json
reports/sensitivity/latest_sensitivity_sweep.md
visuals/sensitivity/v0_4_1/
```

Current sweep families:

```text
logicfolding_vertical_penalty
gamma_tau_etp_tau_gain
overclaim_pressure
```

The purpose is to answer:

```text
Where does the gate flip?
Where does A_TSEK collapse?
Where does diagnostic_average remain stable?
Where does the class transition occur?
```

Boundary: sensitivity sweeps are synthetic local runtime diagnostics only. They are not silicon validation, product validation, manufacturing validation, process-node equivalence, benchmark superiority proof, or universal Tau Scaling proof.

"""
if "## Synthetic Gate Sensitivity Sweep v0.4.1" not in r:
    r = r.replace("## Benchmark and Finding Atlas", section + "## Benchmark and Finding Atlas", 1)

if "| v0.4.1 | Synthetic gate sensitivity sweep and threshold curves. |" not in r:
    r = r.replace(
        "| v0.4.0f | Coherence reflection and agent contract re-sync after benchmark atlas sequence. |\n",
        "| v0.4.0f | Coherence reflection and agent contract re-sync after benchmark atlas sequence. |\n| v0.4.1 | Synthetic gate sensitivity sweep and threshold curves. |\n",
    )

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.2 - Gate Interaction Matrix**

Recommended goals:

- Test paired gate failures.
- Emit gate-pair heatmaps.
- Identify compounding failures.
- Add benchmark atlas row and charts for v0.4.2.
- Preserve non-claim locks: interaction sweeps are local runtime diagnostics only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS and routing.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.0f[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**",
    a,
)
if "python scripts/benchmarks/run_sensitivity_sweep.py" not in a:
    a = a.replace(
        "python scripts/benchmarks/run_synthetic_gate_suite.py\npython -m unittest discover -s tests",
        "python scripts/benchmarks/run_synthetic_gate_suite.py\npython scripts/benchmarks/run_sensitivity_sweep.py\npython -m unittest discover -s tests",
    )
write(agents, a)

matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(
    r"Current contract: \*\*TAU-SCALING-SA v0\.4\.0f[^*]*\*\*",
    "Current contract: **TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep**",
    m,
)
write(matrix, m)

route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.1"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["sensitivity_sweep"] = {
    "read_first": ["configs/seeds/sweeps", "scripts/benchmarks/run_sensitivity_sweep.py", "reports/benchmarks/latest_synthetic_gate_suite.json", "docs/benchmarks/benchmark_atlas.md"],
    "validate": ["python scripts/benchmarks/run_sensitivity_sweep.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/sensitivity/latest_sensitivity_sweep.md", "visuals/sensitivity/v0_4_1/"],
}
write_json(route_path, route)

# Benchmark atlas append/update.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.1 | Sensitivity sweep |" not in t:
    t = t.replace(
        "| v0.4.0c | Benchmark atlas | `python scripts/release/validate_release.py` | Adds benchmark/finding navigation and per-version chart registry | `docs/benchmarks/benchmark_atlas.md` | indexed charts |\n",
        "| v0.4.0c | Benchmark atlas | `python scripts/release/validate_release.py` | Adds benchmark/finding navigation and per-version chart registry | `docs/benchmarks/benchmark_atlas.md` | indexed charts |\n| v0.4.1 | Sensitivity sweep | `python scripts/benchmarks/run_sensitivity_sweep.py` | Threshold curves for LogicFolding, gamma_tau_ETP, and overclaim pressure | `reports/sensitivity/latest_sensitivity_sweep.md` | `visuals/sensitivity/v0_4_1/` |\n",
    )
write(atlas, t)

# Release note/status.
write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_1_synthetic_gate_sensitivity_sweep.md", f"""# TAU-SCALING-SA v0.4.1 - Synthetic Gate Sensitivity Sweep

Generated: {GENERATED_AT}

## Purpose

Move from discrete synthetic gate scenarios to threshold curves.

## Additions

- `scripts/benchmarks/run_sensitivity_sweep.py`
- `configs/seeds/sweeps/`
- `reports/sensitivity/`
- `visuals/sensitivity/v0_4_1/`
- README/AGENTS/route-map/benchmark-atlas updates.

## Sweep Families

```text
logicfolding_vertical_penalty
gamma_tau_etp_tau_gain
overclaim_pressure
```

## Boundary

Sensitivity sweeps are synthetic local runtime diagnostics only. They do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, or universal Tau Scaling law.
""")

write(ROOT / "reports" / "sensitivity" / "v0_4_1" / "latest_v0_4_1_status.md", f"""# Tau Scaling v0.4.1 Sensitivity Sweep Status

Generated: {GENERATED_AT}

Status: patched; validation must pass before commit/push.

Primary command:

```powershell
python scripts/benchmarks/run_sensitivity_sweep.py
```
""")

print("v0.4.1 synthetic gate sensitivity sweep patch written")
