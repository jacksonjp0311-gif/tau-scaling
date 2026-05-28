
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"counterfactual_decision"/"v0_5_7"/"backups"/f"{p.name}_before_v0_5_7_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"generate_counterfactual_decision_record.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdCkNPVU5URVIgPSBST09UIC8gInJlcG9ydHMiIC8gImNhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscyIgLyAibGF0ZXN0X2NhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscy5qc29uIgpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImNvdW50ZXJmYWN0dWFsX2RlY2lzaW9uIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImNvdW50ZXJmYWN0dWFsX2RlY2lzaW9uIiAvICJ2MF81XzciCgpkZWYgcmpzb24ocCk6IHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgY2hhcnRzKHMpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQoc3RyKHAucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKSkKCiAgICBkYXRhID0gc1siZGVjaXNpb25fY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCw0KSkKICAgIHBsdC5iYXIobGlzdChkYXRhLmtleXMoKSksIGxpc3QoZGF0YS52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnRpdGxlKCJDb3VudGVyZmFjdHVhbCBEZWNpc2lvbiBDbGFzc2lmaWNhdGlvbiIpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBzYXZlKCJjb3VudGVyZmFjdHVhbF9kZWNpc2lvbl9jb3VudHMucG5nIikKCiAgICBtZXRyaWNzID0gewogICAgICAgICJzYWZlIjogc1sic2FmZV9jYW5kaWRhdGVfY291bnQiXSwKICAgICAgICAicmVqZWN0ZWQiOiBzWyJyZWplY3RlZF9jb3VudCJdLAogICAgICAgICJkcmlmdCI6IHNbImNvdW50ZXJmYWN0dWFsX2RyaWZ0X2NvdW50Il0sCiAgICAgICAgInRvdGFsIjogc1siY291bnRlcmZhY3R1YWxfY291bnQiXSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCw0KSkKICAgIHBsdC5iYXIobGlzdChtZXRyaWNzLmtleXMoKSksIGxpc3QobWV0cmljcy52YWx1ZXMoKSkpCiAgICBwbHQudGl0bGUoIkNvdW50ZXJmYWN0dWFsIEV2aWRlbmNlIE1ldHJpY3MiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgc2F2ZSgiY291bnRlcmZhY3R1YWxfZGVjaXNpb25fbWV0cmljcy5wbmciKQoKICAgIHN0YXR1cyA9IHMuZ2V0KCJzb3VyY2Vfc3RhdHVzX2NvdW50cyIsIHt9KQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LDQpKQogICAgcGx0LmJhcihsaXN0KHN0YXR1cy5rZXlzKCkpLCBsaXN0KHN0YXR1cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnRpdGxlKCJTb3VyY2UgQ291bnRlcmZhY3R1YWwgU3RhdHVzIENvdW50cyIpCiAgICBwbHQueWxhYmVsKCJSb3dzIikKICAgIHNhdmUoImNvdW50ZXJmYWN0dWFsX3NvdXJjZV9zdGF0dXNfY291bnRzLnBuZyIpCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZXBvcnQocyk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC41LjcgQ291bnRlcmZhY3R1YWwgRGVjaXNpb24gUmVjb3JkIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzWydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgRGVjaXNpb24iLAogICAgICAgICIiLAogICAgICAgIGYiLSBEZWNpc2lvbjogYHtzWydkZWNpc2lvbiddfWAiLAogICAgICAgIGYiLSBTZWxlY3RlZCByZXBvcnQtb25seSB0aHJlc2hvbGQ6IGB7c1snc2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkJ119YCIsCiAgICAgICAgZiItIFJlYXNvbjoge3NbJ2RlY2lzaW9uX3JlYXNvbiddfSIsCiAgICAgICAgZiItIE5leHQgc3RlcDoge3NbJ25leHRfc3RlcCddfSIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEV2aWRlbmNlIFN1bW1hcnkiLAogICAgICAgICIiLAogICAgICAgIGYiLSBDb3VudGVyZmFjdHVhbCBjb3VudDogYHtzWydjb3VudGVyZmFjdHVhbF9jb3VudCddfWAiLAogICAgICAgIGYiLSBTYWZlIGNhbmRpZGF0ZXM6IGB7c1snc2FmZV9jYW5kaWRhdGVfY291bnQnXX1gIiwKICAgICAgICBmIi0gUmVqZWN0ZWQgY2FuZGlkYXRlczogYHtzWydyZWplY3RlZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBEcmlmdCBjb3VudDogYHtzWydjb3VudGVyZmFjdHVhbF9kcmlmdF9jb3VudCddfWAiLAogICAgICAgIGYiLSBSZXZpZXcgYWxsb3dlZDogYHtzWydyZXZpZXdfYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBBcHBsaWNhdGlvbiBhbGxvd2VkOiBge3NbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIENhbGlicmF0aW9uIGFwcGxpZWQ6IGB7c1snY2FsaWJyYXRpb25fYXBwbGllZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe3JlbH0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBjID0gcmpzb24oQ09VTlRFUikKICAgIHRvdGFsID0gaW50KGMuZ2V0KCJjb3VudGVyZmFjdHVhbF9jb3VudCIsIDApIG9yIDApCiAgICBzYWZlID0gaW50KGMuZ2V0KCJzYWZlX2NhbmRpZGF0ZV9jb3VudCIsIDApIG9yIDApCiAgICByZWplY3RlZCA9IGludChjLmdldCgicmVqZWN0ZWRfY291bnQiLCAwKSBvciAwKQogICAgZHJpZnQgPSBpbnQoYy5nZXQoImNvdW50ZXJmYWN0dWFsX2RyaWZ0X2NvdW50IiwgMCkgb3IgMCkKCiAgICBpZiB0b3RhbCA+IDAgYW5kIHNhZmUgPT0gdG90YWwgYW5kIHJlamVjdGVkID09IDAgYW5kIGRyaWZ0ID09IDA6CiAgICAgICAgZGVjaXNpb24gPSAiU0FGRV9GT1JfUkVWSUVXX05PVF9BUFBMSUNBVElPTiIKICAgICAgICByZWFzb24gPSAiQWxsIGNvdW50ZXJmYWN0dWFsIHJvd3MgcHJlc2VydmVkIHN1cHBvcnQgY29udHJvbHMgd2l0aCB6ZXJvIGRyaWZ0IGFuZCB6ZXJvIHJlamVjdGVkIHJvd3MuIgogICAgICAgIHJldmlldyA9IFRydWUKICAgIGVsaWYgcmVqZWN0ZWQgPiAwOgogICAgICAgIGRlY2lzaW9uID0gIlJFSkVDVEVEX1NVUFBPUlRfQ09OVFJPTF9WSU9MQVRJT04iCiAgICAgICAgcmVhc29uID0gIkF0IGxlYXN0IG9uZSBjb3VudGVyZmFjdHVhbCB2aW9sYXRlZCBzdXBwb3J0LWF3YXJlIHJldGVudGlvbi4iCiAgICAgICAgcmV2aWV3ID0gRmFsc2UKICAgIGVsaWYgZHJpZnQgPiAwOgogICAgICAgIGRlY2lzaW9uID0gIk5FRURTX01PUkVfQ09OVFJPTFMiCiAgICAgICAgcmVhc29uID0gIkNvdW50ZXJmYWN0dWFsIGRyaWZ0IHdhcyBvYnNlcnZlZC4iCiAgICAgICAgcmV2aWV3ID0gRmFsc2UKICAgIGVsc2U6CiAgICAgICAgZGVjaXNpb24gPSAiSU5TVUZGSUNJRU5UX0NPVU5URVJGQUNUVUFMX0VWSURFTkNFIgogICAgICAgIHJlYXNvbiA9ICJDb3VudGVyZmFjdHVhbCBldmlkZW5jZSB3YXMgaW5jb21wbGV0ZS4iCiAgICAgICAgcmV2aWV3ID0gRmFsc2UKCiAgICBzID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctY291bnRlcmZhY3R1YWwtZGVjaXNpb24tcmVjb3JkLXYwLjUuNyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9jb3VudGVyZmFjdHVhbHMiOiAicmVwb3J0cy9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMvbGF0ZXN0X2NhbGlicmF0aW9uX2NvdW50ZXJmYWN0dWFscy5qc29uIiwKICAgICAgICAic2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkIjogYy5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIpLAogICAgICAgICJjb3VudGVyZmFjdHVhbF9jb3VudCI6IHRvdGFsLAogICAgICAgICJzYWZlX2NhbmRpZGF0ZV9jb3VudCI6IHNhZmUsCiAgICAgICAgInJlamVjdGVkX2NvdW50IjogcmVqZWN0ZWQsCiAgICAgICAgImNvdW50ZXJmYWN0dWFsX2RyaWZ0X2NvdW50IjogZHJpZnQsCiAgICAgICAgInNvdXJjZV9zdGF0dXNfY291bnRzIjogYy5nZXQoInN0YXR1c19jb3VudHMiLCB7fSksCiAgICAgICAgImRlY2lzaW9uIjogZGVjaXNpb24sCiAgICAgICAgImRlY2lzaW9uX3JlYXNvbiI6IHJlYXNvbiwKICAgICAgICAibmV4dF9zdGVwIjogIkJ1bmRsZSBldmlkZW5jZSBmb3IgcmV2aWV3OyBkbyBub3QgYXBwbHkgY2xhc3NpZmllciBtdXRhdGlvbi4iIGlmIHJldmlldyBlbHNlICJEbyBub3QgYWR2YW5jZSBjYW5kaWRhdGUuIiwKICAgICAgICAiZGVjaXNpb25fY291bnRzIjoge2RlY2lzaW9uOiAxfSwKICAgICAgICAicmV2aWV3X2FsbG93ZWQiOiByZXZpZXcsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJyZXZpZXdfY2FuZGlkYXRlX3dpdGhvdXRfYXBwbGljYXRpb24iIGlmIHJldmlldyBlbHNlICJkb19ub3RfcmV2aWV3X2NhbmRpZGF0ZV95ZXQiLAogICAgICAgICJib3VuZGFyeSI6ICJDb3VudGVyZmFjdHVhbCBkZWNpc2lvbiByZWNvcmRzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgZGVjaXNpb24gYXJ0aWZhY3RzLiBUaGV5IGRvIG5vdCBjaGFuZ2UgY2xhc3NpZmllciBiZWhhdmlvciBhbmQgZG8gbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC41Ljggc2hvdWxkIHByb2R1Y2UgYSByZXZpZXcgcGFja2FnZSB3aXRoIGV2aWRlbmNlIGJ1bmRsZSBhbmQgbXV0YXRpb24gc3RpbGwgZGlzYWJsZWQuIiwKICAgIH0KICAgIHNbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMocykKICAgIHdqc29uKE9VVCAvICJjb3VudGVyZmFjdHVhbF9kZWNpc2lvbl9yZWNvcmRfdjBfNV83Lmpzb24iLCBzKQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9jb3VudGVyZmFjdHVhbF9kZWNpc2lvbl9yZWNvcmQuanNvbiIsIHMpCiAgICB3dGV4dChPVVQgLyAiY291bnRlcmZhY3R1YWxfZGVjaXNpb25fcmVjb3JkX3YwXzVfNy5tZCIsIHJlcG9ydChzKSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfY291bnRlcmZhY3R1YWxfZGVjaXNpb25fcmVjb3JkLm1kIiwgcmVwb3J0KHMpKQogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHNbInNjaGVtYSJdLAogICAgICAgICJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiOiBzWyJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiXSwKICAgICAgICAiZGVjaXNpb24iOiBzWyJkZWNpc2lvbiJdLAogICAgICAgICJyZXZpZXdfYWxsb3dlZCI6IHNbInJldmlld19hbGxvd2VkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzWyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzWyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzWyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogc1siZmluYWxfcmVjb21tZW5kYXRpb24iXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc1siY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL2NvdW50ZXJmYWN0dWFsX2RlY2lzaW9uL2xhdGVzdF9jb3VudGVyZmFjdHVhbF9kZWNpc2lvbl9yZWNvcmQubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"counterfactual_decision"/"README.md", """# Counterfactual Decision Reports

Current layer: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**

## Purpose

This folder stores non-mutating decision records derived from calibration counterfactual outcomes.

## Primary command

```powershell
python scripts/benchmarks/generate_counterfactual_decision_record.py
```

## README Update Rule

Update this mini README whenever decision schemas, report paths, or classification rules change.

Boundary: counterfactual decision records are local classifier-governance artifacts only.
""")
write(ROOT/"visuals"/"counterfactual_decision"/"README.md", """# Counterfactual Decision Visuals

Current layer: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**

## Purpose

This folder stores charts summarizing counterfactual decision outcomes.

## README Update Rule

Update this mini README whenever decision chart names or meanings change.

Boundary: decision visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"counterfactual_decision"/"v0_5_7"/"README.md", """# v0.5.7 Counterfactual Decision Charts

Expected charts:

- `counterfactual_decision_counts.png`
- `counterfactual_decision_metrics.png`
- `counterfactual_source_status_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local decision-record diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.6[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.5[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.6 - Calibration Counterfactuals**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.6 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.7 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.6-ready |", "| Task routing matrix | geometry-aware / v0.5.7-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.6 |", "| Agent contract version sync | current / v0.5.7 |")
if "| Counterfactual decision record |" not in r:
    r=r.replace("| Calibration counterfactual charts | `visuals/calibration_counterfactuals/v0_5_6/` |\n",
                "| Calibration counterfactual charts | `visuals/calibration_counterfactuals/v0_5_6/` |\n| Counterfactual decision record | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` |\n| Counterfactual decision charts | `visuals/counterfactual_decision/v0_5_7/` |\n")
if "python scripts/benchmarks/generate_counterfactual_decision_record.py" not in r:
    r=r.replace("python scripts/benchmarks/run_calibration_counterfactuals.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_calibration_counterfactuals.py\npython scripts/benchmarks/generate_counterfactual_decision_record.py\npython scripts/release/validate_release.py")
if "    counterfactual_decision/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    counterfactual_decision/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    counterfactual_decision/\n")
section="""## Counterfactual Decision Record v0.5.7

v0.5.7 converts v0.5.6 calibration counterfactual outcomes into a non-mutating decision record.

Primary command:

```powershell
python scripts/benchmarks/generate_counterfactual_decision_record.py
```

Primary outputs:

```text
reports/counterfactual_decision/latest_counterfactual_decision_record.json
reports/counterfactual_decision/latest_counterfactual_decision_record.md
visuals/counterfactual_decision/v0_5_7/
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: counterfactual decision records are local classifier-governance decision artifacts. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Counterfactual Decision Record v0.5.7" not in r:
    r=r.replace("## Calibration Counterfactuals v0.5.6", section+"## Calibration Counterfactuals v0.5.6",1)
lesson="| L-039 | v0.5.6 counterfactuals passed, but a passing counterfactual is not an applied policy. | Successful simulations still need an explicit decision record to prevent silent promotion. | A successful counterfactual must become a decision record before any implementation pathway can be discussed. |"
if "L-039" not in r:
    r=r.replace("| L-038 | v0.5.5 selected a report-only calibration threshold, but a threshold is not a classifier change. | Calibration planning can still hide drift unless tested counterfactually. | Any selected calibration threshold must pass report-only counterfactual testing before policy mutation can even be discussed. |\n",
                "| L-038 | v0.5.5 selected a report-only calibration threshold, but a threshold is not a classifier change. | Calibration planning can still hide drift unless tested counterfactually. | Any selected calibration threshold must pass report-only counterfactual testing before policy mutation can even be discussed. |\n"+lesson+"\n")
if "| v0.5.7 |" not in r:
    r=r.replace("| v0.5.6 | Calibration counterfactuals for the selected report-only threshold. |\n",
                "| v0.5.6 | Calibration counterfactuals for the selected report-only threshold. |\n| v0.5.7 | Counterfactual decision record for safe-review classification without application. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**

Recommended goals:

- Bundle v0.5.2-v0.5.7 evidence into a review package.
- Include cause cards, remediation tasks, negative controls, calibration plan, counterfactuals, and decision record.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: review packages are local classifier governance only.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "generate_counterfactual_decision_record.py" not in s:
        s=s.replace("python scripts/benchmarks/run_calibration_counterfactuals.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_calibration_counterfactuals.py\npython scripts/benchmarks/generate_counterfactual_decision_record.py\npython -m unittest discover -s tests")
        s=s.replace("| Calibration counterfactual patch | `reports/calibration_counterfactuals/`, `visuals/calibration_counterfactuals/`, calibration plan | counterfactual report + release validator; no classifier mutation |\n",
                    "| Calibration counterfactual patch | `reports/calibration_counterfactuals/`, `visuals/calibration_counterfactuals/`, calibration plan | counterfactual report + release validator; no classifier mutation |\n| Counterfactual decision patch | `reports/counterfactual_decision/`, `visuals/counterfactual_decision/`, counterfactual report | decision record + release validator; no classifier mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Counterfactual decision patch |" not in s:
        s=s.replace("| Calibration counterfactual patch | outer | validation | governance | calibration plan + negative controls | counterfactual report + charts + release validator | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` |\n",
                    "| Calibration counterfactual patch | outer | validation | governance | calibration plan + negative controls | counterfactual report + charts + release validator | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` |\n| Counterfactual decision patch | outer | validation | governance | calibration counterfactuals + decision criteria | decision record + charts + release validator | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.7"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["counterfactual_decision_record"]={
    "read_first":["reports/calibration_counterfactuals/latest_calibration_counterfactuals.json"],
    "validate":["python scripts/benchmarks/generate_counterfactual_decision_record.py","python scripts/release/validate_release.py"],
    "evidence":["reports/counterfactual_decision/latest_counterfactual_decision_record.md","visuals/counterfactual_decision/v0_5_7/"],
    "mutation_lock":"Does not change classifier behavior; application_allowed and mutation_allowed must remain false."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.7 | Counterfactual decision record |" not in t:
    t=t.replace("| v0.5.6 | Calibration counterfactuals | `python scripts/benchmarks/run_calibration_counterfactuals.py` | Simulates selected calibration candidate without applying classifier mutation | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` | `visuals/calibration_counterfactuals/v0_5_6/` |\n",
                "| v0.5.6 | Calibration counterfactuals | `python scripts/benchmarks/run_calibration_counterfactuals.py` | Simulates selected calibration candidate without applying classifier mutation | `reports/calibration_counterfactuals/latest_calibration_counterfactuals.md` | `visuals/calibration_counterfactuals/v0_5_6/` |\n| v0.5.7 | Counterfactual decision record | `python scripts/benchmarks/generate_counterfactual_decision_record.py` | Classifies counterfactual candidate for review without application | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` | `visuals/counterfactual_decision/v0_5_7/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_7_counterfactual_decision_record.md", f"""# TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record

Generated: {NOW}

## Purpose

Convert v0.5.6 calibration counterfactual outcomes into a non-mutating decision record.

## Boundary

Counterfactual decision records are local classifier-governance artifacts only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.7 patch written")
