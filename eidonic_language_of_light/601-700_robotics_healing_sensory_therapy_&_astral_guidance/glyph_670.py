# glyph_670.py — WASTE_COLLECTION_PATH
# -----------------------------------------------------------------------------
# ID:            670
# Pack:          Pack 007 (601–700)
# Name:          WASTE_COLLECTION_PATH
# Class:         logistics_planning
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # greedy ordering only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_670(bins_xy: Sequence[Tuple[float, float]],
              start_xy: Tuple[float, float]) -> List[Tuple[float, float]]:
    """
    WASTE_COLLECTION_PATH — nearest-neighbor ordering of bin locations.

    Overview
    --------
    Returns a greedy route starting at `start_xy` visiting each bin once.

    Parameters
    ----------
    bins_xy : Sequence[(x,y)]
    start_xy: (x,y)

    Returns
    -------
    List[(x,y)] : ordered bin coordinates

    Examples
    --------
    >>> route = glyph_670([(1,0),(2,0),(0,0)], (0,0))
    >>> route[0] == (0,0)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    import math
    if not bins_xy:
        return [start_xy]
    remaining = list(bins_xy)
    route = [start_xy]
    here = start_xy
    while remaining:
        i = min(range(len(remaining)),
                key=lambda k: math.hypot(remaining[k][0]-here[0], remaining[k][1]-here[1]))
        here = remaining.pop(i)
        route.append(here)
    return route
