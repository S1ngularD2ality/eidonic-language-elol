# glyph_204.py — Dimensional Pathway Tuner
# -----------------------------------------------------------------------------
# ID:            204
# Pack:          Pack 003 (201–300)
# Name:          Dimensional Pathway Tuner
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_204(field: Sequence[Sequence[float]], *, window: int = 3) -> List[List[float]]:
    """
    Dimensional Pathway Tuner — 2D stride-1 mean filter with edge clamping.

    Overview
    --------
    Applies an odd-sized mean kernel to stabilize gradients and pathways.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    window : int, optional (default: 3)

    Returns
    -------
    List[List[float]]
        Tuned field.

    Exceptions
    ----------
    - ValueError : if window < 1 or even.

    Complexity
    ----------
    - Time  : O(H·W·window²)
    - Space : O(H·W)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]: return []
    H, W = len(A), len(A[0]); k = window//2
    out = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            acc=cnt=0.0
            for dy in range(-k,k+1):
                for dx in range(-k,k+1):
                    yy=min(max(y+dy,0),H-1)
                    xx=min(max(x+dx,0),W-1)
                    acc += A[yy][xx]; cnt += 1
            out[y][x]=acc/cnt
    return out
