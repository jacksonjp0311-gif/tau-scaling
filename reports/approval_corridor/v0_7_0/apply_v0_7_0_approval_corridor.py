
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
        d = ROOT / "reports" / "approval_corridor" / "v0_7_0" / "backups" / f"{p.name}_before_v0_7_0_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_approval_governance_corridor.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImFwcHJvdmFsX2NvcnJpZG9yIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImFwcHJvdmFsX2NvcnJpZG9yIiAvICJ2MF83XzAiCgpJTlBVVFMgPSB7CiAgICAiY2FuZGlkYXRlX2JyYW5jaCI6IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FuZGlkYXRlX2JyYW5jaCIgLyAibGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfZ2F0ZS5qc29uIiwKICAgICJjYW5kaWRhdGVfcmVwbGF5IjogUk9PVCAvICJyZXBvcnRzIiAvICJjYW5kaWRhdGVfcmVwbGF5IiAvICJsYXRlc3RfY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfaGFybmVzcy5qc29uIiwKICAgICJodW1hbl9hcHByb3ZhbF90ZW1wbGF0ZSI6IFJPT1QgLyAicmVwb3J0cyIgLyAiaHVtYW5fYXBwcm92YWwiIC8gImxhdGVzdF9odW1hbl9hcHByb3ZhbF90ZW1wbGF0ZV9yZXBvcnQuanNvbiIsCiAgICAiYXBwcm92YWxfdmFsaWRhdG9yIjogUk9PVCAvICJyZXBvcnRzIiAvICJhcHByb3ZhbF92YWxpZGF0b3IiIC8gImxhdGVzdF9odW1hbl9hcHByb3ZhbF92YWxpZGF0b3IuanNvbiIsCiAgICAiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5IjogUk9PVCAvICJyZXBvcnRzIiAvICJhcHByb3ZhbF9nYXRlZF9yZXBsYXkiIC8gImxhdGVzdF9hcHByb3ZhbF9nYXRlZF9yZXBsYXlfZHJ5X3J1bi5qc29uIiwKICAgICJhcHByb3ZhbF9maXh0dXJlcyI6IFJPT1QgLyAicmVwb3J0cyIgLyAiYXBwcm92YWxfZml4dHVyZXMiIC8gImxhdGVzdF9hcHByb3ZhbF9maXh0dXJlX3ZhbGlkYXRvci5qc29uIiwKICAgICJsaXZlX2FwcHJvdmFsX2hhbmRvZmYiOiBST09UIC8gInJlcG9ydHMiIC8gImxpdmVfYXBwcm92YWxfaGFuZG9mZiIgLyAibGF0ZXN0X2xpdmVfYXBwcm92YWxfaGFuZG9mZl9jaGVjay5qc29uIiwKICAgICJyZXBsYXlfZXhlY3V0b3IiOiBST09UIC8gInJlcG9ydHMiIC8gInJlcGxheV9leGVjdXRvciIgLyAibGF0ZXN0X2FwcHJvdmFsX2dhdGVkX3JlcGxheV9leGVjdXRvci5qc29uIiwKICAgICJibG9ja2VkX2NvbnRpbnVpdHkiOiBST09UIC8gInJlcG9ydHMiIC8gImJsb2NrZWRfY29udGludWl0eSIgLyAibGF0ZXN0X2Jsb2NrZWRfc3RhdGVfY29udGludWl0eS5qc29uIiwKICAgICJibG9ja2VkX3RyZW5kIjogUk9PVCAvICJyZXBvcnRzIiAvICJibG9ja2VkX3RyZW5kX3JldmlldyIgLyAibGF0ZXN0X2Jsb2NrZWRfc3RhdGVfdHJlbmRfcmV2aWV3Lmpzb24iLAogICAgInJlbGVhc2VfcmVhZGluZXNzIjogUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIsCn0KClNUQVRFUyA9IFsKICAgICgidjAuNi4wIiwgImNhbmRpZGF0ZV9icmFuY2giLCAiY2FuZGlkYXRlX2JyYW5jaF9zdGF0dXMiKSwKICAgICgidjAuNi4xIiwgImNhbmRpZGF0ZV9yZXBsYXkiLCAicmVwbGF5X3N0YXR1cyIpLAogICAgKCJ2MC42LjIiLCAiaHVtYW5fYXBwcm92YWxfdGVtcGxhdGUiLCAiYXBwcm92YWxfdGVtcGxhdGVfc3RhdHVzIiksCiAgICAoInYwLjYuMyIsICJhcHByb3ZhbF92YWxpZGF0b3IiLCAidmFsaWRhdG9yX3N0YXR1cyIpLAogICAgKCJ2MC42LjQiLCAiYXBwcm92YWxfZ2F0ZWRfcmVwbGF5IiwgImRyeV9ydW5fc3RhdHVzIiksCiAgICAoInYwLjYuNSIsICJhcHByb3ZhbF9maXh0dXJlcyIsICJmaXh0dXJlX3N0YXR1cyIpLAogICAgKCJ2MC42LjYiLCAibGl2ZV9hcHByb3ZhbF9oYW5kb2ZmIiwgImhhbmRvZmZfc3RhdHVzIiksCiAgICAoInYwLjYuNyIsICJyZXBsYXlfZXhlY3V0b3IiLCAiZXhlY3V0b3Jfc3RhdHVzIiksCiAgICAoInYwLjYuOCIsICJibG9ja2VkX2NvbnRpbnVpdHkiLCAiY29udGludWl0eV9zdGF0dXMiKSwKICAgICgidjAuNi45IiwgImJsb2NrZWRfdHJlbmQiLCAidHJlbmRfc3RhdHVzIiksCl0KCkZPUkJJRERFTiA9IFsKICAgICJyZXZpZXdfdG9fYXBwbGljYXRpb24iLAogICAgInNpZ25vZmZfdG9fYnJhbmNoX2NyZWF0aW9uIiwKICAgICJ0ZW1wbGF0ZV90b19hcHByb3ZhbCIsCiAgICAiZml4dHVyZV90b19saXZlX2FwcHJvdmFsIiwKICAgICJoYW5kb2ZmX3RvX211dGF0aW9uIiwKICAgICJyZXBsYXlfcmVhZGluZXNzX3RvX2V4ZWN1dGlvbiIsCiAgICAiYmxvY2tlZF9zdGF0ZV90b19mYWlsdXJlIiwKICAgICJsb2NhbF9ydW50aW1lX2V2aWRlbmNlX3RvX3NpbGljb25fdmFsaWRhdGlvbiIsCl0KCmRlZiByanNvbihwYXRoOiBQYXRoKToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiB7Im1pc3NpbmciOiBUcnVlfQogICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd2pzb24ocGF0aDogUGF0aCwgZGF0YSk6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhkYXRhLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KHRleHQsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgcmVsKHBhdGg6IFBhdGgpOgogICAgcmV0dXJuIHN0cihwYXRoLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBidWlsZF9yb3dzKGRhdGEpOgogICAgcm93cyA9IFtdCiAgICBmb3IgdmVyc2lvbiwga2V5LCBzdGF0dXNfa2V5IGluIFNUQVRFUzoKICAgICAgICBkID0gZGF0YVtrZXldCiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAidmVyc2lvbiI6IHZlcnNpb24sCiAgICAgICAgICAgICJzdGF0ZV9pZCI6IGtleSwKICAgICAgICAgICAgInN0YXR1cyI6IGQuZ2V0KHN0YXR1c19rZXksICJNSVNTSU5HIiBpZiBkLmdldCgibWlzc2luZyIpIGVsc2UgIlJFQ09SREVEIiksCiAgICAgICAgICAgICJtaXNzaW5nIjogYm9vbChkLmdldCgibWlzc2luZyIpKSwKICAgICAgICAgICAgInJlcGxheV9hbGxvd2VkIjogYm9vbChkLmdldCgicmVwbGF5X2FsbG93ZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAiZXhlY3V0b3JfcmFuIjogYm9vbChkLmdldCgiZXhlY3V0b3JfcmFuIiwgRmFsc2UpKSwKICAgICAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogYm9vbChkLmdldCgiYnJhbmNoX2NyZWF0ZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGJvb2woZC5nZXQoIm11dGF0aW9uX2FsbG93ZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IGJvb2woZC5nZXQoImFwcGxpY2F0aW9uX2FsbG93ZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IGJvb2woZC5nZXQoImNhbGlicmF0aW9uX2FwcGxpZWQiLCBGYWxzZSkpLAogICAgICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogYm9vbChkLmdldCgicG9saWN5X2VuZm9yY2VkIiwgRmFsc2UpKSwKICAgICAgICB9KQogICAgcmV0dXJuIHJvd3MKCmRlZiBtYWtlX2NoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihleGMpKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcGF0aCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwYXRoLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwYXRoKSkKCiAgICByb3dzID0gc3VtbWFyeVsiY29ycmlkb3Jfc3RhdGVzIl0KICAgIGxhYmVscyA9IFtyWyJ2ZXJzaW9uIl0gZm9yIHIgaW4gcm93c10KCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDExLCA0KSkKICAgIHBsdC5iYXIobGFiZWxzLCBbMCBpZiByWyJtaXNzaW5nIl0gZWxzZSAxIGZvciByIGluIHJvd3NdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlByZXNlbnQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBDb3JyaWRvciBTdGF0ZSBDb3ZlcmFnZSIpCiAgICBzYXZlKCJhcHByb3ZhbF9jb3JyaWRvcl9zdGF0ZV9jb3ZlcmFnZS5wbmciKQoKICAgIGNvdW50ZXJzID0gewogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bShyWyJyZXBsYXlfYWxsb3dlZCJdIGZvciByIGluIHJvd3MpLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW0oclsiZXhlY3V0b3JfcmFuIl0gZm9yIHIgaW4gcm93cyksCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogc3VtKHJbImJyYW5jaF9jcmVhdGVkIl0gZm9yIHIgaW4gcm93cyksCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW0oclsibXV0YXRpb25fYWxsb3dlZCJdIGZvciByIGluIHJvd3MpLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtKHJbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSBmb3IgciBpbiByb3dzKSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bShyWyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0gZm9yIHIgaW4gcm93cyksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIobGlzdChjb3VudGVycy5rZXlzKCkpLCBsaXN0KGNvdW50ZXJzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICBwbHQudGl0bGUoIkZvcmJpZGRlbiBUcmFuc2l0aW9uIENvdW50ZXJzIikKICAgIHNhdmUoImFwcHJvdmFsX2NvcnJpZG9yX2ZvcmJpZGRlbl9jb3VudGVycy5wbmciKQoKICAgIGhlYWx0aCA9IHsKICAgICAgICAiY29ycmlkb3JfbG9ja2VkIjogaW50KHN1bW1hcnlbImNvcnJpZG9yX2xvY2tlZCJdKSwKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBpbnQoc3VtbWFyeVsicmVsZWFzZV9wYXNzZWQiXSksCiAgICAgICAgInZpb2xhdGlvbl9jb3VudCI6IHN1bW1hcnlbInZpb2xhdGlvbl9jb3VudCJdLAogICAgICAgICJtaXNzaW5nX2NvdW50Ijogc3VtbWFyeVsibWlzc2luZ19jb3VudCJdLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0LnlsYWJlbCgiVmFsdWUiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBDb3JyaWRvciBIZWFsdGgiKQogICAgc2F2ZSgiYXBwcm92YWxfY29ycmlkb3JfaGVhbHRoX3N1bW1hcnkucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjAgQXBwcm92YWwtR292ZXJuYW5jZSBDb3JyaWRvciBNaWxlc3RvbmUiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBNaWxlc3RvbmUgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gQ29ycmlkb3Igc3RhdHVzOiBge3N1bW1hcnlbJ2NvcnJpZG9yX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBDb3JyaWRvciBsb2NrZWQ6IGB7c3VtbWFyeVsnY29ycmlkb3JfbG9ja2VkJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIFZpb2xhdGlvbiBjb3VudDogYHtzdW1tYXJ5Wyd2aW9sYXRpb25fY291bnQnXX1gIiwKICAgICAgICBmIi0gTWlzc2luZyBjb3VudDogYHtzdW1tYXJ5WydtaXNzaW5nX2NvdW50J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENvcnJpZG9yIFN0YXRlIENoYWluIiwKICAgICAgICAiIiwKICAgICAgICAifCBWZXJzaW9uIHwgU3RhdGUgfCBTdGF0dXMgfCBSZXBsYXkgfCBFeGVjdXRlZCB8IE11dGF0aW9uIHwgQXBwbGljYXRpb24gfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS06fC0tLTp8LS0tOnwtLS06fCIsCiAgICBdCiAgICBmb3IgciBpbiBzdW1tYXJ5WyJjb3JyaWRvcl9zdGF0ZXMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7clsndmVyc2lvbiddfWAgfCBge3JbJ3N0YXRlX2lkJ119YCB8IGB7clsnc3RhdHVzJ119YCB8IGB7clsncmVwbGF5X2FsbG93ZWQnXX1gIHwgYHtyWydleGVjdXRvcl9yYW4nXX1gIHwgYHtyWydtdXRhdGlvbl9hbGxvd2VkJ119YCB8IGB7clsnYXBwbGljYXRpb25fYWxsb3dlZCddfWAgfCIpCiAgICBsaW5lcyArPSBbIiIsICIjIyBGb3JiaWRkZW4gVHJhbnNpdGlvbnMiLCAiIl0KICAgIGZvciBpdGVtIGluIHN1bW1hcnlbImZvcmJpZGRlbl90cmFuc2l0aW9ucyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIi0gYHtpdGVtfWAiKQogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBIYXJkIExvY2tzIiwKICAgICAgICAiIiwKICAgICAgICAiYGBgdGV4dCIsCiAgICAgICAgInJlcGxheV9hbGxvd2VkOiBmYWxzZSIsCiAgICAgICAgImV4ZWN1dG9yX3JhbjogZmFsc2UiLAogICAgICAgICJicmFuY2hfY3JlYXRlZDogZmFsc2UiLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkOiBmYWxzZSIsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQ6IGZhbHNlIiwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZDogZmFsc2UiLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQ6IGZhbHNlIiwKICAgICAgICAiYGBgIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWwogICAgICAgICIjIyBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc3VtbWFyeVsiYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgICAgICAiIyMgVGF1IFJldHVybiBQbGFuIiwKICAgICAgICAiIiwKICAgICAgICBzdW1tYXJ5WyJ0YXVfcmV0dXJuX3BsYW4iXSwKICAgICAgICAiIiwKICAgIF0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgZGF0YSA9IHtrOiByanNvbihwKSBmb3IgaywgcCBpbiBJTlBVVFMuaXRlbXMoKX0KICAgIHJvd3MgPSBidWlsZF9yb3dzKGRhdGEpCgogICAgcmVsZWFzZSA9IGRhdGFbInJlbGVhc2VfcmVhZGluZXNzIl0KICAgIHJlbGVhc2VfcGFzc2VkID0gcmVsZWFzZS5nZXQoInBhc3NlZCIpIGlzIFRydWUgYW5kIGxlbihyZWxlYXNlLmdldCgiZmluZGluZ3MiLCBbXSkpID09IDAgYW5kIGxlbihyZWxlYXNlLmdldCgic3RlcF9mYWlsdXJlcyIsIFtdKSkgPT0gMAoKICAgIHZpb2xhdGlvbnMgPSBbXQogICAgZm9yIHJvdyBpbiByb3dzOgogICAgICAgIGZvciBrZXkgaW4gWyJyZXBsYXlfYWxsb3dlZCIsICJleGVjdXRvcl9yYW4iLCAiYnJhbmNoX2NyZWF0ZWQiLCAibXV0YXRpb25fYWxsb3dlZCIsICJhcHBsaWNhdGlvbl9hbGxvd2VkIiwgImNhbGlicmF0aW9uX2FwcGxpZWQiLCAicG9saWN5X2VuZm9yY2VkIl06CiAgICAgICAgICAgIGlmIHJvdy5nZXQoa2V5KSBpcyBUcnVlOgogICAgICAgICAgICAgICAgdmlvbGF0aW9ucy5hcHBlbmQoeyJzdGF0ZV9pZCI6IHJvd1sic3RhdGVfaWQiXSwgInZpb2xhdGlvbiI6IGtleX0pCgogICAgbWlzc2luZ19zdGF0ZXMgPSBbclsic3RhdGVfaWQiXSBmb3IgciBpbiByb3dzIGlmIHJbIm1pc3NpbmciXV0KICAgIGNvcnJpZG9yX2xvY2tlZCA9IHJlbGVhc2VfcGFzc2VkIGFuZCBub3QgdmlvbGF0aW9ucyBhbmQgbm90IG1pc3Npbmdfc3RhdGVzCiAgICBjb3JyaWRvcl9zdGF0dXMgPSAiQVBQUk9WQUxfQ09SUklET1JfTUlMRVNUT05FX0xPQ0tFRF9fTk9fRVhFQ1VUSU9OX05PX01VVEFUSU9OIiBpZiBjb3JyaWRvcl9sb2NrZWQgZWxzZSAiQVBQUk9WQUxfQ09SUklET1JfTUlMRVNUT05FX05FRURTX1JFVklFVyIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctYXBwcm92YWwtZ292ZXJuYW5jZS1jb3JyaWRvci1taWxlc3RvbmUtdjAuNy4wIiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgImNvcnJpZG9yX3N0YXR1cyI6IGNvcnJpZG9yX3N0YXR1cywKICAgICAgICAiY29ycmlkb3JfbG9ja2VkIjogYm9vbChjb3JyaWRvcl9sb2NrZWQpLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IGJvb2wocmVsZWFzZV9wYXNzZWQpLAogICAgICAgICJ2aW9sYXRpb25fY291bnQiOiBsZW4odmlvbGF0aW9ucyksCiAgICAgICAgInZpb2xhdGlvbnMiOiB2aW9sYXRpb25zLAogICAgICAgICJtaXNzaW5nX2NvdW50IjogbGVuKG1pc3Npbmdfc3RhdGVzKSwKICAgICAgICAibWlzc2luZ19zdGF0ZXMiOiBtaXNzaW5nX3N0YXRlcywKICAgICAgICAiY29ycmlkb3Jfc3RhdGVzIjogcm93cywKICAgICAgICAiZm9yYmlkZGVuX3RyYW5zaXRpb25zIjogRk9SQklEREVOLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogIlJldHVybiB0byBUYXUgbWVjaGFuaWNzIGFmdGVyIHBhY2thZ2luZyB0aGlzIGNvcnJpZG9yLiIsCiAgICAgICAgInRhdV9yZXR1cm5fcGxhbiI6ICJTaGlmdCBiYWNrIHRvIGNvcmUgVGF1IFNjYWxpbmc6IGluc3BlY3QgdGF1LXZlY3RvciBzZW1hbnRpY3MsIGdhdGUgYWxnZWJyYSwgVFNFSyB0aHJlc2hvbGRzLCBzeW50aGV0aWMgZ2F0ZSBzdWl0ZSwgc2Vuc2l0aXZpdHkgc3dlZXBzLCBldmlkZW5jZS1jYXJkIGRlc2lnbiwgYW5kIGNsYXNzaWZpZXIgY2FsaWJyYXRpb24gYm91bmRhcmllcy4gRG8gbm90IGFkZCBtb3JlIGFwcHJvdmFsIGdhdGVzIHVubGVzcyBhIHJlYWwgbGl2ZSBhcHByb3ZhbCB3b3JrZmxvdyBpcyBpbnRlbnRpb25hbGx5IGludHJvZHVjZWQuIiwKICAgICAgICAiYm91bmRhcnkiOiAiQXBwcm92YWwtZ292ZXJuYW5jZSBjb3JyaWRvciBtaWxlc3RvbmVzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgbWlsZXN0b25lIGFydGlmYWN0cy4gVGhleSBzdW1tYXJpemUgYXV0aG9yaXR5IGJvdW5kYXJpZXMgYW5kIGV4ZWN1dGlvbiBsb2Nrcy4gVGhleSBkbyBub3QgY3JlYXRlIGxpdmUgYXBwcm92YWwsIGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzLCBjcmVhdGUgYnJhbmNoZXMsIG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhcHBseSBjYWxpYnJhdGlvbiwgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IG1ha2VfY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gImFwcHJvdmFsX2dvdmVybmFuY2VfY29ycmlkb3JfbWlsZXN0b25lX3YwXzdfMC5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfYXBwcm92YWxfZ292ZXJuYW5jZV9jb3JyaWRvcl9taWxlc3RvbmUuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAiYXBwcm92YWxfZ292ZXJuYW5jZV9jb3JyaWRvcl9taWxlc3RvbmVfdjBfN18wLm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfYXBwcm92YWxfZ292ZXJuYW5jZV9jb3JyaWRvcl9taWxlc3RvbmUubWQiLCBtYWtlX21kKHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiY29ycmlkb3Jfc3RhdHVzIjogc3VtbWFyeVsiY29ycmlkb3Jfc3RhdHVzIl0sCiAgICAgICAgImNvcnJpZG9yX2xvY2tlZCI6IHN1bW1hcnlbImNvcnJpZG9yX2xvY2tlZCJdLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0sCiAgICAgICAgInZpb2xhdGlvbl9jb3VudCI6IHN1bW1hcnlbInZpb2xhdGlvbl9jb3VudCJdLAogICAgICAgICJtaXNzaW5nX2NvdW50Ijogc3VtbWFyeVsibWlzc2luZ19jb3VudCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvYXBwcm92YWxfY29ycmlkb3IvbGF0ZXN0X2FwcHJvdmFsX2dvdmVybmFuY2VfY29ycmlkb3JfbWlsZXN0b25lLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT / "reports" / "approval_corridor" / "README.md", """# Approval-Governance Corridor Reports

Current layer: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**

## Purpose

This folder packages v0.6.0-v0.6.9 as one stable governance corridor.

## Primary command

```powershell
python scripts/benchmarks/generate_approval_governance_corridor.py
```

## README Update Rule

Update this mini README whenever corridor state definitions, forbidden transitions, or milestone criteria change.

Boundary: approval corridor reports are local classifier-governance milestone artifacts only.
""")

write(ROOT / "visuals" / "approval_corridor" / "README.md", """# Approval-Governance Corridor Visuals

Current layer: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**

## Purpose

This folder stores charts summarizing the approval-governance corridor.

## README Update Rule

Update this mini README whenever corridor chart names or meanings change.

Boundary: approval-corridor visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "approval_corridor" / "v0_7_0" / "README.md", """# v0.7.0 Approval Corridor Charts

Expected charts:

- `approval_corridor_state_coverage.png`
- `approval_corridor_forbidden_counters.png`
- `approval_corridor_health_summary.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local approval-governance milestone diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.9[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.8[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.9 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.0 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.6.9-ready |", "| Task routing matrix | geometry-aware / v0.7.0-ready |")
r = r.replace("| Agent contract version sync | current / v0.6.9 |", "| Agent contract version sync | current / v0.7.0 |")

if "| Approval-governance corridor |" not in r:
    r = r.replace("| Blocked-state trend charts | `visuals/blocked_trend_review/v0_6_9/` |\n",
                  "| Blocked-state trend charts | `visuals/blocked_trend_review/v0_6_9/` |\n| Approval-governance corridor | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` |\n| Approval corridor charts | `visuals/approval_corridor/v0_7_0/` |\n")

if "python scripts/benchmarks/generate_approval_governance_corridor.py" not in r:
    r = r.replace("python scripts/benchmarks/run_blocked_state_trend_review.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/run_blocked_state_trend_review.py\npython scripts/benchmarks/generate_approval_governance_corridor.py\npython scripts/release/validate_release.py")

if "    approval_corridor/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    approval_corridor/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    approval_corridor/\n")

section = """## Approval-Governance Corridor Milestone v0.7.0

v0.7.0 packages v0.6.0-v0.6.9 as a stable approval-governance corridor.

Primary command:

```powershell
python scripts/benchmarks/generate_approval_governance_corridor.py
```

Primary outputs:

```text
reports/approval_corridor/latest_approval_governance_corridor_milestone.json
reports/approval_corridor/latest_approval_governance_corridor_milestone.md
visuals/approval_corridor/v0_7_0/
```

Current expected lock:

```text
corridor_status: APPROVAL_CORRIDOR_MILESTONE_LOCKED__NO_EXECUTION_NO_MUTATION
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: approval-governance corridor milestones are local classifier-governance milestone artifacts. They summarize authority boundaries and execution locks. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Approval-Governance Corridor Milestone v0.7.0" not in r:
    r = r.replace("## Blocked-State Trend Review v0.6.9", section + "## Blocked-State Trend Review v0.6.9", 1)

lesson = "| L-052 | v0.6.9 confirmed the governance block was still valid. | Continuing to add gates after a valid trend review risks ceremonial accumulation. | A completed approval-governance corridor should be packaged as a milestone before returning to core Tau mechanics. |"
if "L-052" not in r:
    r = r.replace("| L-051 | v0.6.8 recorded blocked execution in a continuity ledger. | A ledger can accumulate blocked states without explaining whether the block is still valid or stale. | Blocked-state trend review must classify persistent blocks before continuing toward another execution or approval layer. |\n",
                  "| L-051 | v0.6.8 recorded blocked execution in a continuity ledger. | A ledger can accumulate blocked states without explaining whether the block is still valid or stale. | Blocked-state trend review must classify persistent blocks before continuing toward another execution or approval layer. |\n" + lesson + "\n")

if "| v0.7.0 |" not in r:
    r = r.replace("| v0.6.9 | Blocked-state trend review; classifies whether block remains valid or stale. |\n",
                  "| v0.6.9 | Blocked-state trend review; classifies whether block remains valid or stale. |\n| v0.7.0 | Approval-governance corridor milestone; packages v0.6.0-v0.6.9 and returns focus to Tau mechanics. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**

Recommended goals:

- Review tau-vector semantics.
- Review gate algebra and TSEK classifier thresholds.
- Review synthetic gate suite and sensitivity sweeps.
- Avoid adding more approval gates unless a real live approval path is intentionally introduced.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.9[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_approval_governance_corridor.py" not in s:
        s = s.replace("python scripts/benchmarks/run_blocked_state_trend_review.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/run_blocked_state_trend_review.py\npython scripts/benchmarks/generate_approval_governance_corridor.py\npython -m unittest discover -s tests")
        s = s.replace("| Blocked trend patch | `reports/blocked_trend_review/`, `visuals/blocked_trend_review/`, blocked continuity | trend review + release validator; no execution |\n",
                      "| Blocked trend patch | `reports/blocked_trend_review/`, `visuals/blocked_trend_review/`, blocked continuity | trend review + release validator; no execution |\n| Approval corridor patch | `reports/approval_corridor/`, `visuals/approval_corridor/`, v0.6 reports | corridor milestone + release validator; no execution |\n")
    if name.endswith("task_routing_matrix.md") and "| Approval corridor patch |" not in s:
        s = s.replace("| Blocked trend patch | outer | analysis | governance | blocked continuity ledger | trend review + charts + release validator | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` |\n",
                      "| Blocked trend patch | outer | analysis | governance | blocked continuity ledger | trend review + charts + release validator | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` |\n| Approval corridor patch | outer | milestone | governance | v0.6 approval reports | corridor manifest + charts + release validator | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.0"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["approval_governance_corridor_milestone"] = {
    "read_first": ["reports/blocked_trend_review/latest_blocked_state_trend_review.json", "reports/release/latest_release_readiness.json"],
    "validate": ["python scripts/benchmarks/generate_approval_governance_corridor.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/approval_corridor/latest_approval_governance_corridor_milestone.md", "visuals/approval_corridor/v0_7_0/"],
    "mutation_lock": "Milestone only; no replay execution, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.0 | Approval-governance corridor milestone |" not in t:
    t = t.replace("| v0.6.9 | Blocked-state trend review | `python scripts/benchmarks/run_blocked_state_trend_review.py` | Classifies whether the persistent block is valid or stale | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` | `visuals/blocked_trend_review/v0_6_9/` |\n",
                  "| v0.6.9 | Blocked-state trend review | `python scripts/benchmarks/run_blocked_state_trend_review.py` | Classifies whether the persistent block is valid or stale | `reports/blocked_trend_review/latest_blocked_state_trend_review.md` | `visuals/blocked_trend_review/v0_6_9/` |\n| v0.7.0 | Approval-governance corridor milestone | `python scripts/benchmarks/generate_approval_governance_corridor.py` | Packages v0.6.0-v0.6.9 as stable corridor and returns focus to Tau mechanics | `reports/approval_corridor/latest_approval_governance_corridor_milestone.md` | `visuals/approval_corridor/v0_7_0/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_0_approval_corridor.md", f"""# TAU-SCALING-SA v0.7.0 - Approval-Governance Corridor Milestone

Generated: {NOW}

## Purpose

Package v0.6.0-v0.6.9 as a stable approval-governance corridor before returning to core Tau Scaling mechanics.

## Boundary

Approval-governance corridor milestones are local classifier-governance milestone artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.0 patch written")
