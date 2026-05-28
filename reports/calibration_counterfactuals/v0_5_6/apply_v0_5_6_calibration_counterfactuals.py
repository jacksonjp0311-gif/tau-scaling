
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd()
NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"calibration_counterfactuals"/"v0_5_6"/"backups"/f"{p.name}_before_v0_5_6_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
runner_b64="CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdClBMQU4gPSBST09UIC8gInJlcG9ydHMiIC8gImNhbGlicmF0aW9uX3BsYW4iIC8gImxhdGVzdF9kaXNhYmxlZF9jYWxpYnJhdGlvbl9wbGFuLmpzb24iCk5FRyA9IFJPT1QgLyAicmVwb3J0cyIgLyAibmVnYXRpdmVfY29udHJvbHMiIC8gImxhdGVzdF9zdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2xzLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FsaWJyYXRpb25fY291bnRlcmZhY3R1YWxzIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImNhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscyIgLyAidjBfNV82IgoKZGVmIHJqc29uKHApOiByZXR1cm4ganNvbi5sb2FkcyhwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKZGVmIHdqc29uKHAsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KGpzb24uZHVtcHMoeCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHNpbXVsYXRlKGNvbnRyb2wsIHRocmVzaG9sZCk6CiAgICBkaWFnID0gY29udHJvbC5nZXQoImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIikKICAgIGhpZ2hfc3VwcG9ydCA9IGlzaW5zdGFuY2UoZGlhZywgKGludCwgZmxvYXQpKSBhbmQgZGlhZyA+PSB0aHJlc2hvbGQKICAgIGN1cnJlbnRfYmVoYXZpb3IgPSBjb250cm9sLmdldCgib2JzZXJ2ZWRfcmVwb3J0X29ubHlfYmVoYXZpb3IiKQogICAgcHJvcG9zZWRfYmVoYXZpb3IgPSAicmV0YWluX2Jsb2NrZWRfbm9fZG93bmdyYWRlIiBpZiBoaWdoX3N1cHBvcnQgZWxzZSAiZWxpZ2libGVfZm9yX3Jldmlld19ub3RfZW5mb3JjZW1lbnQiCiAgICBzdXBwb3J0X3Bhc3NfcHJlc2VydmVkID0gYm9vbChjb250cm9sLmdldCgibmVnYXRpdmVfY29udHJvbF9wYXNzZWQiKSkgYW5kIHByb3Bvc2VkX2JlaGF2aW9yID09ICJyZXRhaW5fYmxvY2tlZF9ub19kb3duZ3JhZGUiCiAgICBkcmlmdCA9IGN1cnJlbnRfYmVoYXZpb3IgIT0gcHJvcG9zZWRfYmVoYXZpb3IKICAgIHJldHVybiB7CiAgICAgICAgImNvbnRyb2xfaWQiOiBjb250cm9sLmdldCgiY29udHJvbF9pZCIpLAogICAgICAgICJnYXRlX3BhaXIiOiBjb250cm9sLmdldCgiZ2F0ZV9wYWlyIiksCiAgICAgICAgImRpYWdub3N0aWNfYXZlcmFnZSI6IGRpYWcsCiAgICAgICAgInNlbGVjdGVkX3RocmVzaG9sZCI6IHRocmVzaG9sZCwKICAgICAgICAiY3VycmVudF9iZWhhdmlvciI6IGN1cnJlbnRfYmVoYXZpb3IsCiAgICAgICAgInByb3Bvc2VkX3JlcG9ydF9vbmx5X2JlaGF2aW9yIjogcHJvcG9zZWRfYmVoYXZpb3IsCiAgICAgICAgImNvdW50ZXJmYWN0dWFsX2RyaWZ0IjogZHJpZnQsCiAgICAgICAgInN1cHBvcnRfcGFzc19wcmVzZXJ2ZWQiOiBzdXBwb3J0X3Bhc3NfcHJlc2VydmVkLAogICAgICAgICJjb3VudGVyZmFjdHVhbF9zdGF0dXMiOiAic2FmZV9yZXBvcnRfb25seV9jYW5kaWRhdGUiIGlmIHN1cHBvcnRfcGFzc19wcmVzZXJ2ZWQgZWxzZSAicmVqZWN0ZWRfc3VwcG9ydF9jb250cm9sX3Zpb2xhdGlvbiIsCiAgICB9CgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHM9W10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VULyJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGUpKQogICAgICAgIHJldHVybiBwYXRocwogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHA9VklTL25hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLGRwaT0xODAsYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCIvIikpCgogICAgY291bnRzPXN1bW1hcnlbInN0YXR1c19jb3VudHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LDQpKQogICAgcGx0LmJhcihsaXN0KGNvdW50cy5rZXlzKCkpLCBsaXN0KGNvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnRlcmZhY3R1YWwgY291bnQiKQogICAgcGx0LnRpdGxlKCJDYWxpYnJhdGlvbiBDb3VudGVyZmFjdHVhbCBTdGF0dXMiKQogICAgc2F2ZSgiY291bnRlcmZhY3R1YWxfc3RhdHVzX2NvdW50cy5wbmciKQoKICAgIGRyaWZ0PXN1bW1hcnlbImRyaWZ0X2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsNCkpCiAgICBwbHQuYmFyKGxpc3QoZHJpZnQua2V5cygpKSwgbGlzdChkcmlmdC52YWx1ZXMoKSkpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBwbHQudGl0bGUoIkN1cnJlbnQgdnMgUHJvcG9zZWQgRHJpZnQiKQogICAgc2F2ZSgiY291bnRlcmZhY3R1YWxfZHJpZnRfY291bnRzLnBuZyIpCgogICAgdmFscz1bclsiZGlhZ25vc3RpY19hdmVyYWdlIl0gZm9yIHIgaW4gc3VtbWFyeVsiY291bnRlcmZhY3R1YWxfcm93cyJdIGlmIGlzaW5zdGFuY2Uoci5nZXQoImRpYWdub3N0aWNfYXZlcmFnZSIpLCAoaW50LGZsb2F0KSldCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsNCkpCiAgICBwbHQuYmFyKFtzdHIoaSsxKSBmb3IgaSBpbiByYW5nZShsZW4odmFscykpXSwgdmFscykKICAgIHBsdC5heGhsaW5lKHN1bW1hcnlbInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCJdLCBsaW5lc3R5bGU9Ii0tIikKICAgIHBsdC54bGFiZWwoIkNvdW50ZXJmYWN0dWFsIikKICAgIHBsdC55bGFiZWwoIkRpYWdub3N0aWMgYXZlcmFnZSIpCiAgICBwbHQudGl0bGUoIkNvdW50ZXJmYWN0dWFsIERpYWdub3N0aWMgU3VwcG9ydCB2cyBUaHJlc2hvbGQiKQogICAgc2F2ZSgiY291bnRlcmZhY3R1YWxfc3VwcG9ydF90aHJlc2hvbGQucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzdW1tYXJ5KToKICAgIGxpbmVzPVsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC41LjYgQ2FsaWJyYXRpb24gQ291bnRlcmZhY3R1YWxzIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gU2VsZWN0ZWQgcmVwb3J0LW9ubHkgdGhyZXNob2xkOiBge3N1bW1hcnlbJ3NlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCddfWAiLAogICAgICAgIGYiLSBDb3VudGVyZmFjdHVhbCBjb3VudDogYHtzdW1tYXJ5Wydjb3VudGVyZmFjdHVhbF9jb3VudCddfWAiLAogICAgICAgIGYiLSBTYWZlIHJlcG9ydC1vbmx5IGNhbmRpZGF0ZXM6IGB7c3VtbWFyeVsnc2FmZV9jYW5kaWRhdGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gUmVqZWN0ZWQgY291bnRlcmZhY3R1YWxzOiBge3N1bW1hcnlbJ3JlamVjdGVkX2NvdW50J119YCIsCiAgICAgICAgZiItIERyaWZ0IGNvdW50OiBge3N1bW1hcnlbJ2NvdW50ZXJmYWN0dWFsX2RyaWZ0X2NvdW50J119YCIsCiAgICAgICAgZiItIEZpbmFsIHJlY29tbWVuZGF0aW9uOiBge3N1bW1hcnlbJ2ZpbmFsX3JlY29tbWVuZGF0aW9uJ119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c3VtbWFyeVsnbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBQb2xpY3kgZW5mb3JjZWQ6IGB7c3VtbWFyeVsncG9saWN5X2VuZm9yY2VkJ119YCIsCiAgICAgICAgZiItIENhbGlicmF0aW9uIGFwcGxpZWQ6IGB7c3VtbWFyeVsnY2FsaWJyYXRpb25fYXBwbGllZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDb3VudGVyZmFjdHVhbCBSb3dzIiwKICAgICAgICAiIiwKICAgICAgICAifCBDb250cm9sIHwgR2F0ZSBwYWlyIHwgRGlhZ25vc3RpYyB8IEN1cnJlbnQgYmVoYXZpb3IgfCBQcm9wb3NlZCBiZWhhdmlvciB8IERyaWZ0IHwgU3VwcG9ydCBwcmVzZXJ2ZWQgfCBTdGF0dXMgfCIsCiAgICAgICAgInwtLS18LS0tfC0tLTp8LS0tfC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHIgaW4gc3VtbWFyeVsiY291bnRlcmZhY3R1YWxfcm93cyJdOgogICAgICAgIGxpbmVzLmFwcGVuZCgKICAgICAgICAgICAgZiJ8IGB7clsnY29udHJvbF9pZCddfWAgfCBge3JbJ2dhdGVfcGFpciddfWAgfCBge3JbJ2RpYWdub3N0aWNfYXZlcmFnZSddfWAgfCAiCiAgICAgICAgICAgIGYiYHtyWydjdXJyZW50X2JlaGF2aW9yJ119YCB8IGB7clsncHJvcG9zZWRfcmVwb3J0X29ubHlfYmVoYXZpb3InXX1gIHwgYHtyWydjb3VudGVyZmFjdHVhbF9kcmlmdCddfWAgfCAiCiAgICAgICAgICAgIGYiYHtyWydzdXBwb3J0X3Bhc3NfcHJlc2VydmVkJ119YCB8IGB7clsnY291bnRlcmZhY3R1YWxfc3RhdHVzJ119YCB8IgogICAgICAgICkKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWw9b3MucGF0aC5yZWxwYXRoKFJPT1QvcCwgT1VUKS5yZXBsYWNlKCJcXCIsIi8iKQogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtyZWx9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzdW1tYXJ5WyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgcGxhbj1yanNvbihQTEFOKQogICAgbmVnPXJqc29uKE5FRykKICAgIHRocmVzaG9sZD1wbGFuLmdldCgic2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkIikKICAgIGNvbnRyb2xzPW5lZy5nZXQoIm5lZ2F0aXZlX2NvbnRyb2xzIiwgW10pCiAgICByb3dzPVtzaW11bGF0ZShjLCB0aHJlc2hvbGQpIGZvciBjIGluIGNvbnRyb2xzXQoKICAgIHN0YXR1cz1Db3VudGVyKHJbImNvdW50ZXJmYWN0dWFsX3N0YXR1cyJdIGZvciByIGluIHJvd3MpCiAgICBkcmlmdD1Db3VudGVyKCJkcmlmdCIgaWYgclsiY291bnRlcmZhY3R1YWxfZHJpZnQiXSBlbHNlICJub19kcmlmdCIgZm9yIHIgaW4gcm93cykKICAgIHJlamVjdGVkPXN0YXR1cy5nZXQoInJlamVjdGVkX3N1cHBvcnRfY29udHJvbF92aW9sYXRpb24iLCAwKQogICAgc2FmZT1zdGF0dXMuZ2V0KCJzYWZlX3JlcG9ydF9vbmx5X2NhbmRpZGF0ZSIsIDApCiAgICBmaW5hbCA9ICJjb3VudGVyZmFjdHVhbF9jYW5kaWRhdGVfc2FmZV9mb3JfcmV2aWV3X25vdF9hcHBsaWNhdGlvbiIgaWYgcmVqZWN0ZWQgPT0gMCBlbHNlICJkb19ub3RfcmV2aWV3X2NhbGlicmF0aW9uX2NhbmRpZGF0ZV9fc3VwcG9ydF92aW9sYXRpb24iCgogICAgc3VtbWFyeT17CiAgICAgICAgInNjaGVtYSI6InRhdS1zY2FsaW5nLWNhbGlicmF0aW9uLWNvdW50ZXJmYWN0dWFscy12MC41LjYiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOmRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9jYWxpYnJhdGlvbl9wbGFuIjoicmVwb3J0cy9jYWxpYnJhdGlvbl9wbGFuL2xhdGVzdF9kaXNhYmxlZF9jYWxpYnJhdGlvbl9wbGFuLmpzb24iLAogICAgICAgICJpbnB1dF9uZWdhdGl2ZV9jb250cm9scyI6InJlcG9ydHMvbmVnYXRpdmVfY29udHJvbHMvbGF0ZXN0X3N1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMuanNvbiIsCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6dGhyZXNob2xkLAogICAgICAgICJjb3VudGVyZmFjdHVhbF9jb3VudCI6bGVuKHJvd3MpLAogICAgICAgICJzYWZlX2NhbmRpZGF0ZV9jb3VudCI6c2FmZSwKICAgICAgICAicmVqZWN0ZWRfY291bnQiOnJlamVjdGVkLAogICAgICAgICJjb3VudGVyZmFjdHVhbF9kcmlmdF9jb3VudCI6ZHJpZnQuZ2V0KCJkcmlmdCIsMCksCiAgICAgICAgInN0YXR1c19jb3VudHMiOmRpY3Qoc3RhdHVzKSwKICAgICAgICAiZHJpZnRfY291bnRzIjpkaWN0KGRyaWZ0KSwKICAgICAgICAiY291bnRlcmZhY3R1YWxfcm93cyI6cm93cywKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6RmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6RmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOkZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ZmluYWwsCiAgICAgICAgImJvdW5kYXJ5IjoiQ2FsaWJyYXRpb24gY291bnRlcmZhY3R1YWxzIGFyZSBsb2NhbCByZXBvcnQtb25seSBjbGFzc2lmaWVyLWdvdmVybmFuY2Ugc2ltdWxhdGlvbnMuIFRoZXkgZG8gbm90IGNoYW5nZSBjbGFzc2lmaWVyIGJlaGF2aW9yIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjoidjAuNS43IHNob3VsZCBwcm9kdWNlIGEgY291bnRlcmZhY3R1YWwgZGVjaXNpb24gcmVjb3JkIGJlZm9yZSBhbnkgY2xhc3NpZmllciBtdXRhdGlvbiBpcyBkaXNjdXNzZWQuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl09Y2hhcnRzKHN1bW1hcnkpCiAgICB3anNvbihPVVQvImNhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFsc192MF81XzYuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQvImxhdGVzdF9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQvImNhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFsc192MF81XzYubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQvImxhdGVzdF9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjpzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAic2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkIjpzdW1tYXJ5WyJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiXSwKICAgICAgICAiY291bnRlcmZhY3R1YWxfY291bnQiOnN1bW1hcnlbImNvdW50ZXJmYWN0dWFsX2NvdW50Il0sCiAgICAgICAgInNhZmVfY2FuZGlkYXRlX2NvdW50IjpzdW1tYXJ5WyJzYWZlX2NhbmRpZGF0ZV9jb3VudCJdLAogICAgICAgICJyZWplY3RlZF9jb3VudCI6c3VtbWFyeVsicmVqZWN0ZWRfY291bnQiXSwKICAgICAgICAiY291bnRlcmZhY3R1YWxfZHJpZnRfY291bnQiOnN1bW1hcnlbImNvdW50ZXJmYWN0dWFsX2RyaWZ0X2NvdW50Il0sCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjpzdW1tYXJ5WyJmaW5hbF9yZWNvbW1lbmRhdGlvbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjpzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6c3VtbWFyeVsicG9saWN5X2VuZm9yY2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOnN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOmxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjoicmVwb3J0cy9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMvbGF0ZXN0X2NhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscy5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQppZiBfX25hbWVfXz09Il9fbWFpbl9fIjoKICAgIG1haW4oKQo="
write(ROOT/"scripts"/"benchmarks"/"run_calibration_counterfactuals.py", base64.b64decode(runner_b64).decode())

write(ROOT/"reports"/"calibration_counterfactuals"/"README.md", """# Calibration Counterfactual Reports

Current layer: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**

## Purpose

This folder stores report-only counterfactual simulations for the selected disabled calibration threshold.

## Primary command

```powershell
python scripts/benchmarks/run_calibration_counterfactuals.py
```

## README Update Rule

Update this mini README whenever counterfactual schemas, report paths, or threshold behavior changes.

Boundary: calibration counterfactuals are local classifier-governance simulations only.
""")
write(ROOT/"visuals"/"calibration_counterfactuals"/"README.md", """# Calibration Counterfactual Visuals

Current layer: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**

## Purpose

This folder stores charts for report-only calibration counterfactuals.

## README Update Rule

Update this mini README whenever counterfactual chart names or meanings change.

Boundary: counterfactual visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"calibration_counterfactuals"/"v0_5_6"/"README.md", """# v0.5.6 Calibration Counterfactual Charts

Expected charts:

- `counterfactual_status_counts.png`
- `counterfactual_drift_counts.png`
- `counterfactual_support_threshold.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local report-only counterfactual diagnostics only.
""")

# README
p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.5[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.4[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.5 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.6 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.5-ready |", "| Task routing matrix | geometry-aware / v0.5.6-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.5 |", "| Agent contract version sync | current / v0.5.6 |")
if "| Calibration counterfactuals |" not in r:
    r=r.replace("| Calibration plan charts | `visuals/calibration_plan/v0_5_5/` |\n",
                "| Calibration plan charts | `visuals/calibration_plan/v0_5_5/` |\n| Calibration counterfactuals | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` |\n| Calibration counterfactual charts | `visuals/calibration_counterfactuals/v0_5_6/` |\n")
if "python scripts/benchmarks/run_calibration_counterfactuals.py" not in r:
    r=r.replace("python scripts/benchmarks/generate_disabled_calibration_plan.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/generate_disabled_calibration_plan.py\npython scripts/benchmarks/run_calibration_counterfactuals.py\npython scripts/release/validate_release.py")
if "    calibration_counterfactuals/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    calibration_counterfactuals/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    calibration_counterfactuals/\n")
section="""## Calibration Counterfactuals v0.5.6

v0.5.6 simulates the selected disabled calibration threshold without applying it.

Primary command:

```powershell
python scripts/benchmarks/run_calibration_counterfactuals.py
```

Primary outputs:

```text
reports/calibration_counterfactuals/latest_calibration_counterfactuals.json
reports/calibration_counterfactuals/latest_calibration_counterfactuals.md
visuals/calibration_counterfactuals/v0_5_6/
```

This layer compares current behavior against proposed report-only calibrated behavior while preserving support-aware negative controls.

Current lock:

```text
mutation_allowed: false
policy_enforced: false
calibration_applied: false
```

Boundary: calibration counterfactuals are local report-only classifier-governance simulations. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Calibration Counterfactuals v0.5.6" not in r:
    r=r.replace("## Disabled Calibration Plan v0.5.5", section+"## Disabled Calibration Plan v0.5.5",1)
lesson="| L-038 | v0.5.5 selected a report-only calibration threshold, but a threshold is not a classifier change. | Calibration planning can still hide drift unless tested counterfactually. | Any selected calibration threshold must pass report-only counterfactual testing before policy mutation can even be discussed. |"
if "L-038" not in r:
    r=r.replace("| L-037 | v0.5.4 support-aware negative controls passed 6/6. | Passing support controls permit calibration planning, but not calibration application. | A calibration plan may only be drafted after support-aware controls pass, and it must preserve high-support retention as a hard constraint. |\n",
                "| L-037 | v0.5.4 support-aware negative controls passed 6/6. | Passing support controls permit calibration planning, but not calibration application. | A calibration plan may only be drafted after support-aware controls pass, and it must preserve high-support retention as a hard constraint. |\n"+lesson+"\n")
if "| v0.5.6 |" not in r:
    r=r.replace("| v0.5.5 | Disabled calibration plan preserving support-aware retention constraints. |\n",
                "| v0.5.5 | Disabled calibration plan preserving support-aware retention constraints. |\n| v0.5.6 | Calibration counterfactuals for the selected report-only threshold. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**

Recommended goals:

- Convert v0.5.6 counterfactual outcomes into a non-mutating decision record.
- Decide whether the calibration candidate is safe for review, rejected, or needs more controls.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: decision records are local classifier governance only.
""", r, flags=re.S)
write(p,r)

# AGENTS
p=ROOT/"AGENTS.md"; backup(p,"agents"); a=read(p)
a=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**", a)
if "run_calibration_counterfactuals.py" not in a:
    a=a.replace("python scripts/benchmarks/generate_disabled_calibration_plan.py\npython -m unittest discover -s tests",
                "python scripts/benchmarks/generate_disabled_calibration_plan.py\npython scripts/benchmarks/run_calibration_counterfactuals.py\npython -m unittest discover -s tests")
if "| Calibration counterfactual patch |" not in a:
    a=a.replace("| Disabled calibration plan patch | `reports/calibration_plan/`, `visuals/calibration_plan/`, negative controls | calibration plan + release validator; no classifier mutation |\n",
                "| Disabled calibration plan patch | `reports/calibration_plan/`, `visuals/calibration_plan/`, negative controls | calibration plan + release validator; no classifier mutation |\n| Calibration counterfactual patch | `reports/calibration_counterfactuals/`, `visuals/calibration_counterfactuals/`, calibration plan | counterfactual report + release validator; no classifier mutation |\n")
write(p,a)

# route map
p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.6"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["calibration_counterfactuals"]={
    "read_first":["reports/calibration_plan/latest_disabled_calibration_plan.json","reports/negative_controls/latest_support_aware_negative_controls.json"],
    "validate":["python scripts/benchmarks/run_calibration_counterfactuals.py","python scripts/release/validate_release.py"],
    "evidence":["reports/calibration_counterfactuals/latest_calibration_counterfactuals.md","visuals/calibration_counterfactuals/v0_5_6/"],
    "mutation_lock":"Does not change classifier behavior; calibration_applied must remain false."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

# task matrix
p=ROOT/"rcc"/"nexus"/"task_routing_matrix.md"; backup(p,"task_matrix"); m=read(p)
m=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**", m)
if "| Calibration counterfactual patch |" not in m:
    m=m.replace("| Disabled calibration plan patch | outer | validation | governance | negative controls + candidate thresholds | calibration plan + charts + release validator | `reports/calibration_plan/latest_disabled_calibration_plan.md` |\n",
                "| Disabled calibration plan patch | outer | validation | governance | negative controls + candidate thresholds | calibration plan + charts + release validator | `reports/calibration_plan/latest_disabled_calibration_plan.md` |\n| Calibration counterfactual patch | outer | validation | governance | calibration plan + negative controls | counterfactual report + charts + release validator | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` |\n")
write(p,m)

# atlas
p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.6 | Calibration counterfactuals |" not in t:
    t=t.replace("| v0.5.5 | Disabled calibration plan | `python scripts/benchmarks/generate_disabled_calibration_plan.py` | Plans report-only threshold calibration while preserving support retention | `reports/calibration_plan/latest_disabled_calibration_plan.md` | `visuals/calibration_plan/v0_5_5/` |\n",
                "| v0.5.5 | Disabled calibration plan | `python scripts/benchmarks/generate_disabled_calibration_plan.py` | Plans report-only threshold calibration while preserving support retention | `reports/calibration_plan/latest_disabled_calibration_plan.md` | `visuals/calibration_plan/v0_5_5/` |\n| v0.5.6 | Calibration counterfactuals | `python scripts/benchmarks/run_calibration_counterfactuals.py` | Simulates selected calibration candidate without applying classifier mutation | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` | `visuals/calibration_counterfactuals/v0_5_6/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_6_calibration_counterfactuals.md", f"""# TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals

Generated: {NOW}

## Purpose

Run report-only counterfactuals for the selected disabled calibration threshold.

## Adds

- `scripts/benchmarks/run_calibration_counterfactuals.py`
- `reports/calibration_counterfactuals/`
- `visuals/calibration_counterfactuals/v0_5_6/`

## Boundary

Calibration counterfactuals are local classifier-governance simulations only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.6 patch written")
