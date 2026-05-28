
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"blocked_trend_review"/"v0_6_9"/"backups"/f"{p.name}_before_v0_6_9_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_blocked_state_trend_review.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdCkNPTlRJTlVJVFkgPSBST09UIC8gInJlcG9ydHMiIC8gImJsb2NrZWRfY29udGludWl0eSIgLyAibGF0ZXN0X2Jsb2NrZWRfc3RhdGVfY29udGludWl0eS5qc29uIgpMRURHRVIgPSBST09UIC8gInJlcG9ydHMiIC8gImJsb2NrZWRfY29udGludWl0eSIgLyAiYmxvY2tlZF9zdGF0ZV9jb250aW51aXR5X2xlZGdlci5qc29ubCIKT1VUID0gUk9PVCAvICJyZXBvcnRzIiAvICJibG9ja2VkX3RyZW5kX3JldmlldyIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJibG9ja2VkX3RyZW5kX3JldmlldyIgLyAidjBfNl85IgoKZGVmIHJqc29uKHApOgogICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgcmVhZF9qc29ubChwKToKICAgIGlmIG5vdCBwLmV4aXN0cygpOgogICAgICAgIHJldHVybiBbXQogICAgcm93cyA9IFtdCiAgICBmb3IgbGluZSBpbiBwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKS5zcGxpdGxpbmVzKCk6CiAgICAgICAgaWYgbGluZS5zdHJpcCgpOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICByb3dzLmFwcGVuZChqc29uLmxvYWRzKGxpbmUpKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICAgICAgcGFzcwogICAgcmV0dXJuIHJvd3MKCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgcmVsKHApOgogICAgcmV0dXJuIHN0cihwLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBjbGFzc2lmeShyb3dzLCBjb250aW51aXR5KToKICAgIGVudHJ5X2NvdW50ID0gbGVuKHJvd3MpCiAgICBleGVjdXRvcl9zdGF0dXNlcyA9IENvdW50ZXIocm93LmdldCgiZXhlY3V0b3Jfc3RhdHVzIiwgIlVOS05PV04iKSBmb3Igcm93IGluIHJvd3MpCiAgICBoYW5kb2ZmX3N0YXR1c2VzID0gQ291bnRlcihyb3cuZ2V0KCJoYW5kb2ZmX3N0YXR1cyIsICJVTktOT1dOIikgZm9yIHJvdyBpbiByb3dzKQogICAgcmVwbGF5X2FsbG93ZWRfY291bnQgPSBzdW0oMSBmb3Igcm93IGluIHJvd3MgaWYgcm93LmdldCgicmVwbGF5X2FsbG93ZWQiKSBpcyBUcnVlKQogICAgbXV0YXRpb25fYWxsb3dlZF9jb3VudCA9IHN1bSgxIGZvciByb3cgaW4gcm93cyBpZiByb3cuZ2V0KCJtdXRhdGlvbl9hbGxvd2VkIikgaXMgVHJ1ZSkKICAgIGV4ZWN1dGlvbl9jb3VudCA9IHN1bSgxIGZvciByb3cgaW4gcm93cyBpZiByb3cuZ2V0KCJleGVjdXRvcl9yYW4iKSBpcyBUcnVlKQogICAgYnJhbmNoX2NvdW50ID0gc3VtKDEgZm9yIHJvdyBpbiByb3dzIGlmIHJvdy5nZXQoImJyYW5jaF9jcmVhdGVkIikgaXMgVHJ1ZSkKICAgIGxpdmVfYXBwcm92YWxfcHJlc2VudF9jb3VudCA9IHN1bSgxIGZvciByb3cgaW4gcm93cyBpZiByb3cuZ2V0KCJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiKSBpcyBUcnVlKQoKICAgIGN1cnJlbnRfZXhlY3V0b3IgPSBjb250aW51aXR5LmdldCgiZXhlY3V0b3Jfc3RhdHVzIikKICAgIGN1cnJlbnRfaGFuZG9mZiA9IGNvbnRpbnVpdHkuZ2V0KCJoYW5kb2ZmX3N0YXR1cyIpCiAgICBjdXJyZW50X2Jsb2NrZWQgPSBjb250aW51aXR5LmdldCgiZXhlY3V0b3JfYmxvY2tlZCIpIGlzIFRydWUgYW5kIGNvbnRpbnVpdHkuZ2V0KCJoYW5kb2ZmX2Jsb2NrZWQiKSBpcyBUcnVlCgogICAgaWYgbXV0YXRpb25fYWxsb3dlZF9jb3VudCBvciBleGVjdXRpb25fY291bnQgb3IgYnJhbmNoX2NvdW50OgogICAgICAgIHN0YXR1cyA9ICJUUkVORF9SRVZJRVdfQUxFUlRfX1VORVhQRUNURURfRVhFQ1VUSU9OX09SX01VVEFUSU9OIgogICAgICAgIHJlY29tbWVuZGF0aW9uID0gIlN0b3AgcHJvbW90aW9uIGFuZCBpbnNwZWN0IGNvbnRpbnVpdHkgbGVkZ2VyIGltbWVkaWF0ZWx5LiIKICAgIGVsaWYgcmVwbGF5X2FsbG93ZWRfY291bnQ6CiAgICAgICAgc3RhdHVzID0gIlRSRU5EX1JFVklFV19BTEVSVF9fUkVQTEFZX0FMTE9XRURfRU5UUllfUFJFU0VOVCIKICAgICAgICByZWNvbW1lbmRhdGlvbiA9ICJJbnNwZWN0IGxpdmUgYXBwcm92YWwgY2hhaW4gYmVmb3JlIGFueSBuZXh0IGxheWVyLiIKICAgIGVsaWYgY3VycmVudF9ibG9ja2VkIGFuZCBjdXJyZW50X2hhbmRvZmYgPT0gIkhBTkRPRkZfQkxPQ0tFRF9fTk9fTElWRV9BUFBST1ZBTCI6CiAgICAgICAgc3RhdHVzID0gIlRSRU5EX1JFVklFV19DT05GSVJNRURfX0dPVkVSTkFOQ0VfQkxPQ0tfU1RJTExfVkFMSUQiCiAgICAgICAgcmVjb21tZW5kYXRpb24gPSAiQ29udGludWUgb25seSB3aXRoIGJsb2NrZWQtc3RhdGUgb2JzZXJ2YWJpbGl0eSBvciBsaXZlLWFwcHJvdmFsIHByZXBhcmF0aW9uOyBkbyBub3QgcmVwbGF5LiIKICAgIGVsaWYgZW50cnlfY291bnQgPT0gMDoKICAgICAgICBzdGF0dXMgPSAiVFJFTkRfUkVWSUVXX0lOQ09NUExFVEVfX05PX0xFREdFUl9FTlRSSUVTIgogICAgICAgIHJlY29tbWVuZGF0aW9uID0gIlJ1biBibG9ja2VkLXN0YXRlIGNvbnRpbnVpdHkgbGVkZ2VyIGJlZm9yZSB0cmVuZCByZXZpZXcuIgogICAgZWxzZToKICAgICAgICBzdGF0dXMgPSAiVFJFTkRfUkVWSUVXX05FRURTX0hVTUFOX0lOU1BFQ1RJT04iCiAgICAgICAgcmVjb21tZW5kYXRpb24gPSAiSW5zcGVjdCBsYXRlc3QgZXhlY3V0b3IvaGFuZG9mZiBzdGF0dXMgYmVmb3JlIGNvbnRpbnVpbmcuIgoKICAgIHJldHVybiB7CiAgICAgICAgImVudHJ5X2NvdW50IjogZW50cnlfY291bnQsCiAgICAgICAgImV4ZWN1dG9yX3N0YXR1c19jb3VudHMiOiBkaWN0KGV4ZWN1dG9yX3N0YXR1c2VzKSwKICAgICAgICAiaGFuZG9mZl9zdGF0dXNfY291bnRzIjogZGljdChoYW5kb2ZmX3N0YXR1c2VzKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWRfY291bnQiOiByZXBsYXlfYWxsb3dlZF9jb3VudCwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZF9jb3VudCI6IG11dGF0aW9uX2FsbG93ZWRfY291bnQsCiAgICAgICAgImV4ZWN1dGlvbl9jb3VudCI6IGV4ZWN1dGlvbl9jb3VudCwKICAgICAgICAiYnJhbmNoX2NvdW50IjogYnJhbmNoX2NvdW50LAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnRfY291bnQiOiBsaXZlX2FwcHJvdmFsX3ByZXNlbnRfY291bnQsCiAgICAgICAgImN1cnJlbnRfZXhlY3V0b3Jfc3RhdHVzIjogY3VycmVudF9leGVjdXRvciwKICAgICAgICAiY3VycmVudF9oYW5kb2ZmX3N0YXR1cyI6IGN1cnJlbnRfaGFuZG9mZiwKICAgICAgICAidHJlbmRfc3RhdHVzIjogc3RhdHVzLAogICAgICAgICJyZWNvbW1lbmRhdGlvbiI6IHJlY29tbWVuZGF0aW9uLAogICAgfQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgY291bnRzID0gc3VtbWFyeVsiZXhlY3V0b3Jfc3RhdHVzX2NvdW50cyJdIG9yIHsibm9uZSI6IDB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIobGlzdChjb3VudHMua2V5cygpKSwgbGlzdChjb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkxlZGdlciBlbnRyaWVzIikKICAgIHBsdC50aXRsZSgiQmxvY2tlZCBUcmVuZCBFeGVjdXRvciBTdGF0dXMgQ291bnRzIikKICAgIHNhdmUoImJsb2NrZWRfdHJlbmRfZXhlY3V0b3Jfc3RhdHVzX2NvdW50cy5wbmciKQoKICAgIGhhbmRvZmYgPSBzdW1tYXJ5WyJoYW5kb2ZmX3N0YXR1c19jb3VudHMiXSBvciB7Im5vbmUiOiAwfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoaGFuZG9mZi5rZXlzKCkpLCBsaXN0KGhhbmRvZmYudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkxlZGdlciBlbnRyaWVzIikKICAgIHBsdC50aXRsZSgiQmxvY2tlZCBUcmVuZCBIYW5kb2ZmIFN0YXR1cyBDb3VudHMiKQogICAgc2F2ZSgiYmxvY2tlZF90cmVuZF9oYW5kb2ZmX3N0YXR1c19jb3VudHMucG5nIikKCiAgICByaXNrID0gewogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkX2NvdW50Il0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dGlvbl9jb3VudCJdLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IHN1bW1hcnlbImJyYW5jaF9jb3VudCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZF9jb3VudCJdLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiOiBzdW1tYXJ5WyJsaXZlX2FwcHJvdmFsX3ByZXNlbnRfY291bnQiXSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3Qocmlzay5rZXlzKCkpLCBsaXN0KHJpc2sudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkxlZGdlciBjb3VudCIpCiAgICBwbHQudGl0bGUoIkJsb2NrZWQgVHJlbmQgUmlzayBDb3VudGVycyIpCiAgICBzYXZlKCJibG9ja2VkX3RyZW5kX3Jpc2tfY291bnRlcnMucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzKToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjYuOSBCbG9ja2VkLVN0YXRlIFRyZW5kIFJldmlldyIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c1snZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFRyZW5kIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIFRyZW5kIHN0YXR1czogYHtzWyd0cmVuZF9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gTGVkZ2VyIGVudHJpZXM6IGB7c1snZW50cnlfY291bnQnXX1gIiwKICAgICAgICBmIi0gQ3VycmVudCBleGVjdXRvciBzdGF0dXM6IGB7c1snY3VycmVudF9leGVjdXRvcl9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gQ3VycmVudCBoYW5kb2ZmIHN0YXR1czogYHtzWydjdXJyZW50X2hhbmRvZmZfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJlcGxheSBhbGxvd2VkIGVudHJpZXM6IGB7c1sncmVwbGF5X2FsbG93ZWRfY291bnQnXX1gIiwKICAgICAgICBmIi0gRXhlY3V0b3ItcmFuIGVudHJpZXM6IGB7c1snZXhlY3V0aW9uX2NvdW50J119YCIsCiAgICAgICAgZiItIEJyYW5jaC1jcmVhdGVkIGVudHJpZXM6IGB7c1snYnJhbmNoX2NvdW50J119YCIsCiAgICAgICAgZiItIE11dGF0aW9uLWFsbG93ZWQgZW50cmllczogYHtzWydtdXRhdGlvbl9hbGxvd2VkX2NvdW50J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJlY29tbWVuZGF0aW9uIiwKICAgICAgICAiIiwKICAgICAgICBzWyJyZWNvbW1lbmRhdGlvbiJdLAogICAgICAgICIiLAogICAgICAgICIjIyBTdGF0dXMgQ291bnRzIiwKICAgICAgICAiIiwKICAgICAgICAiIyMjIEV4ZWN1dG9yIFN0YXR1cyBDb3VudHMiLAogICAgICAgICIiLAogICAgICAgICJ8IEV4ZWN1dG9yIHN0YXR1cyB8IENvdW50IHwiLAogICAgICAgICJ8LS0tfC0tLTp8IiwKICAgIF0KICAgIGZvciBrLCB2IGluIHNbImV4ZWN1dG9yX3N0YXR1c19jb3VudHMiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIyBIYW5kb2ZmIFN0YXR1cyBDb3VudHMiLAogICAgICAgICIiLAogICAgICAgICJ8IEhhbmRvZmYgc3RhdHVzIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssIHYgaW4gc1siaGFuZG9mZl9zdGF0dXNfY291bnRzIl0uaXRlbXMoKToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7a31gIHwge3Z9IHwiKQoKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBjb250aW51aXR5ID0gcmpzb24oQ09OVElOVUlUWSkKICAgIHJvd3MgPSByZWFkX2pzb25sKExFREdFUikKICAgIHRyZW5kID0gY2xhc3NpZnkocm93cywgY29udGludWl0eSkKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctYmxvY2tlZC1zdGF0ZS10cmVuZC1yZXZpZXctdjAuNi45IiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgImlucHV0X2Jsb2NrZWRfY29udGludWl0eSI6IHJlbChDT05USU5VSVRZKSwKICAgICAgICAiaW5wdXRfYmxvY2tlZF9sZWRnZXIiOiByZWwoTEVER0VSKSwKICAgICAgICAqKnRyZW5kLAogICAgICAgICJyZXRpcmVtZW50X3JlY29tbWVuZGF0aW9uIjogImRvX25vdF9yZXRpcmVfYXBwcm92YWxfcGF0aHdheV95ZXQiLAogICAgICAgICJjb250aW51YXRpb25fcmVjb21tZW5kYXRpb24iOiAiY29udGludWVfYmxvY2tlZF9vYnNlcnZhYmlsaXR5X29yX2NyZWF0ZV9saXZlX2FwcHJvdmFsX3ByZXBhcmF0aW9uX2xheWVyIiwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiYm91bmRhcnkiOiAiQmxvY2tlZC1zdGF0ZSB0cmVuZCByZXZpZXdzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYW5hbHlzaXMgYXJ0aWZhY3RzLiBUaGV5IHJldmlldyBibG9ja2VkIGV4ZWN1dGlvbiBjb250aW51aXR5LiBUaGV5IGRvIG5vdCBjcmVhdGUgbGl2ZSBhcHByb3ZhbCwgZXhlY3V0ZSByZXBsYXkgY29tbWFuZHMsIGNyZWF0ZSBicmFuY2hlcywgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFwcGx5IGNhbGlicmF0aW9uLCBvciB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNy4wIHNob3VsZCBwYWNrYWdlIHRoZSBhcHByb3ZhbC1nb3Zlcm5hbmNlIGNvcnJpZG9yIGFzIGEgc3RhYmxlIGdvdmVybmFuY2UgbWlsZXN0b25lLCBub3QgY29udGludWUgYWRkaW5nIGdhdGVzIGluZGVmaW5pdGVseS4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJibG9ja2VkX3N0YXRlX3RyZW5kX3Jldmlld192MF82XzkuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X2Jsb2NrZWRfc3RhdGVfdHJlbmRfcmV2aWV3Lmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gImJsb2NrZWRfc3RhdGVfdHJlbmRfcmV2aWV3X3YwXzZfOS5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfYmxvY2tlZF9zdGF0ZV90cmVuZF9yZXZpZXcubWQiLCByZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJ0cmVuZF9zdGF0dXMiOiBzdW1tYXJ5WyJ0cmVuZF9zdGF0dXMiXSwKICAgICAgICAiZW50cnlfY291bnQiOiBzdW1tYXJ5WyJlbnRyeV9jb3VudCJdLAogICAgICAgICJjdXJyZW50X2V4ZWN1dG9yX3N0YXR1cyI6IHN1bW1hcnlbImN1cnJlbnRfZXhlY3V0b3Jfc3RhdHVzIl0sCiAgICAgICAgImN1cnJlbnRfaGFuZG9mZl9zdGF0dXMiOiBzdW1tYXJ5WyJjdXJyZW50X2hhbmRvZmZfc3RhdHVzIl0sCiAgICAgICAgInJlcGxheV9hbGxvd2VkX2NvdW50Ijogc3VtbWFyeVsicmVwbGF5X2FsbG93ZWRfY291bnQiXSwKICAgICAgICAiZXhlY3V0aW9uX2NvdW50Ijogc3VtbWFyeVsiZXhlY3V0aW9uX2NvdW50Il0sCiAgICAgICAgImJyYW5jaF9jb3VudCI6IHN1bW1hcnlbImJyYW5jaF9jb3VudCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkX2NvdW50Ijogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZF9jb3VudCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvYmxvY2tlZF90cmVuZF9yZXZpZXcvbGF0ZXN0X2Jsb2NrZWRfc3RhdGVfdHJlbmRfcmV2aWV3Lm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT/"reports"/"blocked_trend_review"/"README.md", """# Blocked-State Trend Review Reports

Current layer: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**

## Purpose

This folder stores trend reviews for blocked execution continuity ledgers.

## Primary command

```powershell
python scripts/benchmarks/run_blocked_state_trend_review.py
```

## README Update Rule

Update this mini README whenever blocked-state trend schemas, retirement criteria, or continuation rules change.

Boundary: blocked-state trend reviews are local classifier-governance analysis artifacts only.
""")
write(ROOT/"visuals"/"blocked_trend_review"/"README.md", """# Blocked-State Trend Review Visuals

Current layer: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**

## Purpose

This folder stores charts summarizing blocked-state continuity trends.

## README Update Rule

Update this mini README whenever blocked-trend chart names or meanings change.

Boundary: blocked-trend visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"blocked_trend_review"/"v0_6_9"/"README.md", """# v0.6.9 Blocked-State Trend Charts

Expected charts:

- `blocked_trend_executor_status_counts.png`
- `blocked_trend_handoff_status_counts.png`
- `blocked_trend_risk_counters.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local blocked-trend diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.8[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.7[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.8 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.9 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.8-ready |", "| Task routing matrix | geometry-aware / v0.6.9-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.8 |", "| Agent contract version sync | current / v0.6.9 |")
if "| Blocked-state trend review |" not in r:
    r=r.replace("| Blocked-state continuity charts | `visuals/blocked_continuity/v0_6_8/` |\n",
                "| Blocked-state continuity charts | `visuals/blocked_continuity/v0_6_8/` |\n| Blocked-state trend review | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` |\n| Blocked-state trend charts | `visuals/blocked_trend_review/v0_6_9/` |\n")
if "python scripts/benchmarks/run_blocked_state_trend_review.py" not in r:
    r=r.replace("python scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython scripts/benchmarks/run_blocked_state_trend_review.py\npython scripts/release/validate_release.py")
if "    blocked_trend_review/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    blocked_trend_review/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    blocked_trend_review/\n")
section="""## Blocked-State Trend Review v0.6.9

v0.6.9 reviews blocked-state continuity to distinguish valid governance block from stale target.

Primary command:

```powershell
python scripts/benchmarks/run_blocked_state_trend_review.py
```

Primary outputs:

```text
reports/blocked_trend_review/latest_blocked_state_trend_review.json
reports/blocked_trend_review/latest_blocked_state_trend_review.md
visuals/blocked_trend_review/v0_6_9/
```

Current expected lock:

```text
trend_status: TREND_REVIEW_CONFIRMED__GOVERNANCE_BLOCK_STILL_VALID
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: blocked-state trend reviews are local classifier-governance analysis artifacts. They review blocked execution continuity. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Blocked-State Trend Review v0.6.9" not in r:
    r=r.replace("## Blocked-State Continuity Ledger v0.6.8", section+"## Blocked-State Continuity Ledger v0.6.8",1)
lesson="| L-051 | v0.6.8 recorded blocked execution in a continuity ledger. | A ledger can accumulate blocked states without explaining whether the block is still valid or stale. | Blocked-state trend review must classify persistent blocks before continuing toward another execution or approval layer. |"
if "L-051" not in r:
    r=r.replace("| L-050 | v0.6.7 blocked the executor because live approval handoff was invalid. | Repeated blocked execution states should be preserved as continuity evidence, not treated as no-op failures. | Blocked executor states must append to a continuity ledger so future agents can see why execution remained blocked across versions. |\n",
                "| L-050 | v0.6.7 blocked the executor because live approval handoff was invalid. | Repeated blocked execution states should be preserved as continuity evidence, not treated as no-op failures. | Blocked executor states must append to a continuity ledger so future agents can see why execution remained blocked across versions. |\n"+lesson+"\n")
if "| v0.6.9 |" not in r:
    r=r.replace("| v0.6.8 | Blocked-state continuity ledger; records blocked execution as evidence. |\n",
                "| v0.6.8 | Blocked-state continuity ledger; records blocked execution as evidence. |\n| v0.6.9 | Blocked-state trend review; classifies whether block remains valid or stale. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**

Recommended goals:

- Package v0.6.0-v0.6.9 as a stable governance corridor.
- Summarize authority boundaries: template, fixture, live approval, handoff, executor, continuity, trend.
- Freeze mutation locks unless a separate live approval path is intentionally introduced.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_blocked_state_trend_review.py" not in s:
        s=s.replace("python scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython scripts/benchmarks/run_blocked_state_trend_review.py\npython -m unittest discover -s tests")
        s=s.replace("| Blocked continuity patch | `reports/blocked_continuity/`, `visuals/blocked_continuity/`, replay executor | continuity ledger + release validator; no execution |\n",
                    "| Blocked continuity patch | `reports/blocked_continuity/`, `visuals/blocked_continuity/`, replay executor | continuity ledger + release validator; no execution |\n| Blocked trend patch | `reports/blocked_trend_review/`, `visuals/blocked_trend_review/`, blocked continuity | trend review + release validator; no execution |\n")
    if name.endswith("task_routing_matrix.md") and "| Blocked trend patch |" not in s:
        s=s.replace("| Blocked continuity patch | outer | evidence | governance | replay executor + live approval handoff | continuity ledger + charts + release validator | `reports/blocked_continuity/latest_blocked_state_continuity.md` |\n",
                    "| Blocked continuity patch | outer | evidence | governance | replay executor + live approval handoff | continuity ledger + charts + release validator | `reports/blocked_continuity/latest_blocked_state_continuity.md` |\n| Blocked trend patch | outer | analysis | governance | blocked continuity ledger | trend review + charts + release validator | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.9"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["blocked_state_trend_review"]={
    "read_first":["reports/blocked_continuity/latest_blocked_state_continuity.json","reports/blocked_continuity/blocked_state_continuity_ledger.jsonl"],
    "validate":["python scripts/benchmarks/run_blocked_state_trend_review.py","python scripts/release/validate_release.py"],
    "evidence":["reports/blocked_trend_review/latest_blocked_state_trend_review.md","visuals/blocked_trend_review/v0_6_9/"],
    "mutation_lock":"Reviews blocked-state trend only; no replay execution, branch creation, or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.9 | Blocked-state trend review |" not in t:
    t=t.replace("| v0.6.8 | Blocked-state continuity ledger | `python scripts/benchmarks/run_blocked_state_continuity_ledger.py` | Records blocked executor state as continuity evidence | `reports/blocked_continuity/latest_blocked_state_continuity.md` | `visuals/blocked_continuity/v0_6_8/` |\n",
                "| v0.6.8 | Blocked-state continuity ledger | `python scripts/benchmarks/run_blocked_state_continuity_ledger.py` | Records blocked executor state as continuity evidence | `reports/blocked_continuity/latest_blocked_state_continuity.md` | `visuals/blocked_continuity/v0_6_8/` |\n| v0.6.9 | Blocked-state trend review | `python scripts/benchmarks/run_blocked_state_trend_review.py` | Classifies whether the persistent block is valid or stale | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` | `visuals/blocked_trend_review/v0_6_9/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_9_blocked_trend_review.md", f"""# TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review

Generated: {NOW}

## Purpose

Review blocked-state continuity and classify whether the execution block remains valid or stale.

## Boundary

Blocked-state trend reviews are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.9 patch written")
