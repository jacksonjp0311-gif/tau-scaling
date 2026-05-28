
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"approval_fixtures"/"v0_6_5"/"backups"/f"{p.name}_before_v0_6_5_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"validate_approval_fixtures.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpURU1QTEFURSA9IFJPT1QgLyAicmVwb3J0cyIgLyAiaHVtYW5fYXBwcm92YWwiIC8gImh1bWFuX2FwcHJvdmFsX2FydGlmYWN0X3RlbXBsYXRlX3YwXzZfMi5qc29uIgpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImFwcHJvdmFsX2ZpeHR1cmVzIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImFwcHJvdmFsX2ZpeHR1cmVzIiAvICJ2MF82XzUiCkZJWFRVUkVfRElSID0gT1VUIC8gImZpeHR1cmVzIiAvICJ2MF82XzUiCgpERUNJU0lPTlMgPSBbCiAgICAoImFwcHJvdmVfcmVwbGF5X29ubHlfZml4dHVyZSIsICJBUFBST1ZFX1JFUExBWV9PTkxZIiksCiAgICAoImRlbnlfZml4dHVyZSIsICJERU5ZIiksCiAgICAoInJlcXVlc3RfbW9yZV9ldmlkZW5jZV9maXh0dXJlIiwgIlJFUVVFU1RfTU9SRV9FVklERU5DRSIpLApdCgpkZWYgcmpzb24ocCk6CiAgICByZXR1cm4ganNvbi5sb2FkcyhwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgcmVsKHApOgogICAgcmV0dXJuIHN0cihwLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBtYWtlX2ZpeHR1cmUoYmFzZSwgZml4dHVyZV9uYW1lLCBkZWNpc2lvbik6CiAgICBmeCA9IGRpY3QoYmFzZSkKICAgIGZ4WyJhcnRpZmFjdF9zdGF0dXMiXSA9ICJGSVhUVVJFX09OTFlfTk9UX0xJVkVfQVBQUk9WQUwiCiAgICBmeFsiYXBwcm92YWxfZGVjaXNpb24iXSA9IGRlY2lzaW9uCiAgICBmeFsiYXBwcm92ZXIiXSA9ICJmaXh0dXJlLW9ubHkiCiAgICBmeFsiYXBwcm92YWxfdGltZXN0YW1wIl0gPSBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKQogICAgZnhbImZpeHR1cmVfbmFtZSJdID0gZml4dHVyZV9uYW1lCiAgICBmeFsiZml4dHVyZV9vbmx5Il0gPSBUcnVlCiAgICBmeFsiZml4dHVyZV9ib3VuZGFyeSJdID0gIlRoaXMgZml4dHVyZSB0ZXN0cyB2YWxpZGF0b3IgYmVoYXZpb3Igb25seS4gSXQgaXMgbm90IGEgbGl2ZSBodW1hbiBhcHByb3ZhbCBhcnRpZmFjdC4iCiAgICBsb2NrcyA9IGRpY3QoZnguZ2V0KCJleHBsaWNpdF9sb2NrcyIsIHt9KSkKICAgICMgRXZlbiB0aGUgYXBwcm92YWwgZml4dHVyZSBwZXJtaXRzIHJlcGxheSBpbnRlcnByZXRhdGlvbiBvbmx5OyBicmFuY2gvcnVudGltZS9jbGFzc2lmaWVyIG11dGF0aW9uIHJlbWFpbiBmYWxzZS4KICAgIGxvY2tzWyJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCJdID0gRmFsc2UKICAgIGxvY2tzWyJydW50aW1lX211dGF0aW9uX2FsbG93ZWQiXSA9IEZhbHNlCiAgICBsb2Nrc1siY2xhc3NpZmllcl9tdXRhdGlvbl9hbGxvd2VkIl0gPSBGYWxzZQogICAgbG9ja3NbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSA9IEZhbHNlCiAgICBsb2Nrc1siY2FsaWJyYXRpb25fYXBwbGllZCJdID0gRmFsc2UKICAgIGxvY2tzWyJwb2xpY3lfZW5mb3JjZWQiXSA9IEZhbHNlCiAgICBmeFsiZXhwbGljaXRfbG9ja3MiXSA9IGxvY2tzCiAgICByZXR1cm4gZngKCmRlZiB2YWxpZGF0ZV9maXh0dXJlKGZ4KToKICAgIGRlY2lzaW9uID0gZnguZ2V0KCJhcHByb3ZhbF9kZWNpc2lvbiIpCiAgICBsb2NrcyA9IGZ4LmdldCgiZXhwbGljaXRfbG9ja3MiLCB7fSkgb3Ige30KICAgIHJlcXVpcmVkX3N0YXRlbWVudCA9IHN0cihmeC5nZXQoInJlcXVpcmVkX3N0YXRlbWVudCIsICIiKSkKICAgIGFwcHJvdmVyID0gc3RyKGZ4LmdldCgiYXBwcm92ZXIiLCAiIikpLnN0cmlwKCkKICAgIHRzID0gc3RyKGZ4LmdldCgiYXBwcm92YWxfdGltZXN0YW1wIiwgIiIpKS5zdHJpcCgpCgogICAgYmFzZV92YWxpZCA9ICgKICAgICAgICBmeC5nZXQoInNjaGVtYSIpID09ICJ0YXUtc2NhbGluZy1odW1hbi1hcHByb3ZhbC1hcnRpZmFjdC12MC42LjIiCiAgICAgICAgYW5kIGRlY2lzaW9uIGluIFsiQVBQUk9WRV9SRVBMQVlfT05MWSIsICJERU5ZIiwgIlJFUVVFU1RfTU9SRV9FVklERU5DRSJdCiAgICAgICAgYW5kIGJvb2woYXBwcm92ZXIpCiAgICAgICAgYW5kIGJvb2wodHMpCiAgICAgICAgYW5kIGZ4LmdldCgic2NvcGUiKSA9PSAiY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfb25seSIKICAgICAgICBhbmQgImRvZXMgbm90IGF1dGhvcml6ZSBjbGFzc2lmaWVyIG11dGF0aW9uIiBpbiByZXF1aXJlZF9zdGF0ZW1lbnQKICAgICAgICBhbmQgbG9ja3MuZ2V0KCJydW50aW1lX211dGF0aW9uX2FsbG93ZWQiKSBpcyBGYWxzZQogICAgICAgIGFuZCBsb2Nrcy5nZXQoImNsYXNzaWZpZXJfbXV0YXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgiYXBwbGljYXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgiY2FsaWJyYXRpb25fYXBwbGllZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgicG9saWN5X2VuZm9yY2VkIikgaXMgRmFsc2UKICAgICkKCiAgICBpZiBkZWNpc2lvbiA9PSAiQVBQUk9WRV9SRVBMQVlfT05MWSIgYW5kIGJhc2VfdmFsaWQ6CiAgICAgICAgZXhwZWN0ZWRfb3V0Y29tZSA9ICJWQUxJRF9GT1JfUkVQTEFZX09OTFlfRklYVFVSRSIKICAgICAgICByZXBsYXlfYWxsb3dlZF9pZl9saXZlID0gVHJ1ZQogICAgZWxpZiBkZWNpc2lvbiA9PSAiREVOWSIgYW5kIGJhc2VfdmFsaWQ6CiAgICAgICAgZXhwZWN0ZWRfb3V0Y29tZSA9ICJERU5JQUxfRklYVFVSRV9CTE9DS1NfUkVQTEFZIgogICAgICAgIHJlcGxheV9hbGxvd2VkX2lmX2xpdmUgPSBGYWxzZQogICAgZWxpZiBkZWNpc2lvbiA9PSAiUkVRVUVTVF9NT1JFX0VWSURFTkNFIiBhbmQgYmFzZV92YWxpZDoKICAgICAgICBleHBlY3RlZF9vdXRjb21lID0gIk1PUkVfRVZJREVOQ0VfRklYVFVSRV9CTE9DS1NfUkVQTEFZIgogICAgICAgIHJlcGxheV9hbGxvd2VkX2lmX2xpdmUgPSBGYWxzZQogICAgZWxzZToKICAgICAgICBleHBlY3RlZF9vdXRjb21lID0gIklOVkFMSURfRklYVFVSRSIKICAgICAgICByZXBsYXlfYWxsb3dlZF9pZl9saXZlID0gRmFsc2UKCiAgICByZXR1cm4gewogICAgICAgICJmaXh0dXJlX25hbWUiOiBmeC5nZXQoImZpeHR1cmVfbmFtZSIpLAogICAgICAgICJhcHByb3ZhbF9kZWNpc2lvbiI6IGRlY2lzaW9uLAogICAgICAgICJmaXh0dXJlX3ZhbGlkIjogYm9vbChiYXNlX3ZhbGlkKSwKICAgICAgICAiZXhwZWN0ZWRfb3V0Y29tZSI6IGV4cGVjdGVkX291dGNvbWUsCiAgICAgICAgInJlcGxheV9hbGxvd2VkX2lmX2xpdmUiOiByZXBsYXlfYWxsb3dlZF9pZl9saXZlLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJmaXh0dXJlX29ubHkiOiBUcnVlLAogICAgfQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgcm93cyA9IHN1bW1hcnlbImZpeHR1cmVfcmVzdWx0cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihbclsiYXBwcm92YWxfZGVjaXNpb24iXSBmb3IgciBpbiByb3dzXSwgW2ludChyWyJmaXh0dXJlX3ZhbGlkIl0pIGZvciByIGluIHJvd3NdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkZpeHR1cmUgdmFsaWQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBGaXh0dXJlIFZhbGlkaXR5IikKICAgIHNhdmUoImFwcHJvdmFsX2ZpeHR1cmVfdmFsaWRpdHkucG5nIikKCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihbclsiYXBwcm92YWxfZGVjaXNpb24iXSBmb3IgciBpbiByb3dzXSwgW2ludChyWyJyZXBsYXlfYWxsb3dlZF9pZl9saXZlIl0pIGZvciByIGluIHJvd3NdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlJlcGxheSBhbGxvd2VkIGlmIGxpdmUiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBGaXh0dXJlIFJlcGxheSBTZW1hbnRpY3MiKQogICAgc2F2ZSgiYXBwcm92YWxfZml4dHVyZV9yZXBsYXlfc2VtYW50aWNzLnBuZyIpCgogICAgbG9ja3MgPSB7CiAgICAgICAgImxpdmVfYXBwcm92YWxfcHJlc2VudCI6IGludChzdW1tYXJ5WyJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiXSksCiAgICAgICAgImZpeHR1cmVfb25seSI6IGludChzdW1tYXJ5WyJmaXh0dXJlX29ubHkiXSksCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogaW50KHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGxvY2tzLmtleXMoKSksIGxpc3QobG9ja3MudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBGaXh0dXJlIExvY2sgU3RhdGUiKQogICAgc2F2ZSgiYXBwcm92YWxfZml4dHVyZV9sb2NrX3N0YXRlLnBuZyIpCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZXBvcnQocyk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC42LjUgQXBwcm92YWwgRml4dHVyZSBhbmQgRGVuaWFsIEZpeHR1cmUgVmFsaWRhdG9yIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzWydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgRml4dHVyZSBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBGaXh0dXJlIHN0YXR1czogYHtzWydmaXh0dXJlX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBGaXh0dXJlIGNvdW50OiBge3NbJ2ZpeHR1cmVfY291bnQnXX1gIiwKICAgICAgICBmIi0gVmFsaWQgZml4dHVyZSBjb3VudDogYHtzWyd2YWxpZF9maXh0dXJlX2NvdW50J119YCIsCiAgICAgICAgZiItIExpdmUgYXBwcm92YWwgcHJlc2VudDogYHtzWydsaXZlX2FwcHJvdmFsX3ByZXNlbnQnXX1gIiwKICAgICAgICBmIi0gQnJhbmNoIGNyZWF0ZWQ6IGB7c1snYnJhbmNoX2NyZWF0ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEZpeHR1cmUgTWF0cml4IiwKICAgICAgICAiIiwKICAgICAgICAifCBGaXh0dXJlIHwgRGVjaXNpb24gfCBWYWxpZCB8IEV4cGVjdGVkIG91dGNvbWUgfCBSZXBsYXkgaWYgbGl2ZSB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLXwtLS18IiwKICAgIF0KICAgIGZvciByIGluIHNbImZpeHR1cmVfcmVzdWx0cyJdOgogICAgICAgIGxpbmVzLmFwcGVuZCgKICAgICAgICAgICAgZiJ8IGB7clsnZml4dHVyZV9uYW1lJ119YCB8IGB7clsnYXBwcm92YWxfZGVjaXNpb24nXX1gIHwgYHtyWydmaXh0dXJlX3ZhbGlkJ119YCB8IGB7clsnZXhwZWN0ZWRfb3V0Y29tZSddfWAgfCBge3JbJ3JlcGxheV9hbGxvd2VkX2lmX2xpdmUnXX1gIHwiCiAgICAgICAgKQogICAgbGluZXMgKz0gWyIiLCAiIyMgRml4dHVyZSBGaWxlcyIsICIiXQogICAgZm9yIHAgaW4gc1siZml4dHVyZV9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIi0gYHtwfWAiKQogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgcCBpbiBzWyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc1siYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIGJhc2UgPSByanNvbihURU1QTEFURSkKICAgIGZpeHR1cmVfcGF0aHMgPSBbXQogICAgcmVzdWx0cyA9IFtdCgogICAgZm9yIGZpeHR1cmVfbmFtZSwgZGVjaXNpb24gaW4gREVDSVNJT05TOgogICAgICAgIGZ4ID0gbWFrZV9maXh0dXJlKGJhc2UsIGZpeHR1cmVfbmFtZSwgZGVjaXNpb24pCiAgICAgICAgcGF0aCA9IEZJWFRVUkVfRElSIC8gZiJ7Zml4dHVyZV9uYW1lfS5qc29uIgogICAgICAgIHdqc29uKHBhdGgsIGZ4KQogICAgICAgIGZpeHR1cmVfcGF0aHMuYXBwZW5kKHJlbChwYXRoKSkKICAgICAgICByZXN1bHRzLmFwcGVuZCh2YWxpZGF0ZV9maXh0dXJlKGZ4KSkKCiAgICB2YWxpZF9jb3VudCA9IHN1bSgxIGZvciByIGluIHJlc3VsdHMgaWYgclsiZml4dHVyZV92YWxpZCJdKQogICAgYXBwcm92YWxfZml4dHVyZSA9IG5leHQoKHIgZm9yIHIgaW4gcmVzdWx0cyBpZiByWyJhcHByb3ZhbF9kZWNpc2lvbiJdID09ICJBUFBST1ZFX1JFUExBWV9PTkxZIiksIE5vbmUpCiAgICBkZW5pYWxfZml4dHVyZSA9IG5leHQoKHIgZm9yIHIgaW4gcmVzdWx0cyBpZiByWyJhcHByb3ZhbF9kZWNpc2lvbiJdID09ICJERU5ZIiksIE5vbmUpCiAgICBtb3JlX2V2aWRlbmNlX2ZpeHR1cmUgPSBuZXh0KChyIGZvciByIGluIHJlc3VsdHMgaWYgclsiYXBwcm92YWxfZGVjaXNpb24iXSA9PSAiUkVRVUVTVF9NT1JFX0VWSURFTkNFIiksIE5vbmUpCgogICAgc2VtYW50aWNfcGFzcyA9ICgKICAgICAgICB2YWxpZF9jb3VudCA9PSBsZW4ocmVzdWx0cykKICAgICAgICBhbmQgYXBwcm92YWxfZml4dHVyZSBhbmQgYXBwcm92YWxfZml4dHVyZVsicmVwbGF5X2FsbG93ZWRfaWZfbGl2ZSJdIGlzIFRydWUKICAgICAgICBhbmQgZGVuaWFsX2ZpeHR1cmUgYW5kIGRlbmlhbF9maXh0dXJlWyJyZXBsYXlfYWxsb3dlZF9pZl9saXZlIl0gaXMgRmFsc2UKICAgICAgICBhbmQgbW9yZV9ldmlkZW5jZV9maXh0dXJlIGFuZCBtb3JlX2V2aWRlbmNlX2ZpeHR1cmVbInJlcGxheV9hbGxvd2VkX2lmX2xpdmUiXSBpcyBGYWxzZQogICAgKQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1hcHByb3ZhbC1maXh0dXJlLWRlbmlhbC1maXh0dXJlLXZhbGlkYXRvci12MC42LjUiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfdGVtcGxhdGUiOiByZWwoVEVNUExBVEUpLAogICAgICAgICJmaXh0dXJlX3N0YXR1cyI6ICJGSVhUVVJFU19WQUxJREFURURfX05PX0xJVkVfQVBQUk9WQUxfQ1JFQVRFRCIgaWYgc2VtYW50aWNfcGFzcyBlbHNlICJGSVhUVVJFX1ZBTElEQVRJT05fRkFJTEVEIiwKICAgICAgICAiZml4dHVyZV9jb3VudCI6IGxlbihyZXN1bHRzKSwKICAgICAgICAidmFsaWRfZml4dHVyZV9jb3VudCI6IHZhbGlkX2NvdW50LAogICAgICAgICJmaXh0dXJlX3Jlc3VsdHMiOiByZXN1bHRzLAogICAgICAgICJmaXh0dXJlX3BhdGhzIjogZml4dHVyZV9wYXRocywKICAgICAgICAiZml4dHVyZV9vbmx5IjogVHJ1ZSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF9wcmVzZW50IjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiAiRml4dHVyZSBzZW1hbnRpY3MgYXJlIHZhbGlkYXRlZC4gQSBmdXR1cmUgbGl2ZSBhcHByb3ZhbCBhcnRpZmFjdCBtYXkgYmUgdmFsaWRhdGVkIHNlcGFyYXRlbHksIGJ1dCBmaXh0dXJlcyBkbyBub3QgYXV0aG9yaXplIHJlcGxheS4iLAogICAgICAgICJib3VuZGFyeSI6ICJBcHByb3ZhbCBmaXh0dXJlcyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIHRlc3QgZml4dHVyZXMuIFRoZXkgYXJlIG5vdCBsaXZlIGFwcHJvdmFscywgZG8gbm90IGNyZWF0ZSBicmFuY2hlcywgZG8gbm90IG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBkbyBub3QgYXBwbHkgY2FsaWJyYXRpb24sIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjYuNiBzaG91bGQgYWRkIGEgbGl2ZS1hcHByb3ZhbCBoYW5kb2ZmIGNoZWNrIHRoYXQgcmVmdXNlcyB0byB0cmVhdCBmaXh0dXJlcyBhcyBhcHByb3ZhbHMuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAiYXBwcm92YWxfZml4dHVyZV92YWxpZGF0b3JfdjBfNl81Lmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9hcHByb3ZhbF9maXh0dXJlX3ZhbGlkYXRvci5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJhcHByb3ZhbF9maXh0dXJlX3ZhbGlkYXRvcl92MF82XzUubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2FwcHJvdmFsX2ZpeHR1cmVfdmFsaWRhdG9yLm1kIiwgcmVwb3J0KHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAiZml4dHVyZV9zdGF0dXMiOiBzdW1tYXJ5WyJmaXh0dXJlX3N0YXR1cyJdLAogICAgICAgICJmaXh0dXJlX2NvdW50Ijogc3VtbWFyeVsiZml4dHVyZV9jb3VudCJdLAogICAgICAgICJ2YWxpZF9maXh0dXJlX2NvdW50Ijogc3VtbWFyeVsidmFsaWRfZml4dHVyZV9jb3VudCJdLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiOiBzdW1tYXJ5WyJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiXSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBzdW1tYXJ5WyJicmFuY2hfY3JlYXRlZCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvYXBwcm92YWxfZml4dHVyZXMvbGF0ZXN0X2FwcHJvdmFsX2ZpeHR1cmVfdmFsaWRhdG9yLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT/"reports"/"approval_fixtures"/"README.md", """# Approval Fixture Reports

Current layer: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**

## Purpose

This folder stores approval/denial/more-evidence fixtures and validator reports. Fixtures are not live approvals.

## Primary command

```powershell
python scripts/benchmarks/validate_approval_fixtures.py
```

## README Update Rule

Update this mini README whenever fixture schemas, fixture semantics, or approval gate rules change.

Boundary: approval fixtures are local classifier-governance test fixtures only.
""")
write(ROOT/"visuals"/"approval_fixtures"/"README.md", """# Approval Fixture Visuals

Current layer: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**

## Purpose

This folder stores charts summarizing fixture semantics and locks.

## README Update Rule

Update this mini README whenever approval-fixture chart names or meanings change.

Boundary: approval-fixture visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"approval_fixtures"/"v0_6_5"/"README.md", """# v0.6.5 Approval Fixture Charts

Expected charts:

- `approval_fixture_validity.png`
- `approval_fixture_replay_semantics.png`
- `approval_fixture_lock_state.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local approval-fixture diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.4[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.3[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.4 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.5 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.4-ready |", "| Task routing matrix | geometry-aware / v0.6.5-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.4 |", "| Agent contract version sync | current / v0.6.5 |")
if "| Approval fixture validator |" not in r:
    r=r.replace("| Approval-gated replay charts | `visuals/approval_gated_replay/v0_6_4/` |\n",
                "| Approval-gated replay charts | `visuals/approval_gated_replay/v0_6_4/` |\n| Approval fixture validator | `reports/approval_fixtures/latest_approval_fixture_validator.md` |\n| Approval fixture charts | `visuals/approval_fixtures/v0_6_5/` |\n")
if "python scripts/benchmarks/validate_approval_fixtures.py" not in r:
    r=r.replace("python scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython scripts/benchmarks/validate_approval_fixtures.py\npython scripts/release/validate_release.py")
if "    approval_fixtures/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    approval_fixtures/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    approval_fixtures/\n")
section="""## Approval Fixture and Denial Fixture Validator v0.6.5

v0.6.5 creates and validates approval, denial, and more-evidence fixtures without creating any live approval.

Primary command:

```powershell
python scripts/benchmarks/validate_approval_fixtures.py
```

Primary outputs:

```text
reports/approval_fixtures/latest_approval_fixture_validator.json
reports/approval_fixtures/latest_approval_fixture_validator.md
reports/approval_fixtures/fixtures/v0_6_5/
visuals/approval_fixtures/v0_6_5/
```

Current lock:

```text
fixture_only: true
live_approval_present: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: approval fixtures are local classifier-governance test fixtures. They are not live approvals, do not create branches, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Approval Fixture and Denial Fixture Validator v0.6.5" not in r:
    r=r.replace("## Approval-Gated Replay Dry-Run v0.6.4", section+"## Approval-Gated Replay Dry-Run v0.6.4",1)
lesson="| L-047 | v0.6.4 emitted a blocked replay report because approval was invalid. | The system needs fixtures to prove approval, denial, and more-evidence decisions have distinct replay semantics. | Approval fixture validation must prove fixture semantics without treating fixtures as live approvals. |"
if "L-047" not in r:
    r=r.replace("| L-046 | v0.6.3 rejected template-only approval. | A failed approval validator should produce a blocked replay dry-run rather than silently stopping the lineage. | Approval-gated replay layers must emit explicit blocked reports when approval is invalid, preserving audit continuity without execution. |\n",
                "| L-046 | v0.6.3 rejected template-only approval. | A failed approval validator should produce a blocked replay dry-run rather than silently stopping the lineage. | Approval-gated replay layers must emit explicit blocked reports when approval is invalid, preserving audit continuity without execution. |\n"+lesson+"\n")
if "| v0.6.5 |" not in r:
    r=r.replace("| v0.6.4 | Approval-gated replay dry-run; emits blocked report unless approval validates. |\n",
                "| v0.6.4 | Approval-gated replay dry-run; emits blocked report unless approval validates. |\n| v0.6.5 | Approval fixture and denial fixture validator; fixtures only, no live approval. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**

Recommended goals:

- Refuse to treat fixtures as live approval artifacts.
- Require a separate live approval path outside fixture directories.
- Validate live approval presence without mutating classifier behavior.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "validate_approval_fixtures.py" not in s:
        s=s.replace("python scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_approval_gated_replay_dry_run.py\npython scripts/benchmarks/validate_approval_fixtures.py\npython -m unittest discover -s tests")
        s=s.replace("| Approval-gated replay patch | `reports/approval_gated_replay/`, `visuals/approval_gated_replay/`, approval validator | blocked replay dry-run + release validator; no mutation |\n",
                    "| Approval-gated replay patch | `reports/approval_gated_replay/`, `visuals/approval_gated_replay/`, approval validator | blocked replay dry-run + release validator; no mutation |\n| Approval fixture patch | `reports/approval_fixtures/`, `visuals/approval_fixtures/`, approval template | fixture validator + release validator; fixtures are not approval |\n")
    if name.endswith("task_routing_matrix.md") and "| Approval fixture patch |" not in s:
        s=s.replace("| Approval-gated replay patch | outer | validation | governance | approval validator + replay harness | blocked replay dry-run + charts + release validator | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` |\n",
                    "| Approval-gated replay patch | outer | validation | governance | approval validator + replay harness | blocked replay dry-run + charts + release validator | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` |\n| Approval fixture patch | outer | validation | governance | approval template + approval validator | fixture validator + charts + release validator | `reports/approval_fixtures/latest_approval_fixture_validator.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.5"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["approval_fixture_validator"]={
    "read_first":["reports/human_approval/human_approval_artifact_template_v0_6_2.json"],
    "validate":["python scripts/benchmarks/validate_approval_fixtures.py","python scripts/release/validate_release.py"],
    "evidence":["reports/approval_fixtures/latest_approval_fixture_validator.md","visuals/approval_fixtures/v0_6_5/"],
    "mutation_lock":"Fixtures are not live approvals; no branch creation or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.5 | Approval fixture and denial fixture validator |" not in t:
    t=t.replace("| v0.6.4 | Approval-gated replay dry-run | `python scripts/benchmarks/run_approval_gated_replay_dry_run.py` | Emits blocked replay report unless approval_valid is true | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` | `visuals/approval_gated_replay/v0_6_4/` |\n",
                "| v0.6.4 | Approval-gated replay dry-run | `python scripts/benchmarks/run_approval_gated_replay_dry_run.py` | Emits blocked replay report unless approval_valid is true | `reports/approval_gated_replay/latest_approval_gated_replay_dry_run.md` | `visuals/approval_gated_replay/v0_6_4/` |\n| v0.6.5 | Approval fixture and denial fixture validator | `python scripts/benchmarks/validate_approval_fixtures.py` | Validates approval/denial/more-evidence fixture semantics without live approval | `reports/approval_fixtures/latest_approval_fixture_validator.md` | `visuals/approval_fixtures/v0_6_5/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_5_approval_fixtures.md", f"""# TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator

Generated: {NOW}

## Purpose

Create and validate approval, denial, and request-more-evidence fixtures without treating fixtures as live approvals.

## Boundary

Approval fixtures are local classifier-governance test fixtures only. They do not create live approval, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.5 patch written")
