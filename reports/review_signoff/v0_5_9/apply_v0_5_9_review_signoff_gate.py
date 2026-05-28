
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"review_signoff"/"v0_5_9"/"backups"/f"{p.name}_before_v0_5_9_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_review_signoff_gate.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdClBLRyA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmV2aWV3X3BhY2thZ2UiIC8gImxhdGVzdF9yZXZpZXdfcGFja2FnZS5qc29uIgpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInJldmlld19zaWdub2ZmIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gInJldmlld19zaWdub2ZmIiAvICJ2MF81XzkiCgpDSEVDS1MgPSBbCiAgICAoImV2aWRlbmNlX2J1bmRsZV9jb21wbGV0ZSIsICJBbGwgdjAuNS4yLXYwLjUuNyBldmlkZW5jZSBpbnB1dHMgYXJlIHByZXNlbnQuIiksCiAgICAoInJldmlld19zdGF0dXNfcmVhZHkiLCAiUmV2aWV3IHBhY2thZ2Ugc3RhdHVzIGlzIFJFQURZX0ZPUl9IVU1BTl9SRVZJRVdfTk9UX0FQUExJQ0FUSU9OLiIpLAogICAgKCJkZWNpc2lvbl9zYWZlX2Zvcl9yZXZpZXciLCAiRGVjaXNpb24gY2xhc3MgaXMgU0FGRV9GT1JfUkVWSUVXX05PVF9BUFBMSUNBVElPTi4iKSwKICAgICgicmV2aWV3X2FsbG93ZWRfdHJ1ZSIsICJSZXZpZXcgaXMgYWxsb3dlZC4iKSwKICAgICgiYXBwbGljYXRpb25fYWxsb3dlZF9mYWxzZSIsICJBcHBsaWNhdGlvbiBpcyBub3QgYWxsb3dlZC4iKSwKICAgICgibXV0YXRpb25fYWxsb3dlZF9mYWxzZSIsICJDbGFzc2lmaWVyIG11dGF0aW9uIGlzIG5vdCBhbGxvd2VkLiIpLAogICAgKCJwb2xpY3lfZW5mb3JjZWRfZmFsc2UiLCAiUG9saWN5IGlzIG5vdCBlbmZvcmNlZC4iKSwKICAgICgiY2FsaWJyYXRpb25fYXBwbGllZF9mYWxzZSIsICJDYWxpYnJhdGlvbiBpcyBub3QgYXBwbGllZC4iKSwKICAgICgidGhyZXNob2xkX3ByZXNlbnQiLCAiQSBzZWxlY3RlZCByZXBvcnQtb25seSB0aHJlc2hvbGQgaXMgcHJlc2VudC4iKSwKICAgICgibm9uX2NsYWltX2JvdW5kYXJ5X3ByZXNlbnQiLCAiQm91bmRhcnkvbm9uLWNsYWltIGxhbmd1YWdlIGlzIHByZXNlbnQuIiksCl0KCmRlZiByanNvbihwKTogcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQpkZWYgd3RleHQocCwgcyk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQocywgZW5jb2Rpbmc9InV0Zi04IikKZGVmIHJlbChwKTogcmV0dXJuIHN0cihwLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBldmFsdWF0ZShwa2cpOgogICAgcm93cyA9IFtdCiAgICBtaXNzaW5nID0gcGtnLmdldCgibWlzc2luZ19pbnB1dHMiLCBbXSkKICAgIGZvciBjaGVja19pZCwgZGVzYyBpbiBDSEVDS1M6CiAgICAgICAgaWYgY2hlY2tfaWQgPT0gImV2aWRlbmNlX2J1bmRsZV9jb21wbGV0ZSI6CiAgICAgICAgICAgIHBhc3NlZCA9IGxlbihtaXNzaW5nKSA9PSAwCiAgICAgICAgICAgIG9ic2VydmVkID0gZiJtaXNzaW5nX2lucHV0cz17bGVuKG1pc3NpbmcpfSIKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJyZXZpZXdfc3RhdHVzX3JlYWR5IjoKICAgICAgICAgICAgcGFzc2VkID0gcGtnLmdldCgicmV2aWV3X3BhY2thZ2Vfc3RhdHVzIikgPT0gIlJFQURZX0ZPUl9IVU1BTl9SRVZJRVdfTk9UX0FQUExJQ0FUSU9OIgogICAgICAgICAgICBvYnNlcnZlZCA9IHN0cihwa2cuZ2V0KCJyZXZpZXdfcGFja2FnZV9zdGF0dXMiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJkZWNpc2lvbl9zYWZlX2Zvcl9yZXZpZXciOgogICAgICAgICAgICBwYXNzZWQgPSBwa2cuZ2V0KCJkZWNpc2lvbl9jbGFzcyIpID09ICJTQUZFX0ZPUl9SRVZJRVdfTk9UX0FQUExJQ0FUSU9OIgogICAgICAgICAgICBvYnNlcnZlZCA9IHN0cihwa2cuZ2V0KCJkZWNpc2lvbl9jbGFzcyIpKQogICAgICAgIGVsaWYgY2hlY2tfaWQgPT0gInJldmlld19hbGxvd2VkX3RydWUiOgogICAgICAgICAgICBwYXNzZWQgPSBwa2cuZ2V0KCJyZXZpZXdfYWxsb3dlZCIpIGlzIFRydWUKICAgICAgICAgICAgb2JzZXJ2ZWQgPSBzdHIocGtnLmdldCgicmV2aWV3X2FsbG93ZWQiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJhcHBsaWNhdGlvbl9hbGxvd2VkX2ZhbHNlIjoKICAgICAgICAgICAgcGFzc2VkID0gcGtnLmdldCgiYXBwbGljYXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgICAgIG9ic2VydmVkID0gc3RyKHBrZy5nZXQoImFwcGxpY2F0aW9uX2FsbG93ZWQiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJtdXRhdGlvbl9hbGxvd2VkX2ZhbHNlIjoKICAgICAgICAgICAgcGFzc2VkID0gcGtnLmdldCgibXV0YXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgICAgIG9ic2VydmVkID0gc3RyKHBrZy5nZXQoIm11dGF0aW9uX2FsbG93ZWQiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJwb2xpY3lfZW5mb3JjZWRfZmFsc2UiOgogICAgICAgICAgICBwYXNzZWQgPSBwa2cuZ2V0KCJwb2xpY3lfZW5mb3JjZWQiKSBpcyBGYWxzZQogICAgICAgICAgICBvYnNlcnZlZCA9IHN0cihwa2cuZ2V0KCJwb2xpY3lfZW5mb3JjZWQiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJjYWxpYnJhdGlvbl9hcHBsaWVkX2ZhbHNlIjoKICAgICAgICAgICAgcGFzc2VkID0gcGtnLmdldCgiY2FsaWJyYXRpb25fYXBwbGllZCIpIGlzIEZhbHNlCiAgICAgICAgICAgIG9ic2VydmVkID0gc3RyKHBrZy5nZXQoImNhbGlicmF0aW9uX2FwcGxpZWQiKSkKICAgICAgICBlbGlmIGNoZWNrX2lkID09ICJ0aHJlc2hvbGRfcHJlc2VudCI6CiAgICAgICAgICAgIHBhc3NlZCA9IHBrZy5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpIGlzIG5vdCBOb25lCiAgICAgICAgICAgIG9ic2VydmVkID0gc3RyKHBrZy5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpKQogICAgICAgIGVsaWYgY2hlY2tfaWQgPT0gIm5vbl9jbGFpbV9ib3VuZGFyeV9wcmVzZW50IjoKICAgICAgICAgICAgYm91bmRhcnkgPSBzdHIocGtnLmdldCgiYm91bmRhcnkiLCAiIikpCiAgICAgICAgICAgIHBhc3NlZCA9ICJkbyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IiIGluIGJvdW5kYXJ5Lmxvd2VyKCkgYW5kICJub3QgdmFsaWRhdGUgc2lsaWNvbiIgaW4gYm91bmRhcnkubG93ZXIoKQogICAgICAgICAgICBvYnNlcnZlZCA9ICJib3VuZGFyeV9wcmVzZW50IiBpZiBib3VuZGFyeSBlbHNlICJtaXNzaW5nX2JvdW5kYXJ5IgogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHBhc3NlZCA9IEZhbHNlCiAgICAgICAgICAgIG9ic2VydmVkID0gInVua25vd24iCiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAiY2hlY2tfaWQiOiBjaGVja19pZCwKICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogZGVzYywKICAgICAgICAgICAgInBhc3NlZCI6IGJvb2wocGFzc2VkKSwKICAgICAgICAgICAgIm9ic2VydmVkIjogb2JzZXJ2ZWQsCiAgICAgICAgICAgICJyZXF1aXJlZF9mb3Jfc2lnbm9mZiI6IFRydWUsCiAgICAgICAgfSkKICAgIHJldHVybiByb3dzCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIGNvdW50cyA9IHN1bW1hcnlbImNoZWNrX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDcsNCkpCiAgICBwbHQuYmFyKGxpc3QoY291bnRzLmtleXMoKSksIGxpc3QoY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC55bGFiZWwoIkNoZWNrIGNvdW50IikKICAgIHBsdC50aXRsZSgiUmV2aWV3IFNpZ25vZmYgQ2hlY2tsaXN0IFJlc3VsdHMiKQogICAgc2F2ZSgicmV2aWV3X3NpZ25vZmZfY2hlY2tfY291bnRzLnBuZyIpCgogICAgbG9ja3MgPSB7CiAgICAgICAgInJldmlld19hbGxvd2VkIjogaW50KHN1bW1hcnlbInJldmlld19hbGxvd2VkIl0pLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSksCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdKSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IGludChzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LDQpKQogICAgcGx0LmJhcihsaXN0KGxvY2tzLmtleXMoKSksIGxpc3QobG9ja3MudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJSZXZpZXcgU2lnbm9mZiBMb2NrIFN0YXRlcyIpCiAgICBzYXZlKCJyZXZpZXdfc2lnbm9mZl9sb2NrX3N0YXRlcy5wbmciKQoKICAgIGNsYXNzZXMgPSBzdW1tYXJ5WyJzaWdub2ZmX2NsYXNzX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsNCkpCiAgICBwbHQuYmFyKGxpc3QoY2xhc3Nlcy5rZXlzKCkpLCBsaXN0KGNsYXNzZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNvdW50IikKICAgIHBsdC50aXRsZSgiU2lnbm9mZiBDbGFzc2lmaWNhdGlvbiIpCiAgICBzYXZlKCJyZXZpZXdfc2lnbm9mZl9jbGFzc19jb3VudHMucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzKToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjUuOSBSZXZpZXcgQ2hlY2tsaXN0IGFuZCBTaWdub2ZmIEdhdGUiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBTaWdub2ZmIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIFNpZ25vZmYgc3RhdHVzOiBge3NbJ3NpZ25vZmZfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIENoZWNrbGlzdCBwYXNzIGNvdW50OiBge3NbJ2NoZWNrX3Bhc3NfY291bnQnXX1gIiwKICAgICAgICBmIi0gQ2hlY2tsaXN0IGZhaWwgY291bnQ6IGB7c1snY2hlY2tfZmFpbF9jb3VudCddfWAiLAogICAgICAgIGYiLSBSZXZpZXcgYWxsb3dlZDogYHtzWydyZXZpZXdfYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBBcHBsaWNhdGlvbiBhbGxvd2VkOiBge3NbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIENhbGlicmF0aW9uIGFwcGxpZWQ6IGB7c1snY2FsaWJyYXRpb25fYXBwbGllZCddfWAiLAogICAgICAgIGYiLSBGaW5hbCByZWNvbW1lbmRhdGlvbjogYHtzWydmaW5hbF9yZWNvbW1lbmRhdGlvbiddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGVja2xpc3QiLAogICAgICAgICIiLAogICAgICAgICJ8IENoZWNrIHwgUGFzc2VkIHwgT2JzZXJ2ZWQgfCBEZXNjcmlwdGlvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIHJvdyBpbiBzWyJjaGVja2xpc3QiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7cm93WydjaGVja19pZCddfWAgfCBge3Jvd1sncGFzc2VkJ119YCB8IGB7cm93WydvYnNlcnZlZCddfWAgfCB7cm93WydkZXNjcmlwdGlvbiddfSB8IikKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBwa2cgPSByanNvbihQS0cpCiAgICBjaGVja2xpc3QgPSBldmFsdWF0ZShwa2cpCiAgICBwYXNzX2NvdW50ID0gc3VtKDEgZm9yIHIgaW4gY2hlY2tsaXN0IGlmIHJbInBhc3NlZCJdKQogICAgZmFpbF9jb3VudCA9IGxlbihjaGVja2xpc3QpIC0gcGFzc19jb3VudAogICAgc2lnbm9mZl9zdGF0dXMgPSAiUkVWSUVXX1NJR05PRkZfUkVBRFlfTk9UX0FQUExJQ0FUSU9OIiBpZiBmYWlsX2NvdW50ID09IDAgZWxzZSAiU0lHTk9GRl9CTE9DS0VEIgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXJldmlldy1jaGVja2xpc3Qtc2lnbm9mZi1nYXRlLXYwLjUuOSIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9yZXZpZXdfcGFja2FnZSI6ICJyZXBvcnRzL3Jldmlld19wYWNrYWdlL2xhdGVzdF9yZXZpZXdfcGFja2FnZS5qc29uIiwKICAgICAgICAic2lnbm9mZl9zdGF0dXMiOiBzaWdub2ZmX3N0YXR1cywKICAgICAgICAiY2hlY2tsaXN0IjogY2hlY2tsaXN0LAogICAgICAgICJjaGVja19wYXNzX2NvdW50IjogcGFzc19jb3VudCwKICAgICAgICAiY2hlY2tfZmFpbF9jb3VudCI6IGZhaWxfY291bnQsCiAgICAgICAgImNoZWNrX2NvdW50cyI6IHsicGFzc2VkIjogcGFzc19jb3VudCwgImZhaWxlZCI6IGZhaWxfY291bnR9LAogICAgICAgICJzaWdub2ZmX2NsYXNzX2NvdW50cyI6IHtzaWdub2ZmX3N0YXR1czogMX0sCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IHBrZy5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpLAogICAgICAgICJyZXZpZXdfYWxsb3dlZCI6IHNpZ25vZmZfc3RhdHVzID09ICJSRVZJRVdfU0lHTk9GRl9SRUFEWV9OT1RfQVBQTElDQVRJT04iLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiAiSHVtYW4gcmV2aWV3IG1heSBiZWdpbi4gQXBwbGljYXRpb24gYW5kIG11dGF0aW9uIHJlbWFpbiBibG9ja2VkLiIgaWYgZmFpbF9jb3VudCA9PSAwIGVsc2UgIlJlcGFpciBzaWdub2ZmIGNoZWNrbGlzdCBmYWlsdXJlcyBiZWZvcmUgcmV2aWV3LiIsCiAgICAgICAgImJvdW5kYXJ5IjogIlJldmlldyBzaWdub2ZmIGdhdGVzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2Ugc2lnbm9mZiBhcnRpZmFjdHMuIFRoZXkgZG8gbm90IGNoYW5nZSBjbGFzc2lmaWVyIGJlaGF2aW9yIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjYuMCBzaG91bGQgY3JlYXRlIGEgaHVtYW4tYXBwcm92ZWQgY2FuZGlkYXRlIGJyYW5jaCBvbmx5IGFmdGVyIGV4cGxpY2l0IGV4dGVybmFsIHNpZ25vZmYsIHN0aWxsIG5vbi1tdXRhdGluZyBieSBkZWZhdWx0LiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAicmV2aWV3X3NpZ25vZmZfZ2F0ZV92MF81XzkuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X3Jldmlld19zaWdub2ZmX2dhdGUuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAicmV2aWV3X3NpZ25vZmZfZ2F0ZV92MF81XzkubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3Jldmlld19zaWdub2ZmX2dhdGUubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInNpZ25vZmZfc3RhdHVzIjogc3VtbWFyeVsic2lnbm9mZl9zdGF0dXMiXSwKICAgICAgICAiY2hlY2tfcGFzc19jb3VudCI6IHN1bW1hcnlbImNoZWNrX3Bhc3NfY291bnQiXSwKICAgICAgICAiY2hlY2tfZmFpbF9jb3VudCI6IHN1bW1hcnlbImNoZWNrX2ZhaWxfY291bnQiXSwKICAgICAgICAicmV2aWV3X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXZpZXdfYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvcmV2aWV3X3NpZ25vZmYvbGF0ZXN0X3Jldmlld19zaWdub2ZmX2dhdGUubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"review_signoff"/"README.md", """# Review Signoff Reports

Current layer: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**

## Purpose

This folder stores signoff checklists for review packages.

## Primary command

```powershell
python scripts/benchmarks/run_review_signoff_gate.py
```

## README Update Rule

Update this mini README whenever signoff schemas, checklist rules, or review gates change.

Boundary: review signoff gates are local classifier-governance artifacts only.
""")
write(ROOT/"visuals"/"review_signoff"/"README.md", """# Review Signoff Visuals

Current layer: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**

## Purpose

This folder stores charts summarizing review-signoff checklist state.

## README Update Rule

Update this mini README whenever signoff chart names or meanings change.

Boundary: signoff visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"review_signoff"/"v0_5_9"/"README.md", """# v0.5.9 Review Signoff Charts

Expected charts:

- `review_signoff_check_counts.png`
- `review_signoff_lock_states.png`
- `review_signoff_class_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local review-signoff diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.8[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.7[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.8 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.9 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.8-ready |", "| Task routing matrix | geometry-aware / v0.5.9-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.8 |", "| Agent contract version sync | current / v0.5.9 |")
if "| Review signoff gate |" not in r:
    r=r.replace("| Review package charts | `visuals/review_package/v0_5_8/` |\n",
                "| Review package charts | `visuals/review_package/v0_5_8/` |\n| Review signoff gate | `reports/review_signoff/latest_review_signoff_gate.md` |\n| Review signoff charts | `visuals/review_signoff/v0_5_9/` |\n")
if "python scripts/benchmarks/run_review_signoff_gate.py" not in r:
    r=r.replace("python scripts/benchmarks/generate_review_package.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/generate_review_package.py\npython scripts/benchmarks/run_review_signoff_gate.py\npython scripts/release/validate_release.py")
if "    review_signoff/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    review_signoff/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    review_signoff/\n")
section="""## Review Checklist and Signoff Gate v0.5.9

v0.5.9 converts the v0.5.8 review package into an explicit signoff checklist.

Primary command:

```powershell
python scripts/benchmarks/run_review_signoff_gate.py
```

Primary outputs:

```text
reports/review_signoff/latest_review_signoff_gate.json
reports/review_signoff/latest_review_signoff_gate.md
visuals/review_signoff/v0_5_9/
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: review signoff gates are local classifier-governance signoff artifacts. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Review Checklist and Signoff Gate v0.5.9" not in r:
    r=r.replace("## Review Package and Evidence Bundle v0.5.8", section+"## Review Package and Evidence Bundle v0.5.8",1)
lesson="| L-041 | v0.5.8 produced a review-ready evidence bundle. | Review-ready bundles still require explicit signoff gates to prevent review from being mistaken for application. | A review package must pass a signoff checklist before a candidate branch or implementation pathway is discussed. |"
if "L-041" not in r:
    r=r.replace("| L-040 | v0.5.7 produced SAFE_FOR_REVIEW_NOT_APPLICATION. | Safe-for-review can be mistaken for safe-for-application unless bundled explicitly. | A candidate that reaches SAFE_FOR_REVIEW_NOT_APPLICATION must be bundled into a review package before any implementation pathway is discussed. |\n",
                "| L-040 | v0.5.7 produced SAFE_FOR_REVIEW_NOT_APPLICATION. | Safe-for-review can be mistaken for safe-for-application unless bundled explicitly. | A candidate that reaches SAFE_FOR_REVIEW_NOT_APPLICATION must be bundled into a review package before any implementation pathway is discussed. |\n"+lesson+"\n")
if "| v0.5.9 |" not in r:
    r=r.replace("| v0.5.8 | Review package and evidence bundle for v0.5.2-v0.5.7. |\n",
                "| v0.5.8 | Review package and evidence bundle for v0.5.2-v0.5.7. |\n| v0.5.9 | Review checklist and signoff gate for the evidence bundle. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch**

Recommended goals:

- Create a non-mutating candidate branch package only after explicit human disposition.
- Preserve all review-package and signoff evidence.
- Keep default runtime behavior unchanged.
- Keep `mutation_allowed: false` unless a separate explicit human approval artifact exists.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.8[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_review_signoff_gate.py" not in s:
        s=s.replace("python scripts/benchmarks/generate_review_package.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/generate_review_package.py\npython scripts/benchmarks/run_review_signoff_gate.py\npython -m unittest discover -s tests")
        s=s.replace("| Review package patch | `reports/review_package/`, `visuals/review_package/`, decision record | review package + release validator; no classifier mutation |\n",
                    "| Review package patch | `reports/review_package/`, `visuals/review_package/`, decision record | review package + release validator; no classifier mutation |\n| Review signoff patch | `reports/review_signoff/`, `visuals/review_signoff/`, review package | signoff checklist + release validator; no classifier mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Review signoff patch |" not in s:
        s=s.replace("| Review package patch | outer | evidence | governance | v0.5.2-v0.5.7 evidence surfaces | review package + charts + release validator | `reports/review_package/latest_review_package.md` |\n",
                    "| Review package patch | outer | evidence | governance | v0.5.2-v0.5.7 evidence surfaces | review package + charts + release validator | `reports/review_package/latest_review_package.md` |\n| Review signoff patch | outer | validation | governance | review package + signoff checks | signoff gate + charts + release validator | `reports/review_signoff/latest_review_signoff_gate.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.9"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["review_signoff_gate"]={
    "read_first":["reports/review_package/latest_review_package.json"],
    "validate":["python scripts/benchmarks/run_review_signoff_gate.py","python scripts/release/validate_release.py"],
    "evidence":["reports/review_signoff/latest_review_signoff_gate.md","visuals/review_signoff/v0_5_9/"],
    "mutation_lock":"Does not change classifier behavior; application_allowed and mutation_allowed must remain false."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.9 | Review checklist and signoff gate |" not in t:
    t=t.replace("| v0.5.8 | Review package and evidence bundle | `python scripts/benchmarks/generate_review_package.py` | Bundles v0.5.2-v0.5.7 evidence for review without application | `reports/review_package/latest_review_package.md` | `visuals/review_package/v0_5_8/` |\n",
                "| v0.5.8 | Review package and evidence bundle | `python scripts/benchmarks/generate_review_package.py` | Bundles v0.5.2-v0.5.7 evidence for review without application | `reports/review_package/latest_review_package.md` | `visuals/review_package/v0_5_8/` |\n| v0.5.9 | Review checklist and signoff gate | `python scripts/benchmarks/run_review_signoff_gate.py` | Converts review package into explicit signoff checklist | `reports/review_signoff/latest_review_signoff_gate.md` | `visuals/review_signoff/v0_5_9/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_9_review_signoff_gate.md", f"""# TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate

Generated: {NOW}

## Purpose

Convert the v0.5.8 review package into an explicit signoff checklist.

## Boundary

Review signoff gates are local classifier-governance artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.9 patch written")
