# glyph_123.py — Liminal Mirror Reconnector
# -----------------------------------------------------------------------------
# ID:            123
# Pack:          Pack 002 (101–200)
# Name:          Liminal Mirror Reconnector
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_123(left: Sequence[T], right: Sequence[T]) -> List[T]:
    """
    Liminal Mirror Reconnector — interleave two sequences from opposite ends.

    Overview
    --------
    Emits [L0, Rn-1, L1, Rn-2, ...] up to exhaustion; length equals |L|+|R|.

    Parameters
    ----------
    left  : Sequence[T]
    right : Sequence[T]

    Returns
    -------
    List[T]
        Reconnected stream.

    Examples
    --------
    >>> glyph_123([1,2,3],[9,8])
    [1, 8, 2, 9, 3]
    """
    L = list(left)
    R = list(right)[::-1]
    out: List[T] = []
    i = j = 0
    while i < len(L) or j < len(R):
        if i < len(L): out.append(L[i]); i += 1
        if j < len(R): out.append(R[j]); j += 1
    return out
