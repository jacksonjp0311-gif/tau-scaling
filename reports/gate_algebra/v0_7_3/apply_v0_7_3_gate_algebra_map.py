
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
        d = ROOT / "reports" / "gate_algebra" / "v0_7_3" / "backups" / f"{p.name}_before_v0_7_3_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_gate_algebra_map.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zLCByZQpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImdhdGVfYWxnZWJyYSIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJnYXRlX2FsZ2VicmEiIC8gInYwXzdfMyIKClNPVVJDRV9ESVJTID0gWwogICAgUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjb3JlIiwKICAgIFJPT1QgLyAic3JjIiAvICJ0YXVfc2NhbGluZyIgLyAiZ2F0ZXMiLAogICAgUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJ0YXUiLAogICAgUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjbGFpbXMiLApdClNFRURfRElSID0gUk9PVCAvICJjb25maWdzIiAvICJzZWVkcyIKU0VNQU5USUNTID0gUk9PVCAvICJyZXBvcnRzIiAvICJ0YXVfdmVjdG9yX3NlbWFudGljcyIgLyAibGF0ZXN0X3RhdV92ZWN0b3Jfc2VtYW50aWNzX2xlZGdlci5qc29uIgpSRUxFQVNFID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIKCkdBVEVfRkFNSUxJRVMgPSB7CiAgICAid29ya2xvYWQiOiBbIndvcmtsb2FkIiwgInRhc2siLCAicHJvZmlsZSJdLAogICAgImJhc2VsaW5lIjogWyJiYXNlbGluZSIsICJnYWluIiwgImNhbmRpZGF0ZSJdLAogICAgImxvZ2ljZm9sZGluZyI6IFsibG9naWNmb2xkaW5nIiwgInN1cnZpdmFiaWxpdHkiLCAic3Vydml2ZSJdLAogICAgImVkZ2Vfc3VyZmFjZSI6IFsiZWRnZSIsICJzdXJmYWNlIiwgImJvdW5kYXJ5Il0sCiAgICAiZW5lcmd5X3RoZXJtYWwiOiBbImVuZXJneSIsICJ0aGVybWFsIiwgInBvd2VyIl0sCiAgICAicGRuX3B2dCI6IFsicGRuIiwgInB2dCIsICJ2b2x0YWdlIiwgInByb2Nlc3MiLCAidGVtcGVyYXR1cmUiXSwKICAgICJtb250ZV9jYXJsbyI6IFsibW9udGUiLCAiY2FybG8iLCAic3RyZXNzIiwgInByaW9yIl0sCiAgICAiZXZpZGVuY2UiOiBbImV2aWRlbmNlIiwgImZpbmRpbmciLCAicGFja2FnZSJdLAogICAgImNsYXNzaWZpZXIiOiBbInRzZWsiLCAiY2xhc3MiLCAic2NvcmUiLCAidGhyZXNob2xkIl0sCn0KCmRlZiByZWFkX3RleHQocGF0aDogUGF0aCkgLT4gc3RyOgogICAgcmV0dXJuIHBhdGgucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIsIGVycm9ycz0icmVwbGFjZSIpIGlmIHBhdGguZXhpc3RzKCkgZWxzZSAiIgoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiB7Im1pc3NpbmciOiBUcnVlLCAicGF0aCI6IHN0cihwYXRoKX0KICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHJldHVybiB7InBhcnNlX2Vycm9yIjogc3RyKGV4YyksICJwYXRoIjogc3RyKHBhdGgpfQoKZGVmIHdqc29uKHBhdGg6IFBhdGgsIGRhdGEpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMoZGF0YSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwYXRoOiBQYXRoKSAtPiBzdHI6CiAgICByZXR1cm4gc3RyKHBhdGgucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIHNvdXJjZV90ZXh0KCk6CiAgICBjaHVua3MgPSBbXQogICAgZmlsZXMgPSBbXQogICAgZm9yIGQgaW4gU09VUkNFX0RJUlM6CiAgICAgICAgaWYgZC5leGlzdHMoKToKICAgICAgICAgICAgZm9yIHAgaW4gc29ydGVkKGQucmdsb2IoIioucHkiKSk6CiAgICAgICAgICAgICAgICBjaHVua3MuYXBwZW5kKHJlYWRfdGV4dChwKSkKICAgICAgICAgICAgICAgIGZpbGVzLmFwcGVuZChyZWwocCkpCiAgICByZXR1cm4gIlxuIi5qb2luKGNodW5rcyksIGZpbGVzCgpkZWYgc2Nhbl9nYXRlX2ZhbWlsaWVzKHRleHQ6IHN0ciwgc2VlZF90ZXh0OiBzdHIpOgogICAgcm93cyA9IFtdCiAgICBmb3IgZmFtaWx5LCB0ZXJtcyBpbiBHQVRFX0ZBTUlMSUVTLml0ZW1zKCk6CiAgICAgICAgY29yZV9jb3VudCA9IHN1bShsZW4ocmUuZmluZGFsbChyZS5lc2NhcGUodCksIHRleHQsIHJlLkkpKSBmb3IgdCBpbiB0ZXJtcykKICAgICAgICBzZWVkX2NvdW50ID0gc3VtKGxlbihyZS5maW5kYWxsKHJlLmVzY2FwZSh0KSwgc2VlZF90ZXh0LCByZS5JKSkgZm9yIHQgaW4gdGVybXMpCiAgICAgICAgaWYgY29yZV9jb3VudCBhbmQgc2VlZF9jb3VudDoKICAgICAgICAgICAgc3RhdHVzID0gImNvcmVfYW5kX3NlZWRfdmlzaWJsZSIKICAgICAgICBlbGlmIGNvcmVfY291bnQ6CiAgICAgICAgICAgIHN0YXR1cyA9ICJjb3JlX3Zpc2libGVfc2VlZF9pbXBsaWNpdCIKICAgICAgICBlbGlmIHNlZWRfY291bnQ6CiAgICAgICAgICAgIHN0YXR1cyA9ICJzZWVkX3Zpc2libGVfY29yZV9pbXBsaWNpdCIKICAgICAgICBlbHNlOgogICAgICAgICAgICBzdGF0dXMgPSAibm90X3Zpc2libGUiCiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAiZ2F0ZV9mYW1pbHkiOiBmYW1pbHksCiAgICAgICAgICAgICJ0ZXJtcyI6IHRlcm1zLAogICAgICAgICAgICAiY29yZV9jb3VudCI6IGNvcmVfY291bnQsCiAgICAgICAgICAgICJzZWVkX2NvdW50Ijogc2VlZF9jb3VudCwKICAgICAgICAgICAgInZpc2liaWxpdHlfc3RhdHVzIjogc3RhdHVzLAogICAgICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgIH0pCiAgICByZXR1cm4gcm93cwoKZGVmIHNlZWRfZ2F0ZV9tYXRyaXgoKToKICAgIHJvd3MgPSBbXQogICAgZm9yIHAgaW4gc29ydGVkKFNFRURfRElSLmdsb2IoIiouanNvbiIpKToKICAgICAgICB0ZXh0ID0gcmVhZF90ZXh0KHApLmxvd2VyKCkKICAgICAgICByb3cgPSB7InBhdGgiOiByZWwocCl9CiAgICAgICAgZm9yIGZhbWlseSwgdGVybXMgaW4gR0FURV9GQU1JTElFUy5pdGVtcygpOgogICAgICAgICAgICByb3dbZmFtaWx5XSA9IGFueSh0IGluIHRleHQgZm9yIHQgaW4gdGVybXMpCiAgICAgICAgcm93WyJ2aXNpYmxlX2ZhbWlseV9jb3VudCJdID0gc3VtKDEgZm9yIGYgaW4gR0FURV9GQU1JTElFUyBpZiByb3dbZl0pCiAgICAgICAgcm93cy5hcHBlbmQocm93KQogICAgcmV0dXJuIHJvd3MKCmRlZiBjbGFzc2lmeShyb3dzLCBtYXRyaXgsIHNlbWFudGljcywgcmVsZWFzZSk6CiAgICBnYXBzID0gW10KICAgIGlmIGFueShyWyJ2aXNpYmlsaXR5X3N0YXR1cyJdID09ICJub3RfdmlzaWJsZSIgZm9yIHIgaW4gcm93cyk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInNvbWVfZ2F0ZV9mYW1pbGllc19ub3RfdmlzaWJsZV9pbl9jb3JlX29yX3NlZWRfc2NhbiIpCiAgICBpZiBhbnkoclsidmlzaWJpbGl0eV9zdGF0dXMiXSA9PSAic2VlZF92aXNpYmxlX2NvcmVfaW1wbGljaXQiIGZvciByIGluIHJvd3MpOgogICAgICAgIGdhcHMuYXBwZW5kKCJzb21lX2dhdGVfZmFtaWxpZXNfc2VlZF92aXNpYmxlX2J1dF9jb3JlX2ltcGxpY2l0IikKICAgIGlmIGFueShyWyJ2aXNpYmlsaXR5X3N0YXR1cyJdID09ICJjb3JlX3Zpc2libGVfc2VlZF9pbXBsaWNpdCIgZm9yIHIgaW4gcm93cyk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInNvbWVfZ2F0ZV9mYW1pbGllc19jb3JlX3Zpc2libGVfYnV0X3NlZWRfaW1wbGljaXQiKQogICAgaWYgbWF0cml4IGFuZCBhbnkocm93WyJ2aXNpYmxlX2ZhbWlseV9jb3VudCJdIDwgMyBmb3Igcm93IGluIG1hdHJpeCk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInNvbWVfc2VlZF9jYXJkc19oYXZlX3NwYXJzZV9nYXRlX2ZhbWlseV92aXNpYmlsaXR5IikKICAgIGlmIHNlbWFudGljcy5nZXQoInNlbWFudGljc19zdGF0dXMiKSAhPSAiVEFVX1ZFQ1RPUl9TRU1BTlRJQ1NfTEVER0VSX1JFQURZX19UQVJHRVRFRF9GSUVMRFNfSURFTlRJRklFRCI6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInRhdV92ZWN0b3Jfc2VtYW50aWNzX25vdF9pbl9leHBlY3RlZF9yZWFkeV9zdGF0ZSIpCgogICAgcmVsZWFzZV9wYXNzZWQgPSByZWxlYXNlLmdldCgicGFzc2VkIikgaXMgVHJ1ZSBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJmaW5kaW5ncyIsIFtdKSkgPT0gMCBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJzdGVwX2ZhaWx1cmVzIiwgW10pKSA9PSAwCiAgICBpZiBub3QgcmVsZWFzZV9wYXNzZWQ6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInJlbGVhc2Vfbm90X3Bhc3NpbmciKQoKICAgIHN0YXR1cyA9ICJHQVRFX0FMR0VCUkFfTUFQX1JFQURZX19UQVJHRVRFRF9HQVRFX0dBUFNfSURFTlRJRklFRCIgaWYgcmVsZWFzZV9wYXNzZWQgZWxzZSAiR0FURV9BTEdFQlJBX01BUF9ORUVEU19SRUxFQVNFX1JFVklFVyIKICAgIHJldHVybiBnYXBzLCBzdGF0dXMsIHJlbGVhc2VfcGFzc2VkCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGV4YykpCiAgICAgICAgcmV0dXJuIHBhdGhzCgogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIHJvd3MgPSBzdW1tYXJ5WyJnYXRlX2ZhbWlseV9yb3dzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTEsIDQpKQogICAgcGx0LmJhcihbclsiZ2F0ZV9mYW1pbHkiXSBmb3IgciBpbiByb3dzXSwgW3JbImNvcmVfY291bnQiXSBmb3IgciBpbiByb3dzXSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MzAsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3JlIG1lbnRpb25zIikKICAgIHBsdC50aXRsZSgiR2F0ZSBBbGdlYnJhIENvcmUgVmlzaWJpbGl0eSIpCiAgICBzYXZlKCJnYXRlX2FsZ2VicmFfY29yZV92aXNpYmlsaXR5LnBuZyIpCgogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMSwgNCkpCiAgICBwbHQuYmFyKFtyWyJnYXRlX2ZhbWlseSJdIGZvciByIGluIHJvd3NdLCBbclsic2VlZF9jb3VudCJdIGZvciByIGluIHJvd3NdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlNlZWQgbWVudGlvbnMiKQogICAgcGx0LnRpdGxlKCJHYXRlIEFsZ2VicmEgU2VlZCBWaXNpYmlsaXR5IikKICAgIHNhdmUoImdhdGVfYWxnZWJyYV9zZWVkX3Zpc2liaWxpdHkucG5nIikKCiAgICBoZWFsdGggPSB7CiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJzZW1hbnRpY3NfcmVhZHkiOiBpbnQoc3VtbWFyeVsic2VtYW50aWNzX3JlYWR5Il0pLAogICAgICAgICJnYXBfY291bnQiOiBzdW1tYXJ5WyJnYXBfY291bnQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0LnlsYWJlbCgiVmFsdWUiKQogICAgcGx0LnRpdGxlKCJHYXRlIEFsZ2VicmEgTWFwIEhlYWx0aCIpCiAgICBzYXZlKCJnYXRlX2FsZ2VicmFfaGVhbHRoLnBuZyIpCiAgICByZXR1cm4gcGF0aHMKCmRlZiBtYWtlX21kKHN1bW1hcnkpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNy4zIEdhdGUgQWxnZWJyYSBNYXAiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBNYXAgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gR2F0ZSBhbGdlYnJhIHN0YXR1czogYHtzdW1tYXJ5WydnYXRlX2FsZ2VicmFfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIFNlbWFudGljcyByZWFkeTogYHtzdW1tYXJ5WydzZW1hbnRpY3NfcmVhZHknXX1gIiwKICAgICAgICBmIi0gU291cmNlIGZpbGVzIHNjYW5uZWQ6IGB7c3VtbWFyeVsnc291cmNlX2ZpbGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gU2VlZCBjb3VudDogYHtzdW1tYXJ5WydzZWVkX2NvdW50J119YCIsCiAgICAgICAgZiItIEdhcCBjb3VudDogYHtzdW1tYXJ5WydnYXBfY291bnQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgR2F0ZSBGYW1pbHkgTWFwIiwKICAgICAgICAiIiwKICAgICAgICAifCBHYXRlIGZhbWlseSB8IENvcmUgY291bnQgfCBTZWVkIGNvdW50IHwgVmlzaWJpbGl0eSB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLTp8LS0tfCIsCiAgICBdCiAgICBmb3IgciBpbiBzdW1tYXJ5WyJnYXRlX2ZhbWlseV9yb3dzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3JbJ2dhdGVfZmFtaWx5J119YCB8IHtyWydjb3JlX2NvdW50J119IHwge3JbJ3NlZWRfY291bnQnXX0gfCBge3JbJ3Zpc2liaWxpdHlfc3RhdHVzJ119YCB8IikKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgU2VlZCBHYXRlIE1hdHJpeCIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU2VlZCB8IFZpc2libGUgZmFtaWxpZXMgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIHJvdyBpbiBzdW1tYXJ5WyJzZWVkX2dhdGVfbWF0cml4Il06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3Jvd1sncGF0aCddfWAgfCB7cm93Wyd2aXNpYmxlX2ZhbWlseV9jb3VudCddfSB8IikKICAgIGxpbmVzICs9IFsiIiwgIiMjIFRhcmdldGVkIEdhcHMiLCAiIl0KICAgIGlmIHN1bW1hcnlbImdhcHMiXToKICAgICAgICBmb3IgZ2FwIGluIHN1bW1hcnlbImdhcHMiXToKICAgICAgICAgICAgbGluZXMuYXBwZW5kKGYiLSBge2dhcH1gIikKICAgIGVsc2U6CiAgICAgICAgbGluZXMuYXBwZW5kKCItIGBub25lX2RldGVjdGVkX2luX3YwXzdfM19zY2FuYCIpCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIE5leHQgVGF1IFdvcmsiLAogICAgICAgICIiLAogICAgICAgICIxLiBCdWlsZCBhIGdhdGUtdG8tdGF1LXZlY3RvciBtYXBwaW5nIHRhYmxlLiIsCiAgICAgICAgIjIuIFNlcGFyYXRlIGV2aWRlbmNlLXJlcXVpcmVkIGdhdGVzIGZyb20gY2xhc3NpZmllci13ZWlnaHRlZCBnYXRlcy4iLAogICAgICAgICIzLiBJZGVudGlmeSBnYXRlIGZhbWlsaWVzIHRoYXQgY2FuIG92ZXItcGVuYWxpemUgaGlnaC1zdXBwb3J0IGNsYWltcy4iLAogICAgICAgICI0LiBBZGQgdGVzdHMgZm9yIGdhdGUtZmFtaWx5IGRvd25ncmFkZSBiZWhhdmlvciBiZWZvcmUgY2hhbmdpbmcgdGhyZXNob2xkcy4iLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICB0ZXh0LCBzb3VyY2VfZmlsZXMgPSBzb3VyY2VfdGV4dCgpCiAgICBzZWVkX3RleHQgPSAiXG4iLmpvaW4ocmVhZF90ZXh0KHApIGZvciBwIGluIHNvcnRlZChTRUVEX0RJUi5nbG9iKCIqLmpzb24iKSkpCiAgICBzZW1hbnRpY3MgPSByZWFkX2pzb24oU0VNQU5USUNTKQogICAgcmVsZWFzZSA9IHJlYWRfanNvbihSRUxFQVNFKQoKICAgIGdhdGVfcm93cyA9IHNjYW5fZ2F0ZV9mYW1pbGllcyh0ZXh0LCBzZWVkX3RleHQpCiAgICBtYXRyaXggPSBzZWVkX2dhdGVfbWF0cml4KCkKICAgIGdhcHMsIHN0YXR1cywgcmVsZWFzZV9wYXNzZWQgPSBjbGFzc2lmeShnYXRlX3Jvd3MsIG1hdHJpeCwgc2VtYW50aWNzLCByZWxlYXNlKQogICAgc2VtYW50aWNzX3JlYWR5ID0gc2VtYW50aWNzLmdldCgic2VtYW50aWNzX3N0YXR1cyIpID09ICJUQVVfVkVDVE9SX1NFTUFOVElDU19MRURHRVJfUkVBRFlfX1RBUkdFVEVEX0ZJRUxEU19JREVOVElGSUVEIgoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1nYXRlLWFsZ2VicmEtbWFwLXYwLjcuMyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJnYXRlX2FsZ2VicmFfc3RhdHVzIjogc3RhdHVzLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IGJvb2wocmVsZWFzZV9wYXNzZWQpLAogICAgICAgICJzZW1hbnRpY3NfcmVhZHkiOiBib29sKHNlbWFudGljc19yZWFkeSksCiAgICAgICAgInNvdXJjZV9maWxlcyI6IHNvdXJjZV9maWxlcywKICAgICAgICAic291cmNlX2ZpbGVfY291bnQiOiBsZW4oc291cmNlX2ZpbGVzKSwKICAgICAgICAic2VlZF9jb3VudCI6IGxlbihtYXRyaXgpLAogICAgICAgICJnYXRlX2ZhbWlseV9yb3dzIjogZ2F0ZV9yb3dzLAogICAgICAgICJzZWVkX2dhdGVfbWF0cml4IjogbWF0cml4LAogICAgICAgICJnYXBzIjogZ2FwcywKICAgICAgICAiZ2FwX2NvdW50IjogbGVuKGdhcHMpLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogIk1vdmUgdG8gdjAuNy40IFRTRUsgVGhyZXNob2xkIEJvdW5kYXJ5IFJldmlldyBhZnRlciBnYXRlLWZhbWlseSB2aXNpYmlsaXR5IGlzIG1hcHBlZC4iLAogICAgICAgICJib3VuZGFyeSI6ICJHYXRlIGFsZ2VicmEgbWFwcyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGFuYWx5c2lzIGFydGlmYWN0cy4gVGhleSBtYXAgZ2F0ZSB2aXNpYmlsaXR5IGFuZCBldmlkZW5jZSBzdXJmYWNlcy4gVGhleSBkbyBub3QgY3JlYXRlIGxpdmUgYXBwcm92YWwsIGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzLCBjcmVhdGUgYnJhbmNoZXMsIG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhcHBseSBjYWxpYnJhdGlvbiwgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJnYXRlX2FsZ2VicmFfbWFwX3YwXzdfMy5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJnYXRlX2FsZ2VicmFfbWFwX3YwXzdfMy5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2dhdGVfYWxnZWJyYV9tYXAubWQiLCBtYWtlX21kKHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiZ2F0ZV9hbGdlYnJhX3N0YXR1cyI6IHN1bW1hcnlbImdhdGVfYWxnZWJyYV9zdGF0dXMiXSwKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBzdW1tYXJ5WyJyZWxlYXNlX3Bhc3NlZCJdLAogICAgICAgICJzZW1hbnRpY3NfcmVhZHkiOiBzdW1tYXJ5WyJzZW1hbnRpY3NfcmVhZHkiXSwKICAgICAgICAic291cmNlX2ZpbGVfY291bnQiOiBzdW1tYXJ5WyJzb3VyY2VfZmlsZV9jb3VudCJdLAogICAgICAgICJzZWVkX2NvdW50Ijogc3VtbWFyeVsic2VlZF9jb3VudCJdLAogICAgICAgICJnYXBfY291bnQiOiBzdW1tYXJ5WyJnYXBfY291bnQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL2dhdGVfYWxnZWJyYS9sYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT / "reports" / "gate_algebra" / "README.md", """# Gate Algebra Reports

Current layer: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**

## Purpose

This folder stores gate algebra maps that connect tau-vector semantics to gate-family visibility and classifier boundaries.

## Primary command

```powershell
python scripts/benchmarks/generate_gate_algebra_map.py
```

## README Update Rule

Update this mini README whenever gate families, classifier thresholds, or gate-to-evidence mappings change.

Boundary: gate algebra reports are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "gate_algebra" / "README.md", """# Gate Algebra Visuals

Current layer: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**

## Purpose

This folder stores charts summarizing gate-family visibility across source and seed cards.

## README Update Rule

Update this mini README whenever gate algebra chart names or meanings change.

Boundary: gate algebra visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "gate_algebra" / "v0_7_3" / "README.md", """# v0.7.3 Gate Algebra Charts

Expected charts:

- `gate_algebra_core_visibility.png`
- `gate_algebra_seed_visibility.png`
- `gate_algebra_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local gate-algebra diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.2[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.1[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.2 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.3 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.2-ready |", "| Task routing matrix | geometry-aware / v0.7.3-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.2 |", "| Agent contract version sync | current / v0.7.3 |")

if "| Gate algebra map |" not in r:
    r = r.replace("| Tau vector semantics charts | `visuals/tau_vector_semantics/v0_7_2/` |\n",
                  "| Tau vector semantics charts | `visuals/tau_vector_semantics/v0_7_2/` |\n| Gate algebra map | `reports/gate_algebra/latest_gate_algebra_map.md` |\n| Gate algebra charts | `visuals/gate_algebra/v0_7_3/` |\n")

if "python scripts/benchmarks/generate_gate_algebra_map.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython scripts/benchmarks/generate_gate_algebra_map.py\npython scripts/release/validate_release.py")

if "    gate_algebra/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    gate_algebra/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    gate_algebra/\n")

section = """## Gate Algebra Map v0.7.3

v0.7.3 maps gate-family visibility across core source and seed claim cards before any threshold changes.

Primary command:

```powershell
python scripts/benchmarks/generate_gate_algebra_map.py
```

Primary outputs:

```text
reports/gate_algebra/latest_gate_algebra_map.json
reports/gate_algebra/latest_gate_algebra_map.md
visuals/gate_algebra/v0_7_3/
```

Current lock:

```text
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: gate algebra maps are local classifier-governance analysis artifacts. They map gate visibility and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Gate Algebra Map v0.7.3" not in r:
    r = r.replace("## Tau Vector Semantics Ledger v0.7.2", section + "## Tau Vector Semantics Ledger v0.7.2", 1)

lesson = "| L-055 | v0.7.2 named tau-vector semantic gaps without changing scoring. | Tau semantics alone are not enough; the next layer must map which gates consume or expose those semantics. | Gate algebra must be mapped before TSEK thresholds or policy penalties are tightened. |"
if "L-055" not in r:
    r = r.replace("| L-054 | v0.7.1 identified targeted Tau-mechanics gaps after the approval corridor was sealed. | The next repair should not mutate scoring; it should name and audit tau-vector semantics first. | Tau vector fields must be made explicit before gate algebra or TSEK thresholds are tightened. |\n",
                  "| L-054 | v0.7.1 identified targeted Tau-mechanics gaps after the approval corridor was sealed. | The next repair should not mutate scoring; it should name and audit tau-vector semantics first. | Tau vector fields must be made explicit before gate algebra or TSEK thresholds are tightened. |\n" + lesson + "\n")

if "| v0.7.3 |" not in r:
    r = r.replace("| v0.7.2 | Tau vector semantics ledger; maps tau terms, seed coverage, and evidence surface gaps. |\n",
                  "| v0.7.2 | Tau vector semantics ledger; maps tau terms, seed coverage, and evidence surface gaps. |\n| v0.7.3 | Gate algebra map; maps gate-family visibility before threshold changes. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**

Recommended goals:

- Review TSEK threshold boundaries without changing them.
- Separate downgrade policy from evidence sufficiency.
- Identify over-penalty and under-penalty risk surfaces.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_gate_algebra_map.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython scripts/benchmarks/generate_gate_algebra_map.py\npython -m unittest discover -s tests")
        s = s.replace("| Tau vector semantics patch | `reports/tau_vector_semantics/`, `visuals/tau_vector_semantics/`, seeds/runtime | semantics ledger + release validator; no mutation |\n",
                      "| Tau vector semantics patch | `reports/tau_vector_semantics/`, `visuals/tau_vector_semantics/`, seeds/runtime | semantics ledger + release validator; no mutation |\n| Gate algebra patch | `reports/gate_algebra/`, `visuals/gate_algebra/`, core gates/seeds | gate map + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Gate algebra patch |" not in s:
        s = s.replace("| Tau vector semantics patch | inner | analysis | runtime | core runtime + seeds | semantics ledger + charts + release validator | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` |\n",
                      "| Tau vector semantics patch | inner | analysis | runtime | core runtime + seeds | semantics ledger + charts + release validator | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` |\n| Gate algebra patch | inner | analysis | runtime | core gates + seeds + tau semantics | gate algebra map + charts + release validator | `reports/gate_algebra/latest_gate_algebra_map.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.3"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["gate_algebra_map"] = {
    "read_first": ["src/tau_scaling/gates/", "src/tau_scaling/core/", "configs/seeds/", "reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.json"],
    "validate": ["python scripts/benchmarks/generate_gate_algebra_map.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/gate_algebra/latest_gate_algebra_map.md", "visuals/gate_algebra/v0_7_3/"],
    "mutation_lock": "Gate map only; no replay execution, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.3 | Gate algebra map |" not in t:
    t = t.replace("| v0.7.2 | Tau vector semantics ledger | `python scripts/benchmarks/generate_tau_vector_semantics_ledger.py` | Maps tau terms, seed coverage, and semantic gaps before gate algebra changes | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` | `visuals/tau_vector_semantics/v0_7_2/` |\n",
                  "| v0.7.2 | Tau vector semantics ledger | `python scripts/benchmarks/generate_tau_vector_semantics_ledger.py` | Maps tau terms, seed coverage, and semantic gaps before gate algebra changes | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` | `visuals/tau_vector_semantics/v0_7_2/` |\n| v0.7.3 | Gate algebra map | `python scripts/benchmarks/generate_gate_algebra_map.py` | Maps gate-family visibility before TSEK threshold changes | `reports/gate_algebra/latest_gate_algebra_map.md` | `visuals/gate_algebra/v0_7_3/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_3_gate_algebra_map.md", f"""# TAU-SCALING-SA v0.7.3 - Gate Algebra Map

Generated: {NOW}

## Purpose

Map gate-family visibility across core source and seed claim cards before any threshold changes.

## Boundary

Gate algebra maps are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.3 patch written")
