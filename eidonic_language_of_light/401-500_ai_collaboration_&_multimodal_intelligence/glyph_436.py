# glyph_436.py — Multi-Stream Mixer
# -----------------------------------------------------------------------------
# ID:            436
# Pack:          Pack 005 (401–500)
# Name:          Multi-Stream Mixer
# Class:         mixer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_436(streams: Sequence[Sequence[float]], weights: Sequence[float]) -> List[float]:
    """
    Multi-Stream Mixer — weighted sum of equal-length streams.

    Overview
    --------
    Uses the first K=min(len(streams),len(weights)) streams; truncates to shortest length.

    Parameters
    ----------
    streams : Sequence[Sequence[float]]
    weights : Sequence[float]

    Returns
    -------
    List[float]

    Examples
    --------
    >>> glyph_436([[1,1],[2,2]], [0.5, 0.5])
    [1.5, 1.5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(K·M)
    - Space : O(M)
    """
    if not streams or not weights:
        return []
    k = min(len(streams), len(weights))
    m = min(len(s) for s in streams[:k]) if k else 0
    out = [0.0]*m
    for s, w in zip(streams[:k], weights[:k]):
        for i in range(m):
            out[i] += float(w)*float(s[i])
    return out
