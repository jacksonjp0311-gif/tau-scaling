
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"replay_executor"/"v0_6_7"/"backups"/f"{p.name}_before_v0_6_7_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_approval_gated_replay_executor.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpIQU5ET0ZGID0gUk9PVCAvICJyZXBvcnRzIiAvICJsaXZlX2FwcHJvdmFsX2hhbmRvZmYiIC8gImxhdGVzdF9saXZlX2FwcHJvdmFsX2hhbmRvZmZfY2hlY2suanNvbiIKT1VUID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZXBsYXlfZXhlY3V0b3IiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAicmVwbGF5X2V4ZWN1dG9yIiAvICJ2MF82XzciCgpFWEVDVVRPUl9QTEFOID0gWwogICAgKCJiYXNlbGluZV9jbGFpbSIsICJweXRob24gLW0gdGF1X3NjYWxpbmcgcnVuLWNsYWltIC0tc2VlZCBjb25maWdzL3NlZWRzL2xvZ2ljZm9sZGluZ19jbGFpbV9jYXJkLmpzb24iKSwKICAgICgicHJvbW90aW9uX3BhdGhfY2xhaW0iLCAicHl0aG9uIC1tIHRhdV9zY2FsaW5nIHJ1bi1jbGFpbSAtLXNlZWQgY29uZmlncy9zZWVkcy9sb2dpY2ZvbGRpbmdfcHJvbW90aW9uX3BhdGhfY2xhaW1fY2FyZC5qc29uIiksCiAgICAoInN1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fc3VwcG9ydF9hd2FyZV9uZWdhdGl2ZV9jb250cm9scy5weSIpLAogICAgKCJjYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fY2FsaWJyYXRpb25fY291bnRlcmZhY3R1YWxzLnB5IiksCiAgICAoInJldmlld19zaWdub2ZmX2dhdGUiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fcmV2aWV3X3NpZ25vZmZfZ2F0ZS5weSIpLAogICAgKCJjYW5kaWRhdGVfYnJhbmNoX2dhdGUiLCAicHl0aG9uIHNjcmlwdHMvYmVuY2htYXJrcy9ydW5fY2FuZGlkYXRlX2JyYW5jaF9nYXRlLnB5IiksCl0KCmRlZiByanNvbihwKToKICAgIHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQoKZGVmIHdqc29uKHAsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KGpzb24uZHVtcHMoeCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocCwgcyk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQocywgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocCk6CiAgICByZXR1cm4gc3RyKHAucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgZ2F0ZXMgPSB7CiAgICAgICAgImhhbmRvZmZfdmFsaWQiOiBpbnQoc3VtbWFyeVsiaGFuZG9mZl92YWxpZCJdKSwKICAgICAgICAiZXhlY3V0b3JfYWxsb3dlZCI6IGludChzdW1tYXJ5WyJleGVjdXRvcl9hbGxvd2VkIl0pLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBpbnQoc3VtbWFyeVsiZXhlY3V0b3JfcmFuIl0pLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IGludChzdW1tYXJ5WyJicmFuY2hfY3JlYXRlZCJdKSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChnYXRlcy5rZXlzKCkpLCBsaXN0KGdhdGVzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJCb29sZWFuIHN0YXRlIikKICAgIHBsdC50aXRsZSgiQXBwcm92YWwtR2F0ZWQgUmVwbGF5IEV4ZWN1dG9yIFN0YXRlIikKICAgIHNhdmUoInJlcGxheV9leGVjdXRvcl9nYXRlX3N0YXRlLnBuZyIpCgogICAgc3RlcHMgPSBzdW1tYXJ5WyJleGVjdXRvcl9zdGVwcyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIoW3NbInN0ZXBfaWQiXSBmb3IgcyBpbiBzdGVwc10sIFtpbnQoc1sid291bGRfcnVuX2lmX2F1dGhvcml6ZWQiXSkgZm9yIHMgaW4gc3RlcHNdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIldvdWxkIHJ1biBpZiBhdXRob3JpemVkIikKICAgIHBsdC50aXRsZSgiUmVwbGF5IEV4ZWN1dG9yIFBsYW5uZWQgU3RlcHMiKQogICAgc2F2ZSgicmVwbGF5X2V4ZWN1dG9yX3N0ZXBzLnBuZyIpCgogICAgc3RhdHVzID0ge3N1bW1hcnlbImV4ZWN1dG9yX3N0YXR1cyJdOiAxfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChzdGF0dXMua2V5cygpKSwgbGlzdChzdGF0dXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNvdW50IikKICAgIHBsdC50aXRsZSgiUmVwbGF5IEV4ZWN1dG9yIFN0YXR1cyIpCiAgICBzYXZlKCJyZXBsYXlfZXhlY3V0b3Jfc3RhdHVzLnBuZyIpCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZXBvcnQocyk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC42LjcgQXBwcm92YWwtR2F0ZWQgUmVwbGF5IEV4ZWN1dG9yIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzWydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgRXhlY3V0b3IgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gRXhlY3V0b3Igc3RhdHVzOiBge3NbJ2V4ZWN1dG9yX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBIYW5kb2ZmIHN0YXR1czogYHtzWydoYW5kb2ZmX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBIYW5kb2ZmIHZhbGlkOiBge3NbJ2hhbmRvZmZfdmFsaWQnXX1gIiwKICAgICAgICBmIi0gRXhlY3V0b3IgYWxsb3dlZDogYHtzWydleGVjdXRvcl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEV4ZWN1dG9yIHJhbjogYHtzWydleGVjdXRvcl9yYW4nXX1gIiwKICAgICAgICBmIi0gQnJhbmNoIGNyZWF0ZWQ6IGB7c1snYnJhbmNoX2NyZWF0ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEFwcGxpY2F0aW9uIGFsbG93ZWQ6IGB7c1snYXBwbGljYXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBFeGVjdXRvciBQbGFuIiwKICAgICAgICAiIiwKICAgICAgICAifCBTdGVwIHwgV291bGQgcnVuIGlmIGF1dGhvcml6ZWQgfCBFeGVjdXRlZCBub3cgfCBDb21tYW5kIHwiLAogICAgICAgICJ8LS0tfC0tLXwtLS18LS0tfCIsCiAgICBdCiAgICBmb3Igc3RlcCBpbiBzWyJleGVjdXRvcl9zdGVwcyJdOgogICAgICAgIGxpbmVzLmFwcGVuZCgKICAgICAgICAgICAgZiJ8IGB7c3RlcFsnc3RlcF9pZCddfWAgfCBge3N0ZXBbJ3dvdWxkX3J1bl9pZl9hdXRob3JpemVkJ119YCB8IGB7c3RlcFsnZXhlY3V0ZWRfbm93J119YCB8IGB7c3RlcFsnY29tbWFuZCddfWAgfCIKICAgICAgICApCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEJsb2NrIFJlYXNvbiIsCiAgICAgICAgIiIsCiAgICAgICAgc1siYmxvY2tfcmVhc29uIl0sCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENoYXJ0cyIsCiAgICAgICAgIiIsCiAgICBdCiAgICBmb3IgcCBpbiBzWyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc1siYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIGhhbmRvZmYgPSByanNvbihIQU5ET0ZGKQoKICAgIGhhbmRvZmZfdmFsaWQgPSBoYW5kb2ZmLmdldCgiaGFuZG9mZl9zdGF0dXMiKSA9PSAiTElWRV9BUFBST1ZBTF9IQU5ET0ZGX1ZBTElEX0ZPUl9SRVBMQVlfT05MWSIKICAgIGV4ZWN1dG9yX2FsbG93ZWQgPSBib29sKGhhbmRvZmZfdmFsaWQgYW5kIGhhbmRvZmYuZ2V0KCJyZXBsYXlfYWxsb3dlZCIpIGlzIFRydWUpCiAgICBleGVjdXRvcl9yYW4gPSBGYWxzZQoKICAgIGlmIGV4ZWN1dG9yX2FsbG93ZWQ6CiAgICAgICAgZXhlY3V0b3Jfc3RhdHVzID0gIkVYRUNVVE9SX1JFQURZX19OT1RfUlVOX0JZX0RFRkFVTFQiCiAgICAgICAgYmxvY2tfcmVhc29uID0gIkxpdmUgYXBwcm92YWwgaGFuZG9mZiBpcyB2YWxpZC4gVGhpcyBsYXllciBzdGlsbCByZWNvcmRzIGV4ZWN1dG9yIHJlYWRpbmVzcyB3aXRob3V0IHJ1bm5pbmcgY29tbWFuZHMgYnkgZGVmYXVsdC4iCiAgICBlbHNlOgogICAgICAgIGV4ZWN1dG9yX3N0YXR1cyA9ICJFWEVDVVRPUl9CTE9DS0VEX19MSVZFX0FQUFJPVkFMX0hBTkRPRkZfTk9UX1ZBTElEIgogICAgICAgIGJsb2NrX3JlYXNvbiA9ICJMaXZlIGFwcHJvdmFsIGhhbmRvZmYgaXMgbm90IHZhbGlkIGZvciByZXBsYXkuIEV4ZWN1dG9yIHJlbWFpbnMgYmxvY2tlZC4iCgogICAgc3RlcHMgPSBbCiAgICAgICAgewogICAgICAgICAgICAic3RlcF9pZCI6IHNpZCwKICAgICAgICAgICAgImNvbW1hbmQiOiBjbWQsCiAgICAgICAgICAgICJ3b3VsZF9ydW5faWZfYXV0aG9yaXplZCI6IGJvb2woZXhlY3V0b3JfYWxsb3dlZCksCiAgICAgICAgICAgICJleGVjdXRlZF9ub3ciOiBGYWxzZSwKICAgICAgICB9CiAgICAgICAgZm9yIHNpZCwgY21kIGluIEVYRUNVVE9SX1BMQU4KICAgIF0KCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctYXBwcm92YWwtZ2F0ZWQtcmVwbGF5LWV4ZWN1dG9yLXYwLjYuNyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9saXZlX2FwcHJvdmFsX2hhbmRvZmYiOiByZWwoSEFORE9GRiksCiAgICAgICAgImhhbmRvZmZfc3RhdHVzIjogaGFuZG9mZi5nZXQoImhhbmRvZmZfc3RhdHVzIiksCiAgICAgICAgImhhbmRvZmZfdmFsaWQiOiBib29sKGhhbmRvZmZfdmFsaWQpLAogICAgICAgICJleGVjdXRvcl9hbGxvd2VkIjogYm9vbChleGVjdXRvcl9hbGxvd2VkKSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogYm9vbChleGVjdXRvcl9yYW4pLAogICAgICAgICJleGVjdXRvcl9zdGF0dXMiOiBleGVjdXRvcl9zdGF0dXMsCiAgICAgICAgImV4ZWN1dG9yX3N0ZXBzIjogc3RlcHMsCiAgICAgICAgImJsb2NrX3JlYXNvbiI6IGJsb2NrX3JlYXNvbiwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJLZWVwIGV4ZWN1dG9yIGJsb2NrZWQgdW50aWwgbGl2ZSBhcHByb3ZhbCBoYW5kb2ZmIGlzIHZhbGlkLiIgaWYgbm90IGV4ZWN1dG9yX2FsbG93ZWQgZWxzZSAiRXhlY3V0b3IgcmVhZGluZXNzIGV4aXN0cywgYnV0IGNvbW1hbmQgZXhlY3V0aW9uIHN0aWxsIHJlcXVpcmVzIGEgc2VwYXJhdGUgcnVuIGF1dGhvcml6YXRpb24gbGF5ZXIuIiwKICAgICAgICAiYm91bmRhcnkiOiAiQXBwcm92YWwtZ2F0ZWQgcmVwbGF5IGV4ZWN1dG9ycyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGV4ZWN1dGlvbi1ib3VuZGFyeSBhcnRpZmFjdHMuIFRoaXMgcmVwb3J0IGRvZXMgbm90IGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzIGJ5IGRlZmF1bHQsIGRvZXMgbm90IGNyZWF0ZSBicmFuY2hlcywgZG9lcyBub3QgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGRvZXMgbm90IGFwcGx5IGNhbGlicmF0aW9uLCBhbmQgZG9lcyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjYuOCBzaG91bGQgYWRkIGV4cGxpY2l0IHJ1biBhdXRob3JpemF0aW9uIGlmIGxpdmUgaGFuZG9mZiBiZWNvbWVzIHZhbGlkOyBvdGhlcndpc2UgY29udGludWUgYmxvY2tlZC1zdGF0ZSBvYnNlcnZhYmlsaXR5LiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gImFwcHJvdmFsX2dhdGVkX3JlcGxheV9leGVjdXRvcl92MF82XzcuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X2FwcHJvdmFsX2dhdGVkX3JlcGxheV9leGVjdXRvci5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJhcHByb3ZhbF9nYXRlZF9yZXBsYXlfZXhlY3V0b3JfdjBfNl83Lm1kIiwgcmVwb3J0KHN1bW1hcnkpKQogICAgd3RleHQoT1VUIC8gImxhdGVzdF9hcHByb3ZhbF9nYXRlZF9yZXBsYXlfZXhlY3V0b3IubWQiLCByZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJleGVjdXRvcl9zdGF0dXMiOiBzdW1tYXJ5WyJleGVjdXRvcl9zdGF0dXMiXSwKICAgICAgICAiaGFuZG9mZl9zdGF0dXMiOiBzdW1tYXJ5WyJoYW5kb2ZmX3N0YXR1cyJdLAogICAgICAgICJoYW5kb2ZmX3ZhbGlkIjogc3VtbWFyeVsiaGFuZG9mZl92YWxpZCJdLAogICAgICAgICJleGVjdXRvcl9hbGxvd2VkIjogc3VtbWFyeVsiZXhlY3V0b3JfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBzdW1tYXJ5WyJicmFuY2hfY3JlYXRlZCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvcmVwbGF5X2V4ZWN1dG9yL2xhdGVzdF9hcHByb3ZhbF9nYXRlZF9yZXBsYXlfZXhlY3V0b3IubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"replay_executor"/"README.md", """# Replay Executor Reports

Current layer: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**

## Purpose

This folder stores approval-gated replay executor reports. The executor refuses to run when live approval handoff is invalid.

## Primary command

```powershell
python scripts/benchmarks/run_approval_gated_replay_executor.py
```

## README Update Rule

Update this mini README whenever replay executor schemas, execution rules, or approval gates change.

Boundary: replay executor reports are local classifier-governance execution-boundary artifacts only.
""")
write(ROOT/"visuals"/"replay_executor"/"README.md", """# Replay Executor Visuals

Current layer: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**

## Purpose

This folder stores charts summarizing replay executor state.

## README Update Rule

Update this mini README whenever replay executor chart names or meanings change.

Boundary: replay executor visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"replay_executor"/"v0_6_7"/"README.md", """# v0.6.7 Replay Executor Charts

Expected charts:

- `replay_executor_gate_state.png`
- `replay_executor_steps.png`
- `replay_executor_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local replay-executor diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.6[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.5[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.6 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.7 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.6-ready |", "| Task routing matrix | geometry-aware / v0.6.7-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.6 |", "| Agent contract version sync | current / v0.6.7 |")
if "| Replay executor |" not in r:
    r=r.replace("| Live approval handoff charts | `visuals/live_approval_handoff/v0_6_6/` |\n",
                "| Live approval handoff charts | `visuals/live_approval_handoff/v0_6_6/` |\n| Replay executor | `reports/replay_executor/latest_approval_gated_replay_executor.md` |\n| Replay executor charts | `visuals/replay_executor/v0_6_7/` |\n")
if "python scripts/benchmarks/run_approval_gated_replay_executor.py" not in r:
    r=r.replace("python scripts/benchmarks/run_live_approval_handoff_check.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_live_approval_handoff_check.py\npython scripts/benchmarks/run_approval_gated_replay_executor.py\npython scripts/release/validate_release.py")
if "    replay_executor/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    replay_executor/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    replay_executor/\n")
section="""## Approval-Gated Replay Executor v0.6.7

v0.6.7 adds the replay executor boundary. The executor refuses to run when live approval handoff is invalid.

Primary command:

```powershell
python scripts/benchmarks/run_approval_gated_replay_executor.py
```

Primary outputs:

```text
reports/replay_executor/latest_approval_gated_replay_executor.json
reports/replay_executor/latest_approval_gated_replay_executor.md
visuals/replay_executor/v0_6_7/
```

Current expected lock when live approval handoff is invalid:

```text
handoff_valid: false
executor_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: approval-gated replay executors are local classifier-governance execution-boundary artifacts. They do not execute replay commands by default, do not create branches, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Approval-Gated Replay Executor v0.6.7" not in r:
    r=r.replace("## Live Approval Handoff Check v0.6.6", section+"## Live Approval Handoff Check v0.6.6",1)
lesson="| L-049 | v0.6.6 confirmed no live approval existed. | A missing live approval should still reach the executor boundary and prove execution is blocked. | Replay executors must refuse to run when live approval handoff is invalid, emitting a blocked executor report instead of silently stopping. |"
if "L-049" not in r:
    r=r.replace("| L-048 | v0.6.5 validated fixture semantics but fixtures are still not live approval. | Fixture-validity can be mistaken for live-approval validity unless handoff checks enforce path separation. | Live approval handoff must refuse fixtures and require a separate non-fixture live approval artifact before replay is considered. |\n",
                "| L-048 | v0.6.5 validated fixture semantics but fixtures are still not live approval. | Fixture-validity can be mistaken for live-approval validity unless handoff checks enforce path separation. | Live approval handoff must refuse fixtures and require a separate non-fixture live approval artifact before replay is considered. |\n"+lesson+"\n")
if "| v0.6.7 |" not in r:
    r=r.replace("| v0.6.6 | Live approval handoff check; refuses fixtures as live approval. |\n",
                "| v0.6.6 | Live approval handoff check; refuses fixtures as live approval. |\n| v0.6.7 | Approval-gated replay executor; refuses execution when handoff is invalid. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**

Recommended goals:

- Append blocked executor state to a durable continuity ledger.
- Track approval-chain state across versions.
- Preserve blocked execution as evidence, not failure.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_approval_gated_replay_executor.py" not in s:
        s=s.replace("python scripts/benchmarks/run_live_approval_handoff_check.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_live_approval_handoff_check.py\npython scripts/benchmarks/run_approval_gated_replay_executor.py\npython -m unittest discover -s tests")
        s=s.replace("| Live approval handoff patch | `reports/live_approval_handoff/`, `visuals/live_approval_handoff/`, approval fixtures | handoff check + release validator; fixtures refused as live approval |\n",
                    "| Live approval handoff patch | `reports/live_approval_handoff/`, `visuals/live_approval_handoff/`, approval fixtures | handoff check + release validator; fixtures refused as live approval |\n| Replay executor patch | `reports/replay_executor/`, `visuals/replay_executor/`, live approval handoff | executor gate + release validator; refuses execution when handoff invalid |\n")
    if name.endswith("task_routing_matrix.md") and "| Replay executor patch |" not in s:
        s=s.replace("| Live approval handoff patch | outer | validation | governance | approval fixtures + live approval directory | handoff check + charts + release validator | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` |\n",
                    "| Live approval handoff patch | outer | validation | governance | approval fixtures + live approval directory | handoff check + charts + release validator | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` |\n| Replay executor patch | outer | execution-boundary | governance | live approval handoff | executor blocked report + charts + release validator | `reports/replay_executor/latest_approval_gated_replay_executor.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.7"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["approval_gated_replay_executor"]={
    "read_first":["reports/live_approval_handoff/latest_live_approval_handoff_check.json"],
    "validate":["python scripts/benchmarks/run_approval_gated_replay_executor.py","python scripts/release/validate_release.py"],
    "evidence":["reports/replay_executor/latest_approval_gated_replay_executor.md","visuals/replay_executor/v0_6_7/"],
    "mutation_lock":"Refuses execution when live approval handoff is invalid; no branch creation or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.7 | Approval-gated replay executor |" not in t:
    t=t.replace("| v0.6.6 | Live approval handoff check | `python scripts/benchmarks/run_live_approval_handoff_check.py` | Refuses fixtures as live approval and requires separate live artifact | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` | `visuals/live_approval_handoff/v0_6_6/` |\n",
                "| v0.6.6 | Live approval handoff check | `python scripts/benchmarks/run_live_approval_handoff_check.py` | Refuses fixtures as live approval and requires separate live artifact | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` | `visuals/live_approval_handoff/v0_6_6/` |\n| v0.6.7 | Approval-gated replay executor | `python scripts/benchmarks/run_approval_gated_replay_executor.py` | Refuses execution when live approval handoff is invalid | `reports/replay_executor/latest_approval_gated_replay_executor.md` | `visuals/replay_executor/v0_6_7/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_7_replay_executor.md", f"""# TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor

Generated: {NOW}

## Purpose

Add the replay executor boundary and refuse execution when live approval handoff is invalid.

## Boundary

Replay executors are local classifier-governance execution-boundary artifacts only. They do not execute replay commands by default, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.7 patch written")
