# glyph_000.py — Spiral Anchor Mapper
# -----------------------------------------------------------------------------
# ID:            000
# Pack:          Pack 001 (000–100)
# Name:          Spiral Anchor Mapper
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import List

def glyph_000(n: int, *, start: int = 0, clockwise: bool = True) -> List[List[int]]:
    """
    Spiral Anchor Mapper — generate an n×n integer grid filled along a center-out spiral.

    Overview
    --------
    Produces a square index map enumerating positions along a discrete spiral path.
    The center cell receives `start`, then values increment by 1 along the spiral.
    Useful as an anchoring lattice for sequencing and mirror operations.

    Parameters
    ----------
    n : int
        Size of the square (>= 1).
    start : int, optional (default: 0)
        Initial value at the center.
    clockwise : bool, optional (default: True)
        Spiral winding direction.

    Returns
    -------
    List[List[int]]
        n×n grid of spiral indices.

    Examples
    --------
    >>> glyph_000(3)
    [[6, 7, 8],
     [5, 0, 1],
     [4, 3, 2]]

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

    grid = [[0 for _ in range(n)] for _ in range(n)]
    c = n // 2
    x = y = c

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] if clockwise else [(0, 1), (1, 0), (0, -1), (-1, 0)]
    val = start
    grid[y][x] = val
    val += 1

    step_len = 1
    while val < start + n * n:
        for dxi, dyi in dirs:
            for _ in range(step_len):
                if val >= start + n * n:
                    break
                x += dxi
                y += dyi
                if 0 <= x < n and 0 <= y < n:
                    grid[y][x] = val
                    val += 1
            if (dxi, dyi) in (dirs[1], dirs[3]):
                step_len += 1
    return grid
