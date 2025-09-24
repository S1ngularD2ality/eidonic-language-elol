# glyph_015.py — Spiral Key Encoder
# -----------------------------------------------------------------------------
# ID:            015
# Pack:          Pack 001 (000–100)
# Name:          Spiral Key Encoder
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

def glyph_015(n: int) -> List[int]:
    """
    Spiral Key Encoder — produce spiral visiting order as a 1D key.

    Overview
    --------
    Flattens the index map from `glyph_000` (clockwise, start=0) to a linear key.

    Parameters
    ----------
    n : int
        Grid size (>= 1).

    Returns
    -------
    List[int]
        Visiting indices 0..n^2-1 in spiral order.

    Examples
    --------
    >>> glyph_015(2)
    [0, 1, 2, 3]
    """
    grid = glyph_000(n, start=0, clockwise=True)
    order = []
    # invert: position of k
    pos = {}
    for y in range(n):
        for x in range(n):
            pos[grid[y][x]] = (y, x)
    for k in range(n*n):
        order.append(k)
    return order
