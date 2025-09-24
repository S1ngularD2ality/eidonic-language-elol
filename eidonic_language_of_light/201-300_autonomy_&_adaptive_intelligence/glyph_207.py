# glyph_207.py — Fractal Thread Harmonizer
# -----------------------------------------------------------------------------
# ID:            207
# Pack:          Pack 003 (201–300)
# Name:          Fractal Thread Harmonizer
# Class:         combinator
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from math import ceil
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_207(parts: Sequence[Sequence[T]], *, weight: Sequence[float] | None = None) -> List[T]:
    """
    Fractal Thread Harmonizer — weighted round-robin interleave of streams.

    Overview
    --------
    Cycles across streams, taking `ceil(w_i)` items from stream i per round (w_i from
    `weight`, default=1). Preserves intra-stream order.

    Parameters
    ----------
    parts : Sequence[Sequence[T]]
        Streams to interleave.
    weight : Sequence[float] | None, optional
        Relative pulls per round; rounded up to at least 1.

    Returns
    -------
    List[T]
        Harmonized sequence.

    Examples
    --------
    >>> glyph_207([[1,1,1],[2,2]], weight=[1,2])
    [1, 2, 2, 1, 2, 2, 1]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(total items)
    - Space : O(total items)
    """
    P = [list(p) for p in parts]
    if not P:
        return []
    if not weight:
        weight = [1.0] * len(P)
    w = [max(1, int(ceil(x))) for x in weight]
    pos = [0] * len(P)
    out: List[T] = []
    remaining = sum(len(p) for p in P)
    while remaining > 0:
        for i, p in enumerate(P):
            take = w[i]
            while take and pos[i] < len(p):
                out.append(p[pos[i]])
                pos[i] += 1
                take -= 1
                remaining -= 1
    return out
