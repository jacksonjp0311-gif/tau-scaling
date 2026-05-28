
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"approval_gated_replay"/"v0_6_4"/"backups"/f"{p.name}_before_v0_6_4_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_approval_gated_replay_dry_run.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpWQUxJREFUT1IgPSBST09UIC8gInJlcG9ydHMiIC8gImFwcHJvdmFsX3ZhbGlkYXRvciIgLyAibGF0ZXN0X2h1bWFuX2FwcHJvdmFsX3ZhbGlkYXRvci5qc29uIgpSRVBMQVkgPSBST09UIC8gInJlcG9ydHMiIC8gImNhbmRpZGF0ZV9yZXBsYXkiIC8gImxhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX3JlcGxheV9oYXJuZXNzLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5IgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImFwcHJvdmFsX2dhdGVkX3JlcGxheSIgLyAidjBfNl80IgoKRFJZX1JVTl9TVEVQUyA9IFsKICAgICgiYmFzZWxpbmVfY2xhaW1fcmVwbGF5IiwgInB5dGhvbiAtbSB0YXVfc2NhbGluZyBydW4tY2xhaW0gLS1zZWVkIGNvbmZpZ3Mvc2VlZHMvbG9naWNmb2xkaW5nX2NsYWltX2NhcmQuanNvbiIpLAogICAgKCJwcm9tb3Rpb25fcGF0aF9yZXBsYXkiLCAicHl0aG9uIC1tIHRhdV9zY2FsaW5nIHJ1bi1jbGFpbSAtLXNlZWQgY29uZmlncy9zZWVkcy9sb2dpY2ZvbGRpbmdfcHJvbW90aW9uX3BhdGhfY2xhaW1fY2FyZC5qc29uIiksCiAgICAoInN1cHBvcnRfY29udHJvbF9yZXBsYXkiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fc3VwcG9ydF9hd2FyZV9uZWdhdGl2ZV9jb250cm9scy5weSIpLAogICAgKCJjb3VudGVyZmFjdHVhbF9yZXBsYXkiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fY2FsaWJyYXRpb25fY291bnRlcmZhY3R1YWxzLnB5IiksCiAgICAoInJldmlld19zaWdub2ZmX3JlcGxheSIsICJweXRob24gc2NyaXB0cy9iZW5jaG1hcmtzL3J1bl9yZXZpZXdfc2lnbm9mZl9nYXRlLnB5IiksCl0KCmRlZiByanNvbihwKToKICAgIHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQoKZGVmIHdqc29uKHAsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KGpzb24uZHVtcHMoeCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocCwgcyk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQocywgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocCk6CiAgICByZXR1cm4gc3RyKHAucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgZ2F0ZXMgPSB7CiAgICAgICAgImFwcHJvdmFsX3ZhbGlkIjogaW50KHN1bW1hcnlbImFwcHJvdmFsX3ZhbGlkIl0pLAogICAgICAgICJkcnlfcnVuX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsiZHJ5X3J1bl9hbGxvd2VkIl0pLAogICAgICAgICJkcnlfcnVuX2V4ZWN1dGVkIjogaW50KHN1bW1hcnlbImRyeV9ydW5fZXhlY3V0ZWQiXSksCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogaW50KHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVzLmtleXMoKSksIGxpc3QoZ2F0ZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbC1HYXRlZCBSZXBsYXkgU3RhdGUiKQogICAgc2F2ZSgiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5X3N0YXRlLnBuZyIpCgogICAgc3RlcHMgPSBzdW1tYXJ5WyJkcnlfcnVuX3N0ZXBzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oMTAsIDQpKQogICAgcGx0LmJhcihbc1sic3RlcF9pZCJdIGZvciBzIGluIHN0ZXBzXSwgW2ludChzWyJlbGlnaWJsZSJdKSBmb3IgcyBpbiBzdGVwc10pCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTMwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiRWxpZ2libGUgaWYgYXBwcm92ZWQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbC1HYXRlZCBSZXBsYXkgUGxhbm5lZCBTdGVwcyIpCiAgICBzYXZlKCJhcHByb3ZhbF9nYXRlZF9yZXBsYXlfc3RlcHMucG5nIikKCiAgICBzdGF0dXMgPSB7c3VtbWFyeVsiZHJ5X3J1bl9zdGF0dXMiXTogMX0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3Qoc3RhdHVzLmtleXMoKSksIGxpc3Qoc3RhdHVzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBwbHQudGl0bGUoIkFwcHJvdmFsLUdhdGVkIFJlcGxheSBTdGF0dXMiKQogICAgc2F2ZSgiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5X3N0YXR1cy5wbmciKQogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVwb3J0KHMpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNi40IEFwcHJvdmFsLUdhdGVkIFJlcGxheSBEcnktUnVuIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzWydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgRHJ5LVJ1biBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBEcnktcnVuIHN0YXR1czogYHtzWydkcnlfcnVuX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBBcHByb3ZhbCB2YWxpZDogYHtzWydhcHByb3ZhbF92YWxpZCddfWAiLAogICAgICAgIGYiLSBEcnktcnVuIGFsbG93ZWQ6IGB7c1snZHJ5X3J1bl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIERyeS1ydW4gZXhlY3V0ZWQ6IGB7c1snZHJ5X3J1bl9leGVjdXRlZCddfWAiLAogICAgICAgIGYiLSBCcmFuY2ggY3JlYXRlZDogYHtzWydicmFuY2hfY3JlYXRlZCddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3NbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gQXBwbGljYXRpb24gYWxsb3dlZDogYHtzWydhcHBsaWNhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIENhbGlicmF0aW9uIGFwcGxpZWQ6IGB7c1snY2FsaWJyYXRpb25fYXBwbGllZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBQbGFubmVkIFJlcGxheSBTdGVwcyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU3RlcCB8IEVsaWdpYmxlIGlmIGFwcHJvdmVkIHwgRXhlY3V0ZWQgbm93IHwgQ29tbWFuZCB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHN0ZXAgaW4gc1siZHJ5X3J1bl9zdGVwcyJdOgogICAgICAgIGxpbmVzLmFwcGVuZCgKICAgICAgICAgICAgZiJ8IGB7c3RlcFsnc3RlcF9pZCddfWAgfCBge3N0ZXBbJ2VsaWdpYmxlJ119YCB8IGB7c3RlcFsnZXhlY3V0ZWQnXX1gIHwgYHtzdGVwWydjb21tYW5kJ119YCB8IgogICAgICAgICkKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgQmxvY2sgUmVhc29uIiwKICAgICAgICAiIiwKICAgICAgICBzWyJibG9ja19yZWFzb24iXSwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHNbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzWyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgdmFsaWRhdG9yID0gcmpzb24oVkFMSURBVE9SKQogICAgcmVwbGF5ID0gcmpzb24oUkVQTEFZKQoKICAgIGFwcHJvdmFsX3ZhbGlkID0gYm9vbCh2YWxpZGF0b3IuZ2V0KCJhcHByb3ZhbF92YWxpZCIpKQogICAgZHJ5X3J1bl9hbGxvd2VkID0gYXBwcm92YWxfdmFsaWQgYW5kIGJvb2wodmFsaWRhdG9yLmdldCgicmVwbGF5X2FsbG93ZWQiKSkKICAgIGRyeV9ydW5fZXhlY3V0ZWQgPSBGYWxzZQoKICAgIGlmIGRyeV9ydW5fYWxsb3dlZDoKICAgICAgICBzdGF0dXMgPSAiRFJZX1JVTl9SRUFEWV9fTk9UX0VYRUNVVEVEX0JZX0RFRkFVTFQiCiAgICAgICAgYmxvY2tfcmVhc29uID0gIkFwcHJvdmFsIGlzIHZhbGlkLCBidXQgdGhpcyBsYXllciBzdGlsbCByZWNvcmRzIHRoZSBkcnktcnVuIHBsYW4gd2l0aG91dCBjaGFuZ2luZyBydW50aW1lIGJlaGF2aW9yLiIKICAgIGVsc2U6CiAgICAgICAgc3RhdHVzID0gIkRSWV9SVU5fQkxPQ0tFRF9fQVBQUk9WQUxfTk9UX1ZBTElEIgogICAgICAgIGJsb2NrX3JlYXNvbiA9ICJBcHByb3ZhbCB2YWxpZGF0b3IgZGlkIG5vdCBwcm9kdWNlIGFwcHJvdmFsX3ZhbGlkPXRydWUuIFJlcGxheSByZW1haW5zIGJsb2NrZWQuIgoKICAgIHN0ZXBzID0gWwogICAgICAgIHsKICAgICAgICAgICAgInN0ZXBfaWQiOiBzaWQsCiAgICAgICAgICAgICJjb21tYW5kIjogY21kLAogICAgICAgICAgICAiZWxpZ2libGUiOiBib29sKGRyeV9ydW5fYWxsb3dlZCksCiAgICAgICAgICAgICJleGVjdXRlZCI6IEZhbHNlLAogICAgICAgIH0KICAgICAgICBmb3Igc2lkLCBjbWQgaW4gRFJZX1JVTl9TVEVQUwogICAgXQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1hcHByb3ZhbC1nYXRlZC1yZXBsYXktZHJ5LXJ1bi12MC42LjQiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfYXBwcm92YWxfdmFsaWRhdG9yIjogcmVsKFZBTElEQVRPUiksCiAgICAgICAgImlucHV0X2NhbmRpZGF0ZV9yZXBsYXkiOiByZWwoUkVQTEFZKSwKICAgICAgICAiYXBwcm92YWxfdmFsaWQiOiBhcHByb3ZhbF92YWxpZCwKICAgICAgICAiYXBwcm92YWxfZGVjaXNpb24iOiB2YWxpZGF0b3IuZ2V0KCJhcHByb3ZhbF9kZWNpc2lvbiIpLAogICAgICAgICJkcnlfcnVuX2FsbG93ZWQiOiBkcnlfcnVuX2FsbG93ZWQsCiAgICAgICAgImRyeV9ydW5fZXhlY3V0ZWQiOiBkcnlfcnVuX2V4ZWN1dGVkLAogICAgICAgICJkcnlfcnVuX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAiZHJ5X3J1bl9zdGVwcyI6IHN0ZXBzLAogICAgICAgICJibG9ja19yZWFzb24iOiBibG9ja19yZWFzb24sCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiAiS2VlcCByZXBsYXkgYmxvY2tlZCB1bnRpbCBhcHByb3ZhbF92YWxpZCBpcyB0cnVlLiIgaWYgbm90IGRyeV9ydW5fYWxsb3dlZCBlbHNlICJBcHByb3ZhbCBpcyB2YWxpZDsgbmV4dCBsYXllciBtYXkgcnVuIGEgYm91bmRlZCByZXBsYXkgcGxhbiB3aXRob3V0IG11dGF0aW9uLiIsCiAgICAgICAgImJvdW5kYXJ5IjogIkFwcHJvdmFsLWdhdGVkIHJlcGxheSBkcnktcnVucyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIHBsYW5uaW5nIGFydGlmYWN0cy4gVGhleSBkbyBub3QgY3JlYXRlIGJyYW5jaGVzIGJ5IGRlZmF1bHQsIGRvIG5vdCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciwgZG8gbm90IGFwcGx5IGNhbGlicmF0aW9uLCBhbmQgZG8gbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC42LjUgc2hvdWxkIGFkZCBhbiBleHBsaWNpdCBhcHByb3ZhbCBmaXh0dXJlIG9yIGRlbmlhbCBmaXh0dXJlIHZhbGlkYXRvciBiZWZvcmUgYW55IGV4ZWN1dGFibGUgcmVwbGF5IHBhdGguIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5X2RyeV9ydW5fdjBfNl80Lmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9hcHByb3ZhbF9nYXRlZF9yZXBsYXlfZHJ5X3J1bi5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJhcHByb3ZhbF9nYXRlZF9yZXBsYXlfZHJ5X3J1bl92MF82XzQubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2FwcHJvdmFsX2dhdGVkX3JlcGxheV9kcnlfcnVuLm1kIiwgcmVwb3J0KHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiZHJ5X3J1bl9zdGF0dXMiOiBzdW1tYXJ5WyJkcnlfcnVuX3N0YXR1cyJdLAogICAgICAgICJhcHByb3ZhbF92YWxpZCI6IHN1bW1hcnlbImFwcHJvdmFsX3ZhbGlkIl0sCiAgICAgICAgImRyeV9ydW5fYWxsb3dlZCI6IHN1bW1hcnlbImRyeV9ydW5fYWxsb3dlZCJdLAogICAgICAgICJkcnlfcnVuX2V4ZWN1dGVkIjogc3VtbWFyeVsiZHJ5X3J1bl9leGVjdXRlZCJdLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9hcHByb3ZhbF9nYXRlZF9yZXBsYXkvbGF0ZXN0X2FwcHJvdmFsX2dhdGVkX3JlcGxheV9kcnlfcnVuLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT/"reports"/"approval_gated_replay"/"README.md", """# Approval-Gated Replay Reports

Current layer: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**

## Purpose

This folder stores approval-gated replay dry-run reports. If approval is invalid or template-only, replay remains blocked.

## Primary command

```powershell
python scripts/benchmarks/run_approval_gated_replay_dry_run.py
```

## README Update Rule

Update this mini README whenever approval-gated replay schemas, approval gates, or replay rules change.

Boundary: approval-gated replay reports are local classifier-governance planning artifacts only.
""")
write(ROOT/"visuals"/"approval_gated_replay"/"README.md", """# Approval-Gated Replay Visuals

Current layer: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**

## Purpose

This folder stores charts summarizing approval-gated replay state.

## README Update Rule

Update this mini README whenever approval-gated replay chart names or meanings change.

Boundary: approval-gated replay visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"approval_gated_replay"/"v0_6_4"/"README.md", """# v0.6.4 Approval-Gated Replay Charts

Expected charts:

- `approval_gated_replay_state.png`
- `approval_gated_replay_steps.png`
- `approval_gated_replay_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local approval-gated replay diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.3[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.2[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.3 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.4 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.3-ready |", "| Task routing matrix | geometry-aware / v0.6.4-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.3 |", "| Agent contract version sync | current / v0.6.4 |")
if "| Approval-gated replay dry-run |" not in r:
    r=r.replace("| Human approval validator charts | `visuals/approval_validator/v0_6_3/` |\n",
                "| Human approval validator charts | `visuals/approval_validator/v0_6_3/` |\n| Approval-gated replay dry-run | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` |\n| Approval-gated replay charts | `visuals/approval_gated_replay/v0_6_4/` |\n")
if "python scripts/benchmarks/run_approval_gated_replay_dry_run.py" not in r:
    r=r.replace("python scripts/benchmarks/validate_human_approval_artifact.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/validate_human_approval_artifact.py\npython scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython scripts/release/validate_release.py")
if "    approval_gated_replay/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    approval_gated_replay/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    approval_gated_replay/\n")
section="""## Approval-Gated Replay Dry-Run v0.6.4

v0.6.4 attempts the replay gate but keeps replay blocked unless the approval validator reports `approval_valid: true`.

Primary command:

```powershell
python scripts/benchmarks/run_approval_gated_replay_dry_run.py
```

Primary outputs:

```text
reports/approval_gated_replay/latest_approval_gated_replay_dry_run.json
reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md
visuals/approval_gated_replay/v0_6_4/
```

Current expected lock while approval remains invalid/template-only:

```text
approval_valid: false
dry_run_allowed: false
dry_run_executed: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: approval-gated replay dry-runs are local classifier-governance planning artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Approval-Gated Replay Dry-Run v0.6.4" not in r:
    r=r.replace("## Human Approval Artifact Validator v0.6.3", section+"## Human Approval Artifact Validator v0.6.3",1)
lesson="| L-046 | v0.6.3 rejected template-only approval. | A failed approval validator should produce a blocked replay dry-run rather than silently stopping the lineage. | Approval-gated replay layers must emit explicit blocked reports when approval is invalid, preserving audit continuity without execution. |"
if "L-046" not in r:
    r=r.replace("| L-045 | v0.6.2 created a template, but a template is not approval. | Approval artifacts must be validated before replay can proceed. | Approval validators must reject UNSET/template-only artifacts and keep replay blocked until explicit approval fields pass. |\n",
                "| L-045 | v0.6.2 created a template, but a template is not approval. | Approval artifacts must be validated before replay can proceed. | Approval validators must reject UNSET/template-only artifacts and keep replay blocked until explicit approval fields pass. |\n"+lesson+"\n")
if "| v0.6.4 |" not in r:
    r=r.replace("| v0.6.3 | Human approval artifact validator; rejects UNSET/template-only approval by default. |\n",
                "| v0.6.3 | Human approval artifact validator; rejects UNSET/template-only approval by default. |\n| v0.6.4 | Approval-gated replay dry-run; emits blocked report unless approval validates. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**

Recommended goals:

- Add explicit fixture examples for APPROVE_REPLAY_ONLY, DENY, and REQUEST_MORE_EVIDENCE.
- Validate that denied/template-only states block replay.
- Validate that approval only enables replay planning, not mutation.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_approval_gated_replay_dry_run.py" not in s:
        s=s.replace("python scripts/benchmarks/validate_human_approval_artifact.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/validate_human_approval_artifact.py\npython scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython -m unittest discover -s tests")
        s=s.replace("| Human approval validator patch | `reports/approval_validator/`, `visuals/approval_validator/`, approval artifact | approval validator + release validator; replay blocked unless valid |\n",
                    "| Human approval validator patch | `reports/approval_validator/`, `visuals/approval_validator/`, approval artifact | approval validator + release validator; replay blocked unless valid |\n| Approval-gated replay patch | `reports/approval_gated_replay/`, `visuals/approval_gated_replay/`, approval validator | blocked replay dry-run + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Approval-gated replay patch |" not in s:
        s=s.replace("| Human approval validator patch | outer | validation | governance | approval artifact + replay harness | approval validator + charts + release validator | `reports/approval_validator/latest_human_approval_validator.md` |\n",
                    "| Human approval validator patch | outer | validation | governance | approval artifact + replay harness | approval validator + charts + release validator | `reports/approval_validator/latest_human_approval_validator.md` |\n| Approval-gated replay patch | outer | validation | governance | approval validator + replay harness | blocked replay dry-run + charts + release validator | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.4"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["approval_gated_replay_dry_run"]={
    "read_first":["reports/approval_validator/latest_human_approval_validator.json","reports/candidate_replay/latest_candidate_branch_replay_harness.json"],
    "validate":["python scripts/benchmarks/run_approval_gated_replay_dry_run.py","python scripts/release/validate_release.py"],
    "evidence":["reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md","visuals/approval_gated_replay/v0_6_4/"],
    "mutation_lock":"Emits blocked report when approval invalid; no branch creation or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.4 | Approval-gated replay dry-run |" not in t:
    t=t.replace("| v0.6.3 | Human approval artifact validator | `python scripts/benchmarks/validate_human_approval_artifact.py` | Rejects template-only approval and keeps replay blocked unless explicit approval validates | `reports/approval_validator/latest_human_approval_validator.md` | `visuals/approval_validator/v0_6_3/` |\n",
                "| v0.6.3 | Human approval artifact validator | `python scripts/benchmarks/validate_human_approval_artifact.py` | Rejects template-only approval and keeps replay blocked unless explicit approval validates | `reports/approval_validator/latest_human_approval_validator.md` | `visuals/approval_validator/v0_6_3/` |\n| v0.6.4 | Approval-gated replay dry-run | `python scripts/benchmarks/run_approval_gated_replay_dry_run.py` | Emits blocked replay report unless approval_valid is true | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` | `visuals/approval_gated_replay/v0_6_4/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_4_approval_gated_replay.md", f"""# TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run

Generated: {NOW}

## Purpose

Run the approval-gated replay boundary. If approval is invalid/template-only, emit a blocked dry-run report.

## Boundary

Approval-gated replay dry-runs are local classifier-governance planning artifacts only. They do not create branches by default, do not mutate classifier behavior, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.4 patch written")
