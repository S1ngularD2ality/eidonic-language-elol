# glyph_296.py — Quantum Mirror Streamliner
# -----------------------------------------------------------------------------
# ID:            296
# Pack:          Pack 003 (201–300)
# Name:          Quantum Mirror Streamliner
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_296(seq: Sequence[float], *, period: int, mix: float = 0.5) -> List[float]:
    """
    Quantum Mirror Streamliner — blend with dominant cosine mode.

    Overview
    --------
    Projects onto cos(2πt/period), mixes with original by `mix`∈[0,1].

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    mix : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Streamlined signal.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if period < 2: return [float(v) for v in seq]
    x=[float(v) for v in seq]; n=len(x)
    if n==0: return []
    w=2.0*math.pi/period
    a=sum(x[t]*math.cos(w*t) for t in range(n))*2.0/n
    c=sum(x)/n
    m=max(0.0, min(1.0, float(mix)))
    cosc=[c + a*math.cos(w*t) for t in range(n)]
    return [(1-m)*x[t] + m*cosc[t] for t in range(n)]
