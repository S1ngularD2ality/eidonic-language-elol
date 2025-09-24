# glyph_191.py — Frequency Gate Tetherer
# -----------------------------------------------------------------------------
# ID:            191
# Pack:          Pack 002 (101–200)
# Name:          Frequency Gate Tetherer
# Class:         filter
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

def glyph_191(seq: Sequence[float], *, topk: int = 3) -> List[float]:
    """
    Frequency Gate Tetherer — keep strongest naive DFT bins and reconstruct.

    Overview
    --------
    Computes O(n^2) DFT, zeros all but top-|X_k| magnitudes, inverse transforms.

    Parameters
    ----------
    seq : Sequence[float]
    topk : int, optional (default: 3)

    Returns
    -------
    List[float]
        Tethered (sparsified) signal.
    """
    n = len(seq)
    if n == 0 or topk <= 0:
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
    keep = {it[3] for it in X[:topk]}
    Yr=[0.0]*n; Yi=[0.0]*n
    for sr,si,mag,k in X:
        if k in keep:
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
