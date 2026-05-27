
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
        d=ROOT/"reports"/"over_penalty_causes"/"v0_5_2"/"backups"/f"{p.name}_before_v0_5_2_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
runner_b64="CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdClJFQURJTkVTUyA9IFJPT1QgLyAicmVwb3J0cyIgLyAiZW5mb3JjZW1lbnRfcmVhZGluZXNzIiAvICJsYXRlc3RfZW5mb3JjZW1lbnRfcmVhZGluZXNzX2dhdGUuanNvbiIKT1VUID0gUk9PVCAvICJyZXBvcnRzIiAvICJvdmVyX3BlbmFsdHlfY2F1c2VzIgpDQVJEUyA9IE9VVCAvICJjYXJkcyIgLyAidjBfNV8yIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gIm92ZXJfcGVuYWx0eV9jYXVzZXMiIC8gInYwXzVfMiIKCmRlZiByanNvbihwKTogcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCmRlZiB3anNvbihwLCB4KToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChqc29uLmR1bXBzKHgsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQpkZWYgd3RleHQocCwgcyk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQocywgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiBjYXVzZXMocm93KToKICAgIHJlYXNvbnMgPSByb3cuZ2V0KCJiYXNlbGluZV9vdmVyX3BlbmFsdHlfcmVhc29ucyIsIFtdKSBvciBbXQogICAgZmluZGluZ3MgPSBpbnQocm93LmdldCgiZmluZGluZ3NfY291bnQiLCAwKSBvciAwKQogICAgc2V2ZXJpdHkgPSBpbnQocm93LmdldCgiZHJpZnRfc2V2ZXJpdHkiLCAwKSBvciAwKQogICAgb3V0ID0gW10KICAgIGlmICJtaXNzaW5nX2ZpbmRpbmdfcHJvdmVuYW5jZSIgaW4gcmVhc29ucyBvciBmaW5kaW5ncyA9PSAwOgogICAgICAgIG91dC5hcHBlbmQoIm1pc3NpbmdfZmluZGluZ19wcm92ZW5hbmNlIikKICAgIGlmICJoaWdoX2RpYWdub3N0aWNfc3VwcG9ydCIgaW4gcmVhc29uczoKICAgICAgICBvdXQuYXBwZW5kKCJoaWdoX2RpYWdub3N0aWNfc3VwcG9ydCIpCiAgICBpZiAiaGlnaF9kcmlmdF9zZXZlcml0eSIgaW4gcmVhc29ucyBvciBzZXZlcml0eSA+PSAyOgogICAgICAgIG91dC5hcHBlbmQoImhpZ2hfZHJpZnRfc2V2ZXJpdHkiKQogICAgaWYgb3V0ID09IFsiaGlnaF9kaWFnbm9zdGljX3N1cHBvcnQiXToKICAgICAgICBvdXQuYXBwZW5kKCJoZXVyaXN0aWNfb3Zlcl9zZW5zaXRpdml0eSIpCiAgICByZXR1cm4gb3V0IG9yIFsidW5kaWZmZXJlbnRpYXRlZF9vdmVyX3BlbmFsdHkiXQoKUkVNRURZID0gewogICAgIm1pc3NpbmdfZmluZGluZ19wcm92ZW5hbmNlIjogIkFkZCBleHBsaWNpdCBmaW5kaW5nIHByb3ZlbmFuY2UgYmVmb3JlIHJlY29uc2lkZXJpbmcgdGhlIGRvd25ncmFkZS4iLAogICAgImhpZ2hfZGlhZ25vc3RpY19zdXBwb3J0IjogIkFkZCBhIHNlY29uZGFyeSBldmlkZW5jZS1wcmVzc3VyZSB0ZXN0IGJlZm9yZSBkb3duZ3JhZGluZyBoaWdoLXN1cHBvcnQgY2FzZXMuIiwKICAgICJoaWdoX2RyaWZ0X3NldmVyaXR5IjogIlNlcGFyYXRlIHNldmVyZSBkcmlmdCBjYXNlcyBhbmQgcmVxdWlyZSBtYW51YWwgcmV2aWV3LiIsCiAgICAiaGV1cmlzdGljX292ZXJfc2Vuc2l0aXZpdHkiOiAiUHJlcGFyZSBhIGRpc2FibGVkIGNhbGlicmF0aW9uIHBsYW47IGRvIG5vdCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvci4iLAogICAgInVuZGlmZmVyZW50aWF0ZWRfb3Zlcl9wZW5hbHR5IjogIlJldGFpbiB0aGUgYmxvY2sgYW5kIGNvbGxlY3QgbW9yZSBkaWFnbm9zdGljIGZlYXR1cmVzLiIsCn0KCmRlZiBjYXJkKHJvdywgaSk6CiAgICBjcyA9IGNhdXNlcyhyb3cpCiAgICByZXR1cm4gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctb3Zlci1wZW5hbHR5LWNhdXNlLWNhcmQtdjAuNS4yIiwKICAgICAgICAiY2FyZF9pZCI6IGYib3Zlci1wZW5hbHR5LWNhdXNlLXYwLTUtMi17aTowM2R9IiwKICAgICAgICAiZ2F0ZV9wYWlyIjogcm93LmdldCgiZ2F0ZV9wYWlyIiksCiAgICAgICAgImdhdGVfYSI6IHJvdy5nZXQoImdhdGVfYSIpLAogICAgICAgICJnYXRlX2IiOiByb3cuZ2V0KCJnYXRlX2IiKSwKICAgICAgICAicmVhZGluZXNzX3N0YXR1cyI6IHJvdy5nZXQoInJlYWRpbmVzc19zdGF0dXMiKSwKICAgICAgICAiZGVjaXNpb24iOiByb3cuZ2V0KCJkZWNpc2lvbiIpLAogICAgICAgICJjdXJyZW50X2NsYXNzaWZpY2F0aW9uIjogcm93LmdldCgiY3VycmVudF9jbGFzc2lmaWNhdGlvbiIpLAogICAgICAgICJzaW11bGF0ZWRfcG9saWN5X2NsYXNzaWZpY2F0aW9uIjogcm93LmdldCgic2ltdWxhdGVkX3BvbGljeV9jbGFzc2lmaWNhdGlvbiIpLAogICAgICAgICJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSI6IHJvdy5nZXQoImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIiksCiAgICAgICAgImZpbmRpbmdzX2NvdW50Ijogcm93LmdldCgiZmluZGluZ3NfY291bnQiKSwKICAgICAgICAiZHJpZnRfc2V2ZXJpdHkiOiByb3cuZ2V0KCJkcmlmdF9zZXZlcml0eSIpLAogICAgICAgICJjYXVzZXMiOiBjcywKICAgICAgICAicHJpbWFyeV9jYXVzZSI6IGNzWzBdLAogICAgICAgICJyZW1lZGlhdGlvbiI6IFJFTUVEWVtjc1swXV0sCiAgICAgICAgImNhbmRpZGF0ZV9zdGF0dXMiOiAiYmxvY2tlZF91bnRpbF9yZW1lZGlhdGVkIiwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAibm9uX2NsYWltX2xvY2siOiAiQ2F1c2UgY2FyZHMgYXJlIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSBkaWFnbm9zdGljcyBvbmx5LiIsCiAgICB9CgpkZWYgY2FyZF9tZChjKToKICAgIHJldHVybiBmIiIiIyB7Y1snY2FyZF9pZCddfQoKLSBHYXRlIHBhaXI6IGB7Y1snZ2F0ZV9wYWlyJ119YAotIFByaW1hcnkgY2F1c2U6IGB7Y1sncHJpbWFyeV9jYXVzZSddfWAKLSBDYXVzZXM6IGB7JywgJy5qb2luKGNbJ2NhdXNlcyddKX1gCi0gQ2FuZGlkYXRlIHN0YXR1czogYHtjWydjYW5kaWRhdGVfc3RhdHVzJ119YAotIE11dGF0aW9uIGFsbG93ZWQ6IGB7Y1snbXV0YXRpb25fYWxsb3dlZCddfWAKLSBQb2xpY3kgZW5mb3JjZWQ6IGB7Y1sncG9saWN5X2VuZm9yY2VkJ119YAoKIyMgUmVtZWRpYXRpb24KCntjWydyZW1lZGlhdGlvbiddfQoKIyMgQm91bmRhcnkKCntjWydub25fY2xhaW1fbG9jayddfQoiIiIKCmRlZiBjaGFydHMoc3VtbWFyeSk6CiAgICBwYXRocyA9IFtdCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGUpKQogICAgICAgIHJldHVybiBwYXRocwogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQogICAgZm9yIHRpdGxlLCBkYXRhLCBmbmFtZSBpbiBbCiAgICAgICAgKCJPdmVyLVBlbmFsdHkgQ2F1c2UgQ291bnRzIiwgc3VtbWFyeVsiY2F1c2VfY291bnRzIl0sICJvdmVyX3BlbmFsdHlfY2F1c2VfY291bnRzLnBuZyIpLAogICAgICAgICgiUHJpbWFyeSBDYXVzZSBDb3VudHMiLCBzdW1tYXJ5WyJwcmltYXJ5X2NhdXNlX2NvdW50cyJdLCAib3Zlcl9wZW5hbHR5X3ByaW1hcnlfY2F1c2VfY291bnRzLnBuZyIpLAogICAgICAgICgiQmxvY2tlZCBHYXRlIEludm9sdmVtZW50Iiwgc3VtbWFyeVsiZ2F0ZV9pbnZvbHZlbWVudF9jb3VudHMiXSwgIm92ZXJfcGVuYWx0eV9nYXRlX2ludm9sdmVtZW50LnBuZyIpLAogICAgXToKICAgICAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksNCkpCiAgICAgICAgcGx0LmJhcihsaXN0KGRhdGEua2V5cygpKSwgbGlzdChkYXRhLnZhbHVlcygpKSkKICAgICAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgICAgIHBsdC55bGFiZWwoIkNvdW50IikKICAgICAgICBwbHQudGl0bGUodGl0bGUpCiAgICAgICAgc2F2ZShmbmFtZSkKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzdW1tYXJ5KToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjUuMiBPdmVyLVBlbmFsdHkgQ2F1c2UgRGVjb21wb3NpdGlvbiIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIEJsb2NrZWQgY2FuZGlkYXRlIGNvdW50OiBge3N1bW1hcnlbJ2Jsb2NrZWRfY2FuZGlkYXRlX2NvdW50J119YCIsCiAgICAgICAgZiItIENhdXNlIGNhcmQgY291bnQ6IGB7c3VtbWFyeVsnY2F1c2VfY2FyZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBGaW5hbCByZWNvbW1lbmRhdGlvbjogYHtzdW1tYXJ5WydmaW5hbF9yZWNvbW1lbmRhdGlvbiddfWAiLAogICAgICAgIGYiLSBNdXRhdGlvbiBhbGxvd2VkOiBge3N1bW1hcnlbJ211dGF0aW9uX2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gUG9saWN5IGVuZm9yY2VkOiBge3N1bW1hcnlbJ3BvbGljeV9lbmZvcmNlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBDYXVzZSBDb3VudHMiLAogICAgICAgICIiLAogICAgICAgICJ8IENhdXNlIHwgQ291bnQgfCIsCiAgICAgICAgInwtLS18LS0tOnwiLAogICAgXQogICAgZm9yIGssdiBpbiBzdW1tYXJ5WyJjYXVzZV9jb3VudHMiXS5pdGVtcygpOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtrfWAgfCB7dn0gfCIpCiAgICBsaW5lcyArPSBbIiIsICIjIyBDYXJkcyIsICIiLCAifCBDYXJkIHwgR2F0ZSBwYWlyIHwgUHJpbWFyeSBjYXVzZSB8IFJlbWVkaWF0aW9uIHwiLCAifC0tLXwtLS18LS0tfC0tLXwiXQogICAgZm9yIGMgaW4gc3VtbWFyeVsiY2F1c2VfY2FyZHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiJ8IGB7Y1snY2FyZF9pZCddfWAgfCBge2NbJ2dhdGVfcGFpciddfWAgfCBge2NbJ3ByaW1hcnlfY2F1c2UnXX1gIHwge2NbJ3JlbWVkaWF0aW9uJ119IHwiKQogICAgbGluZXMgKz0gWyIiLCAiIyMgQ2hhcnRzIiwgIiJdCiAgICBmb3IgcCBpbiBzdW1tYXJ5WyJjaGFydF9wYXRocyJdOgogICAgICAgIHJlbCA9IG9zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCJcXCIsICIvIikKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7cmVsfSkiKQogICAgICAgIGxpbmVzLmFwcGVuZCgiIikKICAgIGxpbmVzICs9IFsiIyMgQm91bmRhcnkiLCAiIiwgc3VtbWFyeVsiYm91bmRhcnkiXSwgIiJdCiAgICByZXR1cm4gIlxuIi5qb2luKGxpbmVzKQoKZGVmIG1haW4oKToKICAgIHJlYWRpbmVzcyA9IHJqc29uKFJFQURJTkVTUykKICAgIGJsb2NrZWQgPSBbeCBmb3IgeCBpbiByZWFkaW5lc3MuZ2V0KCJyZWFkaW5lc3Nfcm93cyIsIFtdKSBpZiB4LmdldCgicmVhZGluZXNzX3N0YXR1cyIpID09ICJCTE9DS0VEX0JZX09WRVJfUEVOQUxUWSJdCiAgICBjYXJkcyA9IFtjYXJkKHgsIGkrMSkgZm9yIGkseCBpbiBlbnVtZXJhdGUoYmxvY2tlZCldCiAgICBDQVJEUy5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBmb3IgYyBpbiBjYXJkczoKICAgICAgICB3anNvbihDQVJEUyAvIGYie2NbJ2NhcmRfaWQnXX0uanNvbiIsIGMpCiAgICAgICAgd3RleHQoQ0FSRFMgLyBmIntjWydjYXJkX2lkJ119Lm1kIiwgY2FyZF9tZChjKSkKICAgIGNhdXNlX2NvdW50cywgcHJpbWFyeSwgZ2F0ZXMgPSBDb3VudGVyKCksIENvdW50ZXIoKSwgQ291bnRlcigpCiAgICBmb3IgYyBpbiBjYXJkczoKICAgICAgICBwcmltYXJ5W2NbInByaW1hcnlfY2F1c2UiXV0gKz0gMQogICAgICAgIGZvciBjYXVzZSBpbiBjWyJjYXVzZXMiXTogY2F1c2VfY291bnRzW2NhdXNlXSArPSAxCiAgICAgICAgZ2F0ZXNbY1siZ2F0ZV9hIl1dICs9IDEKICAgICAgICBnYXRlc1tjWyJnYXRlX2IiXV0gKz0gMQogICAgZmluYWwgPSAicmVwYWlyX2ZpbmRpbmdfcHJvdmVuYW5jZV9iZWZvcmVfcG9saWN5X2Rlc2lnbiIgaWYgY2F1c2VfY291bnRzLmdldCgibWlzc2luZ19maW5kaW5nX3Byb3ZlbmFuY2UiLDApIGVsc2UgInByZXBhcmVfZGlzYWJsZWRfY2FsaWJyYXRpb25fcGxhbiIKICAgIHN1bW1hcnkgPSB7CiAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1vdmVyLXBlbmFsdHktY2F1c2UtZGVjb21wb3NpdGlvbi12MC41LjIiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiYmxvY2tlZF9jYW5kaWRhdGVfY291bnQiOiBsZW4oYmxvY2tlZCksCiAgICAgICAgImNhdXNlX2NhcmRfY291bnQiOiBsZW4oY2FyZHMpLAogICAgICAgICJjYXVzZV9jb3VudHMiOiBkaWN0KGNhdXNlX2NvdW50cyksCiAgICAgICAgInByaW1hcnlfY2F1c2VfY291bnRzIjogZGljdChwcmltYXJ5KSwKICAgICAgICAiZ2F0ZV9pbnZvbHZlbWVudF9jb3VudHMiOiBkaWN0KGdhdGVzKSwKICAgICAgICAiY2F1c2VfY2FyZHMiOiBjYXJkcywKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiZmluYWxfcmVjb21tZW5kYXRpb24iOiBmaW5hbCwKICAgICAgICAiYm91bmRhcnkiOiAiT3Zlci1wZW5hbHR5IGNhdXNlIGRlY29tcG9zaXRpb24gaXMgbG9jYWwgY2xhc3NpZmllci1nb3Zlcm5hbmNlIGFuYWx5c2lzIG9ubHkuIEl0IGRvZXMgbm90IGNoYW5nZSBjbGFzc2lmaWVyIGJlaGF2aW9yIGFuZCBkb2VzIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNS4zIHNob3VsZCBpbXBsZW1lbnQgY2F1c2Utc3BlY2lmaWMgcmVtZWRpYXRpb24gcGxhbm5pbmcgd2l0aG91dCBjbGFzc2lmaWVyIG11dGF0aW9uLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAib3Zlcl9wZW5hbHR5X2NhdXNlX2RlY29tcG9zaXRpb25fdjBfNV8yLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF9vdmVyX3BlbmFsdHlfY2F1c2VfZGVjb21wb3NpdGlvbi5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJvdmVyX3BlbmFsdHlfY2F1c2VfZGVjb21wb3NpdGlvbl92MF81XzIubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X292ZXJfcGVuYWx0eV9jYXVzZV9kZWNvbXBvc2l0aW9uLm1kIiwgcmVwb3J0KHN1bW1hcnkpKQogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJibG9ja2VkX2NhbmRpZGF0ZV9jb3VudCI6IHN1bW1hcnlbImJsb2NrZWRfY2FuZGlkYXRlX2NvdW50Il0sCiAgICAgICAgImNhdXNlX2NhcmRfY291bnQiOiBzdW1tYXJ5WyJjYXVzZV9jYXJkX2NvdW50Il0sCiAgICAgICAgImNhdXNlX2NvdW50cyI6IHN1bW1hcnlbImNhdXNlX2NvdW50cyJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IHN1bW1hcnlbImZpbmFsX3JlY29tbWVuZGF0aW9uIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvb3Zlcl9wZW5hbHR5X2NhdXNlcy9sYXRlc3Rfb3Zlcl9wZW5hbHR5X2NhdXNlX2RlY29tcG9zaXRpb24ubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo="
write(ROOT/"scripts"/"benchmarks"/"run_over_penalty_cause_decomposition.py", base64.b64decode(runner_b64).decode())

write(ROOT/"reports"/"over_penalty_causes"/"README.md", """# Over-Penalty Cause Decomposition Reports

Current layer: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**

## Purpose

This folder stores cause-specific decomposition reports and remediation cards for blocked controlled-downgrade candidates.

## Primary command

```powershell
python scripts/benchmarks/run_over_penalty_cause_decomposition.py
```

## README Update Rule

Update this mini README whenever cause-card schemas, report paths, or remediation rules change.

Boundary: cause decomposition reports are local classifier-governance artifacts only.
""")
write(ROOT/"visuals"/"over_penalty_causes"/"README.md", """# Over-Penalty Cause Visuals

Current layer: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**

## Purpose

This folder stores charts summarizing over-penalty causes and gate involvement.

## README Update Rule

Update this mini README whenever cause chart names or meanings change.

Boundary: cause visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"over_penalty_causes"/"v0_5_2"/"README.md", """# v0.5.2 Over-Penalty Cause Charts

Expected charts:

- `over_penalty_cause_counts.png`
- `over_penalty_primary_cause_counts.png`
- `over_penalty_gate_involvement.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local cause-decomposition diagnostics only.
""")

# README updates
p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.1[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.0[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.1 - Nexus Target Refresh and Completed-Signal Retirement**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.1 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.2 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.1-ready |", "| Task routing matrix | geometry-aware / v0.5.2-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.1 |", "| Agent contract version sync | current / v0.5.2 |")
if "| Over-penalty causes |" not in r:
    r=r.replace("| Nexus target refresh charts | `visuals/nexus_target_refresh/v0_5_1/` |\n",
                "| Nexus target refresh charts | `visuals/nexus_target_refresh/v0_5_1/` |\n| Over-penalty causes | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` |\n| Over-penalty cause charts | `visuals/over_penalty_causes/v0_5_2/` |\n")
if "python scripts/benchmarks/run_over_penalty_cause_decomposition.py" not in r:
    r=r.replace("python scripts/feedback/run_nexus_target_refresh.py\npython scripts/release/validate_release.py",
                "python scripts/feedback/run_nexus_target_refresh.py\npython scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython scripts/release/validate_release.py")
if "    over_penalty_causes/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    over_penalty_causes/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    over_penalty_causes/\n")
section="""## Over-Penalty Cause Decomposition v0.5.2

v0.5.2 decomposes the current active blocker promoted by v0.5.1.

Primary command:

```powershell
python scripts/benchmarks/run_over_penalty_cause_decomposition.py
```

Primary outputs:

```text
reports/over_penalty_causes/latest_over_penalty_cause_decomposition.json
reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md
reports/over_penalty_causes/cards/v0_5_2/
visuals/over_penalty_causes/v0_5_2/
```

Current lock:

```text
mutation_allowed: false
policy_enforced: false
```

Boundary: over-penalty cause decomposition is local classifier-governance analysis only. It does not change classifier behavior and does not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Over-Penalty Cause Decomposition v0.5.2" not in r:
    r=r.replace("## Nexus Target Refresh and Completed-Signal Retirement v0.5.1", section+"## Nexus Target Refresh and Completed-Signal Retirement v0.5.1",1)
lesson="| L-034 | v0.5.1 promoted the active blocker, but a blocker is not actionable until decomposed into causes. | Completed-signal retirement identifies what is next; it does not specify how to remediate the blocker. | When Nexus promotes a blocker, the next layer must convert the blocker into cause-specific remediation cards before any new policy design. |"
if "L-034" not in r:
    r=r.replace("| L-033 | v0.5.0 completed the dry-run through enforcement-readiness chain, but Nexus still ranked the old v0.4.6 dry-run target as active. | A healthy feedback score can still carry stale priorities if completed targets are not retired. | Reflective feedback must retire completed targets and promote the current active blocker, or the repo will keep recommending already-completed work. |\n",
                "| L-033 | v0.5.0 completed the dry-run through enforcement-readiness chain, but Nexus still ranked the old v0.4.6 dry-run target as active. | A healthy feedback score can still carry stale priorities if completed targets are not retired. | Reflective feedback must retire completed targets and promote the current active blocker, or the repo will keep recommending already-completed work. |\n"+lesson+"\n")
if "| v0.5.2 |" not in r:
    r=r.replace("| v0.5.1a | Public alignment polish for README metrics and AGENTS validation chain. |\n",
                "| v0.5.1a | Public alignment polish for README metrics and AGENTS validation chain. |\n| v0.5.2 | Over-penalty cause decomposition and remediation cards for blocked controlled downgrades. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**

Recommended goals:

- Convert v0.5.2 cause cards into remediation tasks.
- Separate provenance repair, support-aware negative controls, severity stratification, and heuristic calibration.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: remediation planning is local classifier governance only.
""", r, flags=re.S)
write(p,r)

# AGENTS
p=ROOT/"AGENTS.md"; backup(p,"agents"); a=read(p)
a=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**", a)
if "run_over_penalty_cause_decomposition.py" not in a:
    a=a.replace("python scripts/feedback/run_nexus_target_refresh.py\npython -m unittest discover -s tests",
                "python scripts/feedback/run_nexus_target_refresh.py\npython scripts/benchmarks/run_over_penalty_cause_decomposition.py\npython -m unittest discover -s tests")
if "| Over-penalty cause patch |" not in a:
    a=a.replace("| Nexus target refresh patch | `reports/nexus_target_refresh/`, `visuals/nexus_target_refresh/`, Nexus feedback + readiness gate | target-refresh report + release validator; no classifier mutation |\n",
                "| Nexus target refresh patch | `reports/nexus_target_refresh/`, `visuals/nexus_target_refresh/`, Nexus feedback + readiness gate | target-refresh report + release validator; no classifier mutation |\n| Over-penalty cause patch | `reports/over_penalty_causes/`, `visuals/over_penalty_causes/`, readiness gate | cause cards + release validator; no classifier mutation |\n")
write(p,a)

# route map
p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.2"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["over_penalty_cause_decomposition"]={
    "read_first":["reports/enforcement_readiness/latest_enforcement_readiness_gate.json","reports/regression_review/latest_regression_over_penalty_review.json"],
    "validate":["python scripts/benchmarks/run_over_penalty_cause_decomposition.py","python scripts/release/validate_release.py"],
    "evidence":["reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md","reports/over_penalty_causes/cards/v0_5_2/","visuals/over_penalty_causes/v0_5_2/"],
    "mutation_lock":"Does not change classifier behavior; emits cause cards only."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

# task matrix
p=ROOT/"rcc"/"nexus"/"task_routing_matrix.md"; backup(p,"task_matrix"); m=read(p)
m=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition**", m)
if "| Over-penalty cause patch |" not in m:
    m=m.replace("| Nexus target refresh patch | outer | drift | feedback | Nexus feedback + readiness gate | target-refresh report + charts + release validator | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |\n",
                "| Nexus target refresh patch | outer | drift | feedback | Nexus feedback + readiness gate | target-refresh report + charts + release validator | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` |\n| Over-penalty cause patch | outer | validation | governance | readiness gate + regression review | cause cards + charts + release validator | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` |\n")
write(p,m)

# atlas
p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.2 | Over-penalty cause decomposition |" not in t:
    t=t.replace("| v0.5.1 | Nexus target refresh | `python scripts/feedback/run_nexus_target_refresh.py` | Retires completed Nexus targets and promotes the current active blocker | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` | `visuals/nexus_target_refresh/v0_5_1/` |\n",
                "| v0.5.1 | Nexus target refresh | `python scripts/feedback/run_nexus_target_refresh.py` | Retires completed Nexus targets and promotes the current active blocker | `reports/nexus_target_refresh/latest_nexus_target_refresh.md` | `visuals/nexus_target_refresh/v0_5_1/` |\n| v0.5.2 | Over-penalty cause decomposition | `python scripts/benchmarks/run_over_penalty_cause_decomposition.py` | Converts active blocker into cause-specific remediation cards | `reports/over_penalty_causes/latest_over_penalty_cause_decomposition.md` | `visuals/over_penalty_causes/v0_5_2/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_2_over_penalty_cause_decomposition.md", f"""# TAU-SCALING-SA v0.5.2 - Over-Penalty Cause Decomposition

Generated: {NOW}

## Purpose

Convert the active v0.5.1 blocker into cause-specific remediation cards.

## Adds

- `scripts/benchmarks/run_over_penalty_cause_decomposition.py`
- `reports/over_penalty_causes/`
- `reports/over_penalty_causes/cards/v0_5_2/`
- `visuals/over_penalty_causes/v0_5_2/`

## Boundary

Over-penalty cause decomposition is local classifier-governance analysis only. It does not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.2 patch written")
