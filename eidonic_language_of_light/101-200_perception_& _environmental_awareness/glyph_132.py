# glyph_132.py — Frequency Filter Converger
# -----------------------------------------------------------------------------
# ID:            132
# Pack:          Pack 002 (101–200)
# Name:          Frequency Filter Converger
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_132(seq: Sequence[float], *, keep: int = 3) -> List[float]:
    """
    Frequency Filter Converger — keep top-|X_k| DFT bins, zero the rest (naive).

    Overview
    --------
    Computes O(n^2) DFT, preserves `keep` largest magnitudes, inverse transforms.

    Parameters
    ----------
    seq : Sequence[float]
    keep : int, optional (default: 3)

    Returns
    -------
    List[float]
        Reconstructed series with reduced spectral support.
    """
    n = len(seq)
    if n == 0 or keep <= 0:
        return [0.0]*n
    X = []
    for k in range(n):
        sr=si=0.0
        for t, v in enumerate(seq):
            ang=-2.0*math.pi*k*t/n
            sr += float(v)*math.cos(ang)
            si += float(v)*math.sin(ang)
        X.append([sr, si, (sr*sr+si*si)**0.5, k])
    X.sort(key=lambda it: -it[2])
    mask = {it[3] for it in X[:keep]}
    Yr=[0.0]*n; Yi=[0.0]*n
    for sr,si,mag,k in X:
        if k in mask:
            Yr[k]=sr; Yi[k]=si
    y=[0.0]*n
    for t in range(n):
        sr=si=0.0
        for k in range(n):
            ang=2.0*math.pi*k*t/n
            sr += Yr[k]*math.cos(ang) - Yi[k]*math.sin(ang)
            si += Yr[k]*math.sin(ang) + Yi[k]*math.cos(ang)
        y[t]=sr/n
    return y
