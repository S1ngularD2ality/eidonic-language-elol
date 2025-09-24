# glyph_093.py — Dream Phase Fracturer
# -----------------------------------------------------------------------------
# ID:            093
# Pack:          Pack 001 (000–100)
# Name:          Dream Phase Fracturer
# Class:         analyzer
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

def glyph_093(seq: Sequence[float], *, window: int = 8) -> List[float]:
    """
    Dream Phase Fracturer — local phase jump detector.

    Overview
    --------
    Computes sliding-window wrapped phase and outputs absolute phase differences
    between adjacent windows (proxy for sudden transitions).

    Parameters
    ----------
    seq : Sequence[float]
    window : int, optional (default: 8)

    Returns
    -------
    List[float]
        Phase jump magnitudes (length n).

    Examples
    --------
    >>> glyph_093([0,1,0,-1]*4, window=4)  # doctest: +ELLIPSIS
    [...]
    """
    n = len(seq)
    if n == 0 or window < 2:
        return [0.0] * n
    w = max(2, int(window))
    def phase(t0: int) -> float:
        xs = [float(v) for v in seq[t0:t0+w]]
        if not xs:
            return 0.0
        # crude quadrature
        ys = [xs[i] - xs[i-1] if i>0 else 0.0 for i in range(len(xs))]
        p = math.atan2(sum(ys), sum(xs))
        return p
    out = [0.0]*n
    prev = phase(0)
    for i in range(1, n):
        cur = phase(max(0, i - w + 1))
        dp = abs((cur - prev + math.pi) % (2*math.pi) - math.pi)
        out[i] = dp
        prev = cur
    return out
