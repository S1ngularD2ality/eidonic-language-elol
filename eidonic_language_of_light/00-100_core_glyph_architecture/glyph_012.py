# glyph_012.py — Threshold Frequency Shifter
# -----------------------------------------------------------------------------
# ID:            012
# Pack:          Pack 001 (000–100)
# Name:          Threshold Frequency Shifter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_012(seq: Sequence[float], *, threshold: float, shift: int = 1) -> List[float]:
    """
    Threshold Frequency Shifter — move DFT bins above a magnitude threshold.

    Overview
    --------
    Naive O(n^2) DFT → circularly shift bins with |X[k]| ≥ threshold by `shift` →
    inverse DFT.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float
    shift : int, optional (default: 1)

    Returns
    -------
    List[float]
        Shifted time series.

    Examples
    --------
    >>> glyph_012([0,1,0,-1]*4, threshold=1.0, shift=1)  # doctest: +ELLIPSIS
    [...]
    """
    n = len(seq)
    if n == 0:
        return []
    Xr = [0.0]*n; Xi = [0.0]*n
    for k in range(n):
        sr = si = 0.0
        for t, x in enumerate(seq):
            ang = -2.0*math.pi*k*t/n
            sr += float(x)*math.cos(ang); si += float(x)*math.sin(ang)
        Xr[k], Xi[k] = sr, si
    mags = [math.hypot(Xr[k], Xi[k]) for k in range(n)]
    Yr = [0.0]*n; Yi = [0.0]*n
    for k in range(n):
        nk = (k + (shift if mags[k] >= threshold else 0)) % n
        Yr[nk], Yi[nk] = Xr[k], Xi[k]
    y = [0.0]*n
    for t in range(n):
        sr = si = 0.0
        for k in range(n):
            ang = 2.0*math.pi*k*t/n
            sr += Yr[k]*math.cos(ang) - Yi[k]*math.sin(ang)
            si += Yr[k]*math.sin(ang) + Yi[k]*math.cos(ang)
        y[t] = sr/n
    return y
