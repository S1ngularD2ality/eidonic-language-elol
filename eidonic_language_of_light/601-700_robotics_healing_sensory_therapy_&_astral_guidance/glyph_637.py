# glyph_637.py — DUST_CONTROL_PATH
# -----------------------------------------------------------------------------
# ID:            637
# Pack:          Pack 007 (601–700)
# Name:          DUST_CONTROL_PATH
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_637(waypoints: Sequence[Tuple[float, float]], dust_penalty: Sequence[float]) -> List[Tuple[float, float]]:
    """
    DUST_CONTROL_PATH — reorder waypoints to minimize dust exposure cost.

    Overview
    --------
    Stable sort by dust penalty (ascending), preserving order for ties.

    Parameters
    ----------
    waypoints   : Sequence[(float,float)]
    dust_penalty: Sequence[float]

    Returns
    -------
    List[Tuple[float, float]]
        Reordered waypoints.

    Examples
    --------
    >>> glyph_637([(0,0),(1,0)], [1.0, 0.5])[0]
    (1, 0)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    idx = list(range(len(waypoints)))
    idx.sort(key=lambda i: float(dust_penalty[i]) if i < len(dust_penalty) else 0.0)
    return [waypoints[i] for i in idx]
