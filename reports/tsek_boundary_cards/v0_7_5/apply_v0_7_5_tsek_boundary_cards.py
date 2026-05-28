
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
        d = ROOT / "reports" / "tsek_boundary_cards" / "v0_7_5" / "backups" / f"{p.name}_before_v0_7_5_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_tsek_boundary_explanation_cards.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfYm91bmRhcnlfY2FyZHMiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAidHNla19ib3VuZGFyeV9jYXJkcyIgLyAidjBfN181IgoKVEhSRVNIT0xEX1JFVklFVyA9IFJPT1QgLyAicmVwb3J0cyIgLyAidHNla190aHJlc2hvbGRfcmV2aWV3IiAvICJsYXRlc3RfdHNla190aHJlc2hvbGRfYm91bmRhcnlfcmV2aWV3Lmpzb24iCkdBVEVfQUxHRUJSQSA9IFJPT1QgLyAicmVwb3J0cyIgLyAiZ2F0ZV9hbGdlYnJhIiAvICJsYXRlc3RfZ2F0ZV9hbGdlYnJhX21hcC5qc29uIgpUQVVfVkVDVE9SID0gUk9PVCAvICJyZXBvcnRzIiAvICJ0YXVfdmVjdG9yX3NlbWFudGljcyIgLyAibGF0ZXN0X3RhdV92ZWN0b3Jfc2VtYW50aWNzX2xlZGdlci5qc29uIgpSRUxFQVNFID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIKCkNMQVNTRVMgPSBbCiAgICB7CiAgICAgICAgImNsYXNzIjogIlRTRUstQSIsCiAgICAgICAgInJvbGUiOiAicmVzZXJ2ZWRfc3Ryb25nX2NsYWltX2NsYXNzIiwKICAgICAgICAiYm91bmRhcnlfcXVlc3Rpb24iOiAiV2hhdCB3b3VsZCBiZSByZXF1aXJlZCBmb3IgYSBzdHJvbmcgVGF1IGNsYWltIGJleW9uZCBsb2NhbCBydW50aW1lIGV2aWRlbmNlPyIsCiAgICAgICAgImRlZmF1bHRfYWN0aW9uIjogImtlZXBfdW5hc3NpZ25lZF93aXRob3V0X2V4dGVybmFsX2V2aWRlbmNlIiwKICAgICAgICAicmlzayI6ICJvdmVyY2xhaW1fcmlzayIsCiAgICB9LAogICAgewogICAgICAgICJjbGFzcyI6ICJUU0VLLUIiLAogICAgICAgICJyb2xlIjogInN0cm9uZ2VyX2xvY2FsX2V2aWRlbmNlX2NsYXNzIiwKICAgICAgICAiYm91bmRhcnlfcXVlc3Rpb24iOiAiRG9lcyB0aGUgY2xhaW0gc2hvdyBjb2hlcmVudCBsb2NhbCBldmlkZW5jZSB3aGlsZSBwcmVzZXJ2aW5nIG5vbi1jbGFpbSBsb2Nrcz8iLAogICAgICAgICJkZWZhdWx0X2FjdGlvbiI6ICJhbGxvd19sb2NhbF9zdHJvbmdfZXZpZGVuY2VfbGFiZWxfb25seSIsCiAgICAgICAgInJpc2siOiAicHJvbW90aW9uX3dpdGhvdXRfc2NvcGVfYm91bmRhcnkiLAogICAgfSwKICAgIHsKICAgICAgICAiY2xhc3MiOiAiVFNFSy1DIiwKICAgICAgICAicm9sZSI6ICJib3VuZGVkX2Jhc2VsaW5lX29yX3BhcnRpYWxfZXZpZGVuY2VfY2xhc3MiLAogICAgICAgICJib3VuZGFyeV9xdWVzdGlvbiI6ICJEb2VzIHRoZSBjbGFpbSBoYXZlIGVub3VnaCBzdHJ1Y3R1cmUgZm9yIGxvY2FsIGFuYWx5c2lzIGJ1dCBpbnN1ZmZpY2llbnQgZXZpZGVuY2UgZm9yIHN0cm9uZ2VyIHByb21vdGlvbj8iLAogICAgICAgICJkZWZhdWx0X2FjdGlvbiI6ICJwcmVzZXJ2ZV9jb250cm9sbGVkX2Rvd25ncmFkZSIsCiAgICAgICAgInJpc2siOiAidW5kZXJfZXhwbGFpbmVkX3BhcnRpYWxfZXZpZGVuY2UiLAogICAgfSwKICAgIHsKICAgICAgICAiY2xhc3MiOiAiVFNFSy1EIiwKICAgICAgICAicm9sZSI6ICJ3ZWFrX29yX2hpZ2hfdW5jZXJ0YWludHlfY2xhc3MiLAogICAgICAgICJib3VuZGFyeV9xdWVzdGlvbiI6ICJJcyB0aGUgY2xhaW0gc3RydWN0dXJhbGx5IHByZXNlbnQgYnV0IHRvbyB3ZWFrLCBzcGFyc2UsIG9yIHVuc3RhYmxlIGZvciBDL0I/IiwKICAgICAgICAiZGVmYXVsdF9hY3Rpb24iOiAiZXhwbGFpbl93ZWFrbmVzc193aXRob3V0X3JlamVjdGlvbiIsCiAgICAgICAgInJpc2siOiAibWlzc2luZ19pbnRlcm1lZGlhdGVfZG93bmdyYWRlX3BhdGgiLAogICAgfSwKICAgIHsKICAgICAgICAiY2xhc3MiOiAiVFNFSy1FIiwKICAgICAgICAicm9sZSI6ICJyZWplY3RlZF9vcl9zZXZlcmVfZmFpbHVyZV9jbGFzcyIsCiAgICAgICAgImJvdW5kYXJ5X3F1ZXN0aW9uIjogIkRvZXMgdGhlIGNsYWltIGZhaWwgaGFyZCBnYXRlcywgZXZpZGVuY2Ugc3VmZmljaWVuY3ksIG9yIG5vbi1jbGFpbSBkaXNjaXBsaW5lPyIsCiAgICAgICAgImRlZmF1bHRfYWN0aW9uIjogInJlamVjdF9vcl9ibG9ja19wcm9tb3Rpb24iLAogICAgICAgICJyaXNrIjogIm92ZXJfcGVuYWx0eV9pZl9oaWdoX3N1cHBvcnRfY2xhaW1faXNfcmVqZWN0ZWQiLAogICAgfSwKXQoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiB7Im1pc3NpbmciOiBUcnVlLCAicGF0aCI6IHN0cihwYXRoKX0KICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHJldHVybiB7InBhcnNlX2Vycm9yIjogc3RyKGV4YyksICJwYXRoIjogc3RyKHBhdGgpfQoKZGVmIHdqc29uKHBhdGg6IFBhdGgsIGRhdGEpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMoZGF0YSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwYXRoOiBQYXRoKToKICAgIHJldHVybiBzdHIocGF0aC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgbWFrZV9jYXJkcyh0aHJlc2hvbGQsIGdhdGUsIHRhdSk6CiAgICByZXZpZXdfY291bnRzID0gdGhyZXNob2xkLmdldCgicmVwb3J0X3RzZWtfY2xhc3NfY291bnRzIiwge30pIG9yIHt9CiAgICBjb3JlX2NvdW50cyA9IHRocmVzaG9sZC5nZXQoImNvcmVfdHNla19jbGFzc19jb3VudHMiLCB7fSkgb3Ige30KICAgIGdhdGVfZ2FwX2NvdW50ID0gZ2F0ZS5nZXQoImdhcF9jb3VudCIsIDApCiAgICB0YXVfZ2FwX2NvdW50ID0gdGF1LmdldCgiZ2FwX2NvdW50IiwgMCkKCiAgICBjYXJkcyA9IFtdCiAgICBmb3IgaXRlbSBpbiBDTEFTU0VTOgogICAgICAgIGNscyA9IGl0ZW1bImNsYXNzIl0KICAgICAgICBvYnNlcnZlZF9yZXBvcnRfbWVudGlvbnMgPSBpbnQocmV2aWV3X2NvdW50cy5nZXQoY2xzLCAwKSkKICAgICAgICBvYnNlcnZlZF9jb3JlX21lbnRpb25zID0gaW50KGNvcmVfY291bnRzLmdldChjbHMsIDApKQogICAgICAgIG5lZWRzX2F0dGVudGlvbiA9ICgKICAgICAgICAgICAgb2JzZXJ2ZWRfcmVwb3J0X21lbnRpb25zID09IDAKICAgICAgICAgICAgb3Igb2JzZXJ2ZWRfY29yZV9tZW50aW9ucyA9PSAwCiAgICAgICAgICAgIG9yIChjbHMgPT0gIlRTRUstRCIgYW5kIG9ic2VydmVkX3JlcG9ydF9tZW50aW9ucyA9PSAwKQogICAgICAgICAgICBvciAoY2xzID09ICJUU0VLLUEiIGFuZCBvYnNlcnZlZF9yZXBvcnRfbWVudGlvbnMgPT0gMCkKICAgICAgICApCiAgICAgICAgY2FyZHMuYXBwZW5kKHsKICAgICAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy10c2VrLWJvdW5kYXJ5LWV4cGxhbmF0aW9uLWNhcmQtdjAuNy41IiwKICAgICAgICAgICAgImNsYXNzIjogY2xzLAogICAgICAgICAgICAicm9sZSI6IGl0ZW1bInJvbGUiXSwKICAgICAgICAgICAgImJvdW5kYXJ5X3F1ZXN0aW9uIjogaXRlbVsiYm91bmRhcnlfcXVlc3Rpb24iXSwKICAgICAgICAgICAgImRlZmF1bHRfYWN0aW9uIjogaXRlbVsiZGVmYXVsdF9hY3Rpb24iXSwKICAgICAgICAgICAgInJpc2siOiBpdGVtWyJyaXNrIl0sCiAgICAgICAgICAgICJvYnNlcnZlZF9yZXBvcnRfbWVudGlvbnMiOiBvYnNlcnZlZF9yZXBvcnRfbWVudGlvbnMsCiAgICAgICAgICAgICJvYnNlcnZlZF9jb3JlX21lbnRpb25zIjogb2JzZXJ2ZWRfY29yZV9tZW50aW9ucywKICAgICAgICAgICAgImdhdGVfZ2FwX2NvdW50X2NvbnRleHQiOiBnYXRlX2dhcF9jb3VudCwKICAgICAgICAgICAgInRhdV9nYXBfY291bnRfY29udGV4dCI6IHRhdV9nYXBfY291bnQsCiAgICAgICAgICAgICJuZWVkc19hdHRlbnRpb24iOiBib29sKG5lZWRzX2F0dGVudGlvbiksCiAgICAgICAgICAgICJ0aHJlc2hvbGRfY2hhbmdlX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAgICAgImNsYXNzaWZpZXJfY2hhbmdlX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAgICAgImV2aWRlbmNlX25vdGUiOiAiVGhpcyBjYXJkIGV4cGxhaW5zIGEgY2xhc3MgYm91bmRhcnkgdXNpbmcgbG9jYWwgcmVwbyBldmlkZW5jZSBvbmx5LiBJdCBkb2VzIG5vdCB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0IHBlcmZvcm1hbmNlLCBtYW51ZmFjdHVyaW5nLCBwcm9jZXNzIG5vZGVzLCBiZW5jaG1hcmsgc3VwZXJpb3JpdHksIG9yIHVuaXZlcnNhbCBUYXUgU2NhbGluZyBsYXcuIiwKICAgICAgICB9KQogICAgcmV0dXJuIGNhcmRzCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGV4YykpCiAgICAgICAgcmV0dXJuIHBhdGhzCgogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIGNhcmRzID0gc3VtbWFyeVsiY2FyZHMiXQogICAgbGFiZWxzID0gW2NbImNsYXNzIl0gZm9yIGMgaW4gY2FyZHNdCgogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGFiZWxzLCBbY1sib2JzZXJ2ZWRfcmVwb3J0X21lbnRpb25zIl0gZm9yIGMgaW4gY2FyZHNdKQogICAgcGx0LnlsYWJlbCgiUmVwb3J0IG1lbnRpb25zIikKICAgIHBsdC50aXRsZSgiVFNFSyBCb3VuZGFyeSBDYXJkIFJlcG9ydCBWaXNpYmlsaXR5IikKICAgIHNhdmUoInRzZWtfYm91bmRhcnlfcmVwb3J0X3Zpc2liaWxpdHkucG5nIikKCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsYWJlbHMsIFtpbnQoY1sibmVlZHNfYXR0ZW50aW9uIl0pIGZvciBjIGluIGNhcmRzXSkKICAgIHBsdC55bGFiZWwoIk5lZWRzIGF0dGVudGlvbiIpCiAgICBwbHQudGl0bGUoIlRTRUsgQm91bmRhcnkgQXR0ZW50aW9uIEZsYWdzIikKICAgIHNhdmUoInRzZWtfYm91bmRhcnlfYXR0ZW50aW9uX2ZsYWdzLnBuZyIpCgogICAgaGVhbHRoID0gewogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IGludChzdW1tYXJ5WyJyZWxlYXNlX3Bhc3NlZCJdKSwKICAgICAgICAidGhyZXNob2xkX3JlYWR5IjogaW50KHN1bW1hcnlbInRocmVzaG9sZF9yZWFkeSJdKSwKICAgICAgICAiYXR0ZW50aW9uX2NhcmRzIjogc3VtbWFyeVsiYXR0ZW50aW9uX2NhcmRfY291bnQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgiVFNFSyBCb3VuZGFyeSBDYXJkcyBIZWFsdGgiKQogICAgc2F2ZSgidHNla19ib3VuZGFyeV9jYXJkc19oZWFsdGgucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjUgVFNFSyBCb3VuZGFyeSBFeHBsYW5hdGlvbiBDYXJkcyIsCiAgICAgICAgIiIsCiAgICAgICAgZiJHZW5lcmF0ZWQ6IGB7c3VtbWFyeVsnZ2VuZXJhdGVkX2F0J119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENhcmQgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gQ2FyZCBzdGF0dXM6IGB7c3VtbWFyeVsnY2FyZF9zdGF0dXMnXX1gIiwKICAgICAgICBmIi0gUmVsZWFzZSBwYXNzZWQ6IGB7c3VtbWFyeVsncmVsZWFzZV9wYXNzZWQnXX1gIiwKICAgICAgICBmIi0gVGhyZXNob2xkIHJldmlldyByZWFkeTogYHtzdW1tYXJ5Wyd0aHJlc2hvbGRfcmVhZHknXX1gIiwKICAgICAgICBmIi0gQ2FyZCBjb3VudDogYHtzdW1tYXJ5WydjYXJkX2NvdW50J119YCIsCiAgICAgICAgZiItIEF0dGVudGlvbiBjYXJkczogYHtzdW1tYXJ5WydhdHRlbnRpb25fY2FyZF9jb3VudCddfWAiLAogICAgICAgIGYiLSBUaHJlc2hvbGRzIGNoYW5nZWQ6IGB7c3VtbWFyeVsndGhyZXNob2xkc19jaGFuZ2VkJ119YCIsCiAgICAgICAgZiItIENsYXNzaWZpZXIgY2hhbmdlZDogYHtzdW1tYXJ5WydjbGFzc2lmaWVyX2NoYW5nZWQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQm91bmRhcnkgQ2FyZHMiLAogICAgICAgICIiLAogICAgICAgICJ8IENsYXNzIHwgUm9sZSB8IFJlcG9ydCBtZW50aW9ucyB8IENvcmUgbWVudGlvbnMgfCBOZWVkcyBhdHRlbnRpb24gfCBEZWZhdWx0IGFjdGlvbiB8IiwKICAgICAgICAifC0tLXwtLS18LS0tOnwtLS06fC0tLTp8LS0tfCIsCiAgICBdCiAgICBmb3IgYyBpbiBzdW1tYXJ5WyJjYXJkcyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtjWydjbGFzcyddfWAgfCBge2NbJ3JvbGUnXX1gIHwge2NbJ29ic2VydmVkX3JlcG9ydF9tZW50aW9ucyddfSB8IHtjWydvYnNlcnZlZF9jb3JlX21lbnRpb25zJ119IHwgYHtjWyduZWVkc19hdHRlbnRpb24nXX1gIHwgYHtjWydkZWZhdWx0X2FjdGlvbiddfWAgfCIpCgogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBJbnRlcnByZXRhdGlvbiIsCiAgICAgICAgIiIsCiAgICAgICAgIlRoZXNlIGNhcmRzIGV4cGxhaW4gY2xhc3MgYm91bmRhcmllcy4gVGhleSBkbyBub3QgdHVuZSB0aHJlc2hvbGRzLCBhbHRlciBkb3duZ3JhZGUgcG9saWN5LCBvciBtdXRhdGUgdGhlIGNsYXNzaWZpZXIuIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgTmV4dCBUYXUgV29yayIsCiAgICAgICAgIiIsCiAgICAgICAgIjEuIEJ1aWxkIG92ZXIvdW5kZXItcGVuYWx0eSBuZWdhdGl2ZSBjb250cm9scyBmb3IgdGhlIGNsYXNzIGJvdW5kYXJpZXMgZmxhZ2dlZCBoZXJlLiIsCiAgICAgICAgIjIuIEVuc3VyZSBUU0VLLUQgYW5kIFRTRUstQSBhYnNlbmNlL3ByZXNlbmNlIGlzIGludGVudGlvbmFsIHJhdGhlciB0aGFuIGFjY2lkZW50YWwuIiwKICAgICAgICAiMy4gU2VwYXJhdGUgZXZpZGVuY2Ugc3VmZmljaWVuY3kgZnJvbSBoYXJkLWdhdGUgY29sbGFwc2UgaW4gZXhwbGFuYXRpb24gbGFuZ3VhZ2UuIiwKICAgICAgICAiNC4gS2VlcCB0aHJlc2hvbGRzIHVuY2hhbmdlZCB1bnRpbCBkcnktcnVuIHNlbnNpdGl2aXR5IGV2aWRlbmNlIGV4aXN0cy4iLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICB0aHJlc2hvbGQgPSByZWFkX2pzb24oVEhSRVNIT0xEX1JFVklFVykKICAgIGdhdGUgPSByZWFkX2pzb24oR0FURV9BTEdFQlJBKQogICAgdGF1ID0gcmVhZF9qc29uKFRBVV9WRUNUT1IpCiAgICByZWxlYXNlID0gcmVhZF9qc29uKFJFTEVBU0UpCgogICAgcmVsZWFzZV9wYXNzZWQgPSByZWxlYXNlLmdldCgicGFzc2VkIikgaXMgVHJ1ZSBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJmaW5kaW5ncyIsIFtdKSkgPT0gMCBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJzdGVwX2ZhaWx1cmVzIiwgW10pKSA9PSAwCiAgICB0aHJlc2hvbGRfcmVhZHkgPSB0aHJlc2hvbGQuZ2V0KCJ0aHJlc2hvbGRfcmV2aWV3X3N0YXR1cyIpID09ICJUU0VLX1RIUkVTSE9MRF9CT1VOREFSWV9SRVZJRVdfUkVBRFlfX05PX1RIUkVTSE9MRF9DSEFOR0UiCgogICAgY2FyZHMgPSBtYWtlX2NhcmRzKHRocmVzaG9sZCwgZ2F0ZSwgdGF1KQogICAgZm9yIGNhcmQgaW4gY2FyZHM6CiAgICAgICAgd2pzb24oT1VUIC8gImNhcmRzIiAvIGYie2NhcmRbJ2NsYXNzJ10ubG93ZXIoKS5yZXBsYWNlKCctJywgJ18nKX1fYm91bmRhcnlfY2FyZF92MF83XzUuanNvbiIsIGNhcmQpCgogICAgYXR0ZW50aW9uX2NvdW50ID0gc3VtKDEgZm9yIGMgaW4gY2FyZHMgaWYgY1sibmVlZHNfYXR0ZW50aW9uIl0pCiAgICBjYXJkX3N0YXR1cyA9ICJUU0VLX0JPVU5EQVJZX0NBUkRTX1JFQURZX19OT19USFJFU0hPTERfQ0hBTkdFIiBpZiByZWxlYXNlX3Bhc3NlZCBhbmQgdGhyZXNob2xkX3JlYWR5IGVsc2UgIlRTRUtfQk9VTkRBUllfQ0FSRFNfTkVFRF9SRVZJRVciCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXRzZWstYm91bmRhcnktZXhwbGFuYXRpb24tY2FyZHMtdjAuNy41IiwKICAgICAgICAiZ2VuZXJhdGVkX2F0IjogZGF0ZXRpbWUubm93KHRpbWV6b25lLnV0YykuaXNvZm9ybWF0KCksCiAgICAgICAgImNhcmRfc3RhdHVzIjogY2FyZF9zdGF0dXMsCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogYm9vbChyZWxlYXNlX3Bhc3NlZCksCiAgICAgICAgInRocmVzaG9sZF9yZWFkeSI6IGJvb2wodGhyZXNob2xkX3JlYWR5KSwKICAgICAgICAiY2FyZF9jb3VudCI6IGxlbihjYXJkcyksCiAgICAgICAgImF0dGVudGlvbl9jYXJkX2NvdW50IjogYXR0ZW50aW9uX2NvdW50LAogICAgICAgICJjYXJkcyI6IGNhcmRzLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJ0aHJlc2hvbGRzX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAiTW92ZSB0byB2MC43LjYgT3Zlci9VbmRlci1QZW5hbHR5IE5lZ2F0aXZlIENvbnRyb2xzIGJlZm9yZSBhbnkgdGhyZXNob2xkIGRyeS1ydW4gb3IgdHVuaW5nLiIsCiAgICAgICAgImJvdW5kYXJ5IjogIlRTRUsgYm91bmRhcnkgZXhwbGFuYXRpb24gY2FyZHMgYXJlIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSBhbmFseXNpcyBhcnRpZmFjdHMuIFRoZXkgZXhwbGFpbiBjbGFzcy1ib3VuZGFyeSBzZW1hbnRpY3Mgd2l0aG91dCBjaGFuZ2luZyBjbGFzc2lmaWVyIGJlaGF2aW9yLiBUaGV5IGRvIG5vdCBjcmVhdGUgbGl2ZSBhcHByb3ZhbCwgZXhlY3V0ZSByZXBsYXkgY29tbWFuZHMsIGNyZWF0ZSBicmFuY2hlcywgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFwcGx5IGNhbGlicmF0aW9uLCBvciB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gInRzZWtfYm91bmRhcnlfZXhwbGFuYXRpb25fY2FyZHNfdjBfN181Lmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF90c2VrX2JvdW5kYXJ5X2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gInRzZWtfYm91bmRhcnlfZXhwbGFuYXRpb25fY2FyZHNfdjBfN181Lm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3RfdHNla19ib3VuZGFyeV9leHBsYW5hdGlvbl9jYXJkcy5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJjYXJkX3N0YXR1cyI6IHN1bW1hcnlbImNhcmRfc3RhdHVzIl0sCiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogc3VtbWFyeVsicmVsZWFzZV9wYXNzZWQiXSwKICAgICAgICAidGhyZXNob2xkX3JlYWR5Ijogc3VtbWFyeVsidGhyZXNob2xkX3JlYWR5Il0sCiAgICAgICAgImNhcmRfY291bnQiOiBzdW1tYXJ5WyJjYXJkX2NvdW50Il0sCiAgICAgICAgImF0dGVudGlvbl9jYXJkX2NvdW50Ijogc3VtbWFyeVsiYXR0ZW50aW9uX2NhcmRfY291bnQiXSwKICAgICAgICAidGhyZXNob2xkc19jaGFuZ2VkIjogc3VtbWFyeVsidGhyZXNob2xkc19jaGFuZ2VkIl0sCiAgICAgICAgImNsYXNzaWZpZXJfY2hhbmdlZCI6IHN1bW1hcnlbImNsYXNzaWZpZXJfY2hhbmdlZCJdLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0sCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IHN1bW1hcnlbImV4ZWN1dG9yX3JhbiJdLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogc3VtbWFyeVsiYXBwbGljYXRpb25fYWxsb3dlZCJdLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogc3VtbWFyeVsiY2FsaWJyYXRpb25fYXBwbGllZCJdLAogICAgICAgICJjaGFydF9jb3VudCI6IGxlbihzdW1tYXJ5WyJjaGFydF9wYXRocyJdKSwKICAgICAgICAicmVwb3J0IjogInJlcG9ydHMvdHNla19ib3VuZGFyeV9jYXJkcy9sYXRlc3RfdHNla19ib3VuZGFyeV9leHBsYW5hdGlvbl9jYXJkcy5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT / "reports" / "tsek_boundary_cards" / "README.md", """# TSEK Boundary Card Reports

Current layer: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**

## Purpose

This folder stores one explanation-card surface for TSEK class boundaries.

## Primary command

```powershell
python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py
```

## README Update Rule

Update this mini README whenever TSEK boundary cards, class explanations, or threshold-review interpretation changes.

Boundary: TSEK boundary cards are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "tsek_boundary_cards" / "README.md", """# TSEK Boundary Card Visuals

Current layer: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**

## Purpose

This folder stores charts summarizing TSEK boundary explanation cards.

## README Update Rule

Update this mini README whenever boundary-card chart names or meanings change.

Boundary: TSEK boundary-card visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "tsek_boundary_cards" / "v0_7_5" / "README.md", """# v0.7.5 TSEK Boundary Card Charts

Expected charts:

- `tsek_boundary_report_visibility.png`
- `tsek_boundary_attention_flags.png`
- `tsek_boundary_cards_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local TSEK boundary-card diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.4[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.3[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.4 - TSEK Threshold Boundary Review**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.4 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.5 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.4-ready |", "| Task routing matrix | geometry-aware / v0.7.5-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.4 |", "| Agent contract version sync | current / v0.7.5 |")

if "| TSEK boundary explanation cards |" not in r:
    r = r.replace("| TSEK threshold charts | `visuals/tsek_threshold_review/v0_7_4/` |\n",
                  "| TSEK threshold charts | `visuals/tsek_threshold_review/v0_7_4/` |\n| TSEK boundary explanation cards | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` |\n| TSEK boundary card charts | `visuals/tsek_boundary_cards/v0_7_5/` |\n")

if "python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py" not in r:
    r = r.replace("python scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython scripts/release/validate_release.py")

if "    tsek_boundary_cards/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    tsek_boundary_cards/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    tsek_boundary_cards/\n")

section = """## TSEK Boundary Explanation Cards v0.7.5

v0.7.5 creates one non-mutating explanation-card surface for the TSEK class boundaries.

Primary command:

```powershell
python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py
```

Primary outputs:

```text
reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.json
reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md
reports/tsek_boundary_cards/cards/
visuals/tsek_boundary_cards/v0_7_5/
```

Current lock:

```text
thresholds_changed: false
classifier_changed: false
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: TSEK boundary explanation cards are local classifier-governance analysis artifacts. They explain class-boundary semantics without changing classifier behavior. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## TSEK Boundary Explanation Cards v0.7.5" not in r:
    r = r.replace("## TSEK Threshold Boundary Review v0.7.4", section + "## TSEK Threshold Boundary Review v0.7.4", 1)

lesson = "| L-057 | v0.7.4 reviewed TSEK threshold boundaries without changing thresholds. | Boundary review identifies visibility, but humans and agents need class-level explanation cards before pressure testing penalties. | TSEK class boundaries must be explained as cards before over/under-penalty controls or threshold dry-runs. |"
if "L-057" not in r:
    r = r.replace("| L-056 | v0.7.3 mapped gate-family visibility and found targeted gate gaps. | Gate mapping still does not authorize threshold changes. | TSEK threshold boundaries must be reviewed and explained before any classifier mutation or threshold tuning. |\n",
                  "| L-056 | v0.7.3 mapped gate-family visibility and found targeted gate gaps. | Gate mapping still does not authorize threshold changes. | TSEK threshold boundaries must be reviewed and explained before any classifier mutation or threshold tuning. |\n" + lesson + "\n")

if "| v0.7.5 |" not in r:
    r = r.replace("| v0.7.4 | TSEK threshold boundary review; reviews class-boundary visibility without mutation. |\n",
                  "| v0.7.4 | TSEK threshold boundary review; reviews class-boundary visibility without mutation. |\n| v0.7.5 | TSEK boundary explanation cards; explains each class boundary before penalty controls. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**

Recommended goals:

- Generate negative controls for over-penalty and under-penalty risk.
- Test boundary-card assumptions without changing thresholds.
- Preserve no-classifier-mutation lock.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.4[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_tsek_boundary_explanation_cards.py" not in s:
        s = s.replace("python scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/run_tsek_threshold_boundary_review.py\npython scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython -m unittest discover -s tests")
        s = s.replace("| TSEK threshold review patch | `reports/tsek_threshold_review/`, `visuals/tsek_threshold_review/`, classifier/reports | threshold boundary review + release validator; no mutation |\n",
                      "| TSEK threshold review patch | `reports/tsek_threshold_review/`, `visuals/tsek_threshold_review/`, classifier/reports | threshold boundary review + release validator; no mutation |\n| TSEK boundary card patch | `reports/tsek_boundary_cards/`, `visuals/tsek_boundary_cards/`, threshold review | boundary cards + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| TSEK boundary card patch |" not in s:
        s = s.replace("| TSEK threshold review patch | inner | analysis | classifier | classifier + gate algebra + reports | threshold review + charts + release validator | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` |\n",
                      "| TSEK threshold review patch | inner | analysis | classifier | classifier + gate algebra + reports | threshold review + charts + release validator | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` |\n| TSEK boundary card patch | inner | explanation | classifier | threshold review + TSEK classes | boundary cards + charts + release validator | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.5"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["tsek_boundary_explanation_cards"] = {
    "read_first": ["reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.json", "reports/gate_algebra/latest_gate_algebra_map.json"],
    "validate": ["python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md", "visuals/tsek_boundary_cards/v0_7_5/"],
    "mutation_lock": "Explanation cards only; no classifier change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.5 | TSEK boundary explanation cards |" not in t:
    t = t.replace("| v0.7.4 | TSEK threshold boundary review | `python scripts/benchmarks/run_tsek_threshold_boundary_review.py` | Reviews TSEK class-boundary visibility without changing classifier behavior | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` | `visuals/tsek_threshold_review/v0_7_4/` |\n",
                  "| v0.7.4 | TSEK threshold boundary review | `python scripts/benchmarks/run_tsek_threshold_boundary_review.py` | Reviews TSEK class-boundary visibility without changing classifier behavior | `reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.md` | `visuals/tsek_threshold_review/v0_7_4/` |\n| v0.7.5 | TSEK boundary explanation cards | `python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py` | Creates class-boundary explanation cards without changing thresholds | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` | `visuals/tsek_boundary_cards/v0_7_5/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_5_tsek_boundary_cards.md", f"""# TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards

Generated: {NOW}

## Purpose

Create non-mutating explanation cards for TSEK class boundaries before over/under-penalty controls.

## Boundary

TSEK boundary explanation cards are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.5 patch written")
