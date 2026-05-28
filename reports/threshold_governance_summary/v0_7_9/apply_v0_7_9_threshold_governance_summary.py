
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
        d = ROOT / "reports" / "threshold_governance_summary" / "v0_7_9" / "backups" / f"{p.name}_before_v0_7_9_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_threshold_governance_summary.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9nb3Zlcm5hbmNlX3N1bW1hcnkiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAidGhyZXNob2xkX2dvdmVybmFuY2Vfc3VtbWFyeSIgLyAidjBfN185IgoKSU5QVVRTID0gewogICAgInRhdV9tZWNoYW5pY3MiOiBST09UIC8gInJlcG9ydHMiIC8gInRhdV9tZWNoYW5pY3NfcmV2aWV3IiAvICJsYXRlc3RfdGF1X21lY2hhbmljc19yZXR1cm5fcmV2aWV3Lmpzb24iLAogICAgInRhdV92ZWN0b3IiOiBST09UIC8gInJlcG9ydHMiIC8gInRhdV92ZWN0b3Jfc2VtYW50aWNzIiAvICJsYXRlc3RfdGF1X3ZlY3Rvcl9zZW1hbnRpY3NfbGVkZ2VyLmpzb24iLAogICAgImdhdGVfYWxnZWJyYSI6IFJPT1QgLyAicmVwb3J0cyIgLyAiZ2F0ZV9hbGdlYnJhIiAvICJsYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5qc29uIiwKICAgICJ0aHJlc2hvbGRfcmV2aWV3IjogUk9PVCAvICJyZXBvcnRzIiAvICJ0c2VrX3RocmVzaG9sZF9yZXZpZXciIC8gImxhdGVzdF90c2VrX3RocmVzaG9sZF9ib3VuZGFyeV9yZXZpZXcuanNvbiIsCiAgICAiYm91bmRhcnlfY2FyZHMiOiBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfYm91bmRhcnlfY2FyZHMiIC8gImxhdGVzdF90c2VrX2JvdW5kYXJ5X2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iLAogICAgInBlbmFsdHlfY29udHJvbHMiOiBST09UIC8gInJlcG9ydHMiIC8gInBlbmFsdHlfY29udHJvbHMiIC8gImxhdGVzdF9vdmVyX3VuZGVyX3BlbmFsdHlfbmVnYXRpdmVfY29udHJvbHMuanNvbiIsCiAgICAic2Vuc2l0aXZpdHkiOiBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuIiAvICJsYXRlc3RfdGhyZXNob2xkX3NlbnNpdGl2aXR5X2RyeV9ydW4uanNvbiIsCiAgICAiZGVjaXNpb24iOiBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmQiIC8gImxhdGVzdF90aHJlc2hvbGRfZGVjaXNpb25fcmVjb3JkLmpzb24iLAogICAgInJlbGVhc2UiOiBST09UIC8gInJlcG9ydHMiIC8gInJlbGVhc2UiIC8gImxhdGVzdF9yZWxlYXNlX3JlYWRpbmVzcy5qc29uIiwKfQoKQ0hBSU4gPSBbCiAgICAoInYwLjcuMSIsICJ0YXVfbWVjaGFuaWNzIiwgIm1lY2hhbmljc19zdGF0dXMiKSwKICAgICgidjAuNy4yIiwgInRhdV92ZWN0b3IiLCAic2VtYW50aWNzX3N0YXR1cyIpLAogICAgKCJ2MC43LjMiLCAiZ2F0ZV9hbGdlYnJhIiwgImdhdGVfYWxnZWJyYV9zdGF0dXMiKSwKICAgICgidjAuNy40IiwgInRocmVzaG9sZF9yZXZpZXciLCAidGhyZXNob2xkX3Jldmlld19zdGF0dXMiKSwKICAgICgidjAuNy41IiwgImJvdW5kYXJ5X2NhcmRzIiwgImNhcmRfc3RhdHVzIiksCiAgICAoInYwLjcuNiIsICJwZW5hbHR5X2NvbnRyb2xzIiwgImNvbnRyb2xfc3RhdHVzIiksCiAgICAoInYwLjcuNyIsICJzZW5zaXRpdml0eSIsICJkcnlfcnVuX3N0YXR1cyIpLAogICAgKCJ2MC43LjgiLCAiZGVjaXNpb24iLCAiZGVjaXNpb25fc3RhdHVzIiksCl0KCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCk6CiAgICBpZiBub3QgcGF0aC5leGlzdHMoKToKICAgICAgICByZXR1cm4geyJtaXNzaW5nIjogVHJ1ZSwgInBhdGgiOiBzdHIocGF0aCl9CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJwYXJzZV9lcnJvciI6IHN0cihleGMpLCAicGF0aCI6IHN0cihwYXRoKX0KCmRlZiB3anNvbihwYXRoOiBQYXRoLCBkYXRhKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKGRhdGEsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cik6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocGF0aDogUGF0aCk6CiAgICByZXR1cm4gc3RyKHBhdGgucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGJ1aWxkX2NoYWluKGRhdGEpOgogICAgcm93cyA9IFtdCiAgICBmb3IgdmVyc2lvbiwga2V5LCBzdGF0dXNfa2V5IGluIENIQUlOOgogICAgICAgIGQgPSBkYXRhW2tleV0KICAgICAgICByb3dzLmFwcGVuZCh7CiAgICAgICAgICAgICJ2ZXJzaW9uIjogdmVyc2lvbiwKICAgICAgICAgICAgImFydGlmYWN0Ijoga2V5LAogICAgICAgICAgICAic3RhdHVzIjogZC5nZXQoc3RhdHVzX2tleSwgIk1JU1NJTkciIGlmIGQuZ2V0KCJtaXNzaW5nIikgZWxzZSAiUkVDT1JERUQiKSwKICAgICAgICAgICAgIm1pc3NpbmciOiBib29sKGQuZ2V0KCJtaXNzaW5nIikpLAogICAgICAgICAgICAidGhyZXNob2xkc19jaGFuZ2VkIjogYm9vbChkLmdldCgidGhyZXNob2xkc19jaGFuZ2VkIiwgRmFsc2UpKSwKICAgICAgICAgICAgImNsYXNzaWZpZXJfY2hhbmdlZCI6IGJvb2woZC5nZXQoImNsYXNzaWZpZXJfY2hhbmdlZCIsIEZhbHNlKSksCiAgICAgICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogYm9vbChkLmdldCgibXV0YXRpb25fYWxsb3dlZCIsIEZhbHNlKSksCiAgICAgICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogYm9vbChkLmdldCgiYXBwbGljYXRpb25fYWxsb3dlZCIsIEZhbHNlKSksCiAgICAgICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogYm9vbChkLmdldCgiY2FsaWJyYXRpb25fYXBwbGllZCIsIEZhbHNlKSksCiAgICAgICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IGJvb2woZC5nZXQoInJlcGxheV9hbGxvd2VkIiwgRmFsc2UpKSwKICAgICAgICAgICAgImdhcF9jb3VudCI6IGludChkLmdldCgiZ2FwX2NvdW50IiwgMCkgb3IgMCksCiAgICAgICAgfSkKICAgIHJldHVybiByb3dzCgpkZWYgc3VtbWFyaXplX2RlY2lzaW9uKGRhdGEpOgogICAgZGVjaXNpb24gPSBkYXRhWyJkZWNpc2lvbiJdCiAgICBzZW5zaXRpdml0eSA9IGRhdGFbInNlbnNpdGl2aXR5Il0KICAgIHJldHVybiB7CiAgICAgICAgInRocmVzaG9sZF9kZWNpc2lvbiI6IGRlY2lzaW9uLmdldCgidGhyZXNob2xkX2RlY2lzaW9uIiwgIlVOS05PV04iKSwKICAgICAgICAiZGVjaXNpb25fc3RhdHVzIjogZGVjaXNpb24uZ2V0KCJkZWNpc2lvbl9zdGF0dXMiLCAiVU5LTk9XTiIpLAogICAgICAgICJkZWNpc2lvbl9yYXRpb25hbGUiOiBkZWNpc2lvbi5nZXQoImRlY2lzaW9uX3JhdGlvbmFsZSIsICIiKSwKICAgICAgICAic2NlbmFyaW9fY291bnQiOiBpbnQoc2Vuc2l0aXZpdHkuZ2V0KCJzY2VuYXJpb19jb3VudCIsIDApIG9yIDApLAogICAgICAgICJoaWdoX2F0dGVudGlvbl9jb3VudCI6IGludChzZW5zaXRpdml0eS5nZXQoImhpZ2hfYXR0ZW50aW9uX2NvdW50IiwgMCkgb3IgMCksCiAgICAgICAgIm1vZGVyYXRlX2F0dGVudGlvbl9jb3VudCI6IGludChzZW5zaXRpdml0eS5nZXQoIm1vZGVyYXRlX2F0dGVudGlvbl9jb3VudCIsIDApIG9yIDApLAogICAgICAgICJsb3dfYXR0ZW50aW9uX2NvdW50IjogaW50KHNlbnNpdGl2aXR5LmdldCgibG93X2F0dGVudGlvbl9jb3VudCIsIDApIG9yIDApLAogICAgfQoKZGVmIGNsYXNzaWZ5KGRhdGEsIHJvd3MpOgogICAgcmVsZWFzZSA9IGRhdGFbInJlbGVhc2UiXQogICAgcmVsZWFzZV9wYXNzZWQgPSByZWxlYXNlLmdldCgicGFzc2VkIikgaXMgVHJ1ZSBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJmaW5kaW5ncyIsIFtdKSkgPT0gMCBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJzdGVwX2ZhaWx1cmVzIiwgW10pKSA9PSAwCgogICAgdmlvbGF0aW9ucyA9IFtdCiAgICBmb3Igcm93IGluIHJvd3M6CiAgICAgICAgZm9yIGtleSBpbiBbInRocmVzaG9sZHNfY2hhbmdlZCIsICJjbGFzc2lmaWVyX2NoYW5nZWQiLCAibXV0YXRpb25fYWxsb3dlZCIsICJhcHBsaWNhdGlvbl9hbGxvd2VkIiwgImNhbGlicmF0aW9uX2FwcGxpZWQiLCAicmVwbGF5X2FsbG93ZWQiXToKICAgICAgICAgICAgaWYgcm93LmdldChrZXkpIGlzIFRydWU6CiAgICAgICAgICAgICAgICB2aW9sYXRpb25zLmFwcGVuZCh7ImFydGlmYWN0Ijogcm93WyJhcnRpZmFjdCJdLCAidmlvbGF0aW9uIjoga2V5fSkKCiAgICBtaXNzaW5nID0gW3Jvd1siYXJ0aWZhY3QiXSBmb3Igcm93IGluIHJvd3MgaWYgcm93WyJtaXNzaW5nIl1dCiAgICBkZWNpc2lvbiA9IGRhdGFbImRlY2lzaW9uIl0uZ2V0KCJ0aHJlc2hvbGRfZGVjaXNpb24iKQogICAgbG9ja2VkID0gcmVsZWFzZV9wYXNzZWQgYW5kIG5vdCB2aW9sYXRpb25zIGFuZCBub3QgbWlzc2luZyBhbmQgZGVjaXNpb24gPT0gIkRFRkVSX1RIUkVTSE9MRF9DSEFOR0VfUEVORElOR19NT1JFX0VWSURFTkNFIgoKICAgIHN0YXR1cyA9ICJUSFJFU0hPTERfR09WRVJOQU5DRV9TVU1NQVJZX0xPQ0tFRF9fREVGRVJfQ0hBTkdFX05PX01VVEFUSU9OIiBpZiBsb2NrZWQgZWxzZSAiVEhSRVNIT0xEX0dPVkVSTkFOQ0VfU1VNTUFSWV9ORUVEU19SRVZJRVciCiAgICByZXR1cm4gc3RhdHVzLCBsb2NrZWQsIHJlbGVhc2VfcGFzc2VkLCB2aW9sYXRpb25zLCBtaXNzaW5nCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGV4YykpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgcm93cyA9IHN1bW1hcnlbImNoYWluX3Jvd3MiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpCiAgICBwbHQuYmFyKFtyWyJ2ZXJzaW9uIl0gZm9yIHIgaW4gcm93c10sIFswIGlmIHJbIm1pc3NpbmciXSBlbHNlIDEgZm9yIHIgaW4gcm93c10pCiAgICBwbHQueWxhYmVsKCJQcmVzZW50IikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIEdvdmVybmFuY2UgQ2hhaW4gQ292ZXJhZ2UiKQogICAgc2F2ZSgidGhyZXNob2xkX2dvdmVybmFuY2VfY2hhaW5fY292ZXJhZ2UucG5nIikKCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIoW3JbInZlcnNpb24iXSBmb3IgciBpbiByb3dzXSwgW3JbImdhcF9jb3VudCJdIGZvciByIGluIHJvd3NdKQogICAgcGx0LnlsYWJlbCgiR2FwIGNvdW50IikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIEdvdmVybmFuY2UgR2FwIENvdW50cyIpCiAgICBzYXZlKCJ0aHJlc2hvbGRfZ292ZXJuYW5jZV9nYXBfY291bnRzLnBuZyIpCgogICAgbG9ja3MgPSB7CiAgICAgICAgInN1bW1hcnlfbG9ja2VkIjogaW50KHN1bW1hcnlbInN1bW1hcnlfbG9ja2VkIl0pLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IGludChzdW1tYXJ5WyJyZWxlYXNlX3Bhc3NlZCJdKSwKICAgICAgICAidmlvbGF0aW9ucyI6IHN1bW1hcnlbInZpb2xhdGlvbl9jb3VudCJdLAogICAgICAgICJtaXNzaW5nIjogc3VtbWFyeVsibWlzc2luZ19jb3VudCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGxvY2tzLmtleXMoKSksIGxpc3QobG9ja3MudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIEdvdmVybmFuY2UgU3VtbWFyeSBIZWFsdGgiKQogICAgc2F2ZSgidGhyZXNob2xkX2dvdmVybmFuY2Vfc3VtbWFyeV9oZWFsdGgucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjkgVGhyZXNob2xkIEdvdmVybmFuY2UgU3VtbWFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFN1bW1hcnkgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gU3VtbWFyeSBzdGF0dXM6IGB7c3VtbWFyeVsnc3VtbWFyeV9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gU3VtbWFyeSBsb2NrZWQ6IGB7c3VtbWFyeVsnc3VtbWFyeV9sb2NrZWQnXX1gIiwKICAgICAgICBmIi0gVGhyZXNob2xkIGRlY2lzaW9uOiBge3N1bW1hcnlbJ3RocmVzaG9sZF9kZWNpc2lvbiddfWAiLAogICAgICAgIGYiLSBSZWxlYXNlIHBhc3NlZDogYHtzdW1tYXJ5WydyZWxlYXNlX3Bhc3NlZCddfWAiLAogICAgICAgIGYiLSBWaW9sYXRpb24gY291bnQ6IGB7c3VtbWFyeVsndmlvbGF0aW9uX2NvdW50J119YCIsCiAgICAgICAgZiItIE1pc3NpbmcgY291bnQ6IGB7c3VtbWFyeVsnbWlzc2luZ19jb3VudCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBUaHJlc2hvbGQgRGVjaXNpb24iLAogICAgICAgICIiLAogICAgICAgIGYiLSBEZWNpc2lvbiBzdGF0dXM6IGB7c3VtbWFyeVsnZGVjaXNpb25fc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJhdGlvbmFsZToge3N1bW1hcnlbJ2RlY2lzaW9uX3JhdGlvbmFsZSddfSIsCiAgICAgICAgZiItIFNjZW5hcmlvIGNvdW50OiBge3N1bW1hcnlbJ3NjZW5hcmlvX2NvdW50J119YCIsCiAgICAgICAgZiItIEhpZ2ggYXR0ZW50aW9uIGNvdW50OiBge3N1bW1hcnlbJ2hpZ2hfYXR0ZW50aW9uX2NvdW50J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIHYwLjcueCBDaGFpbiIsCiAgICAgICAgIiIsCiAgICAgICAgInwgVmVyc2lvbiB8IEFydGlmYWN0IHwgU3RhdHVzIHwgR2FwcyB8IFRocmVzaG9sZCBjaGFuZ2VkIHwgQ2xhc3NpZmllciBjaGFuZ2VkIHwgTXV0YXRpb24gfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS06fC0tLTp8LS0tOnwtLS06fCIsCiAgICBdCiAgICBmb3Igcm93IGluIHN1bW1hcnlbImNoYWluX3Jvd3MiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7cm93Wyd2ZXJzaW9uJ119YCB8IGB7cm93WydhcnRpZmFjdCddfWAgfCBge3Jvd1snc3RhdHVzJ119YCB8IHtyb3dbJ2dhcF9jb3VudCddfSB8IGB7cm93Wyd0aHJlc2hvbGRzX2NoYW5nZWQnXX1gIHwgYHtyb3dbJ2NsYXNzaWZpZXJfY2hhbmdlZCddfWAgfCBge3Jvd1snbXV0YXRpb25fYWxsb3dlZCddfWAgfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBHb3Zlcm5hbmNlIENvbmNsdXNpb24iLAogICAgICAgICIiLAogICAgICAgICJUaGUgY3VycmVudCB0aHJlc2hvbGQgZGVjaXNpb24gaXMgKipkZWZlciB0aHJlc2hvbGQgY2hhbmdlIHBlbmRpbmcgbW9yZSBldmlkZW5jZSoqLiBUaGlzIGlzIHRoZSBjb3JyZWN0IG91dGNvbWUgYmVjYXVzZSByZXBvcnQtb25seSBzZW5zaXRpdml0eSBmb3VuZCBoaWdoLWF0dGVudGlvbiBwcmVzc3VyZSB3aGlsZSBwcmVzZXJ2aW5nIGFsbCBtdXRhdGlvbiBhbmQgdGhyZXNob2xkIGxvY2tzLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEV4cGxpY2l0IExvY2tzIiwKICAgICAgICAiIiwKICAgICAgICAiYGBgdGV4dCIsCiAgICAgICAgZiJ0aHJlc2hvbGRzX2NoYW5nZWQ6IHtzdHIoc3VtbWFyeVsndGhyZXNob2xkc19jaGFuZ2VkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmImNsYXNzaWZpZXJfY2hhbmdlZDoge3N0cihzdW1tYXJ5WydjbGFzc2lmaWVyX2NoYW5nZWQnXSkubG93ZXIoKX0iLAogICAgICAgIGYibXV0YXRpb25fYWxsb3dlZDoge3N0cihzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmImFwcGxpY2F0aW9uX2FsbG93ZWQ6IHtzdHIoc3VtbWFyeVsnYXBwbGljYXRpb25fYWxsb3dlZCddKS5sb3dlcigpfSIsCiAgICAgICAgZiJjYWxpYnJhdGlvbl9hcHBsaWVkOiB7c3RyKHN1bW1hcnlbJ2NhbGlicmF0aW9uX2FwcGxpZWQnXSkubG93ZXIoKX0iLAogICAgICAgICJgYGAiLAogICAgICAgICIiLAogICAgICAgICIjIyBOZXh0IFRhdSBXb3JrIiwKICAgICAgICAiIiwKICAgICAgICAiMS4gRnJlZXplIGN1cnJlbnQgdGhyZXNob2xkcyB1bmxlc3MgaHVtYW4gcmV2aWV3IHJlcXVlc3RzIGEgY2FuZGlkYXRlIGJyYW5jaC4iLAogICAgICAgICIyLiBBZGQgbW9yZSBzY2VuYXJpbyBldmlkZW5jZSBmb3IgaGlnaC1hdHRlbnRpb24gcHJlc3N1cmUgc3VyZmFjZXMuIiwKICAgICAgICAiMy4gUHJlc2VydmUgY3VycmVudCBjbGFzc2lmaWVyIHVudGlsIHN0cm9uZ2VyIGV2aWRlbmNlIGV4aXN0cy4iLAogICAgICAgICI0LiBDb25zaWRlciB2MC44LjAgYXMgYSBzdGFibGUgVGF1IHRocmVzaG9sZCBnb3Zlcm5hbmNlIG1pbGVzdG9uZS4iLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBkYXRhID0ge2s6IHJlYWRfanNvbih2KSBmb3IgaywgdiBpbiBJTlBVVFMuaXRlbXMoKX0KICAgIHJvd3MgPSBidWlsZF9jaGFpbihkYXRhKQogICAgc3VtbWFyeV9zdGF0dXMsIGxvY2tlZCwgcmVsZWFzZV9wYXNzZWQsIHZpb2xhdGlvbnMsIG1pc3NpbmcgPSBjbGFzc2lmeShkYXRhLCByb3dzKQogICAgZGVjaXNpb24gPSBzdW1tYXJpemVfZGVjaXNpb24oZGF0YSkKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctdGhyZXNob2xkLWdvdmVybmFuY2Utc3VtbWFyeS12MC43LjkiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAic3VtbWFyeV9zdGF0dXMiOiBzdW1tYXJ5X3N0YXR1cywKICAgICAgICAic3VtbWFyeV9sb2NrZWQiOiBib29sKGxvY2tlZCksCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogYm9vbChyZWxlYXNlX3Bhc3NlZCksCiAgICAgICAgKipkZWNpc2lvbiwKICAgICAgICAiY2hhaW5fcm93cyI6IHJvd3MsCiAgICAgICAgInZpb2xhdGlvbl9jb3VudCI6IGxlbih2aW9sYXRpb25zKSwKICAgICAgICAidmlvbGF0aW9ucyI6IHZpb2xhdGlvbnMsCiAgICAgICAgIm1pc3NpbmdfY291bnQiOiBsZW4obWlzc2luZyksCiAgICAgICAgIm1pc3NpbmdfYXJ0aWZhY3RzIjogbWlzc2luZywKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAidGhyZXNob2xkc19jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgImNsYXNzaWZpZXJfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJjYW5kaWRhdGVfYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJNb3ZlIHRvIHYwLjguMCBTdGFibGUgVGF1IFRocmVzaG9sZCBHb3Zlcm5hbmNlIE1pbGVzdG9uZSBvciBhZGQgbW9yZSBzY2VuYXJpbyBldmlkZW5jZSBiZWZvcmUgYW55IGNhbmRpZGF0ZSBicmFuY2guIiwKICAgICAgICAiYm91bmRhcnkiOiAiVGhyZXNob2xkIGdvdmVybmFuY2Ugc3VtbWFyaWVzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgbWlsZXN0b25lIGFydGlmYWN0cy4gVGhleSBzdW1tYXJpemUgdGhyZXNob2xkIHJldmlldywgY29udHJvbHMsIGRyeS1ydW5zLCBhbmQgZGVjaXNpb25zLiBUaGV5IGRvIG5vdCBjcmVhdGUgbGl2ZSBhcHByb3ZhbCwgZXhlY3V0ZSByZXBsYXkgY29tbWFuZHMsIGNyZWF0ZSBicmFuY2hlcywgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFwcGx5IGNhbGlicmF0aW9uLCBjaGFuZ2UgdGhyZXNob2xkcywgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJ0aHJlc2hvbGRfZ292ZXJuYW5jZV9zdW1tYXJ5X3YwXzdfOS5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfdGhyZXNob2xkX2dvdmVybmFuY2Vfc3VtbWFyeS5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJ0aHJlc2hvbGRfZ292ZXJuYW5jZV9zdW1tYXJ5X3YwXzdfOS5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3RocmVzaG9sZF9nb3Zlcm5hbmNlX3N1bW1hcnkubWQiLCBtYWtlX21kKHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAic3VtbWFyeV9zdGF0dXMiOiBzdW1tYXJ5WyJzdW1tYXJ5X3N0YXR1cyJdLAogICAgICAgICJzdW1tYXJ5X2xvY2tlZCI6IHN1bW1hcnlbInN1bW1hcnlfbG9ja2VkIl0sCiAgICAgICAgInRocmVzaG9sZF9kZWNpc2lvbiI6IHN1bW1hcnlbInRocmVzaG9sZF9kZWNpc2lvbiJdLAogICAgICAgICJzY2VuYXJpb19jb3VudCI6IHN1bW1hcnlbInNjZW5hcmlvX2NvdW50Il0sCiAgICAgICAgImhpZ2hfYXR0ZW50aW9uX2NvdW50Ijogc3VtbWFyeVsiaGlnaF9hdHRlbnRpb25fY291bnQiXSwKICAgICAgICAidmlvbGF0aW9uX2NvdW50Ijogc3VtbWFyeVsidmlvbGF0aW9uX2NvdW50Il0sCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IHN1bW1hcnlbInRocmVzaG9sZHNfY2hhbmdlZCJdLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBzdW1tYXJ5WyJjbGFzc2lmaWVyX2NoYW5nZWQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3RocmVzaG9sZF9nb3Zlcm5hbmNlX3N1bW1hcnkvbGF0ZXN0X3RocmVzaG9sZF9nb3Zlcm5hbmNlX3N1bW1hcnkubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT / "reports" / "threshold_governance_summary" / "README.md", """# Threshold Governance Summary Reports

Current layer: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**

## Purpose

This folder stores milestone summaries for v0.7.x threshold governance.

## Primary command

```powershell
python scripts/benchmarks/generate_threshold_governance_summary.py
```

## README Update Rule

Update this mini README whenever threshold governance summary, milestone status, or candidate-branch criteria change.

Boundary: threshold governance summaries are local classifier-governance milestone artifacts only.
""")

write(ROOT / "visuals" / "threshold_governance_summary" / "README.md", """# Threshold Governance Summary Visuals

Current layer: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**

## Purpose

This folder stores charts summarizing threshold governance state.

## README Update Rule

Update this mini README whenever threshold governance chart names or meanings change.

Boundary: threshold governance summary visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "threshold_governance_summary" / "v0_7_9" / "README.md", """# v0.7.9 Threshold Governance Summary Charts

Expected charts:

- `threshold_governance_chain_coverage.png`
- `threshold_governance_gap_counts.png`
- `threshold_governance_summary_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local threshold-governance diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.8[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.7[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.8 - Threshold Decision Record**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.8 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.9 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.8-ready |", "| Task routing matrix | geometry-aware / v0.7.9-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.8 |", "| Agent contract version sync | current / v0.7.9 |")

if "| Threshold governance summary |" not in r:
    r = r.replace("| Threshold decision charts | `visuals/threshold_decision_record/v0_7_8/` |\n",
                  "| Threshold decision charts | `visuals/threshold_decision_record/v0_7_8/` |\n| Threshold governance summary | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` |\n| Threshold governance charts | `visuals/threshold_governance_summary/v0_7_9/` |\n")

if "python scripts/benchmarks/generate_threshold_governance_summary.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_threshold_decision_record.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_threshold_decision_record.py\npython scripts/benchmarks/generate_threshold_governance_summary.py\npython scripts/release/validate_release.py")

if "    threshold_governance_summary/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    threshold_governance_summary/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    threshold_governance_summary/\n")

section = """## Threshold Governance Summary v0.7.9

v0.7.9 summarizes the full v0.7.x Tau mechanics and threshold-governance chain.

Primary command:

```powershell
python scripts/benchmarks/generate_threshold_governance_summary.py
```

Primary outputs:

```text
reports/threshold_governance_summary/latest_threshold_governance_summary.json
reports/threshold_governance_summary/latest_threshold_governance_summary.md
visuals/threshold_governance_summary/v0_7_9/
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

Boundary: threshold governance summaries are local classifier-governance milestone artifacts. They summarize threshold review, controls, dry-runs, and decisions. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Threshold Governance Summary v0.7.9" not in r:
    r = r.replace("## Threshold Decision Record v0.7.8", section + "## Threshold Decision Record v0.7.8", 1)

lesson = "| L-061 | v0.7.8 deferred threshold changes pending more evidence because high-attention pressure remained. | A deferral decision should become a stable summary before any further threshold work. | Threshold governance must be summarized as a milestone before candidate-branch or tuning discussions resume. |"
if "L-061" not in r:
    r = r.replace("| L-060 | v0.7.7 dry-ran threshold sensitivity in report-only mode. | Dry-run pressure is not a decision by itself. | Threshold sensitivity outputs must be compiled into a decision record before any candidate branch or threshold tuning is considered. |\n",
                  "| L-060 | v0.7.7 dry-ran threshold sensitivity in report-only mode. | Dry-run pressure is not a decision by itself. | Threshold sensitivity outputs must be compiled into a decision record before any candidate branch or threshold tuning is considered. |\n" + lesson + "\n")

if "| v0.7.9 |" not in r:
    r = r.replace("| v0.7.8 | Threshold decision record; converts dry-run pressure into a non-mutating decision. |\n",
                  "| v0.7.8 | Threshold decision record; converts dry-run pressure into a non-mutating decision. |\n| v0.7.9 | Threshold governance summary; summarizes v0.7.x and freezes threshold mutation pending more evidence. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**

Recommended goals:

- Package v0.7.1-v0.7.9 as a stable Tau mechanics/threshold-governance milestone.
- Freeze current threshold decision unless human review requests a candidate branch.
- Preserve no-classifier-mutation lock.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_threshold_governance_summary.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_threshold_decision_record.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_threshold_decision_record.py\npython scripts/benchmarks/generate_threshold_governance_summary.py\npython -m unittest discover -s tests")
        s = s.replace("| Threshold decision patch | `reports/threshold_decision_record/`, `visuals/threshold_decision_record/`, threshold dry-run | decision record + release validator; no mutation |\n",
                      "| Threshold decision patch | `reports/threshold_decision_record/`, `visuals/threshold_decision_record/`, threshold dry-run | decision record + release validator; no mutation |\n| Threshold governance summary patch | `reports/threshold_governance_summary/`, `visuals/threshold_governance_summary/`, v0.7 reports | milestone summary + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Threshold governance summary patch |" not in s:
        s = s.replace("| Threshold decision patch | inner | decision | classifier | threshold sensitivity dry-run | non-mutating decision record + charts + release validator | `reports/threshold_decision_record/latest_threshold_decision_record.md` |\n",
                      "| Threshold decision patch | inner | decision | classifier | threshold sensitivity dry-run | non-mutating decision record + charts + release validator | `reports/threshold_decision_record/latest_threshold_decision_record.md` |\n| Threshold governance summary patch | inner | milestone | classifier | v0.7 Tau mechanics reports | milestone summary + charts + release validator | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.9"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["threshold_governance_summary"] = {
    "read_first": ["reports/threshold_decision_record/latest_threshold_decision_record.json", "reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.json"],
    "validate": ["python scripts/benchmarks/generate_threshold_governance_summary.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/threshold_governance_summary/latest_threshold_governance_summary.md", "visuals/threshold_governance_summary/v0_7_9/"],
    "mutation_lock": "Milestone summary only; no classifier change, threshold change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.9 | Threshold governance summary |" not in t:
    t = t.replace("| v0.7.8 | Threshold decision record | `python scripts/benchmarks/generate_threshold_decision_record.py` | Converts threshold dry-run pressure into non-mutating decision | `reports/threshold_decision_record/latest_threshold_decision_record.md` | `visuals/threshold_decision_record/v0_7_8/` |\n",
                  "| v0.7.8 | Threshold decision record | `python scripts/benchmarks/generate_threshold_decision_record.py` | Converts threshold dry-run pressure into non-mutating decision | `reports/threshold_decision_record/latest_threshold_decision_record.md` | `visuals/threshold_decision_record/v0_7_8/` |\n| v0.7.9 | Threshold governance summary | `python scripts/benchmarks/generate_threshold_governance_summary.py` | Summarizes v0.7.x and freezes threshold mutation pending more evidence | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` | `visuals/threshold_governance_summary/v0_7_9/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_9_threshold_governance_summary.md", f"""# TAU-SCALING-SA v0.7.9 - Threshold Governance Summary

Generated: {NOW}

## Purpose

Summarize the full v0.7.x Tau mechanics and threshold-governance chain after the threshold decision record deferred threshold changes pending more evidence.

## Boundary

Threshold governance summaries are local classifier-governance milestone artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.9 patch written")
