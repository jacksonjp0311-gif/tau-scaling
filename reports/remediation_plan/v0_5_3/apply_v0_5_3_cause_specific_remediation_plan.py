
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path.cwd()
NOW = datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"remediation_plan"/"v0_5_3"/"backups"/f"{p.name}_before_v0_5_3_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
runner_b64="CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdCkNBVVNFUyA9IFJPT1QgLyAicmVwb3J0cyIgLyAib3Zlcl9wZW5hbHR5X2NhdXNlcyIgLyAibGF0ZXN0X292ZXJfcGVuYWx0eV9jYXVzZV9kZWNvbXBvc2l0aW9uLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmVtZWRpYXRpb25fcGxhbiIKVEFTS1MgPSBPVVQgLyAidGFza3MiIC8gInYwXzVfMyIKVklTID0gUk9PVCAvICJ2aXN1YWxzIiAvICJyZW1lZGlhdGlvbl9wbGFuIiAvICJ2MF81XzMiCgpkZWYgcmpzb24ocCk6IHJldHVybiBqc29uLmxvYWRzKHAucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKZGVmIHd0ZXh0KHAsIHMpOgogICAgcC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcC53cml0ZV90ZXh0KHMsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgdGFza19mb3IoY2FyZCwgaWR4KToKICAgIHByaW1hcnkgPSBjYXJkLmdldCgicHJpbWFyeV9jYXVzZSIpCiAgICBjYXVzZXMgPSBjYXJkLmdldCgiY2F1c2VzIiwgW10pCiAgICBnYXRlX3BhaXIgPSBjYXJkLmdldCgiZ2F0ZV9wYWlyIikKICAgIGlmIHByaW1hcnkgPT0gImhpZ2hfZGlhZ25vc3RpY19zdXBwb3J0IjoKICAgICAgICByZW1lZGlhdGlvbl9jbGFzcyA9ICJzdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2wiCiAgICAgICAgYWN0aW9uID0gIkRlc2lnbiBhIHN1cHBvcnQtYXdhcmUgbmVnYXRpdmUgY29udHJvbCBiZWZvcmUgcmVjb25zaWRlcmluZyBkb3duZ3JhZGUgcHJlc3N1cmUuIgogICAgICAgIHZhbGlkYXRpb24gPSBbCiAgICAgICAgICAgICJidWlsZCBkaXNhYmxlZCBuZWdhdGl2ZS1jb250cm9sIGNhc2UiLAogICAgICAgICAgICAiY29tcGFyZSBkb3duZ3JhZGUgcHJlc3N1cmUgYWdhaW5zdCBoaWdoLXN1cHBvcnQgcmV0ZW50aW9uIGJhc2VsaW5lIiwKICAgICAgICAgICAgInJlcnVuIGNhdXNlIGRlY29tcG9zaXRpb24iLAogICAgICAgICAgICAia2VlcCBtdXRhdGlvbl9hbGxvd2VkIGZhbHNlIiwKICAgICAgICBdCiAgICBlbGlmIHByaW1hcnkgPT0gImhldXJpc3RpY19vdmVyX3NlbnNpdGl2aXR5IiBvciAiaGV1cmlzdGljX292ZXJfc2Vuc2l0aXZpdHkiIGluIGNhdXNlczoKICAgICAgICByZW1lZGlhdGlvbl9jbGFzcyA9ICJkaXNhYmxlZF9jYWxpYnJhdGlvbl9wbGFuIgogICAgICAgIGFjdGlvbiA9ICJDcmVhdGUgYSBkaXNhYmxlZCBjYWxpYnJhdGlvbiBwbGFuIHRoYXQgdGVzdHMgdGhyZXNob2xkIHNlbnNpdGl2aXR5IHdpdGhvdXQgY2hhbmdpbmcgY2xhc3NpZmllciBiZWhhdmlvci4iCiAgICAgICAgdmFsaWRhdGlvbiA9IFsKICAgICAgICAgICAgInJ1biBjYWxpYnJhdGlvbiBhcyByZXBvcnQtb25seSIsCiAgICAgICAgICAgICJjb21wYXJlIGJsb2NrZXIgY291bnQgYmVmb3JlL2FmdGVyIHByb3Bvc2FsIiwKICAgICAgICAgICAgImRvIG5vdCBhY3RpdmF0ZSBwb2xpY3kiLAogICAgICAgICAgICAia2VlcCBtdXRhdGlvbl9hbGxvd2VkIGZhbHNlIiwKICAgICAgICBdCiAgICBlbGlmIHByaW1hcnkgPT0gIm1pc3NpbmdfZmluZGluZ19wcm92ZW5hbmNlIjoKICAgICAgICByZW1lZGlhdGlvbl9jbGFzcyA9ICJmaW5kaW5nX3Byb3ZlbmFuY2VfcmVwYWlyIgogICAgICAgIGFjdGlvbiA9ICJBZGQgZXhwbGljaXQgZmluZGluZyBwcm92ZW5hbmNlIGJlZm9yZSB0aGUgY2FuZGlkYXRlIGNhbiBiZSByZWNvbnNpZGVyZWQuIgogICAgICAgIHZhbGlkYXRpb24gPSBbCiAgICAgICAgICAgICJlbWl0IGZpbmRpbmcgcHJvdmVuYW5jZSByZWNvcmQiLAogICAgICAgICAgICAicmVydW4gcG9saWN5IGltcGFjdCBjYXJkcyIsCiAgICAgICAgICAgICJyZXJ1biBkZWNpc2lvbiByZWNvcmQiLAogICAgICAgICAgICAia2VlcCBtdXRhdGlvbl9hbGxvd2VkIGZhbHNlIiwKICAgICAgICBdCiAgICBlbHNlOgogICAgICAgIHJlbWVkaWF0aW9uX2NsYXNzID0gIm1hbnVhbF9yZW1lZGlhdGlvbl9yZXZpZXciCiAgICAgICAgYWN0aW9uID0gIlJldGFpbiBibG9jayBhbmQgY29sbGVjdCBhZGRpdGlvbmFsIGRpYWdub3N0aWMgZmVhdHVyZXMuIgogICAgICAgIHZhbGlkYXRpb24gPSBbCiAgICAgICAgICAgICJtYW51YWwgcmV2aWV3IHJlcXVpcmVkIiwKICAgICAgICAgICAgIm5vIGF1dG9tYXRpYyBkb3duZ3JhZGUiLAogICAgICAgICAgICAia2VlcCBtdXRhdGlvbl9hbGxvd2VkIGZhbHNlIiwKICAgICAgICBdCiAgICByZXR1cm4gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctcmVtZWRpYXRpb24tdGFzay12MC41LjMiLAogICAgICAgICJ0YXNrX2lkIjogZiJyZW1lZGlhdGlvbi10YXNrLXYwLTUtMy17aWR4OjAzZH0iLAogICAgICAgICJzb3VyY2VfY2FyZF9pZCI6IGNhcmQuZ2V0KCJjYXJkX2lkIiksCiAgICAgICAgImdhdGVfcGFpciI6IGdhdGVfcGFpciwKICAgICAgICAicHJpbWFyeV9jYXVzZSI6IHByaW1hcnksCiAgICAgICAgImNhdXNlcyI6IGNhdXNlcywKICAgICAgICAicmVtZWRpYXRpb25fY2xhc3MiOiByZW1lZGlhdGlvbl9jbGFzcywKICAgICAgICAicmVtZWRpYXRpb25fYWN0aW9uIjogYWN0aW9uLAogICAgICAgICJyZXF1aXJlZF92YWxpZGF0aW9uIjogdmFsaWRhdGlvbiwKICAgICAgICAic3RhdHVzIjogInBsYW5uZWRfbm90X2FwcGxpZWQiLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJub25fY2xhaW1fbG9jayI6ICJSZW1lZGlhdGlvbiB0YXNrcyBhcmUgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIHBsYW5uaW5nIGFydGlmYWN0cyBvbmx5LiIsCiAgICB9CgpkZWYgdGFza19tZCh0KToKICAgIGNoZWNrcyA9ICJcbiIuam9pbihmIi0ge3h9IiBmb3IgeCBpbiB0WyJyZXF1aXJlZF92YWxpZGF0aW9uIl0pCiAgICByZXR1cm4gZiIiIiMge3RbJ3Rhc2tfaWQnXX0KCi0gU291cmNlIGNhcmQ6IGB7dFsnc291cmNlX2NhcmRfaWQnXX1gCi0gR2F0ZSBwYWlyOiBge3RbJ2dhdGVfcGFpciddfWAKLSBSZW1lZGlhdGlvbiBjbGFzczogYHt0WydyZW1lZGlhdGlvbl9jbGFzcyddfWAKLSBTdGF0dXM6IGB7dFsnc3RhdHVzJ119YAotIE11dGF0aW9uIGFsbG93ZWQ6IGB7dFsnbXV0YXRpb25fYWxsb3dlZCddfWAKLSBQb2xpY3kgZW5mb3JjZWQ6IGB7dFsncG9saWN5X2VuZm9yY2VkJ119YAoKIyMgQWN0aW9uCgp7dFsncmVtZWRpYXRpb25fYWN0aW9uJ119CgojIyBSZXF1aXJlZCBWYWxpZGF0aW9uCgp7Y2hlY2tzfQoKIyMgQm91bmRhcnkKCnt0Wydub25fY2xhaW1fbG9jayddfQoiIiIKCmRlZiBjaGFydHMoc3VtbWFyeSk6CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGUpKQogICAgICAgIHJldHVybiBwYXRocwogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQogICAgZm9yIHRpdGxlLCBkYXRhLCBmbmFtZSBpbiBbCiAgICAgICAgKCJSZW1lZGlhdGlvbiBDbGFzcyBDb3VudHMiLCBzdW1tYXJ5WyJyZW1lZGlhdGlvbl9jbGFzc19jb3VudHMiXSwgInJlbWVkaWF0aW9uX2NsYXNzX2NvdW50cy5wbmciKSwKICAgICAgICAoIlByaW1hcnkgQ2F1c2UgQ291bnRzIiwgc3VtbWFyeVsicHJpbWFyeV9jYXVzZV9jb3VudHMiXSwgInJlbWVkaWF0aW9uX3ByaW1hcnlfY2F1c2VfY291bnRzLnBuZyIpLAogICAgICAgICgiR2F0ZSBJbnZvbHZlbWVudCIsIHN1bW1hcnlbImdhdGVfaW52b2x2ZW1lbnRfY291bnRzIl0sICJyZW1lZGlhdGlvbl9nYXRlX2ludm9sdmVtZW50LnBuZyIpLAogICAgXToKICAgICAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgICAgIHBsdC5iYXIobGlzdChkYXRhLmtleXMoKSksIGxpc3QoZGF0YS52YWx1ZXMoKSkpCiAgICAgICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgICAgICBwbHQueWxhYmVsKCJDb3VudCIpCiAgICAgICAgcGx0LnRpdGxlKHRpdGxlKQogICAgICAgIHNhdmUoZm5hbWUpCiAgICByZXR1cm4gcGF0aHMKCmRlZiByZXBvcnQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC41LjMgQ2F1c2UtU3BlY2lmaWMgUmVtZWRpYXRpb24gUGxhbiIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIFNvdXJjZSBjYXVzZSBjYXJkczogYHtzdW1tYXJ5Wydzb3VyY2VfY2F1c2VfY2FyZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBSZW1lZGlhdGlvbiB0YXNrIGNvdW50OiBge3N1bW1hcnlbJ3JlbWVkaWF0aW9uX3Rhc2tfY291bnQnXX1gIiwKICAgICAgICBmIi0gRmluYWwgcmVjb21tZW5kYXRpb246IGB7c3VtbWFyeVsnZmluYWxfcmVjb21tZW5kYXRpb24nXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzdW1tYXJ5WydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIFBvbGljeSBlbmZvcmNlZDogYHtzdW1tYXJ5Wydwb2xpY3lfZW5mb3JjZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVtZWRpYXRpb24gQ2xhc3MgQ291bnRzIiwKICAgICAgICAiIiwKICAgICAgICAifCBDbGFzcyB8IENvdW50IHwiLAogICAgICAgICJ8LS0tfC0tLTp8IiwKICAgIF0KICAgIGZvciBrLHYgaW4gc3VtbWFyeVsicmVtZWRpYXRpb25fY2xhc3NfY291bnRzIl0uaXRlbXMoKToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7a31gIHwge3Z9IHwiKQogICAgbGluZXMgKz0gWyIiLCAiIyMgVGFza3MiLCAiIiwgInwgVGFzayB8IEdhdGUgcGFpciB8IENsYXNzIHwgU3RhdHVzIHwgQWN0aW9uIHwiLCAifC0tLXwtLS18LS0tfC0tLXwtLS18Il0KICAgIGZvciB0IGluIHN1bW1hcnlbInJlbWVkaWF0aW9uX3Rhc2tzIl06CiAgICAgICAgYWN0aW9uID0gdFsicmVtZWRpYXRpb25fYWN0aW9uIl0ucmVwbGFjZSgifCIsICJcXHwiKQogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHt0Wyd0YXNrX2lkJ119YCB8IGB7dFsnZ2F0ZV9wYWlyJ119YCB8IGB7dFsncmVtZWRpYXRpb25fY2xhc3MnXX1gIHwgYHt0WydzdGF0dXMnXX1gIHwge2FjdGlvbn0gfCIpCiAgICBsaW5lcyArPSBbIiIsICIjIyBDaGFydHMiLCAiIl0KICAgIGZvciBwIGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgcmVsID0gb3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoIlxcIiwgIi8iKQogICAgICAgIGxpbmVzLmFwcGVuZChmIiFbe1BhdGgocCkuc3RlbX1dKHtyZWx9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzdW1tYXJ5WyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgY2F1c2UgPSByanNvbihDQVVTRVMpCiAgICBjYXJkcyA9IGNhdXNlLmdldCgiY2F1c2VfY2FyZHMiLCBbXSkKICAgIHRhc2tzID0gW3Rhc2tfZm9yKGMsIGkrMSkgZm9yIGksYyBpbiBlbnVtZXJhdGUoY2FyZHMpXQogICAgVEFTS1MubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgZm9yIHQgaW4gdGFza3M6CiAgICAgICAgd2pzb24oVEFTS1MgLyBmInt0Wyd0YXNrX2lkJ119Lmpzb24iLCB0KQogICAgICAgIHd0ZXh0KFRBU0tTIC8gZiJ7dFsndGFza19pZCddfS5tZCIsIHRhc2tfbWQodCkpCiAgICBjbGFzc19jb3VudHMsIGNhdXNlX2NvdW50cywgZ2F0ZV9jb3VudHMgPSBDb3VudGVyKCksIENvdW50ZXIoKSwgQ291bnRlcigpCiAgICBmb3IgdCBpbiB0YXNrczoKICAgICAgICBjbGFzc19jb3VudHNbdFsicmVtZWRpYXRpb25fY2xhc3MiXV0gKz0gMQogICAgICAgIGNhdXNlX2NvdW50c1t0WyJwcmltYXJ5X2NhdXNlIl1dICs9IDEKICAgICAgICAjIGdhdGUgcGFpciBmb3JtYXQgQStCCiAgICAgICAgZm9yIGcgaW4gc3RyKHRbImdhdGVfcGFpciJdKS5zcGxpdCgiKyIpOgogICAgICAgICAgICBpZiBnIGFuZCBnICE9ICJOb25lIjoKICAgICAgICAgICAgICAgIGdhdGVfY291bnRzW2ddICs9IDEKICAgIGlmIGNsYXNzX2NvdW50cy5nZXQoInN1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbCIsIDApID4gMDoKICAgICAgICBmaW5hbCA9ICJidWlsZF9zdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2xzX25leHQiCiAgICBlbGlmIGNsYXNzX2NvdW50cy5nZXQoImRpc2FibGVkX2NhbGlicmF0aW9uX3BsYW4iLCAwKSA+IDA6CiAgICAgICAgZmluYWwgPSAiYnVpbGRfZGlzYWJsZWRfY2FsaWJyYXRpb25fcGxhbl9uZXh0IgogICAgZWxzZToKICAgICAgICBmaW5hbCA9ICJyZXRhaW5fYmxvY2tfYW5kX2NvbGxlY3RfbW9yZV9mZWF0dXJlcyIKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1jYXVzZS1zcGVjaWZpYy1yZW1lZGlhdGlvbi1wbGFuLXYwLjUuMyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJpbnB1dCI6ICJyZXBvcnRzL292ZXJfcGVuYWx0eV9jYXVzZXMvbGF0ZXN0X292ZXJfcGVuYWx0eV9jYXVzZV9kZWNvbXBvc2l0aW9uLmpzb24iLAogICAgICAgICJzb3VyY2VfY2F1c2VfY2FyZF9jb3VudCI6IGxlbihjYXJkcyksCiAgICAgICAgInJlbWVkaWF0aW9uX3Rhc2tfY291bnQiOiBsZW4odGFza3MpLAogICAgICAgICJyZW1lZGlhdGlvbl9jbGFzc19jb3VudHMiOiBkaWN0KGNsYXNzX2NvdW50cyksCiAgICAgICAgInByaW1hcnlfY2F1c2VfY291bnRzIjogZGljdChjYXVzZV9jb3VudHMpLAogICAgICAgICJnYXRlX2ludm9sdmVtZW50X2NvdW50cyI6IGRpY3QoZ2F0ZV9jb3VudHMpLAogICAgICAgICJyZW1lZGlhdGlvbl90YXNrcyI6IHRhc2tzLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IGZpbmFsLAogICAgICAgICJib3VuZGFyeSI6ICJDYXVzZS1zcGVjaWZpYyByZW1lZGlhdGlvbiBwbGFubmluZyBpcyBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgcGxhbm5pbmcgb25seS4gSXQgZG9lcyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvZXMgbm90IHZhbGlkYXRlIHNpbGljb24sIHByb2R1Y3RzLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJ2MC41LjQgc2hvdWxkIGltcGxlbWVudCBzdXBwb3J0LWF3YXJlIG5lZ2F0aXZlIGNvbnRyb2xzIGFzIGRpc2FibGVkL3JlcG9ydC1vbmx5IHRlc3RzLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAiY2F1c2Vfc3BlY2lmaWNfcmVtZWRpYXRpb25fcGxhbl92MF81XzMuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X2NhdXNlX3NwZWNpZmljX3JlbWVkaWF0aW9uX3BsYW4uanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAiY2F1c2Vfc3BlY2lmaWNfcmVtZWRpYXRpb25fcGxhbl92MF81XzMubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X2NhdXNlX3NwZWNpZmljX3JlbWVkaWF0aW9uX3BsYW4ubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgInNvdXJjZV9jYXVzZV9jYXJkX2NvdW50Ijogc3VtbWFyeVsic291cmNlX2NhdXNlX2NhcmRfY291bnQiXSwKICAgICAgICAicmVtZWRpYXRpb25fdGFza19jb3VudCI6IHN1bW1hcnlbInJlbWVkaWF0aW9uX3Rhc2tfY291bnQiXSwKICAgICAgICAicmVtZWRpYXRpb25fY2xhc3NfY291bnRzIjogc3VtbWFyeVsicmVtZWRpYXRpb25fY2xhc3NfY291bnRzIl0sCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogc3VtbWFyeVsiZmluYWxfcmVjb21tZW5kYXRpb24iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogc3VtbWFyeVsicG9saWN5X2VuZm9yY2VkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9yZW1lZGlhdGlvbl9wbGFuL2xhdGVzdF9jYXVzZV9zcGVjaWZpY19yZW1lZGlhdGlvbl9wbGFuLm1kIiwKICAgIH0sIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg=="
write(ROOT/"scripts"/"benchmarks"/"generate_cause_specific_remediation_plan.py", base64.b64decode(runner_b64).decode())

write(ROOT/"reports"/"remediation_plan"/"README.md", """# Cause-Specific Remediation Plan Reports

Current layer: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**

## Purpose

This folder stores remediation plans and task cards derived from v0.5.2 over-penalty cause cards.

## Primary command

```powershell
python scripts/benchmarks/generate_cause_specific_remediation_plan.py
```

## README Update Rule

Update this mini README whenever remediation schemas, task paths, or planning rules change.

Boundary: remediation planning reports are local classifier-governance artifacts only.
""")
write(ROOT/"visuals"/"remediation_plan"/"README.md", """# Remediation Plan Visuals

Current layer: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**

## Purpose

This folder stores charts summarizing remediation task classes and gate involvement.

## README Update Rule

Update this mini README whenever remediation chart names or meanings change.

Boundary: remediation visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"remediation_plan"/"v0_5_3"/"README.md", """# v0.5.3 Remediation Plan Charts

Expected charts:

- `remediation_class_counts.png`
- `remediation_primary_cause_counts.png`
- `remediation_gate_involvement.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local remediation-planning diagnostics only.
""")

# README
p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.2[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.1[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.2 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.3 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.2-ready |", "| Task routing matrix | geometry-aware / v0.5.3-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.2 |", "| Agent contract version sync | current / v0.5.3 |")
if "| Remediation plan |" not in r:
    r=r.replace("| Over-penalty cause charts | `visuals/over_penalty_causes/v0_5_2/` |\n",
                "| Over-penalty cause charts | `visuals/over_penalty_causes/v0_5_2/` |\n| Remediation plan | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` |\n| Remediation plan charts | `visuals/remediation_plan/v0_5_3/` |\n")
if "python scripts/benchmarks/generate_cause_specific_remediation_plan.py" not in r:
    r=r.replace("python scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython scripts/release/validate_release.py")
if "    remediation_plan/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    remediation_plan/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    remediation_plan/\n")
section="""## Cause-Specific Remediation Plan v0.5.3

v0.5.3 converts v0.5.2 cause cards into non-mutating remediation tasks.

Primary command:

```powershell
python scripts/benchmarks/generate_cause_specific_remediation_plan.py
```

Primary outputs:

```text
reports/remediation_plan/latest_cause_specific_remediation_plan.json
reports/remediation_plan/latest_cause_specific_remediation_plan.md
reports/remediation_plan/tasks/v0_5_3/
visuals/remediation_plan/v0_5_3/
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
```

Boundary: cause-specific remediation planning is local classifier-governance planning only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Cause-Specific Remediation Plan v0.5.3" not in r:
    r=r.replace("## Over-Penalty Cause Decomposition v0.5.2", section+"## Over-Penalty Cause Decomposition v0.5.2",1)
lesson="| L-035 | v0.5.2 showed all blocked candidates were high-support / heuristic-sensitivity cases. | Cause cards identify why a blocker exists, but do not define the next safe work unit. | High-support downgrade pressure must become support-aware negative-control tasks before calibration or policy design. |"
if "L-035" not in r:
    r=r.replace("| L-034 | v0.5.1 promoted the active blocker, but a blocker is not actionable until decomposed into causes. | Completed-signal retirement identifies what is next; it does not specify how to remediate the blocker. | When Nexus promotes a blocker, the next layer must convert the blocker into cause-specific remediation cards before any new policy design. |\n",
                "| L-034 | v0.5.1 promoted the active blocker, but a blocker is not actionable until decomposed into causes. | Completed-signal retirement identifies what is next; it does not specify how to remediate the blocker. | When Nexus promotes a blocker, the next layer must convert the blocker into cause-specific remediation cards before any new policy design. |\n"+lesson+"\n")
if "| v0.5.3 |" not in r:
    r=r.replace("| v0.5.2 | Over-penalty cause decomposition and remediation cards for blocked controlled downgrades. |\n",
                "| v0.5.2 | Over-penalty cause decomposition and remediation cards for blocked controlled downgrades. |\n| v0.5.3 | Cause-specific remediation plan for high-support blocked downgrade candidates. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**

Recommended goals:

- Convert v0.5.3 support-aware tasks into disabled/report-only negative-control tests.
- Compare downgrade pressure against high-support retention baselines.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: negative controls are local classifier governance only.
""", r, flags=re.S)
write(p,r)

# AGENTS
p=ROOT/"AGENTS.md"; backup(p,"agents"); a=read(p)
a=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**", a)
if "generate_cause_specific_remediation_plan.py" not in a:
    a=a.replace("python scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython -m unittest discover -s tests",
                "python scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython -m unittest discover -s tests")
if "| Remediation plan patch |" not in a:
    a=a.replace("| Over-penalty cause patch | `reports/over_penalty_causes/`, `visuals/over_penalty_causes/`, readiness gate | cause cards + release validator; no classifier mutation |\n",
                "| Over-penalty cause patch | `reports/over_penalty_causes/`, `visuals/over_penalty_causes/`, readiness gate | cause cards + release validator; no classifier mutation |\n| Remediation plan patch | `reports/remediation_plan/`, `visuals/remediation_plan/`, cause cards | remediation tasks + release validator; no classifier mutation |\n")
write(p,a)

# route map
p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.3"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["cause_specific_remediation_plan"]={
    "read_first":["reports/over_penalty_causes/latest_over_penalty_cause_decomposition.json"],
    "validate":["python scripts/benchmarks/generate_cause_specific_remediation_plan.py","python scripts/release/validate_release.py"],
    "evidence":["reports/remediation_plan/latest_cause_specific_remediation_plan.md","reports/remediation_plan/tasks/v0_5_3/","visuals/remediation_plan/v0_5_3/"],
    "mutation_lock":"Does not change classifier behavior; emits remediation tasks only."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

# task matrix
p=ROOT/"rcc"/"nexus"/"task_routing_matrix.md"; backup(p,"task_matrix"); m=read(p)
m=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.2[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**", m)
if "| Remediation plan patch |" not in m:
    m=m.replace("| Over-penalty cause patch | outer | validation | governance | readiness gate + regression review | cause cards + charts + release validator | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` |\n",
                "| Over-penalty cause patch | outer | validation | governance | readiness gate + regression review | cause cards + charts + release validator | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` |\n| Remediation plan patch | outer | validation | governance | cause cards + remediation tasks | remediation report + charts + release validator | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` |\n")
write(p,m)

# atlas
p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.3 | Cause-specific remediation plan |" not in t:
    t=t.replace("| v0.5.2 | Over-penalty cause decomposition | `python scripts/benchmarks/run_over_penalty_cause_decomposition.py` | Converts active blocker into cause-specific remediation cards | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` | `visuals/over_penalty_causes/v0_5_2/` |\n",
                "| v0.5.2 | Over-penalty cause decomposition | `python scripts/benchmarks/run_over_penalty_cause_decomposition.py` | Converts active blocker into cause-specific remediation cards | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` | `visuals/over_penalty_causes/v0_5_2/` |\n| v0.5.3 | Cause-specific remediation plan | `python scripts/benchmarks/generate_cause_specific_remediation_plan.py` | Converts cause cards into non-mutating remediation tasks | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` | `visuals/remediation_plan/v0_5_3/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_3_cause_specific_remediation_plan.md", f"""# TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan

Generated: {NOW}

## Purpose

Convert v0.5.2 cause cards into non-mutating remediation tasks.

## Adds

- `scripts/benchmarks/generate_cause_specific_remediation_plan.py`
- `reports/remediation_plan/`
- `reports/remediation_plan/tasks/v0_5_3/`
- `visuals/remediation_plan/v0_5_3/`

## Boundary

Cause-specific remediation planning is local classifier-governance planning only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.3 patch written")
