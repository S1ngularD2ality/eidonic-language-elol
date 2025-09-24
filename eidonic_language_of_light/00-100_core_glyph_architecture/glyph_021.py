# glyph_021.py — Thought Path Weaver
# -----------------------------------------------------------------------------
# ID:            021
# Pack:          Pack 001 (000–100)
# Name:          Thought Path Weaver
# Class:         combinator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_021(paths: Sequence[Sequence[T]]) -> List[T]:
    """
    Thought Path Weaver — interleave multiple sequences using round-robin weaving.

    Overview
    --------
    Takes N paths and weaves them by drawing one token from each in order until all
    are exhausted. Shorter paths naturally finish earlier without padding.

    Parameters
    ----------
    paths : Sequence[Sequence[T]]
        The sequences to weave; may be of unequal lengths.

    Returns
    -------
    List[T]
        Interwoven sequence.

    Examples
    --------
    >>> glyph_021([[1,2,3],[10,20],[100]])
    [1, 10, 100, 2, 20, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(total length)
    - Space : O(total length)
    """
    L = [list(p) for p in paths]
    out: List[T] = []
    i = 0
    remaining = True
    while remaining:
        remaining = False
        for p in L:
            if i < len(p):
                out.append(p[i]); remaining = True
        i += 1
    return out
