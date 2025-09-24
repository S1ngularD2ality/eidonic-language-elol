# glyph_115.py — Inner Field Restructurer
# -----------------------------------------------------------------------------
# ID:            115
# Pack:          Pack 002 (101–200)
# Name:          Inner Field Restructurer
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_115(flat: Sequence[float], *, width: int) -> List[List[float]]:
    """
    Inner Field Restructurer — reshape a flat array into rows of given width.

    Overview
    --------
    Drops any partial final row to keep shape consistent.

    Parameters
    ----------
    flat : Sequence[float]
    width : int

    Returns
    -------
    List[List[float]]
        Reshaped matrix (R×width).

    Examples
    --------
    >>> glyph_115([1,2,3,4,5], width=2)
    [[1.0, 2.0], [3.0, 4.0]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if width < 1:
        return []
    m = len(flat) // width
    return [[float(flat[r*width + c]) for c in range(width)] for r in range(m)]
