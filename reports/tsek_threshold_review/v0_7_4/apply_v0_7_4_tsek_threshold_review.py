
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
        d = ROOT / "reports" / "tsek_threshold_review" / "v0_7_4" / "backups" / f"{p.name}_before_v0_7_4_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "run_tsek_threshold_boundary_review.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zLCByZQpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfdGhyZXNob2xkX3JldmlldyIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJ0c2VrX3RocmVzaG9sZF9yZXZpZXciIC8gInYwXzdfNCIKCkNPUkVfRklMRVMgPSBbCiAgICBST09UIC8gInNyYyIgLyAidGF1X3NjYWxpbmciIC8gImNvcmUiIC8gImNsYXNzaWZpZXIucHkiLAogICAgUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjb3JlIiAvICJydW50aW1lLnB5IiwKICAgIFJPT1QgLyAic3JjIiAvICJ0YXVfc2NhbGluZyIgLyAiY29yZSIgLyAibW9kZWxzLnB5IiwKXQpSRVBPUlRTID0gewogICAgImdhdGVfYWxnZWJyYSI6IFJPT1QgLyAicmVwb3J0cyIgLyAiZ2F0ZV9hbGdlYnJhIiAvICJsYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5qc29uIiwKICAgICJ0YXVfdmVjdG9yX3NlbWFudGljcyI6IFJPT1QgLyAicmVwb3J0cyIgLyAidGF1X3ZlY3Rvcl9zZW1hbnRpY3MiIC8gImxhdGVzdF90YXVfdmVjdG9yX3NlbWFudGljc19sZWRnZXIuanNvbiIsCiAgICAic3ludGhldGljX2dhdGUiOiBST09UIC8gInJlcG9ydHMiIC8gImdhdGVzIiAvICJsYXRlc3Rfc3ludGhldGljX2dhdGVfcmVwb3J0Lmpzb24iLAogICAgInNlbnNpdGl2aXR5IjogUk9PVCAvICJyZXBvcnRzIiAvICJzZW5zaXRpdml0eSIgLyAibGF0ZXN0X3NlbnNpdGl2aXR5X3N3ZWVwLmpzb24iLAogICAgImludGVyYWN0aW9ucyI6IFJPT1QgLyAicmVwb3J0cyIgLyAiaW50ZXJhY3Rpb25zIiAvICJsYXRlc3RfZ2F0ZV9pbnRlcmFjdGlvbl9tYXRyaXguanNvbiIsCiAgICAicmVsZWFzZSI6IFJPT1QgLyAicmVwb3J0cyIgLyAicmVsZWFzZSIgLyAibGF0ZXN0X3JlbGVhc2VfcmVhZGluZXNzLmpzb24iLAp9CkJFTkNITUFSS19ESVJTID0gWwogICAgUk9PVCAvICJyZXBvcnRzIiAvICJiZW5jaG1hcmtzIiwKICAgIFJPT1QgLyAicmVwb3J0cyIgLyAiZ2F0ZXMiLAogICAgUk9PVCAvICJyZXBvcnRzIiAvICJpbnRlcmFjdGlvbnMiLAogICAgUk9PVCAvICJyZXBvcnRzIiAvICJleHBsYW5hdGlvbnMiLAogICAgUk9PVCAvICJyZXBvcnRzIiAvICJyZWdyZXNzaW9uX3JldmlldyIsCl0KClRTRUtfQ0xBU1NFUyA9IFsiVFNFSy1BIiwgIlRTRUstQiIsICJUU0VLLUMiLCAiVFNFSy1EIiwgIlRTRUstRSJdCgpkZWYgcmVhZF90ZXh0KHBhdGg6IFBhdGgpIC0+IHN0cjoKICAgIHJldHVybiBwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiLCBlcnJvcnM9InJlcGxhY2UiKSBpZiBwYXRoLmV4aXN0cygpIGVsc2UgIiIKCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCk6CiAgICBpZiBub3QgcGF0aC5leGlzdHMoKToKICAgICAgICByZXR1cm4geyJtaXNzaW5nIjogVHJ1ZSwgInBhdGgiOiBzdHIocGF0aCl9CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJwYXJzZV9lcnJvciI6IHN0cihleGMpLCAicGF0aCI6IHN0cihwYXRoKX0KCmRlZiB3anNvbihwYXRoOiBQYXRoLCBkYXRhKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKGRhdGEsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cik6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocGF0aDogUGF0aCkgLT4gc3RyOgogICAgcmV0dXJuIHN0cihwYXRoLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBzY2FuX2NsYXNzaWZpZXJfY29kZSgpOgogICAgdGV4dCA9ICJcbiIuam9pbihyZWFkX3RleHQocCkgZm9yIHAgaW4gQ09SRV9GSUxFUykKICAgIGNsYXNzX2NvdW50cyA9IHtjOiBsZW4ocmUuZmluZGFsbChyZS5lc2NhcGUoYyksIHRleHQpKSBmb3IgYyBpbiBUU0VLX0NMQVNTRVN9CiAgICB0aHJlc2hvbGRfdGVybXMgPSB7CiAgICAgICAgInRocmVzaG9sZCI6IGxlbihyZS5maW5kYWxsKHIidGhyZXNob2xkIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJzY29yZSI6IGxlbihyZS5maW5kYWxsKHIic2NvcmUiLCB0ZXh0LCByZS5JKSksCiAgICAgICAgImRvd25ncmFkZSI6IGxlbihyZS5maW5kYWxsKHIiZG93bmdyYWRlIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJmaW5kaW5nIjogbGVuKHJlLmZpbmRhbGwociJmaW5kaW5nIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJoYXJkX2dhdGUiOiBsZW4ocmUuZmluZGFsbChyImhhcmRbXyAtXT9nYXRlIiwgdGV4dCwgcmUuSSkpLAogICAgICAgICJldmlkZW5jZSI6IGxlbihyZS5maW5kYWxsKHIiZXZpZGVuY2UiLCB0ZXh0LCByZS5JKSksCiAgICAgICAgInN1cHBvcnQiOiBsZW4ocmUuZmluZGFsbChyInN1cHBvcnQiLCB0ZXh0LCByZS5JKSksCiAgICB9CiAgICBudW1lcmljX2xpdGVyYWxzID0gc29ydGVkKHNldChyZS5maW5kYWxsKHIiKD88IVtBLVphLXowLTlfXSkoPzowP1wuXGQrfDFcLjB8WzItOV1cLlxkKykoPyFbQS1aYS16MC05X10pIiwgdGV4dCkpKVs6ODBdCiAgICBmdW5jdGlvbnMgPSBzb3J0ZWQoc2V0KHJlLmZpbmRhbGwociJkZWZccysoW0EtWmEtel9dW0EtWmEtejAtOV9dKilccypcKCIsIHRleHQpKSkKICAgIHJldHVybiB7CiAgICAgICAgImNsYXNzX2NvdW50cyI6IGNsYXNzX2NvdW50cywKICAgICAgICAidGhyZXNob2xkX3Rlcm1zIjogdGhyZXNob2xkX3Rlcm1zLAogICAgICAgICJudW1lcmljX2xpdGVyYWxzX3NlZW4iOiBudW1lcmljX2xpdGVyYWxzLAogICAgICAgICJmdW5jdGlvbl9jb3VudCI6IGxlbihmdW5jdGlvbnMpLAogICAgICAgICJmdW5jdGlvbnMiOiBmdW5jdGlvbnNbOjEwMF0sCiAgICB9CgpkZWYgc2Nhbl9yZXBvcnRzX2Zvcl9jbGFzc2VzKCk6CiAgICBjb3VudHMgPSBDb3VudGVyKCkKICAgIHNvdXJjZXMgPSBbXQogICAgZm9yIGQgaW4gQkVOQ0hNQVJLX0RJUlM6CiAgICAgICAgaWYgZC5leGlzdHMoKToKICAgICAgICAgICAgZm9yIHAgaW4gc29ydGVkKGQucmdsb2IoIiouanNvbiIpKToKICAgICAgICAgICAgICAgIHRleHQgPSByZWFkX3RleHQocCkKICAgICAgICAgICAgICAgIGlmIG5vdCB0ZXh0LnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgY29udGludWUKICAgICAgICAgICAgICAgIGxvY2FsID0ge2M6IHRleHQuY291bnQoYykgZm9yIGMgaW4gVFNFS19DTEFTU0VTfQogICAgICAgICAgICAgICAgaWYgYW55KGxvY2FsLnZhbHVlcygpKToKICAgICAgICAgICAgICAgICAgICBmb3IgYywgbiBpbiBsb2NhbC5pdGVtcygpOgogICAgICAgICAgICAgICAgICAgICAgICBjb3VudHNbY10gKz0gbgogICAgICAgICAgICAgICAgICAgIHNvdXJjZXMuYXBwZW5kKHJlbChwKSkKICAgIHJldHVybiBkaWN0KGNvdW50cyksIHNvdXJjZXNbOjEwMF0KCmRlZiBjbGFzc2lmeShjb2RlLCByZXBvcnRfY291bnRzLCByZXBvcnRzKToKICAgIGdhcHMgPSBbXQogICAgcmVsZWFzZSA9IHJlcG9ydHNbInJlbGVhc2UiXQogICAgZ2F0ZSA9IHJlcG9ydHNbImdhdGVfYWxnZWJyYSJdCiAgICByZWxlYXNlX3Bhc3NlZCA9IHJlbGVhc2UuZ2V0KCJwYXNzZWQiKSBpcyBUcnVlIGFuZCBsZW4ocmVsZWFzZS5nZXQoImZpbmRpbmdzIiwgW10pKSA9PSAwIGFuZCBsZW4ocmVsZWFzZS5nZXQoInN0ZXBfZmFpbHVyZXMiLCBbXSkpID09IDAKICAgIGdhdGVfcmVhZHkgPSBnYXRlLmdldCgiZ2F0ZV9hbGdlYnJhX3N0YXR1cyIpID09ICJHQVRFX0FMR0VCUkFfTUFQX1JFQURZX19UQVJHRVRFRF9HQVRFX0dBUFNfSURFTlRJRklFRCIKCiAgICBpZiBub3QgcmVsZWFzZV9wYXNzZWQ6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInJlbGVhc2Vfbm90X3Bhc3NpbmciKQogICAgaWYgbm90IGdhdGVfcmVhZHk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoImdhdGVfYWxnZWJyYV9ub3RfcmVhZHkiKQogICAgaWYgc3VtKGNvZGVbImNsYXNzX2NvdW50cyJdLnZhbHVlcygpKSA9PSAwOgogICAgICAgIGdhcHMuYXBwZW5kKCJ0c2VrX2NsYXNzZXNfbm90X3Zpc2libGVfaW5fY29yZV9jb2RlIikKICAgIGlmIGNvZGVbInRocmVzaG9sZF90ZXJtcyJdWyJ0aHJlc2hvbGQiXSA9PSAwOgogICAgICAgIGdhcHMuYXBwZW5kKCJ0aHJlc2hvbGRfdGVybXNfbm90X2V4cGxpY2l0X2luX2NsYXNzaWZpZXJfc2NhbiIpCiAgICBpZiBjb2RlWyJ0aHJlc2hvbGRfdGVybXMiXVsiZG93bmdyYWRlIl0gPT0gMDoKICAgICAgICBnYXBzLmFwcGVuZCgiZG93bmdyYWRlX3Rlcm1zX25vdF9leHBsaWNpdF9pbl9jbGFzc2lmaWVyX3NjYW4iKQogICAgaWYgbm90IHJlcG9ydF9jb3VudHM6CiAgICAgICAgZ2Fwcy5hcHBlbmQoIm5vX3RzZWtfY2xhc3NfZGlzdHJpYnV0aW9uX2ZvdW5kX2luX3JlcG9ydHMiKQogICAgaWYgcmVwb3J0X2NvdW50cy5nZXQoIlRTRUstQSIsIDApID09IDA6CiAgICAgICAgZ2Fwcy5hcHBlbmQoIm5vX3RzZWtfYV9vYnNlcnZlZF9pbl9yZXBvcnRfc2NhbiIpCiAgICBpZiByZXBvcnRfY291bnRzLmdldCgiVFNFSy1EIiwgMCkgPT0gMDoKICAgICAgICBnYXBzLmFwcGVuZCgibm9fdHNla19kX29ic2VydmVkX2luX3JlcG9ydF9zY2FuIikKCiAgICBzdGF0dXMgPSAiVFNFS19USFJFU0hPTERfQk9VTkRBUllfUkVWSUVXX1JFQURZX19OT19USFJFU0hPTERfQ0hBTkdFIiBpZiByZWxlYXNlX3Bhc3NlZCBhbmQgZ2F0ZV9yZWFkeSBlbHNlICJUU0VLX1RIUkVTSE9MRF9CT1VOREFSWV9SRVZJRVdfTkVFRFNfUkVQQUlSIgogICAgcmV0dXJuIGdhcHMsIHN0YXR1cywgcmVsZWFzZV9wYXNzZWQsIGdhdGVfcmVhZHkKCmRlZiBjaGFydHMoc3VtbWFyeSk6CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZXhjKSkKICAgICAgICByZXR1cm4gcGF0aHMKCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgY2xhc3NfY291bnRzID0gc3VtbWFyeVsiY29yZV90c2VrX2NsYXNzX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGNsYXNzX2NvdW50cy5rZXlzKCkpLCBsaXN0KGNsYXNzX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueWxhYmVsKCJDb3JlIG1lbnRpb25zIikKICAgIHBsdC50aXRsZSgiVFNFSyBDbGFzcyBNZW50aW9ucyBpbiBDb3JlIENvZGUiKQogICAgc2F2ZSgidHNla19jb3JlX2NsYXNzX21lbnRpb25zLnBuZyIpCgogICAgcmVwb3J0X2NvdW50cyA9IHN1bW1hcnlbInJlcG9ydF90c2VrX2NsYXNzX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihUU0VLX0NMQVNTRVMsIFtyZXBvcnRfY291bnRzLmdldChjLCAwKSBmb3IgYyBpbiBUU0VLX0NMQVNTRVNdKQogICAgcGx0LnlsYWJlbCgiUmVwb3J0IG1lbnRpb25zIikKICAgIHBsdC50aXRsZSgiVFNFSyBDbGFzcyBNZW50aW9ucyBpbiBSZXBvcnRzIikKICAgIHNhdmUoInRzZWtfcmVwb3J0X2NsYXNzX21lbnRpb25zLnBuZyIpCgogICAgdGVybXMgPSBzdW1tYXJ5WyJ0aHJlc2hvbGRfdGVybXMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdCh0ZXJtcy5rZXlzKCkpLCBsaXN0KHRlcm1zLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3JlIG1lbnRpb25zIikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIEJvdW5kYXJ5IFRlcm0gVmlzaWJpbGl0eSIpCiAgICBzYXZlKCJ0c2VrX3RocmVzaG9sZF90ZXJtX3Zpc2liaWxpdHkucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjQgVFNFSyBUaHJlc2hvbGQgQm91bmRhcnkgUmV2aWV3IiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmV2aWV3IFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIFRocmVzaG9sZCByZXZpZXcgc3RhdHVzOiBge3N1bW1hcnlbJ3RocmVzaG9sZF9yZXZpZXdfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIEdhdGUgYWxnZWJyYSByZWFkeTogYHtzdW1tYXJ5WydnYXRlX2FsZ2VicmFfcmVhZHknXX1gIiwKICAgICAgICBmIi0gR2FwIGNvdW50OiBge3N1bW1hcnlbJ2dhcF9jb3VudCddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3N1bW1hcnlbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ29yZSBUU0VLIENsYXNzIFZpc2liaWxpdHkiLAogICAgICAgICIiLAogICAgICAgICJ8IENsYXNzIHwgQ29yZSBtZW50aW9ucyB8IFJlcG9ydCBtZW50aW9ucyB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLTp8IiwKICAgIF0KICAgIGZvciBjIGluIFRTRUtfQ0xBU1NFUzoKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7Y31gIHwge3N1bW1hcnlbJ2NvcmVfdHNla19jbGFzc19jb3VudHMnXS5nZXQoYywgMCl9IHwge3N1bW1hcnlbJ3JlcG9ydF90c2VrX2NsYXNzX2NvdW50cyddLmdldChjLCAwKX0gfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBUaHJlc2hvbGQgVGVybSBWaXNpYmlsaXR5IiwKICAgICAgICAiIiwKICAgICAgICAifCBUZXJtIHwgQ29yZSBtZW50aW9ucyB8IiwKICAgICAgICAifC0tLXwtLS06fCIsCiAgICBdCiAgICBmb3IgaywgdiBpbiBzdW1tYXJ5WyJ0aHJlc2hvbGRfdGVybXMiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCgogICAgbGluZXMgKz0gWyIiLCAiIyMgTnVtZXJpYyBMaXRlcmFscyBPYnNlcnZlZCIsICIiXQogICAgaWYgc3VtbWFyeVsibnVtZXJpY19saXRlcmFsc19zZWVuIl06CiAgICAgICAgbGluZXMuYXBwZW5kKCJgYGB0ZXh0IikKICAgICAgICBmb3IgaXRlbSBpbiBzdW1tYXJ5WyJudW1lcmljX2xpdGVyYWxzX3NlZW4iXToKICAgICAgICAgICAgbGluZXMuYXBwZW5kKGl0ZW0pCiAgICAgICAgbGluZXMuYXBwZW5kKCJgYGAiKQogICAgZWxzZToKICAgICAgICBsaW5lcy5hcHBlbmQoIi0gYG5vbmVfZGV0ZWN0ZWRgIikKCiAgICBsaW5lcyArPSBbIiIsICIjIyBUYXJnZXRlZCBHYXBzIiwgIiJdCiAgICBpZiBzdW1tYXJ5WyJnYXBzIl06CiAgICAgICAgZm9yIGdhcCBpbiBzdW1tYXJ5WyJnYXBzIl06CiAgICAgICAgICAgIGxpbmVzLmFwcGVuZChmIi0gYHtnYXB9YCIpCiAgICBlbHNlOgogICAgICAgIGxpbmVzLmFwcGVuZCgiLSBgbm9uZV9kZXRlY3RlZF9pbl92MF83XzRfc2NhbmAiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgQm91bmRhcnkgRGVjaXNpb24iLAogICAgICAgICIiLAogICAgICAgICJUaGlzIGxheWVyIGlzICoqcmV2aWV3LW9ubHkqKi4gSXQgZG9lcyBub3QgYWx0ZXIgdGhyZXNob2xkcywgY2xhc3Mgd2VpZ2h0cywgZG93bmdyYWRlIGxvZ2ljLCBzdXBwb3J0IGNvbnN0cmFpbnRzLCBvciBjbGFzc2lmaWVyIGJlaGF2aW9yLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIE5leHQgVGF1IFdvcmsiLAogICAgICAgICIiLAogICAgICAgICIxLiBCdWlsZCBhIFRTRUsgdGhyZXNob2xkIHRhYmxlIGZyb20gY3VycmVudCBjbGFzc2lmaWVyIGxvZ2ljLiIsCiAgICAgICAgIjIuIEFkZCBub24tbXV0YXRpbmcgdGhyZXNob2xkIGV4cGxhbmF0aW9uIGNhcmRzIGZvciBlYWNoIGNsYXNzIGJvdW5kYXJ5LiIsCiAgICAgICAgIjMuIENvbXBhcmUgb2JzZXJ2ZWQgcmVwb3J0IGNsYXNzIGRpc3RyaWJ1dGlvbnMgYWdhaW5zdCBleHBlY3RlZCBkb3duZ3JhZGUvcHJvbW90aW9uIHBhdGh3YXlzLiIsCiAgICAgICAgIjQuIERlc2lnbiB1bmRlci1wZW5hbHR5IGFuZCBvdmVyLXBlbmFsdHkgbmVnYXRpdmUgY29udHJvbHMgYmVmb3JlIGFueSB0aHJlc2hvbGQgY2hhbmdlLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENoYXJ0cyIsCiAgICAgICAgIiIsCiAgICBdCiAgICBmb3IgcCBpbiBzdW1tYXJ5WyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc3VtbWFyeVsiYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIHJlcG9ydHMgPSB7azogcmVhZF9qc29uKHYpIGZvciBrLCB2IGluIFJFUE9SVFMuaXRlbXMoKX0KICAgIGNvZGUgPSBzY2FuX2NsYXNzaWZpZXJfY29kZSgpCiAgICByZXBvcnRfY291bnRzLCByZXBvcnRfc291cmNlcyA9IHNjYW5fcmVwb3J0c19mb3JfY2xhc3NlcygpCiAgICBnYXBzLCBzdGF0dXMsIHJlbGVhc2VfcGFzc2VkLCBnYXRlX3JlYWR5ID0gY2xhc3NpZnkoY29kZSwgcmVwb3J0X2NvdW50cywgcmVwb3J0cykKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctdHNlay10aHJlc2hvbGQtYm91bmRhcnktcmV2aWV3LXYwLjcuNCIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJ0aHJlc2hvbGRfcmV2aWV3X3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBib29sKHJlbGVhc2VfcGFzc2VkKSwKICAgICAgICAiZ2F0ZV9hbGdlYnJhX3JlYWR5IjogYm9vbChnYXRlX3JlYWR5KSwKICAgICAgICAiY29yZV90c2VrX2NsYXNzX2NvdW50cyI6IGNvZGVbImNsYXNzX2NvdW50cyJdLAogICAgICAgICJyZXBvcnRfdHNla19jbGFzc19jb3VudHMiOiByZXBvcnRfY291bnRzLAogICAgICAgICJ0aHJlc2hvbGRfdGVybXMiOiBjb2RlWyJ0aHJlc2hvbGRfdGVybXMiXSwKICAgICAgICAibnVtZXJpY19saXRlcmFsc19zZWVuIjogY29kZVsibnVtZXJpY19saXRlcmFsc19zZWVuIl0sCiAgICAgICAgImNsYXNzaWZpZXJfZnVuY3Rpb25fY291bnQiOiBjb2RlWyJmdW5jdGlvbl9jb3VudCJdLAogICAgICAgICJjbGFzc2lmaWVyX2Z1bmN0aW9ucyI6IGNvZGVbImZ1bmN0aW9ucyJdLAogICAgICAgICJyZXBvcnRfc291cmNlc19zY2FubmVkX3dpdGhfdHNla19jbGFzc2VzIjogcmVwb3J0X3NvdXJjZXMsCiAgICAgICAgImdhcHMiOiBnYXBzLAogICAgICAgICJnYXBfY291bnQiOiBsZW4oZ2FwcyksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9iZWhhdmlvcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJNb3ZlIHRvIHYwLjcuNSBUU0VLIEJvdW5kYXJ5IEV4cGxhbmF0aW9uIENhcmRzIGJlZm9yZSBhbnkgY2xhc3NpZmllciB0aHJlc2hvbGQgY2hhbmdlcy4iLAogICAgICAgICJib3VuZGFyeSI6ICJUU0VLIHRocmVzaG9sZCBib3VuZGFyeSByZXZpZXdzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYW5hbHlzaXMgYXJ0aWZhY3RzLiBUaGV5IGluc3BlY3QgY3VycmVudCB0aHJlc2hvbGQvY2xhc3MtYm91bmRhcnkgdmlzaWJpbGl0eSB3aXRob3V0IGNoYW5naW5nIGNsYXNzaWZpZXIgYmVoYXZpb3IuIFRoZXkgZG8gbm90IGNyZWF0ZSBsaXZlIGFwcHJvdmFsLCBleGVjdXRlIHJlcGxheSBjb21tYW5kcywgY3JlYXRlIGJyYW5jaGVzLCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciwgYXBwbHkgY2FsaWJyYXRpb24sIG9yIHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAidHNla190aHJlc2hvbGRfYm91bmRhcnlfcmV2aWV3X3YwXzdfNC5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfdHNla190aHJlc2hvbGRfYm91bmRhcnlfcmV2aWV3Lmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gInRzZWtfdGhyZXNob2xkX2JvdW5kYXJ5X3Jldmlld192MF83XzQubWQiLCBtYWtlX21kKHN1bW1hcnkpKQogICAgd3RleHQoT1VUIC8gImxhdGVzdF90c2VrX3RocmVzaG9sZF9ib3VuZGFyeV9yZXZpZXcubWQiLCBtYWtlX21kKHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAidGhyZXNob2xkX3Jldmlld19zdGF0dXMiOiBzdW1tYXJ5WyJ0aHJlc2hvbGRfcmV2aWV3X3N0YXR1cyJdLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0sCiAgICAgICAgImdhdGVfYWxnZWJyYV9yZWFkeSI6IHN1bW1hcnlbImdhdGVfYWxnZWJyYV9yZWFkeSJdLAogICAgICAgICJnYXBfY291bnQiOiBzdW1tYXJ5WyJnYXBfY291bnQiXSwKICAgICAgICAidGhyZXNob2xkc19jaGFuZ2VkIjogc3VtbWFyeVsidGhyZXNob2xkc19jaGFuZ2VkIl0sCiAgICAgICAgImNsYXNzaWZpZXJfY2hhbmdlZCI6IHN1bW1hcnlbImNsYXNzaWZpZXJfY2hhbmdlZCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvdHNla190aHJlc2hvbGRfcmV2aWV3L2xhdGVzdF90c2VrX3RocmVzaG9sZF9ib3VuZGFyeV9yZXZpZXcubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT / "reports" / "tsek_threshold_review" / "README.md", """# TSEK Threshold Review Reports

Current layer: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**

## Purpose

This folder stores non-mutating TSEK threshold boundary reviews.

## Primary command

```powershell
python scripts/benchmarks/run_tsek_threshold_boundary_review.py
```

## README Update Rule

Update this mini README whenever TSEK threshold definitions, class-boundary explanations, or downgrade policy reviews change.

Boundary: TSEK threshold reviews are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "tsek_threshold_review" / "README.md", """# TSEK Threshold Review Visuals

Current layer: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**

## Purpose

This folder stores charts summarizing TSEK class and threshold visibility.

## README Update Rule

Update this mini README whenever TSEK threshold chart names or meanings change.

Boundary: TSEK threshold visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "tsek_threshold_review" / "v0_7_4" / "README.md", """# v0.7.4 TSEK Threshold Review Charts

Expected charts:

- `tsek_core_class_mentions.png`
- `tsek_report_class_mentions.png`
- `tsek_threshold_term_visibility.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local TSEK threshold diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.3[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.2[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.3 - Gate Algebra Map**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.3 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.4 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.3-ready |", "| Task routing matrix | geometry-aware / v0.7.4-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.3 |", "| Agent contract version sync | current / v0.7.4 |")

if "| TSEK threshold boundary review |" not in r:
    r = r.replace("| Gate algebra charts | `visuals/gate_algebra/v0_7_3/` |\n",
                  "| Gate algebra charts | `visuals/gate_algebra/v0_7_3/` |\n| TSEK threshold boundary review | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` |\n| TSEK threshold charts | `visuals/tsek_threshold_review/v0_7_4/` |\n")

if "python scripts/benchmarks/run_tsek_threshold_boundary_review.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_gate_algebra_map.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_gate_algebra_map.py\npython scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython scripts/release/validate_release.py")

if "    tsek_threshold_review/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    tsek_threshold_review/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    tsek_threshold_review/\n")

section = """## TSEK Threshold Boundary Review v0.7.4

v0.7.4 reviews TSEK class-boundary and threshold visibility without changing classifier behavior.

Primary command:

```powershell
python scripts/benchmarks/run_tsek_threshold_boundary_review.py
```

Primary outputs:

```text
reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.json
reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md
visuals/tsek_threshold_review/v0_7_4/
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

Boundary: TSEK threshold boundary reviews are local classifier-governance analysis artifacts. They inspect current threshold/class-boundary visibility without changing classifier behavior. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## TSEK Threshold Boundary Review v0.7.4" not in r:
    r = r.replace("## Gate Algebra Map v0.7.3", section + "## Gate Algebra Map v0.7.3", 1)

lesson = "| L-056 | v0.7.3 mapped gate-family visibility and found targeted gate gaps. | Gate mapping still does not authorize threshold changes. | TSEK threshold boundaries must be reviewed and explained before any classifier mutation or threshold tuning. |"
if "L-056" not in r:
    r = r.replace("| L-055 | v0.7.2 named tau-vector semantic gaps without changing scoring. | Tau semantics alone are not enough; the next layer must map which gates consume or expose those semantics. | Gate algebra must be mapped before TSEK thresholds or policy penalties are tightened. |\n",
                  "| L-055 | v0.7.2 named tau-vector semantic gaps without changing scoring. | Tau semantics alone are not enough; the next layer must map which gates consume or expose those semantics. | Gate algebra must be mapped before TSEK thresholds or policy penalties are tightened. |\n" + lesson + "\n")

if "| v0.7.4 |" not in r:
    r = r.replace("| v0.7.3 | Gate algebra map; maps gate-family visibility before threshold changes. |\n",
                  "| v0.7.3 | Gate algebra map; maps gate-family visibility before threshold changes. |\n| v0.7.4 | TSEK threshold boundary review; reviews class-boundary visibility without mutation. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**

Recommended goals:

- Generate one explanation card per TSEK class boundary.
- Explain downgrade vs evidence sufficiency.
- Preserve no-threshold-change and no-classifier-mutation locks.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "run_tsek_threshold_boundary_review.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_gate_algebra_map.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_gate_algebra_map.py\npython scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython -m unittest discover -s tests")
        s = s.replace("| Gate algebra patch | `reports/gate_algebra/`, `visuals/gate_algebra/`, core gates/seeds | gate map + release validator; no mutation |\n",
                      "| Gate algebra patch | `reports/gate_algebra/`, `visuals/gate_algebra/`, core gates/seeds | gate map + release validator; no mutation |\n| TSEK threshold review patch | `reports/tsek_threshold_review/`, `visuals/tsek_threshold_review/`, classifier/reports | threshold boundary review + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| TSEK threshold review patch |" not in s:
        s = s.replace("| Gate algebra patch | inner | analysis | runtime | core gates + seeds + tau semantics | gate algebra map + charts + release validator | `reports/gate_algebra/latest_gate_algebra_map.md` |\n",
                      "| Gate algebra patch | inner | analysis | runtime | core gates + seeds + tau semantics | gate algebra map + charts + release validator | `reports/gate_algebra/latest_gate_algebra_map.md` |\n| TSEK threshold review patch | inner | analysis | classifier | classifier + gate algebra + reports | threshold review + charts + release validator | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.4"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["tsek_threshold_boundary_review"] = {
    "read_first": ["src/tau_scaling/core/classifier.py", "reports/gate_algebra/latest_gate_algebra_map.json", "reports/release/latest_release_readiness.json"],
    "validate": ["python scripts/benchmarks/run_tsek_threshold_boundary_review.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md", "visuals/tsek_threshold_review/v0_7_4/"],
    "mutation_lock": "Threshold review only; no classifier change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.4 | TSEK threshold boundary review |" not in t:
    t = t.replace("| v0.7.3 | Gate algebra map | `python scripts/benchmarks/generate_gate_algebra_map.py` | Maps gate-family visibility before TSEK threshold changes | `reports/gate_algebra/latest_gate_algebra_map.md` | `visuals/gate_algebra/v0_7_3/` |\n",
                  "| v0.7.3 | Gate algebra map | `python scripts/benchmarks/generate_gate_algebra_map.py` | Maps gate-family visibility before TSEK threshold changes | `reports/gate_algebra/latest_gate_algebra_map.md` | `visuals/gate_algebra/v0_7_3/` |\n| v0.7.4 | TSEK threshold boundary review | `python scripts/benchmarks/run_tsek_threshold_boundary_review.py` | Reviews TSEK class-boundary visibility without changing classifier behavior | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` | `visuals/tsek_threshold_review/v0_7_4/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_4_tsek_threshold_review.md", f"""# TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review

Generated: {NOW}

## Purpose

Review TSEK threshold and class-boundary visibility without changing classifier behavior.

## Boundary

TSEK threshold boundary reviews are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.4 patch written")
