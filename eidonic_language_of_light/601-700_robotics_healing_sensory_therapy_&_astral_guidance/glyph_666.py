# glyph_666.py — SAFETY_ZONE_CREATE
# -----------------------------------------------------------------------------
# ID:            666
# Pack:          Pack 007 (601–700)
# Name:          SAFETY_ZONE_CREATE
# Class:         safety_planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple, Dict, List

def glyph_666(center: Tuple[float, float], *,
              radius_m: float = 2.0,
              petals: int = 6) -> Dict[str, List[Tuple[float, float]]]:
    """
    SAFETY_ZONE_CREATE — generate a radial marker lattice (flower pattern).

    Overview
    --------
    Returns points for placing visual or soft markers around a center with
    `petals` spokes at radius `radius_m`.

    Parameters
    ----------
    center : (x,y)
    radius_m : float, optional (default: ``2.0``)
    petals : int, optional (default: ``6``)

    Returns
    -------
    {'points': List[(x,y)]}

    Examples
    --------
    >>> len(glyph_666((0,0), radius_m=1.0, petals=4)['points'])
    4

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    import math
    cx, cy = center
    p = max(0, petals)
    pts = []
    for i in range(p):
        ang = 2*math.pi * (i / p) if p else 0.0
        pts.append((cx + radius_m*math.cos(ang), cy + radius_m*math.sin(ang)))
    return {"points": pts}
