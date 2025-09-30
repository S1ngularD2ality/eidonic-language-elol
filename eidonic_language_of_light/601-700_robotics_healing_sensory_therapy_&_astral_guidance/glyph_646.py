# glyph_646.py — EMERGENCY_RESOURCE_DROP
# -----------------------------------------------------------------------------
# ID:            646
# Pack:          Pack 007 (601–700)
# Name:          EMERGENCY_RESOURCE_DROP
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # geometry only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple, List, Dict

def glyph_646(center_xy: Tuple[float, float], radius_m: float, count: int) -> Dict[str, List[Tuple[float, float]]]:
    """
    EMERGENCY_RESOURCE_DROP — compute evenly spaced drop points on a circle.

    Overview
    --------
    Returns `count` points around `center_xy` at `radius_m`, starting angle 0.

    Parameters
    ----------
    center_xy : (float, float)
    radius_m  : float
    count     : int

    Returns
    -------
    {'points': List[(x,y)]}

    Examples
    --------
    >>> len(glyph_646((0,0), 2.0, 4)['points']) == 4
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    import math
    cx, cy = center_xy
    k = max(0, int(count))
    pts = []
    for i in range(k):
        ang = 2*math.pi * (i / k) if k else 0.0
        pts.append((cx + radius_m*math.cos(ang), cy + radius_m*math.sin(ang)))
    return {"points": pts}
