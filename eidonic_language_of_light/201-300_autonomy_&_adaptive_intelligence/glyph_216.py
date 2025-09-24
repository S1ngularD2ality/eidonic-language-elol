# glyph_216.py — Dream Gate Divider
# -----------------------------------------------------------------------------
# ID:            216
# Pack:          Pack 003 (201–300)
# Name:          Dream Gate Divider
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_216(seq: Sequence[int], *, gates: int = 2) -> List[List[int]]:
    """
    Dream Gate Divider — partition by index modulo `gates`.

    Overview
    --------
    Splits a sequence into `gates` lanes preserving order within each lane.

    Parameters
    ----------
    seq : Sequence[int]
    gates : int, optional (default: 2)

    Returns
    -------
    List[List[int]]
        Partitioned lanes (length == gates).

    Examples
    --------
    >>> glyph_216([10,11,12,13,14], gates=3)
    [[10, 13], [11, 14], [12]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    g = max(1, int(gates))
    out = [[] for _ in range(g)]
    for i, v in enumerate(seq):
        out[i % g].append(int(v))
    return out
