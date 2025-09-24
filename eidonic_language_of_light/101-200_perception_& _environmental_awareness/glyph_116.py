# glyph_116.py — Time Thread Distributor
# -----------------------------------------------------------------------------
# ID:            116
# Pack:          Pack 002 (101–200)
# Name:          Time Thread Distributor
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

def glyph_116(seq: Sequence[int], *, bins: int) -> List[List[int]]:
    """
    Time Thread Distributor — route events into modulo bins.

    Overview
    --------
    Bin i receives elements whose original index % bins == i.

    Parameters
    ----------
    seq : Sequence[int]
    bins : int

    Returns
    -------
    List[List[int]]
        Bins of events.

    Examples
    --------
    >>> glyph_116([10,11,12,13,14], bins=2)
    [[10, 12, 14], [11, 13]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if bins < 1:
        return []
    out: List[List[int]] = [[] for _ in range(bins)]
    for i, v in enumerate(seq):
        out[i % bins].append(int(v))
    return out
