# glyph_161.py — Dimensional Thread Divider
# -----------------------------------------------------------------------------
# ID:            161
# Pack:          Pack 002 (101–200)
# Name:          Dimensional Thread Divider
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

def glyph_161(seq: Sequence[int], *, threads: int) -> List[List[int]]:
    """
    Dimensional Thread Divider — round-robin partition into `threads` lanes.

    Overview
    --------
    Distributes items across `threads` by original index modulo `threads`. This
    preserves temporal order within each lane while maximizing separation.

    Parameters
    ----------
    seq : Sequence[int]
    threads : int

    Returns
    -------
    List[List[int]]
        Lanes of items (length == threads). Empty if threads < 1.

    Examples
    --------
    >>> glyph_161([0,1,2,3,4,5], threads=3)
    [[0, 3], [1, 4], [2, 5]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if threads < 1:
        return []
    out: List[List[int]] = [[] for _ in range(threads)]
    for i, v in enumerate(seq):
        out[i % threads].append(int(v))
    return out
