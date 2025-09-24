# glyph_155.py — Anchor Field Stabilizer
# -----------------------------------------------------------------------------
# ID:            155
# Pack:          Pack 002 (101–200)
# Name:          Anchor Field Stabilizer
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

def glyph_155(field: Sequence[Sequence[float]], *, window: int = 3) -> List[List[float]]:
    """
    Anchor Field Stabilizer — 2D mean filter with edge clamping.

    Overview
    --------
    For each cell, average values in an odd window with boundary replication.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    window : int, optional (default: 3)

    Returns
    -------
    List[List[float]]
        Stabilized field.
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]: return []
    H, W = len(A), len(A[0]); k = window//2
    out = [[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            acc = 0.0; cnt = 0
            for dy in range(-k, k+1):
                for dx in range(-k, k+1):
                    yy = min(max(y+dy,0),H-1)
                    xx = min(max(x+dx,0),W-1)
                    acc += A[yy][xx]; cnt += 1
            out[y][x] = acc / cnt
    return out
