# glyph_291.py — Flame Cycle Disassembler
# -----------------------------------------------------------------------------
# ID:            291
# Pack:          Pack 003 (201–300)
# Name:          Flame Cycle Disassembler
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_291(seq: Sequence[int], *, phases: int) -> List[List[int]]:
    """
    Flame Cycle Disassembler — partition indices by phase lanes.

    Overview
    --------
    Groups positions i by (i % phases).

    Parameters
    ----------
    seq : Sequence[int]
    phases : int

    Returns
    -------
    List[List[int]]
        Phase buckets.

    Examples
    --------
    >>> glyph_291(range(7), phases=3)
    [[0,3,6],[1,4],[2,5]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    p = max(1, int(phases))
    out = [[] for _ in range(p)]
    for i, _ in enumerate(seq):
        out[i % p].append(i)
    return out
