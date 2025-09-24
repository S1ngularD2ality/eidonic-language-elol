# glyph_023.py — Recursive Cycle Indexer
# -----------------------------------------------------------------------------
# ID:            023
# Pack:          Pack 001 (000–100)
# Name:          Recursive Cycle Indexer
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_023(seq: Sequence[int], *, base: int) -> List[int]:
    """
    Recursive Cycle Indexer — assign indices modulo a recursive base.

    Overview
    --------
    Returns i % base for each position, then applies the same modulo on the quotient
    to produce a hierarchical index stream flattened at level 0.

    Parameters
    ----------
    seq : Sequence[int]
        Sequence whose length drives the indexing (values are ignored).
    base : int
        Modulus for the cycle (>= 2).

    Returns
    -------
    List[int]
        Primary modulo indices for each element.

    Examples
    --------
    >>> glyph_023([0]*7, base=3)
    [0,1,2,0,1,2,0]

    Exceptions
    ----------
    - ValueError : if base < 2.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if base < 2:
        raise ValueError("base must be >= 2")
    n = len(seq)
    return [i % base for i in range(n)]
