
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
        d = ROOT / "reports" / "penalty_controls" / "v0_7_6" / "backups" / f"{p.name}_before_v0_7_6_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_text(read(p), encoding="utf-8")

write(ROOT / "scripts" / "benchmarks" / "generate_over_under_penalty_controls.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpPVVQgPSBST09UIC8gInJlcG9ydHMiIC8gInBlbmFsdHlfY29udHJvbHMiClZJUyA9IFJPT1QgLyAidmlzdWFscyIgLyAicGVuYWx0eV9jb250cm9scyIgLyAidjBfN182IgoKQk9VTkRBUllfQ0FSRFMgPSBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfYm91bmRhcnlfY2FyZHMiIC8gImxhdGVzdF90c2VrX2JvdW5kYXJ5X2V4cGxhbmF0aW9uX2NhcmRzLmpzb24iClRIUkVTSE9MRF9SRVZJRVcgPSBST09UIC8gInJlcG9ydHMiIC8gInRzZWtfdGhyZXNob2xkX3JldmlldyIgLyAibGF0ZXN0X3RzZWtfdGhyZXNob2xkX2JvdW5kYXJ5X3Jldmlldy5qc29uIgpHQVRFX0FMR0VCUkEgPSBST09UIC8gInJlcG9ydHMiIC8gImdhdGVfYWxnZWJyYSIgLyAibGF0ZXN0X2dhdGVfYWxnZWJyYV9tYXAuanNvbiIKUkVMRUFTRSA9IFJPT1QgLyAicmVwb3J0cyIgLyAicmVsZWFzZSIgLyAibGF0ZXN0X3JlbGVhc2VfcmVhZGluZXNzLmpzb24iCgpDT05UUk9MX0NMQVNTRVMgPSBbCiAgICB7CiAgICAgICAgImNvbnRyb2xfaWQiOiAib3Zlcl9wZW5hbHR5X2hpZ2hfc3VwcG9ydF9jbGFpbSIsCiAgICAgICAgInJpc2tfdHlwZSI6ICJvdmVyX3BlbmFsdHkiLAogICAgICAgICJ0YXJnZXRfY2xhc3NfYm91bmRhcnkiOiAiVFNFSy1DL1RTRUstRSIsCiAgICAgICAgInB1cnBvc2UiOiAiRGV0ZWN0IGNhc2VzIHdoZXJlIGhpZ2gtc3VwcG9ydCBsb2NhbCBldmlkZW5jZSBpcyBwdXNoZWQgdG9vIGhhcnNobHkgaW50byByZWplY3Rpb24uIiwKICAgICAgICAiZXhwZWN0ZWRfYmVoYXZpb3IiOiAicmV0YWluX29yX2V4cGxhaW5fY29udHJvbGxlZF9kb3duZ3JhZGUiLAogICAgfSwKICAgIHsKICAgICAgICAiY29udHJvbF9pZCI6ICJ1bmRlcl9wZW5hbHR5X3NwYXJzZV9ldmlkZW5jZV9jbGFpbSIsCiAgICAgICAgInJpc2tfdHlwZSI6ICJ1bmRlcl9wZW5hbHR5IiwKICAgICAgICAidGFyZ2V0X2NsYXNzX2JvdW5kYXJ5IjogIlRTRUstQi9UU0VLLUMiLAogICAgICAgICJwdXJwb3NlIjogIkRldGVjdCBjYXNlcyB3aGVyZSBzcGFyc2UgZXZpZGVuY2UgaXMgcHJvbW90ZWQgdG9vIHN0cm9uZ2x5LiIsCiAgICAgICAgImV4cGVjdGVkX2JlaGF2aW9yIjogImRvd25ncmFkZV9vcl9ibG9ja19wcm9tb3Rpb24iLAogICAgfSwKICAgIHsKICAgICAgICAiY29udHJvbF9pZCI6ICJtaXNzaW5nX2ludGVybWVkaWF0ZV90c2VrX2RfcGF0aCIsCiAgICAgICAgInJpc2tfdHlwZSI6ICJib3VuZGFyeV9nYXAiLAogICAgICAgICJ0YXJnZXRfY2xhc3NfYm91bmRhcnkiOiAiVFNFSy1DL1RTRUstRC9UU0VLLUUiLAogICAgICAgICJwdXJwb3NlIjogIkRldGVjdCB3aGV0aGVyIHRoZSBpbnRlcm1lZGlhdGUgd2VhayBjbGFzcyBpcyBhYnNlbnQgYmVjYXVzZSBvZiBkZXNpZ24gb3IgaW5zdWZmaWNpZW50IHNjZW5hcmlvIGNvdmVyYWdlLiIsCiAgICAgICAgImV4cGVjdGVkX2JlaGF2aW9yIjogImV4cGxhaW5fYWJzZW5jZV9vcl9hZGRfZnV0dXJlX3NjZW5hcmlvIiwKICAgIH0sCiAgICB7CiAgICAgICAgImNvbnRyb2xfaWQiOiAicmVzZXJ2ZWRfdHNla19hX292ZXJjbGFpbV9ndWFyZCIsCiAgICAgICAgInJpc2tfdHlwZSI6ICJvdmVyY2xhaW0iLAogICAgICAgICJ0YXJnZXRfY2xhc3NfYm91bmRhcnkiOiAiVFNFSy1BL1RTRUstQiIsCiAgICAgICAgInB1cnBvc2UiOiAiUHJldmVudCBsb2NhbCBydW50aW1lIGV2aWRlbmNlIGZyb20gYmVpbmcgbWlzcmVhZCBhcyBleHRlcm5hbGx5IHZhbGlkYXRlZCBzdHJvbmcgcHJvb2YuIiwKICAgICAgICAiZXhwZWN0ZWRfYmVoYXZpb3IiOiAia2VlcF90c2VrX2FfcmVzZXJ2ZWRfd2l0aG91dF9leHRlcm5hbF9ldmlkZW5jZSIsCiAgICB9LAogICAgewogICAgICAgICJjb250cm9sX2lkIjogImdhdGVfZ2FwX3BlbmFsdHlfYWxpZ25tZW50IiwKICAgICAgICAicmlza190eXBlIjogImdhdGVfbWFwcGluZyIsCiAgICAgICAgInRhcmdldF9jbGFzc19ib3VuZGFyeSI6ICJnYXRlX2ZhbWlseV90b190c2VrX3Njb3JlIiwKICAgICAgICAicHVycG9zZSI6ICJDaGVjayB3aGV0aGVyIGtub3duIGdhdGUgdmlzaWJpbGl0eSBnYXBzIGFyZSB0cmVhdGVkIGFzIGV4cGxhbmF0aW9uIHRhcmdldHMgcmF0aGVyIHRoYW4gZGlyZWN0IHBlbmFsdHkgY2hhbmdlcy4iLAogICAgICAgICJleHBlY3RlZF9iZWhhdmlvciI6ICJyZXBvcnRfb25seV9ub190aHJlc2hvbGRfY2hhbmdlIiwKICAgIH0sCl0KCmRlZiByZWFkX2pzb24ocGF0aDogUGF0aCk6CiAgICBpZiBub3QgcGF0aC5leGlzdHMoKToKICAgICAgICByZXR1cm4geyJtaXNzaW5nIjogVHJ1ZSwgInBhdGgiOiBzdHIocGF0aCl9CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGpzb24ubG9hZHMocGF0aC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICByZXR1cm4geyJwYXJzZV9lcnJvciI6IHN0cihleGMpLCAicGF0aCI6IHN0cihwYXRoKX0KCmRlZiB3anNvbihwYXRoOiBQYXRoLCBkYXRhKToKICAgIHBhdGgucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHBhdGgud3JpdGVfdGV4dChqc29uLmR1bXBzKGRhdGEsIGluZGVudD0yLCBzb3J0X2tleXM9VHJ1ZSkgKyAiXG4iLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHd0ZXh0KHBhdGg6IFBhdGgsIHRleHQ6IHN0cik6CiAgICBwYXRoLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwYXRoLndyaXRlX3RleHQodGV4dCwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiByZWwocGF0aDogUGF0aCk6CiAgICByZXR1cm4gc3RyKHBhdGgucmVsYXRpdmVfdG8oUk9PVCkpLnJlcGxhY2UoIlxcIiwgIi8iKQoKZGVmIGJ1aWxkX2NvbnRyb2xzKGNhcmRzLCB0aHJlc2hvbGQsIGdhdGUpOgogICAgYXR0ZW50aW9uID0gY2FyZHMuZ2V0KCJhdHRlbnRpb25fY2FyZF9jb3VudCIsIDApCiAgICBnYXRlX2dhcHMgPSBnYXRlLmdldCgiZ2FwX2NvdW50IiwgMCkKICAgIHRocmVzaG9sZF9nYXBzID0gdGhyZXNob2xkLmdldCgiZ2FwX2NvdW50IiwgMCkKICAgIGNvbnRyb2xzID0gW10KICAgIGZvciBpdGVtIGluIENPTlRST0xfQ0xBU1NFUzoKICAgICAgICBwcmVzc3VyZV9zY29yZSA9IDAKICAgICAgICBpZiBpdGVtWyJyaXNrX3R5cGUiXSBpbiB7Im92ZXJfcGVuYWx0eSIsICJ1bmRlcl9wZW5hbHR5IiwgImJvdW5kYXJ5X2dhcCIsICJvdmVyY2xhaW0ifToKICAgICAgICAgICAgcHJlc3N1cmVfc2NvcmUgKz0gaW50KGF0dGVudGlvbikKICAgICAgICBpZiBpdGVtWyJyaXNrX3R5cGUiXSBpbiB7ImdhdGVfbWFwcGluZyIsICJvdmVyX3BlbmFsdHkifToKICAgICAgICAgICAgcHJlc3N1cmVfc2NvcmUgKz0gaW50KGdhdGVfZ2FwcykKICAgICAgICBpZiBpdGVtWyJyaXNrX3R5cGUiXSBpbiB7ImJvdW5kYXJ5X2dhcCIsICJ1bmRlcl9wZW5hbHR5In06CiAgICAgICAgICAgIHByZXNzdXJlX3Njb3JlICs9IGludCh0aHJlc2hvbGRfZ2FwcykKCiAgICAgICAgY29udHJvbHMuYXBwZW5kKHsKICAgICAgICAgICAgInNjaGVtYSI6ICJ0YXUtc2NhbGluZy1vdmVyLXVuZGVyLXBlbmFsdHktY29udHJvbC12MC43LjYiLAogICAgICAgICAgICAqKml0ZW0sCiAgICAgICAgICAgICJwcmVzc3VyZV9zY29yZSI6IHByZXNzdXJlX3Njb3JlLAogICAgICAgICAgICAiY29udHJvbF9zdGF0dXMiOiAiUkVQT1JUX09OTFlfQ09OVFJPTF9ERUZJTkVEIiwKICAgICAgICAgICAgInRocmVzaG9sZF9jaGFuZ2VfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICAgICAiY29udHJvbF9yZXN1bHQiOiAicGVuZGluZ19mdXR1cmVfZHJ5X3J1biIsCiAgICAgICAgICAgICJldmlkZW5jZV9ib3VuZGFyeSI6ICJDb250cm9sIGlzIGJhc2VkIG9uIGxvY2FsIHJlcG9ydHMgYW5kIGV4cGxhbmF0aW9uIGNhcmRzIG9ubHk7IGl0IGlzIG5vdCBwcm9kdWN0LCBzaWxpY29uLCBtYW51ZmFjdHVyaW5nLCBvciB1bml2ZXJzYWwgVGF1IHZhbGlkYXRpb24uIiwKICAgICAgICB9KQogICAgcmV0dXJuIGNvbnRyb2xzCgpkZWYgY2hhcnRzKHN1bW1hcnkpOgogICAgcGF0aHMgPSBbXQogICAgdHJ5OgogICAgICAgIGltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZXhjOgogICAgICAgIHd0ZXh0KE9VVCAvICJjaGFydF9nZW5lcmF0aW9uX3NraXBwZWQudHh0Iiwgc3RyKGV4YykpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgY29udHJvbHMgPSBzdW1tYXJ5WyJjb250cm9scyJdCiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDExLCA0KSkKICAgIHBsdC5iYXIoW2NbImNvbnRyb2xfaWQiXSBmb3IgYyBpbiBjb250cm9sc10sIFtjWyJwcmVzc3VyZV9zY29yZSJdIGZvciBjIGluIGNvbnRyb2xzXSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MzUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJQcmVzc3VyZSBzY29yZSIpCiAgICBwbHQudGl0bGUoIk92ZXIvVW5kZXItUGVuYWx0eSBDb250cm9sIFByZXNzdXJlIikKICAgIHNhdmUoInBlbmFsdHlfY29udHJvbF9wcmVzc3VyZV9zY29yZXMucG5nIikKCiAgICB0eXBlcyA9IHt9CiAgICBmb3IgYyBpbiBjb250cm9sczoKICAgICAgICB0eXBlc1tjWyJyaXNrX3R5cGUiXV0gPSB0eXBlcy5nZXQoY1sicmlza190eXBlIl0sIDApICsgMQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdCh0eXBlcy5rZXlzKCkpLCBsaXN0KHR5cGVzLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjUsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJDb250cm9sIGNvdW50IikKICAgIHBsdC50aXRsZSgiUGVuYWx0eSBDb250cm9sIFJpc2sgVHlwZXMiKQogICAgc2F2ZSgicGVuYWx0eV9jb250cm9sX3Jpc2tfdHlwZXMucG5nIikKCiAgICBoZWFsdGggPSB7CiAgICAgICAgInJlbGVhc2VfcGFzc2VkIjogaW50KHN1bW1hcnlbInJlbGVhc2VfcGFzc2VkIl0pLAogICAgICAgICJjYXJkc19yZWFkeSI6IGludChzdW1tYXJ5WyJjYXJkc19yZWFkeSJdKSwKICAgICAgICAiY29udHJvbHNfZGVmaW5lZCI6IHN1bW1hcnlbImNvbnRyb2xfY291bnQiXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IGludChzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0pLAogICAgfQogICAgcGx0LmZpZ3VyZShmaWdzaXplPSg4LCA0KSkKICAgIHBsdC5iYXIobGlzdChoZWFsdGgua2V5cygpKSwgbGlzdChoZWFsdGgudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yMCwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIlZhbHVlIikKICAgIHBsdC50aXRsZSgiUGVuYWx0eSBDb250cm9scyBIZWFsdGgiKQogICAgc2F2ZSgicGVuYWx0eV9jb250cm9sc19oZWFsdGgucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIG1ha2VfbWQoc3VtbWFyeSk6CiAgICBsaW5lcyA9IFsKICAgICAgICAiIyBUYXUgU2NhbGluZyB2MC43LjYgT3Zlci9VbmRlci1QZW5hbHR5IE5lZ2F0aXZlIENvbnRyb2xzIiwKICAgICAgICAiIiwKICAgICAgICBmIkdlbmVyYXRlZDogYHtzdW1tYXJ5WydnZW5lcmF0ZWRfYXQnXX1gIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ29udHJvbCBSZXN1bHQiLAogICAgICAgICIiLAogICAgICAgIGYiLSBDb250cm9sIHN0YXR1czogYHtzdW1tYXJ5Wydjb250cm9sX3N0YXR1cyddfWAiLAogICAgICAgIGYiLSBSZWxlYXNlIHBhc3NlZDogYHtzdW1tYXJ5WydyZWxlYXNlX3Bhc3NlZCddfWAiLAogICAgICAgIGYiLSBCb3VuZGFyeSBjYXJkcyByZWFkeTogYHtzdW1tYXJ5WydjYXJkc19yZWFkeSddfWAiLAogICAgICAgIGYiLSBDb250cm9sIGNvdW50OiBge3N1bW1hcnlbJ2NvbnRyb2xfY291bnQnXX1gIiwKICAgICAgICBmIi0gVGhyZXNob2xkcyBjaGFuZ2VkOiBge3N1bW1hcnlbJ3RocmVzaG9sZHNfY2hhbmdlZCddfWAiLAogICAgICAgIGYiLSBDbGFzc2lmaWVyIGNoYW5nZWQ6IGB7c3VtbWFyeVsnY2xhc3NpZmllcl9jaGFuZ2VkJ119YCIsCiAgICAgICAgIiIsCiAgICAgICAgIiMjIENvbnRyb2xzIiwKICAgICAgICAiIiwKICAgICAgICAifCBDb250cm9sIHwgUmlzayB8IEJvdW5kYXJ5IHwgUHJlc3N1cmUgfCBFeHBlY3RlZCBiZWhhdmlvciB8IiwKICAgICAgICAifC0tLXwtLS18LS0tfC0tLTp8LS0tfCIsCiAgICBdCiAgICBmb3IgYyBpbiBzdW1tYXJ5WyJjb250cm9scyJdOgogICAgICAgIGxpbmVzLmFwcGVuZChmInwgYHtjWydjb250cm9sX2lkJ119YCB8IGB7Y1sncmlza190eXBlJ119YCB8IGB7Y1sndGFyZ2V0X2NsYXNzX2JvdW5kYXJ5J119YCB8IHtjWydwcmVzc3VyZV9zY29yZSddfSB8IGB7Y1snZXhwZWN0ZWRfYmVoYXZpb3InXX1gIHwiKQoKICAgIGxpbmVzICs9IFsKICAgICAgICAiIiwKICAgICAgICAiIyMgSW50ZXJwcmV0YXRpb24iLAogICAgICAgICIiLAogICAgICAgICJUaGVzZSBjb250cm9scyBkZWZpbmUgd2hhdCBtdXN0IGJlIHRlc3RlZCBiZWZvcmUgYW55IHRocmVzaG9sZCBkcnktcnVuIG9yIGNsYXNzaWZpZXItcG9saWN5IGNoYW5nZS4gVGhleSBkbyBub3QgcnVuIGEgdGhyZXNob2xkIGNoYW5nZSBhbmQgZG8gbm90IGFsdGVyIGNsYXNzaWZpZXIgYmVoYXZpb3IuIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgTmV4dCBUYXUgV29yayIsCiAgICAgICAgIiIsCiAgICAgICAgIjEuIENvbnZlcnQgdGhlc2UgY29udHJvbHMgaW50byByZXBvcnQtb25seSBzeW50aGV0aWMgc2NlbmFyaW9zLiIsCiAgICAgICAgIjIuIENvbXBhcmUgY3VycmVudCBUU0VLIG91dHB1dCBhZ2FpbnN0IGV4cGVjdGVkIG92ZXIvdW5kZXItcGVuYWx0eSBiZWhhdmlvci4iLAogICAgICAgICIzLiBTZXBhcmF0ZSB0cnVlIHJlamVjdGlvbiBmcm9tIG92ZXItcGVuYWx0eSBjb2xsYXBzZS4iLAogICAgICAgICI0LiBQcmVzZXJ2ZSB0aHJlc2hvbGQgYW5kIGNsYXNzaWZpZXIgbXV0YXRpb24gbG9ja3MgdW50aWwgZHJ5LXJ1biBldmlkZW5jZSBleGlzdHMuIiwKICAgICAgICAiIiwKICAgICAgICAiIyMgQ2hhcnRzIiwKICAgICAgICAiIiwKICAgIF0KICAgIGZvciBwIGluIHN1bW1hcnlbImNoYXJ0X3BhdGhzIl06CiAgICAgICAgbGluZXMuYXBwZW5kKGYiIVt7UGF0aChwKS5zdGVtfV0oe29zLnBhdGgucmVscGF0aChST09UIC8gcCwgT1VUKS5yZXBsYWNlKCdcXCcsICcvJyl9KSIpCiAgICAgICAgbGluZXMuYXBwZW5kKCIiKQogICAgbGluZXMgKz0gWyIjIyBCb3VuZGFyeSIsICIiLCBzdW1tYXJ5WyJib3VuZGFyeSJdLCAiIl0KICAgIHJldHVybiAiXG4iLmpvaW4obGluZXMpCgpkZWYgbWFpbigpOgogICAgY2FyZHMgPSByZWFkX2pzb24oQk9VTkRBUllfQ0FSRFMpCiAgICB0aHJlc2hvbGQgPSByZWFkX2pzb24oVEhSRVNIT0xEX1JFVklFVykKICAgIGdhdGUgPSByZWFkX2pzb24oR0FURV9BTEdFQlJBKQogICAgcmVsZWFzZSA9IHJlYWRfanNvbihSRUxFQVNFKQoKICAgIHJlbGVhc2VfcGFzc2VkID0gcmVsZWFzZS5nZXQoInBhc3NlZCIpIGlzIFRydWUgYW5kIGxlbihyZWxlYXNlLmdldCgiZmluZGluZ3MiLCBbXSkpID09IDAgYW5kIGxlbihyZWxlYXNlLmdldCgic3RlcF9mYWlsdXJlcyIsIFtdKSkgPT0gMAogICAgY2FyZHNfcmVhZHkgPSBjYXJkcy5nZXQoImNhcmRfc3RhdHVzIikgPT0gIlRTRUtfQk9VTkRBUllfQ0FSRFNfUkVBRFlfX05PX1RIUkVTSE9MRF9DSEFOR0UiCiAgICBjb250cm9scyA9IGJ1aWxkX2NvbnRyb2xzKGNhcmRzLCB0aHJlc2hvbGQsIGdhdGUpCgogICAgZm9yIGNvbnRyb2wgaW4gY29udHJvbHM6CiAgICAgICAgd2pzb24oT1VUIC8gImNvbnRyb2xzIiAvIGYie2NvbnRyb2xbJ2NvbnRyb2xfaWQnXX1fdjBfN182Lmpzb24iLCBjb250cm9sKQoKICAgIHN0YXR1cyA9ICJQRU5BTFRZX0NPTlRST0xTX0RFRklORURfX1JFUE9SVF9PTkxZX05PX01VVEFUSU9OIiBpZiByZWxlYXNlX3Bhc3NlZCBhbmQgY2FyZHNfcmVhZHkgZWxzZSAiUEVOQUxUWV9DT05UUk9MU19ORUVEX1JFVklFVyIKCiAgICBzdW1tYXJ5ID0gewogICAgICAgICJzY2hlbWEiOiAidGF1LXNjYWxpbmctb3Zlci11bmRlci1wZW5hbHR5LW5lZ2F0aXZlLWNvbnRyb2xzLXYwLjcuNiIsCiAgICAgICAgImdlbmVyYXRlZF9hdCI6IGRhdGV0aW1lLm5vdyh0aW1lem9uZS51dGMpLmlzb2Zvcm1hdCgpLAogICAgICAgICJjb250cm9sX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBib29sKHJlbGVhc2VfcGFzc2VkKSwKICAgICAgICAiY2FyZHNfcmVhZHkiOiBib29sKGNhcmRzX3JlYWR5KSwKICAgICAgICAiY29udHJvbF9jb3VudCI6IGxlbihjb250cm9scyksCiAgICAgICAgImNvbnRyb2xzIjogY29udHJvbHMsCiAgICAgICAgImF0dGVudGlvbl9jYXJkX2NvdW50IjogY2FyZHMuZ2V0KCJhdHRlbnRpb25fY2FyZF9jb3VudCIsIDApLAogICAgICAgICJ0aHJlc2hvbGRfZ2FwX2NvdW50IjogdGhyZXNob2xkLmdldCgiZ2FwX2NvdW50IiwgMCksCiAgICAgICAgImdhdGVfZ2FwX2NvdW50IjogZ2F0ZS5nZXQoImdhcF9jb3VudCIsIDApLAogICAgICAgICJyZXBsYXlfYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJ0aHJlc2hvbGRzX2NoYW5nZWQiOiBGYWxzZSwKICAgICAgICAiY2xhc3NpZmllcl9jaGFuZ2VkIjogRmFsc2UsCiAgICAgICAgIm5leHRfcmVjb21tZW5kYXRpb24iOiAiTW92ZSB0byB2MC43LjcgVGhyZXNob2xkIFNlbnNpdGl2aXR5IERyeS1SdW4gdXNpbmcgdGhlc2UgcmVwb3J0LW9ubHkgY29udHJvbHMuIiwKICAgICAgICAiYm91bmRhcnkiOiAiT3Zlci91bmRlci1wZW5hbHR5IG5lZ2F0aXZlIGNvbnRyb2xzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYW5hbHlzaXMgYXJ0aWZhY3RzLiBUaGV5IGRlZmluZSB0ZXN0IGNvbnRyb2xzIGJlZm9yZSB0aHJlc2hvbGQgZHJ5LXJ1bnMuIFRoZXkgZG8gbm90IGNyZWF0ZSBsaXZlIGFwcHJvdmFsLCBleGVjdXRlIHJlcGxheSBjb21tYW5kcywgY3JlYXRlIGJyYW5jaGVzLCBtdXRhdGUgY2xhc3NpZmllciBiZWhhdmlvciwgYXBwbHkgY2FsaWJyYXRpb24sIGNoYW5nZSB0aHJlc2hvbGRzLCBvciB2YWxpZGF0ZSBzaWxpY29uLCBwcm9kdWN0cywgbWFudWZhY3R1cmluZywgcHJvY2VzcyBub2RlcywgYmVuY2htYXJrIHN1cGVyaW9yaXR5LCBvciB1bml2ZXJzYWwgVGF1IFNjYWxpbmcgbGF3LiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gIm92ZXJfdW5kZXJfcGVuYWx0eV9uZWdhdGl2ZV9jb250cm9sc192MF83XzYuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X292ZXJfdW5kZXJfcGVuYWx0eV9uZWdhdGl2ZV9jb250cm9scy5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJvdmVyX3VuZGVyX3BlbmFsdHlfbmVnYXRpdmVfY29udHJvbHNfdjBfN182Lm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKICAgIHd0ZXh0KE9VVCAvICJsYXRlc3Rfb3Zlcl91bmRlcl9wZW5hbHR5X25lZ2F0aXZlX2NvbnRyb2xzLm1kIiwgbWFrZV9tZChzdW1tYXJ5KSkKCiAgICBwcmludChqc29uLmR1bXBzKHsKICAgICAgICAic2NoZW1hIjogc3VtbWFyeVsic2NoZW1hIl0sCiAgICAgICAgImNvbnRyb2xfc3RhdHVzIjogc3VtbWFyeVsiY29udHJvbF9zdGF0dXMiXSwKICAgICAgICAicmVsZWFzZV9wYXNzZWQiOiBzdW1tYXJ5WyJyZWxlYXNlX3Bhc3NlZCJdLAogICAgICAgICJjYXJkc19yZWFkeSI6IHN1bW1hcnlbImNhcmRzX3JlYWR5Il0sCiAgICAgICAgImNvbnRyb2xfY291bnQiOiBzdW1tYXJ5WyJjb250cm9sX2NvdW50Il0sCiAgICAgICAgInRocmVzaG9sZHNfY2hhbmdlZCI6IHN1bW1hcnlbInRocmVzaG9sZHNfY2hhbmdlZCJdLAogICAgICAgICJjbGFzc2lmaWVyX2NoYW5nZWQiOiBzdW1tYXJ5WyJjbGFzc2lmaWVyX2NoYW5nZWQiXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJleGVjdXRvcl9yYW4iOiBzdW1tYXJ5WyJleGVjdXRvcl9yYW4iXSwKICAgICAgICAibXV0YXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IHN1bW1hcnlbImFwcGxpY2F0aW9uX2FsbG93ZWQiXSwKICAgICAgICAiY2FsaWJyYXRpb25fYXBwbGllZCI6IHN1bW1hcnlbImNhbGlicmF0aW9uX2FwcGxpZWQiXSwKICAgICAgICAiY2hhcnRfY291bnQiOiBsZW4oc3VtbWFyeVsiY2hhcnRfcGF0aHMiXSksCiAgICAgICAgInJlcG9ydCI6ICJyZXBvcnRzL3BlbmFsdHlfY29udHJvbHMvbGF0ZXN0X292ZXJfdW5kZXJfcGVuYWx0eV9uZWdhdGl2ZV9jb250cm9scy5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT / "reports" / "penalty_controls" / "README.md", """# Penalty Control Reports

Current layer: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**

## Purpose

This folder stores report-only over/under-penalty negative controls for TSEK boundaries.

## Primary command

```powershell
python scripts/benchmarks/generate_over_under_penalty_controls.py
```

## README Update Rule

Update this mini README whenever penalty controls, threshold dry-run assumptions, or TSEK boundary control logic changes.

Boundary: penalty controls are local classifier-governance analysis artifacts only.
""")

write(ROOT / "visuals" / "penalty_controls" / "README.md", """# Penalty Control Visuals

Current layer: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**

## Purpose

This folder stores charts summarizing TSEK over/under-penalty controls.

## README Update Rule

Update this mini README whenever penalty-control chart names or meanings change.

Boundary: penalty-control visuals are local classifier-governance diagnostics only.
""")

write(ROOT / "visuals" / "penalty_controls" / "v0_7_6" / "README.md", """# v0.7.6 Penalty Control Charts

Expected charts:

- `penalty_control_pressure_scores.png`
- `penalty_control_risk_types.png`
- `penalty_controls_health.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local penalty-control diagnostics only.
""")

p = ROOT / "README.md"
backup(p, "readme")
r = read(p)
r = re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.7\.5[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**", r)
r = re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.7\.4[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.7.5 - TSEK Boundary Explanation Cards**", r)
r = re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.7\.5 \|", "| Current checkpoint | TAU-SCALING-SA v0.7.6 |", r)
r = r.replace("| Task routing matrix | geometry-aware / v0.7.5-ready |", "| Task routing matrix | geometry-aware / v0.7.6-ready |")
r = r.replace("| Agent contract version sync | current / v0.7.5 |", "| Agent contract version sync | current / v0.7.6 |")

if "| Over/under-penalty controls |" not in r:
    r = r.replace("| TSEK boundary card charts | `visuals/tsek_boundary_cards/v0_7_5/` |\n",
                  "| TSEK boundary card charts | `visuals/tsek_boundary_cards/v0_7_5/` |\n| Over/under-penalty controls | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` |\n| Penalty control charts | `visuals/penalty_controls/v0_7_6/` |\n")

if "python scripts/benchmarks/generate_over_under_penalty_controls.py" not in r:
    r = r.replace("python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython scripts/release/validate_release.py",
                  "python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython scripts/benchmarks/generate_over_under_penalty_controls.py\npython scripts/release/validate_release.py")

if "    penalty_controls/" not in r:
    r = r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    penalty_controls/\n")
    r = r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    penalty_controls/\n")

section = """## Over/Under-Penalty Negative Controls v0.7.6

v0.7.6 defines report-only controls for TSEK over-penalty, under-penalty, boundary-gap, and overclaim risks.

Primary command:

```powershell
python scripts/benchmarks/generate_over_under_penalty_controls.py
```

Primary outputs:

```text
reports/penalty_controls/latest_over_under_penalty_negative_controls.json
reports/penalty_controls/latest_over_under_penalty_negative_controls.md
reports/penalty_controls/controls/
visuals/penalty_controls/v0_7_6/
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

Boundary: over/under-penalty negative controls are local classifier-governance analysis artifacts. They define test controls before threshold dry-runs. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""

if "## Over/Under-Penalty Negative Controls v0.7.6" not in r:
    r = r.replace("## TSEK Boundary Explanation Cards v0.7.5", section + "## TSEK Boundary Explanation Cards v0.7.5", 1)

lesson = "| L-058 | v0.7.5 generated boundary cards and flagged every class boundary for attention. | Explanation cards alone still do not test whether boundaries over-penalize or under-penalize claims. | TSEK boundary cards must be followed by report-only over/under-penalty controls before threshold dry-runs or classifier tuning. |"
if "L-058" not in r:
    r = r.replace("| L-057 | v0.7.4 reviewed TSEK threshold boundaries without changing thresholds. | Boundary review identifies visibility, but humans and agents need class-level explanation cards before pressure testing penalties. | TSEK class boundaries must be explained as cards before over/under-penalty controls or threshold dry-runs. |\n",
                  "| L-057 | v0.7.4 reviewed TSEK threshold boundaries without changing thresholds. | Boundary review identifies visibility, but humans and agents need class-level explanation cards before pressure testing penalties. | TSEK class boundaries must be explained as cards before over/under-penalty controls or threshold dry-runs. |\n" + lesson + "\n")

if "| v0.7.6 |" not in r:
    r = r.replace("| v0.7.5 | TSEK boundary explanation cards; explains each class boundary before penalty controls. |\n",
                  "| v0.7.5 | TSEK boundary explanation cards; explains each class boundary before penalty controls. |\n| v0.7.6 | Over/under-penalty negative controls; defines report-only controls before threshold dry-runs. |\n")

r = re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.7.7 - Threshold Sensitivity Dry-Run**

Recommended goals:

- Run report-only threshold sensitivity against v0.7.6 controls.
- Compare current class outcomes against over/under-penalty expectations.
- Preserve no-classifier-mutation lock.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p, r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.7\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls**"),
]:
    p = ROOT / name
    backup(p, name.replace("/", "_"))
    s = read(p)
    s = re.sub(pattern, repl, s)
    if name == "AGENTS.md" and "generate_over_under_penalty_controls.py" not in s:
        s = s.replace("python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython -m unittest discover -s tests",
                      "python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py\npython scripts/benchmarks/generate_over_under_penalty_controls.py\npython -m unittest discover -s tests")
        s = s.replace("| TSEK boundary card patch | `reports/tsek_boundary_cards/`, `visuals/tsek_boundary_cards/`, threshold review | boundary cards + release validator; no mutation |\n",
                      "| TSEK boundary card patch | `reports/tsek_boundary_cards/`, `visuals/tsek_boundary_cards/`, threshold review | boundary cards + release validator; no mutation |\n| Penalty controls patch | `reports/penalty_controls/`, `visuals/penalty_controls/`, TSEK boundary cards | report-only penalty controls + release validator; no mutation |\n")
    if name.endswith("task_routing_matrix.md") and "| Penalty controls patch |" not in s:
        s = s.replace("| TSEK boundary card patch | inner | explanation | classifier | threshold review + TSEK classes | boundary cards + charts + release validator | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` |\n",
                      "| TSEK boundary card patch | inner | explanation | classifier | threshold review + TSEK classes | boundary cards + charts + release validator | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` |\n| Penalty controls patch | inner | analysis | classifier | TSEK boundary cards + threshold review | report-only controls + charts + release validator | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` |\n")
    write(p, s)

p = ROOT / "rcc" / "nexus" / "route_map.json"
backup(p, "route_map")
try:
    route = json.loads(read(p))
except Exception:
    route = {}
route["version"] = "v0.7.6"
route["updated_at"] = NOW
route.setdefault("v0_7_routes", {})["over_under_penalty_negative_controls"] = {
    "read_first": ["reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.json", "reports/tsek_threshold_review/latest_tsek_threshold_boundary_review.json"],
    "validate": ["python scripts/benchmarks/generate_over_under_penalty_controls.py", "python scripts/release/validate_release.py"],
    "evidence": ["reports/penalty_controls/latest_over_under_penalty_negative_controls.md", "visuals/penalty_controls/v0_7_6/"],
    "mutation_lock": "Report-only penalty controls; no classifier change, threshold change, branch creation, or mutation."
}
write(p, json.dumps(route, indent=2, sort_keys=True) + "\n")

p = ROOT / "docs" / "benchmarks" / "benchmark_atlas.md"
backup(p, "atlas")
t = read(p)
if "| v0.7.6 | Over/under-penalty negative controls |" not in t:
    t = t.replace("| v0.7.5 | TSEK boundary explanation cards | `python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py` | Creates class-boundary explanation cards without changing thresholds | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` | `visuals/tsek_boundary_cards/v0_7_5/` |\n",
                  "| v0.7.5 | TSEK boundary explanation cards | `python scripts/benchmarks/generate_tsek_boundary_explanation_cards.py` | Creates class-boundary explanation cards without changing thresholds | `reports/tsek_boundary_cards/latest_tsek_boundary_explanation_cards.md` | `visuals/tsek_boundary_cards/v0_7_5/` |\n| v0.7.6 | Over/under-penalty negative controls | `python scripts/benchmarks/generate_over_under_penalty_controls.py` | Defines report-only controls before threshold dry-runs | `reports/penalty_controls/latest_over_under_penalty_negative_controls.md` | `visuals/penalty_controls/v0_7_6/` |\n")
write(p, t)

write(ROOT / "docs" / "release_notes" / "tau_scaling_v0_7_6_penalty_controls.md", f"""# TAU-SCALING-SA v0.7.6 - Over/Under-Penalty Negative Controls

Generated: {NOW}

## Purpose

Define report-only controls for over-penalty, under-penalty, boundary-gap, and overclaim risks before threshold dry-runs.

## Boundary

Over/under-penalty negative controls are local classifier-governance analysis artifacts only. They do not create live approval, execute replay commands, create branches, mutate classifier behavior, apply calibration, change thresholds, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")

print("v0.7.6 patch written")
