# glyph_053.py — Harmonic Vortex Indexer
# -----------------------------------------------------------------------------
# ID:            053
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Vortex Indexer
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List, Tuple

def glyph_053(points: Sequence[Tuple[float, float]]) -> List[int]:
    """
    Harmonic Vortex Indexer — order points by polar angle then radius.

    Overview
    --------
    Sort indices by `(atan2(y,x), x^2+y^2)`, yielding a spiral-like visitation.

    Parameters
    ----------
    points : Sequence[Tuple[float, float]]
        (x, y) Cartesian coordinates.

    Returns
    -------
    List[int]
        Indices in sorted order.

    Examples
    --------
    >>> glyph_053([(1,0), (0,1), (-1,0), (0,-1)])
    [0,1,2,3]  # starting at angle 0 and moving CCW

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    return sorted(
        range(len(points)),
        key=lambda i: (math.atan2(points[i][1], points[i][0]),
                       points[i][0] ** 2 + points[i][1] ** 2),
    )
