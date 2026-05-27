
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
        dest = ROOT / "reports" / "policy_decision" / "v0_4_8" / "backups" / f"{path.name}_before_v0_4_8_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(read(path), encoding="utf-8")

runner_b64 = "CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKCmltcG9ydCBqc29uCmltcG9ydCBvcwpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB0eXBpbmcgaW1wb3J0IEFueQoKUkVQT19ST09UID0gUGF0aChfX2ZpbGVfXykucmVzb2x2ZSgpLnBhcmVudHNbMl0KSU1QQUNUX1BBVEggPSBSRVBPX1JPT1QgLyAicmVwb3J0cyIgLyAicG9saWN5X2ltcGFjdCIgLyAibGF0ZXN0X3BvbGljeV9pbXBhY3RfY2FyZHMuanNvbiIKT1VUX0RJUiA9IFJFUE9fUk9PVCAvICJyZXBvcnRzIiAvICJwb2xpY3lfZGVjaXNpb24iClZJU19ESVIgPSBSRVBPX1JPT1QgLyAidmlzdWFscyIgLyAicG9saWN5X2RlY2lzaW9uIiAvICJ2MF80XzgiCgpkZWYgcmVhZF9qc29uKHBhdGg6IFBhdGgpIC0+IGRpY3Rbc3RyLCBBbnldOgogICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd3JpdGVfanNvbihwYXRoOiBQYXRoLCBwYXlsb2FkOiBBbnkpIC0+IE5vbmU6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhwYXlsb2FkLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3cml0ZV90ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cikgLT4gTm9uZToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIGRlY2lkZShjYXJkOiBkaWN0W3N0ciwgQW55XSkgLT4gdHVwbGVbc3RyLCBzdHIsIHN0cl06CiAgICBpbXBhY3QgPSBjYXJkLmdldCgiaW1wYWN0X2NsYXNzIikKICAgIHJpc2sgPSBjYXJkLmdldCgicmlza19sYWJlbCIpCgogICAgaWYgaW1wYWN0ID09ICJtYW51YWxfcmV2aWV3X3JlcXVpcmVkIjoKICAgICAgICByZXR1cm4gKAogICAgICAgICAgICAiREVGRVJfVE9fSFVNQU5fUkVWSUVXIiwKICAgICAgICAgICAgIm1hbnVhbF9yZXZpZXdfZ2F0ZSIsCiAgICAgICAgICAgICJEbyBub3QgZW5mb3JjZSBhdXRvbWF0aWNhbGx5LiBIdW1hbiByZXZpZXcgaXMgcmVxdWlyZWQgYmVmb3JlIGFueSBjbGFzc2lmaWVyLXBvbGljeSBtdXRhdGlvbi4iLAogICAgICAgICkKICAgIGlmIGltcGFjdCA9PSAiY29udHJvbGxlZF9wb2xpY3lfZG93bmdyYWRlIjoKICAgICAgICByZXR1cm4gKAogICAgICAgICAgICAiQVBQUk9WRV9GT1JfUkVHUkVTU0lPTl9SRVZJRVciLAogICAgICAgICAgICAiY29udHJvbGxlZF9kb3duZ3JhZGVfY2FuZGlkYXRlIiwKICAgICAgICAgICAgIkNhbmRpZGF0ZSBmb3IgZnV0dXJlIGNvbnRyb2xsZWQgZG93bmdyYWRlLCBidXQgb25seSBhZnRlciByZWdyZXNzaW9uIGFuZCBvdmVyLXBlbmFsdHkgcmV2aWV3LiIsCiAgICAgICAgKQogICAgaWYgaW1wYWN0ID09ICJoYXJkX3JlamVjdF9jYW5kaWRhdGUiOgogICAgICAgIHJldHVybiAoCiAgICAgICAgICAgICJSRUpFQ1RfRU5GT1JDRU1FTlRfRk9SX05PVyIsCiAgICAgICAgICAgICJoYXJkX3JlamVjdF9yaXNrIiwKICAgICAgICAgICAgIkRvIG5vdCBlbmZvcmNlLiBIYXJkLXJlamVjdCBwb2xpY3kgcmVxdWlyZXMgZXhwbGljaXQgcHJvdmVuYW5jZSBhbmQgcmVncmVzc2lvbiByZXZpZXcuIiwKICAgICAgICApCiAgICByZXR1cm4gKAogICAgICAgICJSRVRBSU5fQ1VSUkVOVF9CRUhBVklPUiIsCiAgICAgICAgcmlzayBvciAibG93IiwKICAgICAgICAiTm8gY2xhc3MgZHJpZnQ7IHJldGFpbiBjdXJyZW50IGJlaGF2aW9yLiIsCiAgICApCgpkZWYgZGVjaXNpb25fcm93KGNhcmQ6IGRpY3Rbc3RyLCBBbnldKSAtPiBkaWN0W3N0ciwgQW55XToKICAgIGRlY2lzaW9uLCBkZWNpc2lvbl9jbGFzcywgcmF0aW9uYWxlID0gZGVjaWRlKGNhcmQpCiAgICByZXR1cm4gewogICAgICAgICJjYXJkX2lkIjogY2FyZC5nZXQoImNhcmRfaWQiKSwKICAgICAgICAiZ2F0ZV9wYWlyIjogY2FyZC5nZXQoImdhdGVfcGFpciIpLAogICAgICAgICJnYXRlX2EiOiBjYXJkLmdldCgiZ2F0ZV9hIiksCiAgICAgICAgImdhdGVfYiI6IGNhcmQuZ2V0KCJnYXRlX2IiKSwKICAgICAgICAiY3VycmVudF9jbGFzc2lmaWNhdGlvbiI6IGNhcmQuZ2V0KCJjdXJyZW50X2NsYXNzaWZpY2F0aW9uIiksCiAgICAgICAgInNpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24iOiBjYXJkLmdldCgic2ltdWxhdGVkX3BvbGljeV9jbGFzc2lmaWNhdGlvbiIpLAogICAgICAgICJpbXBhY3RfY2xhc3MiOiBjYXJkLmdldCgiaW1wYWN0X2NsYXNzIiksCiAgICAgICAgInJpc2tfbGFiZWwiOiBjYXJkLmdldCgicmlza19sYWJlbCIpLAogICAgICAgICJkZWNpc2lvbiI6IGRlY2lzaW9uLAogICAgICAgICJkZWNpc2lvbl9jbGFzcyI6IGRlY2lzaW9uX2NsYXNzLAogICAgICAgICJkZWNpc2lvbl9yYXRpb25hbGUiOiByYXRpb25hbGUsCiAgICAgICAgImZpbmRpbmdfY29kZXMiOiBjYXJkLmdldCgiZmluZGluZ19jb2RlcyIsIFtdKSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibm9uX2NsYWltX2xvY2siOiAiUG9saWN5IGRlY2lzaW9ucyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGRlY2lzaW9ucyBvbmx5OyB0aGV5IGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uIG9yIHByb2R1Y3QgY2xhaW1zLiIsCiAgICB9CgpkZWYgZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnk6IGRpY3Rbc3RyLCBBbnldKSAtPiBsaXN0W3N0cl06CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgd3JpdGVfdGV4dChPVVRfRElSIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBmIm1hdHBsb3RsaWIgdW5hdmFpbGFibGU6IHtleGN9XG4iKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJU19ESVIubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKHBhdGg6IFBhdGgpIC0+IE5vbmU6CiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocGF0aCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocGF0aC5yZWxhdGl2ZV90byhSRVBPX1JPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikpCgogICAgZGVjaXNpb25fY291bnRzID0gc3VtbWFyeVsiZGVjaXNpb25fY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZGVjaXNpb25fY291bnRzLmtleXMoKSksIGxpc3QoZGVjaXNpb25fY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJEZWNpc2lvbiBjb3VudCIpCiAgICBwbHQudGl0bGUoIlBvbGljeSBEZWNpc2lvbiBDb3VudHMiKQogICAgc2F2ZShWSVNfRElSIC8gInBvbGljeV9kZWNpc2lvbl9jb3VudHMucG5nIikKCiAgICBjbGFzc19jb3VudHMgPSBzdW1tYXJ5WyJkZWNpc2lvbl9jbGFzc19jb3VudHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChjbGFzc19jb3VudHMua2V5cygpKSwgbGlzdChjbGFzc19jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkRlY2lzaW9uIGNsYXNzIGNvdW50IikKICAgIHBsdC50aXRsZSgiUG9saWN5IERlY2lzaW9uIENsYXNzZXMiKQogICAgc2F2ZShWSVNfRElSIC8gInBvbGljeV9kZWNpc2lvbl9jbGFzc19jb3VudHMucG5nIikKCiAgICBnYXRlX2NvdW50cyA9IHN1bW1hcnlbImRlY2lzaW9uX2dhdGVfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZV9jb3VudHMua2V5cygpKSwgbGlzdChnYXRlX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTQ1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiRGVjaXNpb24gaW52b2x2ZW1lbnQiKQogICAgcGx0LnRpdGxlKCJEZWNpc2lvbiBJbnZvbHZlbWVudCBieSBHYXRlIikKICAgIHNhdmUoVklTX0RJUiAvICJwb2xpY3lfZGVjaXNpb25fZ2F0ZV9jb3VudHMucG5nIikKCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZW5kZXJfbWQoc3VtbWFyeTogZGljdFtzdHIsIEFueV0pIC0+IHN0cjoKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjQuOCBQb2xpY3kgRGVjaXNpb24gUmVjb3JkIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gSW5wdXQgaW1wYWN0IGNhcmRzOiBge3N1bW1hcnlbJ2lucHV0X2NhcmRfY291bnQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzdW1tYXJ5Wydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICBmIi0gRmluYWwgcmVjb21tZW5kYXRpb246IGB7c3VtbWFyeVsnZmluYWxfcmVjb21tZW5kYXRpb24nXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgRGVjaXNpb24gQ291bnRzIiwKICAgICAgICAiIiwKICAgICAgICAifCBEZWNpc2lvbiB8IENvdW50IHwiLAogICAgICAgICJ8LS0tfC0tLTp8IiwKICAgIF0KICAgIGZvciBrLCB2IGluIHN1bW1hcnlbImRlY2lzaW9uX2NvdW50cyJdLml0ZW1zKCk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2t9YCB8IHt2fSB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIERlY2lzaW9uIFJvd3MiLAogICAgICAgICIiLAogICAgICAgICJ8IENhcmQgfCBHYXRlIHBhaXIgfCBDdXJyZW50IHwgU2ltdWxhdGVkIHwgSW1wYWN0IHwgRGVjaXNpb24gfCBNdXRhdGlvbiBhbGxvd2VkIHwiLAogICAgICAgICJ8LS0tfC0tLXwtLS18LS0tfC0tLXwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIHJvdyBpbiBzdW1tYXJ5WyJkZWNpc2lvbl9yb3dzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKAogICAgICAgICAgICBmInwgYHtyb3dbJ2NhcmRfaWQnXX1gIHwgYHtyb3dbJ2dhdGVfcGFpciddfWAgfCBge3Jvd1snY3VycmVudF9jbGFzc2lmaWNhdGlvbiddfWAgfCAiCiAgICAgICAgICAgIGYiYHtyb3dbJ3NpbXVsYXRlZF9wb2xpY3lfY2xhc3NpZmljYXRpb24nXX1gIHwgYHtyb3dbJ2ltcGFjdF9jbGFzcyddfWAgfCBge3Jvd1snZGVjaXNpb24nXX1gIHwgYHtyb3dbJ211dGF0aW9uX2FsbG93ZWQnXX1gIHwiCiAgICAgICAgKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIGNoYXJ0IGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJFUE9fUk9PVCAvIGNoYXJ0LCBPVVRfRElSKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcyArPSBbZiIhW3tQYXRoKGNoYXJ0KS5zdGVtfV0oe3JlbH0pIiwgIiJdCgogICAgbGluZXMgKz0gWwogICAgICAgICIjIyBEZWNpc2lvbiBMb2NrIiwKICAgICAgICAiIiwKICAgICAgICAiVGhpcyByZWNvcmQgZG9lcyBub3QgcGVybWl0IGNsYXNzaWZpZXIgbXV0YXRpb24uIEl0IG9ubHkgY29udmVydHMgaW1wYWN0IGNhcmRzIGludG8gYSBnb3Zlcm5lZCBkZWNpc2lvbiBzdXJmYWNlLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEJvdW5kYXJ5IiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJib3VuZGFyeSJdLAogICAgICAgICIiLAogICAgXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCkgLT4gTm9uZToKICAgIGltcGFjdCA9IHJlYWRfanNvbihJTVBBQ1RfUEFUSCkKICAgIGNhcmRzID0gaW1wYWN0LmdldCgiY2FyZHMiLCBbXSkKICAgIHJvd3MgPSBbZGVjaXNpb25fcm93KGNhcmQpIGZvciBjYXJkIGluIGNhcmRzXQoKICAgIGRlY2lzaW9uX2NvdW50cyA9IENvdW50ZXIocm93WyJkZWNpc2lvbiJdIGZvciByb3cgaW4gcm93cykKICAgIGRlY2lzaW9uX2NsYXNzX2NvdW50cyA9IENvdW50ZXIocm93WyJkZWNpc2lvbl9jbGFzcyJdIGZvciByb3cgaW4gcm93cykKICAgIGdhdGVfY291bnRzID0gQ291bnRlcigpCiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgZ2F0ZV9jb3VudHNbcm93WyJnYXRlX2EiXV0gKz0gMQogICAgICAgIGdhdGVfY291bnRzW3Jvd1siZ2F0ZV9iIl1dICs9IDEKCiAgICBtdXRhdGlvbl9hbGxvd2VkID0gRmFsc2UKICAgIGZpbmFsX3JlY29tbWVuZGF0aW9uID0gIm5vX2NsYXNzaWZpZXJfbXV0YXRpb25fX3ByZXBhcmVfcmVncmVzc2lvbl9yZXZpZXdfZm9yX2NvbnRyb2xsZWRfZG93bmdyYWRlcyIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctcG9saWN5LWRlY2lzaW9uLXJlY29yZC12MC40LjgiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXQiOiAicmVwb3J0cy9wb2xpY3lfaW1wYWN0L2xhdGVzdF9wb2xpY3lfaW1wYWN0X2NhcmRzLmpzb24iLAogICAgICAgICJpbnB1dF9jYXJkX2NvdW50IjogbGVuKGNhcmRzKSwKICAgICAgICAiZGVjaXNpb25fY291bnRzIjogZGljdChkZWNpc2lvbl9jb3VudHMpLAogICAgICAgICJkZWNpc2lvbl9jbGFzc19jb3VudHMiOiBkaWN0KGRlY2lzaW9uX2NsYXNzX2NvdW50cyksCiAgICAgICAgImRlY2lzaW9uX2dhdGVfY291bnRzIjogZGljdChnYXRlX2NvdW50cyksCiAgICAgICAgImRlY2lzaW9uX3Jvd3MiOiByb3dzLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogbXV0YXRpb25fYWxsb3dlZCwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogZmluYWxfcmVjb21tZW5kYXRpb24sCiAgICAgICAgImJvdW5kYXJ5IjogIlBvbGljeSBkZWNpc2lvbiByZWNvcmRzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYXJ0aWZhY3RzIG9ubHkuIFRoZXkgZG8gbm90IGNoYW5nZSBjbGFzc2lmaWVyIGJlaGF2aW9yIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjQuOSBzaG91bGQgcnVuIHJlZ3Jlc3Npb24vb3Zlci1wZW5hbHR5IHJldmlldyBmb3IgdGhlIHNpeCBjb250cm9sbGVkIGRvd25ncmFkZSBjYW5kaWRhdGVzIGJlZm9yZSBhbnkgZW5mb3JjZW1lbnQgY2FuZGlkYXRlLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gZ2VuZXJhdGVfY2hhcnRzKHN1bW1hcnkpCgogICAgT1VUX0RJUi5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAicG9saWN5X2RlY2lzaW9uX3JlY29yZF92MF80XzguanNvbiIsIHN1bW1hcnkpCiAgICB3cml0ZV9qc29uKE9VVF9ESVIgLyAibGF0ZXN0X3BvbGljeV9kZWNpc2lvbl9yZWNvcmQuanNvbiIsIHN1bW1hcnkpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAicG9saWN5X2RlY2lzaW9uX3JlY29yZF92MF80XzgubWQiLCByZW5kZXJfbWQoc3VtbWFyeSkpCiAgICB3cml0ZV90ZXh0KE9VVF9ESVIgLyAibGF0ZXN0X3BvbGljeV9kZWNpc2lvbl9yZWNvcmQubWQiLCByZW5kZXJfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJpbnB1dF9jYXJkX2NvdW50Ijogc3VtbWFyeVsiaW5wdXRfY2FyZF9jb3VudCJdLAogICAgICAgICJkZWNpc2lvbl9jb3VudHMiOiBzdW1tYXJ5WyJkZWNpc2lvbl9jb3VudHMiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogc3VtbWFyeVsicG9saWN5X2VuZm9yY2VkIl0sCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogc3VtbWFyeVsiZmluYWxfcmVjb21tZW5kYXRpb24iXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3BvbGljeV9kZWNpc2lvbi9sYXRlc3RfcG9saWN5X2RlY2lzaW9uX3JlY29yZC5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo="
write(ROOT / "scripts" / "benchmarks" / "generate_policy_decision_record.py", base64.b64decode(runner_b64.encode("ascii")).decode("utf-8"))

write(ROOT / "reports" / "policy_decision" / "README.md", """# Policy Decision Records

Current layer: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**

## Purpose

This folder stores non-mutating decision records derived from policy impact cards.

## Primary command

```powershell
python scripts/benchmarks/generate_policy_decision_record.py
```

## README Update Rule

Update this mini README whenever policy decision schemas, report paths, or decision rules change.

Boundary: policy decision records are local classifier-governance artifacts only.
""")

write(ROOT / "visuals" / "policy_decision" / "README.md", """# Policy Decision Visuals

Current layer: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**

## Purpose

This folder stores charts summarizing policy decision records.

## README Update Rule

Update this mini README whenever decision chart names or chart meanings change.

Boundary: decision visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "policy_decision" / "v0_4_8" / "README.md", """# v0.4.8 Policy Decision Charts

## Expected Charts

- `policy_decision_counts.png`
- `policy_decision_class_counts.png`
- `policy_decision_gate_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local policy-decision diagnostics only.
""")

readme = ROOT / "README.md"
backup(readme, "readme")
r = read(readme)

# Version state.
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.4\.7[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.4\.6[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.4.7 - Policy Impact Explanation Cards**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.4\.7 \|", "| Current checkpoint | TAU-SCALING-SA v0.4.8 |", r)
r = r.replace("| Agent contract version sync | v0.4.0f / updated from v0.3.3e |", "| Agent contract version sync | current / v0.4.8 |")
r = r.replace("| Task routing matrix | geometry-aware / v0.4-ready |", "| Task routing matrix | geometry-aware / v0.4.8-ready |")

# Metrics and Quick Start.
if "| Policy decision record | `reports/policy_decision/latest_policy_decision_record.md` |" not in r:
    r = r.replace("| Policy impact charts | `visuals/policy_impact/v0_4_7/` |\n",
                  "| Policy impact charts | `visuals/policy_impact/v0_4_7/` |\n| Policy decision record | `reports/policy_decision/latest_policy_decision_record.md` |\n| Policy decision charts | `visuals/policy_decision/v0_4_8/` |\n")

if "python scripts/benchmarks/generate_policy_decision_record.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_policy_impact_cards.py\npython scripts/feedback/run_nexus_feedback.py",
                  "python scripts/benchmarks/generate_policy_impact_cards.py\npython scripts/benchmarks/generate_policy_decision_record.py\npython scripts/feedback/run_nexus_feedback.py")

# Directory box repair for surfaces created in v0.4.6, v0.4.7, v0.4.8.
if "    policy_dry_run/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    policy_dry_run/\n    policy_impact/\n    policy_decision/\n")
if "    policy_dry_run/" not in r.split("  visuals/")[-1]:
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    policy_dry_run/\n    policy_impact/\n    policy_decision/\n")

section = """## Policy Decision Record v0.4.8

v0.4.8 converts policy impact cards into a non-mutating decision record.

Primary command:

```powershell
python scripts/benchmarks/generate_policy_decision_record.py
```

Primary outputs:

```text
reports/policy_decision/latest_policy_decision_record.json
reports/policy_decision/latest_policy_decision_record.md
visuals/policy_decision/v0_4_8/
```

This layer decides:

```text
which simulated downgrades are approved for regression review
which cases must defer to human review
which cases must not be enforced
whether classifier mutation is allowed
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
```

Boundary: policy decision records are local classifier-governance artifacts only. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Policy Decision Record v0.4.8" not in r:
    r = r.replace("## Policy Impact Explanation Cards v0.4.7", section + "## Policy Impact Explanation Cards v0.4.7", 1)

lesson = "| L-030 | v0.4.7 generated impact cards, but impact cards alone do not authorize classifier mutation. | Explanation artifacts identify drift reasons; they do not decide enforcement readiness. | Simulated policy impacts must be converted into a decision record with mutation_allowed=false until regression and over-penalty review pass. |"
if lesson not in r:
    r = r.replace("| L-029 | v0.4.6 produced 9 drift cases but drift alone is not an enforcement decision. | A dry-run simulator can show impact without explaining whether each impact is justified. | Any simulated classifier drift must receive an impact explanation card before enforcement is considered. |\n",
                  "| L-029 | v0.4.6 produced 9 drift cases but drift alone is not an enforcement decision. | A dry-run simulator can show impact without explaining whether each impact is justified. | Any simulated classifier drift must receive an impact explanation card before enforcement is considered. |\n" + lesson + "\n")

if "| v0.4.8 | Policy decision record for non-mutating enforcement readiness classification. |" not in r:
    r = r.replace("| v0.4.7 | Policy impact explanation cards for dry-run drift cases. |\n",
                  "| v0.4.7 | Policy impact explanation cards for dry-run drift cases. |\n| v0.4.8 | Policy decision record for non-mutating enforcement readiness classification. |\n")

next_section = """## Next Recommended Version

**TAU-SCALING-SA v0.4.9 - Regression and Over-Penalty Review**

Recommended goals:

- Regression-test the six controlled downgrade candidates.
- Check whether downgrades over-penalize ordinary incomplete evidence.
- Preserve classifier non-mutation until review passes.
- Preserve non-claim locks: regression review is local classifier governance only.
"""
r = re.sub(r"## Next Recommended Version\s+.*\Z", next_section, r, flags=re.S)
write(readme, r)

# AGENTS.
agents = ROOT / "AGENTS.md"
backup(agents, "agents")
a = read(agents)
a = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**", a)
if "Policy decision patch" not in a:
    a = a.replace("| Policy impact patch | `reports/policy_impact/`, `visuals/policy_impact/`, dry-run report | impact cards + release validator; no classifier mutation |\n",
                  "| Policy impact patch | `reports/policy_impact/`, `visuals/policy_impact/`, dry-run report | impact cards + release validator; no classifier mutation |\n| Policy decision patch | `reports/policy_decision/`, `visuals/policy_decision/`, impact cards | decision record + release validator; mutation_allowed must remain false |\n")
write(agents, a)

# Route map.
route_path = ROOT / "rcc" / "nexus" / "route_map.json"
backup(route_path, "route_map")
try:
    route = json.loads(read(route_path))
except Exception:
    route = {}
route["version"] = "v0.4.8"
route["updated_at"] = GENERATED_AT
route.setdefault("v0_4_routes", {})
route["v0_4_routes"]["policy_decision_record"] = {
    "read_first": ["reports/policy_impact/latest_policy_impact_cards.json", "reports/policy_dry_run/latest_pair_policy_dry_run.json"],
    "validate": ["python scripts/benchmarks/generate_policy_decision_record.py", "python scripts/feedback/run_nexus_feedback.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/policy_decision/latest_policy_decision_record.md", "visuals/policy_decision/v0_4_8/"],
    "mutation_lock": "Does not change classifier behavior; mutation_allowed must remain false."
}
write_json(route_path, route)

# Task matrix.
matrix = ROOT / "rcc" / "nexus" / "task_routing_matrix.md"
backup(matrix, "task_matrix")
m = read(matrix)
m = re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.4\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.4.8 - Policy Decision Record**", m)
if "| Policy decision patch |" not in m:
    m = m.replace("| Policy impact patch | outer | validation | governance | dry-run report + impact cards | impact report + charts + release validator | `reports/policy_impact/latest_policy_impact_cards.md` |\n",
                  "| Policy impact patch | outer | validation | governance | dry-run report + impact cards | impact report + charts + release validator | `reports/policy_impact/latest_policy_impact_cards.md` |\n| Policy decision patch | outer | validation | governance | impact cards + decision record | decision record + charts + release validator | `reports/policy_decision/latest_policy_decision_record.md` |\n")
write(matrix, m)

# Benchmark atlas.
atlas = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(atlas, "atlas")
t = read(atlas)
if "| v0.4.8 | Policy decision record |" not in t:
    t = t.replace("| v0.4.7 | Policy impact explanation cards | `python scripts/benchmarks/generate_policy_impact_cards.py` | Explains each dry-run drift case before policy decision | `reports/policy_impact/latest_policy_impact_cards.md` | `visuals/policy_impact/v0_4_7/` |\n",
                  "| v0.4.7 | Policy impact explanation cards | `python scripts/benchmarks/generate_policy_impact_cards.py` | Explains each dry-run drift case before policy decision | `reports/policy_impact/latest_policy_impact_cards.md` | `visuals/policy_impact/v0_4_7/` |\n| v0.4.8 | Policy decision record | `python scripts/benchmarks/generate_policy_decision_record.py` | Converts impact cards into non-mutating decision records | `reports/policy_decision/latest_policy_decision_record.md` | `visuals/policy_decision/v0_4_8/` |\n")
write(atlas, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_4_8_policy_decision_record.md", f"""# TAU-SCALING-SA v0.4.8 - Policy Decision Record

Generated: {GENERATED_AT}

## Purpose

Convert policy impact cards into a non-mutating policy decision record.

## Adds

- `scripts/benchmarks/generate_policy_decision_record.py`
- `reports/policy_decision/`
- `visuals/policy_decision/v0_4_8/`

## Additional repairs

- Adds missing Full Directory Box entries for policy dry-run, policy impact, and policy decision surfaces.
- Updates AGENTS/task routing/benchmark atlas for the decision layer.
- Adds L-030 to the AI Failure Learning Ledger.

## Boundary

Policy decision records are local classifier-governance artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.4.8 policy decision record patch written")
