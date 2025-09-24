# glyph_092.py — Frequency Loop Binder
# -----------------------------------------------------------------------------
# ID:            092
# Pack:          Pack 001 (000–100)
# Name:          Frequency Loop Binder
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

def glyph_092(seq: Sequence[float], *, period: int) -> List[float]:
    """
    Frequency Loop Binder — match-and-blend toward a target periodic template.

    Overview
    --------
    Projects `seq` onto a sine/cosine pair with the given integer period and
    reconstructs the best-fit sinusoid.

    Parameters
    ----------
    seq : Sequence[float]
    period : int
        Fundamental samples per cycle (>= 2).

    Returns
    -------
    List[float]
        Bound periodic approximation.

    Examples
    --------
    >>> glyph_092([0,1,0,-1]*4, period=4)  # doctest: +ELLIPSIS
    [...]
    """
    if period < 2:
        return [float(v) for v in seq]
    n = len(seq)
    if n == 0:
        return []
    x = [float(v) for v in seq]
    w = 2.0 * math.pi / period
    a = sum(x[t] * math.cos(w * t) for t in range(n)) * 2.0 / n
    b = sum(x[t] * math.sin(w * t) for t in range(n)) * 2.0 / n
    c = sum(x) / n
    return [c + a * math.cos(w * t) + b * math.sin(w * t) for t in range(n)]
