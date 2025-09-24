# glyph_070.py — Thoughtform Spiral Resolver
# -----------------------------------------------------------------------------
# ID:            070
# Pack:          Pack 001 (000–100)
# Name:          Thoughtform Spiral Resolver
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple

def glyph_070(grid: Sequence[Sequence[float]]) -> Tuple[int, int]:
    """
    Thoughtform Spiral Resolver — find grid center by maximal radial symmetry.

    Overview
    --------
    Estimates the coordinates with minimal mean absolute difference under 180°
    rotation (mirror across center), interpreted as the spiral's core.

    Parameters
    ----------
    grid : Sequence[Sequence[float]]
        2D field.

    Returns
    -------
    (int, int)
        Estimated center (x, y).

    Examples
    --------
    >>> glyph_070([[0,1,0],[1,2,1],[0,1,0]])
    (1, 1)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(1)
    """
    A = [list(map(float, row)) for row in grid]
    if not A or not A[0]:
        return (0, 0)
    H, W = len(A), len(A[0])
    best = (0, 0)
    best_err = float("inf")
    for cy in range(H):
        for cx in range(W):
            err = 0.0
            for y in range(H):
                for x in range(W):
                    mx = 2*cx - x
                    my = 2*cy - y
                    if 0 <= mx < W and 0 <= my < H:
                        err += abs(A[y][x] - A[my][mx])
            if err < best_err:
                best_err = err
                best = (cx, cy)
    return best
