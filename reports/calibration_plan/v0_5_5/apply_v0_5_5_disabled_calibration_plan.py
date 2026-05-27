
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
        d=ROOT/"reports"/"calibration_plan"/"v0_5_5"/"backups"/f"{p.name}_before_v0_5_5_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
runner_b64="CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zLCBtYXRoCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdCk5FRyA9IFJPT1QgLyAicmVwb3J0cyIgLyAibmVnYXRpdmVfY29udHJvbHMiIC8gImxhdGVzdF9zdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2xzLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FsaWJyYXRpb25fcGxhbiIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJjYWxpYnJhdGlvbl9wbGFuIiAvICJ2MF81XzUiCgpDQU5ESURBVEVfVEhSRVNIT0xEUyA9IFswLjcwLCAwLjc1LCAwLjgwLCAwLjg1LCAwLjkwLCAwLjk1XQoKZGVmIHJqc29uKHApOiByZXR1cm4ganNvbi5sb2FkcyhwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKZGVmIHdqc29uKHAsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KGpzb24uZHVtcHMoeCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIGV2YWx1YXRlX3RocmVzaG9sZCh0aHJlc2hvbGQsIGNvbnRyb2xzKToKICAgIHJldGFpbmVkID0gMAogICAgdmlvbGF0ZWQgPSAwCiAgICBtYXJnaW5zID0gW10KICAgIHJvd3MgPSBbXQogICAgZm9yIGMgaW4gY29udHJvbHM6CiAgICAgICAgZGlhZyA9IGMuZ2V0KCJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSIpCiAgICAgICAgaGlnaCA9IGlzaW5zdGFuY2UoZGlhZywgKGludCwgZmxvYXQpKSBhbmQgZGlhZyA+PSB0aHJlc2hvbGQKICAgICAgICBleHBlY3RlZF9yZXRhaW4gPSBib29sKGMuZ2V0KCJuZWdhdGl2ZV9jb250cm9sX3Bhc3NlZCIpKSBhbmQgYm9vbChjLmdldCgiaGlnaF9zdXBwb3J0X2RldGVjdGVkIikpCiAgICAgICAgIyBUaGUgY2FsaWJyYXRpb24gcGxhbiBpcyBhY2NlcHRhYmxlIG9ubHkgaWYgZXZlcnkgYWxyZWFkeS1wYXNzaW5nIGhpZ2gtc3VwcG9ydAogICAgICAgICMgY29udHJvbCByZW1haW5zIHJldGFpbmVkIHVuZGVyIHRoZSBjYW5kaWRhdGUgdGhyZXNob2xkLgogICAgICAgIHByZXNlcnZlcyA9IChub3QgZXhwZWN0ZWRfcmV0YWluKSBvciBoaWdoCiAgICAgICAgaWYgZXhwZWN0ZWRfcmV0YWluIGFuZCBwcmVzZXJ2ZXM6CiAgICAgICAgICAgIHJldGFpbmVkICs9IDEKICAgICAgICBpZiBleHBlY3RlZF9yZXRhaW4gYW5kIG5vdCBwcmVzZXJ2ZXM6CiAgICAgICAgICAgIHZpb2xhdGVkICs9IDEKICAgICAgICBtYXJnaW4gPSBOb25lIGlmIG5vdCBpc2luc3RhbmNlKGRpYWcsIChpbnQsIGZsb2F0KSkgZWxzZSByb3VuZChkaWFnIC0gdGhyZXNob2xkLCA2KQogICAgICAgIGlmIG1hcmdpbiBpcyBub3QgTm9uZToKICAgICAgICAgICAgbWFyZ2lucy5hcHBlbmQobWFyZ2luKQogICAgICAgIHJvd3MuYXBwZW5kKHsKICAgICAgICAgICAgImNvbnRyb2xfaWQiOiBjLmdldCgiY29udHJvbF9pZCIpLAogICAgICAgICAgICAiZ2F0ZV9wYWlyIjogYy5nZXQoImdhdGVfcGFpciIpLAogICAgICAgICAgICAiZGlhZ25vc3RpY19hdmVyYWdlIjogZGlhZywKICAgICAgICAgICAgInRocmVzaG9sZCI6IHRocmVzaG9sZCwKICAgICAgICAgICAgImV4cGVjdGVkX3JldGFpbiI6IGV4cGVjdGVkX3JldGFpbiwKICAgICAgICAgICAgInByZXNlcnZlc19yZXRlbnRpb24iOiBwcmVzZXJ2ZXMsCiAgICAgICAgICAgICJtYXJnaW4iOiBtYXJnaW4sCiAgICAgICAgfSkKICAgIHJldHVybiB7CiAgICAgICAgInRocmVzaG9sZCI6IHRocmVzaG9sZCwKICAgICAgICAicmV0YWluZWRfY29udHJvbF9jb3VudCI6IHJldGFpbmVkLAogICAgICAgICJ2aW9sYXRpb25fY291bnQiOiB2aW9sYXRlZCwKICAgICAgICAibWluaW11bV9tYXJnaW4iOiBtaW4obWFyZ2lucykgaWYgbWFyZ2lucyBlbHNlIE5vbmUsCiAgICAgICAgInJvd3MiOiByb3dzLAogICAgICAgICJjYW5kaWRhdGVfc3RhdHVzIjogImFkbWlzc2libGVfcmVwb3J0X29ubHkiIGlmIHZpb2xhdGVkID09IDAgZWxzZSAicmVqZWN0ZWRfcmV0ZW50aW9uX3Zpb2xhdGlvbiIsCiAgICB9CgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQoc3RyKHAucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSkKCiAgICByZXN1bHRzID0gc3VtbWFyeVsidGhyZXNob2xkX3Jlc3VsdHMiXQogICAgbGFiZWxzID0gW3N0cihyWyJ0aHJlc2hvbGQiXSkgZm9yIHIgaW4gcmVzdWx0c10KCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksNCkpCiAgICBwbHQuYmFyKGxhYmVscywgW3JbInJldGFpbmVkX2NvbnRyb2xfY291bnQiXSBmb3IgciBpbiByZXN1bHRzXSkKICAgIHBsdC54bGFiZWwoIkNhbmRpZGF0ZSB0aHJlc2hvbGQiKQogICAgcGx0LnlsYWJlbCgiUmV0YWluZWQgY29udHJvbHMiKQogICAgcGx0LnRpdGxlKCJIaWdoLVN1cHBvcnQgUmV0ZW50aW9uIGJ5IENhbmRpZGF0ZSBUaHJlc2hvbGQiKQogICAgc2F2ZSgiY2FsaWJyYXRpb25fcmV0ZW50aW9uX2J5X3RocmVzaG9sZC5wbmciKQoKICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSw0KSkKICAgIHBsdC5iYXIobGFiZWxzLCBbclsidmlvbGF0aW9uX2NvdW50Il0gZm9yIHIgaW4gcmVzdWx0c10pCiAgICBwbHQueGxhYmVsKCJDYW5kaWRhdGUgdGhyZXNob2xkIikKICAgIHBsdC55bGFiZWwoIlJldGVudGlvbiB2aW9sYXRpb25zIikKICAgIHBsdC50aXRsZSgiUmV0ZW50aW9uIFZpb2xhdGlvbnMgYnkgQ2FuZGlkYXRlIFRocmVzaG9sZCIpCiAgICBzYXZlKCJjYWxpYnJhdGlvbl92aW9sYXRpb25fYnlfdGhyZXNob2xkLnBuZyIpCgogICAgbWFyZ2lucyA9IFtyWyJtaW5pbXVtX21hcmdpbiJdIGlmIHJbIm1pbmltdW1fbWFyZ2luIl0gaXMgbm90IE5vbmUgZWxzZSAwIGZvciByIGluIHJlc3VsdHNdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksNCkpCiAgICBwbHQuYmFyKGxhYmVscywgbWFyZ2lucykKICAgIHBsdC54bGFiZWwoIkNhbmRpZGF0ZSB0aHJlc2hvbGQiKQogICAgcGx0LnlsYWJlbCgiTWluaW11bSBzdXBwb3J0IG1hcmdpbiIpCiAgICBwbHQudGl0bGUoIk1pbmltdW0gU3VwcG9ydCBNYXJnaW4gYnkgVGhyZXNob2xkIikKICAgIHNhdmUoImNhbGlicmF0aW9uX21pbmltdW1fbWFyZ2luLnBuZyIpCgogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVwb3J0KHN1bW1hcnkpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNS41IERpc2FibGVkIENhbGlicmF0aW9uIFBsYW4iLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBTb3VyY2UgbmVnYXRpdmUgY29udHJvbHM6IGB7c3VtbWFyeVsnc291cmNlX25lZ2F0aXZlX2NvbnRyb2xfY291bnQnXX1gIiwKICAgICAgICBmIi0gUGFzc2luZyBzb3VyY2UgY29udHJvbHM6IGB7c3VtbWFyeVsnc291cmNlX3Bhc3NlZF9jb250cm9sX2NvdW50J119YCIsCiAgICAgICAgZiItIENhbmRpZGF0ZSB0aHJlc2hvbGRzOiBge3N1bW1hcnlbJ2NhbmRpZGF0ZV90aHJlc2hvbGRfY291bnQnXX1gIiwKICAgICAgICBmIi0gQWRtaXNzaWJsZSByZXBvcnQtb25seSB0aHJlc2hvbGRzOiBge3N1bW1hcnlbJ2FkbWlzc2libGVfdGhyZXNob2xkX2NvdW50J119YCIsCiAgICAgICAgZiItIFJlamVjdGVkIHRocmVzaG9sZHM6IGB7c3VtbWFyeVsncmVqZWN0ZWRfdGhyZXNob2xkX2NvdW50J119YCIsCiAgICAgICAgZiItIFNlbGVjdGVkIHJlcG9ydC1vbmx5IHRocmVzaG9sZDogYHtzdW1tYXJ5WydzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQnXX1gIiwKICAgICAgICBmIi0gRmluYWwgcmVjb21tZW5kYXRpb246IGB7c3VtbWFyeVsnZmluYWxfcmVjb21tZW5kYXRpb24nXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzdW1tYXJ5Wydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgVGhyZXNob2xkIFJlc3VsdHMiLAogICAgICAgICIiLAogICAgICAgICJ8IFRocmVzaG9sZCB8IFJldGFpbmVkIGNvbnRyb2xzIHwgVmlvbGF0aW9ucyB8IE1pbmltdW0gbWFyZ2luIHwgU3RhdHVzIHwiLAogICAgICAgICJ8LS0tOnwtLS06fC0tLTp8LS0tOnwtLS18IiwKICAgIF0KICAgIGZvciByIGluIHN1bW1hcnlbInRocmVzaG9sZF9yZXN1bHRzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCB7clsndGhyZXNob2xkJ119IHwge3JbJ3JldGFpbmVkX2NvbnRyb2xfY291bnQnXX0gfCB7clsndmlvbGF0aW9uX2NvdW50J119IHwge3JbJ21pbmltdW1fbWFyZ2luJ119IHwgYHtyWydjYW5kaWRhdGVfc3RhdHVzJ119YCB8IikKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe3JlbH0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBuZWcgPSByanNvbihORUcpCiAgICBjb250cm9scyA9IG5lZy5nZXQoIm5lZ2F0aXZlX2NvbnRyb2xzIiwgW10pCiAgICBwYXNzZWQgPSBbYyBmb3IgYyBpbiBjb250cm9scyBpZiBjLmdldCgibmVnYXRpdmVfY29udHJvbF9wYXNzZWQiKV0KCiAgICByZXN1bHRzID0gW2V2YWx1YXRlX3RocmVzaG9sZCh0LCBjb250cm9scykgZm9yIHQgaW4gQ0FORElEQVRFX1RIUkVTSE9MRFNdCiAgICBhZG1pc3NpYmxlID0gW3IgZm9yIHIgaW4gcmVzdWx0cyBpZiByWyJjYW5kaWRhdGVfc3RhdHVzIl0gPT0gImFkbWlzc2libGVfcmVwb3J0X29ubHkiXQoKICAgICMgQ29uc2VydmF0aXZlIHNlbGVjdGlvbjogYW1vbmcgYWRtaXNzaWJsZSB0aHJlc2hvbGRzLCB1c2UgdGhlIGhpZ2hlc3QgdGhyZXNob2xkIHRoYXQKICAgICMgcHJlc2VydmVzIGFsbCBwYXNzaW5nIHN1cHBvcnQgY29udHJvbHMuIElmIG5vbmUsIG5vIGNhbGlicmF0aW9uIGNhbmRpZGF0ZSBpcyBhbGxvd2VkLgogICAgc2VsZWN0ZWQgPSBhZG1pc3NpYmxlWy0xXVsidGhyZXNob2xkIl0gaWYgYWRtaXNzaWJsZSBlbHNlIE5vbmUKICAgIGZpbmFsID0gImRyYWZ0X3JlcG9ydF9vbmx5X2NhbGlicmF0aW9uX2NhbmRpZGF0ZV9wcmVzZXJ2aW5nX3N1cHBvcnRfY29udHJvbHMiIGlmIHNlbGVjdGVkIGlzIG5vdCBOb25lIGVsc2UgImRvX25vdF9jYWxpYnJhdGVfX3N1cHBvcnRfcmV0ZW50aW9uX3Zpb2xhdGlvbiIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctZGlzYWJsZWQtY2FsaWJyYXRpb24tcGxhbi12MC41LjUiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfbmVnYXRpdmVfY29udHJvbHMiOiAicmVwb3J0cy9uZWdhdGl2ZV9jb250cm9scy9sYXRlc3Rfc3VwcG9ydF9hd2FyZV9uZWdhdGl2ZV9jb250cm9scy5qc29uIiwKICAgICAgICAic291cmNlX25lZ2F0aXZlX2NvbnRyb2xfY291bnQiOiBsZW4oY29udHJvbHMpLAogICAgICAgICJzb3VyY2VfcGFzc2VkX2NvbnRyb2xfY291bnQiOiBsZW4ocGFzc2VkKSwKICAgICAgICAiY2FuZGlkYXRlX3RocmVzaG9sZF9jb3VudCI6IGxlbihDQU5ESURBVEVfVEhSRVNIT0xEUyksCiAgICAgICAgImFkbWlzc2libGVfdGhyZXNob2xkX2NvdW50IjogbGVuKGFkbWlzc2libGUpLAogICAgICAgICJyZWplY3RlZF90aHJlc2hvbGRfY291bnQiOiBsZW4ocmVzdWx0cykgLSBsZW4oYWRtaXNzaWJsZSksCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IHNlbGVjdGVkLAogICAgICAgICJ0aHJlc2hvbGRfcmVzdWx0cyI6IHJlc3VsdHMsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiBmaW5hbCwKICAgICAgICAiYm91bmRhcnkiOiAiRGlzYWJsZWQgY2FsaWJyYXRpb24gcGxhbm5pbmcgaXMgbG9jYWwgcmVwb3J0LW9ubHkgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGFuYWx5c2lzLiBJdCBkb2VzIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciBhbmQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjUuNiBzaG91bGQgcnVuIGNhbGlicmF0aW9uIGNvdW50ZXJmYWN0dWFscyB3aXRob3V0IGFwcGx5aW5nIGNsYXNzaWZpZXIgbXV0YXRpb24uIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJkaXNhYmxlZF9jYWxpYnJhdGlvbl9wbGFuX3YwXzVfNS5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfZGlzYWJsZWRfY2FsaWJyYXRpb25fcGxhbi5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJkaXNhYmxlZF9jYWxpYnJhdGlvbl9wbGFuX3YwXzVfNS5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfZGlzYWJsZWRfY2FsaWJyYXRpb25fcGxhbi5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInNvdXJjZV9uZWdhdGl2ZV9jb250cm9sX2NvdW50Ijogc3VtbWFyeVsic291cmNlX25lZ2F0aXZlX2NvbnRyb2xfY291bnQiXSwKICAgICAgICAic291cmNlX3Bhc3NlZF9jb250cm9sX2NvdW50Ijogc3VtbWFyeVsic291cmNlX3Bhc3NlZF9jb250cm9sX2NvdW50Il0sCiAgICAgICAgImNhbmRpZGF0ZV90aHJlc2hvbGRfY291bnQiOiBzdW1tYXJ5WyJjYW5kaWRhdGVfdGhyZXNob2xkX2NvdW50Il0sCiAgICAgICAgImFkbWlzc2libGVfdGhyZXNob2xkX2NvdW50Ijogc3VtbWFyeVsiYWRtaXNzaWJsZV90aHJlc2hvbGRfY291bnQiXSwKICAgICAgICAicmVqZWN0ZWRfdGhyZXNob2xkX2NvdW50Ijogc3VtbWFyeVsicmVqZWN0ZWRfdGhyZXNob2xkX2NvdW50Il0sCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IHN1bW1hcnlbInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IHN1bW1hcnlbImZpbmFsX3JlY29tbWVuZGF0aW9uIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvY2FsaWJyYXRpb25fcGxhbi9sYXRlc3RfZGlzYWJsZWRfY2FsaWJyYXRpb25fcGxhbi5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo="
write(ROOT/"scripts"/"benchmarks"/"generate_disabled_calibration_plan.py", base64.b64decode(runner_b64).decode())

write(ROOT/"reports"/"calibration_plan"/"README.md", """# Disabled Calibration Plan Reports

Current layer: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**

## Purpose

This folder stores report-only calibration planning surfaces that must preserve support-aware negative-control retention.

## Primary command

```powershell
python scripts/benchmarks/generate_disabled_calibration_plan.py
```

## README Update Rule

Update this mini README whenever calibration-plan schemas, threshold sweeps, or report paths change.

Boundary: disabled calibration planning is local classifier-governance analysis only.
""")
write(ROOT/"visuals"/"calibration_plan"/"README.md", """# Disabled Calibration Plan Visuals

Current layer: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**

## Purpose

This folder stores charts for report-only calibration planning.

## README Update Rule

Update this mini README whenever calibration chart names or meanings change.

Boundary: calibration visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"calibration_plan"/"v0_5_5"/"README.md", """# v0.5.5 Disabled Calibration Plan Charts

Expected charts:

- `calibration_retention_by_threshold.png`
- `calibration_violation_by_threshold.png`
- `calibration_minimum_margin.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local report-only calibration diagnostics only.
""")

# README
p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.4[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.3[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.4 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.5 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.4-ready |", "| Task routing matrix | geometry-aware / v0.5.5-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.4 |", "| Agent contract version sync | current / v0.5.5 |")
if "| Disabled calibration plan |" not in r:
    r=r.replace("| Support-aware control charts | `visuals/negative_controls/v0_5_4/` |\n",
                "| Support-aware control charts | `visuals/negative_controls/v0_5_4/` |\n| Disabled calibration plan | `reports/calibration_plan/latest_disabled_calibration_plan.md` |\n| Calibration plan charts | `visuals/calibration_plan/v0_5_5/` |\n")
if "python scripts/benchmarks/generate_disabled_calibration_plan.py" not in r:
    r=r.replace("python scripts/benchmarks/run_support_aware_negative_controls.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_support_aware_negative_controls.py\npython scripts/benchmarks/generate_disabled_calibration_plan.py\npython scripts/release/validate_release.py")
if "    calibration_plan/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    calibration_plan/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    calibration_plan/\n")
section="""## Disabled Calibration Plan v0.5.5

v0.5.5 drafts a report-only calibration plan after v0.5.4 support-aware negative controls passed.

Primary command:

```powershell
python scripts/benchmarks/generate_disabled_calibration_plan.py
```

Primary outputs:

```text
reports/calibration_plan/latest_disabled_calibration_plan.json
reports/calibration_plan/latest_disabled_calibration_plan.md
visuals/calibration_plan/v0_5_5/
```

This layer compares candidate thresholds against high-support retention constraints. It does not apply calibration.

Current lock:

```text
mutation_allowed: false
policy_enforced: false
calibration_applied: false
```

Boundary: disabled calibration planning is local report-only classifier-governance analysis. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Disabled Calibration Plan v0.5.5" not in r:
    r=r.replace("## Support-Aware Negative Controls v0.5.4", section+"## Support-Aware Negative Controls v0.5.4",1)
lesson="| L-037 | v0.5.4 support-aware negative controls passed 6/6. | Passing support controls permit calibration planning, but not calibration application. | A calibration plan may only be drafted after support-aware controls pass, and it must preserve high-support retention as a hard constraint. |"
if "L-037" not in r:
    r=r.replace("| L-036 | v0.5.3 converted all six blocked cases into support-aware negative-control tasks. | Remediation planning is not enough; high-support retention must be tested as a disabled/report-only control. | Before calibration or policy design, high-support downgrade pressure must pass support-aware negative controls with mutation disabled. |\n",
                "| L-036 | v0.5.3 converted all six blocked cases into support-aware negative-control tasks. | Remediation planning is not enough; high-support retention must be tested as a disabled/report-only control. | Before calibration or policy design, high-support downgrade pressure must pass support-aware negative controls with mutation disabled. |\n"+lesson+"\n")
if "| v0.5.5 |" not in r:
    r=r.replace("| v0.5.4 | Support-aware negative controls for high-support blocked downgrade candidates. |\n",
                "| v0.5.4 | Support-aware negative controls for high-support blocked downgrade candidates. |\n| v0.5.5 | Disabled calibration plan preserving support-aware retention constraints. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**

Recommended goals:

- Run report-only counterfactuals for the selected disabled calibration threshold.
- Compare current behavior vs proposed behavior without applying mutation.
- Preserve all support-aware negative-control passes.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: counterfactuals are local classifier governance only.
""", r, flags=re.S)
write(p,r)

# AGENTS
p=ROOT/"AGENTS.md"; backup(p,"agents"); a=read(p)
a=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**", a)
if "generate_disabled_calibration_plan.py" not in a:
    a=a.replace("python scripts/benchmarks/run_support_aware_negative_controls.py\npython -m unittest discover -s tests",
                "python scripts/benchmarks/run_support_aware_negative_controls.py\npython scripts/benchmarks/generate_disabled_calibration_plan.py\npython -m unittest discover -s tests")
if "| Disabled calibration plan patch |" not in a:
    a=a.replace("| Support-aware negative-control patch | `reports/negative_controls/`, `visuals/negative_controls/`, remediation tasks | negative-control report + release validator; no classifier mutation |\n",
                "| Support-aware negative-control patch | `reports/negative_controls/`, `visuals/negative_controls/`, remediation tasks | negative-control report + release validator; no classifier mutation |\n| Disabled calibration plan patch | `reports/calibration_plan/`, `visuals/calibration_plan/`, negative controls | calibration plan + release validator; no classifier mutation |\n")
write(p,a)

# route map
p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.5"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["disabled_calibration_plan"]={
    "read_first":["reports/negative_controls/latest_support_aware_negative_controls.json"],
    "validate":["python scripts/benchmarks/generate_disabled_calibration_plan.py","python scripts/release/validate_release.py"],
    "evidence":["reports/calibration_plan/latest_disabled_calibration_plan.md","visuals/calibration_plan/v0_5_5/"],
    "mutation_lock":"Does not change classifier behavior; calibration_applied must remain false."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

# task matrix
p=ROOT/"rcc"/"nexus"/"task_routing_matrix.md"; backup(p,"task_matrix"); m=read(p)
m=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**", m)
if "| Disabled calibration plan patch |" not in m:
    m=m.replace("| Support-aware negative-control patch | outer | validation | governance | remediation tasks + cause cards | negative-control report + charts + release validator | `reports/negative_controls/latest_support_aware_negative_controls.md` |\n",
                "| Support-aware negative-control patch | outer | validation | governance | remediation tasks + cause cards | negative-control report + charts + release validator | `reports/negative_controls/latest_support_aware_negative_controls.md` |\n| Disabled calibration plan patch | outer | validation | governance | negative controls + candidate thresholds | calibration plan + charts + release validator | `reports/calibration_plan/latest_disabled_calibration_plan.md` |\n")
write(p,m)

# atlas
p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.5 | Disabled calibration plan |" not in t:
    t=t.replace("| v0.5.4 | Support-aware negative controls | `python scripts/benchmarks/run_support_aware_negative_controls.py` | Tests high-support retention before calibration or policy design | `reports/negative_controls/latest_support_aware_negative_controls.md` | `visuals/negative_controls/v0_5_4/` |\n",
                "| v0.5.4 | Support-aware negative controls | `python scripts/benchmarks/run_support_aware_negative_controls.py` | Tests high-support retention before calibration or policy design | `reports/negative_controls/latest_support_aware_negative_controls.md` | `visuals/negative_controls/v0_5_4/` |\n| v0.5.5 | Disabled calibration plan | `python scripts/benchmarks/generate_disabled_calibration_plan.py` | Plans report-only threshold calibration while preserving support retention | `reports/calibration_plan/latest_disabled_calibration_plan.md` | `visuals/calibration_plan/v0_5_5/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_5_disabled_calibration_plan.md", f"""# TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan

Generated: {NOW}

## Purpose

Draft a report-only calibration plan after support-aware negative controls passed.

## Adds

- `scripts/benchmarks/generate_disabled_calibration_plan.py`
- `reports/calibration_plan/`
- `visuals/calibration_plan/v0_5_5/`

## Boundary

Disabled calibration planning is local classifier-governance analysis only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.5 patch written")
