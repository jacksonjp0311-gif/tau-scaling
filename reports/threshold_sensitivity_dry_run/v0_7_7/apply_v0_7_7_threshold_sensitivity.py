
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
        d = ROOT / "reports" / "threshold_sensitivity_dry_run" / "v0_7_7" / "backups" / f"{p.name}_before_v0_7_7_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "run_threshold_sensitivity_dry_run.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInRocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gInRocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuIiAvICJ2MF83XzciCgpQRU5BTFRZID0gUk9PVCAvICJyZXBvcnRzIiAvICJwZW5hbHR5X2NvbnRyb2xzIiAvICJsYXRlc3Rfb3Zlcl91bmRlcl9wZW5hbHR5X25lZ2F0aXZlX2NvbnRyb2xzLmpzb24iCkJPVU5EQVJZID0gUk9PVCAvICJyZXBvcnRzIiAvICJ0c2VrX2JvdW5kYXJ5X2NhcmRzIiAvICJsYXRlc3RfdHNla19ib3VuZGFyeV9leHBsYW5hdGlvbl9jYXJkcy5qc29uIgpUSFJFU0hPTEQgPSBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfdGhyZXNob2xkX3JldmlldyIgLyAibGF0ZXN0X3RzZWtfdGhyZXNob2xkX2JvdW5kYXJ5X3Jldmlldy5qc29uIgpSRUxFQVNFID0gUk9PVCAvICJyZXBvcnRzIiAvICJyZWxlYXNlIiAvICJsYXRlc3RfcmVsZWFzZV9yZWFkaW5lc3MuanNvbiIKClNJTVVMQVRFRF9BREpVU1RNRU5UUyA9IFsKICAgIHsic2NlbmFyaW8iOiAidGlnaHRlbl9wcm9tb3Rpb25fYm91bmRhcnlfcmVwb3J0X29ubHkiLCAiZGlyZWN0aW9uIjogInByb21vdGlvbl9oYXJkZXIiLCAidGFyZ2V0IjogIlRTRUstQi9UU0VLLUMiLCAicmlza19jaGVja2VkIjogInVuZGVyX3BlbmFsdHlfc3BhcnNlX2V2aWRlbmNlX2NsYWltIn0sCiAgICB7InNjZW5hcmlvIjogInNvZnRlbl9yZWplY3Rpb25fYm91bmRhcnlfcmVwb3J0X29ubHkiLCAiZGlyZWN0aW9uIjogInJlamVjdGlvbl9oYXJkZXJfdG9fdHJpZ2dlciIsICJ0YXJnZXQiOiAiVFNFSy1DL1RTRUstRSIsICJyaXNrX2NoZWNrZWQiOiAib3Zlcl9wZW5hbHR5X2hpZ2hfc3VwcG9ydF9jbGFpbSJ9LAogICAgeyJzY2VuYXJpbyI6ICJleHBvc2VfdHNla19kX2ludGVybWVkaWF0ZV9yZXBvcnRfb25seSIsICJkaXJlY3Rpb24iOiAiaW50ZXJtZWRpYXRlX3Zpc2liaWxpdHkiLCAidGFyZ2V0IjogIlRTRUstQy9UU0VLLUQvVFNFSy1FIiwgInJpc2tfY2hlY2tlZCI6ICJtaXNzaW5nX2ludGVybWVkaWF0ZV90c2VrX2RfcGF0aCJ9LAogICAgeyJzY2VuYXJpbyI6ICJyZXNlcnZlX3RzZWtfYV9yZXBvcnRfb25seSIsICJkaXJlY3Rpb24iOiAic3Ryb25nX2NsYXNzX2d1YXJkIiwgInRhcmdldCI6ICJUU0VLLUEvVFNFSy1CIiwgInJpc2tfY2hlY2tlZCI6ICJyZXNlcnZlZF90c2VrX2Ffb3ZlcmNsYWltX2d1YXJkIn0sCiAgICB7InNjZW5hcmlvIjogImdhdGVfZ2FwX25ldXRyYWxpdHlfcmVwb3J0X29ubHkiLCAiZGlyZWN0aW9uIjogIm5vX2RpcmVjdF9wZW5hbHR5IiwgInRhcmdldCI6ICJnYXRlX2ZhbWlseV90b190c2VrX3Njb3JlIiwgInJpc2tfY2hlY2tlZCI6ICJnYXRlX2dhcF9wZW5hbHR5X2FsaWdubWVudCJ9LApdCgpkZWYgcmVhZF9qc29uKHBhdGg6IFBhdGgpOgogICAgaWYgbm90IHBhdGguZXhpc3RzKCk6CiAgICAgICAgcmV0dXJuIHsibWlzc2luZyI6IFRydWUsICJwYXRoIjogc3RyKHBhdGgpfQogICAgdHJ5OgogICAgICAgIHJldHVybiBqc29uLmxvYWRzKHBhdGgucmVhZF90ZXh0KGVuY29kaW5nPSJ1dGYtOCIpKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBleGM6CiAgICAgICAgcmV0dXJuIHsicGFyc2VfZXJyb3IiOiBzdHIoZXhjKSwgInBhdGgiOiBzdHIocGF0aCl9CgpkZWYgd2pzb24ocGF0aDogUGF0aCwgZGF0YSk6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQoanNvbi5kdW1wcyhkYXRhLCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwYXRoOiBQYXRoLCB0ZXh0OiBzdHIpOgogICAgcGF0aC5wYXJlbnQubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQogICAgcGF0aC53cml0ZV90ZXh0KHRleHQsIGVuY29kaW5nPSJ1dGYtOCIpCgpkZWYgcmVsKHBhdGg6IFBhdGgpOgogICAgcmV0dXJuIHN0cihwYXRoLnJlbGF0aXZlX3RvKFJPT1QpKS5yZXBsYWNlKCJcXCIsICIvIikKCmRlZiBidWlsZF9zY2VuYXJpb3MocGVuYWx0eSk6CiAgICBjb250cm9scyA9IHtjWyJjb250cm9sX2lkIl06IGMgZm9yIGMgaW4gcGVuYWx0eS5nZXQoImNvbnRyb2xzIiwgW10pfQogICAgcm93cyA9IFtdCiAgICBmb3IgaXRlbSBpbiBTSU1VTEFURURfQURKVVNUTUVOVFM6CiAgICAgICAgY29udHJvbCA9IGNvbnRyb2xzLmdldChpdGVtWyJyaXNrX2NoZWNrZWQiXSwge30pCiAgICAgICAgcHJlc3N1cmUgPSBpbnQoY29udHJvbC5nZXQoInByZXNzdXJlX3Njb3JlIiwgMCkpCiAgICAgICAgaWYgcHJlc3N1cmUgPj0gODoKICAgICAgICAgICAgc2Vuc2l0aXZpdHkgPSAiaGlnaF9hdHRlbnRpb24iCiAgICAgICAgZWxpZiBwcmVzc3VyZSA+PSA0OgogICAgICAgICAgICBzZW5zaXRpdml0eSA9ICJtb2RlcmF0ZV9hdHRlbnRpb24iCiAgICAgICAgZWxzZToKICAgICAgICAgICAgc2Vuc2l0aXZpdHkgPSAibG93X2F0dGVudGlvbiIKCiAgICAgICAgcm93cy5hcHBlbmQoewogICAgICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXRocmVzaG9sZC1zZW5zaXRpdml0eS1kcnktcnVuLXNjZW5hcmlvLXYwLjcuNyIsCiAgICAgICAgICAgICoqaXRlbSwKICAgICAgICAgICAgImNvbnRyb2xfcHJlc3N1cmVfc2NvcmUiOiBwcmVzc3VyZSwKICAgICAgICAgICAgInNlbnNpdGl2aXR5X2NsYXNzIjogc2Vuc2l0aXZpdHksCiAgICAgICAgICAgICJzaW11bGF0ZWRfb25seSI6IFRydWUsCiAgICAgICAgICAgICJjdXJyZW50X2NsYXNzaWZpZXJfb3V0cHV0X2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAgICAgInRocmVzaG9sZF9jaGFuZ2VfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAiZHJ5X3J1bl9yZXN1bHQiOiAiUkVQT1JUX09OTFlfUkVWSUVXX1JFUVVJUkVEIiwKICAgICAgICAgICAgImludGVycHJldGF0aW9uIjogIlNjZW5hcmlvIGRlZmluZXMgcHJlc3N1cmUgdG8gaW5zcGVjdCBsYXRlcjsgaXQgZG9lcyBub3QgY2hhbmdlIHRocmVzaG9sZHMgb3IgY2xhc3NpZmllciBiZWhhdmlvci4iLAogICAgICAgIH0pCiAgICByZXR1cm4gcm93cwoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICB3dGV4dChPVVQgLyAiY2hhcnRfZ2VuZXJhdGlvbl9za2lwcGVkLnR4dCIsIHN0cihleGMpKQogICAgICAgIHJldHVybiBwYXRocwogICAgVklTLm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKCiAgICBkZWYgc2F2ZShuYW1lKToKICAgICAgICBwID0gVklTIC8gbmFtZQogICAgICAgIHBsdC50aWdodF9sYXlvdXQoKQogICAgICAgIHBsdC5zYXZlZmlnKHAsIGRwaT0xODAsIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICAgICAgcGx0LmNsb3NlKCkKICAgICAgICBwYXRocy5hcHBlbmQocmVsKHApKQoKICAgIHJvd3MgPSBzdW1tYXJ5WyJkcnlfcnVuX3NjZW5hcmlvcyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDExLCA0KSkKICAgIHBsdC5iYXIoW3JbInNjZW5hcmlvIl0gZm9yIHIgaW4gcm93c10sIFtyWyJjb250cm9sX3ByZXNzdXJlX3Njb3JlIl0gZm9yIHIgaW4gcm93c10pCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTM1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiUHJlc3N1cmUgc2NvcmUiKQogICAgcGx0LnRpdGxlKCJUaHJlc2hvbGQgU2Vuc2l0aXZpdHkgRHJ5LVJ1biBQcmVzc3VyZSIpCiAgICBzYXZlKCJ0aHJlc2hvbGRfc2Vuc2l0aXZpdHlfcHJlc3N1cmVfc2NvcmVzLnBuZyIpCgogICAgY291bnRzID0ge30KICAgIGZvciByIGluIHJvd3M6CiAgICAgICAgY291bnRzW3JbInNlbnNpdGl2aXR5X2NsYXNzIl1dID0gY291bnRzLmdldChyWyJzZW5zaXRpdml0eV9jbGFzcyJdLCAwKSArIDEKICAgIHBsdC5maWd1cmUoZmlnc2l6ZT0oOCwgNCkpCiAgICBwbHQuYmFyKGxpc3QoY291bnRzLmtleXMoKSksIGxpc3QoY291bnRzLnZhbHVlcygpKSkKICAgIHBsdC55bGFiZWwoIlNjZW5hcmlvIGNvdW50IikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIFNlbnNpdGl2aXR5IENsYXNzZXMiKQogICAgc2F2ZSgidGhyZXNob2xkX3NlbnNpdGl2aXR5X2NsYXNzZXMucG5nIikKCiAgICBoZWFsdGggPSB7CiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJjb250cm9sc19yZWFkeSI6IGludChzdW1tYXJ5WyJjb250cm9sc19yZWFkeSJdKSwKICAgICAgICAic2NlbmFyaW9zIjogc3VtbWFyeVsic2NlbmFyaW9fY291bnQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgiVGhyZXNob2xkIFNlbnNpdGl2aXR5IERyeS1SdW4gSGVhbHRoIikKICAgIHNhdmUoInRocmVzaG9sZF9zZW5zaXRpdml0eV9oZWFsdGgucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjcgVGhyZXNob2xkIFNlbnNpdGl2aXR5IERyeS1SdW4iLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3N1bW1hcnlbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBEcnktUnVuIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIERyeS1ydW4gc3RhdHVzOiBge3N1bW1hcnlbJ2RyeV9ydW5fc3RhdHVzJ119YCIsCiAgICAgICAgZiItIFJlbGVhc2UgcGFzc2VkOiBge3N1bW1hcnlbJ3JlbGVhc2VfcGFzc2VkJ119YCIsCiAgICAgICAgZiItIENvbnRyb2xzIHJlYWR5OiBge3N1bW1hcnlbJ2NvbnRyb2xzX3JlYWR5J119YCIsCiAgICAgICAgZiItIFNjZW5hcmlvIGNvdW50OiBge3N1bW1hcnlbJ3NjZW5hcmlvX2NvdW50J119YCIsCiAgICAgICAgZiItIFRocmVzaG9sZHMgY2hhbmdlZDogYHtzdW1tYXJ5Wyd0aHJlc2hvbGRzX2NoYW5nZWQnXX1gIiwKICAgICAgICBmIi0gQ2xhc3NpZmllciBjaGFuZ2VkOiBge3N1bW1hcnlbJ2NsYXNzaWZpZXJfY2hhbmdlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBSZXBvcnQtT25seSBTY2VuYXJpb3MiLAogICAgICAgICIiLAogICAgICAgICJ8IFNjZW5hcmlvIHwgRGlyZWN0aW9uIHwgVGFyZ2V0IHwgUHJlc3N1cmUgfCBTZW5zaXRpdml0eSB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLTp8LS0tfCIsCiAgICBdCiAgICBmb3IgciBpbiBzdW1tYXJ5WyJkcnlfcnVuX3NjZW5hcmlvcyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtyWydzY2VuYXJpbyddfWAgfCBge3JbJ2RpcmVjdGlvbiddfWAgfCBge3JbJ3RhcmdldCddfWAgfCB7clsnY29udHJvbF9wcmVzc3VyZV9zY29yZSddfSB8IGB7clsnc2Vuc2l0aXZpdHlfY2xhc3MnXX1gIHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgSW50ZXJwcmV0YXRpb24iLAogICAgICAgICIiLAogICAgICAgICJUaGlzIGRyeS1ydW4gb25seSBtb2RlbHMgd2hlcmUgdGhyZXNob2xkIHNlbnNpdGl2aXR5IHNob3VsZCBiZSBpbnNwZWN0ZWQuIEl0IGRvZXMgbm90IGNoYW5nZSB0aHJlc2hvbGRzLCBjbGFzcyBsb2dpYywgb3IgcnVudGltZSBjbGFzc2lmaWVyIGJlaGF2aW9yLiIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIE5leHQgVGF1IFdvcmsiLAogICAgICAgICIiLAogICAgICAgICIxLiBDb252ZXJ0IGhpZ2gtYXR0ZW50aW9uIHNlbnNpdGl2aXR5IHNjZW5hcmlvcyBpbnRvIGEgZGVjaXNpb24gcmVjb3JkLiIsCiAgICAgICAgIjIuIERlY2lkZSB3aGV0aGVyIGFueSBzY2VuYXJpbyBkZXNlcnZlcyBhIGZ1dHVyZSBjYW5kaWRhdGUgYnJhbmNoIHByb3Bvc2FsLiIsCiAgICAgICAgIjMuIEtlZXAgYWxsIGNoYW5nZXMgcmVwb3J0LW9ubHkgdW50aWwgZXhwbGljaXQgaHVtYW4gcmV2aWV3LiIsCiAgICAgICAgIjQuIFByZXNlcnZlIGxvY2FsLXJ1bnRpbWUgZXZpZGVuY2UgYm91bmRhcnkuIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzdW1tYXJ5WyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgcGVuYWx0eSA9IHJlYWRfanNvbihQRU5BTFRZKQogICAgYm91bmRhcnkgPSByZWFkX2pzb24oQk9VTkRBUlkpCiAgICB0aHJlc2hvbGQgPSByZWFkX2pzb24oVEhSRVNIT0xEKQogICAgcmVsZWFzZSA9IHJlYWRfanNvbihSRUxFQVNFKQoKICAgIHJlbGVhc2VfcGFzc2VkID0gcmVsZWFzZS5nZXQoInBhc3NlZCIpIGlzIFRydWUgYW5kIGxlbihyZWxlYXNlLmdldCgiZmluZGluZ3MiLCBbXSkpID09IDAgYW5kIGxlbihyZWxlYXNlLmdldCgic3RlcF9mYWlsdXJlcyIsIFtdKSkgPT0gMAogICAgY29udHJvbHNfcmVhZHkgPSBwZW5hbHR5LmdldCgiY29udHJvbF9zdGF0dXMiKSA9PSAiUEVOQUxUWV9DT05UUk9MU19ERUZJTkVEX19SRVBPUlRfT05MWV9OT19NVVRBVElPTiIKICAgIGJvdW5kYXJ5X3JlYWR5ID0gYm91bmRhcnkuZ2V0KCJjYXJkX3N0YXR1cyIpID09ICJUU0VLX0JPVU5EQVJZX0NBUkRTX1JFQURZX19OT19USFJFU0hPTERfQ0hBTkdFIgogICAgdGhyZXNob2xkX3JlYWR5ID0gdGhyZXNob2xkLmdldCgidGhyZXNob2xkX3Jldmlld19zdGF0dXMiKSA9PSAiVFNFS19USFJFU0hPTERfQk9VTkRBUllfUkVWSUVXX1JFQURZX19OT19USFJFU0hPTERfQ0hBTkdFIgoKICAgIHNjZW5hcmlvcyA9IGJ1aWxkX3NjZW5hcmlvcyhwZW5hbHR5KQogICAgZm9yIHJvdyBpbiBzY2VuYXJpb3M6CiAgICAgICAgd2pzb24oT1VUIC8gInNjZW5hcmlvcyIgLyBmIntyb3dbJ3NjZW5hcmlvJ119X3YwXzdfNy5qc29uIiwgcm93KQoKICAgIHN0YXR1cyA9ICJUSFJFU0hPTERfU0VOU0lUSVZJVFlfRFJZX1JVTl9SRUFEWV9fUkVQT1JUX09OTFlfTk9fTVVUQVRJT04iIGlmIHJlbGVhc2VfcGFzc2VkIGFuZCBjb250cm9sc19yZWFkeSBhbmQgYm91bmRhcnlfcmVhZHkgYW5kIHRocmVzaG9sZF9yZWFkeSBlbHNlICJUSFJFU0hPTERfU0VOU0lUSVZJVFlfRFJZX1JVTl9ORUVEU19SRVZJRVciCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLXRocmVzaG9sZC1zZW5zaXRpdml0eS1kcnktcnVuLXYwLjcuNyIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJkcnlfcnVuX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBib29sKHJlbGVhc2VfcGFzc2VkKSwKICAgICAgICAiY29udHJvbHNfcmVhZHkiOiBib29sKGNvbnRyb2xzX3JlYWR5KSwKICAgICAgICAiYm91bmRhcnlfY2FyZHNfcmVhZHkiOiBib29sKGJvdW5kYXJ5X3JlYWR5KSwKICAgICAgICAidGhyZXNob2xkX3Jldmlld19yZWFkeSI6IGJvb2wodGhyZXNob2xkX3JlYWR5KSwKICAgICAgICAic2NlbmFyaW9fY291bnQiOiBsZW4oc2NlbmFyaW9zKSwKICAgICAgICAiZHJ5X3J1bl9zY2VuYXJpb3MiOiBzY2VuYXJpb3MsCiAgICAgICAgImhpZ2hfYXR0ZW50aW9uX2NvdW50Ijogc3VtKDEgZm9yIHMgaW4gc2NlbmFyaW9zIGlmIHNbInNlbnNpdGl2aXR5X2NsYXNzIl0gPT0gImhpZ2hfYXR0ZW50aW9uIiksCiAgICAgICAgIm1vZGVyYXRlX2F0dGVudGlvbl9jb3VudCI6IHN1bSgxIGZvciBzIGluIHNjZW5hcmlvcyBpZiBzWyJzZW5zaXRpdml0eV9jbGFzcyJdID09ICJtb2RlcmF0ZV9hdHRlbnRpb24iKSwKICAgICAgICAibG93X2F0dGVudGlvbl9jb3VudCI6IHN1bSgxIGZvciBzIGluIHNjZW5hcmlvcyBpZiBzWyJzZW5zaXRpdml0eV9jbGFzcyJdID09ICJsb3dfYXR0ZW50aW9uIiksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgImV4ZWN1dG9yX3JhbiI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IEZhbHNlLAogICAgICAgICJicmFuY2hfY3JlYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJhcHBsaWNhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAicG9saWN5X2VuZm9yY2VkIjogRmFsc2UsCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBGYWxzZSwKICAgICAgICAicnVudGltZV9iZWhhdmlvcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAibmV4dF9yZWNvbW1lbmRhdGlvbiI6ICJNb3ZlIHRvIHYwLjcuOCBUaHJlc2hvbGQgRGVjaXNpb24gUmVjb3JkIGlmIHRoZSBkcnktcnVuIHN1cmZhY2VzIHJldmlldy13b3J0aHkgcHJlc3N1cmUuIiwKICAgICAgICAiYm91bmRhcnkiOiAiVGhyZXNob2xkIHNlbnNpdGl2aXR5IGRyeS1ydW5zIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYW5hbHlzaXMgYXJ0aWZhY3RzLiBUaGV5IG1vZGVsIHNlbnNpdGl2aXR5IHByZXNzdXJlIHVzaW5nIHJlcG9ydC1vbmx5IGNvbnRyb2xzLiBUaGV5IGRvIG5vdCBjcmVhdGUgbGl2ZSBhcHByb3ZhbCwgZXhlY3V0ZSByZXBsYXkgY29tbWFuZHMsIGNyZWF0ZSBicmFuY2hlcywgbXV0YXRlIGNsYXNzaWZpZXIgYmVoYXZpb3IsIGFwcGx5IGNhbGlicmF0aW9uLCBjaGFuZ2UgdGhyZXNob2xkcywgb3IgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgfQogICAgc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSA9IGNoYXJ0cyhzdW1tYXJ5KQoKICAgIHdqc29uKE9VVCAvICJ0aHJlc2hvbGRfc2Vuc2l0aXZpdHlfZHJ5X3J1bl92MF83XzcuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X3RocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuLmpzb24iLCBzdW1tYXJ5KQogICAgd3RleHQoT1VUIC8gInRocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuX3YwXzdfNy5tZCIsIG1ha2VfbWQoc3VtbWFyeSkpCiAgICB3dGV4dChPVVQgLyAibGF0ZXN0X3RocmVzaG9sZF9zZW5zaXRpdml0eV9kcnlfcnVuLm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImRyeV9ydW5fc3RhdHVzIjogc3VtbWFyeVsiZHJ5X3J1bl9zdGF0dXMiXSwKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBzdW1tYXJ5WyJyZWxlYXNlX3Bhc3NlZCJdLAogICAgICAgICJjb250cm9sc19yZWFkeSI6IHN1bW1hcnlbImNvbnRyb2xzX3JlYWR5Il0sCiAgICAgICAgInNjZW5hcmlvX2NvdW50Ijogc3VtbWFyeVsic2NlbmFyaW9fY291bnQiXSwKICAgICAgICAiaGlnaF9hdHRlbnRpb25fY291bnQiOiBzdW1tYXJ5WyJoaWdoX2F0dGVudGlvbl9jb3VudCJdLAogICAgICAgICJ0aHJlc2hvbGRzX2NoYW5nZWQiOiBzdW1tYXJ5WyJ0aHJlc2hvbGRzX2NoYW5nZWQiXSwKICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogc3VtbWFyeVsiY2xhc3NpZmllcl9jaGFuZ2VkIl0sCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogc3VtbWFyeVsicmVwbGF5X2FsbG93ZWQiXSwKICAgICAgICAiZXhlY3V0b3JfcmFuIjogc3VtbWFyeVsiZXhlY3V0b3JfcmFuIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy90aHJlc2hvbGRfc2Vuc2l0aXZpdHlfZHJ5X3J1bi9sYXRlc3RfdGhyZXNob2xkX3NlbnNpdGl2aXR5X2RyeV9ydW4ubWQiLAogICAgfSwgaW5kZW50PTIsIHNvcnRfa2V5cz1UcnVlKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCkK").decode())

write(ROOT / "reports" / "threshold_sensitivity_dry_run" / "README.md", """# Threshold Sensitivity Dry-Run Reports

Current layer: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**

## Purpose

This folder stores report-only threshold sensitivity dry-runs for TSEK boundary controls.

## Primary command

```powershell
python scripts/benchmarks/run_threshold_sensitivity_dry_run.py
```

## README Update Rule

Update this mini README whenever threshold dry-run scenarios, sensitivity classes, or decision-record pathways change.

Boundary: threshold sensitivity dry-runs are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "threshold_sensitivity_dry_run" / "README.md", """# Threshold Sensitivity Dry-Run Visuals

Current layer: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**

## Purpose

This folder stores charts summarizing report-only threshold sensitivity pressure.

## README Update Rule

Update this mini README whenever threshold sensitivity chart names or meanings change.

Boundary: threshold sensitivity visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "threshold_sensitivity_dry_run" / "v0_7_7" / "README.md", """# v0.7.7 Threshold Sensitivity Charts

Expected charts:

- `threshold_sensitivity_pressure_scores.png`
- `threshold_sensitivity_classes.png`
- `threshold_sensitivity_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local threshold-sensitivity diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.6[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.5[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.6 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.7 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.6-ready |", "| Task routing matrix | geometry-aware / v0.7.7-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.6 |", "| Agent contract version sync | current / v0.7.7 |")

if "| Threshold sensitivity dry-run |" not in r:
    r = r.replace("| Penalty control charts | `visuals/penalty_controls/v0_7_6/` |\n",
                  "| Penalty control charts | `visuals/penalty_controls/v0_7_6/` |\n| Threshold sensitivity dry-run | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` |\n| Threshold sensitivity charts | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n")

if "python scripts/benchmarks/run_threshold_sensitivity_dry_run.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_over_under_penalty_controls.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_over_under_penalty_controls.py\npython scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython scripts/release/validate_release.py")

if "    threshold_sensitivity_dry_run/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    threshold_sensitivity_dry_run/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    threshold_sensitivity_dry_run/\n")

section = """## Threshold Sensitivity Dry-Run v0.7.7

v0.7.7 runs report-only threshold sensitivity scenarios using the v0.7.6 over/under-penalty controls.

Primary command:

```powershell
python scripts/benchmarks/run_threshold_sensitivity_dry_run.py
```

Primary outputs:

```text
reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.json
reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md
reports/threshold_sensitivity_dry_run/scenarios/
visuals/threshold_sensitivity_dry_run/v0_7_7/
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

Boundary: threshold sensitivity dry-runs are local classifier-governance analysis artifacts. They model sensitivity pressure using report-only controls. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Threshold Sensitivity Dry-Run v0.7.7" not in r:
    r = r.replace("## Over/Under-Penalty Negative Controls v0.7.6", section + "## Over/Under-Penalty Negative Controls v0.7.6", 1)

lesson = "| L-059 | v0.7.6 defined report-only over/under-penalty controls. | Controls alone do not show which threshold pressures are high attention. | Threshold sensitivity must be dry-run in report-only mode before any decision record or classifier change is discussed. |"
if "L-059" not in r:
    r = r.replace("| L-058 | v0.7.5 generated boundary cards and flagged every class boundary for attention. | Explanation cards alone still do not test whether boundaries over-penalize or under-penalize claims. | TSEK boundary cards must be followed by report-only over/under-penalty controls before threshold dry-runs or classifier tuning. |\n",
                  "| L-058 | v0.7.5 generated boundary cards and flagged every class boundary for attention. | Explanation cards alone still do not test whether boundaries over-penalize or under-penalize claims. | TSEK boundary cards must be followed by report-only over/under-penalty controls before threshold dry-runs or classifier tuning. |\n" + lesson + "\n")

if "| v0.7.7 |" not in r:
    r = r.replace("| v0.7.6 | Over/under-penalty negative controls; defines report-only controls before threshold dry-runs. |\n",
                  "| v0.7.6 | Over/under-penalty negative controls; defines report-only controls before threshold dry-runs. |\n| v0.7.7 | Threshold sensitivity dry-run; models threshold pressure without changing classifier behavior. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.8 - Threshold Decision Record**

Recommended goals:

- Convert threshold sensitivity dry-run outputs into a decision record.
- Classify whether threshold tuning is rejected, deferred, or review-ready.
- Preserve no-classifier-mutation lock.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.6[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "run_threshold_sensitivity_dry_run.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_over_under_penalty_controls.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_over_under_penalty_controls.py\npython scripts/benchmarks/run_threshold_sensitivity_dry_run.py\npython -m unittest discover -s tests")
        s = s.replace("| Penalty controls patch | `reports/penalty_controls/`, `visuals/penalty_controls/`, TSEK boundary cards | report-only penalty controls + release validator; no mutation |\n",
                      "| Penalty controls patch | `reports/penalty_controls/`, `visuals/penalty_controls/`, TSEK boundary cards | report-only penalty controls + release validator; no mutation |\n| Threshold sensitivity patch | `reports/threshold_sensitivity_dry_run/`, `visuals/threshold_sensitivity_dry_run/`, penalty controls | report-only dry-run + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Threshold sensitivity patch |" not in s:
        s = s.replace("| Penalty controls patch | inner | analysis | classifier | TSEK boundary cards + threshold review | report-only controls + charts + release validator | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` |\n",
                      "| Penalty controls patch | inner | analysis | classifier | TSEK boundary cards + threshold review | report-only controls + charts + release validator | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` |\n| Threshold sensitivity patch | inner | dry-run | classifier | penalty controls + threshold review | report-only threshold sensitivity + charts + release validator | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.7"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["threshold_sensitivity_dry_run"] = {
    "read_first": ["reports/penalty_controls/latest_over_under_penalty_negative_controls.json", "reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.json"],
    "validate": ["python scripts/benchmarks/run_threshold_sensitivity_dry_run.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md", "visuals/threshold_sensitivity_dry_run/v0_7_7/"],
    "mutation_lock": "Report-only threshold sensitivity; no classifier change, threshold change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.7 | Threshold sensitivity dry-run |" not in t:
    t = t.replace("| v0.7.6 | Over/under-penalty negative controls | `python scripts/benchmarks/generate_over_under_penalty_controls.py` | Defines report-only controls before threshold dry-runs | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` | `visuals/penalty_controls/v0_7_6/` |\n",
                  "| v0.7.6 | Over/under-penalty negative controls | `python scripts/benchmarks/generate_over_under_penalty_controls.py` | Defines report-only controls before threshold dry-runs | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` | `visuals/penalty_controls/v0_7_6/` |\n| v0.7.7 | Threshold sensitivity dry-run | `python scripts/benchmarks/run_threshold_sensitivity_dry_run.py` | Models threshold pressure without changing classifier behavior | `reports/threshold_sensitivity_dry_run/latest_threshold_sensitivity_dry_run.md` | `visuals/threshold_sensitivity_dry_run/v0_7_7/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_7_threshold_sensitivity.md", f"""# TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run

Generated: {NOW}

## Purpose

Run report-only threshold sensitivity scenarios using the v0.7.6 over/under-penalty controls.

## Boundary

Threshold sensitivity dry-runs are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.7 patch written")
