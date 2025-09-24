# glyph_060.py — Recursive Flame Filter
# -----------------------------------------------------------------------------
# ID:            060
# Pack:          Pack 001 (000–100)
# Name:          Recursive Flame Filter
# Class:         filter
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

def glyph_060(seq: Sequence[float], *, rounds: int = 2, k: float = 0.3) -> List[float]:
    """
    Recursive Flame Filter — iterated soft-threshold smoothing with neighbor pull.

    Overview
    --------
    Repeats: `m = mean(neighbors)`, `y = y + k * tanh(m - y)` with reflecting edges.
    Stabilizes without blurring sharp structures too aggressively.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    rounds : int, optional (default: 2)
        Number of iterations (>= 1).
    k : float, optional (default: 0.3)
        Pull strength; typically in [0,1].

    Returns
    -------
    List[float]
        Filtered sequence.

    Examples
    --------
    >>> glyph_060([0, 10, 0], rounds=3, k=0.5)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(rounds · n)
    - Space : O(n)
    """
    y = [float(v) for v in seq]
    n = len(y)
    if n == 0:
        return []
    r = max(1, int(rounds))
    kk = float(k)
    for _ in range(r):
        z = y[:]
        for i in range(n):
            a = z[i - 1] if i - 1 >= 0 else z[i]
            b = z[i + 1] if i + 1 < n else z[i]
            m = (a + z[i] + b) / 3.0
            y[i] = y[i] + kk * math.tanh(m - y[i])
    return y
