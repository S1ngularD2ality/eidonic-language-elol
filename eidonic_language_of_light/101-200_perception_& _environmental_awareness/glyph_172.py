# glyph_172.py — Mirror Field Refiner
# -----------------------------------------------------------------------------
# ID:            172
# Pack:          Pack 002 (101–200)
# Name:          Mirror Field Refiner
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

def glyph_172(field: Sequence[Sequence[float]], *, window: int = 3) -> List[List[float]]:
    """
    Mirror Field Refiner — smooth then enforce mirror symmetry.

    Overview
    --------
    Applies mean filter with edge clamping; then averages each cell with its
    mirrored counterpart across both axes.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    window : int, optional (default: 3)

    Returns
    -------
    List[List[float]]
        Refined, symmetric field.
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return []
    H, W = len(A), len(A[0]); k = window//2
    # mean filter
    B = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            acc=cnt=0.0
            for dy in range(-k,k+1):
                for dx in range(-k,k+1):
                    yy=min(max(y+dy,0),H-1)
                    xx=min(max(x+dx,0),W-1)
                    acc += A[yy][xx]; cnt += 1
            B[y][x]=acc/cnt
    # mirror enforce
    C = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            C[y][x] = 0.5*(B[y][x] + B[H-1-y][W-1-x])
    return C
