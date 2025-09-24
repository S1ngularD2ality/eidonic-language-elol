# glyph_263.py — Anchor Spiral Projector
# -----------------------------------------------------------------------------
# ID:            263
# Pack:          Pack 003 (201–300)
# Original Name: Anchor Spiral Projector
# Manifest Name: Anchor Spiral Projector
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_263(n: int, *, clockwise: bool = True) -> List[Tuple[int, int]]:
    """
    Anchor Spiral Projector — emit (y,x) lattice coordinates in a center-out spiral.

    Overview
    --------
    Deterministically enumerates coordinates along a spiral path beginning at center.

    Parameters
    ----------
    n : int
        Side length (n >= 1).
    clockwise : bool, optional (default: True)

    Returns
    -------
    List[Tuple[int,int]]
        Spiral path coordinates in visitation order.

    Examples
    --------
    >>> glyph_263(3)
    [(1, 1), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2)]

    Exceptions
    ----------
    - ValueError : if n < 1.

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n^2)
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    c = n // 2
    x = y = c
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    if not clockwise:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    out: List[Tuple[int,int]] = [(y, x)]
    step = 1
    while len(out) < n*n:
        for dxi, dyi in dirs:
            for _ in range(step):
                if len(out) >= n*n: break
                x += dxi; y += dyi
                if 0 <= x < n and 0 <= y < n:
                    out.append((y, x))
            if (dxi, dyi) in (dirs[1], dirs[3]):
                step += 1
    return out
