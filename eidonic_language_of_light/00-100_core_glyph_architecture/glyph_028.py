# glyph_028.py — Dimensional Thread Mapper
# -----------------------------------------------------------------------------
# ID:            028
# Pack:          Pack 001 (000–100)
# Name:          Dimensional Thread Mapper
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_028(n: int) -> List[Tuple[int, int]]:
    """
    Dimensional Thread Mapper — produce 2D Hilbert-like scan order (simple Z-curve).

    Overview
    --------
    Emits (y,x) coordinates for a Z-order curve on an n×n grid, n power-of-two.

    Parameters
    ----------
    n : int
        Grid size; should be a power of two (>= 1).

    Returns
    -------
    List[Tuple[int,int]]
        Visit order across the grid.

    Examples
    --------
    >>> coords = glyph_028(2)
    >>> set(coords) == {(0,0),(0,1),(1,0),(1,1)}
    True
    """
    if n < 1:
        return []
    coords: List[Tuple[int,int]] = []
    for y in range(n):
        for x in range(n):
            z = _interleave_bits(x, y)
            coords.append((y, x, z))
    coords.sort(key=lambda t: t[2])
    return [(y,x) for y,x,_ in coords]

def _interleave_bits(x: int, y: int) -> int:
    def spread(v: int) -> int:
        v &= 0xFFFF
        v = (v | (v << 8)) & 0x00FF00FF
        v = (v | (v << 4)) & 0x0F0F0F0F
        v = (v | (v << 2)) & 0x33333333
        v = (v | (v << 1)) & 0x55555555
        return v
    return (spread(x) << 1) | spread(y)
