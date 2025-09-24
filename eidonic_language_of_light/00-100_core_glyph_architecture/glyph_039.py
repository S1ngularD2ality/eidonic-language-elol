# glyph_039.py — Perceptual Grid Regulator
# -----------------------------------------------------------------------------
# ID:            039
# Pack:          Pack 001 (000–100)
# Name:          Perceptual Grid Regulator
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_039(grid: Sequence[Sequence[float]], *, window: int = 3) -> List[List[float]]:
    """
    Perceptual Grid Regulator — local mean-variance normalization (2D).

    Overview
    --------
    For each cell, subtract neighborhood mean and divide by neighborhood std (≥1e-6).

    Parameters
    ----------
    grid : Sequence[Sequence[float]]
    window : int, optional (default: 3)
        Odd window size.

    Returns
    -------
    List[List[float]]
        Locally normalized grid.
    """
    if window<1 or window%2==0: raise ValueError("window must be odd >=1")
    A=[list(map(float,row)) for row in grid]
    if not A or not A[0]: return []
    H,W=len(A),len(A[0])
    k=window//2
    out=[[0.0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            vals=[]
            for dy in range(-k,k+1):
                for dx in range(-k,k+1):
                    yy=min(max(y+dy,0),H-1)
                    xx=min(max(x+dx,0),W-1)
                    vals.append(A[yy][xx])
            m=sum(vals)/len(vals)
            var=sum((v-m)**2 for v in vals)/len(vals)
            s=(var**0.5) or 1e-6
            out[y][x]=(A[y][x]-m)/s
    return out
