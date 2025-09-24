# glyph_006.py — Thoughtform Anchor Grid
# -----------------------------------------------------------------------------
# ID:            006
# Pack:          Pack 001 (000–100)
# Name:          Thoughtform Anchor Grid
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_006(n: int, *, value: int = 1) -> List[List[int]]:
    """
    Thoughtform Anchor Grid — create an n×n grid anchored to a base value.

    Overview
    --------
    Initializes a constant grid (baseline “anchor”) for overlays and routing.

    Parameters
    ----------
    n : int
        Grid size (>= 1).
    value : int, optional (default: 1)
        Fill value.

    Returns
    -------
    List[List[int]]
        n×n grid.

    Examples
    --------
    >>> glyph_006(2, value=9)
    [[9, 9],
     [9, 9]]

    Exceptions
    ----------
    - ValueError : if `n < 1`.

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n^2)
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    return [[int(value) for _ in range(n)] for _ in range(n)]
