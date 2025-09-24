# glyph_075.py — Quantum Lens Redirector
# -----------------------------------------------------------------------------
# ID:            075
# Pack:          Pack 001 (000–100)
# Name:          Quantum Lens Redirector
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

def glyph_075(grid: Sequence[Sequence[float]], lens: Sequence[Tuple[int,int,float]], *, decay: float = 1.0) -> List[List[float]]:
    """
    Quantum Lens Redirector — multiplicative modulation by exponential lenses.

    Overview
    --------
    Each lens at (x,y,w) multiplies cells by (1 + w * exp(-decay * distance)).

    Parameters
    ----------
    grid : Sequence[Sequence[float]]
    lens : Sequence[Tuple[int,int,float]]
    decay : float, optional (default: 1.0)

    Returns
    -------
    List[List[float]]
        Modulated grid.

    Examples
    --------
    >>> glyph_075([[1,1],[1,1]], [(0,0,1.0)], decay=1.0)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W·L)
    - Space : O(H·W)
    """
    import math
    A = [list(map(float, row)) for row in grid]
    if not A or not A[0]:
        return []
    H,W = len(A), len(A[0])
    out = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            m = 1.0
            for lx, ly, w in lens:
                d = math.hypot(x-lx, y-ly)
                m *= (1.0 + float(w) * math.exp(-decay * d))
            out[y][x] = A[y][x] * m
    return out
