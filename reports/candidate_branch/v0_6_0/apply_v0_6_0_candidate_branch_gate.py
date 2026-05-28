
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"candidate_branch"/"v0_6_0"/"backups"/f"{p.name}_before_v0_6_0_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_candidate_branch_gate.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpTSUdOT0ZGID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZXZpZXdfc2lnbm9mZiIgLyAibGF0ZXN0X3Jldmlld19zaWdub2ZmX2dhdGUuanNvbiIKUkVWSUVXID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZXZpZXdfcGFja2FnZSIgLyAibGF0ZXN0X3Jldmlld19wYWNrYWdlLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FuZGlkYXRlX2JyYW5jaCIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJjYW5kaWRhdGVfYnJhbmNoIiAvICJ2MF82XzAiCgpkZWYgcmpzb24ocCk6IHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCmRlZiByZWwocCk6IHJldHVybiBzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIGdhdGUgPSB7CiAgICAgICAgInNpZ25vZmZfcmVhZHkiOiBpbnQoc3VtbWFyeVsic2lnbm9mZl9yZWFkeSJdKSwKICAgICAgICAiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiXSksCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogaW50KHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0pLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSksCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdKSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZS5rZXlzKCkpLCBsaXN0KGdhdGUudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJDYW5kaWRhdGUgQnJhbmNoIEdhdGUgU3RhdGUiKQogICAgc2F2ZSgiY2FuZGlkYXRlX2JyYW5jaF9nYXRlX3N0YXRlLnBuZyIpCgogICAgY2hlY2tzID0gewogICAgICAgICJzaWdub2ZmX3Bhc3MiOiBpbnQoc3VtbWFyeVsic2lnbm9mZl9jaGVja19wYXNzX2NvdW50Il0pLAogICAgICAgICJzaWdub2ZmX2ZhaWwiOiBpbnQoc3VtbWFyeVsic2lnbm9mZl9jaGVja19mYWlsX2NvdW50Il0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg3LCA0KSkKICAgIHBsdC5iYXIobGlzdChjaGVja3Mua2V5cygpKSwgbGlzdChjaGVja3MudmFsdWVzKCkpKQogICAgcGx0LnlsYWJlbCgiQ2hlY2sgY291bnQiKQogICAgcGx0LnRpdGxlKCJTaWdub2ZmIENoZWNrbGlzdCBDb3VudHMiKQogICAgc2F2ZSgiY2FuZGlkYXRlX2JyYW5jaF9zaWdub2ZmX2NvdW50cy5wbmciKQoKICAgIGNsYXNzZXMgPSB7c3VtbWFyeVsiY2FuZGlkYXRlX2JyYW5jaF9zdGF0dXMiXTogMX0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoY2xhc3Nlcy5rZXlzKCkpLCBsaXN0KGNsYXNzZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNvdW50IikKICAgIHBsdC50aXRsZSgiQ2FuZGlkYXRlIEJyYW5jaCBTdGF0dXMiKQogICAgc2F2ZSgiY2FuZGlkYXRlX2JyYW5jaF9zdGF0dXMucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzKToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjYuMCBIdW1hbi1BcHByb3ZlZCBDYW5kaWRhdGUgQnJhbmNoIEdhdGUiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBHYXRlIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIENhbmRpZGF0ZSBicmFuY2ggc3RhdHVzOiBge3NbJ2NhbmRpZGF0ZV9icmFuY2hfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFNlbGVjdGVkIHJlcG9ydC1vbmx5IHRocmVzaG9sZDogYHtzWydzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQnXX1gIiwKICAgICAgICBmIi0gU2lnbm9mZiByZWFkeTogYHtzWydzaWdub2ZmX3JlYWR5J119YCIsCiAgICAgICAgZiItIEJyYW5jaCBwcm9wb3NhbCBhbGxvd2VkOiBge3NbJ2JyYW5jaF9wcm9wb3NhbF9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEJyYW5jaCBjcmVhdGVkOiBge3NbJ2JyYW5jaF9jcmVhdGVkJ119YCIsCiAgICAgICAgZiItIEFwcGxpY2F0aW9uIGFsbG93ZWQ6IGB7c1snYXBwbGljYXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3NbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gQ2FsaWJyYXRpb24gYXBwbGllZDogYHtzWydjYWxpYnJhdGlvbl9hcHBsaWVkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEh1bWFuIEFwcHJvdmFsIFJlcXVpcmVtZW50IiwKICAgICAgICAiIiwKICAgICAgICBzWyJodW1hbl9hcHByb3ZhbF9yZXF1aXJlbWVudCJdLAogICAgICAgICIiLAogICAgICAgICIjIyBDYW5kaWRhdGUgQnJhbmNoIFByb3Bvc2FsIiwKICAgICAgICAiIiwKICAgICAgICAifCBGaWVsZCB8IFZhbHVlIHwiLAogICAgICAgICJ8LS0tfC0tLXwiLAogICAgICAgIGYifCBQcm9wb3NlZCBicmFuY2ggbmFtZSB8IGB7c1sncHJvcG9zZWRfYnJhbmNoX25hbWUnXX1gIHwiLAogICAgICAgIGYifCBTb3VyY2Ugc2lnbm9mZiB8IGB7c1snaW5wdXRfcmV2aWV3X3NpZ25vZmYnXX1gIHwiLAogICAgICAgIGYifCBTb3VyY2UgcmV2aWV3IHBhY2thZ2UgfCBge3NbJ2lucHV0X3Jldmlld19wYWNrYWdlJ119YCB8IiwKICAgICAgICBmInwgRGVmYXVsdCBicmFuY2ggY3JlYXRpb24gfCBge3NbJ2JyYW5jaF9jcmVhdGVkJ119YCB8IiwKICAgICAgICBmInwgUnVudGltZSBiZWhhdmlvciBjaGFuZ2VkIHwgYGZhbHNlYCB8IiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHNbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzWyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgc2lnbm9mZiA9IHJqc29uKFNJR05PRkYpCiAgICByZXZpZXcgPSByanNvbihSRVZJRVcpCgogICAgc2lnbm9mZl9yZWFkeSA9IHNpZ25vZmYuZ2V0KCJzaWdub2ZmX3N0YXR1cyIpID09ICJSRVZJRVdfU0lHTk9GRl9SRUFEWV9OT1RfQVBQTElDQVRJT04iCiAgICBwYXNzX2NvdW50ID0gaW50KHNpZ25vZmYuZ2V0KCJjaGVja19wYXNzX2NvdW50IiwgMCkgb3IgMCkKICAgIGZhaWxfY291bnQgPSBpbnQoc2lnbm9mZi5nZXQoImNoZWNrX2ZhaWxfY291bnQiLCAwKSBvciAwKQogICAgdGhyZXNob2xkID0gc2lnbm9mZi5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIsIHJldmlldy5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpKQoKICAgIHN0YXR1cyA9ICJDQU5ESURBVEVfQlJBTkNIX1BST1BPU0FMX1JFQURZX19IVU1BTl9BUFBST1ZBTF9SRVFVSVJFRCIgaWYgc2lnbm9mZl9yZWFkeSBhbmQgZmFpbF9jb3VudCA9PSAwIGVsc2UgIkNBTkRJREFURV9CUkFOQ0hfQkxPQ0tFRCIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctaHVtYW4tYXBwcm92ZWQtY2FuZGlkYXRlLWJyYW5jaC1nYXRlLXYwLjYuMCIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9yZXZpZXdfc2lnbm9mZiI6ICJyZXBvcnRzL3Jldmlld19zaWdub2ZmL2xhdGVzdF9yZXZpZXdfc2lnbm9mZl9nYXRlLmpzb24iLAogICAgICAgICJpbnB1dF9yZXZpZXdfcGFja2FnZSI6ICJyZXBvcnRzL3Jldmlld19wYWNrYWdlL2xhdGVzdF9yZXZpZXdfcGFja2FnZS5qc29uIiwKICAgICAgICAiY2FuZGlkYXRlX2JyYW5jaF9zdGF0dXMiOiBzdGF0dXMsCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IHRocmVzaG9sZCwKICAgICAgICAic2lnbm9mZl9yZWFkeSI6IGJvb2woc2lnbm9mZl9yZWFkeSksCiAgICAgICAgInNpZ25vZmZfY2hlY2tfcGFzc19jb3VudCI6IHBhc3NfY291bnQsCiAgICAgICAgInNpZ25vZmZfY2hlY2tfZmFpbF9jb3VudCI6IGZhaWxfY291bnQsCiAgICAgICAgImJyYW5jaF9wcm9wb3NhbF9hbGxvd2VkIjogYm9vbChzaWdub2ZmX3JlYWR5IGFuZCBmYWlsX2NvdW50ID09IDApLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJwcm9wb3NlZF9icmFuY2hfbmFtZSI6ICJjYW5kaWRhdGUvdjAuNi4wLXRocmVzaG9sZC0wLjgtcmV2aWV3LW9ubHkiLAogICAgICAgICJodW1hbl9hcHByb3ZhbF9yZXF1aXJlZCI6IFRydWUsCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiOiBGYWxzZSwKICAgICAgICAiaHVtYW5fYXBwcm92YWxfcmVxdWlyZW1lbnQiOiAiQSBodW1hbiBhcHByb3ZhbCBhcnRpZmFjdCBtdXN0IGJlIGFkZGVkIGJlZm9yZSBjcmVhdGluZyBhbnkgY2FuZGlkYXRlIGJyYW5jaCBvciBpbXBsZW1lbnRhdGlvbiBwYXRod2F5LiBUaGlzIGdhdGUgb25seSBwcmVwYXJlcyBhIHByb3Bvc2FsLiIsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiAiUHJlcGFyZSBodW1hbiByZXZpZXcgZGlzcG9zaXRpb24uIERvIG5vdCBjcmVhdGUgYnJhbmNoLCBhcHBseSBjYWxpYnJhdGlvbiwgb3IgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IgZnJvbSB0aGlzIHJlcG9ydCBhbG9uZS4iLAogICAgICAgICJib3VuZGFyeSI6ICJIdW1hbi1hcHByb3ZlZCBjYW5kaWRhdGUgYnJhbmNoIGdhdGVzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgcHJvcG9zYWwgYXJ0aWZhY3RzLiBUaGV5IGRvIG5vdCBjcmVhdGUgYSBicmFuY2ggYnkgZGVmYXVsdCwgZG8gbm90IGNoYW5nZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhbmQgZG8gbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC42LjEgc2hvdWxkIHJlcGxheSBhIGNhbmRpZGF0ZSBicmFuY2ggb25seSBhZnRlciBleHBsaWNpdCBodW1hbiBhcHByb3ZhbCBhcnRpZmFjdCBleGlzdHMuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJjYW5kaWRhdGVfYnJhbmNoX2dhdGVfdjBfNl8wLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX2dhdGUuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAiY2FuZGlkYXRlX2JyYW5jaF9nYXRlX3YwXzZfMC5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfY2FuZGlkYXRlX2JyYW5jaF9nYXRlLm1kIiwgcmVwb3J0KHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiY2FuZGlkYXRlX2JyYW5jaF9zdGF0dXMiOiBzdW1tYXJ5WyJjYW5kaWRhdGVfYnJhbmNoX3N0YXR1cyJdLAogICAgICAgICJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiOiBzdW1tYXJ5WyJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiXSwKICAgICAgICAiYnJhbmNoX3Byb3Bvc2FsX2FsbG93ZWQiOiBzdW1tYXJ5WyJicmFuY2hfcHJvcG9zYWxfYWxsb3dlZCJdLAogICAgICAgICJodW1hbl9hcHByb3ZhbF9yZXF1aXJlZCI6IHN1bW1hcnlbImh1bWFuX2FwcHJvdmFsX3JlcXVpcmVkIl0sCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiOiBzdW1tYXJ5WyJodW1hbl9hcHByb3ZhbF9wcmVzZW50Il0sCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogc3VtbWFyeVsiYnJhbmNoX2NyZWF0ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL2NhbmRpZGF0ZV9icmFuY2gvbGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfZ2F0ZS5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT/"reports"/"candidate_branch"/"README.md", """# Candidate Branch Gate Reports

Current layer: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**

## Purpose

This folder stores non-mutating candidate-branch proposal gates. It does not create branches by default.

## Primary command

```powershell
python scripts/benchmarks/run_candidate_branch_gate.py
```

## README Update Rule

Update this mini README whenever candidate branch gate schemas, approval requirements, or branch proposal rules change.

Boundary: candidate branch gates are local classifier-governance proposal artifacts only.
""")
write(ROOT/"visuals"/"candidate_branch"/"README.md", """# Candidate Branch Gate Visuals

Current layer: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**

## Purpose

This folder stores charts summarizing candidate-branch gate state.

## README Update Rule

Update this mini README whenever candidate-branch chart names or meanings change.

Boundary: candidate-branch visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"candidate_branch"/"v0_6_0"/"README.md", """# v0.6.0 Candidate Branch Gate Charts

Expected charts:

- `candidate_branch_gate_state.png`
- `candidate_branch_signoff_counts.png`
- `candidate_branch_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local candidate-branch diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.9[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.8[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.9 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.0 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.9-ready |", "| Task routing matrix | geometry-aware / v0.6.0-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.9 |", "| Agent contract version sync | current / v0.6.0 |")
if "| Candidate branch gate |" not in r:
    r=r.replace("| Review signoff charts | `visuals/review_signoff/v0_5_9/` |\n",
                "| Review signoff charts | `visuals/review_signoff/v0_5_9/` |\n| Candidate branch gate | `reports/candidate_branch/latest_candidate_branch_gate.md` |\n| Candidate branch charts | `visuals/candidate_branch/v0_6_0/` |\n")
if "python scripts/benchmarks/run_candidate_branch_gate.py" not in r:
    r=r.replace("python scripts/benchmarks/run_review_signoff_gate.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_review_signoff_gate.py\npython scripts/benchmarks/run_candidate_branch_gate.py\npython scripts/release/validate_release.py")
if "    candidate_branch/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    candidate_branch/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    candidate_branch/\n")
section="""## Human-Approved Candidate Branch Gate v0.6.0

v0.6.0 prepares a non-mutating candidate branch proposal after v0.5.9 signoff.

Primary command:

```powershell
python scripts/benchmarks/run_candidate_branch_gate.py
```

Primary outputs:

```text
reports/candidate_branch/latest_candidate_branch_gate.json
reports/candidate_branch/latest_candidate_branch_gate.md
visuals/candidate_branch/v0_6_0/
```

Current lock:

```text
branch_created: false
human_approval_required: true
human_approval_present: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: candidate branch gates are local classifier-governance proposal artifacts. They do not create a branch by default, do not change classifier behavior, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Human-Approved Candidate Branch Gate v0.6.0" not in r:
    r=r.replace("## Review Checklist and Signoff Gate v0.5.9", section+"## Review Checklist and Signoff Gate v0.5.9",1)
lesson="| L-042 | v0.5.9 passed the signoff gate, but signoff readiness is still not branch creation. | A signoff-ready candidate needs an explicit human approval artifact before branch creation or implementation. | Candidate-branch gates must prepare proposals only; branches require explicit human approval and remain non-mutating by default. |"
if "L-042" not in r:
    r=r.replace("| L-041 | v0.5.8 produced a review-ready evidence bundle. | Review-ready bundles still require explicit signoff gates to prevent review from being mistaken for application. | A review package must pass a signoff checklist before a candidate branch or implementation pathway is discussed. |\n",
                "| L-041 | v0.5.8 produced a review-ready evidence bundle. | Review-ready bundles still require explicit signoff gates to prevent review from being mistaken for application. | A review package must pass a signoff checklist before a candidate branch or implementation pathway is discussed. |\n"+lesson+"\n")
if "| v0.6.0 |" not in r:
    r=r.replace("| v0.5.9 | Review checklist and signoff gate for the evidence bundle. |\n",
                "| v0.5.9 | Review checklist and signoff gate for the evidence bundle. |\n| v0.6.0 | Human-approved candidate branch gate; proposal only, no branch by default. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**

Recommended goals:

- Only run after explicit human approval artifact exists.
- Replay the candidate proposal against baseline evidence.
- Keep default runtime behavior unchanged.
- Keep `mutation_allowed: false` unless a separate explicit human approval artifact exists.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_candidate_branch_gate.py" not in s:
        s=s.replace("python scripts/benchmarks/run_review_signoff_gate.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_review_signoff_gate.py\npython scripts/benchmarks/run_candidate_branch_gate.py\npython -m unittest discover -s tests")
        s=s.replace("| Review signoff patch | `reports/review_signoff/`, `visuals/review_signoff/`, review package | signoff checklist + release validator; no classifier mutation |\n",
                    "| Review signoff patch | `reports/review_signoff/`, `visuals/review_signoff/`, review package | signoff checklist + release validator; no classifier mutation |\n| Candidate branch gate patch | `reports/candidate_branch/`, `visuals/candidate_branch/`, review signoff | proposal gate + release validator; no branch by default |\n")
    if name.endswith("task_routing_matrix.md") and "| Candidate branch gate patch |" not in s:
        s=s.replace("| Review signoff patch | outer | validation | governance | review package + signoff checks | signoff gate + charts + release validator | `reports/review_signoff/latest_review_signoff_gate.md` |\n",
                    "| Review signoff patch | outer | validation | governance | review package + signoff checks | signoff gate + charts + release validator | `reports/review_signoff/latest_review_signoff_gate.md` |\n| Candidate branch gate patch | outer | governance | review | signoff gate + human approval requirement | candidate branch gate + charts + release validator | `reports/candidate_branch/latest_candidate_branch_gate.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.0"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["candidate_branch_gate"]={
    "read_first":["reports/review_signoff/latest_review_signoff_gate.json"],
    "validate":["python scripts/benchmarks/run_candidate_branch_gate.py","python scripts/release/validate_release.py"],
    "evidence":["reports/candidate_branch/latest_candidate_branch_gate.md","visuals/candidate_branch/v0_6_0/"],
    "mutation_lock":"Does not create branch by default; explicit human approval artifact required."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.0 | Human-approved candidate branch gate |" not in t:
    t=t.replace("| v0.5.9 | Review checklist and signoff gate | `python scripts/benchmarks/run_review_signoff_gate.py` | Converts review package into explicit signoff checklist | `reports/review_signoff/latest_review_signoff_gate.md` | `visuals/review_signoff/v0_5_9/` |\n",
                "| v0.5.9 | Review checklist and signoff gate | `python scripts/benchmarks/run_review_signoff_gate.py` | Converts review package into explicit signoff checklist | `reports/review_signoff/latest_review_signoff_gate.md` | `visuals/review_signoff/v0_5_9/` |\n| v0.6.0 | Human-approved candidate branch gate | `python scripts/benchmarks/run_candidate_branch_gate.py` | Prepares candidate branch proposal only; no branch by default | `reports/candidate_branch/latest_candidate_branch_gate.md` | `visuals/candidate_branch/v0_6_0/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_0_candidate_branch_gate.md", f"""# TAU-SCALING-SA v0.6.0 - Human-Approved Candidate Branch Gate

Generated: {NOW}

## Purpose

Prepare a non-mutating candidate branch proposal after v0.5.9 signoff.

## Boundary

Candidate branch gates are local classifier-governance proposal artifacts only. They do not create branches by default, do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.0 patch written")
