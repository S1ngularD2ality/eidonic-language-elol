# glyph_054.py — Soul Line Activator
# -----------------------------------------------------------------------------
# ID:            054
# Pack:          Pack 001 (000–100)
# Name:          Soul Line Activator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_054(n: int, lines: Sequence[Tuple[Tuple[int, int], Tuple[int, int]]]) -> List[List[int]]:
    """
    Soul Line Activator — rasterize 4-connected lines on an n×n grid.

    Overview
    --------
    Draws lines defined by endpoints using an integer Bresenham variant. Cells on lines
    are set to 1; others 0.

    Parameters
    ----------
    n : int
        Grid size (>= 1).
    lines : Sequence[Tuple[Tuple[int,int], Tuple[int,int]]]
        List of ((x0,y0),(x1,y1)) endpoints.

    Returns
    -------
    List[List[int]]
        n×n binary grid.

    Examples
    --------
    >>> glyph_054(3, [((0,0),(2,2))])
    [[1,0,0],[0,1,0],[0,0,1]]

    Exceptions
    ----------
    - ValueError : if `n < 1`.

    Complexity
    ----------
    - Time  : O(sum |Δ| per line)
    - Space : O(n^2)
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    G = [[0] * n for _ in range(n)]
    for (x0, y0), (x1, y1) in lines:
        _bresenham(G, x0, y0, x1, y1)
    return G

def _bresenham(G: List[List[int]], x0: int, y0: int, x1: int, y1: int) -> None:
    dx = abs(x1 - x0); sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0); sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        if 0 <= y0 < len(G) and 0 <= x0 < len(G[0]):
            G[y0][x0] = 1
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy; x0 += sx
        if e2 <= dx:
            err += dx; y0 += sy
