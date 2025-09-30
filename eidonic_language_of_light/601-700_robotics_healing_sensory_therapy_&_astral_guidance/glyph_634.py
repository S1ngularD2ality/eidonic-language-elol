# glyph_634.py — CROWD_SAFETY_PATH
# -----------------------------------------------------------------------------
# ID:            634
# Pack:          Pack 007 (601–700)
# Name:          CROWD_SAFETY_PATH
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict
import math

def glyph_634(waypoints: Sequence[Tuple[float, float]],
              people: Sequence[Tuple[float, float]], *,
              min_dist_m: float = 1.2) -> Dict[str, bool | int]:
    """
    CROWD_SAFETY_PATH — check that every waypoint respects crowd distance.

    Overview
    --------
    Screens a waypoint list; returns first violation if any.

    Parameters
    ----------
    waypoints : Sequence[(float,float)]
    people    : Sequence[(float,float)]
    min_dist_m: float, optional (default: ``1.2``)

    Returns
    -------
    Dict[str, bool | int]
        {'ok': bool, 'first_violation_idx': int}

    Examples
    --------
    >>> glyph_634([(0,0),(1,0)], [(0.5,0)], min_dist_m=1.0)['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N·M)
    - Space : O(1)
    """
    for i, p in enumerate(waypoints):
        for h in people:
            if math.hypot(p[0]-h[0], p[1]-h[1]) < min_dist_m:
                return {"ok": False, "first_violation_idx": i}
    return {"ok": True, "first_violation_idx": -1}
