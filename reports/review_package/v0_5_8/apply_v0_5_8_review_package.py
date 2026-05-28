
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"review_package"/"v0_5_8"/"backups"/f"{p.name}_before_v0_5_8_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"generate_review_package.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdCgpJTlBVVFMgPSB7CiAgICAiY2F1c2VfZGVjb21wb3NpdGlvbiI6IFJPT1QgLyAicmVwb3J0cyIgLyAib3Zlcl9wZW5hbHR5X2NhdXNlcyIgLyAibGF0ZXN0X292ZXJfcGVuYWx0eV9jYXVzZV9kZWNvbXBvc2l0aW9uLmpzb24iLAogICAgInJlbWVkaWF0aW9uX3BsYW4iOiBST09UIC8gInJlcG9ydHMiIC8gInJlbWVkaWF0aW9uX3BsYW4iIC8gImxhdGVzdF9jYXVzZV9zcGVjaWZpY19yZW1lZGlhdGlvbl9wbGFuLmpzb24iLAogICAgIm5lZ2F0aXZlX2NvbnRyb2xzIjogUk9PVCAvICJyZXBvcnRzIiAvICJuZWdhdGl2ZV9jb250cm9scyIgLyAibGF0ZXN0X3N1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMuanNvbiIsCiAgICAiY2FsaWJyYXRpb25fcGxhbiI6IFJPT1QgLyAicmVwb3J0cyIgLyAiY2FsaWJyYXRpb25fcGxhbiIgLyAibGF0ZXN0X2Rpc2FibGVkX2NhbGlicmF0aW9uX3BsYW4uanNvbiIsCiAgICAiY2FsaWJyYXRpb25fY291bnRlcmZhY3R1YWxzIjogUk9PVCAvICJyZXBvcnRzIiAvICJjYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMiIC8gImxhdGVzdF9jYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMuanNvbiIsCiAgICAiY291bnRlcmZhY3R1YWxfZGVjaXNpb24iOiBST09UIC8gInJlcG9ydHMiIC8gImNvdW50ZXJmYWN0dWFsX2RlY2lzaW9uIiAvICJsYXRlc3RfY291bnRlcmZhY3R1YWxfZGVjaXNpb25fcmVjb3JkLmpzb24iLAp9Ck9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmV2aWV3X3BhY2thZ2UiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAicmV2aWV3X3BhY2thZ2UiIC8gInYwXzVfOCIKCmRlZiByanNvbihwOiBQYXRoKToKICAgIHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQoKZGVmIHdqc29uKHA6IFBhdGgsIHgpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KGpzb24uZHVtcHMoeCwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocDogUGF0aCwgczogc3RyKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwOiBQYXRoKSAtPiBzdHI6CiAgICByZXR1cm4gc3RyKHAucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGxvYWRfaW5wdXRzKCk6CiAgICBsb2FkZWQgPSB7fQogICAgbWlzc2luZyA9IFtdCiAgICBmb3IgaywgcCBpbiBJTlBVVFMuaXRlbXMoKToKICAgICAgICBpZiBwLmV4aXN0cygpOgogICAgICAgICAgICBsb2FkZWRba10gPSByanNvbihwKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIG1pc3NpbmcuYXBwZW5kKHJlbChwKSkKICAgIHJldHVybiBsb2FkZWQsIG1pc3NpbmcKCmRlZiBjaGFydHMoc3VtbWFyeSk6CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGUpKQogICAgICAgIHJldHVybiBwYXRocwoKICAgIFZJUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCgogICAgZGVmIHNhdmUobmFtZSk6CiAgICAgICAgcCA9IFZJUyAvIG5hbWUKICAgICAgICBwbHQudGlnaHRfbGF5b3V0KCkKICAgICAgICBwbHQuc2F2ZWZpZyhwLCBkcGk9MTgwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgICAgIHBsdC5jbG9zZSgpCiAgICAgICAgcGF0aHMuYXBwZW5kKHJlbChwKSkKCiAgICBzdGFnZXMgPSBzdW1tYXJ5WyJzdGFnZV9zdW1tYXJ5Il0KICAgIGxhYmVscyA9IFtzWyJzdGFnZSJdIGZvciBzIGluIHN0YWdlc10KICAgIGNvdW50cyA9IFtzWyJwcmltYXJ5X2NvdW50Il0gZm9yIHMgaW4gc3RhZ2VzXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSgxMCwgNCkpCiAgICBwbHQuYmFyKGxhYmVscywgY291bnRzKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlByaW1hcnkgY291bnQiKQogICAgcGx0LnRpdGxlKCJSZXZpZXcgUGFja2FnZSBFdmlkZW5jZSBDaGFpbiIpCiAgICBzYXZlKCJyZXZpZXdfcGFja2FnZV9ldmlkZW5jZV9jaGFpbi5wbmciKQoKICAgIGdhdGVzID0gewogICAgICAgICJyZXZpZXdfYWxsb3dlZCI6IGludChib29sKHN1bW1hcnlbInJldmlld19hbGxvd2VkIl0pKSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IGludChib29sKHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSkpLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KGJvb2woc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdKSksCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBpbnQoYm9vbChzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0pKSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZ2F0ZXMua2V5cygpKSwgbGlzdChnYXRlcy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTIwLCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQm9vbGVhbiBzdGF0ZSIpCiAgICBwbHQudGl0bGUoIlJldmlldyB2cyBBcHBsaWNhdGlvbiBMb2NrcyIpCiAgICBzYXZlKCJyZXZpZXdfcGFja2FnZV9sb2NrX3N0YXRlcy5wbmciKQoKICAgIGRlY2lzaW9uID0gc3VtbWFyeVsiZGVjaXNpb25fY2xhc3NfY291bnRzIl0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoZGVjaXNpb24ua2V5cygpKSwgbGlzdChkZWNpc2lvbi52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJSZXZpZXcgUGFja2FnZSBEZWNpc2lvbiBDbGFzc2lmaWNhdGlvbiIpCiAgICBzYXZlKCJyZXZpZXdfcGFja2FnZV9kZWNpc2lvbl9jb3VudHMucG5nIikKCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZXBvcnQocyk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC41LjggUmV2aWV3IFBhY2thZ2UgYW5kIEV2aWRlbmNlIEJ1bmRsZSIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c1snZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJldmlldyBEZWNpc2lvbiIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIFJldmlldyBwYWNrYWdlIHN0YXR1czogYHtzWydyZXZpZXdfcGFja2FnZV9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gRGVjaXNpb24gY2xhc3M6IGB7c1snZGVjaXNpb25fY2xhc3MnXX1gIiwKICAgICAgICBmIi0gU2VsZWN0ZWQgcmVwb3J0LW9ubHkgdGhyZXNob2xkOiBge3NbJ3NlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCddfWAiLAogICAgICAgIGYiLSBSZXZpZXcgYWxsb3dlZDogYHtzWydyZXZpZXdfYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBBcHBsaWNhdGlvbiBhbGxvd2VkOiBge3NbJ2FwcGxpY2F0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzWydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICBmIi0gQ2FsaWJyYXRpb24gYXBwbGllZDogYHtzWydjYWxpYnJhdGlvbl9hcHBsaWVkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEV2aWRlbmNlIENoYWluIiwKICAgICAgICAiIiwKICAgICAgICAifCBTdGFnZSB8IFNvdXJjZSB8IFByaW1hcnkgbWV0cmljIHwgQ291bnQgfCBTdGF0dXMgfCIsCiAgICAgICAgInwtLS18LS0tfC0tLXwtLS06fC0tLXwiLAogICAgXQogICAgZm9yIHN0IGluIHNbInN0YWdlX3N1bW1hcnkiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IHtzdFsnc3RhZ2UnXX0gfCBge3N0Wydzb3VyY2UnXX1gIHwgYHtzdFsncHJpbWFyeV9tZXRyaWMnXX1gIHwge3N0WydwcmltYXJ5X2NvdW50J119IHwgYHtzdFsnc3RhdHVzJ119YCB8IikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiIsCiAgICAgICAgIiMjIEJ1bmRsZSBGaWxlcyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgQnVuZGxlIEl0ZW0gfCBQYXRoIHwiLAogICAgICAgICJ8LS0tfC0tLXwiLAogICAgXQogICAgZm9yIGl0ZW0gaW4gc1siYnVuZGxlX2l0ZW1zIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCB7aXRlbVsnbmFtZSddfSB8IGB7aXRlbVsncGF0aCddfWAgfCIpCgogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgcCBpbiBzWyJjaGFydF9wYXRocyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgnXFwnLCAnLycpfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKCiAgICBsaW5lcyArPSBbCiAgICAgICAgIiMjIEZpbmFsIFJlY29tbWVuZGF0aW9uIiwKICAgICAgICAiIiwKICAgICAgICBzWyJmaW5hbF9yZWNvbW1lbmRhdGlvbiJdLAogICAgICAgICIiLAogICAgICAgICIjIyBCb3VuZGFyeSIsCiAgICAgICAgIiIsCiAgICAgICAgc1siYm91bmRhcnkiXSwKICAgICAgICAiIiwKICAgIF0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgZGF0YSwgbWlzc2luZyA9IGxvYWRfaW5wdXRzKCkKCiAgICBjYXVzZSA9IGRhdGEuZ2V0KCJjYXVzZV9kZWNvbXBvc2l0aW9uIiwge30pCiAgICByZW1lZGlhdGlvbiA9IGRhdGEuZ2V0KCJyZW1lZGlhdGlvbl9wbGFuIiwge30pCiAgICBuZWdhdGl2ZSA9IGRhdGEuZ2V0KCJuZWdhdGl2ZV9jb250cm9scyIsIHt9KQogICAgY2FsX3BsYW4gPSBkYXRhLmdldCgiY2FsaWJyYXRpb25fcGxhbiIsIHt9KQogICAgY291bnRlciA9IGRhdGEuZ2V0KCJjYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMiLCB7fSkKICAgIGRlY2lzaW9uID0gZGF0YS5nZXQoImNvdW50ZXJmYWN0dWFsX2RlY2lzaW9uIiwge30pCgogICAgZGVjaXNpb25fY2xhc3MgPSBkZWNpc2lvbi5nZXQoImRlY2lzaW9uIiwgIlVOS05PV04iKQogICAgcmV2aWV3X2FsbG93ZWQgPSBib29sKGRlY2lzaW9uLmdldCgicmV2aWV3X2FsbG93ZWQiLCBGYWxzZSkpCiAgICBhcHBsaWNhdGlvbl9hbGxvd2VkID0gRmFsc2UKICAgIG11dGF0aW9uX2FsbG93ZWQgPSBGYWxzZQogICAgcG9saWN5X2VuZm9yY2VkID0gRmFsc2UKICAgIGNhbGlicmF0aW9uX2FwcGxpZWQgPSBGYWxzZQoKICAgIHN0YWdlcyA9IFsKICAgICAgICB7CiAgICAgICAgICAgICJzdGFnZSI6ICJjYXVzZV9kZWNvbXBvc2l0aW9uIiwKICAgICAgICAgICAgInNvdXJjZSI6IHJlbChJTlBVVFNbImNhdXNlX2RlY29tcG9zaXRpb24iXSksCiAgICAgICAgICAgICJwcmltYXJ5X21ldHJpYyI6ICJjYXVzZV9jYXJkX2NvdW50IiwKICAgICAgICAgICAgInByaW1hcnlfY291bnQiOiBpbnQoY2F1c2UuZ2V0KCJjYXVzZV9jYXJkX2NvdW50IiwgMCkgb3IgMCksCiAgICAgICAgICAgICJzdGF0dXMiOiAibG9hZGVkIiBpZiAiY2F1c2VfZGVjb21wb3NpdGlvbiIgaW4gZGF0YSBlbHNlICJtaXNzaW5nIiwKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgInN0YWdlIjogInJlbWVkaWF0aW9uX3BsYW4iLAogICAgICAgICAgICAic291cmNlIjogcmVsKElOUFVUU1sicmVtZWRpYXRpb25fcGxhbiJdKSwKICAgICAgICAgICAgInByaW1hcnlfbWV0cmljIjogInJlbWVkaWF0aW9uX3Rhc2tfY291bnQiLAogICAgICAgICAgICAicHJpbWFyeV9jb3VudCI6IGludChyZW1lZGlhdGlvbi5nZXQoInJlbWVkaWF0aW9uX3Rhc2tfY291bnQiLCAwKSBvciAwKSwKICAgICAgICAgICAgInN0YXR1cyI6ICJsb2FkZWQiIGlmICJyZW1lZGlhdGlvbl9wbGFuIiBpbiBkYXRhIGVsc2UgIm1pc3NpbmciLAogICAgICAgIH0sCiAgICAgICAgewogICAgICAgICAgICAic3RhZ2UiOiAibmVnYXRpdmVfY29udHJvbHMiLAogICAgICAgICAgICAic291cmNlIjogcmVsKElOUFVUU1sibmVnYXRpdmVfY29udHJvbHMiXSksCiAgICAgICAgICAgICJwcmltYXJ5X21ldHJpYyI6ICJwYXNzZWRfY29udHJvbF9jb3VudCIsCiAgICAgICAgICAgICJwcmltYXJ5X2NvdW50IjogaW50KG5lZ2F0aXZlLmdldCgicGFzc2VkX2NvbnRyb2xfY291bnQiLCAwKSBvciAwKSwKICAgICAgICAgICAgInN0YXR1cyI6ICJsb2FkZWQiIGlmICJuZWdhdGl2ZV9jb250cm9scyIgaW4gZGF0YSBlbHNlICJtaXNzaW5nIiwKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgInN0YWdlIjogImNhbGlicmF0aW9uX3BsYW4iLAogICAgICAgICAgICAic291cmNlIjogcmVsKElOUFVUU1siY2FsaWJyYXRpb25fcGxhbiJdKSwKICAgICAgICAgICAgInByaW1hcnlfbWV0cmljIjogImFkbWlzc2libGVfdGhyZXNob2xkX2NvdW50IiwKICAgICAgICAgICAgInByaW1hcnlfY291bnQiOiBpbnQoY2FsX3BsYW4uZ2V0KCJhZG1pc3NpYmxlX3RocmVzaG9sZF9jb3VudCIsIDApIG9yIDApLAogICAgICAgICAgICAic3RhdHVzIjogImxvYWRlZCIgaWYgImNhbGlicmF0aW9uX3BsYW4iIGluIGRhdGEgZWxzZSAibWlzc2luZyIsCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJzdGFnZSI6ICJjYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMiLAogICAgICAgICAgICAic291cmNlIjogcmVsKElOUFVUU1siY2FsaWJyYXRpb25fY291bnRlcmZhY3R1YWxzIl0pLAogICAgICAgICAgICAicHJpbWFyeV9tZXRyaWMiOiAic2FmZV9jYW5kaWRhdGVfY291bnQiLAogICAgICAgICAgICAicHJpbWFyeV9jb3VudCI6IGludChjb3VudGVyLmdldCgic2FmZV9jYW5kaWRhdGVfY291bnQiLCAwKSBvciAwKSwKICAgICAgICAgICAgInN0YXR1cyI6ICJsb2FkZWQiIGlmICJjYWxpYnJhdGlvbl9jb3VudGVyZmFjdHVhbHMiIGluIGRhdGEgZWxzZSAibWlzc2luZyIsCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJzdGFnZSI6ICJjb3VudGVyZmFjdHVhbF9kZWNpc2lvbiIsCiAgICAgICAgICAgICJzb3VyY2UiOiByZWwoSU5QVVRTWyJjb3VudGVyZmFjdHVhbF9kZWNpc2lvbiJdKSwKICAgICAgICAgICAgInByaW1hcnlfbWV0cmljIjogInJldmlld19hbGxvd2VkIiwKICAgICAgICAgICAgInByaW1hcnlfY291bnQiOiBpbnQocmV2aWV3X2FsbG93ZWQpLAogICAgICAgICAgICAic3RhdHVzIjogZGVjaXNpb25fY2xhc3MsCiAgICAgICAgfSwKICAgIF0KCiAgICBjb21wbGV0ZSA9IG5vdCBtaXNzaW5nIGFuZCByZXZpZXdfYWxsb3dlZCBhbmQgbm90IGFwcGxpY2F0aW9uX2FsbG93ZWQgYW5kIG5vdCBtdXRhdGlvbl9hbGxvd2VkIGFuZCBub3QgY2FsaWJyYXRpb25fYXBwbGllZAogICAgc3RhdHVzID0gIlJFQURZX0ZPUl9IVU1BTl9SRVZJRVdfTk9UX0FQUExJQ0FUSU9OIiBpZiBjb21wbGV0ZSBlbHNlICJJTkNPTVBMRVRFX09SX05PVF9SRVZJRVdfUkVBRFkiCgogICAgYnVuZGxlX2l0ZW1zID0gWwogICAgICAgIHsibmFtZSI6IGssICJwYXRoIjogcmVsKHApLCAiZXhpc3RzIjogcC5leGlzdHMoKX0KICAgICAgICBmb3IgaywgcCBpbiBJTlBVVFMuaXRlbXMoKQogICAgXQoKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1yZXZpZXctcGFja2FnZS1ldmlkZW5jZS1idW5kbGUtdjAuNS44IiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgInJldmlld19wYWNrYWdlX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAibWlzc2luZ19pbnB1dHMiOiBtaXNzaW5nLAogICAgICAgICJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiOiBkZWNpc2lvbi5nZXQoInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCIsIGNvdW50ZXIuZ2V0KCJzZWxlY3RlZF9yZXBvcnRfb25seV90aHJlc2hvbGQiKSksCiAgICAgICAgImRlY2lzaW9uX2NsYXNzIjogZGVjaXNpb25fY2xhc3MsCiAgICAgICAgImRlY2lzaW9uX2NsYXNzX2NvdW50cyI6IHtkZWNpc2lvbl9jbGFzczogMX0sCiAgICAgICAgInJldmlld19hbGxvd2VkIjogcmV2aWV3X2FsbG93ZWQsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBhcHBsaWNhdGlvbl9hbGxvd2VkLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogbXV0YXRpb25fYWxsb3dlZCwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogcG9saWN5X2VuZm9yY2VkLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogY2FsaWJyYXRpb25fYXBwbGllZCwKICAgICAgICAic3RhZ2Vfc3VtbWFyeSI6IHN0YWdlcywKICAgICAgICAiYnVuZGxlX2l0ZW1zIjogYnVuZGxlX2l0ZW1zLAogICAgICAgICJzb3VyY2VfZGVjaXNpb25fcmVjb3JkIjogcmVsKElOUFVUU1siY291bnRlcmZhY3R1YWxfZGVjaXNpb24iXSksCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogIlNlbmQgdGhpcyBwYWNrYWdlIHRvIHJldmlldy4gRG8gbm90IGFwcGx5IGNhbGlicmF0aW9uLCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciwgb3IgZW5mb3JjZSBwb2xpY3kgZnJvbSB0aGlzIHBhY2thZ2UgYWxvbmUuIiBpZiBjb21wbGV0ZSBlbHNlICJSZXBhaXIgbWlzc2luZyBvciBub24tcmV2aWV3LXJlYWR5IGV2aWRlbmNlIGJlZm9yZSBwYWNrYWdpbmcuIiwKICAgICAgICAiYm91bmRhcnkiOiAiUmV2aWV3IHBhY2thZ2VzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgZXZpZGVuY2UgYnVuZGxlcy4gVGhleSBkbyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNS45IHNob3VsZCBjcmVhdGUgYSByZXZpZXcgY2hlY2tsaXN0IC8gc2lnbm9mZiBnYXRlLCBzdGlsbCB3aXRoIG11dGF0aW9uIGRpc2FibGVkLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gInJldmlld19wYWNrYWdlX3YwXzVfOC5qc29uIiwgc3VtbWFyeSkKICAgIHdqc29uKE9VVCAvICJsYXRlc3RfcmV2aWV3X3BhY2thZ2UuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAicmV2aWV3X3BhY2thZ2VfdjBfNV84Lm1kIiwgcmVwb3J0KHN1bW1hcnkpKQogICAgd3RleHQoT1VUIC8gImxhdGVzdF9yZXZpZXdfcGFja2FnZS5tZCIsIHJlcG9ydChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInJldmlld19wYWNrYWdlX3N0YXR1cyI6IHN1bW1hcnlbInJldmlld19wYWNrYWdlX3N0YXR1cyJdLAogICAgICAgICJkZWNpc2lvbl9jbGFzcyI6IHN1bW1hcnlbImRlY2lzaW9uX2NsYXNzIl0sCiAgICAgICAgInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCI6IHN1bW1hcnlbInNlbGVjdGVkX3JlcG9ydF9vbmx5X3RocmVzaG9sZCJdLAogICAgICAgICJyZXZpZXdfYWxsb3dlZCI6IHN1bW1hcnlbInJldmlld19hbGxvd2VkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgIm1pc3NpbmdfaW5wdXRfY291bnQiOiBsZW4oc3VtbWFyeVsibWlzc2luZ19pbnB1dHMiXSksCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9yZXZpZXdfcGFja2FnZS9sYXRlc3RfcmV2aWV3X3BhY2thZ2UubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT/"reports"/"review_package"/"README.md", """# Review Package Reports

Current layer: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**

## Purpose

This folder stores review packages that bundle v0.5.2-v0.5.7 evidence into one non-mutating review surface.

## Primary command

```powershell
python scripts/benchmarks/generate_review_package.py
```

## README Update Rule

Update this mini README whenever review-package schemas, bundle contents, or signoff rules change.

Boundary: review packages are local classifier-governance evidence bundles only.
""")
write(ROOT/"visuals"/"review_package"/"README.md", """# Review Package Visuals

Current layer: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**

## Purpose

This folder stores charts summarizing bundled review evidence.

## README Update Rule

Update this mini README whenever review-package chart names or meanings change.

Boundary: review-package visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"review_package"/"v0_5_8"/"README.md", """# v0.5.8 Review Package Charts

Expected charts:

- `review_package_evidence_chain.png`
- `review_package_lock_states.png`
- `review_package_decision_counts.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local review-package diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.7[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.6[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.7 - Counterfactual Decision Record**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.7 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.8 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.7-ready |", "| Task routing matrix | geometry-aware / v0.5.8-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.7 |", "| Agent contract version sync | current / v0.5.8 |")
if "| Review package |" not in r:
    r=r.replace("| Counterfactual decision charts | `visuals/counterfactual_decision/v0_5_7/` |\n",
                "| Counterfactual decision charts | `visuals/counterfactual_decision/v0_5_7/` |\n| Review package | `reports/review_package/latest_review_package.md` |\n| Review package charts | `visuals/review_package/v0_5_8/` |\n")
if "python scripts/benchmarks/generate_review_package.py" not in r:
    r=r.replace("python scripts/benchmarks/generate_counterfactual_decision_record.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/generate_counterfactual_decision_record.py\npython scripts/benchmarks/generate_review_package.py\npython scripts/release/validate_release.py")
if "    review_package/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    review_package/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    review_package/\n")
section="""## Review Package and Evidence Bundle v0.5.8

v0.5.8 bundles v0.5.2 through v0.5.7 into one non-mutating review package.

Primary command:

```powershell
python scripts/benchmarks/generate_review_package.py
```

Primary outputs:

```text
reports/review_package/latest_review_package.json
reports/review_package/latest_review_package.md
visuals/review_package/v0_5_8/
```

This layer bundles cause cards, remediation tasks, support-aware negative controls, disabled calibration plan, calibration counterfactuals, and counterfactual decision record.

Current lock:

```text
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: review packages are local classifier-governance evidence bundles. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Review Package and Evidence Bundle v0.5.8" not in r:
    r=r.replace("## Counterfactual Decision Record v0.5.7", section+"## Counterfactual Decision Record v0.5.7",1)
lesson="| L-040 | v0.5.7 produced SAFE_FOR_REVIEW_NOT_APPLICATION. | Safe-for-review can be mistaken for safe-for-application unless bundled explicitly. | A candidate that reaches SAFE_FOR_REVIEW_NOT_APPLICATION must be bundled into a review package before any implementation pathway is discussed. |"
if "L-040" not in r:
    r=r.replace("| L-039 | v0.5.6 counterfactuals passed, but a passing counterfactual is not an applied policy. | Successful simulations still need an explicit decision record to prevent silent promotion. | A successful counterfactual must become a decision record before any implementation pathway can be discussed. |\n",
                "| L-039 | v0.5.6 counterfactuals passed, but a passing counterfactual is not an applied policy. | Successful simulations still need an explicit decision record to prevent silent promotion. | A successful counterfactual must become a decision record before any implementation pathway can be discussed. |\n"+lesson+"\n")
if "| v0.5.8 |" not in r:
    r=r.replace("| v0.5.7 | Counterfactual decision record for safe-review classification without application. |\n",
                "| v0.5.7 | Counterfactual decision record for safe-review classification without application. |\n| v0.5.8 | Review package and evidence bundle for v0.5.2-v0.5.7. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.9 - Review Checklist and Signoff Gate**

Recommended goals:

- Convert the review package into a checklist/signoff gate.
- Require explicit human-review disposition before any implementation pathway.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: signoff gates are local classifier governance only.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.5\.7[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "generate_review_package.py" not in s:
        s=s.replace("python scripts/benchmarks/generate_counterfactual_decision_record.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/generate_counterfactual_decision_record.py\npython scripts/benchmarks/generate_review_package.py\npython -m unittest discover -s tests")
        s=s.replace("| Counterfactual decision patch | `reports/counterfactual_decision/`, `visuals/counterfactual_decision/`, counterfactual report | decision record + release validator; no classifier mutation |\n",
                    "| Counterfactual decision patch | `reports/counterfactual_decision/`, `visuals/counterfactual_decision/`, counterfactual report | decision record + release validator; no classifier mutation |\n| Review package patch | `reports/review_package/`, `visuals/review_package/`, decision record | review package + release validator; no classifier mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Review package patch |" not in s:
        s=s.replace("| Counterfactual decision patch | outer | validation | governance | calibration counterfactuals + decision criteria | decision record + charts + release validator | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` |\n",
                    "| Counterfactual decision patch | outer | validation | governance | calibration counterfactuals + decision criteria | decision record + charts + release validator | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` |\n| Review package patch | outer | evidence | governance | v0.5.2-v0.5.7 evidence surfaces | review package + charts + release validator | `reports/review_package/latest_review_package.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.8"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["review_package"]={
    "read_first":["reports/counterfactual_decision/latest_counterfactual_decision_record.json"],
    "validate":["python scripts/benchmarks/generate_review_package.py","python scripts/release/validate_release.py"],
    "evidence":["reports/review_package/latest_review_package.md","visuals/review_package/v0_5_8/"],
    "mutation_lock":"Does not change classifier behavior; application_allowed and mutation_allowed must remain false."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.8 | Review package and evidence bundle |" not in t:
    t=t.replace("| v0.5.7 | Counterfactual decision record | `python scripts/benchmarks/generate_counterfactual_decision_record.py` | Classifies counterfactual candidate for review without application | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` | `visuals/counterfactual_decision/v0_5_7/` |\n",
                "| v0.5.7 | Counterfactual decision record | `python scripts/benchmarks/generate_counterfactual_decision_record.py` | Classifies counterfactual candidate for review without application | `reports/counterfactual_decision/latest_counterfactual_decision_record.md` | `visuals/counterfactual_decision/v0_5_7/` |\n| v0.5.8 | Review package and evidence bundle | `python scripts/benchmarks/generate_review_package.py` | Bundles v0.5.2-v0.5.7 evidence for review without application | `reports/review_package/latest_review_package.md` | `visuals/review_package/v0_5_8/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_8_review_package.md", f"""# TAU-SCALING-SA v0.5.8 - Review Package and Evidence Bundle

Generated: {NOW}

## Purpose

Bundle v0.5.2-v0.5.7 evidence into one non-mutating review package.

## Boundary

Review packages are local classifier-governance evidence bundles only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.8 patch written")
