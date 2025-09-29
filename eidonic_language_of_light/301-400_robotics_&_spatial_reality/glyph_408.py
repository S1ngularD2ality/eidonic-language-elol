# glyph_408.py — Attention Arbiter
# -----------------------------------------------------------------------------
# ID:            408
# Pack:          Pack 005 (401–500)
# Name:          Attention Arbiter
# Class:         selector
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping

def glyph_408(events: Sequence[Mapping[str, float]], *, w_priority: float = 1.0, w_recency: float = 0.5) -> int:
    """
    Attention Arbiter — pick index maximizing weighted (priority + recency).

    Overview
    --------
    Computes score = ``w_priority*priority + w_recency*recency``; returns argmax index.

    Parameters
    ----------
    events    : Sequence[{'priority':float,'recency':float}]
    w_priority: float, optional (default: 1.0)
    w_recency : float, optional (default: 0.5)

    Returns
    -------
    int : selected event index, or -1 if empty.

    Examples
    --------
    >>> glyph_408([{'priority':1,'recency':0.9},{'priority':2,'recency':0.0}])
    1

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    best, idx = float("-inf"), -1
    for i, e in enumerate(events):
        score = w_priority * float(e.get("priority", 0.0)) + w_recency * float(e.get("recency", 0.0))
        if score > best:
            best, idx = score, i
    return idx
