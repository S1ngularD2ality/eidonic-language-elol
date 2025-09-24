# glyph_044.py — Spiral Harmonic Tracker
# -----------------------------------------------------------------------------
# ID:            044
# Pack:          Pack 001 (000–100)
# Name:          Spiral Harmonic Tracker
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

def glyph_044(seq: Sequence[float], *, base_period: int, harmonics: int = 4) -> List[float]:
    """
    Spiral Harmonic Tracker — correlate energy at base and harmonic periods.

    Overview
    --------
    For k in 1..H, compute the average product x[i]*x[i+k*base_period] across valid i.
    This approximates periodic energy aligned to multiples of `base_period`.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    base_period : int
        Fundamental lag (>= 1).
    harmonics : int, optional (default: 4)
        Number of multiples to score.

    Returns
    -------
    List[float]
        Length-`harmonics` scores.

    Examples
    --------
    >>> glyph_044([1,0,1,0,1,0], base_period=2, harmonics=2)
    [~0.5, ~0.5]

    Exceptions
    ----------
    - ValueError : if `base_period < 1` or `harmonics < 1`.

    Complexity
    ----------
    - Time  : O(H * n)
    - Space : O(1)
    """
    if base_period < 1:
        raise ValueError("base_period must be >= 1")
    H = max(1, int(harmonics))
    n = len(seq)
    if n == 0:
        return [0.0] * H
    x = [float(v) for v in seq]
    scores: List[float] = []
    for k in range(1, H + 1):
        p = k * base_period
        s = 0.0
        m = 0
        for i in range(n - p):
            s += x[i] * x[i + p]
            m += 1
        scores.append(s / max(1, m))
    return scores
