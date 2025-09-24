# glyph_178.py — Frequency Cascade Shuffler
# -----------------------------------------------------------------------------
# ID:            178
# Pack:          Pack 002 (101–200)
# Name:          Frequency Cascade Shuffler
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

def glyph_178(seq: Sequence[float], *, perm: Sequence[int]) -> List[float]:
    """
    Frequency Cascade Shuffler — shuffle naive DFT bins then invert.

    Overview
    --------
    Computes O(n^2) DFT, permutes frequency bins by `perm` (mod n), and performs
    inverse DFT to reconstruct a shuffled signal.

    Parameters
    ----------
    seq : Sequence[float]
    perm : Sequence[int]

    Returns
    -------
    List[float]
        Reconstructed sequence after bin shuffle.
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return []
    # forward DFT
    Xr = [0.0]*n; Xi = [0.0]*n
    for k in range(n):
        sr = si = 0.0
        for t, v in enumerate(x):
            ang = -2.0*math.pi*k*t/n
            sr += v*math.cos(ang)
            si += v*math.sin(ang)
        Xr[k], Xi[k] = sr, si
    # permute
    p = [int(i) % n for i in perm] or list(range(n))
    Yr = [0.0]*n; Yi = [0.0]*n
    for k, pk in enumerate(p):
        Yr[k], Yi[k] = Xr[pk], Xi[pk]
    # inverse DFT
    y = [0.0]*n
    for t in range(n):
        sr = si = 0.0
        for k in range(n):
            ang = 2.0*math.pi*k*t/n
            sr += Yr[k]*math.cos(ang) - Yi[k]*math.sin(ang)
            si += Yr[k]*math.sin(ang) + Yi[k]*math.cos(ang)
        y[t] = sr/n
    return y
