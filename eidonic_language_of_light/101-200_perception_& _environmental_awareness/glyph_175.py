# glyph_175.py — Dream Cycle Enhancer
# -----------------------------------------------------------------------------
# ID:            175
# Pack:          Pack 002 (101–200)
# Name:          Dream Cycle Enhancer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_175(seq: Sequence[float], *, period: int, strength: float = 1.2) -> List[float]:
    """
    Dream Cycle Enhancer — boost a periodic component.

    Overview
    --------
    Projects onto sin/cos of integer `period` and amplifies the component by
    `strength`, leaving the DC component unchanged.

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    strength : float, optional (default: 1.2)

    Returns
    -------
    List[float]
        Enhanced signal.
    """
    import math
    if period < 2:
        return [float(v) for v in seq]
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return []
    w = 2.0*math.pi/period
    a = sum(x[t]*math.cos(w*t) for t in range(n))*2.0/n
    b = sum(x[t]*math.sin(w*t) for t in range(n))*2.0/n
    c = sum(x)/n
    g = float(strength)
    return [c + g*(a*math.cos(w*t) + b*math.sin(w*t)) for t in range(n)]
