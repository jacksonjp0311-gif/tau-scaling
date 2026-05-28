
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
        d = ROOT / "reports" / "stable_tau_threshold_governance" / "v0_8_0" / "backups" / f"{p.name}_before_v0_8_0_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_stable_tau_threshold_governance_milestone.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInN0YWJsZV90YXVfdGhyZXNob2xkX2dvdmVybmFuY2UiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAic3RhYmxlX3RhdV90aHJlc2hvbGRfZ292ZXJuYW5jZSIgLyAidjBfOF8wIgoKSU5QVVRTID0gewogICAgImFwcHJvdmFsX2NvcnJpZG9yIjogUk9PVCAvICJyZXBvcnRzIiAvICJhcHByb3ZhbF9jb3JyaWRvciIgLyAibGF0ZXN0X2FwcHJvdmFsX2dvdmVybmFuY2VfY29ycmlkb3JfbWlsZXN0b25lLmpzb24iLAogICAgInRhdV9tZWNoYW5pY3MiOiBST09UIC8gInJlcG9ydHMiIC8gInRhdV9tZWNoYW5pY3NfcmV2aWV3IiAvICJsYXRlc3RfdGF1X21lY2hhbmljc19yZXR1cm5fcmV2aWV3Lmpzb24iLAogICAgInRhdV92ZWN0b3IiOiBST09UIC8gInJlcG9ydHMiIC8gInRhdV92ZWN0b3Jfc2VtYW50aWNzIiAvICJsYXRlc3RfdGF1X3ZlY3Rvcl9zZW1hbnRpY3NfbGVkZ2VyLmpzb24iLAogICAgImdhdGVfYWxnZWJyYSI6IFJPT1QgLyAicmVwb3J0cyIgLyAiZ2F0ZV9hbGdlYnJhIiAvICJsYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5qc29uIiwKICAgICJ0aHJlc2hvbGRfcmV2aWV3IjogUk9PVCAvICJyZXBvcnRzIiAvICJ0c2VrX3RocmVzaG9sZF9yZXZpZXciIC8gImxhdGVzdF90c2VrX3RocmVzaG9sZF9ib3VuZGFyeV9yZXZpZXcuanNvbiIsCiAgICAiYm91bmRhcnlfY2FyZHMiOiBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfYm91bmRhcnlfY2FyZHMiIC8gImxhdGVzdF90c2VrX2JvdW5kYXJ5X2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iLAogICAgInBlbmFsdHlfY29udHJvbHMiOiBST09UIC8gInJlcG9ydHMiIC8gInBlbmFsdHlfY29udHJvbHMiIC8gImxhdGVzdF9vdmVyX3VuZGVyX3BlbmFsdHlfbmVnYXRpdmVfY29udHJvbHMuanNvbiIsCiAgICAidGhyZXNob2xkX3NlbnNpdGl2aXR5IjogUk9PVCAvICJyZXBvcnRzIiAvICJ0aHJlc2hvbGRfc2Vuc2l0aXZpdHlfZHJ5X3J1biIgLyAibGF0ZXN0X3RocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuLmpzb24iLAogICAgInRocmVzaG9sZF9kZWNpc2lvbiI6IFJPT1QgLyAicmVwb3J0cyIgLyAidGhyZXNob2xkX2RlY2lzaW9uX3JlY29yZCIgLyAibGF0ZXN0X3RocmVzaG9sZF9kZWNpc2lvbl9yZWNvcmQuanNvbiIsCiAgICAidGhyZXNob2xkX2dvdmVybmFuY2UiOiBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9nb3Zlcm5hbmNlX3N1bW1hcnkiIC8gImxhdGVzdF90aHJlc2hvbGRfZ292ZXJuYW5jZV9zdW1tYXJ5Lmpzb24iLAogICAgInJlbGVhc2UiOiBST09UIC8gInJlcG9ydHMiIC8gInJlbGVhc2UiIC8gImxhdGVzdF9yZWxlYXNlX3JlYWRpbmVzcy5qc29uIiwKfQoKQ0hBSU4gPSBbCiAgICAoInYwLjcuMCIsICJhcHByb3ZhbF9jb3JyaWRvciIsICJjb3JyaWRvcl9zdGF0dXMiKSwKICAgICgidjAuNy4xIiwgInRhdV9tZWNoYW5pY3MiLCAibWVjaGFuaWNzX3N0YXR1cyIpLAogICAgKCJ2MC43LjIiLCAidGF1X3ZlY3RvciIsICJzZW1hbnRpY3Nfc3RhdHVzIiksCiAgICAoInYwLjcuMyIsICJnYXRlX2FsZ2VicmEiLCAiZ2F0ZV9hbGdlYnJhX3N0YXR1cyIpLAogICAgKCJ2MC43LjQiLCAidGhyZXNob2xkX3JldmlldyIsICJ0aHJlc2hvbGRfcmV2aWV3X3N0YXR1cyIpLAogICAgKCJ2MC43LjUiLCAiYm91bmRhcnlfY2FyZHMiLCAiY2FyZF9zdGF0dXMiKSwKICAgICgidjAuNy42IiwgInBlbmFsdHlfY29udHJvbHMiLCAiY29udHJvbF9zdGF0dXMiKSwKICAgICgidjAuNy43IiwgInRocmVzaG9sZF9zZW5zaXRpdml0eSIsICJkcnlfcnVuX3N0YXR1cyIpLAogICAgKCJ2MC43LjgiLCAidGhyZXNob2xkX2RlY2lzaW9uIiwgImRlY2lzaW9uX3N0YXR1cyIpLAogICAgKCJ2MC43LjkiLCAidGhyZXNob2xkX2dvdmVybmFuY2UiLCAic3VtbWFyeV9zdGF0dXMiKSwKXQoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiB7Im1pc3NpbmciOiBUcnVlLCAicGF0aCI6IHN0cihwYXRoKX0KICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHJldHVybiB7InBhcnNlX2Vycm9yIjogc3RyKGV4YyksICJwYXRoIjogc3RyKHBhdGgpfQoKZGVmIHdqc29uKHBhdGg6IFBhdGgsIGRhdGEpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMoZGF0YSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwYXRoOiBQYXRoKToKICAgIHJldHVybiBzdHIocGF0aC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgcm93cyhkYXRhKToKICAgIG91dCA9IFtdCiAgICBmb3IgdmVyc2lvbiwga2V5LCBzdGF0dXNfa2V5IGluIENIQUlOOgogICAgICAgIGQgPSBkYXRhW2tleV0KICAgICAgICBvdXQuYXBwZW5kKHsKICAgICAgICAgICAgInZlcnNpb24iOiB2ZXJzaW9uLAogICAgICAgICAgICAiYXJ0aWZhY3QiOiBrZXksCiAgICAgICAgICAgICJzdGF0dXMiOiBkLmdldChzdGF0dXNfa2V5LCAiTUlTU0lORyIgaWYgZC5nZXQoIm1pc3NpbmciKSBlbHNlICJSRUNPUkRFRCIpLAogICAgICAgICAgICAibWlzc2luZyI6IGJvb2woZC5nZXQoIm1pc3NpbmciKSksCiAgICAgICAgICAgICJ0aHJlc2hvbGRzX2NoYW5nZWQiOiBib29sKGQuZ2V0KCJ0aHJlc2hvbGRzX2NoYW5nZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogYm9vbChkLmdldCgiY2xhc3NpZmllcl9jaGFuZ2VkIiwgRmFsc2UpKSwKICAgICAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBib29sKGQuZ2V0KCJtdXRhdGlvbl9hbGxvd2VkIiwgRmFsc2UpKSwKICAgICAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBib29sKGQuZ2V0KCJhcHBsaWNhdGlvbl9hbGxvd2VkIiwgRmFsc2UpKSwKICAgICAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBib29sKGQuZ2V0KCJjYWxpYnJhdGlvbl9hcHBsaWVkIiwgRmFsc2UpKSwKICAgICAgICAgICAgInJlcGxheV9hbGxvd2VkIjogYm9vbChkLmdldCgicmVwbGF5X2FsbG93ZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBib29sKGQuZ2V0KCJicmFuY2hfY3JlYXRlZCIsIEZhbHNlKSksCiAgICAgICAgICAgICJnYXBfY291bnQiOiBpbnQoZC5nZXQoImdhcF9jb3VudCIsIDApIG9yIDApLAogICAgICAgIH0pCiAgICByZXR1cm4gb3V0CgpkZWYgY2xhc3NpZnkoZGF0YSwgY2hhaW5fcm93cyk6CiAgICByZWxlYXNlID0gZGF0YVsicmVsZWFzZSJdCiAgICByZWxlYXNlX3Bhc3NlZCA9IHJlbGVhc2UuZ2V0KCJwYXNzZWQiKSBpcyBUcnVlIGFuZCBsZW4ocmVsZWFzZS5nZXQoImZpbmRpbmdzIiwgW10pKSA9PSAwIGFuZCBsZW4ocmVsZWFzZS5nZXQoInN0ZXBfZmFpbHVyZXMiLCBbXSkpID09IDAKICAgIGdvdiA9IGRhdGFbInRocmVzaG9sZF9nb3Zlcm5hbmNlIl0KICAgIGRlY2lzaW9uID0gZGF0YVsidGhyZXNob2xkX2RlY2lzaW9uIl0KCiAgICB2aW9sYXRpb25zID0gW10KICAgIGZvciByb3cgaW4gY2hhaW5fcm93czoKICAgICAgICBmb3Iga2V5IGluIFsidGhyZXNob2xkc19jaGFuZ2VkIiwgImNsYXNzaWZpZXJfY2hhbmdlZCIsICJtdXRhdGlvbl9hbGxvd2VkIiwgImFwcGxpY2F0aW9uX2FsbG93ZWQiLCAiY2FsaWJyYXRpb25fYXBwbGllZCIsICJyZXBsYXlfYWxsb3dlZCIsICJicmFuY2hfY3JlYXRlZCJdOgogICAgICAgICAgICBpZiByb3dba2V5XSBpcyBUcnVlOgogICAgICAgICAgICAgICAgdmlvbGF0aW9ucy5hcHBlbmQoeyJhcnRpZmFjdCI6IHJvd1siYXJ0aWZhY3QiXSwgInZpb2xhdGlvbiI6IGtleX0pCgogICAgbWlzc2luZyA9IFtyb3dbImFydGlmYWN0Il0gZm9yIHJvdyBpbiBjaGFpbl9yb3dzIGlmIHJvd1sibWlzc2luZyJdXQogICAgY29ycmVjdF9kZWNpc2lvbiA9IGRlY2lzaW9uLmdldCgidGhyZXNob2xkX2RlY2lzaW9uIikgPT0gIkRFRkVSX1RIUkVTSE9MRF9DSEFOR0VfUEVORElOR19NT1JFX0VWSURFTkNFIgogICAgZ292X2xvY2tlZCA9IGdvdi5nZXQoInN1bW1hcnlfbG9ja2VkIikgaXMgVHJ1ZQogICAgbWlsZXN0b25lX2xvY2tlZCA9IHJlbGVhc2VfcGFzc2VkIGFuZCBub3QgdmlvbGF0aW9ucyBhbmQgbm90IG1pc3NpbmcgYW5kIGNvcnJlY3RfZGVjaXNpb24gYW5kIGdvdl9sb2NrZWQKCiAgICBzdGF0dXMgPSAiU1RBQkxFX1RBVV9USFJFU0hPTERfR09WRVJOQU5DRV9NSUxFU1RPTkVfTE9DS0VEX19OT19NVVRBVElPTiIgaWYgbWlsZXN0b25lX2xvY2tlZCBlbHNlICJTVEFCTEVfVEFVX1RIUkVTSE9MRF9HT1ZFUk5BTkNFX01JTEVTVE9ORV9ORUVEU19SRVZJRVciCiAgICByZXR1cm4gc3RhdHVzLCBtaWxlc3RvbmVfbG9ja2VkLCByZWxlYXNlX3Bhc3NlZCwgY29ycmVjdF9kZWNpc2lvbiwgZ292X2xvY2tlZCwgdmlvbGF0aW9ucywgbWlzc2luZwoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihleGMpKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICByb3dzID0gc3VtbWFyeVsibWlsZXN0b25lX2NoYWluIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTEsIDQpKQogICAgcGx0LmJhcihbclsidmVyc2lvbiJdIGZvciByIGluIHJvd3NdLCBbMCBpZiByWyJtaXNzaW5nIl0gZWxzZSAxIGZvciByIGluIHJvd3NdKQogICAgcGx0LnlsYWJlbCgiUHJlc2VudCIpCiAgICBwbHQudGl0bGUoInYwLjguMCBNaWxlc3RvbmUgQ2hhaW4gQ292ZXJhZ2UiKQogICAgc2F2ZSgic3RhYmxlX3RhdV90aHJlc2hvbGRfY2hhaW5fY292ZXJhZ2UucG5nIikKCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDExLCA0KSkKICAgIHBsdC5iYXIoW3JbInZlcnNpb24iXSBmb3IgciBpbiByb3dzXSwgW3JbImdhcF9jb3VudCJdIGZvciByIGluIHJvd3NdKQogICAgcGx0LnlsYWJlbCgiR2FwIGNvdW50IikKICAgIHBsdC50aXRsZSgidjAuOC4wIE1pbGVzdG9uZSBHYXAgQ29tcHJlc3Npb24iKQogICAgc2F2ZSgic3RhYmxlX3RhdV90aHJlc2hvbGRfZ2FwX2NvbXByZXNzaW9uLnBuZyIpCgogICAgaGVhbHRoID0gewogICAgICAgICJtaWxlc3RvbmVfbG9ja2VkIjogaW50KHN1bW1hcnlbIm1pbGVzdG9uZV9sb2NrZWQiXSksCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJkZWNpc2lvbl9kZWZlcnJlZCI6IGludChzdW1tYXJ5WyJ0aHJlc2hvbGRfZGVjaXNpb25fZGVmZXJyZWQiXSksCiAgICAgICAgInZpb2xhdGlvbnMiOiBzdW1tYXJ5WyJ2aW9sYXRpb25fY291bnQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgidjAuOC4wIFN0YWJsZSBNaWxlc3RvbmUgSGVhbHRoIikKICAgIHNhdmUoInN0YWJsZV90YXVfdGhyZXNob2xkX21pbGVzdG9uZV9oZWFsdGgucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC44LjAgU3RhYmxlIFRhdSBUaHJlc2hvbGQgR292ZXJuYW5jZSBNaWxlc3RvbmUiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBNaWxlc3RvbmUgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gTWlsZXN0b25lIHN0YXR1czogYHtzdW1tYXJ5WydtaWxlc3RvbmVfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIE1pbGVzdG9uZSBsb2NrZWQ6IGB7c3VtbWFyeVsnbWlsZXN0b25lX2xvY2tlZCddfWAiLAogICAgICAgIGYiLSBUaHJlc2hvbGQgZGVjaXNpb246IGB7c3VtbWFyeVsndGhyZXNob2xkX2RlY2lzaW9uJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIFRocmVzaG9sZCBnb3Zlcm5hbmNlIGxvY2tlZDogYHtzdW1tYXJ5Wyd0aHJlc2hvbGRfZ292ZXJuYW5jZV9sb2NrZWQnXX1gIiwKICAgICAgICBmIi0gVmlvbGF0aW9uIGNvdW50OiBge3N1bW1hcnlbJ3Zpb2xhdGlvbl9jb3VudCddfWAiLAogICAgICAgIGYiLSBNaXNzaW5nIGNvdW50OiBge3N1bW1hcnlbJ21pc3NpbmdfY291bnQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgTWlsZXN0b25lIENoYWluIiwKICAgICAgICAiIiwKICAgICAgICAifCBWZXJzaW9uIHwgQXJ0aWZhY3QgfCBTdGF0dXMgfCBHYXBzIHwgVGhyZXNob2xkIGNoYW5nZWQgfCBDbGFzc2lmaWVyIGNoYW5nZWQgfCBNdXRhdGlvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLTp8LS0tOnwtLS06fC0tLTp8IiwKICAgIF0KICAgIGZvciByb3cgaW4gc3VtbWFyeVsibWlsZXN0b25lX2NoYWluIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3Jvd1sndmVyc2lvbiddfWAgfCBge3Jvd1snYXJ0aWZhY3QnXX1gIHwgYHtyb3dbJ3N0YXR1cyddfWAgfCB7cm93WydnYXBfY291bnQnXX0gfCBge3Jvd1sndGhyZXNob2xkc19jaGFuZ2VkJ119YCB8IGB7cm93WydjbGFzc2lmaWVyX2NoYW5nZWQnXX1gIHwgYHtyb3dbJ211dGF0aW9uX2FsbG93ZWQnXX1gIHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgU3RhYmxlIERlY2lzaW9uIiwKICAgICAgICAiIiwKICAgICAgICAiVGhlIHN0YWJsZSB2MC44LjAgZGVjaXNpb24gaXMgdG8gKipkZWZlciB0aHJlc2hvbGQgY2hhbmdlIHBlbmRpbmcgbW9yZSBldmlkZW5jZSoqLiBUaGUgc3lzdGVtIGZvdW5kIHJlYWwgcHJlc3N1cmUgc3VyZmFjZXMsIGJ1dCBub3QgZW5vdWdoIGV2aWRlbmNlIHRvIHR1bmUgdGhyZXNob2xkcyBvciBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvci4iLAogICAgICAgICIiLAogICAgICAgICIjIyBFeHBsaWNpdCBMb2NrcyIsCiAgICAgICAgIiIsCiAgICAgICAgImBgYHRleHQiLAogICAgICAgIGYidGhyZXNob2xkc19jaGFuZ2VkOiB7c3RyKHN1bW1hcnlbJ3RocmVzaG9sZHNfY2hhbmdlZCddKS5sb3dlcigpfSIsCiAgICAgICAgZiJjbGFzc2lmaWVyX2NoYW5nZWQ6IHtzdHIoc3VtbWFyeVsnY2xhc3NpZmllcl9jaGFuZ2VkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmIm11dGF0aW9uX2FsbG93ZWQ6IHtzdHIoc3VtbWFyeVsnbXV0YXRpb25fYWxsb3dlZCddKS5sb3dlcigpfSIsCiAgICAgICAgZiJhcHBsaWNhdGlvbl9hbGxvd2VkOiB7c3RyKHN1bW1hcnlbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXSkubG93ZXIoKX0iLAogICAgICAgIGYiY2FsaWJyYXRpb25fYXBwbGllZDoge3N0cihzdW1tYXJ5WydjYWxpYnJhdGlvbl9hcHBsaWVkJ10pLmxvd2VyKCl9IiwKICAgICAgICBmImNhbmRpZGF0ZV9icmFuY2hfY3JlYXRlZDoge3N0cihzdW1tYXJ5WydjYW5kaWRhdGVfYnJhbmNoX2NyZWF0ZWQnXSkubG93ZXIoKX0iLAogICAgICAgICJgYGAiLAogICAgICAgICIiLAogICAgICAgICIjIyBXaGF0IFRoaXMgTWlsZXN0b25lIE1lYW5zIiwKICAgICAgICAiIiwKICAgICAgICAidjAuOC4wIGNsb3NlcyB0aGUgZmlyc3QgVGF1IG1lY2hhbmljcyByZXR1cm4gYXJjOiBhcHByb3ZhbCBjb250YWlubWVudCwgdGF1IHNlbWFudGljcywgZ2F0ZSBhbGdlYnJhLCB0aHJlc2hvbGQgcmV2aWV3LCBib3VuZGFyeSBjYXJkcywgcGVuYWx0eSBjb250cm9scywgZHJ5LXJ1biwgZGVjaXNpb24gcmVjb3JkLCBhbmQgZ292ZXJuYW5jZSBzdW1tYXJ5LiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIE5leHQgV29yayIsCiAgICAgICAgIiIsCiAgICAgICAgIjEuIEFkZCBtb3JlIHNjZW5hcmlvIGV2aWRlbmNlIGZvciB0aGUgdHdvIGhpZ2gtYXR0ZW50aW9uIHRocmVzaG9sZCBwcmVzc3VyZXMuIiwKICAgICAgICAiMi4gS2VlcCB0aHJlc2hvbGRzIGZyb3plbiB1bmxlc3MgaHVtYW4gcmV2aWV3IGV4cGxpY2l0bHkgcmVxdWVzdHMgYSBjYW5kaWRhdGUgYnJhbmNoLiIsCiAgICAgICAgIjMuIEtlZXAgY2xhc3NpZmllciBtdXRhdGlvbiBkaXNhYmxlZC4iLAogICAgICAgICI0LiBVc2UgdjAuOC54IGZvciBldmlkZW5jZSBleHBhbnNpb24sIG5vdCB0aHJlc2hvbGQgdHVuaW5nLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENoYXJ0cyIsCiAgICAgICAgIiIsCiAgICBdCiAgICBmb3IgcCBpbiBzdW1tYXJ5WyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc3VtbWFyeVsiYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIGRhdGEgPSB7azogcmVhZF9qc29uKHYpIGZvciBrLCB2IGluIElOUFVUUy5pdGVtcygpfQogICAgY2hhaW5fcm93cyA9IHJvd3MoZGF0YSkKICAgIHN0YXR1cywgbG9ja2VkLCByZWxlYXNlX3Bhc3NlZCwgZGVjaXNpb25fZGVmZXJyZWQsIGdvdl9sb2NrZWQsIHZpb2xhdGlvbnMsIG1pc3NpbmcgPSBjbGFzc2lmeShkYXRhLCBjaGFpbl9yb3dzKQogICAgZGVjaXNpb24gPSBkYXRhWyJ0aHJlc2hvbGRfZGVjaXNpb24iXS5nZXQoInRocmVzaG9sZF9kZWNpc2lvbiIsICJVTktOT1dOIikKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctc3RhYmxlLXRhdS10aHJlc2hvbGQtZ292ZXJuYW5jZS1taWxlc3RvbmUtdjAuOC4wIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgIm1pbGVzdG9uZV9zdGF0dXMiOiBzdGF0dXMsCiAgICAgICAgIm1pbGVzdG9uZV9sb2NrZWQiOiBib29sKGxvY2tlZCksCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogYm9vbChyZWxlYXNlX3Bhc3NlZCksCiAgICAgICAgInRocmVzaG9sZF9kZWNpc2lvbiI6IGRlY2lzaW9uLAogICAgICAgICJ0aHJlc2hvbGRfZGVjaXNpb25fZGVmZXJyZWQiOiBib29sKGRlY2lzaW9uX2RlZmVycmVkKSwKICAgICAgICAidGhyZXNob2xkX2dvdmVybmFuY2VfbG9ja2VkIjogYm9vbChnb3ZfbG9ja2VkKSwKICAgICAgICAibWlsZXN0b25lX2NoYWluIjogY2hhaW5fcm93cywKICAgICAgICAidmlvbGF0aW9uX2NvdW50IjogbGVuKHZpb2xhdGlvbnMpLAogICAgICAgICJ2aW9sYXRpb25zIjogdmlvbGF0aW9ucywKICAgICAgICAibWlzc2luZ19jb3VudCI6IGxlbihtaXNzaW5nKSwKICAgICAgICAibWlzc2luZ19hcnRpZmFjdHMiOiBtaXNzaW5nLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJ0aHJlc2hvbGRzX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgImNhbmRpZGF0ZV9icmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogIlVzZSB2MC44LnggZm9yIHNjZW5hcmlvIGV2aWRlbmNlIGV4cGFuc2lvbi4gRG8gbm90IHR1bmUgdGhyZXNob2xkcyBvciBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciB3aXRob3V0IGV4cGxpY2l0IGh1bWFuIHJldmlldyBhbmQgYSBjYW5kaWRhdGUgYnJhbmNoIGdhdGUuIiwKICAgICAgICAiYm91bmRhcnkiOiAiU3RhYmxlIFRhdSB0aHJlc2hvbGQgZ292ZXJuYW5jZSBtaWxlc3RvbmVzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgbWlsZXN0b25lIGFydGlmYWN0cy4gVGhleSBwYWNrYWdlIGV2aWRlbmNlLCBkcnktcnVucywgYW5kIGRlY2lzaW9ucyBpbnRvIGEgc3RhYmxlIHJlbGVhc2Ugc3VyZmFjZS4gVGhleSBkbyBub3QgY3JlYXRlIGxpdmUgYXBwcm92YWwsIGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzLCBjcmVhdGUgYnJhbmNoZXMsIG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhcHBseSBjYWxpYnJhdGlvbiwgY2hhbmdlIHRocmVzaG9sZHMsIG9yIHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAic3RhYmxlX3RhdV90aHJlc2hvbGRfZ292ZXJuYW5jZV9taWxlc3RvbmVfdjBfOF8wLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9zdGFibGVfdGF1X3RocmVzaG9sZF9nb3Zlcm5hbmNlX21pbGVzdG9uZS5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJzdGFibGVfdGF1X3RocmVzaG9sZF9nb3Zlcm5hbmNlX21pbGVzdG9uZV92MF84XzAubWQiLCBtYWtlX21kKHN1bW1hcnkpKQogICAgd3RleHQoT1VUIC8gImxhdGVzdF9zdGFibGVfdGF1X3RocmVzaG9sZF9nb3Zlcm5hbmNlX21pbGVzdG9uZS5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJtaWxlc3RvbmVfc3RhdHVzIjogc3VtbWFyeVsibWlsZXN0b25lX3N0YXR1cyJdLAogICAgICAgICJtaWxlc3RvbmVfbG9ja2VkIjogc3VtbWFyeVsibWlsZXN0b25lX2xvY2tlZCJdLAogICAgICAgICJ0aHJlc2hvbGRfZGVjaXNpb24iOiBzdW1tYXJ5WyJ0aHJlc2hvbGRfZGVjaXNpb24iXSwKICAgICAgICAidGhyZXNob2xkX2RlY2lzaW9uX2RlZmVycmVkIjogc3VtbWFyeVsidGhyZXNob2xkX2RlY2lzaW9uX2RlZmVycmVkIl0sCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IHN1bW1hcnlbInRocmVzaG9sZHNfY2hhbmdlZCJdLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBzdW1tYXJ5WyJjbGFzc2lmaWVyX2NoYW5nZWQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3N0YWJsZV90YXVfdGhyZXNob2xkX2dvdmVybmFuY2UvbGF0ZXN0X3N0YWJsZV90YXVfdGhyZXNob2xkX2dvdmVybmFuY2VfbWlsZXN0b25lLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT / "reports" / "stable_tau_threshold_governance" / "README.md", """# Stable Tau Threshold Governance Reports

Current layer: **TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**

## Purpose

This folder stores the stable milestone package for the v0.7.x Tau mechanics and threshold governance arc.

## Primary command

```powershell
python scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py
```

## README Update Rule

Update this mini README whenever the stable threshold governance milestone or v0.8.x evidence-expansion path changes.

Boundary: stable Tau threshold governance reports are local classifier-governance milestone artifacts only.
""")

write(ROOT / "visuals" / "stable_tau_threshold_governance" / "README.md", """# Stable Tau Threshold Governance Visuals

Current layer: **TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**

## Purpose

This folder stores charts summarizing the stable v0.8.0 milestone.

## README Update Rule

Update this mini README whenever stable milestone chart names or meanings change.

Boundary: stable Tau threshold governance visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "stable_tau_threshold_governance" / "v0_8_0" / "README.md", """# v0.8.0 Stable Tau Threshold Governance Charts

Expected charts:

- `stable_tau_threshold_chain_coverage.png`
- `stable_tau_threshold_gap_compression.png`
- `stable_tau_threshold_milestone_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local stable threshold-governance diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.9[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.8[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.9 - Threshold Governance Summary**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.9 \|", "| Current checkpoint | TAU-SCALING-SA v0.8.0 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.9-ready |", "| Task routing matrix | geometry-aware / v0.8.0-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.9 |", "| Agent contract version sync | current / v0.8.0 |")

if "| Stable Tau threshold governance |" not in r:
    r = r.replace("| Threshold governance charts | `visuals/threshold_governance_summary/v0_7_9/` |\n",
                  "| Threshold governance charts | `visuals/threshold_governance_summary/v0_7_9/` |\n| Stable Tau threshold governance | `reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md` |\n| Stable Tau threshold charts | `visuals/stable_tau_threshold_governance/v0_8_0/` |\n")

if "python scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_threshold_governance_summary.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_threshold_governance_summary.py\npython scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py\npython scripts/release/validate_release.py")

if "    stable_tau_threshold_governance/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    stable_tau_threshold_governance/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    stable_tau_threshold_governance/\n")

section = """## Stable Tau Threshold Governance Milestone v0.8.0

v0.8.0 packages the full v0.7.x Tau mechanics and threshold-governance chain into a stable milestone.

Primary command:

```powershell
python scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py
```

Primary outputs:

```text
reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.json
reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md
visuals/stable_tau_threshold_governance/v0_8_0/
```

Current lock:

```text
threshold_decision: DEFER_THRESHOLD_CHANGE_PENDING_MORE_EVIDENCE
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

Boundary: stable Tau threshold governance milestones are local classifier-governance milestone artifacts. They package evidence, dry-runs, and decisions into a stable release surface. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Stable Tau Threshold Governance Milestone v0.8.0" not in r:
    r = r.replace("## Threshold Governance Summary v0.7.9", section + "## Threshold Governance Summary v0.7.9", 1)

lesson = "| L-062 | v0.7.9 locked threshold governance with a deferred threshold-change decision. | A locked governance summary should be promoted into a stable milestone before any new evidence-expansion path starts. | v0.8.0 must package v0.7.x as a stable no-mutation milestone and route future work to scenario evidence expansion. |"
if "L-062" not in r:
    r = r.replace("| L-061 | v0.7.8 deferred threshold changes pending more evidence because high-attention pressure remained. | A deferral decision should become a stable summary before any further threshold work. | Threshold governance must be summarized as a milestone before candidate-branch or tuning discussions resume. |\n",
                  "| L-061 | v0.7.8 deferred threshold changes pending more evidence because high-attention pressure remained. | A deferral decision should become a stable summary before any further threshold work. | Threshold governance must be summarized as a milestone before candidate-branch or tuning discussions resume. |\n" + lesson + "\n")

if "| v0.8.0 |" not in r:
    r = r.replace("| v0.7.9 | Threshold governance summary; summarizes v0.7.x and freezes threshold mutation pending more evidence. |\n",
                  "| v0.7.9 | Threshold governance summary; summarizes v0.7.x and freezes threshold mutation pending more evidence. |\n| v0.8.0 | Stable Tau threshold governance milestone; packages v0.7.x and routes future work to evidence expansion. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.8.1 - High-Attention Scenario Evidence Expansion**

Recommended goals:

- Expand evidence for the two high-attention threshold pressure surfaces.
- Keep threshold and classifier mutation disabled.
- Preserve no-candidate-branch behavior unless explicitly approved by human review.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_stable_tau_threshold_governance_milestone.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_threshold_governance_summary.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_threshold_governance_summary.py\npython scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py\npython -m unittest discover -s tests")
        s = s.replace("| Threshold governance summary patch | `reports/threshold_governance_summary/`, `visuals/threshold_governance_summary/`, v0.7 reports | milestone summary + release validator; no mutation |\n",
                      "| Threshold governance summary patch | `reports/threshold_governance_summary/`, `visuals/threshold_governance_summary/`, v0.7 reports | milestone summary + release validator; no mutation |\n| Stable threshold governance patch | `reports/stable_tau_threshold_governance/`, `visuals/stable_tau_threshold_governance/`, v0.7 reports | stable milestone + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Stable threshold governance patch |" not in s:
        s = s.replace("| Threshold governance summary patch | inner | milestone | classifier | v0.7 Tau mechanics reports | milestone summary + charts + release validator | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` |\n",
                      "| Threshold governance summary patch | inner | milestone | classifier | v0.7 Tau mechanics reports | milestone summary + charts + release validator | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` |\n| Stable threshold governance patch | inner | milestone | classifier | v0.7 reports + threshold decision | stable milestone + charts + release validator | `reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.8.0"
route["updated_at"] = NOW
route.setdefault("v0_8_routes", {})["stable_tau_threshold_governance_milestone"] = {
    "read_first": ["reports/threshold_governance_summary/latest_threshold_governance_summary.json", "reports/threshold_decision_record/latest_threshold_decision_record.json"],
    "validate": ["python scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md", "visuals/stable_tau_threshold_governance/v0_8_0/"],
    "mutation_lock": "Stable milestone only; no classifier change, threshold change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.8.0 | Stable Tau threshold governance milestone |" not in t:
    t = t.replace("| v0.7.9 | Threshold governance summary | `python scripts/benchmarks/generate_threshold_governance_summary.py` | Summarizes v0.7.x and freezes threshold mutation pending more evidence | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` | `visuals/threshold_governance_summary/v0_7_9/` |\n",
                  "| v0.7.9 | Threshold governance summary | `python scripts/benchmarks/generate_threshold_governance_summary.py` | Summarizes v0.7.x and freezes threshold mutation pending more evidence | `reports/threshold_governance_summary/latest_threshold_governance_summary.md` | `visuals/threshold_governance_summary/v0_7_9/` |\n| v0.8.0 | Stable Tau threshold governance milestone | `python scripts/benchmarks/generate_stable_tau_threshold_governance_milestone.py` | Packages v0.7.x and routes future work to evidence expansion | `reports/stable_tau_threshold_governance/latest_stable_tau_threshold_governance_milestone.md` | `visuals/stable_tau_threshold_governance/v0_8_0/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_8_0_stable_threshold_governance.md", f"""# TAU-SCALING-SA v0.8.0 - Stable Tau Threshold Governance Milestone

Generated: {NOW}

## Purpose

Package the full v0.7.x Tau mechanics and threshold-governance chain into a stable milestone.

## Boundary

Stable Tau threshold governance milestones are local classifier-governance milestone artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.8.0 patch written")
