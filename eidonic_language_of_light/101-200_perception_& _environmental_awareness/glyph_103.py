# glyph_103.py — Subconscious Signal Combiner
# -----------------------------------------------------------------------------
# ID:            103
# Pack:          Pack 002 (101–200)
# Name:          Subconscious Signal Combiner
# Class:         combinator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_103(streams: Sequence[Sequence[float]], weights: Sequence[float]) -> List[float]:
    """
    Subconscious Signal Combiner — weighted sum across aligned streams.

    Overview
    --------
    Aligns by the shortest stream length; returns Σ_j w_j * x_j[i].

    Parameters
    ----------
    streams : Sequence[Sequence[float]]
    weights : Sequence[float]  # len(weights) == len(streams)

    Returns
    -------
    List[float]
        Combined stream.

    Examples
    --------
    >>> glyph_103([[1,2,3],[10,20,30]], [0.5, 0.5])
    [5.5, 11.0, 16.5]

    Exceptions
    ----------
    - ValueError : if len(weights) != len(streams).

    Complexity
    ----------
    - Time  : O(m·n)
    - Space : O(n)
    """
    if not streams:
        return []
    if len(weights) != len(streams):
        raise ValueError("weights length must match number of streams")
    m = min(len(s) for s in streams)
    w = [float(v) for v in weights]
    out: List[float] = [0.0]*m
    for j, s in enumerate(streams):
        for i in range(m):
            out[i] += w[j]*float(s[i])
    return out
