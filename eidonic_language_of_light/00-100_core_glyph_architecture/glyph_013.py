# glyph_013.py — Quantum Field Stabilizer
# -----------------------------------------------------------------------------
# ID:            013
# Pack:          Pack 001 (000–100)
# Name:          Quantum Field Stabilizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_013(field: Sequence[Sequence[float]], *, window: int = 3) -> List[List[float]]:
    """
    Quantum Field Stabilizer — median filter on a 2D field (odd window).

    Overview
    --------
    Robustly suppresses salt-and-pepper noise while preserving edges.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    window : int, optional (default: 3)

    Returns
    -------
    List[List[float]]
        Filtered field.

    Examples
    --------
    >>> glyph_013([[0,9,0],[0,1,0],[0,9,0]], window=3)  # doctest: +ELLIPSIS
    [...]
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")
    A = [list(map(float, row)) for row in field]
    if not A or not A[0]:
        return []
    H,W = len(A), len(A[0])
    k = window//2
    out = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            vals = []
            for dy in range(-k, k+1):
                for dx in range(-k, k+1):
                    yy = min(max(y+dy, 0), H-1)
                    xx = min(max(x+dx, 0), W-1)
                    vals.append(A[yy][xx])
            vals.sort()
            out[y][x] = vals[len(vals)//2]
    return out
