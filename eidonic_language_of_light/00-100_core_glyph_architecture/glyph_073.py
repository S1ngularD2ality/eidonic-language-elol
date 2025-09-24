# glyph_073.py — Lightflow Frequency Bender
# -----------------------------------------------------------------------------
# ID:            073
# Pack:          Pack 001 (000–100)
# Name:          Lightflow Frequency Bender
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List
import math

def glyph_073(seq: Sequence[float], *, threshold: float, shift: int = 1) -> List[float]:
    """
    Lightflow Frequency Bender — selective frequency-bin rotation (DFT).

    Overview
    --------
    Computes a naive DFT, shifts bins whose magnitude ≥ threshold by `shift`,
    then inverse-transforms. Portable O(n^2) implementation.

    Parameters
    ----------
    seq : Sequence[float]
        Real input samples.
    threshold : float
        Magnitude cutoff.
    shift : int, optional (default: 1)
        Circular shift of selected bins (can be negative).

    Returns
    -------
    List[float]
        Time-domain sequence after bending.

    Examples
    --------
    >>> glyph_073([0,1,0,-1]*8, threshold=1.0, shift=1)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    n = len(seq)
    if n == 0:
        return []
    Xr = [0.0]*n; Xi = [0.0]*n
    for k in range(n):
        sr = si = 0.0
        for t, x in enumerate(seq):
            ang = -2.0*math.pi*k*t/n
            sr += float(x)*math.cos(ang)
            si += float(x)*math.sin(ang)
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
