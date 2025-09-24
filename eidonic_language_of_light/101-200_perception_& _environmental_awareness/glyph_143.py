# glyph_143.py — Anchor Spiral Tetherer
# -----------------------------------------------------------------------------
# ID:            143
# Pack:          Pack 002 (101–200)
# Name:          Anchor Spiral Tetherer
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_143(n: int) -> List[Tuple[int, int]]:
    """
    Anchor Spiral Tetherer — anchor points on a square spiral path.

    Overview
    --------
    Emits integer (y,x) positions following a center-out clockwise spiral across
    an n×n grid.

    Parameters
    ----------
    n : int

    Returns
    -------
    List[Tuple[int,int]]
        Spiral coordinates.

    Examples
    --------
    >>> set(glyph_143(2)) == {(0,0),(0,1),(1,1),(1,0)}
    True
    """
    if n < 1: return []
    c = n // 2
    y = x = c
    path = [(y,x)]
    step = 1
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    while len(path) < n*n:
        for dyi, dxi in dirs:
            for _ in range(step):
                if len(path) >= n*n: break
                y += dyi; x += dxi
                if 0<=y<n and 0<=x<n: path.append((y,x))
            if (dyi,dxi) in (dirs[1], dirs[3]): step += 1
    return path
