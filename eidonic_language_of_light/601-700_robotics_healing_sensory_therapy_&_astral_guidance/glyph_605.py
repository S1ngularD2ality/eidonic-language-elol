# glyph_605.py — EMERGENCY_STOP
# -----------------------------------------------------------------------------
# ID:            605
# Pack:          Pack 007 (601–700)
# Name:          EMERGENCY_STOP
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # logical gate only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_605(signals: Mapping[str, Any]) -> Dict[str, Any]:
    """
    EMERGENCY_STOP — compute an immediate stop decision from boolean sensors.

    Parameters
    ----------
    signals : Mapping[str,Any]
        Keys may include 'impact', 'tilt', 'overcurrent', 'human_close', etc.

    Returns
    -------
    {'stop': bool, 'reasons': List[str]}
    """
    reasons = [k for k,v in signals.items() if bool(v)]
    return {"stop": len(reasons) > 0, "reasons": reasons}
