# glyph_613.py — HAZARD_DISTANCE_ALERT
# -----------------------------------------------------------------------------
# ID:            613
# Pack:          Pack 007 (601–700)
# Name:          HAZARD_DISTANCE_ALERT
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure range gating
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any
import math

def glyph_613(hazards: Sequence[Tuple[float,float]], here: Tuple[float,float],
              *, alert_m: float = 2.0) -> Dict[str, Any]:
    """
    HAZARD_DISTANCE_ALERT — min distance & alert boolean.

    Returns
    -------
    {'min_dist': float, 'alert': bool}
    """
    if not hazards:
        return {"min_dist": math.inf, "alert": False}
    dmin = min(math.hypot(here[0]-x, here[1]-y) for x,y in hazards)
    return {"min_dist": float(dmin), "alert": dmin < alert_m}
