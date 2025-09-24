# glyph_196.py — Dream Sequence Tracker
# -----------------------------------------------------------------------------
# ID:            196
# Pack:          Pack 002 (101–200)
# Name:          Dream Sequence Tracker
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_196(seq: Sequence[float]) -> List[int]:
    """
    Dream Sequence Tracker — running argmax indices.

    Overview
    --------
    Returns index of the maximum seen so far for each position.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[int]
        Argmax prefix indices.

    Examples
    --------
    >>> glyph_196([1,3,2,5,4])
    [0, 1, 1, 3, 3]
    """
    best_idx = -1
    best_val = float("-inf")
    out: List[int] = []
    for i, v in enumerate(seq):
        fv = float(v)
        if fv > best_val:
            best_val = fv; best_idx = i
        out.append(best_idx)
    return out
