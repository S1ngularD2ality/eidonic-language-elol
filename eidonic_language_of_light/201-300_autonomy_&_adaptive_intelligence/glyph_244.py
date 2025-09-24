# glyph_244.py — Recursive Phase Bender
# -----------------------------------------------------------------------------
# ID:            244
# Pack:          Pack 003 (201–300)
# Name:          Recursive Phase Bender
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_244(seq: Sequence[float], *, period: int, depth: int = 2, bend: float = 0.5) -> List[float]:
    """
    Recursive Phase Bender — iteratively mix with phase-shifted cosine.

    Overview
    --------
    At each depth i, y = 0.5*(y + cos(2πt/period + bend*i)).

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    depth : int, optional (default: 2)
    bend : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Bent signal.

    Examples
    --------
    >>> glyph_244([0,0,0,0], period=2, depth=1)
    [1.0, 0.0, -1.0, 0.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(depth·n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0 or period < 1:
        return x
    w = 2.0 * math.pi / max(1, period)
    y = x[:]
    for i in range(max(0, depth)):
        y = [0.5*(y[t] + math.cos(w*t + bend*i)) for t in range(n)]
    return y
