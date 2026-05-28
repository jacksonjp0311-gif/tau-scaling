
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"blocked_continuity"/"v0_6_8"/"backups"/f"{p.name}_before_v0_6_8_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_blocked_state_continuity_ledger.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpFWEVDVVRPUiA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmVwbGF5X2V4ZWN1dG9yIiAvICJsYXRlc3RfYXBwcm92YWxfZ2F0ZWRfcmVwbGF5X2V4ZWN1dG9yLmpzb24iCkhBTkRPRkYgPSBST09UIC8gInJlcG9ydHMiIC8gImxpdmVfYXBwcm92YWxfaGFuZG9mZiIgLyAibGF0ZXN0X2xpdmVfYXBwcm92YWxfaGFuZG9mZl9jaGVjay5qc29uIgpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gImJsb2NrZWRfY29udGludWl0eSIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJibG9ja2VkX2NvbnRpbnVpdHkiIC8gInYwXzZfOCIKTEVER0VSID0gT1VUIC8gImJsb2NrZWRfc3RhdGVfY29udGludWl0eV9sZWRnZXIuanNvbmwiCgpkZWYgcmpzb24ocCk6CiAgICByZXR1cm4ganNvbi5sb2FkcyhwLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgYXBwZW5kX2pzb25sKHAsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgd2l0aCBwLm9wZW4oImEiLCBlbmNvZGluZz0idXRmLTgiKSBhcyBmOgogICAgICAgIGYud3JpdGUoanNvbi5kdW1wcyh4LCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iKQoKZGVmIHJlbChwKToKICAgIHJldHVybiBzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgcmVhZF9sZWRnZXIocCk6CiAgICBpZiBub3QgcC5leGlzdHMoKToKICAgICAgICByZXR1cm4gW10KICAgIHJvd3MgPSBbXQogICAgZm9yIGxpbmUgaW4gcC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04Iikuc3BsaXRsaW5lcygpOgogICAgICAgIGlmIGxpbmUuc3RyaXAoKToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgcm93cy5hcHBlbmQoanNvbi5sb2FkcyhsaW5lKSkKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgICAgIHBhc3MKICAgIHJldHVybiByb3dzCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICBnYXRlcyA9IHsKICAgICAgICAiZXhlY3V0b3JfYmxvY2tlZCI6IGludChzdW1tYXJ5WyJleGVjdXRvcl9ibG9ja2VkIl0pLAogICAgICAgICJoYW5kb2ZmX2Jsb2NrZWQiOiBpbnQoc3VtbWFyeVsiaGFuZG9mZl9ibG9ja2VkIl0pLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiOiBpbnQoc3VtbWFyeVsibGl2ZV9hcHByb3ZhbF9wcmVzZW50Il0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdKSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZXMua2V5cygpKSwgbGlzdChnYXRlcy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQm9vbGVhbiBzdGF0ZSIpCiAgICBwbHQudGl0bGUoIkJsb2NrZWQtU3RhdGUgQ29udGludWl0eSBTbmFwc2hvdCIpCiAgICBzYXZlKCJibG9ja2VkX2NvbnRpbnVpdHlfc25hcHNob3QucG5nIikKCiAgICBsZWRnZXJfY291bnRzID0gc3VtbWFyeVsibGVkZ2VyX3N0YXR1c19jb3VudHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChsZWRnZXJfY291bnRzLmtleXMoKSksIGxpc3QobGVkZ2VyX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiTGVkZ2VyIGVudHJpZXMiKQogICAgcGx0LnRpdGxlKCJCbG9ja2VkLVN0YXRlIENvbnRpbnVpdHkgTGVkZ2VyIikKICAgIHNhdmUoImJsb2NrZWRfY29udGludWl0eV9sZWRnZXJfY291bnRzLnBuZyIpCgogICAgdGltZWxpbmUgPSBzdW1tYXJ5WyJsZWRnZXJfdGFpbCJdCiAgICBsYWJlbHMgPSBbZiJlbnRyeV97aSsxfSIgZm9yIGksIF8gaW4gZW51bWVyYXRlKHRpbWVsaW5lKV0KICAgIHZhbHMgPSBbMSBmb3IgXyBpbiB0aW1lbGluZV0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOSwgNCkpCiAgICBwbHQuYmFyKGxhYmVscywgdmFscykKICAgIHBsdC55bGFiZWwoIlJlY29yZGVkIikKICAgIHBsdC50aXRsZSgiQmxvY2tlZC1TdGF0ZSBMZWRnZXIgVGFpbCIpCiAgICBzYXZlKCJibG9ja2VkX2NvbnRpbnVpdHlfdGFpbC5wbmciKQogICAgcmV0dXJuIHBhdGhzCgpkZWYgcmVwb3J0KHMpOgogICAgbGluZXMgPSBbCiAgICAgICAgIiMgVGF1IFNjYWxpbmcgdjAuNi44IEJsb2NrZWQtU3RhdGUgQ29udGludWl0eSBMZWRnZXIiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDb250aW51aXR5IFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIENvbnRpbnVpdHkgc3RhdHVzOiBge3NbJ2NvbnRpbnVpdHlfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIEV4ZWN1dG9yIHN0YXR1czogYHtzWydleGVjdXRvcl9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gSGFuZG9mZiBzdGF0dXM6IGB7c1snaGFuZG9mZl9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gTGVkZ2VyIHBhdGg6IGB7c1snbGVkZ2VyX3BhdGgnXX1gIiwKICAgICAgICBmIi0gTGVkZ2VyIGVudHJpZXM6IGB7c1snbGVkZ2VyX2VudHJ5X2NvdW50J119YCIsCiAgICAgICAgZiItIEV4ZWN1dG9yIGJsb2NrZWQ6IGB7c1snZXhlY3V0b3JfYmxvY2tlZCddfWAiLAogICAgICAgIGYiLSBIYW5kb2ZmIGJsb2NrZWQ6IGB7c1snaGFuZG9mZl9ibG9ja2VkJ119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c1snbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBBcHBsaWNhdGlvbiBhbGxvd2VkOiBge3NbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ3VycmVudCBCbG9jayBSZWFzb24iLAogICAgICAgICIiLAogICAgICAgIHNbImJsb2NrX3JlYXNvbiJdLAogICAgICAgICIiLAogICAgICAgICIjIyBMZWRnZXIgVGFpbCIsCiAgICAgICAgIiIsCiAgICAgICAgInwgSW5kZXggfCBWZXJzaW9uIHwgRXhlY3V0b3Igc3RhdHVzIHwgSGFuZG9mZiBzdGF0dXMgfCBSZXBsYXkgYWxsb3dlZCB8IiwKICAgICAgICAifC0tLTp8LS0tfC0tLXwtLS18LS0tfCIsCiAgICBdCiAgICBmb3IgaSwgcm93IGluIGVudW1lcmF0ZShzWyJsZWRnZXJfdGFpbCJdLCAxKToKICAgICAgICBsaW5lcy5hcHBlbmQoCiAgICAgICAgICAgIGYifCB7aX0gfCBge3Jvdy5nZXQoJ3ZlcnNpb24nKX1gIHwgYHtyb3cuZ2V0KCdleGVjdXRvcl9zdGF0dXMnKX1gIHwgYHtyb3cuZ2V0KCdoYW5kb2ZmX3N0YXR1cycpfWAgfCBge3Jvdy5nZXQoJ3JlcGxheV9hbGxvd2VkJyl9YCB8IgogICAgICAgICkKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBleGVjdXRvciA9IHJqc29uKEVYRUNVVE9SKQogICAgaGFuZG9mZiA9IHJqc29uKEhBTkRPRkYpCgogICAgZXhlY3V0b3JfYmxvY2tlZCA9IGV4ZWN1dG9yLmdldCgiZXhlY3V0b3Jfc3RhdHVzIikgPT0gIkVYRUNVVE9SX0JMT0NLRURfX0xJVkVfQVBQUk9WQUxfSEFORE9GRl9OT1RfVkFMSUQiCiAgICBoYW5kb2ZmX2Jsb2NrZWQgPSBzdHIoaGFuZG9mZi5nZXQoImhhbmRvZmZfc3RhdHVzIiwgIiIpKS5zdGFydHN3aXRoKCJIQU5ET0ZGX0JMT0NLRUQiKQogICAgcmVwbGF5X2FsbG93ZWQgPSBib29sKGV4ZWN1dG9yLmdldCgiZXhlY3V0b3JfYWxsb3dlZCIpIGFuZCBoYW5kb2ZmLmdldCgicmVwbGF5X2FsbG93ZWQiKSkKCiAgICBlbnRyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLWJsb2NrZWQtc3RhdGUtY29udGludWl0eS1sZWRnZXItZW50cnktdjAuNi44IiwKICAgICAgICAidmVyc2lvbiI6ICJ2MC42LjgiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiZXhlY3V0b3Jfc3RhdHVzIjogZXhlY3V0b3IuZ2V0KCJleGVjdXRvcl9zdGF0dXMiKSwKICAgICAgICAiaGFuZG9mZl9zdGF0dXMiOiBoYW5kb2ZmLmdldCgiaGFuZG9mZl9zdGF0dXMiKSwKICAgICAgICAiZXhlY3V0b3JfYmxvY2tlZCI6IGJvb2woZXhlY3V0b3JfYmxvY2tlZCksCiAgICAgICAgImhhbmRvZmZfYmxvY2tlZCI6IGJvb2woaGFuZG9mZl9ibG9ja2VkKSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF9wcmVzZW50IjogYm9vbChoYW5kb2ZmLmdldCgibGl2ZV9hcHByb3ZhbF9wcmVzZW50IikpLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ZhbGlkIjogYm9vbChoYW5kb2ZmLmdldCgibGl2ZV9hcHByb3ZhbF92YWxpZCIpKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBib29sKHJlcGxheV9hbGxvd2VkKSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogYm9vbChleGVjdXRvci5nZXQoImV4ZWN1dG9yX3JhbiIpKSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAiYmxvY2tfcmVhc29uIjogZXhlY3V0b3IuZ2V0KCJibG9ja19yZWFzb24iLCAiTGl2ZSBhcHByb3ZhbCBoYW5kb2ZmIGlzIG5vdCB2YWxpZCBmb3IgcmVwbGF5LiIpLAogICAgfQogICAgYXBwZW5kX2pzb25sKExFREdFUiwgZW50cnkpCiAgICByb3dzID0gcmVhZF9sZWRnZXIoTEVER0VSKQoKICAgIHN0YXR1c19jb3VudHMgPSB7fQogICAgZm9yIHJvdyBpbiByb3dzOgogICAgICAgIGtleSA9IHJvdy5nZXQoImV4ZWN1dG9yX3N0YXR1cyIsICJVTktOT1dOIikKICAgICAgICBzdGF0dXNfY291bnRzW2tleV0gPSBzdGF0dXNfY291bnRzLmdldChrZXksIDApICsgMQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1ibG9ja2VkLXN0YXRlLWNvbnRpbnVpdHktbGVkZ2VyLXYwLjYuOCIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9yZXBsYXlfZXhlY3V0b3IiOiByZWwoRVhFQ1VUT1IpLAogICAgICAgICJpbnB1dF9saXZlX2FwcHJvdmFsX2hhbmRvZmYiOiByZWwoSEFORE9GRiksCiAgICAgICAgImNvbnRpbnVpdHlfc3RhdHVzIjogIkJMT0NLRURfU1RBVEVfUkVDT1JERURfX05PX0VYRUNVVElPTiIsCiAgICAgICAgImxlZGdlcl9wYXRoIjogcmVsKExFREdFUiksCiAgICAgICAgImxlZGdlcl9lbnRyeV9jb3VudCI6IGxlbihyb3dzKSwKICAgICAgICAibGVkZ2VyX3N0YXR1c19jb3VudHMiOiBzdGF0dXNfY291bnRzLAogICAgICAgICJsZWRnZXJfdGFpbCI6IHJvd3NbLTU6XSwKICAgICAgICAiZXhlY3V0b3Jfc3RhdHVzIjogZXhlY3V0b3IuZ2V0KCJleGVjdXRvcl9zdGF0dXMiKSwKICAgICAgICAiaGFuZG9mZl9zdGF0dXMiOiBoYW5kb2ZmLmdldCgiaGFuZG9mZl9zdGF0dXMiKSwKICAgICAgICAiZXhlY3V0b3JfYmxvY2tlZCI6IGJvb2woZXhlY3V0b3JfYmxvY2tlZCksCiAgICAgICAgImhhbmRvZmZfYmxvY2tlZCI6IGJvb2woaGFuZG9mZl9ibG9ja2VkKSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF9wcmVzZW50IjogYm9vbChoYW5kb2ZmLmdldCgibGl2ZV9hcHByb3ZhbF9wcmVzZW50IikpLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ZhbGlkIjogYm9vbChoYW5kb2ZmLmdldCgibGl2ZV9hcHByb3ZhbF92YWxpZCIpKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBib29sKHJlcGxheV9hbGxvd2VkKSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiYmxvY2tfcmVhc29uIjogZW50cnlbImJsb2NrX3JlYXNvbiJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJQcmVzZXJ2ZSBibG9ja2VkIHN0YXRlIGFzIGV2aWRlbmNlLiBEbyBub3QgcmVwbGF5LCBjcmVhdGUgYnJhbmNoZXMsIG9yIG11dGF0ZSBiZWhhdmlvciB3aXRob3V0IGEgdmFsaWQgbGl2ZSBhcHByb3ZhbCBoYW5kb2ZmLiIsCiAgICAgICAgImJvdW5kYXJ5IjogIkJsb2NrZWQtc3RhdGUgY29udGludWl0eSBsZWRnZXJzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgbWVtb3J5IGFydGlmYWN0cy4gVGhleSBwcmVzZXJ2ZSB3aHkgZXhlY3V0aW9uIHdhcyBibG9ja2VkLiBUaGV5IGRvIG5vdCBjcmVhdGUgbGl2ZSBhcHByb3ZhbCwgZXhlY3V0ZSByZXBsYXkgY29tbWFuZHMsIGNyZWF0ZSBicmFuY2hlcywgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFwcGx5IGNhbGlicmF0aW9uLCBvciB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNi45IHNob3VsZCBhZGQgYmxvY2tlZC1zdGF0ZSB0cmVuZCByZXZpZXcgYW5kIHJldGlyZW1lbnQgY3JpdGVyaWEgYmVmb3JlIGNvbnRpbnVpbmcgdG93YXJkIGFueSBsaXZlIGFwcHJvdmFsIHBhdGh3YXkuIiwKICAgIH0KICAgIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0gPSBjaGFydHMoc3VtbWFyeSkKCiAgICB3anNvbihPVVQgLyAiYmxvY2tlZF9zdGF0ZV9jb250aW51aXR5X3YwXzZfOC5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfYmxvY2tlZF9zdGF0ZV9jb250aW51aXR5Lmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gImJsb2NrZWRfc3RhdGVfY29udGludWl0eV92MF82XzgubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2Jsb2NrZWRfc3RhdGVfY29udGludWl0eS5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImNvbnRpbnVpdHlfc3RhdHVzIjogc3VtbWFyeVsiY29udGludWl0eV9zdGF0dXMiXSwKICAgICAgICAibGVkZ2VyX2VudHJ5X2NvdW50Ijogc3VtbWFyeVsibGVkZ2VyX2VudHJ5X2NvdW50Il0sCiAgICAgICAgImV4ZWN1dG9yX3N0YXR1cyI6IHN1bW1hcnlbImV4ZWN1dG9yX3N0YXR1cyJdLAogICAgICAgICJoYW5kb2ZmX3N0YXR1cyI6IHN1bW1hcnlbImhhbmRvZmZfc3RhdHVzIl0sCiAgICAgICAgImV4ZWN1dG9yX2Jsb2NrZWQiOiBzdW1tYXJ5WyJleGVjdXRvcl9ibG9ja2VkIl0sCiAgICAgICAgImhhbmRvZmZfYmxvY2tlZCI6IHN1bW1hcnlbImhhbmRvZmZfYmxvY2tlZCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvYmxvY2tlZF9jb250aW51aXR5L2xhdGVzdF9ibG9ja2VkX3N0YXRlX2NvbnRpbnVpdHkubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"blocked_continuity"/"README.md", """# Blocked-State Continuity Reports

Current layer: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**

## Purpose

This folder stores continuity reports and ledger entries for blocked execution states.

## Primary command

```powershell
python scripts/benchmarks/run_blocked_state_continuity_ledger.py
```

## README Update Rule

Update this mini README whenever blocked-state ledger schemas, retirement rules, or execution-boundary rules change.

Boundary: blocked-state ledgers are local classifier-governance memory artifacts only.
""")
write(ROOT/"visuals"/"blocked_continuity"/"README.md", """# Blocked-State Continuity Visuals

Current layer: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**

## Purpose

This folder stores charts summarizing blocked execution continuity.

## README Update Rule

Update this mini README whenever blocked-continuity chart names or meanings change.

Boundary: blocked-continuity visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"blocked_continuity"/"v0_6_8"/"README.md", """# v0.6.8 Blocked-State Continuity Charts

Expected charts:

- `blocked_continuity_snapshot.png`
- `blocked_continuity_ledger_counts.png`
- `blocked_continuity_tail.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local blocked-continuity diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.7[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.6[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.7 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.8 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.7-ready |", "| Task routing matrix | geometry-aware / v0.6.8-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.7 |", "| Agent contract version sync | current / v0.6.8 |")
if "| Blocked-state continuity |" not in r:
    r=r.replace("| Replay executor charts | `visuals/replay_executor/v0_6_7/` |\n",
                "| Replay executor charts | `visuals/replay_executor/v0_6_7/` |\n| Blocked-state continuity | `reports/blocked_continuity/latest_blocked_state_continuity.md` |\n| Blocked-state continuity charts | `visuals/blocked_continuity/v0_6_8/` |\n")
if "python scripts/benchmarks/run_blocked_state_continuity_ledger.py" not in r:
    r=r.replace("python scripts/benchmarks/run_approval_gated_replay_executor.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_approval_gated_replay_executor.py\npython scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython scripts/release/validate_release.py")
if "    blocked_continuity/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    blocked_continuity/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    blocked_continuity/\n")
section="""## Blocked-State Continuity Ledger v0.6.8

v0.6.8 records blocked executor state as durable continuity evidence.

Primary command:

```powershell
python scripts/benchmarks/run_blocked_state_continuity_ledger.py
```

Primary outputs:

```text
reports/blocked_continuity/blocked_state_continuity_ledger.jsonl
reports/blocked_continuity/latest_blocked_state_continuity.json
reports/blocked_continuity/latest_blocked_state_continuity.md
visuals/blocked_continuity/v0_6_8/
```

Current expected lock:

```text
continuity_status: BLOCKED_STATE_RECORDED__NO_EXECUTION
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: blocked-state continuity ledgers are local classifier-governance memory artifacts. They preserve why execution was blocked. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Blocked-State Continuity Ledger v0.6.8" not in r:
    r=r.replace("## Approval-Gated Replay Executor v0.6.7", section+"## Approval-Gated Replay Executor v0.6.7",1)
lesson="| L-050 | v0.6.7 blocked the executor because live approval handoff was invalid. | Repeated blocked execution states should be preserved as continuity evidence, not treated as no-op failures. | Blocked executor states must append to a continuity ledger so future agents can see why execution remained blocked across versions. |"
if "L-050" not in r:
    r=r.replace("| L-049 | v0.6.6 confirmed no live approval existed. | A missing live approval should still reach the executor boundary and prove execution is blocked. | Replay executors must refuse to run when live approval handoff is invalid, emitting a blocked executor report instead of silently stopping. |\n",
                "| L-049 | v0.6.6 confirmed no live approval existed. | A missing live approval should still reach the executor boundary and prove execution is blocked. | Replay executors must refuse to run when live approval handoff is invalid, emitting a blocked executor report instead of silently stopping. |\n"+lesson+"\n")
if "| v0.6.8 |" not in r:
    r=r.replace("| v0.6.7 | Approval-gated replay executor; refuses execution when handoff is invalid. |\n",
                "| v0.6.7 | Approval-gated replay executor; refuses execution when handoff is invalid. |\n| v0.6.8 | Blocked-state continuity ledger; records blocked execution as evidence. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.9 - Blocked-State Trend Review**

Recommended goals:

- Review blocked-state ledger trend.
- Distinguish persistent governance block from stale target.
- Define retirement or continuation criteria for the approval-gated pathway.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_blocked_state_continuity_ledger.py" not in s:
        s=s.replace("python scripts/benchmarks/run_approval_gated_replay_executor.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/run_approval_gated_replay_executor.py\npython scripts/benchmarks/run_blocked_state_continuity_ledger.py\npython -m unittest discover -s tests")
        s=s.replace("| Replay executor patch | `reports/replay_executor/`, `visuals/replay_executor/`, live approval handoff | executor gate + release validator; refuses execution when handoff invalid |\n",
                    "| Replay executor patch | `reports/replay_executor/`, `visuals/replay_executor/`, live approval handoff | executor gate + release validator; refuses execution when handoff invalid |\n| Blocked continuity patch | `reports/blocked_continuity/`, `visuals/blocked_continuity/`, replay executor | continuity ledger + release validator; no execution |\n")
    if name.endswith("task_routing_matrix.md") and "| Blocked continuity patch |" not in s:
        s=s.replace("| Replay executor patch | outer | execution-boundary | governance | live approval handoff | executor blocked report + charts + release validator | `reports/replay_executor/latest_approval_gated_replay_executor.md` |\n",
                    "| Replay executor patch | outer | execution-boundary | governance | live approval handoff | executor blocked report + charts + release validator | `reports/replay_executor/latest_approval_gated_replay_executor.md` |\n| Blocked continuity patch | outer | evidence | governance | replay executor + live approval handoff | continuity ledger + charts + release validator | `reports/blocked_continuity/latest_blocked_state_continuity.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.8"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["blocked_state_continuity"]={
    "read_first":["reports/replay_executor/latest_approval_gated_replay_executor.json","reports/live_approval_handoff/latest_live_approval_handoff_check.json"],
    "validate":["python scripts/benchmarks/run_blocked_state_continuity_ledger.py","python scripts/release/validate_release.py"],
    "evidence":["reports/blocked_continuity/latest_blocked_state_continuity.md","visuals/blocked_continuity/v0_6_8/"],
    "mutation_lock":"Records blocked state only; no replay execution, branch creation, or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.8 | Blocked-state continuity ledger |" not in t:
    t=t.replace("| v0.6.7 | Approval-gated replay executor | `python scripts/benchmarks/run_approval_gated_replay_executor.py` | Refuses execution when live approval handoff is invalid | `reports/replay_executor/latest_approval_gated_replay_executor.md` | `visuals/replay_executor/v0_6_7/` |\n",
                "| v0.6.7 | Approval-gated replay executor | `python scripts/benchmarks/run_approval_gated_replay_executor.py` | Refuses execution when live approval handoff is invalid | `reports/replay_executor/latest_approval_gated_replay_executor.md` | `visuals/replay_executor/v0_6_7/` |\n| v0.6.8 | Blocked-state continuity ledger | `python scripts/benchmarks/run_blocked_state_continuity_ledger.py` | Records blocked executor state as continuity evidence | `reports/blocked_continuity/latest_blocked_state_continuity.md` | `visuals/blocked_continuity/v0_6_8/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_8_blocked_continuity.md", f"""# TAU-SCALING-SA v0.6.8 - Blocked-State Continuity Ledger

Generated: {NOW}

## Purpose

Record blocked executor state as durable continuity evidence.

## Boundary

Blocked-state continuity ledgers are local classifier-governance memory artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.8 patch written")
