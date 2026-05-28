
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
NOW = datetime.now(timezone.utc).isoformat()

def read(p):
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""

def write(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def backup(p, label):
    if p.exists():
        d = ROOT / "reports" / "threshold_decision_record" / "v0_7_8" / "backups" / f"{p.name}_before_v0_7_8_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_threshold_decision_record.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmQiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAidGhyZXNob2xkX2RlY2lzaW9uX3JlY29yZCIgLyAidjBfN184IgoKRFJZX1JVTiA9IFJPT1QgLyAicmVwb3J0cyIgLyAidGhyZXNob2xkX3NlbnNpdGl2aXR5X2RyeV9ydW4iIC8gImxhdGVzdF90aHJlc2hvbGRfc2Vuc2l0aXZpdHlfZHJ5X3J1bi5qc29uIgpQRU5BTFRZID0gUk9PVCAvICJyZXBvcnRzIiAvICJwZW5hbHR5X2NvbnRyb2xzIiAvICJsYXRlc3Rfb3Zlcl91bmRlcl9wZW5hbHR5X25lZ2F0aXZlX2NvbnRyb2xzLmpzb24iCkJPVU5EQVJZID0gUk9PVCAvICJyZXBvcnRzIiAvICJ0c2VrX2JvdW5kYXJ5X2NhcmRzIiAvICJsYXRlc3RfdHNla19ib3VuZGFyeV9leHBsYW5hdGlvbl9jYXJkcy5qc29uIgpSRUxFQVNFID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIKCkRFQ0lTSU9OX09QVElPTlMgPSBbCiAgICAiUkVKRUNUX1RIUkVTSE9MRF9DSEFOR0UiLAogICAgIkRFRkVSX1RIUkVTSE9MRF9DSEFOR0VfUEVORElOR19NT1JFX0VWSURFTkNFIiwKICAgICJSRVZJRVdfUkVBRFlfUkVQT1JUX09OTFkiLAogICAgIkNBTkRJREFURV9CUkFOQ0hfUkVRVUlSRURfQkVGT1JFX0FOWV9NVVRBVElPTiIsCl0KCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCk6CiAgICBpZiBub3QgcGF0aC5leGlzdHMoKToKICAgICAgICByZXR1cm4geyJtaXNzaW5nIjogVHJ1ZSwgInBhdGgiOiBzdHIocGF0aCl9CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJwYXJzZV9lcnJvciI6IHN0cihleGMpLCAicGF0aCI6IHN0cihwYXRoKX0KCmRlZiB3anNvbihwYXRoOiBQYXRoLCBkYXRhKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKGRhdGEsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cik6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocGF0aDogUGF0aCk6CiAgICByZXR1cm4gc3RyKHBhdGgucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGRlY2lkZShkcnksIHBlbmFsdHksIGJvdW5kYXJ5LCByZWxlYXNlKToKICAgIHJlbGVhc2VfcGFzc2VkID0gcmVsZWFzZS5nZXQoInBhc3NlZCIpIGlzIFRydWUgYW5kIGxlbihyZWxlYXNlLmdldCgiZmluZGluZ3MiLCBbXSkpID09IDAgYW5kIGxlbihyZWxlYXNlLmdldCgic3RlcF9mYWlsdXJlcyIsIFtdKSkgPT0gMAogICAgZHJ5X3JlYWR5ID0gZHJ5LmdldCgiZHJ5X3J1bl9zdGF0dXMiKSA9PSAiVEhSRVNIT0xEX1NFTlNJVElWSVRZX0RSWV9SVU5fUkVBRFlfX1JFUE9SVF9PTkxZX05PX01VVEFUSU9OIgogICAgY29udHJvbHNfcmVhZHkgPSBwZW5hbHR5LmdldCgiY29udHJvbF9zdGF0dXMiKSA9PSAiUEVOQUxUWV9DT05UUk9MU19ERUZJTkVEX19SRVBPUlRfT05MWV9OT19NVVRBVElPTiIKICAgIGNhcmRzX3JlYWR5ID0gYm91bmRhcnkuZ2V0KCJjYXJkX3N0YXR1cyIpID09ICJUU0VLX0JPVU5EQVJZX0NBUkRTX1JFQURZX19OT19USFJFU0hPTERfQ0hBTkdFIgoKICAgIGhpZ2ggPSBpbnQoZHJ5LmdldCgiaGlnaF9hdHRlbnRpb25fY291bnQiLCAwKSkKICAgIG1vZGVyYXRlID0gaW50KGRyeS5nZXQoIm1vZGVyYXRlX2F0dGVudGlvbl9jb3VudCIsIDApKQogICAgbG93ID0gaW50KGRyeS5nZXQoImxvd19hdHRlbnRpb25fY291bnQiLCAwKSkKICAgIHNjZW5hcmlvX2NvdW50ID0gaW50KGRyeS5nZXQoInNjZW5hcmlvX2NvdW50IiwgMCkpCgogICAgaWYgbm90IHJlbGVhc2VfcGFzc2VkIG9yIG5vdCBkcnlfcmVhZHkgb3Igbm90IGNvbnRyb2xzX3JlYWR5IG9yIG5vdCBjYXJkc19yZWFkeToKICAgICAgICBkZWNpc2lvbiA9ICJERUZFUl9USFJFU0hPTERfQ0hBTkdFX1BFTkRJTkdfTU9SRV9FVklERU5DRSIKICAgICAgICByYXRpb25hbGUgPSAiT25lIG9yIG1vcmUgcHJlcmVxdWlzaXRlIHJlcG9ydC1vbmx5IGxheWVycyBpcyBub3QgaW4gdGhlIGV4cGVjdGVkIHJlYWR5IHN0YXRlLiIKICAgIGVsaWYgaGlnaCA+IDA6CiAgICAgICAgZGVjaXNpb24gPSAiREVGRVJfVEhSRVNIT0xEX0NIQU5HRV9QRU5ESU5HX01PUkVfRVZJREVOQ0UiCiAgICAgICAgcmF0aW9uYWxlID0gIkhpZ2gtYXR0ZW50aW9uIHRocmVzaG9sZCBwcmVzc3VyZSBleGlzdHM7IHRocmVzaG9sZCB0dW5pbmcgaXMgbm90IGp1c3RpZmllZCB3aXRob3V0IGFkZGl0aW9uYWwgZXZpZGVuY2UgYW5kIHJldmlldy4iCiAgICBlbGlmIHNjZW5hcmlvX2NvdW50ID09IDA6CiAgICAgICAgZGVjaXNpb24gPSAiUkVKRUNUX1RIUkVTSE9MRF9DSEFOR0UiCiAgICAgICAgcmF0aW9uYWxlID0gIk5vIHNjZW5hcmlvcyBleGlzdCB0byBqdXN0aWZ5IHRocmVzaG9sZCBjaGFuZ2UuIgogICAgZWxzZToKICAgICAgICBkZWNpc2lvbiA9ICJSRVZJRVdfUkVBRFlfUkVQT1JUX09OTFkiCiAgICAgICAgcmF0aW9uYWxlID0gIlJlcG9ydC1vbmx5IHNlbnNpdGl2aXR5IGV4aXN0cywgYnV0IG5vIGNsYXNzaWZpZXIgbXV0YXRpb24gaXMgYXV0aG9yaXplZC4iCgogICAgcmV0dXJuIHsKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBib29sKHJlbGVhc2VfcGFzc2VkKSwKICAgICAgICAiZHJ5X3J1bl9yZWFkeSI6IGJvb2woZHJ5X3JlYWR5KSwKICAgICAgICAiY29udHJvbHNfcmVhZHkiOiBib29sKGNvbnRyb2xzX3JlYWR5KSwKICAgICAgICAiYm91bmRhcnlfY2FyZHNfcmVhZHkiOiBib29sKGNhcmRzX3JlYWR5KSwKICAgICAgICAiaGlnaF9hdHRlbnRpb25fY291bnQiOiBoaWdoLAogICAgICAgICJtb2RlcmF0ZV9hdHRlbnRpb25fY291bnQiOiBtb2RlcmF0ZSwKICAgICAgICAibG93X2F0dGVudGlvbl9jb3VudCI6IGxvdywKICAgICAgICAic2NlbmFyaW9fY291bnQiOiBzY2VuYXJpb19jb3VudCwKICAgICAgICAiZGVjaXNpb24iOiBkZWNpc2lvbiwKICAgICAgICAicmF0aW9uYWxlIjogcmF0aW9uYWxlLAogICAgfQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihleGMpKQogICAgICAgIHJldHVybiBwYXRocwogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIGRlY2lzaW9uID0ge3N1bW1hcnlbInRocmVzaG9sZF9kZWNpc2lvbiJdOiAxfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZGVjaXNpb24ua2V5cygpKSwgbGlzdChkZWNpc2lvbi52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiU2VsZWN0ZWQiKQogICAgcGx0LnRpdGxlKCJUaHJlc2hvbGQgRGVjaXNpb24gUmVjb3JkIikKICAgIHNhdmUoInRocmVzaG9sZF9kZWNpc2lvbl9zZWxlY3RlZC5wbmciKQoKICAgIGF0dGVudGlvbiA9IHsKICAgICAgICAiaGlnaCI6IHN1bW1hcnlbImhpZ2hfYXR0ZW50aW9uX2NvdW50Il0sCiAgICAgICAgIm1vZGVyYXRlIjogc3VtbWFyeVsibW9kZXJhdGVfYXR0ZW50aW9uX2NvdW50Il0sCiAgICAgICAgImxvdyI6IHN1bW1hcnlbImxvd19hdHRlbnRpb25fY291bnQiXSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoYXR0ZW50aW9uLmtleXMoKSksIGxpc3QoYXR0ZW50aW9uLnZhbHVlcygpKSkKICAgIHBsdC55bGFiZWwoIlNjZW5hcmlvIGNvdW50IikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIERlY2lzaW9uIEF0dGVudGlvbiBDb3VudHMiKQogICAgc2F2ZSgidGhyZXNob2xkX2RlY2lzaW9uX2F0dGVudGlvbl9jb3VudHMucG5nIikKCiAgICBsb2NrcyA9IHsKICAgICAgICAidGhyZXNob2xkc19jaGFuZ2VkIjogaW50KHN1bW1hcnlbInRocmVzaG9sZHNfY2hhbmdlZCJdKSwKICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogaW50KHN1bW1hcnlbImNsYXNzaWZpZXJfY2hhbmdlZCJdKSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgICAgICJyZXZpZXdfcmVhZHkiOiBpbnQoc3VtbWFyeVsidGhyZXNob2xkX2RlY2lzaW9uIl0gPT0gIlJFVklFV19SRUFEWV9SRVBPUlRfT05MWSIpLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChsb2Nrcy5rZXlzKCkpLCBsaXN0KGxvY2tzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjAsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJWYWx1ZSIpCiAgICBwbHQudGl0bGUoIlRocmVzaG9sZCBEZWNpc2lvbiBMb2NrcyIpCiAgICBzYXZlKCJ0aHJlc2hvbGRfZGVjaXNpb25fbG9ja3MucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjggVGhyZXNob2xkIERlY2lzaW9uIFJlY29yZCIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIERlY2lzaW9uIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIERlY2lzaW9uIHN0YXR1czogYHtzdW1tYXJ5WydkZWNpc2lvbl9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gVGhyZXNob2xkIGRlY2lzaW9uOiBge3N1bW1hcnlbJ3RocmVzaG9sZF9kZWNpc2lvbiddfWAiLAogICAgICAgIGYiLSBSYXRpb25hbGU6IHtzdW1tYXJ5WydkZWNpc2lvbl9yYXRpb25hbGUnXX0iLAogICAgICAgIGYiLSBSZWxlYXNlIHBhc3NlZDogYHtzdW1tYXJ5WydyZWxlYXNlX3Bhc3NlZCddfWAiLAogICAgICAgIGYiLSBEcnktcnVuIHJlYWR5OiBge3N1bW1hcnlbJ2RyeV9ydW5fcmVhZHknXX1gIiwKICAgICAgICBmIi0gQ29udHJvbHMgcmVhZHk6IGB7c3VtbWFyeVsnY29udHJvbHNfcmVhZHknXX1gIiwKICAgICAgICBmIi0gQm91bmRhcnkgY2FyZHMgcmVhZHk6IGB7c3VtbWFyeVsnYm91bmRhcnlfY2FyZHNfcmVhZHknXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQXR0ZW50aW9uIENvdW50cyIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIEhpZ2ggYXR0ZW50aW9uOiBge3N1bW1hcnlbJ2hpZ2hfYXR0ZW50aW9uX2NvdW50J119YCIsCiAgICAgICAgZiItIE1vZGVyYXRlIGF0dGVudGlvbjogYHtzdW1tYXJ5Wydtb2RlcmF0ZV9hdHRlbnRpb25fY291bnQnXX1gIiwKICAgICAgICBmIi0gTG93IGF0dGVudGlvbjogYHtzdW1tYXJ5Wydsb3dfYXR0ZW50aW9uX2NvdW50J119YCIsCiAgICAgICAgZiItIFNjZW5hcmlvIGNvdW50OiBge3N1bW1hcnlbJ3NjZW5hcmlvX2NvdW50J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEV4cGxpY2l0IExvY2tzIiwKICAgICAgICAiIiwKICAgICAgICAiYGBgdGV4dCIsCiAgICAgICAgZiJ0aHJlc2hvbGRzX2NoYW5nZWQ6IHtzdHIoc3VtbWFyeVsndGhyZXNob2xkc19jaGFuZ2VkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmImNsYXNzaWZpZXJfY2hhbmdlZDoge3N0cihzdW1tYXJ5WydjbGFzc2lmaWVyX2NoYW5nZWQnXSkubG93ZXIoKX0iLAogICAgICAgIGYibXV0YXRpb25fYWxsb3dlZDoge3N0cihzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmImFwcGxpY2F0aW9uX2FsbG93ZWQ6IHtzdHIoc3VtbWFyeVsnYXBwbGljYXRpb25fYWxsb3dlZCddKS5sb3dlcigpfSIsCiAgICAgICAgZiJjYWxpYnJhdGlvbl9hcHBsaWVkOiB7c3RyKHN1bW1hcnlbJ2NhbGlicmF0aW9uX2FwcGxpZWQnXSkubG93ZXIoKX0iLAogICAgICAgICJgYGAiLAogICAgICAgICIiLAogICAgICAgICIjIyBJbnRlcnByZXRhdGlvbiIsCiAgICAgICAgIiIsCiAgICAgICAgIlRoaXMgZGVjaXNpb24gcmVjb3JkIGNvbnZlcnRzIHRoZSByZXBvcnQtb25seSBzZW5zaXRpdml0eSBkcnktcnVuIGludG8gYSBnb3Zlcm5hbmNlIGRlY2lzaW9uLiBJdCBkb2VzIG5vdCB0dW5lIHRocmVzaG9sZHMsIGFsdGVyIGNsYXNzaWZpZXIgc2NvcmluZywgb3IgYXV0aG9yaXplIG11dGF0aW9uLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIE5leHQgVGF1IFdvcmsiLAogICAgICAgICIiLAogICAgICAgICIxLiBJZiBkZWNpc2lvbiBpcyByZXBvcnQtb25seSByZXZpZXctcmVhZHksIHByZXBhcmUgYSBodW1hbi1yZWFkYWJsZSBzdW1tYXJ5IG9mIHRoZSBwcmVzc3VyZSBzdXJmYWNlcy4iLAogICAgICAgICIyLiBJZiBkZWNpc2lvbiBpcyBkZWZlcnJlZCwgZ2F0aGVyIGFkZGl0aW9uYWwgc2NlbmFyaW8gZXZpZGVuY2UgYmVmb3JlIGFueSBjYW5kaWRhdGUgYnJhbmNoLiIsCiAgICAgICAgIjMuIElmIGRlY2lzaW9uIGlzIHJlamVjdGVkLCBmcmVlemUgY3VycmVudCB0aHJlc2hvbGRzIGFuZCBkb2N1bWVudCB3aHkuIiwKICAgICAgICAiNC4gUHJlc2VydmUgbm8tdGhyZXNob2xkLWNoYW5nZSBhbmQgbm8tY2xhc3NpZmllci1tdXRhdGlvbiBsb2Nrcy4iLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBkcnkgPSByZWFkX2pzb24oRFJZX1JVTikKICAgIHBlbmFsdHkgPSByZWFkX2pzb24oUEVOQUxUWSkKICAgIGJvdW5kYXJ5ID0gcmVhZF9qc29uKEJPVU5EQVJZKQogICAgcmVsZWFzZSA9IHJlYWRfanNvbihSRUxFQVNFKQoKICAgIGRlY2lzaW9uID0gZGVjaWRlKGRyeSwgcGVuYWx0eSwgYm91bmRhcnksIHJlbGVhc2UpCgogICAgc3RhdHVzID0gIlRIUkVTSE9MRF9ERUNJU0lPTl9SRUNPUkRFRF9fTk9fTVVUQVRJT04iCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctdGhyZXNob2xkLWRlY2lzaW9uLXJlY29yZC12MC43LjgiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiZGVjaXNpb25fc3RhdHVzIjogc3RhdHVzLAogICAgICAgICJ0aHJlc2hvbGRfZGVjaXNpb24iOiBkZWNpc2lvblsiZGVjaXNpb24iXSwKICAgICAgICAiZGVjaXNpb25fcmF0aW9uYWxlIjogZGVjaXNpb25bInJhdGlvbmFsZSJdLAogICAgICAgICoqe2s6IHYgZm9yIGssIHYgaW4gZGVjaXNpb24uaXRlbXMoKSBpZiBrIG5vdCBpbiB7ImRlY2lzaW9uIiwgInJhdGlvbmFsZSJ9fSwKICAgICAgICAiZGVjaXNpb25fb3B0aW9ucyI6IERFQ0lTSU9OX09QVElPTlMsCiAgICAgICAgImlucHV0X3RocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuIjogcmVsKERSWV9SVU4pLAogICAgICAgICJpbnB1dF9wZW5hbHR5X2NvbnRyb2xzIjogcmVsKFBFTkFMVFkpLAogICAgICAgICJpbnB1dF9ib3VuZGFyeV9jYXJkcyI6IHJlbChCT1VOREFSWSksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9iZWhhdmlvcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiY2FuZGlkYXRlX2JyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAiTW92ZSB0byB2MC43LjkgVGhyZXNob2xkIEdvdmVybmFuY2UgU3VtbWFyeSBvciBmcmVlemUgdjAuNy54IGFzIGEgVGF1IHRocmVzaG9sZCBhbmFseXNpcyBtaWxlc3RvbmUuIiwKICAgICAgICAiYm91bmRhcnkiOiAiVGhyZXNob2xkIGRlY2lzaW9uIHJlY29yZHMgYXJlIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSBkZWNpc2lvbiBhcnRpZmFjdHMuIFRoZXkgY29udmVydCByZXBvcnQtb25seSBkcnktcnVuIGV2aWRlbmNlIGludG8gYSBub24tbXV0YXRpbmcgZGVjaXNpb24uIFRoZXkgZG8gbm90IGNyZWF0ZSBsaXZlIGFwcHJvdmFsLCBleGVjdXRlIHJlcGxheSBjb21tYW5kcywgY3JlYXRlIGJyYW5jaGVzLCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciwgYXBwbHkgY2FsaWJyYXRpb24sIGNoYW5nZSB0aHJlc2hvbGRzLCBvciB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gInRocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmRfdjBfN184Lmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF90aHJlc2hvbGRfZGVjaXNpb25fcmVjb3JkLmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gInRocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmRfdjBfN184Lm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfdGhyZXNob2xkX2RlY2lzaW9uX3JlY29yZC5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJkZWNpc2lvbl9zdGF0dXMiOiBzdW1tYXJ5WyJkZWNpc2lvbl9zdGF0dXMiXSwKICAgICAgICAidGhyZXNob2xkX2RlY2lzaW9uIjogc3VtbWFyeVsidGhyZXNob2xkX2RlY2lzaW9uIl0sCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogc3VtbWFyeVsicmVsZWFzZV9wYXNzZWQiXSwKICAgICAgICAiZHJ5X3J1bl9yZWFkeSI6IHN1bW1hcnlbImRyeV9ydW5fcmVhZHkiXSwKICAgICAgICAic2NlbmFyaW9fY291bnQiOiBzdW1tYXJ5WyJzY2VuYXJpb19jb3VudCJdLAogICAgICAgICJoaWdoX2F0dGVudGlvbl9jb3VudCI6IHN1bW1hcnlbImhpZ2hfYXR0ZW50aW9uX2NvdW50Il0sCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IHN1bW1hcnlbInRocmVzaG9sZHNfY2hhbmdlZCJdLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBzdW1tYXJ5WyJjbGFzc2lmaWVyX2NoYW5nZWQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3RocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmQvbGF0ZXN0X3RocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmQubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT / "reports" / "threshold_decision_record" / "README.md", """# Threshold Decision Record Reports

Current layer: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**

## Purpose

This folder stores non-mutating decision records for threshold sensitivity dry-run outputs.

## Primary command

```powershell
python scripts/benchmarks/generate_threshold_decision_record.py
```

## README Update Rule

Update this mini README whenever threshold decision logic, dry-run interpretation, or candidate-branch criteria change.

Boundary: threshold decision records are local classifier-governance decision artifacts only.
""")

write(ROOT / "visuals" / "threshold_decision_record" / "README.md", """# Threshold Decision Record Visuals

Current layer: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**

## Purpose

This folder stores charts summarizing threshold decision records.

## README Update Rule

Update this mini README whenever threshold decision chart names or meanings change.

Boundary: threshold decision visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "threshold_decision_record" / "v0_7_8" / "README.md", """# v0.7.8 Threshold Decision Charts

Expected charts:

- `threshold_decision_selected.png`
- `threshold_decision_attention_counts.png`
- `threshold_decision_locks.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local threshold-decision diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.7[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.6[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.7 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.8 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.7-ready |", "| Task routing matrix | geometry-aware / v0.7.8-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.7 |", "| Agent contract version sync | current / v0.7.8 |")

if "| Threshold decision record |" not in r:
    r = r.replace("| Threshold sensitivity charts | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n",
                  "| Threshold sensitivity charts | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n| Threshold decision record | `reports/threshold_decision_record/latest_threshold_decision_record.md` |\n| Threshold decision charts | `visuals/threshold_decision_record/v0_7_8/` |\n")

if "python scripts/benchmarks/generate_threshold_decision_record.py" not in r:
    r = r.replace("python scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython scripts/benchmarks/generate_threshold_decision_record.py\npython scripts/release/validate_release.py")

if "    threshold_decision_record/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    threshold_decision_record/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    threshold_decision_record/\n")

section = """## Threshold Decision Record v0.7.8

v0.7.8 converts the report-only threshold sensitivity dry-run into a non-mutating threshold decision record.

Primary command:

```powershell
python scripts/benchmarks/generate_threshold_decision_record.py
```

Primary outputs:

```text
reports/threshold_decision_record/latest_threshold_decision_record.json
reports/threshold_decision_record/latest_threshold_decision_record.md
visuals/threshold_decision_record/v0_7_8/
```

Current lock:

```text
thresholds_changed: false
classifier_changed: false
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: threshold decision records are local classifier-governance decision artifacts. They convert report-only dry-run evidence into a non-mutating decision. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Threshold Decision Record v0.7.8" not in r:
    r = r.replace("## Threshold Sensitivity Dry-Run v0.7.7", section + "## Threshold Sensitivity Dry-Run v0.7.7", 1)

lesson = "| L-060 | v0.7.7 dry-ran threshold sensitivity in report-only mode. | Dry-run pressure is not a decision by itself. | Threshold sensitivity outputs must be compiled into a decision record before any candidate branch or threshold tuning is considered. |"
if "L-060" not in r:
    r = r.replace("| L-059 | v0.7.6 defined report-only over/under-penalty controls. | Controls alone do not show which threshold pressures are high attention. | Threshold sensitivity must be dry-run in report-only mode before any decision record or classifier change is discussed. |\n",
                  "| L-059 | v0.7.6 defined report-only over/under-penalty controls. | Controls alone do not show which threshold pressures are high attention. | Threshold sensitivity must be dry-run in report-only mode before any decision record or classifier change is discussed. |\n" + lesson + "\n")

if "| v0.7.8 |" not in r:
    r = r.replace("| v0.7.7 | Threshold sensitivity dry-run; models threshold pressure without changing classifier behavior. |\n",
                  "| v0.7.7 | Threshold sensitivity dry-run; models threshold pressure without changing classifier behavior. |\n| v0.7.8 | Threshold decision record; converts dry-run pressure into a non-mutating decision. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**

Recommended goals:

- Summarize v0.7.1-v0.7.8 Tau mechanics return path.
- Freeze current threshold decision unless human review requests a candidate branch.
- Preserve no-classifier-mutation lock.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_threshold_decision_record.py" not in s:
        s = s.replace("python scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython scripts/benchmarks/generate_threshold_decision_record.py\npython -m unittest discover -s tests")
        s = s.replace("| Threshold sensitivity patch | `reports/threshold_sensitivity_dry_run/`, `visuals/threshold_sensitivity_dry_run/`, penalty controls | report-only dry-run + release validator; no mutation |\n",
                      "| Threshold sensitivity patch | `reports/threshold_sensitivity_dry_run/`, `visuals/threshold_sensitivity_dry_run/`, penalty controls | report-only dry-run + release validator; no mutation |\n| Threshold decision patch | `reports/threshold_decision_record/`, `visuals/threshold_decision_record/`, threshold dry-run | decision record + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Threshold decision patch |" not in s:
        s = s.replace("| Threshold sensitivity patch | inner | dry-run | classifier | penalty controls + threshold review | report-only threshold sensitivity + charts + release validator | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` |\n",
                      "| Threshold sensitivity patch | inner | dry-run | classifier | penalty controls + threshold review | report-only threshold sensitivity + charts + release validator | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` |\n| Threshold decision patch | inner | decision | classifier | threshold sensitivity dry-run | non-mutating decision record + charts + release validator | `reports/threshold_decision_record/latest_threshold_decision_record.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.8"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["threshold_decision_record"] = {
    "read_first": ["reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.json", "reports/penalty_controls/latest_over_under_penalty_negative_controls.json"],
    "validate": ["python scripts/benchmarks/generate_threshold_decision_record.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/threshold_decision_record/latest_threshold_decision_record.md", "visuals/threshold_decision_record/v0_7_8/"],
    "mutation_lock": "Decision record only; no classifier change, threshold change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.8 | Threshold decision record |" not in t:
    t = t.replace("| v0.7.7 | Threshold sensitivity dry-run | `python scripts/benchmarks/run_threshold_sensitivity_dry_run.py` | Models threshold pressure without changing classifier behavior | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n",
                  "| v0.7.7 | Threshold sensitivity dry-run | `python scripts/benchmarks/run_threshold_sensitivity_dry_run.py` | Models threshold pressure without changing classifier behavior | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n| v0.7.8 | Threshold decision record | `python scripts/benchmarks/generate_threshold_decision_record.py` | Converts threshold dry-run pressure into non-mutating decision | `reports/threshold_decision_record/latest_threshold_decision_record.md` | `visuals/threshold_decision_record/v0_7_8/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_8_threshold_decision_record.md", f"""# TAU-SCALING-SA v0.7.8 - Threshold Decision Record

Generated: {NOW}

## Purpose

Convert the report-only threshold sensitivity dry-run into a non-mutating threshold decision record.

## Boundary

Threshold decision records are local classifier-governance decision artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.8 patch written")
