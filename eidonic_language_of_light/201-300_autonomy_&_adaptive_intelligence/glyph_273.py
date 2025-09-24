# glyph_273.py — Anchor Pattern Shuffler
# -----------------------------------------------------------------------------
# ID:            273
# Pack:          Pack 003 (201–300)
# Original Name: Anchor Pattern Shuffler
# Manifest Name: Anchor Pattern Shuffler
# Class:         combinator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List, TypeVar
T = TypeVar("T")

def glyph_273(parts: Sequence[Sequence[T]]) -> List[T]:
    """
    Anchor Pattern Shuffler — interleave streams one-by-one (round-robin).

    Overview
    --------
    Pulls one item from each non-empty stream per round; preserves intra-stream order.

    Parameters
    ----------
    parts : Sequence[Sequence[T]]

    Returns
    -------
    List[T]
        Shuffled (interleaved) stream.

    Examples
    --------
    >>> glyph_273([[1,2,3],[10,20]])
    [1, 10, 2, 20, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(total_len)
    - Space : O(total_len)
    """
    P=[list(p) for p in parts]
    out: List[T]=[]
    pos=[0]*len(P)
    remaining=sum(len(p) for p in P)
    while remaining:
        for i,p in enumerate(P):
            if pos[i] < len(p):
                out.append(p[pos[i]]); pos[i]+=1; remaining-=1
    return out
