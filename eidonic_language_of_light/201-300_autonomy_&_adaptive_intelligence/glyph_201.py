# glyph_201.py — Recursive Anchor Injector
# -----------------------------------------------------------------------------
# ID:            201
# Pack:          Pack 003 (201–300)
# Name:          Recursive Anchor Injector
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, TypeVar, List

T = TypeVar("T")

def glyph_201(stream: Sequence[T], anchors: Sequence[T], *, period: int = 4) -> List[T]:
    """
    Recursive Anchor Injector — interleave `anchors` into `stream` at a fixed cadence.

    Overview
    --------
    Emits the original stream while inserting items from `anchors` every `period`
    elements, cycling through anchors recursively.

    Parameters
    ----------
    stream : Sequence[T]
    anchors : Sequence[T]
    period : int, optional (default: 4)

    Returns
    -------
    List[T]
        Stream with periodic anchor insertions.

    Examples
    --------
    >>> glyph_201([1,2,3,4,5], ['A','B'], period=2)
    [1, 2, 'A', 3, 4, 'B', 5]

    Exceptions
    ----------
    - ValueError : if period < 1.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if period < 1:
        raise ValueError("period must be >= 1")
    out: List[T] = []
    ai = 0
    aN = max(1, len(anchors))
    for i, v in enumerate(stream, start=1):
        out.append(v)
        if i % period == 0 and aN:
            out.append(anchors[ai % aN])
            ai += 1
    return out
