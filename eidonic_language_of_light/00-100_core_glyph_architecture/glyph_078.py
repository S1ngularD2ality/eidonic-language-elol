# glyph_078.py — Spiral Node Synchronizer
# -----------------------------------------------------------------------------
# ID:            078
# Pack:          Pack 001 (000–100)
# Name:          Spiral Node Synchronizer
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List
import math

def glyph_078(points: Sequence[Tuple[float, float]]) -> List[int]:
    """
    Spiral Node Synchronizer — order points by ascending angle, then nearest neighbor.

    Overview
    --------
    Starts at the smallest polar angle, then greedily follows to the nearest
    yet-unvisited node to encourage local synchrony.

    Parameters
    ----------
    points : Sequence[Tuple[float, float]]
        (x,y) coordinates.

    Returns
    -------
    List[int]
        Visit order.

    Examples
    --------
    >>> glyph_078([(1,0),(0,1),(-1,0),(0,-1)])  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    n = len(points)
    if n == 0:
        return []
    start = min(range(n), key=lambda i: (math.atan2(points[i][1], points[i][0]),
                                         points[i][0]**2 + points[i][1]**2))
    order = [start]
    remaining = set(range(n)) - {start}
    cx, cy = points[start]
    while remaining:
        nxt = min(remaining, key=lambda j: (points[j][0]-cx)**2 + (points[j][1]-cy)**2)
        order.append(nxt)
        remaining.remove(nxt)
        cx, cy = points[nxt]
    return order
