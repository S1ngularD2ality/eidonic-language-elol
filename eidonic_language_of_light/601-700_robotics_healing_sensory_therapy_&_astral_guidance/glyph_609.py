# glyph_609.py — HUMIDITY_SAFETY_MODE
# -----------------------------------------------------------------------------
# ID:            609
# Pack:          Pack 007 (601–700)
# Name:          HUMIDITY_SAFETY_MODE
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy-only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Any

def glyph_609(rh_percent: float) -> Dict[str, Any]:
    """
    HUMIDITY_SAFETY_MODE — recommend behavior under ambient humidity.

    Returns
    -------
    {'mode':'ok'|'caution'|'halt'}
    """
    rh = max(0.0, min(100.0, rh_percent))
    mode = 'ok' if 20.0 <= rh <= 70.0 else ('caution' if 10.0 <= rh <= 80.0 else 'halt')
    return {"mode": mode}
