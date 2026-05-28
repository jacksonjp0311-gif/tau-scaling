
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"human_approval"/"v0_6_2"/"backups"/f"{p.name}_before_v0_6_2_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"generate_human_approval_template.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpSRVBMQVkgPSBST09UIC8gInJlcG9ydHMiIC8gImNhbmRpZGF0ZV9yZXBsYXkiIC8gImxhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX3JlcGxheV9oYXJuZXNzLmpzb24iCkNBTkRJREFURSA9IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FuZGlkYXRlX2JyYW5jaCIgLyAibGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfZ2F0ZS5qc29uIgpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImh1bWFuX2FwcHJvdmFsIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImh1bWFuX2FwcHJvdmFsIiAvICJ2MF82XzIiCgpBUFBST1ZBTF9URU1QTEFURSA9IHsKICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctaHVtYW4tYXBwcm92YWwtYXJ0aWZhY3QtdjAuNi4yIiwKICAgICJhcnRpZmFjdF9zdGF0dXMiOiAiVEVNUExBVEVfT05MWV9OT1RfQVBQUk9WRUQiLAogICAgImFwcHJvdmFsX2RlY2lzaW9uIjogIlVOU0VUIiwKICAgICJhbGxvd2VkX3ZhbHVlcyI6IFsiQVBQUk9WRV9SRVBMQVlfT05MWSIsICJERU5ZIiwgIlJFUVVFU1RfTU9SRV9FVklERU5DRSJdLAogICAgImFwcHJvdmVyIjogIiIsCiAgICAiYXBwcm92YWxfdGltZXN0YW1wIjogIiIsCiAgICAic2NvcGUiOiAiY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfb25seSIsCiAgICAic2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkIjogMC44LAogICAgImNhbmRpZGF0ZV9icmFuY2giOiAiY2FuZGlkYXRlL3YwLjYuMC10aHJlc2hvbGQtMC44LXJldmlldy1vbmx5IiwKICAgICJleHBsaWNpdF9sb2NrcyI6IHsKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9tdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImNsYXNzaWZpZXJfbXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UKICAgIH0sCiAgICAicmVxdWlyZWRfc3RhdGVtZW50IjogIkkgdW5kZXJzdGFuZCB0aGlzIGFwcHJvdmFsLCBpZiBzZXQgdG8gQVBQUk9WRV9SRVBMQVlfT05MWSwgYXV0aG9yaXplcyByZXBsYXkgb25seSBhbmQgZG9lcyBub3QgYXV0aG9yaXplIGNsYXNzaWZpZXIgbXV0YXRpb24sIHJ1bnRpbWUgbXV0YXRpb24sIGNhbGlicmF0aW9uIGFwcGxpY2F0aW9uLCBwcm9kdWN0aW9uIHVzZSwgc2lsaWNvbiB2YWxpZGF0aW9uLCBvciBwcm9kdWN0IGNsYWltcy4iLAogICAgIm5vdGVzIjogIiIKfQoKZGVmIHJqc29uKHApOgogICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwKToKICAgIHJldHVybiBzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICBnYXRlcyA9IHsKICAgICAgICAidGVtcGxhdGVfY3JlYXRlZCI6IDEsCiAgICAgICAgImFwcHJvdmFsX3ByZXNlbnQiOiBpbnQoc3VtbWFyeVsiaHVtYW5fYXBwcm92YWxfcHJlc2VudCJdKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsicmVwbGF5X2FsbG93ZWQiXSksCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIl0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVzLmtleXMoKSksIGxpc3QoZ2F0ZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJIdW1hbiBBcHByb3ZhbCBHYXRlIFN0YXRlIikKICAgIHNhdmUoImh1bWFuX2FwcHJvdmFsX2dhdGVfc3RhdGUucG5nIikKCiAgICBkZWNpc2lvbnMgPSB7c3VtbWFyeVsiYXBwcm92YWxfdGVtcGxhdGVfc3RhdHVzIl06IDF9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGRlY2lzaW9ucy5rZXlzKCkpLCBsaXN0KGRlY2lzaW9ucy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBBcnRpZmFjdCBUZW1wbGF0ZSBTdGF0dXMiKQogICAgc2F2ZSgiaHVtYW5fYXBwcm92YWxfdGVtcGxhdGVfc3RhdHVzLnBuZyIpCgogICAgbG9ja3MgPSBzdW1tYXJ5WyJsb2NrX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGxvY2tzLmtleXMoKSksIGxpc3QobG9ja3MudmFsdWVzKCkpKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBBcnRpZmFjdCBMb2NrIENvdW50cyIpCiAgICBzYXZlKCJodW1hbl9hcHByb3ZhbF9sb2NrX2NvdW50cy5wbmciKQogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVwb3J0KHMpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNi4yIEh1bWFuIEFwcHJvdmFsIEFydGlmYWN0IFRlbXBsYXRlIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzWydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQXBwcm92YWwgVGVtcGxhdGUgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gQXBwcm92YWwgdGVtcGxhdGUgc3RhdHVzOiBge3NbJ2FwcHJvdmFsX3RlbXBsYXRlX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBUZW1wbGF0ZSBwYXRoOiBge3NbJ2FwcHJvdmFsX3RlbXBsYXRlX3BhdGgnXX1gIiwKICAgICAgICBmIi0gSHVtYW4gYXBwcm92YWwgcHJlc2VudDogYHtzWydodW1hbl9hcHByb3ZhbF9wcmVzZW50J119YCIsCiAgICAgICAgZiItIFJlcGxheSBhbGxvd2VkOiBge3NbJ3JlcGxheV9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEJyYW5jaCBjcmVhdGlvbiBhbGxvd2VkOiBge3NbJ2JyYW5jaF9jcmVhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c1snbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBDYWxpYnJhdGlvbiBhcHBsaWVkOiBge3NbJ2NhbGlicmF0aW9uX2FwcGxpZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgVGVtcGxhdGUgSW5zdHJ1Y3Rpb25zIiwKICAgICAgICAiIiwKICAgICAgICBzWyJ0ZW1wbGF0ZV9pbnN0cnVjdGlvbnMiXSwKICAgICAgICAiIiwKICAgICAgICAiIyMgQXBwcm92YWwgQm91bmRhcnkiLAogICAgICAgICIiLAogICAgICAgIHNbImFwcHJvdmFsX2JvdW5kYXJ5Il0sCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENoYXJ0cyIsCiAgICAgICAgIiIsCiAgICBdCiAgICBmb3IgcCBpbiBzWyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc1siYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIHJlcGxheSA9IHJqc29uKFJFUExBWSkKICAgIGNhbmRpZGF0ZSA9IHJqc29uKENBTkRJREFURSkKCiAgICB0ZW1wbGF0ZSA9IGRpY3QoQVBQUk9WQUxfVEVNUExBVEUpCiAgICB0ZW1wbGF0ZVsic2VsZWN0ZWRfcmVwb3J0X29ubHlfdGhyZXNob2xkIl0gPSBjYW5kaWRhdGUuZ2V0KCJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiLCAwLjgpCiAgICB0ZW1wbGF0ZVsiY2FuZGlkYXRlX2JyYW5jaCJdID0gY2FuZGlkYXRlLmdldCgicHJvcG9zZWRfYnJhbmNoX25hbWUiLCB0ZW1wbGF0ZVsiY2FuZGlkYXRlX2JyYW5jaCJdKQogICAgdGVtcGxhdGVbImdlbmVyYXRlZF9hdCJdID0gZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCkKICAgIHRlbXBsYXRlX3BhdGggPSBPVVQgLyAiaHVtYW5fYXBwcm92YWxfYXJ0aWZhY3RfdGVtcGxhdGVfdjBfNl8yLmpzb24iCiAgICB3anNvbih0ZW1wbGF0ZV9wYXRoLCB0ZW1wbGF0ZSkKCiAgICBsb2NrX3ZhbHVlcyA9IHRlbXBsYXRlWyJleHBsaWNpdF9sb2NrcyJdCiAgICBmYWxzZV9sb2NrcyA9IHN1bSgxIGZvciB2IGluIGxvY2tfdmFsdWVzLnZhbHVlcygpIGlmIHYgaXMgRmFsc2UpCiAgICB0cnVlX2xvY2tzID0gc3VtKDEgZm9yIHYgaW4gbG9ja192YWx1ZXMudmFsdWVzKCkgaWYgdiBpcyBUcnVlKQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1odW1hbi1hcHByb3ZhbC1hcnRpZmFjdC10ZW1wbGF0ZS12MC42LjIiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfY2FuZGlkYXRlX3JlcGxheSI6ICJyZXBvcnRzL2NhbmRpZGF0ZV9yZXBsYXkvbGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfcmVwbGF5X2hhcm5lc3MuanNvbiIsCiAgICAgICAgImlucHV0X2NhbmRpZGF0ZV9icmFuY2hfZ2F0ZSI6ICJyZXBvcnRzL2NhbmRpZGF0ZV9icmFuY2gvbGF0ZXN0X2NhbmRpZGF0ZV9icmFuY2hfZ2F0ZS5qc29uIiwKICAgICAgICAiYXBwcm92YWxfdGVtcGxhdGVfcGF0aCI6IHJlbCh0ZW1wbGF0ZV9wYXRoKSwKICAgICAgICAiYXBwcm92YWxfdGVtcGxhdGVfc3RhdHVzIjogIlRFTVBMQVRFX0NSRUFURURfX05PVF9BUFBST1ZFRCIsCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3JlcXVpcmVkIjogVHJ1ZSwKICAgICAgICAiaHVtYW5fYXBwcm92YWxfcHJlc2VudCI6IEZhbHNlLAogICAgICAgICJhcHByb3ZhbF9kZWNpc2lvbiI6ICJVTlNFVCIsCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAibG9ja19jb3VudHMiOiB7ImZhbHNlX2xvY2tzIjogZmFsc2VfbG9ja3MsICJ0cnVlX2xvY2tzIjogdHJ1ZV9sb2Nrc30sCiAgICAgICAgInRlbXBsYXRlX2luc3RydWN0aW9ucyI6ICJUbyBhcHByb3ZlIHJlcGxheSBpbiBhIGZ1dHVyZSBsYXllciwgY29weSB0aGUgdGVtcGxhdGUgdG8gYSBsb2NhbCBhcHByb3ZhbCBhcnRpZmFjdCwgc2V0IGFwcHJvdmFsX2RlY2lzaW9uIHRvIEFQUFJPVkVfUkVQTEFZX09OTFksIGZpbGwgYXBwcm92ZXIgYW5kIHRpbWVzdGFtcCwgYW5kIHByZXNlcnZlIGV2ZXJ5IGV4cGxpY2l0IGxvY2sgdW5sZXNzIGEgc2VwYXJhdGUgc3Ryb25nZXIgZ292ZXJuYW5jZSBhcnRpZmFjdCBleGlzdHMuIiwKICAgICAgICAiYXBwcm92YWxfYm91bmRhcnkiOiAiVGhpcyB2MC42LjIgbGF5ZXIgY3JlYXRlcyBhIHRlbXBsYXRlIG9ubHkuIEl0IGRvZXMgbm90IGFwcHJvdmUgcmVwbGF5LCBjcmVhdGUgYSBicmFuY2gsIGFwcGx5IGNhbGlicmF0aW9uLCBvciBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvci4iLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJVc2UgdGhpcyB0ZW1wbGF0ZSBmb3IgYSBmdXR1cmUgZXhwbGljaXQgYXBwcm92YWwgb3IgZGVuaWFsIGFydGlmYWN0LiBEbyBub3QgcmVwbGF5IG9yIGNyZWF0ZSBicmFuY2hlcyBmcm9tIHRoZSB0ZW1wbGF0ZSBhbG9uZS4iLAogICAgICAgICJib3VuZGFyeSI6ICJIdW1hbiBhcHByb3ZhbCBhcnRpZmFjdCB0ZW1wbGF0ZXMgYXJlIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSB0ZW1wbGF0ZXMuIFRoZXkgZG8gbm90IGNyZWF0ZSBhcHByb3ZhbCBieSB0aGVtc2VsdmVzLCBkbyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjYuMyBzaG91bGQgYWRkIGFuIGFwcHJvdmFsIGFydGlmYWN0IHZhbGlkYXRvciB0aGF0IHJlZnVzZXMgcmVwbGF5IHVubGVzcyB0aGUgYXBwcm92YWwgYXJ0aWZhY3QgaXMgZXhwbGljaXRseSBjb21wbGV0ZWQuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAiaHVtYW5fYXBwcm92YWxfdGVtcGxhdGVfcmVwb3J0X3YwXzZfMi5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfaHVtYW5fYXBwcm92YWxfdGVtcGxhdGVfcmVwb3J0Lmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gImh1bWFuX2FwcHJvdmFsX3RlbXBsYXRlX3JlcG9ydF92MF82XzIubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2h1bWFuX2FwcHJvdmFsX3RlbXBsYXRlX3JlcG9ydC5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImFwcHJvdmFsX3RlbXBsYXRlX3N0YXR1cyI6IHN1bW1hcnlbImFwcHJvdmFsX3RlbXBsYXRlX3N0YXR1cyJdLAogICAgICAgICJhcHByb3ZhbF90ZW1wbGF0ZV9wYXRoIjogc3VtbWFyeVsiYXBwcm92YWxfdGVtcGxhdGVfcGF0aCJdLAogICAgICAgICJodW1hbl9hcHByb3ZhbF9yZXF1aXJlZCI6IHN1bW1hcnlbImh1bWFuX2FwcHJvdmFsX3JlcXVpcmVkIl0sCiAgICAgICAgImh1bWFuX2FwcHJvdmFsX3ByZXNlbnQiOiBzdW1tYXJ5WyJodW1hbl9hcHByb3ZhbF9wcmVzZW50Il0sCiAgICAgICAgImFwcHJvdmFsX2RlY2lzaW9uIjogc3VtbWFyeVsiYXBwcm92YWxfZGVjaXNpb24iXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9odW1hbl9hcHByb3ZhbC9sYXRlc3RfaHVtYW5fYXBwcm92YWxfdGVtcGxhdGVfcmVwb3J0Lm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==").decode())

write(ROOT/"reports"/"human_approval"/"README.md", """# Human Approval Artifact Reports

Current layer: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**

## Purpose

This folder stores human approval / denial templates and reports. Templates do not approve anything by themselves.

## Primary command

```powershell
python scripts/benchmarks/generate_human_approval_template.py
```

## README Update Rule

Update this mini README whenever approval schemas, approval requirements, or signoff rules change.

Boundary: approval templates are local classifier-governance templates only.
""")
write(ROOT/"visuals"/"human_approval"/"README.md", """# Human Approval Visuals

Current layer: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**

## Purpose

This folder stores charts summarizing approval-template state.

## README Update Rule

Update this mini README whenever approval chart names or meanings change.

Boundary: approval visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"human_approval"/"v0_6_2"/"README.md", """# v0.6.2 Human Approval Charts

Expected charts:

- `human_approval_gate_state.png`
- `human_approval_template_status.png`
- `human_approval_lock_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local approval-template diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.1[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.0[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.1 - Candidate Branch Replay Harness**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.1 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.2 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.1-ready |", "| Task routing matrix | geometry-aware / v0.6.2-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.1 |", "| Agent contract version sync | current / v0.6.2 |")
if "| Human approval template |" not in r:
    r=r.replace("| Candidate replay charts | `visuals/candidate_replay/v0_6_1/` |\n",
                "| Candidate replay charts | `visuals/candidate_replay/v0_6_1/` |\n| Human approval template | `reports/human_approval/latest_human_approval_template_report.md` |\n| Human approval charts | `visuals/human_approval/v0_6_2/` |\n")
if "python scripts/benchmarks/generate_human_approval_template.py" not in r:
    r=r.replace("python scripts/benchmarks/run_candidate_branch_replay_harness.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_candidate_branch_replay_harness.py\npython scripts/benchmarks/generate_human_approval_template.py\npython scripts/release/validate_release.py")
if "    human_approval/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    human_approval/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    human_approval/\n")
section="""## Human Approval Artifact Template v0.6.2

v0.6.2 creates the explicit human approval / denial artifact template. A template is not an approval.

Primary command:

```powershell
python scripts/benchmarks/generate_human_approval_template.py
```

Primary outputs:

```text
reports/human_approval/human_approval_artifact_template_v0_6_2.json
reports/human_approval/latest_human_approval_template_report.json
reports/human_approval/latest_human_approval_template_report.md
visuals/human_approval/v0_6_2/
```

Current lock:

```text
human_approval_required: true
human_approval_present: false
approval_decision: UNSET
replay_allowed: false
branch_creation_allowed: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: human approval templates are local classifier-governance templates. They do not create approval by themselves, do not change classifier behavior, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Human Approval Artifact Template v0.6.2" not in r:
    r=r.replace("## Candidate Branch Replay Harness v0.6.1", section+"## Candidate Branch Replay Harness v0.6.1",1)
lesson="| L-044 | v0.6.1 correctly blocked replay because no human approval artifact existed. | Blocking replay is useful only if the system provides an explicit approval/denial artifact format. | Approval templates must be created before approval validation; templates alone do not authorize replay, branching, or mutation. |"
if "L-044" not in r:
    r=r.replace("| L-043 | v0.6.0 allowed a branch proposal but confirmed human approval was absent. | Proposal-readiness can be mistaken for replay-readiness unless replay is separately blocked. | Candidate replay harnesses must remain blocked until an explicit human approval artifact exists. |\n",
                "| L-043 | v0.6.0 allowed a branch proposal but confirmed human approval was absent. | Proposal-readiness can be mistaken for replay-readiness unless replay is separately blocked. | Candidate replay harnesses must remain blocked until an explicit human approval artifact exists. |\n"+lesson+"\n")
if "| v0.6.2 |" not in r:
    r=r.replace("| v0.6.1 | Candidate branch replay harness; replay blocked until explicit approval artifact exists. |\n",
                "| v0.6.1 | Candidate branch replay harness; replay blocked until explicit approval artifact exists. |\n| v0.6.2 | Human approval artifact template; template only, no approval by default. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**

Recommended goals:

- Validate a completed approval or denial artifact.
- Refuse replay unless approval_decision is explicitly APPROVE_REPLAY_ONLY.
- Keep default runtime behavior unchanged.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "generate_human_approval_template.py" not in s:
        s=s.replace("python scripts/benchmarks/run_candidate_branch_replay_harness.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_candidate_branch_replay_harness.py\npython scripts/benchmarks/generate_human_approval_template.py\npython -m unittest discover -s tests")
        s=s.replace("| Candidate replay harness patch | `reports/candidate_replay/`, `visuals/candidate_replay/`, candidate gate | replay harness + release validator; replay blocked by default |\n",
                    "| Candidate replay harness patch | `reports/candidate_replay/`, `visuals/candidate_replay/`, candidate gate | replay harness + release validator; replay blocked by default |\n| Human approval template patch | `reports/human_approval/`, `visuals/human_approval/`, replay harness | approval template + release validator; no approval by default |\n")
    if name.endswith("task_routing_matrix.md") and "| Human approval template patch |" not in s:
        s=s.replace("| Candidate replay harness patch | outer | validation | governance | candidate gate + signoff | replay harness + charts + release validator | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` |\n",
                    "| Candidate replay harness patch | outer | validation | governance | candidate gate + signoff | replay harness + charts + release validator | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` |\n| Human approval template patch | outer | governance | review | replay harness + candidate gate | approval template + charts + release validator | `reports/human_approval/latest_human_approval_template_report.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.2"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["human_approval_template"]={
    "read_first":["reports/candidate_replay/latest_candidate_branch_replay_harness.json"],
    "validate":["python scripts/benchmarks/generate_human_approval_template.py","python scripts/release/validate_release.py"],
    "evidence":["reports/human_approval/latest_human_approval_template_report.md","visuals/human_approval/v0_6_2/"],
    "mutation_lock":"Template only; no approval, replay, branch creation, or classifier mutation by default."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.2 | Human approval artifact template |" not in t:
    t=t.replace("| v0.6.1 | Candidate branch replay harness | `python scripts/benchmarks/run_candidate_branch_replay_harness.py` | Prepares replay plan but blocks replay until explicit approval artifact exists | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` | `visuals/candidate_replay/v0_6_1/` |\n",
                "| v0.6.1 | Candidate branch replay harness | `python scripts/benchmarks/run_candidate_branch_replay_harness.py` | Prepares replay plan but blocks replay until explicit approval artifact exists | `reports/candidate_replay/latest_candidate_branch_replay_harness.md` | `visuals/candidate_replay/v0_6_1/` |\n| v0.6.2 | Human approval artifact template | `python scripts/benchmarks/generate_human_approval_template.py` | Creates approval/denial template only; no approval by default | `reports/human_approval/latest_human_approval_template_report.md` | `visuals/human_approval/v0_6_2/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_2_human_approval_template.md", f"""# TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template

Generated: {NOW}

## Purpose

Create the explicit human approval / denial artifact template. The template itself does not approve replay.

## Boundary

Human approval templates are local classifier-governance templates only. They do not create approval by themselves, do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.2 patch written")
