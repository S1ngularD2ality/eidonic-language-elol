# glyph_066.py — Polarity Layer Transmitter
# -----------------------------------------------------------------------------
# ID:            066
# Pack:          Pack 001 (000–100)
# Name:          Polarity Layer Transmitter
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_066(signs: Sequence[int], pos: Sequence[float], neg: Sequence[float]) -> List[float]:
    """
    Polarity Layer Transmitter — select values from positive/negative layers by sign.

    Overview
    --------
    For each index i, output `pos[i]` if `signs[i] >= 0`, else `neg[i]`.
    Useful for routing activations by instantaneous polarity.

    Parameters
    ----------
    signs : Sequence[int]
        Sign stream in {-1,0,1}.
    pos, neg : Sequence[float]
        Equal-length layers for positive and negative routes.

    Returns
    -------
    List[float]
        Routed values.

    Examples
    --------
    >>> glyph_066([1,0,-1], [10,20,30], [1,2,3])
    [10.0, 20.0, 3.0]

    Exceptions
    ----------
    - ValueError : on length mismatch.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(signs)
    if n != len(pos) or n != len(neg):
        raise ValueError("Input lengths must match")
    out: List[float] = []
    for i in range(n):
        out.append(float(pos[i]) if int(signs[i]) >= 0 else float(neg[i]))
    return out
