
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"approval_validator"/"v0_6_3"/"backups"/f"{p.name}_before_v0_6_3_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"validate_human_approval_artifact.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpURU1QTEFURSA9IFJPT1QgLyAicmVwb3J0cyIgLyAiaHVtYW5fYXBwcm92YWwiIC8gImh1bWFuX2FwcHJvdmFsX2FydGlmYWN0X3RlbXBsYXRlX3YwXzZfMi5qc29uIgpSRVBMQVkgPSBST09UIC8gInJlcG9ydHMiIC8gImNhbmRpZGF0ZV9yZXBsYXkiIC8gImxhdGVzdF9jYW5kaWRhdGVfYnJhbmNoX3JlcGxheV9oYXJuZXNzLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAiYXBwcm92YWxfdmFsaWRhdG9yIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImFwcHJvdmFsX3ZhbGlkYXRvciIgLyAidjBfNl8zIgoKZGVmIHJqc29uKHApOgogICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwKToKICAgIHJldHVybiBzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgdmFsaWRhdGVfYXJ0aWZhY3QoYXJ0aWZhY3QpOgogICAgY2hlY2tzID0gW10KCiAgICBkZWYgYWRkKGNoZWNrX2lkLCBwYXNzZWQsIG9ic2VydmVkLCByZXF1aXJlZD1UcnVlKToKICAgICAgICBjaGVja3MuYXBwZW5kKHsKICAgICAgICAgICAgImNoZWNrX2lkIjogY2hlY2tfaWQsCiAgICAgICAgICAgICJwYXNzZWQiOiBib29sKHBhc3NlZCksCiAgICAgICAgICAgICJvYnNlcnZlZCI6IG9ic2VydmVkLAogICAgICAgICAgICAicmVxdWlyZWQiOiByZXF1aXJlZCwKICAgICAgICB9KQoKICAgIGRlY2lzaW9uID0gYXJ0aWZhY3QuZ2V0KCJhcHByb3ZhbF9kZWNpc2lvbiIpCiAgICBhcHByb3ZlciA9IHN0cihhcnRpZmFjdC5nZXQoImFwcHJvdmVyIiwgIiIpKS5zdHJpcCgpCiAgICB0cyA9IHN0cihhcnRpZmFjdC5nZXQoImFwcHJvdmFsX3RpbWVzdGFtcCIsICIiKSkuc3RyaXAoKQogICAgcmVxdWlyZWRfc3RhdGVtZW50ID0gc3RyKGFydGlmYWN0LmdldCgicmVxdWlyZWRfc3RhdGVtZW50IiwgIiIpKS5zdHJpcCgpCiAgICBsb2NrcyA9IGFydGlmYWN0LmdldCgiZXhwbGljaXRfbG9ja3MiLCB7fSkgb3Ige30KCiAgICBhZGQoInNjaGVtYV9pc192MF82XzIiLCBhcnRpZmFjdC5nZXQoInNjaGVtYSIpID09ICJ0YXUtc2NhbGluZy1odW1hbi1hcHByb3ZhbC1hcnRpZmFjdC12MC42LjIiLCBzdHIoYXJ0aWZhY3QuZ2V0KCJzY2hlbWEiKSkpCiAgICBhZGQoImRlY2lzaW9uX2lzX2V4cGxpY2l0IiwgZGVjaXNpb24gaW4gWyJBUFBST1ZFX1JFUExBWV9PTkxZIiwgIkRFTlkiLCAiUkVRVUVTVF9NT1JFX0VWSURFTkNFIl0sIHN0cihkZWNpc2lvbikpCiAgICBhZGQoImFwcHJvdmVyX3ByZXNlbnQiLCBib29sKGFwcHJvdmVyKSwgYXBwcm92ZXIgb3IgIm1pc3NpbmciKQogICAgYWRkKCJ0aW1lc3RhbXBfcHJlc2VudCIsIGJvb2wodHMpLCB0cyBvciAibWlzc2luZyIpCiAgICBhZGQoInNjb3BlX3JlcGxheV9vbmx5IiwgYXJ0aWZhY3QuZ2V0KCJzY29wZSIpID09ICJjYW5kaWRhdGVfYnJhbmNoX3JlcGxheV9vbmx5Iiwgc3RyKGFydGlmYWN0LmdldCgic2NvcGUiKSkpCiAgICBhZGQoInJlcXVpcmVkX3N0YXRlbWVudF9wcmVzZW50IiwgImRvZXMgbm90IGF1dGhvcml6ZSBjbGFzc2lmaWVyIG11dGF0aW9uIiBpbiByZXF1aXJlZF9zdGF0ZW1lbnQsICJwcmVzZW50IiBpZiByZXF1aXJlZF9zdGF0ZW1lbnQgZWxzZSAibWlzc2luZyIpCiAgICBhZGQoInJ1bnRpbWVfbXV0YXRpb25fbG9ja2VkIiwgbG9ja3MuZ2V0KCJydW50aW1lX211dGF0aW9uX2FsbG93ZWQiKSBpcyBGYWxzZSwgc3RyKGxvY2tzLmdldCgicnVudGltZV9tdXRhdGlvbl9hbGxvd2VkIikpKQogICAgYWRkKCJjbGFzc2lmaWVyX211dGF0aW9uX2xvY2tlZCIsIGxvY2tzLmdldCgiY2xhc3NpZmllcl9tdXRhdGlvbl9hbGxvd2VkIikgaXMgRmFsc2UsIHN0cihsb2Nrcy5nZXQoImNsYXNzaWZpZXJfbXV0YXRpb25fYWxsb3dlZCIpKSkKICAgIGFkZCgiYXBwbGljYXRpb25fbG9ja2VkIiwgbG9ja3MuZ2V0KCJhcHBsaWNhdGlvbl9hbGxvd2VkIikgaXMgRmFsc2UsIHN0cihsb2Nrcy5nZXQoImFwcGxpY2F0aW9uX2FsbG93ZWQiKSkpCiAgICBhZGQoImNhbGlicmF0aW9uX3VuYXBwbGllZCIsIGxvY2tzLmdldCgiY2FsaWJyYXRpb25fYXBwbGllZCIpIGlzIEZhbHNlLCBzdHIobG9ja3MuZ2V0KCJjYWxpYnJhdGlvbl9hcHBsaWVkIikpKQogICAgYWRkKCJwb2xpY3lfdW5lbmZvcmNlZCIsIGxvY2tzLmdldCgicG9saWN5X2VuZm9yY2VkIikgaXMgRmFsc2UsIHN0cihsb2Nrcy5nZXQoInBvbGljeV9lbmZvcmNlZCIpKSkKCiAgICByZXR1cm4gY2hlY2tzCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihlKSkKICAgICAgICByZXR1cm4gcGF0aHMKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICBjb3VudHMgPSB7CiAgICAgICAgInBhc3NlZCI6IHN1bW1hcnlbImNoZWNrX3Bhc3NfY291bnQiXSwKICAgICAgICAiZmFpbGVkIjogc3VtbWFyeVsiY2hlY2tfZmFpbF9jb3VudCJdLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg3LCA0KSkKICAgIHBsdC5iYXIobGlzdChjb3VudHMua2V5cygpKSwgbGlzdChjb3VudHMudmFsdWVzKCkpKQogICAgcGx0LnlsYWJlbCgiQ2hlY2sgY291bnQiKQogICAgcGx0LnRpdGxlKCJIdW1hbiBBcHByb3ZhbCBWYWxpZGF0b3IgQ2hlY2tzIikKICAgIHNhdmUoImFwcHJvdmFsX3ZhbGlkYXRvcl9jaGVja19jb3VudHMucG5nIikKCiAgICBnYXRlcyA9IHsKICAgICAgICAiYXBwcm92YWxfdmFsaWQiOiBpbnQoc3VtbWFyeVsiYXBwcm92YWxfdmFsaWQiXSksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogaW50KHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0pLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCJdKSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVzLmtleXMoKSksIGxpc3QoZ2F0ZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBWYWxpZGF0b3IgR2F0ZSBTdGF0ZSIpCiAgICBzYXZlKCJhcHByb3ZhbF92YWxpZGF0b3JfZ2F0ZV9zdGF0ZS5wbmciKQoKICAgIGNsYXNzZXMgPSB7c3VtbWFyeVsidmFsaWRhdG9yX3N0YXR1cyJdOiAxfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LCA0KSkKICAgIHBsdC5iYXIobGlzdChjbGFzc2VzLmtleXMoKSksIGxpc3QoY2xhc3Nlcy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJBcHByb3ZhbCBWYWxpZGF0b3IgU3RhdHVzIikKICAgIHNhdmUoImFwcHJvdmFsX3ZhbGlkYXRvcl9zdGF0dXMucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzKToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjYuMyBIdW1hbiBBcHByb3ZhbCBBcnRpZmFjdCBWYWxpZGF0b3IiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBWYWxpZGF0b3IgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gVmFsaWRhdG9yIHN0YXR1czogYHtzWyd2YWxpZGF0b3Jfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIEFwcHJvdmFsIGRlY2lzaW9uOiBge3NbJ2FwcHJvdmFsX2RlY2lzaW9uJ119YCIsCiAgICAgICAgZiItIEFwcHJvdmFsIHZhbGlkOiBge3NbJ2FwcHJvdmFsX3ZhbGlkJ119YCIsCiAgICAgICAgZiItIFJlcGxheSBhbGxvd2VkOiBge3NbJ3JlcGxheV9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEJyYW5jaCBjcmVhdGlvbiBhbGxvd2VkOiBge3NbJ2JyYW5jaF9jcmVhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c1snbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBBcHBsaWNhdGlvbiBhbGxvd2VkOiBge3NbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gQ2FsaWJyYXRpb24gYXBwbGllZDogYHtzWydjYWxpYnJhdGlvbl9hcHBsaWVkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFZhbGlkYXRpb24gQ2hlY2tzIiwKICAgICAgICAiIiwKICAgICAgICAifCBDaGVjayB8IFBhc3NlZCB8IE9ic2VydmVkIHwgUmVxdWlyZWQgfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS18IiwKICAgIF0KICAgIGZvciByb3cgaW4gc1siY2hlY2tzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3Jvd1snY2hlY2tfaWQnXX1gIHwgYHtyb3dbJ3Bhc3NlZCddfWAgfCBge3Jvd1snb2JzZXJ2ZWQnXX1gIHwgYHtyb3dbJ3JlcXVpcmVkJ119YCB8IikKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBhcnRpZmFjdCA9IHJqc29uKFRFTVBMQVRFKQogICAgcmVwbGF5ID0gcmpzb24oUkVQTEFZKQogICAgY2hlY2tzID0gdmFsaWRhdGVfYXJ0aWZhY3QoYXJ0aWZhY3QpCgogICAgcGFzc19jb3VudCA9IHN1bSgxIGZvciBjIGluIGNoZWNrcyBpZiBjWyJwYXNzZWQiXSkKICAgIGZhaWxfY291bnQgPSBzdW0oMSBmb3IgYyBpbiBjaGVja3MgaWYgY1sicmVxdWlyZWQiXSBhbmQgbm90IGNbInBhc3NlZCJdKQoKICAgIGRlY2lzaW9uID0gYXJ0aWZhY3QuZ2V0KCJhcHByb3ZhbF9kZWNpc2lvbiIpCiAgICBhcHByb3ZhbF92YWxpZCA9ICgKICAgICAgICBmYWlsX2NvdW50ID09IDAKICAgICAgICBhbmQgZGVjaXNpb24gPT0gIkFQUFJPVkVfUkVQTEFZX09OTFkiCiAgICAgICAgYW5kIHJlcGxheS5nZXQoInJlcGxheV9zdGF0dXMiKSA9PSAiUkVQTEFZX0JMT0NLRURfX0hVTUFOX0FQUFJPVkFMX0FSVElGQUNUX1JFUVVJUkVEIgogICAgKQoKICAgIGlmIGFwcHJvdmFsX3ZhbGlkOgogICAgICAgIHN0YXR1cyA9ICJBUFBST1ZBTF9WQUxJRF9GT1JfUkVQTEFZX09OTFkiCiAgICBlbGlmIGRlY2lzaW9uID09ICJERU5ZIjoKICAgICAgICBzdGF0dXMgPSAiQVBQUk9WQUxfREVOSUVEIgogICAgZWxpZiBkZWNpc2lvbiA9PSAiUkVRVUVTVF9NT1JFX0VWSURFTkNFIjoKICAgICAgICBzdGF0dXMgPSAiQVBQUk9WQUxfUkVRVUVTVFNfTU9SRV9FVklERU5DRSIKICAgIGVsc2U6CiAgICAgICAgc3RhdHVzID0gIkFQUFJPVkFMX0lOVkFMSURfT1JfVEVNUExBVEVfT05MWSIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctaHVtYW4tYXBwcm92YWwtYXJ0aWZhY3QtdmFsaWRhdG9yLXYwLjYuMyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dF9hcHByb3ZhbF9hcnRpZmFjdCI6IHJlbChURU1QTEFURSksCiAgICAgICAgImlucHV0X2NhbmRpZGF0ZV9yZXBsYXkiOiByZWwoUkVQTEFZKSwKICAgICAgICAiYXBwcm92YWxfZGVjaXNpb24iOiBkZWNpc2lvbiwKICAgICAgICAidmFsaWRhdG9yX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAiYXBwcm92YWxfdmFsaWQiOiBib29sKGFwcHJvdmFsX3ZhbGlkKSwKICAgICAgICAiY2hlY2tzIjogY2hlY2tzLAogICAgICAgICJjaGVja19wYXNzX2NvdW50IjogcGFzc19jb3VudCwKICAgICAgICAiY2hlY2tfZmFpbF9jb3VudCI6IGZhaWxfY291bnQsCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogYm9vbChhcHByb3ZhbF92YWxpZCksCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiAiUmVwbGF5IG1heSBiZSBwcmVwYXJlZCBvbmx5IGlmIGFwcHJvdmFsX3ZhbGlkIGlzIHRydWUuIEJyYW5jaCBjcmVhdGlvbiBhbmQgbXV0YXRpb24gcmVtYWluIGJsb2NrZWQuIiBpZiBhcHByb3ZhbF92YWxpZCBlbHNlICJBcHByb3ZhbCBpcyBub3QgdmFsaWQgZm9yIHJlcGxheS4gS2VlcCByZXBsYXkgYmxvY2tlZC4iLAogICAgICAgICJib3VuZGFyeSI6ICJIdW1hbiBhcHByb3ZhbCB2YWxpZGF0b3JzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgdmFsaWRhdGlvbiBhcnRpZmFjdHMuIFRoZXkgZG8gbm90IGNyZWF0ZSBicmFuY2hlcyBieSBkZWZhdWx0LCBkbyBub3QgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGRvIG5vdCBhcHBseSBjYWxpYnJhdGlvbiwgYW5kIGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNi40IHNob3VsZCBhZGQgYXBwcm92YWwtZ2F0ZWQgcmVwbGF5IGRyeS1ydW4gb25seSBpZiBhcHByb3ZhbF92YWxpZCBpcyB0cnVlOyBvdGhlcndpc2UgcHJlc2VydmUgYmxvY2tlZCBzdGF0ZS4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJodW1hbl9hcHByb3ZhbF92YWxpZGF0b3JfdjBfNl8zLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9odW1hbl9hcHByb3ZhbF92YWxpZGF0b3IuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAiaHVtYW5fYXBwcm92YWxfdmFsaWRhdG9yX3YwXzZfMy5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfaHVtYW5fYXBwcm92YWxfdmFsaWRhdG9yLm1kIiwgcmVwb3J0KHN1bW1hcnkpKQoKICAgIHByaW50KGpzb24uZHVtcHMoewogICAgICAgICJzY2hlbWEiOiBzdW1tYXJ5WyJzY2hlbWEiXSwKICAgICAgICAidmFsaWRhdG9yX3N0YXR1cyI6IHN1bW1hcnlbInZhbGlkYXRvcl9zdGF0dXMiXSwKICAgICAgICAiYXBwcm92YWxfZGVjaXNpb24iOiBzdW1tYXJ5WyJhcHByb3ZhbF9kZWNpc2lvbiJdLAogICAgICAgICJhcHByb3ZhbF92YWxpZCI6IHN1bW1hcnlbImFwcHJvdmFsX3ZhbGlkIl0sCiAgICAgICAgImNoZWNrX3Bhc3NfY291bnQiOiBzdW1tYXJ5WyJjaGVja19wYXNzX2NvdW50Il0sCiAgICAgICAgImNoZWNrX2ZhaWxfY291bnQiOiBzdW1tYXJ5WyJjaGVja19mYWlsX2NvdW50Il0sCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogc3VtbWFyeVsicmVwbGF5X2FsbG93ZWQiXSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvYXBwcm92YWxfdmFsaWRhdG9yL2xhdGVzdF9odW1hbl9hcHByb3ZhbF92YWxpZGF0b3IubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"approval_validator"/"README.md", """# Human Approval Validator Reports

Current layer: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**

## Purpose

This folder stores validation reports for completed approval or denial artifacts.

## Primary command

```powershell
python scripts/benchmarks/validate_human_approval_artifact.py
```

## README Update Rule

Update this mini README whenever approval-validation schemas, approval decisions, or replay gates change.

Boundary: approval validators are local classifier-governance validators only.
""")
write(ROOT/"visuals"/"approval_validator"/"README.md", """# Human Approval Validator Visuals

Current layer: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**

## Purpose

This folder stores charts summarizing approval-validator state.

## README Update Rule

Update this mini README whenever approval-validator chart names or meanings change.

Boundary: approval-validator visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"approval_validator"/"v0_6_3"/"README.md", """# v0.6.3 Human Approval Validator Charts

Expected charts:

- `approval_validator_check_counts.png`
- `approval_validator_gate_state.png`
- `approval_validator_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local approval-validator diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.2[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.1[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.2 - Human Approval Artifact Template**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.2 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.3 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.2-ready |", "| Task routing matrix | geometry-aware / v0.6.3-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.2 |", "| Agent contract version sync | current / v0.6.3 |")
if "| Human approval validator |" not in r:
    r=r.replace("| Human approval charts | `visuals/human_approval/v0_6_2/` |\n",
                "| Human approval charts | `visuals/human_approval/v0_6_2/` |\n| Human approval validator | `reports/approval_validator/latest_human_approval_validator.md` |\n| Human approval validator charts | `visuals/approval_validator/v0_6_3/` |\n")
if "python scripts/benchmarks/validate_human_approval_artifact.py" not in r:
    r=r.replace("python scripts/benchmarks/generate_human_approval_template.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/generate_human_approval_template.py\npython scripts/benchmarks/validate_human_approval_artifact.py\npython scripts/release/validate_release.py")
if "    approval_validator/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    approval_validator/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    approval_validator/\n")
section="""## Human Approval Artifact Validator v0.6.3

v0.6.3 validates the human approval artifact and refuses replay while the artifact remains template-only or incomplete.

Primary command:

```powershell
python scripts/benchmarks/validate_human_approval_artifact.py
```

Primary outputs:

```text
reports/approval_validator/latest_human_approval_validator.json
reports/approval_validator/latest_human_approval_validator.md
visuals/approval_validator/v0_6_3/
```

Current expected lock when the artifact remains template-only:

```text
approval_valid: false
approval_decision: UNSET
replay_allowed: false
branch_creation_allowed: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: approval validators are local classifier-governance validation artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Human Approval Artifact Validator v0.6.3" not in r:
    r=r.replace("## Human Approval Artifact Template v0.6.2", section+"## Human Approval Artifact Template v0.6.2",1)
lesson="| L-045 | v0.6.2 created a template, but a template is not approval. | Approval artifacts must be validated before replay can proceed. | Approval validators must reject UNSET/template-only artifacts and keep replay blocked until explicit approval fields pass. |"
if "L-045" not in r:
    r=r.replace("| L-044 | v0.6.1 correctly blocked replay because no human approval artifact existed. | Blocking replay is useful only if the system provides an explicit approval/denial artifact format. | Approval templates must be created before approval validation; templates alone do not authorize replay, branching, or mutation. |\n",
                "| L-044 | v0.6.1 correctly blocked replay because no human approval artifact existed. | Blocking replay is useful only if the system provides an explicit approval/denial artifact format. | Approval templates must be created before approval validation; templates alone do not authorize replay, branching, or mutation. |\n"+lesson+"\n")
if "| v0.6.3 |" not in r:
    r=r.replace("| v0.6.2 | Human approval artifact template; template only, no approval by default. |\n",
                "| v0.6.2 | Human approval artifact template; template only, no approval by default. |\n| v0.6.3 | Human approval artifact validator; rejects UNSET/template-only approval by default. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.4 - Approval-Gated Replay Dry-Run**

Recommended goals:

- Run only when `approval_valid: true`.
- If approval remains invalid/template-only, emit a blocked dry-run report.
- Keep branch creation disabled by default.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "validate_human_approval_artifact.py" not in s:
        s=s.replace("python scripts/benchmarks/generate_human_approval_template.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/generate_human_approval_template.py\npython scripts/benchmarks/validate_human_approval_artifact.py\npython -m unittest discover -s tests")
        s=s.replace("| Human approval template patch | `reports/human_approval/`, `visuals/human_approval/`, replay harness | approval template + release validator; no approval by default |\n",
                    "| Human approval template patch | `reports/human_approval/`, `visuals/human_approval/`, replay harness | approval template + release validator; no approval by default |\n| Human approval validator patch | `reports/approval_validator/`, `visuals/approval_validator/`, approval artifact | approval validator + release validator; replay blocked unless valid |\n")
    if name.endswith("task_routing_matrix.md") and "| Human approval validator patch |" not in s:
        s=s.replace("| Human approval template patch | outer | governance | review | replay harness + candidate gate | approval template + charts + release validator | `reports/human_approval/latest_human_approval_template_report.md` |\n",
                    "| Human approval template patch | outer | governance | review | replay harness + candidate gate | approval template + charts + release validator | `reports/human_approval/latest_human_approval_template_report.md` |\n| Human approval validator patch | outer | validation | governance | approval artifact + replay harness | approval validator + charts + release validator | `reports/approval_validator/latest_human_approval_validator.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.3"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["human_approval_validator"]={
    "read_first":["reports/human_approval/human_approval_artifact_template_v0_6_2.json","reports/candidate_replay/latest_candidate_branch_replay_harness.json"],
    "validate":["python scripts/benchmarks/validate_human_approval_artifact.py","python scripts/release/validate_release.py"],
    "evidence":["reports/approval_validator/latest_human_approval_validator.md","visuals/approval_validator/v0_6_3/"],
    "mutation_lock":"Rejects template-only/UNSET approvals; replay remains blocked unless approval_valid is true."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.3 | Human approval artifact validator |" not in t:
    t=t.replace("| v0.6.2 | Human approval artifact template | `python scripts/benchmarks/generate_human_approval_template.py` | Creates approval/denial template only; no approval by default | `reports/human_approval/latest_human_approval_template_report.md` | `visuals/human_approval/v0_6_2/` |\n",
                "| v0.6.2 | Human approval artifact template | `python scripts/benchmarks/generate_human_approval_template.py` | Creates approval/denial template only; no approval by default | `reports/human_approval/latest_human_approval_template_report.md` | `visuals/human_approval/v0_6_2/` |\n| v0.6.3 | Human approval artifact validator | `python scripts/benchmarks/validate_human_approval_artifact.py` | Rejects template-only approval and keeps replay blocked unless explicit approval validates | `reports/approval_validator/latest_human_approval_validator.md` | `visuals/approval_validator/v0_6_3/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_3_human_approval_validator.md", f"""# TAU-SCALING-SA v0.6.3 - Human Approval Artifact Validator

Generated: {NOW}

## Purpose

Validate the human approval artifact and reject template-only/UNSET approval by default.

## Boundary

Approval validators are local classifier-governance validation artifacts only. They do not create branches by default, do not mutate classifier behavior, and do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.3 patch written")
