# glyph_183.py — Dimensional Flame Refiner
# -----------------------------------------------------------------------------
# ID:            183
# Pack:          Pack 002 (101–200)
# Name:          Dimensional Flame Refiner
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_183(field: Sequence[Sequence[float]], *, alpha: float = 0.6) -> List[List[float]]:
    """
    Dimensional Flame Refiner — unsharp mask on a 2D field.

    Overview
    --------
    Smooth with a 3×3 mean, then compute y = x + α(x - smooth).

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    alpha : float, optional (default: 0.6)

    Returns
    -------
    List[List[float]]
        Sharpened field.

    Examples
    --------
    >>> glyph_183([[1,2],[3,4]], alpha=0.5)  # doctest: +ELLIPSIS
    [[...], [...]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return []
    H, W = len(A), len(A[0])
    k = 1
    S = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            acc=cnt=0.0
            for dy in range(-k,k+1):
                for dx in range(-k,k+1):
                    yy=min(max(y+dy,0),H-1)
                    xx=min(max(x+dx,0),W-1)
                    acc += A[yy][xx]; cnt += 1
            S[y][x]=acc/cnt
    a = float(alpha)
    return [[A[y][x] + a*(A[y][x]-S[y][x]) for x in range(W)] for y in range(H)]
