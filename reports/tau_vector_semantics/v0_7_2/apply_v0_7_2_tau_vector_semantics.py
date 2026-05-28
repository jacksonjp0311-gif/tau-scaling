
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
        d = ROOT / "reports" / "tau_vector_semantics" / "v0_7_2" / "backups" / f"{p.name}_before_v0_7_2_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_tau_vector_semantics_ledger.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zLCByZQpmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRhdV92ZWN0b3Jfc2VtYW50aWNzIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gInRhdV92ZWN0b3Jfc2VtYW50aWNzIiAvICJ2MF83XzIiCgpDT1JFX0ZJTEVTID0gWwogICAgUk9PVCAvICJzcmMiIC8gInRhdV9zY2FsaW5nIiAvICJjb3JlIiAvICJydW50aW1lLnB5IiwKICAgIFJPT1QgLyAic3JjIiAvICJ0YXVfc2NhbGluZyIgLyAiY29yZSIgLyAiY2xhc3NpZmllci5weSIsCiAgICBST09UIC8gInNyYyIgLyAidGF1X3NjYWxpbmciIC8gImNvcmUiIC8gIm1vZGVscy5weSIsCl0KU0VFRF9ESVIgPSBST09UIC8gImNvbmZpZ3MiIC8gInNlZWRzIgpNRUNIID0gUk9PVCAvICJyZXBvcnRzIiAvICJ0YXVfbWVjaGFuaWNzX3JldmlldyIgLyAibGF0ZXN0X3RhdV9tZWNoYW5pY3NfcmV0dXJuX3Jldmlldy5qc29uIgpSRUxFQVNFID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIKClRBVV9URVJNUyA9IFsKICAgICJ0YXVfZ2FpbiIsCiAgICAidGF1X3ZlY3RvciIsCiAgICAibG9naWNmb2xkaW5nIiwKICAgICJzdXJ2aXZhYmlsaXR5IiwKICAgICJlZGdlX3N1cmZhY2UiLAogICAgImVuZXJneSIsCiAgICAidGhlcm1hbCIsCiAgICAicGRuIiwKICAgICJwdnQiLAogICAgIm1vbnRlX2NhcmxvIiwKICAgICJiYXNlbGluZSIsCiAgICAiY2FuZGlkYXRlIiwKICAgICJ3b3JrbG9hZCIsCl0KCmRlZiByZWFkX3RleHQocGF0aDogUGF0aCkgLT4gc3RyOgogICAgcmV0dXJuIHBhdGgucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIsIGVycm9ycz0icmVwbGFjZSIpIGlmIHBhdGguZXhpc3RzKCkgZWxzZSAiIgoKZGVmIHJlYWRfanNvbihwYXRoOiBQYXRoKToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiB7Im1pc3NpbmciOiBUcnVlLCAicGF0aCI6IHN0cihwYXRoKX0KICAgIHRyeToKICAgICAgICByZXR1cm4ganNvbi5sb2FkcyhwYXRoLnJlYWRfdGV4dChlbmNvZGluZz0idXRmLTgiKSkKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHJldHVybiB7InBhcnNlX2Vycm9yIjogc3RyKGV4YyksICJwYXRoIjogc3RyKHBhdGgpfQoKZGVmIHdqc29uKHBhdGg6IFBhdGgsIGRhdGEpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KGpzb24uZHVtcHMoZGF0YSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSArICJcbiIsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgd3RleHQocGF0aDogUGF0aCwgdGV4dDogc3RyKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwYXRoOiBQYXRoKSAtPiBzdHI6CiAgICByZXR1cm4gc3RyKHBhdGgucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGZsYXR0ZW5fa2V5cyhvYmosIHByZWZpeD0iIik6CiAgICBrZXlzID0gW10KICAgIGlmIGlzaW5zdGFuY2Uob2JqLCBkaWN0KToKICAgICAgICBmb3IgaywgdiBpbiBvYmouaXRlbXMoKToKICAgICAgICAgICAgcCA9IGYie3ByZWZpeH0ue2t9IiBpZiBwcmVmaXggZWxzZSBzdHIoaykKICAgICAgICAgICAga2V5cy5hcHBlbmQocCkKICAgICAgICAgICAga2V5cy5leHRlbmQoZmxhdHRlbl9rZXlzKHYsIHApKQogICAgZWxpZiBpc2luc3RhbmNlKG9iaiwgbGlzdCk6CiAgICAgICAgZm9yIGksIHYgaW4gZW51bWVyYXRlKG9ials6MjBdKToKICAgICAgICAgICAgcCA9IGYie3ByZWZpeH1bXSIgaWYgcHJlZml4IGVsc2UgIltdIgogICAgICAgICAgICBrZXlzLmV4dGVuZChmbGF0dGVuX2tleXModiwgcCkpCiAgICByZXR1cm4ga2V5cwoKZGVmIHNlZWRfc2VtYW50aWNzKCk6CiAgICByb3dzID0gW10KICAgIGFsbF9rZXlzID0gQ291bnRlcigpCiAgICBmb3IgcCBpbiBzb3J0ZWQoU0VFRF9ESVIuZ2xvYigiKi5qc29uIikpOgogICAgICAgIGRhdGEgPSByZWFkX2pzb24ocCkKICAgICAgICB0ZXh0ID0ganNvbi5kdW1wcyhkYXRhKS5sb3dlcigpCiAgICAgICAga2V5cyA9IGZsYXR0ZW5fa2V5cyhkYXRhKQogICAgICAgIGZvciBrIGluIGtleXM6CiAgICAgICAgICAgIGFsbF9rZXlzW2tdICs9IDEKICAgICAgICBwcmVzZW50X3Rlcm1zID0gW3Rlcm0gZm9yIHRlcm0gaW4gVEFVX1RFUk1TIGlmIHRlcm0ubG93ZXIoKSBpbiB0ZXh0XQogICAgICAgIHJvd3MuYXBwZW5kKHsKICAgICAgICAgICAgInBhdGgiOiByZWwocCksCiAgICAgICAgICAgICJrZXlfY291bnQiOiBsZW4oa2V5cyksCiAgICAgICAgICAgICJwcmVzZW50X3RhdV90ZXJtcyI6IHByZXNlbnRfdGVybXMsCiAgICAgICAgICAgICJ0ZXJtX2NvdW50IjogbGVuKHByZXNlbnRfdGVybXMpLAogICAgICAgICAgICAiaGFzX3dvcmtsb2FkIjogIndvcmtsb2FkIiBpbiB0ZXh0LAogICAgICAgICAgICAiaGFzX2Jhc2VsaW5lIjogImJhc2VsaW5lIiBpbiB0ZXh0LAogICAgICAgICAgICAiaGFzX2NhbmRpZGF0ZSI6ICJjYW5kaWRhdGUiIGluIHRleHQsCiAgICAgICAgICAgICJoYXNfdGF1IjogInRhdSIgaW4gdGV4dCwKICAgICAgICAgICAgImhhc19nYXRlIjogYW55KHggaW4gdGV4dCBmb3IgeCBpbiBbImdhdGUiLCAidGhlcm1hbCIsICJwZG4iLCAicHZ0IiwgImVuZXJneSJdKSwKICAgICAgICB9KQogICAgcmV0dXJuIHJvd3MsIGRpY3QoYWxsX2tleXMubW9zdF9jb21tb24oODApKQoKZGVmIGNvZGVfc2VtYW50aWNzKCk6CiAgICB0ZXh0ID0gIlxuIi5qb2luKHJlYWRfdGV4dChwKSBmb3IgcCBpbiBDT1JFX0ZJTEVTKQogICAgcm93cyA9IFtdCiAgICBmb3IgdGVybSBpbiBUQVVfVEVSTVM6CiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAidGVybSI6IHRlcm0sCiAgICAgICAgICAgICJjb3JlX2NvdW50IjogbGVuKHJlLmZpbmRhbGwocmUuZXNjYXBlKHRlcm0pLCB0ZXh0LCByZS5JKSksCiAgICAgICAgICAgICJzZWVkX2NvdW50IjogMCwKICAgICAgICAgICAgInNlbWFudGljX3N0YXR1cyI6ICJjb3JlX3Zpc2libGUiIGlmIHJlLnNlYXJjaChyZS5lc2NhcGUodGVybSksIHRleHQsIHJlLkkpIGVsc2UgInNlZWRfb3JfcmVwb3J0X29ubHkiLAogICAgICAgIH0pCiAgICAjIHN5bWJvbGljIGZpZWxkIGFwcHJveGltYXRpb25zIGZyb20gY29kZSBuYW1lcyAvIGRpY3Qga2V5cwogICAgZnVuY3Rpb25zID0gc29ydGVkKHNldChyZS5maW5kYWxsKHIiZGVmXHMrKFtBLVphLXpfXVtBLVphLXowLTlfXSopXHMqXCgiLCB0ZXh0KSkpCiAgICBjbGFzc2VzID0gc29ydGVkKHNldChyZS5maW5kYWxsKHIiY2xhc3NccysoW0EtWmEtel9dW0EtWmEtejAtOV9dKilccypbOihdIiwgdGV4dCkpKQogICAgcmV0dXJuIHJvd3MsIGZ1bmN0aW9ucywgY2xhc3NlcwoKZGVmIGNsYXNzaWZ5KHJvd3MsIHNlZWRzLCBtZWNoYW5pY3MsIHJlbGVhc2UpOgogICAgZ2FwcyA9IFtdCiAgICBzZWVkX2NvdW50ID0gbGVuKHNlZWRzKQogICAgaWYgc2VlZF9jb3VudCA9PSAwOgogICAgICAgIGdhcHMuYXBwZW5kKCJub19zZWVkX2NhcmRzX2ZvdW5kIikKICAgIGlmIGFueShub3Qgc1siaGFzX3RhdSJdIGZvciBzIGluIHNlZWRzKToKICAgICAgICBnYXBzLmFwcGVuZCgic29tZV9zZWVkX2NhcmRzX2RvX25vdF9leHBsaWNpdGx5X3N1cmZhY2VfdGF1X3Rlcm1zIikKICAgIGlmIGFueShub3Qgc1siaGFzX2dhdGUiXSBmb3IgcyBpbiBzZWVkcyk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInNvbWVfc2VlZF9jYXJkc19kb19ub3RfZXhwbGljaXRseV9zdXJmYWNlX2dhdGVfdGVybXMiKQogICAgaWYgYW55KG5vdCBzWyJoYXNfYmFzZWxpbmUiXSBmb3IgcyBpbiBzZWVkcyk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInNvbWVfc2VlZF9jYXJkc19kb19ub3RfZXhwbGljaXRseV9zdXJmYWNlX2Jhc2VsaW5lX3Rlcm1zIikKICAgIGlmIGFueShyWyJjb3JlX2NvdW50Il0gPT0gMCBmb3IgciBpbiByb3dzIGlmIHJbInRlcm0iXSBpbiBbInRhdV92ZWN0b3IiLCAidGF1X2dhaW4iXSk6CiAgICAgICAgZ2Fwcy5hcHBlbmQoInRhdV92ZWN0b3Jfb3JfdGF1X2dhaW5fc2VtYW50aWNzX25lZWRfbW9yZV9leHBsaWNpdF9jb3JlX25hbWluZyIpCgogICAgcmVsZWFzZV9wYXNzZWQgPSByZWxlYXNlLmdldCgicGFzc2VkIikgaXMgVHJ1ZSBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJmaW5kaW5ncyIsIFtdKSkgPT0gMCBhbmQgbGVuKHJlbGVhc2UuZ2V0KCJzdGVwX2ZhaWx1cmVzIiwgW10pKSA9PSAwCiAgICBtZWNoYW5pY3NfcmVhZHkgPSBtZWNoYW5pY3MuZ2V0KCJyZWxlYXNlX3Bhc3NlZCIpIGlzIFRydWUgYW5kIG1lY2hhbmljcy5nZXQoImFwcHJvdmFsX2NvcnJpZG9yX2xvY2tlZCIpIGlzIFRydWUKCiAgICBpZiByZWxlYXNlX3Bhc3NlZCBhbmQgbWVjaGFuaWNzX3JlYWR5OgogICAgICAgIHN0YXR1cyA9ICJUQVVfVkVDVE9SX1NFTUFOVElDU19MRURHRVJfUkVBRFlfX1RBUkdFVEVEX0ZJRUxEU19JREVOVElGSUVEIgogICAgZWxzZToKICAgICAgICBzdGF0dXMgPSAiVEFVX1ZFQ1RPUl9TRU1BTlRJQ1NfTEVER0VSX05FRURTX1JFVklFVyIKCiAgICByZXR1cm4gZ2Fwcywgc3RhdHVzLCByZWxlYXNlX3Bhc3NlZCwgbWVjaGFuaWNzX3JlYWR5CgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGV4YykpCiAgICAgICAgcmV0dXJuIHBhdGhzCgogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIHRlcm1zID0gc3VtbWFyeVsidGF1X3Rlcm1fcm93cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIoW3JbInRlcm0iXSBmb3IgciBpbiB0ZXJtc10sIFtyWyJjb3JlX2NvdW50Il0gZm9yIHIgaW4gdGVybXNdKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0zNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkNvcmUgY29kZSBtZW50aW9ucyIpCiAgICBwbHQudGl0bGUoIlRhdSBWZWN0b3IgU2VtYW50aWNzIENvcmUgVGVybSBWaXNpYmlsaXR5IikKICAgIHNhdmUoInRhdV92ZWN0b3JfY29yZV90ZXJtX3Zpc2liaWxpdHkucG5nIikKCiAgICBzZWVkcyA9IHN1bW1hcnlbInNlZWRfc2VtYW50aWNfcm93cyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDEwLCA0KSkKICAgIHBsdC5iYXIoW1BhdGgoc1sicGF0aCJdKS5zdGVtIGZvciBzIGluIHNlZWRzXSwgW3NbInRlcm1fY291bnQiXSBmb3IgcyBpbiBzZWVkc10pCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTM1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiVGF1IHRlcm0gY291bnQiKQogICAgcGx0LnRpdGxlKCJTZWVkIENhcmQgVGF1IFRlcm0gQ292ZXJhZ2UiKQogICAgc2F2ZSgidGF1X3ZlY3Rvcl9zZWVkX3Rlcm1fY292ZXJhZ2UucG5nIikKCiAgICBoZWFsdGggPSB7CiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJtZWNoYW5pY3NfcmVhZHkiOiBpbnQoc3VtbWFyeVsibWVjaGFuaWNzX3JlYWR5Il0pLAogICAgICAgICJnYXBzIjogc3VtbWFyeVsiZ2FwX2NvdW50Il0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsibXV0YXRpb25fYWxsb3dlZCJdKSwKICAgIH0KICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoaGVhbHRoLmtleXMoKSksIGxpc3QoaGVhbHRoLnZhbHVlcygpKSkKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgiVGF1IFZlY3RvciBTZW1hbnRpY3MgSGVhbHRoIikKICAgIHNhdmUoInRhdV92ZWN0b3Jfc2VtYW50aWNzX2hlYWx0aC5wbmciKQogICAgcmV0dXJuIHBhdGhzCgpkZWYgbWFrZV9tZChzdW1tYXJ5KToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjcuMiBUYXUgVmVjdG9yIFNlbWFudGljcyBMZWRnZXIiLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBMZWRnZXIgUmVzdWx0IiwKICAgICAgICAiIiwKICAgICAgICBmIi0gU2VtYW50aWNzIHN0YXR1czogYHtzdW1tYXJ5WydzZW1hbnRpY3Nfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIE1lY2hhbmljcyByZWFkeTogYHtzdW1tYXJ5WydtZWNoYW5pY3NfcmVhZHknXX1gIiwKICAgICAgICBmIi0gU2VlZCBjb3VudDogYHtzdW1tYXJ5WydzZWVkX2NvdW50J119YCIsCiAgICAgICAgZiItIEdhcCBjb3VudDogYHtzdW1tYXJ5WydnYXBfY291bnQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgVGF1IFRlcm0gTGVkZ2VyIiwKICAgICAgICAiIiwKICAgICAgICAifCBUZXJtIHwgQ29yZSBjb3VudCB8IFN0YXR1cyB8IiwKICAgICAgICAifC0tLXwtLS06fC0tLXwiLAogICAgXQogICAgZm9yIHIgaW4gc3VtbWFyeVsidGF1X3Rlcm1fcm93cyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtyWyd0ZXJtJ119YCB8IHtyWydjb3JlX2NvdW50J119IHwgYHtyWydzZW1hbnRpY19zdGF0dXMnXX1gIHwiKQogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBTZWVkIFNlbWFudGljcyIsCiAgICAgICAgIiIsCiAgICAgICAgInwgU2VlZCB8IFRhdSB0ZXJtcyB8IFdvcmtsb2FkIHwgQmFzZWxpbmUgfCBDYW5kaWRhdGUgfCBHYXRlIHwiLAogICAgICAgICJ8LS0tfC0tLTp8LS0tOnwtLS06fC0tLTp8LS0tOnwiLAogICAgXQogICAgZm9yIHMgaW4gc3VtbWFyeVsic2VlZF9zZW1hbnRpY19yb3dzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYifCBge3NbJ3BhdGgnXX1gIHwge3NbJ3Rlcm1fY291bnQnXX0gfCBge3NbJ2hhc193b3JrbG9hZCddfWAgfCBge3NbJ2hhc19iYXNlbGluZSddfWAgfCBge3NbJ2hhc19jYW5kaWRhdGUnXX1gIHwgYHtzWydoYXNfZ2F0ZSddfWAgfCIpCiAgICBsaW5lcyArPSBbIiIsICIjIyBUYXJnZXRlZCBHYXBzIiwgIiJdCiAgICBpZiBzdW1tYXJ5WyJnYXBzIl06CiAgICAgICAgZm9yIGdhcCBpbiBzdW1tYXJ5WyJnYXBzIl06CiAgICAgICAgICAgIGxpbmVzLmFwcGVuZChmIi0gYHtnYXB9YCIpCiAgICBlbHNlOgogICAgICAgIGxpbmVzLmFwcGVuZCgiLSBgbm9uZV9kZXRlY3RlZF9pbl92MF83XzJfc2NhbmAiKQogICAgbGluZXMgKz0gWwogICAgICAgICIiLAogICAgICAgICIjIyBOZXh0IFRhdSBXb3JrIiwKICAgICAgICAiIiwKICAgICAgICAiMS4gQ29udmVydCBpbXBsaWNpdCB0YXUgdGVybXMgaW50byBhbiBleHBsaWNpdCB0YXUtdmVjdG9yIHNjaGVtYSB0YWJsZS4iLAogICAgICAgICIyLiBEZWZpbmUgZmllbGQtbGV2ZWwgc2VtYW50aWNzOiB3aGF0IGVhY2ggdGF1IGNvbXBvbmVudCBtZWFucywgd2hhdCBldmlkZW5jZSBzdXBwb3J0cyBpdCwgYW5kIHdoaWNoIGdhdGVzIGNvbnN1bWUgaXQuIiwKICAgICAgICAiMy4gQWRkIGNsYWltLWNhcmQgbmVnYXRpdmUgY29udHJvbHMgZm9yIG92ZXJsb2FkZWQgdGF1IGZpZWxkcy4iLAogICAgICAgICI0LiBSZXZpZXcgVFNFSyBzY29yZSBzZW5zaXRpdml0eSB0byBpbmRpdmlkdWFsIHRhdS12ZWN0b3IgY29tcG9uZW50cy4iLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc3VtbWFyeVsiY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHN1bW1hcnlbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBtZWNoYW5pY3MgPSByZWFkX2pzb24oTUVDSCkKICAgIHJlbGVhc2UgPSByZWFkX2pzb24oUkVMRUFTRSkKICAgIHNlZWRzLCBrZXlfY291bnRzID0gc2VlZF9zZW1hbnRpY3MoKQogICAgdGVybV9yb3dzLCBmdW5jdGlvbnMsIGNsYXNzZXMgPSBjb2RlX3NlbWFudGljcygpCgogICAgc2VlZF90ZXh0cyA9IHtQYXRoKHNbInBhdGgiXSkubmFtZTogc2V0KHNbInByZXNlbnRfdGF1X3Rlcm1zIl0pIGZvciBzIGluIHNlZWRzfQogICAgZm9yIHJvdyBpbiB0ZXJtX3Jvd3M6CiAgICAgICAgcm93WyJzZWVkX2NvdW50Il0gPSBzdW0oMSBmb3IgdGVybXMgaW4gc2VlZF90ZXh0cy52YWx1ZXMoKSBpZiByb3dbInRlcm0iXSBpbiB0ZXJtcykKCiAgICBnYXBzLCBzdGF0dXMsIHJlbGVhc2VfcGFzc2VkLCBtZWNoYW5pY3NfcmVhZHkgPSBjbGFzc2lmeSh0ZXJtX3Jvd3MsIHNlZWRzLCBtZWNoYW5pY3MsIHJlbGVhc2UpCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXRhdS12ZWN0b3Itc2VtYW50aWNzLWxlZGdlci12MC43LjIiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAic2VtYW50aWNzX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBib29sKHJlbGVhc2VfcGFzc2VkKSwKICAgICAgICAibWVjaGFuaWNzX3JlYWR5IjogYm9vbChtZWNoYW5pY3NfcmVhZHkpLAogICAgICAgICJzZWVkX2NvdW50IjogbGVuKHNlZWRzKSwKICAgICAgICAidGF1X3Rlcm1fcm93cyI6IHRlcm1fcm93cywKICAgICAgICAic2VlZF9zZW1hbnRpY19yb3dzIjogc2VlZHMsCiAgICAgICAgInNlZWRfa2V5X2NvdW50c190b3AiOiBrZXlfY291bnRzLAogICAgICAgICJjb3JlX2Z1bmN0aW9uX2NvdW50IjogbGVuKGZ1bmN0aW9ucyksCiAgICAgICAgImNvcmVfY2xhc3NfY291bnQiOiBsZW4oY2xhc3NlcyksCiAgICAgICAgImNvcmVfZnVuY3Rpb25zIjogZnVuY3Rpb25zWzo4MF0sCiAgICAgICAgImNvcmVfY2xhc3NlcyI6IGNsYXNzZXNbOjgwXSwKICAgICAgICAiZ2FwcyI6IGdhcHMsCiAgICAgICAgImdhcF9jb3VudCI6IGxlbihnYXBzKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGVkIjogRmFsc2UsCiAgICAgICAgImJyYW5jaF9jcmVhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJwb2xpY3lfZW5mb3JjZWQiOiBGYWxzZSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IEZhbHNlLAogICAgICAgICJydW50aW1lX2JlaGF2aW9yX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJNb3ZlIHRvIHYwLjcuMyBHYXRlIEFsZ2VicmEgTWFwOiBleHBsaWNpdGx5IG1hcCB0YXUtdmVjdG9yIGZpZWxkcyB0byBnYXRlcyBhbmQgVFNFSyBzY29yaW5nLiIsCiAgICAgICAgImJvdW5kYXJ5IjogIlRhdSB2ZWN0b3Igc2VtYW50aWNzIGxlZGdlcnMgYXJlIGxvY2FsIGNsYXNzaWZpZXItZ292ZXJuYW5jZSBhbmFseXNpcyBhcnRpZmFjdHMuIFRoZXkgZG9jdW1lbnQgc2VtYW50aWNzIGFuZCBldmlkZW5jZSBzdXJmYWNlcy4gVGhleSBkbyBub3QgY3JlYXRlIGxpdmUgYXBwcm92YWwsIGV4ZWN1dGUgcmVwbGF5IGNvbW1hbmRzLCBjcmVhdGUgYnJhbmNoZXMsIG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBhcHBseSBjYWxpYnJhdGlvbiwgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJ0YXVfdmVjdG9yX3NlbWFudGljc19sZWRnZXJfdjBfN18yLmpzb24iLCBzdW1tYXJ5KQogICAgd2pzb24oT1VUIC8gImxhdGVzdF90YXVfdmVjdG9yX3NlbWFudGljc19sZWRnZXIuanNvbiIsIHN1bW1hcnkpCiAgICB3dGV4dChPVVQgLyAidGF1X3ZlY3Rvcl9zZW1hbnRpY3NfbGVkZ2VyX3YwXzdfMi5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3RhdV92ZWN0b3Jfc2VtYW50aWNzX2xlZGdlci5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJzZW1hbnRpY3Nfc3RhdHVzIjogc3VtbWFyeVsic2VtYW50aWNzX3N0YXR1cyJdLAogICAgICAgICJyZWxlYXNlX3Bhc3NlZCI6IHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0sCiAgICAgICAgIm1lY2hhbmljc19yZWFkeSI6IHN1bW1hcnlbIm1lY2hhbmljc19yZWFkeSJdLAogICAgICAgICJzZWVkX2NvdW50Ijogc3VtbWFyeVsic2VlZF9jb3VudCJdLAogICAgICAgICJnYXBfY291bnQiOiBzdW1tYXJ5WyJnYXBfY291bnQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3RhdV92ZWN0b3Jfc2VtYW50aWNzL2xhdGVzdF90YXVfdmVjdG9yX3NlbWFudGljc19sZWRnZXIubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT / "reports" / "tau_vector_semantics" / "README.md", """# Tau Vector Semantics Reports

Current layer: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**

## Purpose

This folder stores tau-vector semantics ledgers that map tau terms, seed coverage, and evidence requirements.

## Primary command

```powershell
python scripts/benchmarks/generate_tau_vector_semantics_ledger.py
```

## README Update Rule

Update this mini README whenever tau-vector field names, evidence mappings, or semantic definitions change.

Boundary: tau vector semantics reports are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "tau_vector_semantics" / "README.md", """# Tau Vector Semantics Visuals

Current layer: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**

## Purpose

This folder stores charts summarizing tau-vector term visibility and seed coverage.

## README Update Rule

Update this mini README whenever tau-vector chart names or meanings change.

Boundary: tau-vector visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "tau_vector_semantics" / "v0_7_2" / "README.md", """# v0.7.2 Tau Vector Semantics Charts

Expected charts:

- `tau_vector_core_term_visibility.png`
- `tau_vector_seed_term_coverage.png`
- `tau_vector_semantics_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local tau-vector semantic diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.1[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.0[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.1 - Tau Mechanics Return Review**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.1 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.2 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.1-ready |", "| Task routing matrix | geometry-aware / v0.7.2-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.1 |", "| Agent contract version sync | current / v0.7.2 |")

if "| Tau vector semantics ledger |" not in r:
    r = r.replace("| Tau mechanics charts | `visuals/tau_mechanics_review/v0_7_1/` |\n",
                  "| Tau mechanics charts | `visuals/tau_mechanics_review/v0_7_1/` |\n| Tau vector semantics ledger | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` |\n| Tau vector semantics charts | `visuals/tau_vector_semantics/v0_7_2/` |\n")

if "python scripts/benchmarks/generate_tau_vector_semantics_ledger.py" not in r:
    r = r.replace("python scripts/benchmarks/run_tau_mechanics_return_review.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/run_tau_mechanics_return_review.py\npython scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython scripts/release/validate_release.py")

if "    tau_vector_semantics/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    tau_vector_semantics/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    tau_vector_semantics/\n")

section = """## Tau Vector Semantics Ledger v0.7.2

v0.7.2 defines the first explicit tau-vector semantics ledger after returning from approval-governance containment.

Primary command:

```powershell
python scripts/benchmarks/generate_tau_vector_semantics_ledger.py
```

Primary outputs:

```text
reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.json
reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md
visuals/tau_vector_semantics/v0_7_2/
```

Current lock:

```text
replay_allowed: false
executor_ran: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: tau vector semantics ledgers are local classifier-governance analysis artifacts. They document semantics and evidence surfaces. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Tau Vector Semantics Ledger v0.7.2" not in r:
    r = r.replace("## Tau Mechanics Return Review v0.7.1", section + "## Tau Mechanics Return Review v0.7.1", 1)

lesson = "| L-054 | v0.7.1 identified targeted Tau-mechanics gaps after the approval corridor was sealed. | The next repair should not mutate scoring; it should name and audit tau-vector semantics first. | Tau vector fields must be made explicit before gate algebra or TSEK thresholds are tightened. |"
if "L-054" not in r:
    r = r.replace("| L-053 | v0.7.0 sealed the approval-governance corridor. | Once containment is sealed, further progress must return to the object being governed. | Tau mechanics reviews should examine tau vectors, gate algebra, TSEK thresholds, sensitivity behavior, and evidence-card design before adding any new governance gate. |\n",
                  "| L-053 | v0.7.0 sealed the approval-governance corridor. | Once containment is sealed, further progress must return to the object being governed. | Tau mechanics reviews should examine tau vectors, gate algebra, TSEK thresholds, sensitivity behavior, and evidence-card design before adding any new governance gate. |\n" + lesson + "\n")

if "| v0.7.2 |" not in r:
    r = r.replace("| v0.7.1 | Tau mechanics return review; inspects tau vectors, gate algebra, thresholds, and evidence surfaces. |\n",
                  "| v0.7.1 | Tau mechanics return review; inspects tau vectors, gate algebra, thresholds, and evidence surfaces. |\n| v0.7.2 | Tau vector semantics ledger; maps tau terms, seed coverage, and evidence surface gaps. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.3 - Gate Algebra Map**

Recommended goals:

- Map tau-vector fields to gates.
- Separate evidence gates from classifier scoring.
- Identify over-penalty and under-penalty risks by gate family.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.1[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_tau_vector_semantics_ledger.py" not in s:
        s = s.replace("python scripts/benchmarks/run_tau_mechanics_return_review.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/run_tau_mechanics_return_review.py\npython scripts/benchmarks/generate_tau_vector_semantics_ledger.py\npython -m unittest discover -s tests")
        s = s.replace("| Tau mechanics review patch | `reports/tau_mechanics_review/`, `visuals/tau_mechanics_review/`, core runtime/seeds | mechanics scan + release validator; no mutation |\n",
                      "| Tau mechanics review patch | `reports/tau_mechanics_review/`, `visuals/tau_mechanics_review/`, core runtime/seeds | mechanics scan + release validator; no mutation |\n| Tau vector semantics patch | `reports/tau_vector_semantics/`, `visuals/tau_vector_semantics/`, seeds/runtime | semantics ledger + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Tau vector semantics patch |" not in s:
        s = s.replace("| Tau mechanics review patch | inner | analysis | runtime | core runtime + seeds + reports | mechanics scan + charts + release validator | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` |\n",
                      "| Tau mechanics review patch | inner | analysis | runtime | core runtime + seeds + reports | mechanics scan + charts + release validator | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` |\n| Tau vector semantics patch | inner | analysis | runtime | core runtime + seeds | semantics ledger + charts + release validator | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.2"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["tau_vector_semantics_ledger"] = {
    "read_first": ["src/tau_scaling/core/", "configs/seeds/", "reports/tau_mechanics_review/latest_tau_mechanics_return_review.json"],
    "validate": ["python scripts/benchmarks/generate_tau_vector_semantics_ledger.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md", "visuals/tau_vector_semantics/v0_7_2/"],
    "mutation_lock": "Semantics ledger only; no replay execution, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.2 | Tau vector semantics ledger |" not in t:
    t = t.replace("| v0.7.1 | Tau mechanics return review | `python scripts/benchmarks/run_tau_mechanics_return_review.py` | Reviews tau-vector, gate, threshold, seed, and evidence surfaces | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` | `visuals/tau_mechanics_review/v0_7_1/` |\n",
                  "| v0.7.1 | Tau mechanics return review | `python scripts/benchmarks/run_tau_mechanics_return_review.py` | Reviews tau-vector, gate, threshold, seed, and evidence surfaces | `reports/tau_mechanics_review/latest_tau_mechanics_return_review.md` | `visuals/tau_mechanics_review/v0_7_1/` |\n| v0.7.2 | Tau vector semantics ledger | `python scripts/benchmarks/generate_tau_vector_semantics_ledger.py` | Maps tau terms, seed coverage, and semantic gaps before gate algebra changes | `reports/tau_vector_semantics/latest_tau_vector_semantics_ledger.md` | `visuals/tau_vector_semantics/v0_7_2/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_2_tau_vector_semantics.md", f"""# TAU-SCALING-SA v0.7.2 - Tau Vector Semantics Ledger

Generated: {NOW}

## Purpose

Create the first explicit tau-vector semantics ledger after returning from approval-governance containment.

## Boundary

Tau vector semantics ledgers are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.2 patch written")
