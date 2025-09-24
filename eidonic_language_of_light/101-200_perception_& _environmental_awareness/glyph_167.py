# glyph_167.py — Symbolic Spiral Disassembler
# -----------------------------------------------------------------------------
# ID:            167
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Spiral Disassembler
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_167(grid: Sequence[Sequence[int]], *, clockwise: bool = True) -> List[int]:
    """
    Symbolic Spiral Disassembler — read out a grid along a spiral path.

    Overview
    --------
    Emits values encountered when traversing the grid in a center-out spiral,
    clockwise or counter-clockwise.

    Parameters
    ----------
    grid : Sequence[Sequence[int]]
    clockwise : bool, optional (default: True)

    Returns
    -------
    List[int]
        Linearized spiral order.

    Examples
    --------
    >>> glyph_167([[0,1],[2,3]], clockwise=True)  # doctest: +ELLIPSIS
    [...]
    """
    A = [list(row) for row in grid]
    if not A or not A[0]:
        return []
    n, m = len(A), len(A[0])
    cy, cx = n//2, m//2
    dirs = [(0,1),(1,0),(0,-1),(-1,0)] if clockwise else [(1,0),(0,1),(-1,0),(0,-1)]
    y, x = cy, cx
    out = [A[y][x]]
    step = 1
    def inside(y,x): return 0 <= y < n and 0 <= x < m
    while len(out) < n*m:
        for dyi, dxi in dirs:
            for _ in range(step):
                if len(out) >= n*m: break
                y += dyi; x += dxi
                if inside(y,x):
                    out.append(A[y][x])
            if (dyi,dxi) in (dirs[1], dirs[3]):
                step += 1
    return out
