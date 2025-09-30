# glyph_675.py — HAZARD_MARKER_DEPLOY
# -----------------------------------------------------------------------------
# ID:            675
# Pack:          Pack 007 (601–700)
# Name:          HAZARD_MARKER_DEPLOY
# Class:         safety_planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # lattice only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple, Dict, List

def glyph_675(hazard_center: Tuple[float, float], *,
              inner_m: float = 1.0, outer_m: float = 3.0, count: int = 6) -> Dict[str, List[Tuple[float, float]]]:
    """
    HAZARD_MARKER_DEPLOY — two-ring marker coordinates for a known hazard.

    Overview
    --------
    Generates two concentric rings for clear human-visible marking.

    Parameters
    ----------
    hazard_center : (x,y)
    inner_m : float, optional (default: ``1.0``)
    outer_m : float, optional (default: ``3.0``)
    count   : int, optional (default: ``6``)  # points per ring

    Returns
    -------
    {'inner': List[(x,y)], 'outer': List[(x,y)]}

    Examples
    --------
    >>> res = glyph_675((0,0), inner_m=1.0, outer_m=2.0, count=4)
    >>> len(res['inner']) == len(res['outer']) == 4
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
    cx, cy = hazard_center
    k = max(0, count)
    inner = []
    outer = []
    for i in range(k):
        ang = 2*math.pi * (i / k) if k else 0.0
        inner.append((cx + inner_m*math.cos(ang), cy + inner_m*math.sin(ang)))
        outer.append((cx + outer_m*math.cos(ang), cy + outer_m*math.sin(ang)))
    return {"inner": inner, "outer": outer}
