# glyph_257.py — Harmonic Index Collapser
# -----------------------------------------------------------------------------
# ID:            257
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Index Collapser
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_257(seq: Sequence[float]) -> List[int]:
    """
    Harmonic Index Collapser — running argmax indices.

    Overview
    --------
    For each position, record index of the largest value seen so far.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[int]
        Argmax prefix.

    Examples
    --------
    >>> glyph_257([1,3,2,5,4])
    [0,1,1,3,3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    best_i = -1
    best_v = float("-inf")
    out: List[int] = []
    for i, v in enumerate(seq):
        fv = float(v)
        if fv > best_v:
            best_v = fv; best_i = i
        out.append(best_i)
    return out
