# glyph_288.py — Thought Sequence Rewriter
# -----------------------------------------------------------------------------
# ID:            288
# Pack:          Pack 003 (201–300)
# Name:          Thought Sequence Rewriter
# Class:         control
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, TypeVar, List
T = TypeVar("T")

def glyph_288(seq: List[T], *, rule: Callable[[T], T]) -> List[T]:
    """
    Thought Sequence Rewriter — apply a deterministic per-item rule.

    Overview
    --------
    Returns [rule(x) for x in seq] without side-effects.

    Parameters
    ----------
    seq : List[T]
    rule : Callable[[T], T]

    Returns
    -------
    List[T]
        Rewritten sequence.

    Examples
    --------
    >>> glyph_288([1,2,3], rule=lambda v: v*v)
    [1, 4, 9]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [rule(x) for x in seq]
