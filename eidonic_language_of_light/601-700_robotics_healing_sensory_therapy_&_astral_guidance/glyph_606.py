# glyph_606.py — ADAPTIVE_SPEED_CONTROL
# -----------------------------------------------------------------------------
# ID:            606
# Pack:          Pack 007 (601–700)
# Name:          ADAPTIVE_SPEED_CONTROL
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # algebraic policy
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Any

def glyph_606(clear_distance_m: float, crowd_factor: float, *,
              v_max: float = 1.0, v_min: float = 0.05) -> Dict[str, Any]:
    """
    ADAPTIVE_SPEED_CONTROL — compute safe speed from clearance & crowding.

    Returns
    -------
    {'v_cmd': float}

    Notes
    -----
    v_cmd = clamp(v_min, v_max, (clear_distance_m / (1 + crowd_factor)))
    """
    v = clear_distance_m / (1.0 + max(0.0, crowd_factor))
    v = max(v_min, min(v_max, v))
    return {"v_cmd": float(v)}
