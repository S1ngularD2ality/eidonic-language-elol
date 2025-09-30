# glyph_652.py — FLOOD_ZONE_AVOID
# -----------------------------------------------------------------------------
# ID:            652
# Pack:          Pack 007 (601–700)
# Name:          FLOOD_ZONE_AVOID
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # predicate over path points
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any

def glyph_652(path_xyh: Sequence[Tuple[float, float, float]], *,
              min_height_m: float = 0.3) -> Dict[str, Any]:
    """
    FLOOD_ZONE_AVOID — flag path points below safe elevation threshold.

    Overview
    --------
    Checks each (x,y,height_m) and returns first violation index.

    Parameters
    ----------
    path_xyh : Sequence[(x, y, h_m)]
    min_height_m : float, optional (default: ``0.3``)

    Returns
    -------
    {'ok': bool, 'first_violation_idx': int}

    Examples
    --------
    >>> glyph_652([(0,0,0.5),(1,0,0.2)])['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    for i, (_, _, h) in enumerate(path_xyh):
        if h < min_height_m:
            return {"ok": False, "first_violation_idx": i}
    return {"ok": True, "first_violation_idx": -1}
