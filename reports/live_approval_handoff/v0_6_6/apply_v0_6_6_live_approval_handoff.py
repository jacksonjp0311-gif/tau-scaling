
from __future__ import annotations
import base64, json, re
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path.cwd(); NOW=datetime.now(timezone.utc).isoformat()
def read(p): return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
def write(p,s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s, encoding="utf-8")
def backup(p,label):
    if p.exists():
        d=ROOT/"reports"/"live_approval_handoff"/"v0_6_6"/"backups"/f"{p.name}_before_v0_6_6_{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
        d.parent.mkdir(parents=True, exist_ok=True); d.write_text(read(p), encoding="utf-8")
write(ROOT/"scripts"/"benchmarks"/"run_live_approval_handoff_check.py", base64.b64decode("CmZyb20gX19mdXR1cmVfXyBpbXBvcnQgYW5ub3RhdGlvbnMKaW1wb3J0IGpzb24sIG9zCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZQpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKClJPT1QgPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50c1syXQpGSVhUVVJFUyA9IFJPT1QgLyAicmVwb3J0cyIgLyAiYXBwcm92YWxfZml4dHVyZXMiIC8gImxhdGVzdF9hcHByb3ZhbF9maXh0dXJlX3ZhbGlkYXRvci5qc29uIgpMSVZFX0RJUiA9IFJPT1QgLyAicmVwb3J0cyIgLyAiaHVtYW5fYXBwcm92YWwiIC8gImxpdmUiCk9VVCA9IFJPT1QgLyAicmVwb3J0cyIgLyAibGl2ZV9hcHByb3ZhbF9oYW5kb2ZmIgpWSVMgPSBST09UIC8gInZpc3VhbHMiIC8gImxpdmVfYXBwcm92YWxfaGFuZG9mZiIgLyAidjBfNl82IgoKZGVmIHJqc29uKHApOgogICAgcmV0dXJuIGpzb24ubG9hZHMocC5yZWFkX3RleHQoZW5jb2Rpbmc9InV0Zi04IikpCgpkZWYgd2pzb24ocCwgeCk6CiAgICBwLnBhcmVudC5ta2RpcihwYXJlbnRzPVRydWUsIGV4aXN0X29rPVRydWUpCiAgICBwLndyaXRlX3RleHQoanNvbi5kdW1wcyh4LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpICsgIlxuIiwgZW5jb2Rpbmc9InV0Zi04IikKCmRlZiB3dGV4dChwLCBzKToKICAgIHAucGFyZW50Lm1rZGlyKHBhcmVudHM9VHJ1ZSwgZXhpc3Rfb2s9VHJ1ZSkKICAgIHAud3JpdGVfdGV4dChzLCBlbmNvZGluZz0idXRmLTgiKQoKZGVmIHJlbChwKToKICAgIHJldHVybiBzdHIocC5yZWxhdGl2ZV90byhST09UKSkucmVwbGFjZSgiXFwiLCAiLyIpCgpkZWYgZmluZF9saXZlX2FwcHJvdmFsKCk6CiAgICBpZiBub3QgTElWRV9ESVIuZXhpc3RzKCk6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIGNhbmRpZGF0ZXMgPSBzb3J0ZWQoTElWRV9ESVIuZ2xvYigiKi5qc29uIikpCiAgICBmb3IgcCBpbiBjYW5kaWRhdGVzOgogICAgICAgIHRyeToKICAgICAgICAgICAgZGF0YSA9IHJqc29uKHApCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgY29udGludWUKICAgICAgICBpZiBkYXRhLmdldCgiZml4dHVyZV9vbmx5IikgaXMgVHJ1ZToKICAgICAgICAgICAgY29udGludWUKICAgICAgICBpZiBkYXRhLmdldCgiYXBwcm92YWxfZGVjaXNpb24iKSBpbiBbIkFQUFJPVkVfUkVQTEFZX09OTFkiLCAiREVOWSIsICJSRVFVRVNUX01PUkVfRVZJREVOQ0UiXToKICAgICAgICAgICAgcmV0dXJuIHAKICAgIHJldHVybiBOb25lCgpkZWYgdmFsaWRhdGVfbGl2ZShkYXRhKToKICAgIGlmIG5vdCBkYXRhOgogICAgICAgIHJldHVybiB7CiAgICAgICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiOiBGYWxzZSwKICAgICAgICAgICAgImxpdmVfYXBwcm92YWxfdmFsaWQiOiBGYWxzZSwKICAgICAgICAgICAgImFwcHJvdmFsX2RlY2lzaW9uIjogIk1JU1NJTkciLAogICAgICAgICAgICAidmFsaWRhdGlvbl9zdGF0dXMiOiAiTElWRV9BUFBST1ZBTF9NSVNTSU5HIiwKICAgICAgICAgICAgInJlYXNvbiI6ICJObyBsaXZlIGFwcHJvdmFsIGFydGlmYWN0IHdhcyBmb3VuZCBpbiByZXBvcnRzL2h1bWFuX2FwcHJvdmFsL2xpdmUvLiIsCiAgICAgICAgfQoKICAgIGxvY2tzID0gZGF0YS5nZXQoImV4cGxpY2l0X2xvY2tzIiwge30pIG9yIHt9CiAgICBkZWNpc2lvbiA9IGRhdGEuZ2V0KCJhcHByb3ZhbF9kZWNpc2lvbiIpCiAgICByZXF1aXJlZF9zdGF0ZW1lbnQgPSBzdHIoZGF0YS5nZXQoInJlcXVpcmVkX3N0YXRlbWVudCIsICIiKSkKICAgIG9rID0gKAogICAgICAgIGRhdGEuZ2V0KCJzY2hlbWEiKSA9PSAidGF1LXNjYWxpbmctaHVtYW4tYXBwcm92YWwtYXJ0aWZhY3QtdjAuNi4yIgogICAgICAgIGFuZCBkYXRhLmdldCgiZml4dHVyZV9vbmx5IikgaXMgbm90IFRydWUKICAgICAgICBhbmQgZGVjaXNpb24gaW4gWyJBUFBST1ZFX1JFUExBWV9PTkxZIiwgIkRFTlkiLCAiUkVRVUVTVF9NT1JFX0VWSURFTkNFIl0KICAgICAgICBhbmQgYm9vbChzdHIoZGF0YS5nZXQoImFwcHJvdmVyIiwgIiIpKS5zdHJpcCgpKQogICAgICAgIGFuZCBib29sKHN0cihkYXRhLmdldCgiYXBwcm92YWxfdGltZXN0YW1wIiwgIiIpKS5zdHJpcCgpKQogICAgICAgIGFuZCBkYXRhLmdldCgic2NvcGUiKSA9PSAiY2FuZGlkYXRlX2JyYW5jaF9yZXBsYXlfb25seSIKICAgICAgICBhbmQgImRvZXMgbm90IGF1dGhvcml6ZSBjbGFzc2lmaWVyIG11dGF0aW9uIiBpbiByZXF1aXJlZF9zdGF0ZW1lbnQKICAgICAgICBhbmQgbG9ja3MuZ2V0KCJydW50aW1lX211dGF0aW9uX2FsbG93ZWQiKSBpcyBGYWxzZQogICAgICAgIGFuZCBsb2Nrcy5nZXQoImNsYXNzaWZpZXJfbXV0YXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgiYXBwbGljYXRpb25fYWxsb3dlZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgiY2FsaWJyYXRpb25fYXBwbGllZCIpIGlzIEZhbHNlCiAgICAgICAgYW5kIGxvY2tzLmdldCgicG9saWN5X2VuZm9yY2VkIikgaXMgRmFsc2UKICAgICkKCiAgICBpZiBvayBhbmQgZGVjaXNpb24gPT0gIkFQUFJPVkVfUkVQTEFZX09OTFkiOgogICAgICAgIHN0YXR1cyA9ICJMSVZFX0FQUFJPVkFMX1ZBTElEX0ZPUl9SRVBMQVlfT05MWSIKICAgICAgICByZWFzb24gPSAiQSBub24tZml4dHVyZSBsaXZlIGFwcHJvdmFsIGFydGlmYWN0IGV4cGxpY2l0bHkgYXBwcm92ZXMgcmVwbGF5IG9ubHkgd2hpbGUgcHJlc2VydmluZyBhbGwgbXV0YXRpb24vYXBwbGljYXRpb24gbG9ja3MuIgogICAgZWxpZiBvayBhbmQgZGVjaXNpb24gPT0gIkRFTlkiOgogICAgICAgIHN0YXR1cyA9ICJMSVZFX0FQUFJPVkFMX0RFTklFU19SRVBMQVkiCiAgICAgICAgcmVhc29uID0gIkEgdmFsaWQgbm9uLWZpeHR1cmUgbGl2ZSBhcHByb3ZhbCBhcnRpZmFjdCBkZW5pZXMgcmVwbGF5LiIKICAgIGVsaWYgb2sgYW5kIGRlY2lzaW9uID09ICJSRVFVRVNUX01PUkVfRVZJREVOQ0UiOgogICAgICAgIHN0YXR1cyA9ICJMSVZFX0FQUFJPVkFMX1JFUVVFU1RTX01PUkVfRVZJREVOQ0UiCiAgICAgICAgcmVhc29uID0gIkEgdmFsaWQgbm9uLWZpeHR1cmUgbGl2ZSBhcHByb3ZhbCBhcnRpZmFjdCByZXF1ZXN0cyBtb3JlIGV2aWRlbmNlIGJlZm9yZSByZXBsYXkuIgogICAgZWxzZToKICAgICAgICBzdGF0dXMgPSAiTElWRV9BUFBST1ZBTF9JTlZBTElEIgogICAgICAgIHJlYXNvbiA9ICJBIGxpdmUgYXBwcm92YWwgYXJ0aWZhY3Qgd2FzIGZvdW5kLCBidXQgaXQgZGlkIG5vdCBzYXRpc2Z5IGFsbCBzY2hlbWEsIGlkZW50aXR5LCBzdGF0ZW1lbnQsIGFuZCBsb2NrIHJlcXVpcmVtZW50cy4iCgogICAgcmV0dXJuIHsKICAgICAgICAibGl2ZV9hcHByb3ZhbF9wcmVzZW50IjogVHJ1ZSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF92YWxpZCI6IGJvb2wob2spLAogICAgICAgICJhcHByb3ZhbF9kZWNpc2lvbiI6IGRlY2lzaW9uLAogICAgICAgICJ2YWxpZGF0aW9uX3N0YXR1cyI6IHN0YXR1cywKICAgICAgICAicmVhc29uIjogcmVhc29uLAogICAgfQoKZGVmIGNoYXJ0cyhzdW1tYXJ5KToKICAgIHBhdGhzID0gW10KICAgIHRyeToKICAgICAgICBpbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgd3RleHQoT1VUIC8gImNoYXJ0X2dlbmVyYXRpb25fc2tpcHBlZC50eHQiLCBzdHIoZSkpCiAgICAgICAgcmV0dXJuIHBhdGhzCiAgICBWSVMubWtkaXIocGFyZW50cz1UcnVlLCBleGlzdF9vaz1UcnVlKQoKICAgIGRlZiBzYXZlKG5hbWUpOgogICAgICAgIHAgPSBWSVMgLyBuYW1lCiAgICAgICAgcGx0LnRpZ2h0X2xheW91dCgpCiAgICAgICAgcGx0LnNhdmVmaWcocCwgZHBpPTE4MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgICAgICBwbHQuY2xvc2UoKQogICAgICAgIHBhdGhzLmFwcGVuZChyZWwocCkpCgogICAgZ2F0ZXMgPSB7CiAgICAgICAgImxpdmVfcHJlc2VudCI6IGludChzdW1tYXJ5WyJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiXSksCiAgICAgICAgImxpdmVfdmFsaWQiOiBpbnQoc3VtbWFyeVsibGl2ZV9hcHByb3ZhbF92YWxpZCJdKSwKICAgICAgICAiZml4dHVyZV9taXN1c2UiOiBpbnQoc3VtbWFyeVsiZml4dHVyZV9taXN1c2VfZGV0ZWN0ZWQiXSksCiAgICAgICAgInJlcGxheV9hbGxvd2VkIjogaW50KHN1bW1hcnlbInJlcGxheV9hbGxvd2VkIl0pLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogaW50KHN1bW1hcnlbIm11dGF0aW9uX2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KGdhdGVzLmtleXMoKSksIGxpc3QoZ2F0ZXMudmFsdWVzKCkpKQogICAgcGx0Lnh0aWNrcyhyb3RhdGlvbj0yNSwgaGE9InJpZ2h0IikKICAgIHBsdC55bGFiZWwoIkJvb2xlYW4gc3RhdGUiKQogICAgcGx0LnRpdGxlKCJMaXZlIEFwcHJvdmFsIEhhbmRvZmYgR2F0ZSIpCiAgICBzYXZlKCJsaXZlX2FwcHJvdmFsX2hhbmRvZmZfZ2F0ZS5wbmciKQoKICAgIGZpeHR1cmVfc3RhdGUgPSB7CiAgICAgICAgImZpeHR1cmVzX3ZhbGlkIjogaW50KHN1bW1hcnlbImZpeHR1cmVzX3ZhbGlkYXRlZCJdKSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF9wcmVzZW50IjogaW50KHN1bW1hcnlbImxpdmVfYXBwcm92YWxfcHJlc2VudCJdKSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBpbnQoc3VtbWFyeVsicmVwbGF5X2FsbG93ZWQiXSksCiAgICB9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDgsIDQpKQogICAgcGx0LmJhcihsaXN0KGZpeHR1cmVfc3RhdGUua2V5cygpKSwgbGlzdChmaXh0dXJlX3N0YXRlLnZhbHVlcygpKSkKICAgIHBsdC54dGlja3Mocm90YXRpb249MjAsIGhhPSJyaWdodCIpCiAgICBwbHQueWxhYmVsKCJCb29sZWFuIHN0YXRlIikKICAgIHBsdC50aXRsZSgiRml4dHVyZSB2cyBMaXZlIEFwcHJvdmFsIFNlcGFyYXRpb24iKQogICAgc2F2ZSgiZml4dHVyZV92c19saXZlX2FwcHJvdmFsLnBuZyIpCgogICAgc3RhdHVzID0ge3N1bW1hcnlbImhhbmRvZmZfc3RhdHVzIl06IDF9CiAgICBwbHQuZmlndXJlKGZpZ3NpemU9KDksIDQpKQogICAgcGx0LmJhcihsaXN0KHN0YXR1cy5rZXlzKCkpLCBsaXN0KHN0YXR1cy52YWx1ZXMoKSkpCiAgICBwbHQueHRpY2tzKHJvdGF0aW9uPTI1LCBoYT0icmlnaHQiKQogICAgcGx0LnlsYWJlbCgiQ291bnQiKQogICAgcGx0LnRpdGxlKCJMaXZlIEFwcHJvdmFsIEhhbmRvZmYgU3RhdHVzIikKICAgIHNhdmUoImxpdmVfYXBwcm92YWxfaGFuZG9mZl9zdGF0dXMucG5nIikKICAgIHJldHVybiBwYXRocwoKZGVmIHJlcG9ydChzKToKICAgIGxpbmVzID0gWwogICAgICAgICIjIFRhdSBTY2FsaW5nIHYwLjYuNiBMaXZlIEFwcHJvdmFsIEhhbmRvZmYgQ2hlY2siLAogICAgICAgICIiLAogICAgICAgIGYiR2VuZXJhdGVkOiBge3NbJ2dlbmVyYXRlZF9hdCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBIYW5kb2ZmIFJlc3VsdCIsCiAgICAgICAgIiIsCiAgICAgICAgZiItIEhhbmRvZmYgc3RhdHVzOiBge3NbJ2hhbmRvZmZfc3RhdHVzJ119YCIsCiAgICAgICAgZiItIExpdmUgYXBwcm92YWwgcGF0aDogYHtzWydsaXZlX2FwcHJvdmFsX3BhdGgnXX1gIiwKICAgICAgICBmIi0gTGl2ZSBhcHByb3ZhbCBwcmVzZW50OiBge3NbJ2xpdmVfYXBwcm92YWxfcHJlc2VudCddfWAiLAogICAgICAgIGYiLSBMaXZlIGFwcHJvdmFsIHZhbGlkOiBge3NbJ2xpdmVfYXBwcm92YWxfdmFsaWQnXX1gIiwKICAgICAgICBmIi0gRml4dHVyZSBtaXN1c2UgZGV0ZWN0ZWQ6IGB7c1snZml4dHVyZV9taXN1c2VfZGV0ZWN0ZWQnXX1gIiwKICAgICAgICBmIi0gQXBwcm92YWwgZGVjaXNpb246IGB7c1snYXBwcm92YWxfZGVjaXNpb24nXX1gIiwKICAgICAgICBmIi0gUmVwbGF5IGFsbG93ZWQ6IGB7c1sncmVwbGF5X2FsbG93ZWQnXX1gIiwKICAgICAgICBmIi0gQnJhbmNoIGNyZWF0ZWQ6IGB7c1snYnJhbmNoX2NyZWF0ZWQnXX1gIiwKICAgICAgICBmIi0gTXV0YXRpb24gYWxsb3dlZDogYHtzWydtdXRhdGlvbl9hbGxvd2VkJ119YCIsCiAgICAgICAgZiItIEFwcGxpY2F0aW9uIGFsbG93ZWQ6IGB7c1snYXBwbGljYXRpb25fYWxsb3dlZCddfWAiLAogICAgICAgICIiLAogICAgICAgICIjIyBSZWFzb24iLAogICAgICAgICIiLAogICAgICAgIHNbInJlYXNvbiJdLAogICAgICAgICIiLAogICAgICAgICIjIyBDaGFydHMiLAogICAgICAgICIiLAogICAgXQogICAgZm9yIHAgaW4gc1siY2hhcnRfcGF0aHMiXToKICAgICAgICBsaW5lcy5hcHBlbmQoZiIhW3tQYXRoKHApLnN0ZW19XSh7b3MucGF0aC5yZWxwYXRoKFJPT1QgLyBwLCBPVVQpLnJlcGxhY2UoJ1xcJywgJy8nKX0pIikKICAgICAgICBsaW5lcy5hcHBlbmQoIiIpCiAgICBsaW5lcyArPSBbIiMjIEJvdW5kYXJ5IiwgIiIsIHNbImJvdW5kYXJ5Il0sICIiXQogICAgcmV0dXJuICJcbiIuam9pbihsaW5lcykKCmRlZiBtYWluKCk6CiAgICBmaXh0dXJlcyA9IHJqc29uKEZJWFRVUkVTKQogICAgZml4dHVyZV9wYXRocyA9IFtST09UIC8gcCBmb3IgcCBpbiBmaXh0dXJlcy5nZXQoImZpeHR1cmVfcGF0aHMiLCBbXSldCiAgICBmaXh0dXJlX21pc3VzZSA9IGFueShzdHIocCkuc3RhcnRzd2l0aChzdHIoTElWRV9ESVIpKSBmb3IgcCBpbiBmaXh0dXJlX3BhdGhzKQoKICAgIGxpdmVfcGF0aCA9IGZpbmRfbGl2ZV9hcHByb3ZhbCgpCiAgICBsaXZlX2RhdGEgPSByanNvbihsaXZlX3BhdGgpIGlmIGxpdmVfcGF0aCBlbHNlIE5vbmUKICAgIGxpdmUgPSB2YWxpZGF0ZV9saXZlKGxpdmVfZGF0YSkKCiAgICBmaXh0dXJlc192YWxpZGF0ZWQgPSBmaXh0dXJlcy5nZXQoImZpeHR1cmVfc3RhdHVzIikgPT0gIkZJWFRVUkVTX1ZBTElEQVRFRF9fTk9fTElWRV9BUFBST1ZBTF9DUkVBVEVEIgogICAgcmVwbGF5X2FsbG93ZWQgPSBsaXZlWyJsaXZlX2FwcHJvdmFsX3ZhbGlkIl0gYW5kIGxpdmVbImFwcHJvdmFsX2RlY2lzaW9uIl0gPT0gIkFQUFJPVkVfUkVQTEFZX09OTFkiIGFuZCBub3QgZml4dHVyZV9taXN1c2UKCiAgICBpZiByZXBsYXlfYWxsb3dlZDoKICAgICAgICBoYW5kb2ZmX3N0YXR1cyA9ICJMSVZFX0FQUFJPVkFMX0hBTkRPRkZfVkFMSURfRk9SX1JFUExBWV9PTkxZIgogICAgZWxpZiBmaXh0dXJlX21pc3VzZToKICAgICAgICBoYW5kb2ZmX3N0YXR1cyA9ICJIQU5ET0ZGX0JMT0NLRURfX0ZJWFRVUkVfTUlTVVNFX0RFVEVDVEVEIgogICAgZWxpZiBub3QgbGl2ZVsibGl2ZV9hcHByb3ZhbF9wcmVzZW50Il06CiAgICAgICAgaGFuZG9mZl9zdGF0dXMgPSAiSEFORE9GRl9CTE9DS0VEX19OT19MSVZFX0FQUFJPVkFMIgogICAgZWxpZiBsaXZlWyJ2YWxpZGF0aW9uX3N0YXR1cyJdID09ICJMSVZFX0FQUFJPVkFMX0RFTklFU19SRVBMQVkiOgogICAgICAgIGhhbmRvZmZfc3RhdHVzID0gIkhBTkRPRkZfQkxPQ0tFRF9fTElWRV9ERU5JQUwiCiAgICBlbGlmIGxpdmVbInZhbGlkYXRpb25fc3RhdHVzIl0gPT0gIkxJVkVfQVBQUk9WQUxfUkVRVUVTVFNfTU9SRV9FVklERU5DRSI6CiAgICAgICAgaGFuZG9mZl9zdGF0dXMgPSAiSEFORE9GRl9CTE9DS0VEX19NT1JFX0VWSURFTkNFX1JFUVVFU1RFRCIKICAgIGVsc2U6CiAgICAgICAgaGFuZG9mZl9zdGF0dXMgPSAiSEFORE9GRl9CTE9DS0VEX19MSVZFX0FQUFJPVkFMX0lOVkFMSUQiCgogICAgc3VtbWFyeSA9IHsKICAgICAgICAic2NoZW1hIjogInRhdS1zY2FsaW5nLWxpdmUtYXBwcm92YWwtaGFuZG9mZi1jaGVjay12MC42LjYiLAogICAgICAgICJnZW5lcmF0ZWRfYXQiOiBkYXRldGltZS5ub3codGltZXpvbmUudXRjKS5pc29mb3JtYXQoKSwKICAgICAgICAiaW5wdXRfZml4dHVyZV92YWxpZGF0b3IiOiByZWwoRklYVFVSRVMpLAogICAgICAgICJsaXZlX2FwcHJvdmFsX2RpcmVjdG9yeSI6IHJlbChMSVZFX0RJUiksCiAgICAgICAgImxpdmVfYXBwcm92YWxfcGF0aCI6IHJlbChsaXZlX3BhdGgpIGlmIGxpdmVfcGF0aCBlbHNlICJNSVNTSU5HIiwKICAgICAgICAiZml4dHVyZXNfdmFsaWRhdGVkIjogYm9vbChmaXh0dXJlc192YWxpZGF0ZWQpLAogICAgICAgICJmaXh0dXJlX21pc3VzZV9kZXRlY3RlZCI6IGJvb2woZml4dHVyZV9taXN1c2UpLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiOiBsaXZlWyJsaXZlX2FwcHJvdmFsX3ByZXNlbnQiXSwKICAgICAgICAibGl2ZV9hcHByb3ZhbF92YWxpZCI6IGxpdmVbImxpdmVfYXBwcm92YWxfdmFsaWQiXSwKICAgICAgICAiYXBwcm92YWxfZGVjaXNpb24iOiBsaXZlWyJhcHByb3ZhbF9kZWNpc2lvbiJdLAogICAgICAgICJoYW5kb2ZmX3N0YXR1cyI6IGhhbmRvZmZfc3RhdHVzLAogICAgICAgICJyZWFzb24iOiBsaXZlWyJyZWFzb24iXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBib29sKHJlcGxheV9hbGxvd2VkKSwKICAgICAgICAiYnJhbmNoX2NyZWF0ZWQiOiBGYWxzZSwKICAgICAgICAiYnJhbmNoX2NyZWF0aW9uX2FsbG93ZWQiOiBGYWxzZSwKICAgICAgICAiYXBwbGljYXRpb25fYWxsb3dlZCI6IEZhbHNlLAogICAgICAgICJtdXRhdGlvbl9hbGxvd2VkIjogRmFsc2UsCiAgICAgICAgInBvbGljeV9lbmZvcmNlZCI6IEZhbHNlLAogICAgICAgICJjYWxpYnJhdGlvbl9hcHBsaWVkIjogRmFsc2UsCiAgICAgICAgInJ1bnRpbWVfYmVoYXZpb3JfY2hhbmdlZCI6IEZhbHNlLAogICAgICAgICJmaW5hbF9yZWNvbW1lbmRhdGlvbiI6ICJSZXBsYXkgbWF5IGJlIHByZXBhcmVkIGluIGEgZnV0dXJlIGxheWVyIG9ubHkgaWYgaGFuZG9mZl9zdGF0dXMgaXMgTElWRV9BUFBST1ZBTF9IQU5ET0ZGX1ZBTElEX0ZPUl9SRVBMQVlfT05MWS4iIGlmIHJlcGxheV9hbGxvd2VkIGVsc2UgIktlZXAgcmVwbGF5IGJsb2NrZWQuIEEgbm9uLWZpeHR1cmUgbGl2ZSBhcHByb3ZhbCBhcnRpZmFjdCBpcyByZXF1aXJlZC4iLAogICAgICAgICJib3VuZGFyeSI6ICJMaXZlIGFwcHJvdmFsIGhhbmRvZmYgY2hlY2tzIGFyZSBsb2NhbCBjbGFzc2lmaWVyLWdvdmVybmFuY2UgYm91bmRhcnkgYXJ0aWZhY3RzLiBUaGV5IGRvIG5vdCBjcmVhdGUgYnJhbmNoZXMgYnkgZGVmYXVsdCwgZG8gbm90IG11dGF0ZSBjbGFzc2lmaWVyIGJlaGF2aW9yLCBkbyBub3QgYXBwbHkgY2FsaWJyYXRpb24sIGFuZCBkbyBub3QgdmFsaWRhdGUgc2lsaWNvbiwgcHJvZHVjdHMsIG1hbnVmYWN0dXJpbmcsIHByb2Nlc3Mgbm9kZXMsIGJlbmNobWFyayBzdXBlcmlvcml0eSwgb3IgdW5pdmVyc2FsIFRhdSBTY2FsaW5nIGxhdy4iLAogICAgICAgICJuZXh0X3JlY29tbWVuZGF0aW9uIjogInYwLjYuNyBzaG91bGQgY3JlYXRlIGFuIGFwcHJvdmFsLWdhdGVkIHJlcGxheSBleGVjdXRvciB0aGF0IHN0aWxsIHJlZnVzZXMgdG8gcnVuIHVubGVzcyB0aGUgbGl2ZSBhcHByb3ZhbCBoYW5kb2ZmIGlzIHZhbGlkLiIsCiAgICB9CiAgICBzdW1tYXJ5WyJjaGFydF9wYXRocyJdID0gY2hhcnRzKHN1bW1hcnkpCgogICAgd2pzb24oT1VUIC8gImxpdmVfYXBwcm92YWxfaGFuZG9mZl9jaGVja192MF82XzYuanNvbiIsIHN1bW1hcnkpCiAgICB3anNvbihPVVQgLyAibGF0ZXN0X2xpdmVfYXBwcm92YWxfaGFuZG9mZl9jaGVjay5qc29uIiwgc3VtbWFyeSkKICAgIHd0ZXh0KE9VVCAvICJsaXZlX2FwcHJvdmFsX2hhbmRvZmZfY2hlY2tfdjBfNl82Lm1kIiwgcmVwb3J0KHN1bW1hcnkpKQogICAgd3RleHQoT1VUIC8gImxhdGVzdF9saXZlX2FwcHJvdmFsX2hhbmRvZmZfY2hlY2subWQiLCByZXBvcnQoc3VtbWFyeSkpCgogICAgcHJpbnQoanNvbi5kdW1wcyh7CiAgICAgICAgInNjaGVtYSI6IHN1bW1hcnlbInNjaGVtYSJdLAogICAgICAgICJoYW5kb2ZmX3N0YXR1cyI6IHN1bW1hcnlbImhhbmRvZmZfc3RhdHVzIl0sCiAgICAgICAgImxpdmVfYXBwcm92YWxfcHJlc2VudCI6IHN1bW1hcnlbImxpdmVfYXBwcm92YWxfcHJlc2VudCJdLAogICAgICAgICJsaXZlX2FwcHJvdmFsX3ZhbGlkIjogc3VtbWFyeVsibGl2ZV9hcHByb3ZhbF92YWxpZCJdLAogICAgICAgICJmaXh0dXJlX21pc3VzZV9kZXRlY3RlZCI6IHN1bW1hcnlbImZpeHR1cmVfbWlzdXNlX2RldGVjdGVkIl0sCiAgICAgICAgImFwcHJvdmFsX2RlY2lzaW9uIjogc3VtbWFyeVsiYXBwcm92YWxfZGVjaXNpb24iXSwKICAgICAgICAicmVwbGF5X2FsbG93ZWQiOiBzdW1tYXJ5WyJyZXBsYXlfYWxsb3dlZCJdLAogICAgICAgICJicmFuY2hfY3JlYXRlZCI6IHN1bW1hcnlbImJyYW5jaF9jcmVhdGVkIl0sCiAgICAgICAgIm11dGF0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJtdXRhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImFwcGxpY2F0aW9uX2FsbG93ZWQiOiBzdW1tYXJ5WyJhcHBsaWNhdGlvbl9hbGxvd2VkIl0sCiAgICAgICAgImNhbGlicmF0aW9uX2FwcGxpZWQiOiBzdW1tYXJ5WyJjYWxpYnJhdGlvbl9hcHBsaWVkIl0sCiAgICAgICAgImNoYXJ0X2NvdW50IjogbGVuKHN1bW1hcnlbImNoYXJ0X3BhdGhzIl0pLAogICAgICAgICJyZXBvcnQiOiAicmVwb3J0cy9saXZlX2FwcHJvdmFsX2hhbmRvZmYvbGF0ZXN0X2xpdmVfYXBwcm92YWxfaGFuZG9mZl9jaGVjay5tZCIsCiAgICB9LCBpbmRlbnQ9Miwgc29ydF9rZXlzPVRydWUpKQoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgIG1haW4oKQo=").decode())

write(ROOT/"reports"/"live_approval_handoff"/"README.md", """# Live Approval Handoff Reports

Current layer: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**

## Purpose

This folder stores live approval handoff checks. It refuses to treat fixture files as live approval.

## Primary command

```powershell
python scripts/benchmarks/run_live_approval_handoff_check.py
```

## README Update Rule

Update this mini README whenever live approval handoff schemas, fixture-separation rules, or replay gates change.

Boundary: live approval handoff checks are local classifier-governance boundary artifacts only.
""")
write(ROOT/"visuals"/"live_approval_handoff"/"README.md", """# Live Approval Handoff Visuals

Current layer: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**

## Purpose

This folder stores charts summarizing live approval handoff state.

## README Update Rule

Update this mini README whenever live approval handoff chart names or meanings change.

Boundary: live approval handoff visuals are local classifier-governance diagnostics only.
""")
write(ROOT/"visuals"/"live_approval_handoff"/"v0_6_6"/"README.md", """# v0.6.6 Live Approval Handoff Charts

Expected charts:

- `live_approval_handoff_gate.png`
- `fixture_vs_live_approval.png`
- `live_approval_handoff_status.png`

## README Update Rule

Update this mini README whenever chart names or meanings change.

Boundary: local live approval handoff diagnostics only.
""")

p=ROOT/"README.md"; backup(p,"readme"); r=read(p)
r=re.sub(r"Current checkpoint: \*\*TAU-SCALING-SA v0\.6\.5[^*]*\*\*", "Current checkpoint: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**", r)
r=re.sub(r"Previous seal: \*\*TAU-SCALING-SA v0\.6\.4[^*]*\*\*", "Previous seal: **TAU-SCALING-SA v0.6.5 - Approval Fixture and Denial Fixture Validator**", r)
r=re.sub(r"\| Current checkpoint \| TAU-SCALING-SA v0\.6\.5 \|", "| Current checkpoint | TAU-SCALING-SA v0.6.6 |", r)
r=r.replace("| Task routing matrix | geometry-aware / v0.6.5-ready |", "| Task routing matrix | geometry-aware / v0.6.6-ready |")
r=r.replace("| Agent contract version sync | current / v0.6.5 |", "| Agent contract version sync | current / v0.6.6 |")
if "| Live approval handoff |" not in r:
    r=r.replace("| Approval fixture charts | `visuals/approval_fixtures/v0_6_5/` |\n",
                "| Approval fixture charts | `visuals/approval_fixtures/v0_6_5/` |\n| Live approval handoff | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` |\n| Live approval handoff charts | `visuals/live_approval_handoff/v0_6_6/` |\n")
if "python scripts/benchmarks/run_live_approval_handoff_check.py" not in r:
    r=r.replace("python scripts/benchmarks/validate_approval_fixtures.py\npython scripts/release/validate_release.py",
                "python scripts/benchmarks/validate_approval_fixtures.py\npython scripts/benchmarks/run_live_approval_handoff_check.py\npython scripts/release/validate_release.py")
if "    live_approval_handoff/" not in r:
    r=r.replace("  reports/\n    nexus_feedback/\n", "  reports/\n    nexus_feedback/\n    live_approval_handoff/\n")
    r=r.replace("  visuals/\n    nexus_feedback/\n", "  visuals/\n    nexus_feedback/\n    live_approval_handoff/\n")
section="""## Live Approval Handoff Check v0.6.6

v0.6.6 refuses to treat fixtures as live approvals and checks for a separate live approval artifact.

Primary command:

```powershell
python scripts/benchmarks/run_live_approval_handoff_check.py
```

Primary outputs:

```text
reports/live_approval_handoff/latest_live_approval_handoff_check.json
reports/live_approval_handoff/latest_live_approval_handoff_check.md
visuals/live_approval_handoff/v0_6_6/
```

Current expected lock when no live approval artifact exists:

```text
live_approval_present: false
live_approval_valid: false
replay_allowed: false
branch_created: false
mutation_allowed: false
policy_enforced: false
calibration_applied: false
application_allowed: false
```

Boundary: live approval handoff checks are local classifier-governance boundary artifacts. They do not create branches by default, do not mutate classifier behavior, do not apply calibration, and do not validate silicon, product performance, manufacturing capability, process-node equivalence, benchmark superiority, AI understanding, or universal Tau Scaling law.

"""
if "## Live Approval Handoff Check v0.6.6" not in r:
    r=r.replace("## Approval Fixture and Denial Fixture Validator v0.6.5", section+"## Approval Fixture and Denial Fixture Validator v0.6.5",1)
lesson="| L-048 | v0.6.5 validated fixture semantics but fixtures are still not live approval. | Fixture-validity can be mistaken for live-approval validity unless handoff checks enforce path separation. | Live approval handoff must refuse fixtures and require a separate non-fixture live approval artifact before replay is considered. |"
if "L-048" not in r:
    r=r.replace("| L-047 | v0.6.4 emitted a blocked replay report because approval was invalid. | The system needs fixtures to prove approval, denial, and more-evidence decisions have distinct replay semantics. | Approval fixture validation must prove fixture semantics without treating fixtures as live approvals. |\n",
                "| L-047 | v0.6.4 emitted a blocked replay report because approval was invalid. | The system needs fixtures to prove approval, denial, and more-evidence decisions have distinct replay semantics. | Approval fixture validation must prove fixture semantics without treating fixtures as live approvals. |\n"+lesson+"\n")
if "| v0.6.6 |" not in r:
    r=r.replace("| v0.6.5 | Approval fixture and denial fixture validator; fixtures only, no live approval. |\n",
                "| v0.6.5 | Approval fixture and denial fixture validator; fixtures only, no live approval. |\n| v0.6.6 | Live approval handoff check; refuses fixtures as live approval. |\n")
r=re.sub(r"## Next Recommended Version\s+.*\Z", """## Next Recommended Version

**TAU-SCALING-SA v0.6.7 - Approval-Gated Replay Executor**

Recommended goals:

- Refuse to run unless live approval handoff is valid.
- Emit blocked executor report when live approval is missing.
- Keep branch creation disabled by default.
- Keep `mutation_allowed: false`.
""", r, flags=re.S)
write(p,r)

for name, pattern, repl in [
    ("AGENTS.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**"),
    ("rcc/nexus/task_routing_matrix.md", r"Current contract: \*\*TAU-SCALING-SA v0\.6\.5[^*]*\*\*", "Current contract: **TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check**")
]:
    p=ROOT/name; backup(p, name.replace('/','_')); s=read(p); s=re.sub(pattern, repl, s)
    if name=="AGENTS.md" and "run_live_approval_handoff_check.py" not in s:
        s=s.replace("python scripts/benchmarks/validate_approval_fixtures.py\npython -m unittest discover -s tests",
                    "python scripts/benchmarks/validate_approval_fixtures.py\npython scripts/benchmarks/run_live_approval_handoff_check.py\npython -m unittest discover -s tests")
        s=s.replace("| Approval fixture patch | `reports/approval_fixtures/`, `visuals/approval_fixtures/`, approval template | fixture validator + release validator; fixtures are not approval |\n",
                    "| Approval fixture patch | `reports/approval_fixtures/`, `visuals/approval_fixtures/`, approval template | fixture validator + release validator; fixtures are not approval |\n| Live approval handoff patch | `reports/live_approval_handoff/`, `visuals/live_approval_handoff/`, approval fixtures | handoff check + release validator; fixtures refused as live approval |\n")
    if name.endswith("task_routing_matrix.md") and "| Live approval handoff patch |" not in s:
        s=s.replace("| Approval fixture patch | outer | validation | governance | approval template + approval validator | fixture validator + charts + release validator | `reports/approval_fixtures/latest_approval_fixture_validator.md` |\n",
                    "| Approval fixture patch | outer | validation | governance | approval template + approval validator | fixture validator + charts + release validator | `reports/approval_fixtures/latest_approval_fixture_validator.md` |\n| Live approval handoff patch | outer | validation | governance | approval fixtures + live approval directory | handoff check + charts + release validator | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` |\n")
    write(p,s)

p=ROOT/"rcc"/"nexus"/"route_map.json"; backup(p,"route_map")
try: route=json.loads(read(p))
except Exception: route={}
route["version"]="v0.6.6"; route["updated_at"]=NOW
route.setdefault("v0_6_routes",{})["live_approval_handoff_check"]={
    "read_first":["reports/approval_fixtures/latest_approval_fixture_validator.json","reports/human_approval/live/"],
    "validate":["python scripts/benchmarks/run_live_approval_handoff_check.py","python scripts/release/validate_release.py"],
    "evidence":["reports/live_approval_handoff/latest_live_approval_handoff_check.md","visuals/live_approval_handoff/v0_6_6/"],
    "mutation_lock":"Refuses fixtures as live approval; no branch creation or mutation."
}
write(p,json.dumps(route,indent=2,sort_keys=True)+"\n")

p=ROOT/"docs"/"benchmarks"/"benchmark_atlas.md"; backup(p,"atlas"); t=read(p)
if "| v0.6.6 | Live approval handoff check |" not in t:
    t=t.replace("| v0.6.5 | Approval fixture and denial fixture validator | `python scripts/benchmarks/validate_approval_fixtures.py` | Validates approval/denial/more-evidence fixture semantics without live approval | `reports/approval_fixtures/latest_approval_fixture_validator.md` | `visuals/approval_fixtures/v0_6_5/` |\n",
                "| v0.6.5 | Approval fixture and denial fixture validator | `python scripts/benchmarks/validate_approval_fixtures.py` | Validates approval/denial/more-evidence fixture semantics without live approval | `reports/approval_fixtures/latest_approval_fixture_validator.md` | `visuals/approval_fixtures/v0_6_5/` |\n| v0.6.6 | Live approval handoff check | `python scripts/benchmarks/run_live_approval_handoff_check.py` | Refuses fixtures as live approval and requires separate live artifact | `reports/live_approval_handoff/latest_live_approval_handoff_check.md` | `visuals/live_approval_handoff/v0_6_6/` |\n")
write(p,t)

write(ROOT/"docs"/"release_notes"/"tau_scaling_v0_6_6_live_approval_handoff.md", f"""# TAU-SCALING-SA v0.6.6 - Live Approval Handoff Check

Generated: {NOW}

## Purpose

Refuse to treat fixtures as live approvals and require a separate non-fixture live approval artifact.

## Boundary

Live approval handoff checks are local classifier-governance boundary artifacts only. They do not create live approval, create branches, mutate classifier behavior, or validate silicon, products, manufacturing, process nodes, benchmark superiority, or universal Tau Scaling law.
""")
print("v0.6.6 patch written")
