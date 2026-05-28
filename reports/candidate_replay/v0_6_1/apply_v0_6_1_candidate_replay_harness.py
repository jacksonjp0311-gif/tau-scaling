
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"candidate_replay"/"v0_6_1"/"backups"/f"{p.name}_before_v0_6_1_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_candidate_branch_replay_harness.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpDQU5ESURBVEUgPSBST09UIC8gInJlcG9ydHMiIC8gImNhbmRpZGF0ZV9icmFuY2giIC8gImxhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX2dhdGUuanNvbiIKU0lHTk9GRiA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmV2aWV3X3NpZ25vZmYiIC8gImxhdGVzdF9yZXZpZXdfc2lnbm9mZl9nYXRlLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FuZGlkYXRlX3JlcGxheSIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJjYW5kaWRhdGVfcmVwbGF5IiAvICJ2MF82XzEiCgpSRVBMQVlfU1RFUFMgPSBbCiAgICAoImJhc2VsaW5lX2NsYWltIiwgInB5dGhvbiAtbSB0YXVfc2NhbGluZyBydW4tY2xhaW0gLS1zZWVkIGNvbmZpZ3Mvc2VlZHMvbG9naWNmb2xkaW5nX2NsYWltX2NhcmQuanNvbiIpLAogICAgKCJwcm9tb3Rpb25fcGF0aF9jbGFpbSIsICJweXRob24gLW0gdGF1X3NjYWxpbmcgcnVuLWNsYWltIC0tc2VlZCBjb25maWdzL3NlZWRzL2xvZ2ljZm9sZGluZ19wcm9tb3Rpb25fcGF0aF9jbGFpbV9jYXJkLmpzb24iKSwKICAgICgic3VwcG9ydF9jb250cm9scyIsICJweXRob24gc2NyaXB0cy9iZW5jaG1hcmtzL3J1bl9zdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2xzLnB5IiksCiAgICAoImNhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscyIsICJweXRob24gc2NyaXB0cy9iZW5jaG1hcmtzL3J1bl9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMucHkiKSwKICAgICgicmV2aWV3X3NpZ25vZmYiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fcmV2aWV3X3NpZ25vZmZfZ2F0ZS5weSIpLApdCgpkZWYgcmpzb24ocCk6CiAgICByZXR1cm4ganNvbi5sb2FkcyhwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgcmVsKHApOgogICAgcmV0dXJuIHN0cihwLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBjaGFydHMoc3VtbWFyeSk6CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGUpKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICBnYXRlcyA9IHsKICAgICAgICAiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiXSksCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiOiBpbnQoc3VtbWFyeVsiaHVtYW5fYXBwcm92YWxfcHJlc2VudCJdKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsicmVwbGF5X2FsbG93ZWQiXSksCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogaW50KHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVzLmtleXMoKSksIGxpc3QoZ2F0ZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJDYW5kaWRhdGUgUmVwbGF5IEdhdGUgU3RhdGUiKQogICAgc2F2ZSgiY2FuZGlkYXRlX3JlcGxheV9nYXRlX3N0YXRlLnBuZyIpCgogICAgc3RlcHMgPSBzdW1tYXJ5WyJyZXBsYXlfc3RlcHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpCiAgICBwbHQuYmFyKFtzWyJzdGVwX2lkIl0gZm9yIHMgaW4gc3RlcHNdLCBbaW50KHNbImluY2x1ZGVkIl0pIGZvciBzIGluIHN0ZXBzXSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MzAsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJJbmNsdWRlZCIpCiAgICBwbHQudGl0bGUoIlJlcGxheSBIYXJuZXNzIFBsYW5uZWQgU3RlcHMiKQogICAgc2F2ZSgiY2FuZGlkYXRlX3JlcGxheV9zdGVwcy5wbmciKQoKICAgIGNsYXNzZXMgPSB7c3VtbWFyeVsicmVwbGF5X3N0YXR1cyJdOiAxfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChjbGFzc2VzLmtleXMoKSksIGxpc3QoY2xhc3Nlcy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJDYW5kaWRhdGUgUmVwbGF5IFN0YXR1cyIpCiAgICBzYXZlKCJjYW5kaWRhdGVfcmVwbGF5X3N0YXR1cy5wbmciKQogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVwb3J0KHMpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNi4xIENhbmRpZGF0ZSBCcmFuY2ggUmVwbGF5IEhhcm5lc3MiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBSZXBsYXkgR2F0ZSBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBSZXBsYXkgc3RhdHVzOiBge3NbJ3JlcGxheV9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gUmVwbGF5IGFsbG93ZWQ6IGB7c1sncmVwbGF5X2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gSHVtYW4gYXBwcm92YWwgcHJlc2VudDogYHtzWydodW1hbl9hcHByb3ZhbF9wcmVzZW50J119YCIsCiAgICAgICAgZiItIEJyYW5jaCBwcm9wb3NhbCBhbGxvd2VkOiBge3NbJ2JyYW5jaF9wcm9wb3NhbF9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEJyYW5jaCBjcmVhdGVkOiBge3NbJ2JyYW5jaF9jcmVhdGVkJ119YCIsCiAgICAgICAgZiItIEFwcGxpY2F0aW9uIGFsbG93ZWQ6IGB7c1snYXBwbGljYXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3NbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gQ2FsaWJyYXRpb24gYXBwbGllZDogYHtzWydjYWxpYnJhdGlvbl9hcHBsaWVkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJlcGxheSBQbGFuIiwKICAgICAgICAiIiwKICAgICAgICAifCBTdGVwIHwgSW5jbHVkZWQgfCBDb21tYW5kIHwgUHVycG9zZSB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHN0ZXAgaW4gc1sicmVwbGF5X3N0ZXBzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKAogICAgICAgICAgICBmInwgYHtzdGVwWydzdGVwX2lkJ119YCB8IGB7c3RlcFsnaW5jbHVkZWQnXX1gIHwgYHtzdGVwWydjb21tYW5kJ119YCB8IHtzdGVwWydwdXJwb3NlJ119IHwiCiAgICAgICAgKQogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBBcHByb3ZhbCBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc1siYXBwcm92YWxfYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHNbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzWyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgY2FuZGlkYXRlID0gcmpzb24oQ0FORElEQVRFKQogICAgc2lnbm9mZiA9IHJqc29uKFNJR05PRkYpCgogICAgcHJvcG9zYWxfYWxsb3dlZCA9IGJvb2woY2FuZGlkYXRlLmdldCgiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiKSkKICAgIGh1bWFuX2FwcHJvdmFsX3ByZXNlbnQgPSBib29sKGNhbmRpZGF0ZS5nZXQoImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiKSkKICAgIHNpZ25vZmZfcmVhZHkgPSBzaWdub2ZmLmdldCgic2lnbm9mZl9zdGF0dXMiKSA9PSAiUkVWSUVXX1NJR05PRkZfUkVBRFlfTk9UX0FQUExJQ0FUSU9OIgoKICAgICMgVGhpcyBoYXJuZXNzIGlzIGludGVudGlvbmFsbHkgYmxvY2tlZCB1bmxlc3MgYSBmdXR1cmUgZXhwbGljaXQgYXBwcm92YWwgYXJ0aWZhY3QgZXhpc3RzLgogICAgcmVwbGF5X2FsbG93ZWQgPSBwcm9wb3NhbF9hbGxvd2VkIGFuZCBzaWdub2ZmX3JlYWR5IGFuZCBodW1hbl9hcHByb3ZhbF9wcmVzZW50CiAgICBzdGF0dXMgPSAiUkVQTEFZX0JMT0NLRURfX0hVTUFOX0FQUFJPVkFMX0FSVElGQUNUX1JFUVVJUkVEIgogICAgaWYgcmVwbGF5X2FsbG93ZWQ6CiAgICAgICAgc3RhdHVzID0gIlJFUExBWV9SRUFEWV9fQVBQUk9WQUxfUFJFU0VOVCIKCiAgICByZXBsYXlfc3RlcHMgPSBbCiAgICAgICAgewogICAgICAgICAgICAic3RlcF9pZCI6IHNpZCwKICAgICAgICAgICAgImNvbW1hbmQiOiBjbWQsCiAgICAgICAgICAgICJpbmNsdWRlZCI6IFRydWUsCiAgICAgICAgICAgICJwdXJwb3NlIjogIlJlcGxheSBiYXNlbGluZS9jYW5kaWRhdGUgZXZpZGVuY2Ugd2l0aG91dCBjaGFuZ2luZyBkZWZhdWx0IHJ1bnRpbWUgYmVoYXZpb3IuIiwKICAgICAgICB9CiAgICAgICAgZm9yIHNpZCwgY21kIGluIFJFUExBWV9TVEVQUwogICAgXQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1jYW5kaWRhdGUtYnJhbmNoLXJlcGxheS1oYXJuZXNzLXYwLjYuMSIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9jYW5kaWRhdGVfYnJhbmNoX2dhdGUiOiAicmVwb3J0cy9jYW5kaWRhdGVfYnJhbmNoL2xhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX2dhdGUuanNvbiIsCiAgICAgICAgImlucHV0X3Jldmlld19zaWdub2ZmIjogInJlcG9ydHMvcmV2aWV3X3NpZ25vZmYvbGF0ZXN0X3Jldmlld19zaWdub2ZmX2dhdGUuanNvbiIsCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IGNhbmRpZGF0ZS5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpLAogICAgICAgICJwcm9wb3NlZF9icmFuY2hfbmFtZSI6IGNhbmRpZGF0ZS5nZXQoInByb3Bvc2VkX2JyYW5jaF9uYW1lIiksCiAgICAgICAgImJyYW5jaF9wcm9wb3NhbF9hbGxvd2VkIjogcHJvcG9zYWxfYWxsb3dlZCwKICAgICAgICAiaHVtYW5fYXBwcm92YWxfcmVxdWlyZWQiOiBUcnVlLAogICAgICAgICJodW1hbl9hcHByb3ZhbF9wcmVzZW50IjogaHVtYW5fYXBwcm92YWxfcHJlc2VudCwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiByZXBsYXlfYWxsb3dlZCwKICAgICAgICAicmVwbGF5X3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVwbGF5X3N0ZXBzIjogcmVwbGF5X3N0ZXBzLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9iZWhhdmlvcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgImFwcHJvdmFsX2JvdW5kYXJ5IjogIlJlcGxheSBpcyBpbnRlbnRpb25hbGx5IGJsb2NrZWQgdW50aWwgYSBzZXBhcmF0ZSBleHBsaWNpdCBodW1hbiBhcHByb3ZhbCBhcnRpZmFjdCBleGlzdHMuIFRoaXMgdjAuNi4xIGxheWVyIHByZXBhcmVzIHRoZSByZXBsYXkgaGFybmVzcyBhbmQgcHJvdmVzIHRoZSBibG9jay4iLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJBZGQgYW4gZXhwbGljaXQgaHVtYW4gYXBwcm92YWwgYXJ0aWZhY3QgYmVmb3JlIHJlcGxheWluZyBhbnkgY2FuZGlkYXRlIGJyYW5jaC4gRG8gbm90IGNyZWF0ZSBhIGJyYW5jaCBvciBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciBmcm9tIHRoaXMgcmVwb3J0LiIsCiAgICAgICAgImJvdW5kYXJ5IjogIkNhbmRpZGF0ZSBicmFuY2ggcmVwbGF5IGhhcm5lc3NlcyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIHBsYW5uaW5nIGFydGlmYWN0cy4gVGhleSBkbyBub3QgY3JlYXRlIGJyYW5jaGVzIGJ5IGRlZmF1bHQsIGRvIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciwgYW5kIGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNi4yIHNob3VsZCBhZGQgYSBodW1hbiBhcHByb3ZhbCBhcnRpZmFjdCB0ZW1wbGF0ZSBvciBleHBsaWNpdCBhcHByb3ZhbC1kZW5pYWwgbGVkZ2VyIGJlZm9yZSByZXBsYXkgY2FuIHByb2NlZWQuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAiY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfaGFybmVzc192MF82XzEuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfcmVwbGF5X2hhcm5lc3MuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAiY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfaGFybmVzc192MF82XzEubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfcmVwbGF5X2hhcm5lc3MubWQiLCByZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJyZXBsYXlfc3RhdHVzIjogc3VtbWFyeVsicmVwbGF5X3N0YXR1cyJdLAogICAgICAgICJicmFuY2hfcHJvcG9zYWxfYWxsb3dlZCI6IHN1bW1hcnlbImJyYW5jaF9wcm9wb3NhbF9hbGxvd2VkIl0sCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3JlcXVpcmVkIjogc3VtbWFyeVsiaHVtYW5fYXBwcm92YWxfcmVxdWlyZWQiXSwKICAgICAgICAiaHVtYW5fYXBwcm92YWxfcHJlc2VudCI6IHN1bW1hcnlbImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9jYW5kaWRhdGVfcmVwbGF5L2xhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX3JlcGxheV9oYXJuZXNzLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT/"reports"/"candidate_replay"/"README.md", """# Candidate Branch Replay Reports

Current layer: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**

## Purpose

This folder stores replay harness plans for candidate branch proposals. Replay remains blocked until explicit human approval exists.

## Primary command

```powershell
python scripts/benchmarks/run_candidate_branch_replay_harness.py
```

## README Update Rule

Update this mini README whenever replay schemas, approval requirements, or replay steps change.

Boundary: candidate replay harnesses are local classifier-governance planning artifacts only.
""")
write(ROOT/"visuals"/"candidate_replay"/"README.md", """# Candidate Branch Replay Visuals

Current layer: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**

## Purpose

This folder stores charts summarizing candidate replay gate state.

## README Update Rule

Update this mini README whenever replay chart names or meanings change.

Boundary: replay visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"candidate_replay"/"v0_6_1"/"README.md", """# v0.6.1 Candidate Replay Charts

Expected charts:

- `candidate_replay_gate_state.png`
- `candidate_replay_steps.png`
- `candidate_replay_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local candidate-replay diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.0[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.9[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.0 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.1 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.0-ready |", "| Task routing matrix | geometry-aware / v0.6.1-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.0 |", "| Agent contract version sync | current / v0.6.1 |")
if "| Candidate replay harness |" not in r:
    r=r.replace("| Candidate branch charts | `visuals/candidate_branch/v0_6_0/` |\n",
                "| Candidate branch charts | `visuals/candidate_branch/v0_6_0/` |\n| Candidate replay harness | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` |\n| Candidate replay charts | `visuals/candidate_replay/v0_6_1/` |\n")
if "python scripts/benchmarks/run_candidate_branch_replay_harness.py" not in r:
    r=r.replace("python scripts/benchmarks/run_candidate_branch_gate.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_candidate_branch_gate.py\npython scripts/benchmarks/run_candidate_branch_replay_harness.py\npython scripts/release/validate_release.py")
if "    candidate_replay/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    candidate_replay/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    candidate_replay/\n")
section="""## Candidate Branch Replay Harness v0.6.1

v0.6.1 prepares the candidate replay harness, but blocks replay until explicit human approval exists.

Primary command:

```powershell
python scripts/benchmarks/run_candidate_branch_replay_harness.py
```

Primary outputs:

```text
reports/candidate_replay/latest_candidate_branch_replay_harness.json
reports/candidate_replay/latest_candidate_branch_replay_harness.md
visuals/candidate_replay/v0_6_1/
```

Current lock:

```text
human_approval_required: true
human_approval_present: false
replay_allowed: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: candidate replay harnesses are local classifier-governance planning artifacts. They do not create branches by default, do not change classifier behavior, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Candidate Branch Replay Harness v0.6.1" not in r:
    r=r.replace("## Human-Approved Candidate Branch Gate v0.6.0", section+"## Human-Approved Candidate Branch Gate v0.6.0",1)
lesson="| L-043 | v0.6.0 allowed a branch proposal but confirmed human approval was absent. | Proposal-readiness can be mistaken for replay-readiness unless replay is separately blocked. | Candidate replay harnesses must remain blocked until an explicit human approval artifact exists. |"
if "L-043" not in r:
    r=r.replace("| L-042 | v0.5.9 passed the signoff gate, but signoff readiness is still not branch creation. | A signoff-ready candidate needs an explicit human approval artifact before branch creation or implementation. | Candidate-branch gates must prepare proposals only; branches require explicit human approval and remain non-mutating by default. |\n",
                "| L-042 | v0.5.9 passed the signoff gate, but signoff readiness is still not branch creation. | A signoff-ready candidate needs an explicit human approval artifact before branch creation or implementation. | Candidate-branch gates must prepare proposals only; branches require explicit human approval and remain non-mutating by default. |\n"+lesson+"\n")
if "| v0.6.1 |" not in r:
    r=r.replace("| v0.6.0 | Human-approved candidate branch gate; proposal only, no branch by default. |\n",
                "| v0.6.0 | Human-approved candidate branch gate; proposal only, no branch by default. |\n| v0.6.1 | Candidate branch replay harness; replay blocked until explicit approval artifact exists. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**

Recommended goals:

- Add an explicit approval/denial artifact template.
- Require a signed local decision before candidate replay can proceed.
- Keep default runtime behavior unchanged.
- Keep `mutation_allowed: false` unless a separate explicit human approval artifact exists.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.0[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_candidate_branch_replay_harness.py" not in s:
        s=s.replace("python scripts/benchmarks/run_candidate_branch_gate.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_candidate_branch_gate.py\npython scripts/benchmarks/run_candidate_branch_replay_harness.py\npython -m unittest discover -s tests")
        s=s.replace("| Candidate branch gate patch | `reports/candidate_branch/`, `visuals/candidate_branch/`, review signoff | proposal gate + release validator; no branch by default |\n",
                    "| Candidate branch gate patch | `reports/candidate_branch/`, `visuals/candidate_branch/`, review signoff | proposal gate + release validator; no branch by default |\n| Candidate replay harness patch | `reports/candidate_replay/`, `visuals/candidate_replay/`, candidate gate | replay harness + release validator; replay blocked by default |\n")
    if name.endswith("task_routing_matrix.md") and "| Candidate replay harness patch |" not in s:
        s=s.replace("| Candidate branch gate patch | outer | governance | review | signoff gate + human approval requirement | candidate branch gate + charts + release validator | `reports/candidate_branch/latest_candidate_branch_gate.md` |\n",
                    "| Candidate branch gate patch | outer | governance | review | signoff gate + human approval requirement | candidate branch gate + charts + release validator | `reports/candidate_branch/latest_candidate_branch_gate.md` |\n| Candidate replay harness patch | outer | validation | governance | candidate gate + signoff | replay harness + charts + release validator | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.1"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["candidate_branch_replay_harness"]={
    "read_first":["reports/candidate_branch/latest_candidate_branch_gate.json","reports/review_signoff/latest_review_signoff_gate.json"],
    "validate":["python scripts/benchmarks/run_candidate_branch_replay_harness.py","python scripts/release/validate_release.py"],
    "evidence":["reports/candidate_replay/latest_candidate_branch_replay_harness.md","visuals/candidate_replay/v0_6_1/"],
    "mutation_lock":"Replay blocked until explicit human approval artifact exists."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.1 | Candidate branch replay harness |" not in t:
    t=t.replace("| v0.6.0 | Human-approved candidate branch gate | `python scripts/benchmarks/run_candidate_branch_gate.py` | Prepares candidate branch proposal only; no branch by default | `reports/candidate_branch/latest_candidate_branch_gate.md` | `visuals/candidate_branch/v0_6_0/` |\n",
                "| v0.6.0 | Human-approved candidate branch gate | `python scripts/benchmarks/run_candidate_branch_gate.py` | Prepares candidate branch proposal only; no branch by default | `reports/candidate_branch/latest_candidate_branch_gate.md` | `visuals/candidate_branch/v0_6_0/` |\n| v0.6.1 | Candidate branch replay harness | `python scripts/benchmarks/run_candidate_branch_replay_harness.py` | Prepares replay plan but blocks replay until explicit approval artifact exists | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` | `visuals/candidate_replay/v0_6_1/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_1_candidate_replay_harness.md", f"""# TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness

Generated: {NOW}

## Purpose

Prepare a candidate branch replay harness while blocking replay until explicit human approval exists.

## Boundary

Candidate replay harnesses are local classifier-governance planning artifacts only. They do not create branches by default, do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.1 patch written")
