# glyph_215.py — Frequency Pattern Limiter
# -----------------------------------------------------------------------------
# ID:            215
# Pack:          Pack 003 (201–300)
# Name:          Frequency Pattern Limiter
# Class:         filter
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_215(seq: Sequence[float], *, topk: int = 3) -> List[float]:
    """
    Frequency Pattern Limiter — keep strongest naive DFT bins and reconstruct.

    Overview
    --------
    O(n^2) DFT → zero weak bins → inverse DFT. Deterministic, pure.

    Parameters
    ----------
    seq : Sequence[float]
    topk : int, optional (default: 3)

    Returns
    -------
    List[float]
        Limited-band reconstruction.

    Examples
    --------
    >>> glyph_215([0,1,0,-1]*4, topk=1)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0 or topk <= 0:
        return [0.0] * n
    # forward DFT
    mags = []
    Re = [0.0] * n
    Im = [0.0] * n
    for k in range(n):
        sr = si = 0.0
        for t, v in enumerate(x):
            ang = -2.0 * math.pi * k * t / n
            sr += v * math.cos(ang)
            si += v * math.sin(ang)
        Re[k], Im[k] = sr, si
        mags.append((k, (sr*sr + si*si) ** 0.5))
    keep = {k for k, _ in sorted(mags, key=lambda kv: -kv[1])[:topk]}
    # inverse DFT with kept bins
    y = [0.0] * n
    for t in range(n):
        s = 0.0
        for k in range(n):
            if k in keep:
                ang = 2.0 * math.pi * k * t / n
                s += Re[k]*math.cos(ang) - Im[k]*math.sin(ang)
        y[t] = s / n
    return y
