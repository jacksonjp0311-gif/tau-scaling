
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
        d = ROOT / "reports" / "tau_mechanics_review" / "v0_7_1" / "backups" / f"{p.name}_before_v0_7_1_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "run_tau_mechanics_return_review.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zLCByZQpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRhdV9tZWNoYW5pY3NfcmV2aWV3IgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gInRhdV9tZWNoYW5pY3NfcmV2aWV3IiAvICJ2MF83XzEiCgpQQVRIUyA9IHsKICAgICJydW50aW1lIjogUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjb3JlIiAvICJydW50aW1lLnB5IiwKICAgICJjbGFzc2lmaWVyIjogUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjb3JlIiAvICJjbGFzc2lmaWVyLnB5IiwKICAgICJtb2RlbHMiOiBST09UIC8gInNyYyIgLyAidGF1X3NjYWxpbmciIC8gImNvcmUiIC8gIm1vZGVscy5weSIsCiAgICAicmVsZWFzZSI6IFJPT1QgLyAicmVwb3J0cyIgLyAicmVsZWFzZSIgLyAibGF0ZXN0X3JlbGVhc2VfcmVhZGluZXNzLmpzb24iLAogICAgInN5bnRoZXRpY19nYXRlIjogUk9PVCAvICJyZXBvcnRzIiAvICJnYXRlcyIgLyAibGF0ZXN0X3N5bnRoZXRpY19nYXRlX3JlcG9ydC5qc29uIiwKICAgICJzZW5zaXRpdml0eSI6IFJPT1QgLyAicmVwb3J0cyIgLyAic2Vuc2l0aXZpdHkiIC8gImxhdGVzdF9zZW5zaXRpdml0eV9zd2VlcC5qc29uIiwKICAgICJpbnRlcmFjdGlvbnMiOiBST09UIC8gInJlcG9ydHMiIC8gImludGVyYWN0aW9ucyIgLyAibGF0ZXN0X2dhdGVfaW50ZXJhY3Rpb25fbWF0cml4Lmpzb24iLAogICAgImJlbmNobWFyayI6IFJPT1QgLyAicmVwb3J0cyIgLyAiYmVuY2htYXJrcyIgLyAibGF0ZXN0X2JlbmNobWFya19zdW1tYXJ5Lmpzb24iLAogICAgImFwcHJvdmFsX2NvcnJpZG9yIjogUk9PVCAvICJyZXBvcnRzIiAvICJhcHByb3ZhbF9jb3JyaWRvciIgLyAibGF0ZXN0X2FwcHJvdmFsX2dvdmVybmFuY2VfY29ycmlkb3JfbWlsZXN0b25lLmpzb24iLAp9CgpTRUVEX0RJUiA9IFJPT1QgLyAiY29uZmlncyIgLyAic2VlZHMiCgpkZWYgcmVhZF90ZXh0KHBhdGg6IFBhdGgpIC0+IHN0cjoKICAgIHJldHVybiBwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiLCBlcnJvcnM9InJlcGxhY2UiKSBpZiBwYXRoLmV4aXN0cygpIGVsc2UgIiIKCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCk6CiAgICBpZiBub3QgcGF0aC5leGlzdHMoKToKICAgICAgICByZXR1cm4geyJtaXNzaW5nIjogVHJ1ZSwgInBhdGgiOiBzdHIocGF0aCl9CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJwYXJzZV9lcnJvciI6IHN0cihleGMpLCAicGF0aCI6IHN0cihwYXRoKX0KCmRlZiB3anNvbihwYXRoOiBQYXRoLCBkYXRhKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKGRhdGEsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cik6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocGF0aDogUGF0aCkgLT4gc3RyOgogICAgcmV0dXJuIHN0cihwYXRoLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBleHRyYWN0X2NvZGVfc2lnbmFscygpOgogICAgdGV4dCA9ICJcbiIuam9pbihyZWFkX3RleHQocCkgZm9yIHAgaW4gW1BBVEhTWyJydW50aW1lIl0sIFBBVEhTWyJjbGFzc2lmaWVyIl0sIFBBVEhTWyJtb2RlbHMiXV0pCiAgICB0b2tlbnMgPSB7CiAgICAgICAgInRhdV9tZW50aW9ucyI6IGxlbihyZS5maW5kYWxsKHIiXGJ0YXVcYnx0YXVfIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJnYXRlX21lbnRpb25zIjogbGVuKHJlLmZpbmRhbGwociJcYmdhdGVcYnxnYXRlc3x0aHJlc2hvbGQiLCB0ZXh0LCByZS5JKSksCiAgICAgICAgInRzZWtfbWVudGlvbnMiOiBsZW4ocmUuZmluZGFsbChyIlRTRUsiLCB0ZXh0KSksCiAgICAgICAgImV2aWRlbmNlX21lbnRpb25zIjogbGVuKHJlLmZpbmRhbGwociJldmlkZW5jZSIsIHRleHQsIHJlLkkpKSwKICAgICAgICAiYmFzZWxpbmVfbWVudGlvbnMiOiBsZW4ocmUuZmluZGFsbChyImJhc2VsaW5lIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJ3b3JrbG9hZF9tZW50aW9ucyI6IGxlbihyZS5maW5kYWxsKHIid29ya2xvYWQiLCB0ZXh0LCByZS5JKSksCiAgICB9CiAgICBmdW5jdGlvbnMgPSBzb3J0ZWQoc2V0KHJlLmZpbmRhbGwociJkZWZccysoW0EtWmEtel9dW0EtWmEtejAtOV9dKilccypcKCIsIHRleHQpKSkKICAgIGNsYXNzZXMgPSBzb3J0ZWQoc2V0KHJlLmZpbmRhbGwociJjbGFzc1xzKyhbQS1aYS16X11bQS1aYS16MC05X10qKVxzKls6KF0iLCB0ZXh0KSkpCiAgICByZXR1cm4geyJ0b2tlbl9jb3VudHMiOiB0b2tlbnMsICJmdW5jdGlvbl9jb3VudCI6IGxlbihmdW5jdGlvbnMpLCAiY2xhc3NfY291bnQiOiBsZW4oY2xhc3NlcyksICJmdW5jdGlvbnMiOiBmdW5jdGlvbnNbOjgwXSwgImNsYXNzZXMiOiBjbGFzc2VzWzo4MF19CgpkZWYgY29sbGVjdF9zZWVkX2NhcmRzKCk6CiAgICBjYXJkcyA9IFtdCiAgICBmb3IgcCBpbiBzb3J0ZWQoU0VFRF9ESVIuZ2xvYigiKi5qc29uIikpOgogICAgICAgIGRhdGEgPSByZWFkX2pzb24ocCkKICAgICAgICB0ZXh0ID0ganNvbi5kdW1wcyhkYXRhKS5sb3dlcigpCiAgICAgICAgY2FyZHMuYXBwZW5kKHsKICAgICAgICAgICAgInBhdGgiOiByZWwocCksCiAgICAgICAgICAgICJoYXNfd29ya2xvYWQiOiAid29ya2xvYWQiIGluIHRleHQsCiAgICAgICAgICAgICJoYXNfYmFzZWxpbmUiOiAiYmFzZWxpbmUiIGluIHRleHQsCiAgICAgICAgICAgICJoYXNfY2FuZGlkYXRlIjogImNhbmRpZGF0ZSIgaW4gdGV4dCwKICAgICAgICAgICAgImhhc190YXUiOiAidGF1IiBpbiB0ZXh0LAogICAgICAgICAgICAiaGFzX2dhdGUiOiAiZ2F0ZSIgaW4gdGV4dCBvciAidGhlcm1hbCIgaW4gdGV4dCBvciAicGRuIiBpbiB0ZXh0IG9yICJwdnQiIGluIHRleHQsCiAgICAgICAgICAgICJrZXlzIjogc29ydGVkKGxpc3QoZGF0YS5rZXlzKCkpKSBpZiBpc2luc3RhbmNlKGRhdGEsIGRpY3QpIGVsc2UgW10sCiAgICAgICAgfSkKICAgIHJldHVybiBjYXJkcwoKZGVmIGNsYXNzaWZ5X21lY2hhbmljcyhjb2RlLCBjYXJkcywgcmVwb3J0cyk6CiAgICBjb3ZlcmFnZSA9IHsKICAgICAgICAic2VlZF9jb3VudCI6IGxlbihjYXJkcyksCiAgICAgICAgInNlZWRzX3dpdGhfd29ya2xvYWQiOiBzdW0oY1siaGFzX3dvcmtsb2FkIl0gZm9yIGMgaW4gY2FyZHMpLAogICAgICAgICJzZWVkc193aXRoX2Jhc2VsaW5lIjogc3VtKGNbImhhc19iYXNlbGluZSJdIGZvciBjIGluIGNhcmRzKSwKICAgICAgICAic2VlZHNfd2l0aF9jYW5kaWRhdGUiOiBzdW0oY1siaGFzX2NhbmRpZGF0ZSJdIGZvciBjIGluIGNhcmRzKSwKICAgICAgICAic2VlZHNfd2l0aF90YXUiOiBzdW0oY1siaGFzX3RhdSJdIGZvciBjIGluIGNhcmRzKSwKICAgICAgICAic2VlZHNfd2l0aF9nYXRlIjogc3VtKGNbImhhc19nYXRlIl0gZm9yIGMgaW4gY2FyZHMpLAogICAgfQogICAgcmVsZWFzZSA9IHJlcG9ydHNbInJlbGVhc2UiXQogICAgYXBwcm92YWwgPSByZXBvcnRzWyJhcHByb3ZhbF9jb3JyaWRvciJdCiAgICByZWxlYXNlX3Bhc3NlZCA9IHJlbGVhc2UuZ2V0KCJwYXNzZWQiKSBpcyBUcnVlIGFuZCBsZW4ocmVsZWFzZS5nZXQoImZpbmRpbmdzIiwgW10pKSA9PSAwIGFuZCBsZW4ocmVsZWFzZS5nZXQoInN0ZXBfZmFpbHVyZXMiLCBbXSkpID09IDAKICAgIGNvcnJpZG9yX2xvY2tlZCA9IGFwcHJvdmFsLmdldCgiY29ycmlkb3JfbG9ja2VkIikgaXMgVHJ1ZQoKICAgIGdhcHMgPSBbXQogICAgaWYgY292ZXJhZ2VbInNlZWRfY291bnQiXSA9PSAwOgogICAgICAgIGdhcHMuYXBwZW5kKCJub19zZWVkX2NhcmRzX2ZvdW5kIikKICAgIGlmIGNvdmVyYWdlWyJzZWVkc193aXRoX3RhdSJdIDwgY292ZXJhZ2VbInNlZWRfY291bnQiXToKICAgICAgICBnYXBzLmFwcGVuZCgic29tZV9zZWVkX2NhcmRzX2RvX25vdF9zdXJmYWNlX3RhdV90ZXJtcyIpCiAgICBpZiBjb3ZlcmFnZVsic2VlZHNfd2l0aF9nYXRlIl0gPCBjb3ZlcmFnZVsic2VlZF9jb3VudCJdOgogICAgICAgIGdhcHMuYXBwZW5kKCJzb21lX3NlZWRfY2FyZHNfZG9fbm90X3N1cmZhY2VfZ2F0ZV90ZXJtcyIpCiAgICBpZiBjb2RlWyJ0b2tlbl9jb3VudHMiXVsidHNla19tZW50aW9ucyJdID09IDA6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInRzZWtfbm90X3Zpc2libGVfaW5fY29yZV9jb2RlX3NjYW4iKQogICAgaWYgbm90IHJlbGVhc2VfcGFzc2VkOgogICAgICAgIGdhcHMuYXBwZW5kKCJyZWxlYXNlX25vdF9wYXNzaW5nIikKICAgIGlmIG5vdCBjb3JyaWRvcl9sb2NrZWQ6CiAgICAgICAgZ2Fwcy5hcHBlbmQoImFwcHJvdmFsX2NvcnJpZG9yX25vdF9sb2NrZWQiKQoKICAgIGlmIG5vdCBnYXBzOgogICAgICAgIHN0YXR1cyA9ICJUQVVfTUVDSEFOSUNTX1JFVklFV19SRUFEWV9fUkVUVVJOX1RPX0NPUkVfRU5HSU5FIgogICAgZWxzZToKICAgICAgICBzdGF0dXMgPSAiVEFVX01FQ0hBTklDU19SRVZJRVdfUkVBRFlfX1RBUkdFVEVEX0dBUFNfSURFTlRJRklFRCIKCiAgICByZXR1cm4gY292ZXJhZ2UsIGdhcHMsIHN0YXR1cywgcmVsZWFzZV9wYXNzZWQsIGNvcnJpZG9yX2xvY2tlZAoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihleGMpKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcGF0aCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwYXRoLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwYXRoKSkKCiAgICBjb3VudHMgPSBzdW1tYXJ5WyJjb2RlX3NpZ25hbHMiXVsidG9rZW5fY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKQogICAgcGx0LmJhcihsaXN0KGNvdW50cy5rZXlzKCkpLCBsaXN0KGNvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJUYXUgTWVjaGFuaWNzIENvZGUgU2lnbmFsIFNjYW4iKQogICAgc2F2ZSgidGF1X21lY2hhbmljc19jb2RlX3NpZ25hbHMucG5nIikKCiAgICBjb3YgPSBzdW1tYXJ5WyJzZWVkX2NvdmVyYWdlIl0KICAgIG9yZGVyZWQgPSBbInNlZWRfY291bnQiLCAic2VlZHNfd2l0aF93b3JrbG9hZCIsICJzZWVkc193aXRoX2Jhc2VsaW5lIiwgInNlZWRzX3dpdGhfY2FuZGlkYXRlIiwgInNlZWRzX3dpdGhfdGF1IiwgInNlZWRzX3dpdGhfZ2F0ZSJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIob3JkZXJlZCwgW2NvdltrXSBmb3IgayBpbiBvcmRlcmVkXSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBwbHQudGl0bGUoIlRhdSBNZWNoYW5pY3MgU2VlZCBDb3ZlcmFnZSIpCiAgICBzYXZlKCJ0YXVfbWVjaGFuaWNzX3NlZWRfY292ZXJhZ2UucG5nIikKCiAgICBoZWFsdGggPSB7CiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJjb3JyaWRvcl9sb2NrZWQiOiBpbnQoc3VtbWFyeVsiYXBwcm92YWxfY29ycmlkb3JfbG9ja2VkIl0pLAogICAgICAgICJtZWNoYW5pY3NfZ2FwcyI6IHN1bW1hcnlbImdhcF9jb3VudCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGhlYWx0aC5rZXlzKCkpLCBsaXN0KGhlYWx0aC52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiVmFsdWUiKQogICAgcGx0LnRpdGxlKCJUYXUgTWVjaGFuaWNzIFJldHVybiBIZWFsdGgiKQogICAgc2F2ZSgidGF1X21lY2hhbmljc19yZXR1cm5faGVhbHRoLnBuZyIpCiAgICByZXR1cm4gcGF0aHMKCmRlZiBtYWtlX21kKHN1bW1hcnkpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNy4xIFRhdSBNZWNoYW5pY3MgUmV0dXJuIFJldmlldyIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJldmlldyBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBNZWNoYW5pY3Mgc3RhdHVzOiBge3N1bW1hcnlbJ21lY2hhbmljc19zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gUmVsZWFzZSBwYXNzZWQ6IGB7c3VtbWFyeVsncmVsZWFzZV9wYXNzZWQnXX1gIiwKICAgICAgICBmIi0gQXBwcm92YWwgY29ycmlkb3IgbG9ja2VkOiBge3N1bW1hcnlbJ2FwcHJvdmFsX2NvcnJpZG9yX2xvY2tlZCddfWAiLAogICAgICAgIGYiLSBTZWVkIGNvdW50OiBge3N1bW1hcnlbJ3NlZWRfY292ZXJhZ2UnXVsnc2VlZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBHYXAgY291bnQ6IGB7c3VtbWFyeVsnZ2FwX2NvdW50J119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c3VtbWFyeVsnbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDb3JlIENvZGUgU2lnbmFscyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU2lnbmFsIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc3VtbWFyeVsiY29kZV9zaWduYWxzIl1bInRva2VuX2NvdW50cyJdLml0ZW1zKCk6CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge2t9YCB8IHt2fSB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFNlZWQgQ292ZXJhZ2UiLAogICAgICAgICIiLAogICAgICAgICJ8IFNlZWQgfCBXb3JrbG9hZCB8IEJhc2VsaW5lIHwgQ2FuZGlkYXRlIHwgVGF1IHwgR2F0ZSB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLTp8LS0tOnwtLS06fC0tLTp8IiwKICAgIF0KICAgIGZvciBjYXJkIGluIHN1bW1hcnlbInNlZWRfY2FyZHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7Y2FyZFsncGF0aCddfWAgfCBge2NhcmRbJ2hhc193b3JrbG9hZCddfWAgfCBge2NhcmRbJ2hhc19iYXNlbGluZSddfWAgfCBge2NhcmRbJ2hhc19jYW5kaWRhdGUnXX1gIHwgYHtjYXJkWydoYXNfdGF1J119YCB8IGB7Y2FyZFsnaGFzX2dhdGUnXX1gIHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIFRhcmdldGVkIEdhcHMiLCAiIl0KICAgIGlmIHN1bW1hcnlbImdhcHMiXToKICAgICAgICBmb3IgZ2FwIGluIHN1bW1hcnlbImdhcHMiXToKICAgICAgICAgICAgbGluZXMuYXBwZW5kKGYiLSBge2dhcH1gIikKICAgIGVsc2U6CiAgICAgICAgbGluZXMuYXBwZW5kKCItIGBub25lX2RldGVjdGVkX2luX3YwXzdfMV9zY2FuYCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBOZXh0IFRhdSBXb3JrIiwKICAgICAgICAiIiwKICAgICAgICAiMS4gRGVmaW5lIHRoZSB0YXUtdmVjdG9yIGZpZWxkIG5hbWVzIGFuZCB1bml0cyBtb3JlIGV4cGxpY2l0bHkuIiwKICAgICAgICAiMi4gU2VwYXJhdGUgZ2F0ZSBhbGdlYnJhIGZyb20gY2xhc3NpZmllciBzY29yaW5nIGluIGRvY3VtZW50YXRpb24gYW5kIHRlc3RzLiIsCiAgICAgICAgIjMuIFJldmlldyBUU0VLIHRocmVzaG9sZCBkZWZpbml0aW9ucyBhbmQgZG93bmdyYWRlL3Byb21vdGlvbiBib3VuZGFyaWVzLiIsCiAgICAgICAgIjQuIENvbm5lY3Qgc3ludGhldGljIGdhdGUgc3VpdGUgb3V0cHV0cyBiYWNrIHRvIGNsYWltLWNhcmQgZXZpZGVuY2UgcmVxdWlyZW1lbnRzLiIsCiAgICAgICAgIjUuIEFkZCBuZWdhdGl2ZSBjb250cm9scyBmb3IgdGF1LXZlY3RvciBvdmVyZml0dGluZyBhbmQgZ2F0ZSBvdmVyLXBlbmFsdHkuIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWwogICAgICAgICIjIyBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc3VtbWFyeVsiYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgIF0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgcmVwb3J0cyA9IHtrOiByZWFkX2pzb24odikgZm9yIGssIHYgaW4gUEFUSFMuaXRlbXMoKSBpZiBrIG5vdCBpbiB7InJ1bnRpbWUiLCAiY2xhc3NpZmllciIsICJtb2RlbHMifX0KICAgIGNvZGUgPSBleHRyYWN0X2NvZGVfc2lnbmFscygpCiAgICBjYXJkcyA9IGNvbGxlY3Rfc2VlZF9jYXJkcygpCiAgICBjb3ZlcmFnZSwgZ2Fwcywgc3RhdHVzLCByZWxlYXNlX3Bhc3NlZCwgY29ycmlkb3JfbG9ja2VkID0gY2xhc3NpZnlfbWVjaGFuaWNzKGNvZGUsIGNhcmRzLCByZXBvcnRzKQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy10YXUtbWVjaGFuaWNzLXJldHVybi1yZXZpZXctdjAuNy4xIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgIm1lY2hhbmljc19zdGF0dXMiOiBzdGF0dXMsCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogYm9vbChyZWxlYXNlX3Bhc3NlZCksCiAgICAgICAgImFwcHJvdmFsX2NvcnJpZG9yX2xvY2tlZCI6IGJvb2woY29ycmlkb3JfbG9ja2VkKSwKICAgICAgICAiY29kZV9zaWduYWxzIjogY29kZSwKICAgICAgICAic2VlZF9jb3ZlcmFnZSI6IGNvdmVyYWdlLAogICAgICAgICJzZWVkX2NhcmRzIjogY2FyZHMsCiAgICAgICAgImdhcHMiOiBnYXBzLAogICAgICAgICJnYXBfY291bnQiOiBsZW4oZ2FwcyksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9iZWhhdmlvcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAiTW92ZSBmcm9tIGdvdmVybmFuY2UgY29udGFpbm1lbnQgaW50byBUYXUgbWVjaGFuaWNzOiB0YXUgdmVjdG9ycywgZ2F0ZSBhbGdlYnJhLCBUU0VLIHRocmVzaG9sZHMsIHN5bnRoZXRpYyBnYXRlIHN1aXRlIGludGVycHJldGF0aW9uLCBhbmQgZXZpZGVuY2UtY2FyZCBkZXNpZ24uIiwKICAgICAgICAiYm91bmRhcnkiOiAiVGF1IG1lY2hhbmljcyByZXR1cm4gcmV2aWV3cyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGFuYWx5c2lzIGFydGlmYWN0cy4gVGhleSBpbnNwZWN0IHJ1bnRpbWUgbWVjaGFuaWNzIGFuZCBldmlkZW5jZSBzdXJmYWNlcy4gVGhleSBkbyBub3QgY3JlYXRlIGxpdmUgYXBwcm92YWwsIGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzLCBjcmVhdGUgYnJhbmNoZXMsIG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhcHBseSBjYWxpYnJhdGlvbiwgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJ0YXVfbWVjaGFuaWNzX3JldHVybl9yZXZpZXdfdjBfN18xLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF90YXVfbWVjaGFuaWNzX3JldHVybl9yZXZpZXcuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAidGF1X21lY2hhbmljc19yZXR1cm5fcmV2aWV3X3YwXzdfMS5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3RhdV9tZWNoYW5pY3NfcmV0dXJuX3Jldmlldy5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJtZWNoYW5pY3Nfc3RhdHVzIjogc3VtbWFyeVsibWVjaGFuaWNzX3N0YXR1cyJdLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0sCiAgICAgICAgImFwcHJvdmFsX2NvcnJpZG9yX2xvY2tlZCI6IHN1bW1hcnlbImFwcHJvdmFsX2NvcnJpZG9yX2xvY2tlZCJdLAogICAgICAgICJzZWVkX2NvdW50Ijogc3VtbWFyeVsic2VlZF9jb3ZlcmFnZSJdWyJzZWVkX2NvdW50Il0sCiAgICAgICAgImdhcF9jb3VudCI6IHN1bW1hcnlbImdhcF9jb3VudCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvdGF1X21lY2hhbmljc19yZXZpZXcvbGF0ZXN0X3RhdV9tZWNoYW5pY3NfcmV0dXJuX3Jldmlldy5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT / "reports" / "tau_mechanics_review" / "README.md", """# Tau Mechanics Return Review Reports

Current layer: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**

## Purpose

This folder stores reviews of the core Tau mechanics after approval-governance corridor consolidation.

## Primary command

```powershell
python scripts/benchmarks/run_tau_mechanics_return_review.py
```

## README Update Rule

Update this mini README whenever tau-vector semantics, gate algebra, classifier thresholds, or evidence-card review rules change.

Boundary: tau mechanics reviews are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "tau_mechanics_review" / "README.md", """# Tau Mechanics Return Review Visuals

Current layer: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**

## Purpose

This folder stores charts summarizing tau mechanics review signals.

## README Update Rule

Update this mini README whenever tau mechanics chart names or meanings change.

Boundary: tau-mechanics visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "tau_mechanics_review" / "v0_7_1" / "README.md", """# v0.7.1 Tau Mechanics Review Charts

Expected charts:

- `tau_mechanics_code_signals.png`
- `tau_mechanics_seed_coverage.png`
- `tau_mechanics_return_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local tau-mechanics diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.0[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.9[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.0 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.1 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.0-ready |", "| Task routing matrix | geometry-aware / v0.7.1-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.0 |", "| Agent contract version sync | current / v0.7.1 |")

if "| Tau mechanics return review |" not in r:
    r = r.replace("| Approval corridor charts | `visuals/approval_corridor/v0_7_0/` |\n",
                  "| Approval corridor charts | `visuals/approval_corridor/v0_7_0/` |\n| Tau mechanics return review | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` |\n| Tau mechanics charts | `visuals/tau_mechanics_review/v0_7_1/` |\n")

if "python scripts/benchmarks/run_tau_mechanics_return_review.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_approval_governance_corridor.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_approval_governance_corridor.py\npython scripts/benchmarks/run_tau_mechanics_return_review.py\npython scripts/release/validate_release.py")

if "    tau_mechanics_review/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    tau_mechanics_review/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    tau_mechanics_review/\n")

section = """## Tau Mechanics Return Review v0.7.1

v0.7.1 returns attention from approval-governance containment to the core Tau mechanics.

Primary command:

```powershell
python scripts/benchmarks/run_tau_mechanics_return_review.py
```

Primary outputs:

```text
reports/tau_mechanics_review/latest_tau_mechanics_return_review.json
reports/tau_mechanics_review/latest_tau_mechanics_return_review.md
visuals/tau_mechanics_review/v0_7_1/
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

Boundary: tau mechanics reviews are local classifier-governance analysis artifacts. They inspect runtime mechanics and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Tau Mechanics Return Review v0.7.1" not in r:
    r = r.replace("## Approval-Governance Corridor Milestone v0.7.0", section + "## Approval-Governance Corridor Milestone v0.7.0", 1)

lesson = "| L-053 | v0.7.0 sealed the approval-governance corridor. | Once containment is sealed, further progress must return to the object being governed. | Tau mechanics reviews should examine tau vectors, gate algebra, TSEK thresholds, sensitivity behavior, and evidence-card design before adding any new governance gate. |"
if "L-053" not in r:
    r = r.replace("| L-052 | v0.6.9 confirmed the governance block was still valid. | Continuing to add gates after a valid trend review risks ceremonial accumulation. | A completed approval-governance corridor should be packaged as a milestone before returning to core Tau mechanics. |\n",
                  "| L-052 | v0.6.9 confirmed the governance block was still valid. | Continuing to add gates after a valid trend review risks ceremonial accumulation. | A completed approval-governance corridor should be packaged as a milestone before returning to core Tau mechanics. |\n" + lesson + "\n")

if "| v0.7.1 |" not in r:
    r = r.replace("| v0.7.0 | Approval-governance corridor milestone; packages v0.6.0-v0.6.9 and returns focus to Tau mechanics. |\n",
                  "| v0.7.0 | Approval-governance corridor milestone; packages v0.6.0-v0.6.9 and returns focus to Tau mechanics. |\n| v0.7.1 | Tau mechanics return review; inspects tau vectors, gate algebra, thresholds, and evidence surfaces. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**

Recommended goals:

- Define tau-vector field names and intended semantics.
- Map each tau field to claim-card evidence requirements.
- Identify fields that are too implicit, overloaded, or under-tested.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "run_tau_mechanics_return_review.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_approval_governance_corridor.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_approval_governance_corridor.py\npython scripts/benchmarks/run_tau_mechanics_return_review.py\npython -m unittest discover -s tests")
        s = s.replace("| Approval corridor patch | `reports/approval_corridor/`, `visuals/approval_corridor/`, v0.6 reports | corridor milestone + release validator; no execution |\n",
                      "| Approval corridor patch | `reports/approval_corridor/`, `visuals/approval_corridor/`, v0.6 reports | corridor milestone + release validator; no execution |\n| Tau mechanics review patch | `reports/tau_mechanics_review/`, `visuals/tau_mechanics_review/`, core runtime/seeds | mechanics scan + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Tau mechanics review patch |" not in s:
        s = s.replace("| Approval corridor patch | outer | milestone | governance | v0.6 approval reports | corridor manifest + charts + release validator | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` |\n",
                      "| Approval corridor patch | outer | milestone | governance | v0.6 approval reports | corridor manifest + charts + release validator | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` |\n| Tau mechanics review patch | inner | analysis | runtime | core runtime + seeds + reports | mechanics scan + charts + release validator | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.1"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["tau_mechanics_return_review"] = {
    "read_first": ["src/tau_scaling/core/", "configs/seeds/", "reports/approval_corridor/latest_approval_governance_corridor_milestone.json"],
    "validate": ["python scripts/benchmarks/run_tau_mechanics_return_review.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/tau_mechanics_review/latest_tau_mechanics_return_review.md", "visuals/tau_mechanics_review/v0_7_1/"],
    "mutation_lock": "Review only; no replay execution, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.1 | Tau mechanics return review |" not in t:
    t = t.replace("| v0.7.0 | Approval-governance corridor milestone | `python scripts/benchmarks/generate_approval_governance_corridor.py` | Packages v0.6.0-v0.6.9 as stable corridor and returns focus to Tau mechanics | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` | `visuals/approval_corridor/v0_7_0/` |\n",
                  "| v0.7.0 | Approval-governance corridor milestone | `python scripts/benchmarks/generate_approval_governance_corridor.py` | Packages v0.6.0-v0.6.9 as stable corridor and returns focus to Tau mechanics | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` | `visuals/approval_corridor/v0_7_0/` |\n| v0.7.1 | Tau mechanics return review | `python scripts/benchmarks/run_tau_mechanics_return_review.py` | Reviews tau-vector, gate, threshold, seed, and evidence surfaces | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` | `visuals/tau_mechanics_review/v0_7_1/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_1_tau_mechanics_return_review.md", f"""# TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review

Generated: {NOW}

## Purpose

Return from approval-governance containment to core Tau mechanics: tau vectors, gate algebra, TSEK thresholds, synthetic behavior, sensitivity sweeps, and evidence-card design.

## Boundary

Tau mechanics return reviews are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.1 patch written")
