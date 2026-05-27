
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd()
NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"negative_controls"/"v0_5_4"/"backups"/f"{p.name}_before_v0_5_4_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
runner_b64="CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gY29sbGVjdGlvbnMgaW1wb3J0IENvdW50ZXIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWV6b25lCmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUk9PVCA9IFBhdGgoX19maWxlX18pLnJlc29sdmUoKS5wYXJlbnRzWzJdClBMQU4gPSBST09UIC8gInJlcG9ydHMiIC8gInJlbWVkaWF0aW9uX3BsYW4iIC8gImxhdGVzdF9jYXVzZV9zcGVjaWZpY19yZW1lZGlhdGlvbl9wbGFuLmpzb24iCkNBVVNFUyA9IFJPT1QgLyAicmVwb3J0cyIgLyAib3Zlcl9wZW5hbHR5X2NhdXNlcyIgLyAibGF0ZXN0X292ZXJfcGVuYWx0eV9jYXVzZV9kZWNvbXBvc2l0aW9uLmpzb24iCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAibmVnYXRpdmVfY29udHJvbHMiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAibmVnYXRpdmVfY29udHJvbHMiIC8gInYwXzVfNCIKClNVUFBPUlRfVEhSRVNIT0xEID0gMC43NQoKZGVmIHJqc29uKHApOgogICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIG1ha2VfY29udHJvbCh0YXNrLCBzb3VyY2VfY2FyZCk6CiAgICBkaWFnID0gc291cmNlX2NhcmQuZ2V0KCJjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSIpCiAgICBoaWdoX3N1cHBvcnQgPSBpc2luc3RhbmNlKGRpYWcsIChpbnQsIGZsb2F0KSkgYW5kIGRpYWcgPj0gU1VQUE9SVF9USFJFU0hPTEQKICAgIGhhc19oaWdoX3N1cHBvcnRfY2F1c2UgPSAiaGlnaF9kaWFnbm9zdGljX3N1cHBvcnQiIGluIHNvdXJjZV9jYXJkLmdldCgiY2F1c2VzIiwgW10pCiAgICBzaG91bGRfcmV0YWluID0gaGlnaF9zdXBwb3J0IG9yIGhhc19oaWdoX3N1cHBvcnRfY2F1c2UKCiAgICAjIFJlcG9ydC1vbmx5IG5lZ2F0aXZlIGNvbnRyb2w6CiAgICAjIEEgaGlnaC1zdXBwb3J0IGNhbmRpZGF0ZSBwYXNzZXMgdGhlIGNvbnRyb2wgd2hlbiB0aGUgc3lzdGVtIHJlZnVzZXMgZG93bmdyYWRlL2VuZm9yY2VtZW50LgogICAgb2JzZXJ2ZWRfb3V0Y29tZSA9ICJyZXRhaW5fYmxvY2tlZF9ub19kb3duZ3JhZGUiIGlmIHNob3VsZF9yZXRhaW4gZWxzZSAicmVxdWlyZXNfbWFudWFsX3JldmlldyIKICAgIHBhc3NfY29udHJvbCA9IG9ic2VydmVkX291dGNvbWUgPT0gInJldGFpbl9ibG9ja2VkX25vX2Rvd25ncmFkZSIKCiAgICByZXR1cm4gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctc3VwcG9ydC1hd2FyZS1uZWdhdGl2ZS1jb250cm9sLXYwLjUuNCIsCiAgICAgICAgImNvbnRyb2xfaWQiOiB0YXNrWyJ0YXNrX2lkIl0ucmVwbGFjZSgicmVtZWRpYXRpb24tdGFzayIsICJuZWdhdGl2ZS1jb250cm9sIiksCiAgICAgICAgInNvdXJjZV90YXNrX2lkIjogdGFza1sidGFza19pZCJdLAogICAgICAgICJzb3VyY2VfY2FyZF9pZCI6IHRhc2suZ2V0KCJzb3VyY2VfY2FyZF9pZCIpLAogICAgICAgICJnYXRlX3BhaXIiOiB0YXNrLmdldCgiZ2F0ZV9wYWlyIiksCiAgICAgICAgImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIjogZGlhZywKICAgICAgICAic3VwcG9ydF90aHJlc2hvbGQiOiBTVVBQT1JUX1RIUkVTSE9MRCwKICAgICAgICAiaGlnaF9zdXBwb3J0X2RldGVjdGVkIjogYm9vbChzaG91bGRfcmV0YWluKSwKICAgICAgICAiZXhwZWN0ZWRfc2FmZV9iZWhhdmlvciI6ICJyZXRhaW5faGlnaF9zdXBwb3J0X2Nhc2VfYW5kX2Jsb2NrX2Rvd25ncmFkZSIsCiAgICAgICAgIm9ic2VydmVkX3JlcG9ydF9vbmx5X2JlaGF2aW9yIjogb2JzZXJ2ZWRfb3V0Y29tZSwKICAgICAgICAibmVnYXRpdmVfY29udHJvbF9wYXNzZWQiOiBib29sKHBhc3NfY29udHJvbCksCiAgICAgICAgImNvbnRyb2xfY2xhc3MiOiAic3VwcG9ydF9hd2FyZV9yZXRlbnRpb25fY29udHJvbCIsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgIm5vbl9jbGFpbV9sb2NrIjogIlN1cHBvcnQtYXdhcmUgbmVnYXRpdmUgY29udHJvbHMgYXJlIGxvY2FsIHJlcG9ydC1vbmx5IGNsYXNzaWZpZXItZ292ZXJuYW5jZSB0ZXN0cy4iLAogICAgfQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpKQoKICAgIHBhc3NfY291bnRzID0gc3VtbWFyeVsiY29udHJvbF9wYXNzX2NvdW50cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDcsNCkpCiAgICBwbHQuYmFyKGxpc3QocGFzc19jb3VudHMua2V5cygpKSwgbGlzdChwYXNzX2NvdW50cy52YWx1ZXMoKSkpCiAgICBwbHQueWxhYmVsKCJDb250cm9sIGNvdW50IikKICAgIHBsdC50aXRsZSgiU3VwcG9ydC1Bd2FyZSBOZWdhdGl2ZSBDb250cm9sIE91dGNvbWVzIikKICAgIHNhdmUoInN1cHBvcnRfY29udHJvbF9vdXRjb21lcy5wbmciKQoKICAgIGdhdGVfY291bnRzID0gc3VtbWFyeVsiZ2F0ZV9pbnZvbHZlbWVudF9jb3VudHMiXQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg5LDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVfY291bnRzLmtleXMoKSksIGxpc3QoZ2F0ZV9jb3VudHMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNvbnRyb2wgaW52b2x2ZW1lbnQiKQogICAgcGx0LnRpdGxlKCJTdXBwb3J0IENvbnRyb2wgR2F0ZSBJbnZvbHZlbWVudCIpCiAgICBzYXZlKCJzdXBwb3J0X2NvbnRyb2xfZ2F0ZV9pbnZvbHZlbWVudC5wbmciKQoKICAgIHZhbHVlcyA9IFtjLmdldCgiY3VycmVudF9kaWFnbm9zdGljX2F2ZXJhZ2UiKSBmb3IgYyBpbiBzdW1tYXJ5WyJuZWdhdGl2ZV9jb250cm9scyJdIGlmIGlzaW5zdGFuY2UoYy5nZXQoImN1cnJlbnRfZGlhZ25vc3RpY19hdmVyYWdlIiksIChpbnQsIGZsb2F0KSldCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsNCkpCiAgICBwbHQuYmFyKFtzdHIoaSsxKSBmb3IgaSBpbiByYW5nZShsZW4odmFsdWVzKSldLCB2YWx1ZXMpCiAgICBwbHQuYXhobGluZShTVVBQT1JUX1RIUkVTSE9MRCwgbGluZXN0eWxlPSItLSIpCiAgICBwbHQueGxhYmVsKCJDb250cm9sIikKICAgIHBsdC55bGFiZWwoIkRpYWdub3N0aWMgYXZlcmFnZSIpCiAgICBwbHQudGl0bGUoIkRpYWdub3N0aWMgU3VwcG9ydCB2cyBSZXRlbnRpb24gVGhyZXNob2xkIikKICAgIHNhdmUoInN1cHBvcnRfY29udHJvbF9kaWFnbm9zdGljX3RocmVzaG9sZC5wbmciKQoKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzdW1tYXJ5KToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjUuNCBTdXBwb3J0LUF3YXJlIE5lZ2F0aXZlIENvbnRyb2xzIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gU291cmNlIHJlbWVkaWF0aW9uIHRhc2tzOiBge3N1bW1hcnlbJ3NvdXJjZV9yZW1lZGlhdGlvbl90YXNrX2NvdW50J119YCIsCiAgICAgICAgZiItIE5lZ2F0aXZlIGNvbnRyb2wgY291bnQ6IGB7c3VtbWFyeVsnbmVnYXRpdmVfY29udHJvbF9jb3VudCddfWAiLAogICAgICAgIGYiLSBQYXNzZWQgY29udHJvbHM6IGB7c3VtbWFyeVsncGFzc2VkX2NvbnRyb2xfY291bnQnXX1gIiwKICAgICAgICBmIi0gRmFpbGVkIGNvbnRyb2xzOiBge3N1bW1hcnlbJ2ZhaWxlZF9jb250cm9sX2NvdW50J119YCIsCiAgICAgICAgZiItIEZpbmFsIHJlY29tbWVuZGF0aW9uOiBge3N1bW1hcnlbJ2ZpbmFsX3JlY29tbWVuZGF0aW9uJ119YCIsCiAgICAgICAgZiItIE11dGF0aW9uIGFsbG93ZWQ6IGB7c3VtbWFyeVsnbXV0YXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgIGYiLSBQb2xpY3kgZW5mb3JjZWQ6IGB7c3VtbWFyeVsncG9saWN5X2VuZm9yY2VkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENvbnRyb2wgT3V0Y29tZXMiLAogICAgICAgICIiLAogICAgICAgICJ8IENvbnRyb2wgfCBHYXRlIHBhaXIgfCBEaWFnbm9zdGljIGF2ZXJhZ2UgfCBIaWdoIHN1cHBvcnQgfCBQYXNzZWQgfCBPYnNlcnZlZCBiZWhhdmlvciB8IiwKICAgICAgICAifC0tLXwtLS18LS0tOnwtLS18LS0tfC0tLXwiLAogICAgXQogICAgZm9yIGMgaW4gc3VtbWFyeVsibmVnYXRpdmVfY29udHJvbHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoCiAgICAgICAgICAgIGYifCBge2NbJ2NvbnRyb2xfaWQnXX1gIHwgYHtjWydnYXRlX3BhaXInXX1gIHwgYHtjWydjdXJyZW50X2RpYWdub3N0aWNfYXZlcmFnZSddfWAgfCAiCiAgICAgICAgICAgIGYiYHtjWydoaWdoX3N1cHBvcnRfZGV0ZWN0ZWQnXX1gIHwgYHtjWyduZWdhdGl2ZV9jb250cm9sX3Bhc3NlZCddfWAgfCBge2NbJ29ic2VydmVkX3JlcG9ydF9vbmx5X2JlaGF2aW9yJ119YCB8IgogICAgICAgICkKICAgIGxpbmVzICs9IFsiIiwgIiMjIENoYXJ0cyIsICIiXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICByZWwgPSBvcy5wYXRoLnJlbHBhdGgoUk9PVCAvIHAsIE9VVCkucmVwbGFjZSgiXFwiLCAiLyIpCiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe3JlbH0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBwbGFuID0gcmpzb24oUExBTikKICAgIGNhdXNlcyA9IHJqc29uKENBVVNFUykKICAgIGNhdXNlX2J5X2lkID0ge2NbImNhcmRfaWQiXTogYyBmb3IgYyBpbiBjYXVzZXMuZ2V0KCJjYXVzZV9jYXJkcyIsIFtdKX0KICAgIHRhc2tzID0gW3QgZm9yIHQgaW4gcGxhbi5nZXQoInJlbWVkaWF0aW9uX3Rhc2tzIiwgW10pIGlmIHQuZ2V0KCJyZW1lZGlhdGlvbl9jbGFzcyIpID09ICJzdXBwb3J0X2F3YXJlX25lZ2F0aXZlX2NvbnRyb2wiXQoKICAgIGNvbnRyb2xzID0gW10KICAgIGZvciB0YXNrIGluIHRhc2tzOgogICAgICAgIGNhcmQgPSBjYXVzZV9ieV9pZC5nZXQodGFzay5nZXQoInNvdXJjZV9jYXJkX2lkIiksIHt9KQogICAgICAgIGNvbnRyb2xzLmFwcGVuZChtYWtlX2NvbnRyb2wodGFzaywgY2FyZCkpCgogICAgcGFzc19jb3VudGVyID0gQ291bnRlcigicGFzc2VkIiBpZiBjWyJuZWdhdGl2ZV9jb250cm9sX3Bhc3NlZCJdIGVsc2UgImZhaWxlZCIgZm9yIGMgaW4gY29udHJvbHMpCiAgICBnYXRlcyA9IENvdW50ZXIoKQogICAgZm9yIGMgaW4gY29udHJvbHM6CiAgICAgICAgZm9yIGcgaW4gc3RyKGMuZ2V0KCJnYXRlX3BhaXIiKSkuc3BsaXQoIisiKToKICAgICAgICAgICAgaWYgZyBhbmQgZyAhPSAiTm9uZSI6CiAgICAgICAgICAgICAgICBnYXRlc1tnXSArPSAxCgogICAgZmFpbGVkID0gcGFzc19jb3VudGVyLmdldCgiZmFpbGVkIiwgMCkKICAgIGZpbmFsID0gInJldGFpbl9ibG9ja19fc3VwcG9ydF9jb250cm9sc19jb25maXJtX2hpZ2hfc3VwcG9ydF9yZXRlbnRpb24iIGlmIGZhaWxlZCA9PSAwIGVsc2UgInJldmlld19mYWlsZWRfc3VwcG9ydF9jb250cm9sc19iZWZvcmVfY2FsaWJyYXRpb24iCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXN1cHBvcnQtYXdhcmUtbmVnYXRpdmUtY29udHJvbHMtdjAuNS40IiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgImlucHV0X3BsYW4iOiAicmVwb3J0cy9yZW1lZGlhdGlvbl9wbGFuL2xhdGVzdF9jYXVzZV9zcGVjaWZpY19yZW1lZGlhdGlvbl9wbGFuLmpzb24iLAogICAgICAgICJpbnB1dF9jYXVzZXMiOiAicmVwb3J0cy9vdmVyX3BlbmFsdHlfY2F1c2VzL2xhdGVzdF9vdmVyX3BlbmFsdHlfY2F1c2VfZGVjb21wb3NpdGlvbi5qc29uIiwKICAgICAgICAic291cmNlX3JlbWVkaWF0aW9uX3Rhc2tfY291bnQiOiBsZW4odGFza3MpLAogICAgICAgICJuZWdhdGl2ZV9jb250cm9sX2NvdW50IjogbGVuKGNvbnRyb2xzKSwKICAgICAgICAicGFzc2VkX2NvbnRyb2xfY291bnQiOiBwYXNzX2NvdW50ZXIuZ2V0KCJwYXNzZWQiLCAwKSwKICAgICAgICAiZmFpbGVkX2NvbnRyb2xfY291bnQiOiBmYWlsZWQsCiAgICAgICAgImNvbnRyb2xfcGFzc19jb3VudHMiOiBkaWN0KHBhc3NfY291bnRlciksCiAgICAgICAgImdhdGVfaW52b2x2ZW1lbnRfY291bnRzIjogZGljdChnYXRlcyksCiAgICAgICAgIm5lZ2F0aXZlX2NvbnRyb2xzIjogY29udHJvbHMsCiAgICAgICAgInN1cHBvcnRfdGhyZXNob2xkIjogU1VQUE9SVF9USFJFU0hPTEQsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImZpbmFsX3JlY29tbWVuZGF0aW9uIjogZmluYWwsCiAgICAgICAgImJvdW5kYXJ5IjogIlN1cHBvcnQtYXdhcmUgbmVnYXRpdmUgY29udHJvbHMgYXJlIGRpc2FibGVkL3JlcG9ydC1vbmx5IGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSB0ZXN0cy4gVGhleSBkbyBub3QgY2hhbmdlIGNsYXNzaWZpZXIgYmVoYXZpb3IgYW5kIGRvIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAidjAuNS41IHNob3VsZCBjcmVhdGUgYSBkaXNhYmxlZCBjYWxpYnJhdGlvbiBwbGFuIG9ubHkgaWYgc3VwcG9ydC1hd2FyZSBjb250cm9scyBwYXNzLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAic3VwcG9ydF9hd2FyZV9uZWdhdGl2ZV9jb250cm9sc192MF81XzQuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X3N1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAic3VwcG9ydF9hd2FyZV9uZWdhdGl2ZV9jb250cm9sc192MF81XzQubWQiLCByZXBvcnQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3N1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMubWQiLCByZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJzb3VyY2VfcmVtZWRpYXRpb25fdGFza19jb3VudCI6IHN1bW1hcnlbInNvdXJjZV9yZW1lZGlhdGlvbl90YXNrX2NvdW50Il0sCiAgICAgICAgIm5lZ2F0aXZlX2NvbnRyb2xfY291bnQiOiBzdW1tYXJ5WyJuZWdhdGl2ZV9jb250cm9sX2NvdW50Il0sCiAgICAgICAgInBhc3NlZF9jb250cm9sX2NvdW50Ijogc3VtbWFyeVsicGFzc2VkX2NvbnRyb2xfY291bnQiXSwKICAgICAgICAiZmFpbGVkX2NvbnRyb2xfY291bnQiOiBzdW1tYXJ5WyJmYWlsZWRfY29udHJvbF9jb3VudCJdLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6IHN1bW1hcnlbImZpbmFsX3JlY29tbWVuZGF0aW9uIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IHN1bW1hcnlbInBvbGljeV9lbmZvcmNlZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvbmVnYXRpdmVfY29udHJvbHMvbGF0ZXN0X3N1cHBvcnRfYXdhcmVfbmVnYXRpdmVfY29udHJvbHMubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK"
write(ROOT/"scripts"/"benchmarks"/"run_support_aware_negative_controls.py", base64.b64decode(runner_b64).decode())

write(ROOT/"reports"/"negative_controls"/"README.md", """# Support-Aware Negative Control Reports

Current layer: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**

## Purpose

This folder stores disabled/report-only negative-control tests for high-support blocked downgrade candidates.

## Primary command

```powershell
python scripts/benchmarks/run_support_aware_negative_controls.py
```

## README Update Rule

Update this mini README whenever negative-control schemas, report paths, or support thresholds change.

Boundary: negative controls are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"negative_controls"/"README.md", """# Support-Aware Negative Control Visuals

Current layer: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**

## Purpose

This folder stores charts summarizing support-aware negative-control outcomes.

## README Update Rule

Update this mini README whenever negative-control chart names or meanings change.

Boundary: negative-control visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"negative_controls"/"v0_5_4"/"README.md", """# v0.5.4 Support-Aware Negative-Control Charts

Expected charts:

- `support_control_outcomes.png`
- `support_control_gate_involvement.png`
- `support_control_diagnostic_threshold.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local support-control diagnostics only.
""")

# README
p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.5\.3[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.5\.2[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.5.3 - Cause-Specific Remediation Plan**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.5\.3 \|", "| Current checkpoint | TAU-SCALING-SA v0.5.4 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.5.3-ready |", "| Task routing matrix | geometry-aware / v0.5.4-ready |")
r=r.replace("| Agent contract version sync | current / v0.5.3 |", "| Agent contract version sync | current / v0.5.4 |")
if "| Support-aware negative controls |" not in r:
    r=r.replace("| Remediation plan charts | `visuals/remediation_plan/v0_5_3/` |\n",
                "| Remediation plan charts | `visuals/remediation_plan/v0_5_3/` |\n| Support-aware negative controls | `reports/negative_controls/latest_support_aware_negative_controls.md` |\n| Support-aware control charts | `visuals/negative_controls/v0_5_4/` |\n")
if "python scripts/benchmarks/run_support_aware_negative_controls.py" not in r:
    r=r.replace("python scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython scripts/benchmarks/run_support_aware_negative_controls.py\npython scripts/release/validate_release.py")
if "    negative_controls/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    negative_controls/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    negative_controls/\n")
section="""## Support-Aware Negative Controls v0.5.4

v0.5.4 converts v0.5.3 support-aware remediation tasks into disabled/report-only negative-control tests.

Primary command:

```powershell
python scripts/benchmarks/run_support_aware_negative_controls.py
```

Primary outputs:

```text
reports/negative_controls/latest_support_aware_negative_controls.json
reports/negative_controls/latest_support_aware_negative_controls.md
visuals/negative_controls/v0_5_4/
```

This layer checks whether high-support cases are safely retained and blocked from downgrade pressure before any calibration plan is considered.

Current lock:

```text
mutation_allowed: false
policy_enforced: false
```

Boundary: support-aware negative controls are local classifier-governance diagnostics only. They do not change classifier behavior and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Support-Aware Negative Controls v0.5.4" not in r:
    r=r.replace("## Cause-Specific Remediation Plan v0.5.3", section+"## Cause-Specific Remediation Plan v0.5.3",1)
lesson="| L-036 | v0.5.3 converted all six blocked cases into support-aware negative-control tasks. | Remediation planning is not enough; high-support retention must be tested as a disabled/report-only control. | Before calibration or policy design, high-support downgrade pressure must pass support-aware negative controls with mutation disabled. |"
if "L-036" not in r:
    r=r.replace("| L-035 | v0.5.2 showed all blocked candidates were high-support / heuristic-sensitivity cases. | Cause cards identify why a blocker exists, but do not define the next safe work unit. | High-support downgrade pressure must become support-aware negative-control tasks before calibration or policy design. |\n",
                "| L-035 | v0.5.2 showed all blocked candidates were high-support / heuristic-sensitivity cases. | Cause cards identify why a blocker exists, but do not define the next safe work unit. | High-support downgrade pressure must become support-aware negative-control tasks before calibration or policy design. |\n"+lesson+"\n")
if "| v0.5.4 |" not in r:
    r=r.replace("| v0.5.3 | Cause-specific remediation plan for high-support blocked downgrade candidates. |\n",
                "| v0.5.3 | Cause-specific remediation plan for high-support blocked downgrade candidates. |\n| v0.5.4 | Support-aware negative controls for high-support blocked downgrade candidates. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.5.5 - Disabled Calibration Plan**

Recommended goals:

- Build a report-only calibration plan only after support-aware negative controls pass.
- Compare proposed thresholds against high-support retention constraints.
- Keep `mutation_allowed: false`.
- Preserve non-claim locks: calibration planning is local classifier governance only.
""", r, flags=re.S)
write(p,r)

# AGENTS
p=ROOT/"AGENTS.md"; backup(p,"agents"); a=read(p)
a=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**", a)
if "run_support_aware_negative_controls.py" not in a:
    a=a.replace("python scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython -m unittest discover -s tests",
                "python scripts/benchmarks/generate_cause_specific_remediation_plan.py\npython scripts/benchmarks/run_support_aware_negative_controls.py\npython -m unittest discover -s tests")
if "| Support-aware negative-control patch |" not in a:
    a=a.replace("| Remediation plan patch | `reports/remediation_plan/`, `visuals/remediation_plan/`, cause cards | remediation tasks + release validator; no classifier mutation |\n",
                "| Remediation plan patch | `reports/remediation_plan/`, `visuals/remediation_plan/`, cause cards | remediation tasks + release validator; no classifier mutation |\n| Support-aware negative-control patch | `reports/negative_controls/`, `visuals/negative_controls/`, remediation tasks | negative-control report + release validator; no classifier mutation |\n")
write(p,a)

# route map
p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.5.4"; route["updated_at"]=NOW
route.setdefault("v0_5_routes",{})["support_aware_negative_controls"]={
    "read_first":["reports/remediation_plan/latest_cause_specific_remediation_plan.json","reports/over_penalty_causes/latest_over_penalty_cause_decomposition.json"],
    "validate":["python scripts/benchmarks/run_support_aware_negative_controls.py","python scripts/release/validate_release.py"],
    "evidence":["reports/negative_controls/latest_support_aware_negative_controls.md","visuals/negative_controls/v0_5_4/"],
    "mutation_lock":"Does not change classifier behavior; emits disabled/report-only negative controls."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

# task matrix
p=ROOT/"rcc"/"nexus"/"task_routing_matrix.md"; backup(p,"task_matrix"); m=read(p)
m=re.sub(r"Current contract: \*\*TAU-SCALING-SA v0\.5\.3[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls**", m)
if "| Support-aware negative-control patch |" not in m:
    m=m.replace("| Remediation plan patch | outer | validation | governance | cause cards + remediation tasks | remediation report + charts + release validator | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` |\n",
                "| Remediation plan patch | outer | validation | governance | cause cards + remediation tasks | remediation report + charts + release validator | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` |\n| Support-aware negative-control patch | outer | validation | governance | remediation tasks + cause cards | negative-control report + charts + release validator | `reports/negative_controls/latest_support_aware_negative_controls.md` |\n")
write(p,m)

# atlas
p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.5.4 | Support-aware negative controls |" not in t:
    t=t.replace("| v0.5.3 | Cause-specific remediation plan | `python scripts/benchmarks/generate_cause_specific_remediation_plan.py` | Converts cause cards into non-mutating remediation tasks | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` | `visuals/remediation_plan/v0_5_3/` |\n",
                "| v0.5.3 | Cause-specific remediation plan | `python scripts/benchmarks/generate_cause_specific_remediation_plan.py` | Converts cause cards into non-mutating remediation tasks | `reports/remediation_plan/latest_cause_specific_remediation_plan.md` | `visuals/remediation_plan/v0_5_3/` |\n| v0.5.4 | Support-aware negative controls | `python scripts/benchmarks/run_support_aware_negative_controls.py` | Tests high-support retention before calibration or policy design | `reports/negative_controls/latest_support_aware_negative_controls.md` | `visuals/negative_controls/v0_5_4/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_5_4_support_aware_negative_controls.md", f"""# TAU-SCALING-SA v0.5.4 - Support-Aware Negative Controls

Generated: {NOW}

## Purpose

Convert v0.5.3 support-aware remediation tasks into disabled/report-only negative-control tests.

## Adds

- `scripts/benchmarks/run_support_aware_negative_controls.py`
- `reports/negative_controls/`
- `visuals/negative_controls/v0_5_4/`

## Boundary

Support-aware negative controls are local classifier-governance diagnostics only. They do not validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.5.4 patch written")
