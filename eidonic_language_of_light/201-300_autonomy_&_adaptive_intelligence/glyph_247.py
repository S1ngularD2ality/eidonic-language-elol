# glyph_247.py — Spiral Intent Enhancer
# -----------------------------------------------------------------------------
# ID:            247
# Pack:          Pack 003 (201–300)
# Name:          Spiral Intent Enhancer
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_247(seq: Sequence[float], *, cutoff: float = 0.2) -> List[float]:
    """
    Spiral Intent Enhancer — one-pole low-pass smoothing.

    Overview
    --------
    y[0]=x[0]; y[t]=(1-c)*y[t-1]+c*x[t], c∈(0,1].

    Parameters
    ----------
    seq : Sequence[float]
    cutoff : float, optional (default: 0.2)

    Returns
    -------
    List[float]
        Smoothed signal.

    Examples
    --------
    >>> glyph_247([0,1,0,1], cutoff=0.5)
    [0.0, 0.5, 0.25, 0.625]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    c = max(1e-12, min(1.0, float(cutoff)))
    it = iter(seq)
    try:
        prev = float(next(it))
    except StopIteration:
        return []
    out = [prev]
    for v in it:
        prev = (1.0 - c) * prev + c * float(v)
        out.append(prev)
    return out
