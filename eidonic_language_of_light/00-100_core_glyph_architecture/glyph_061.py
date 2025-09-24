# glyph_061.py — Timeline Braid Weaver
# -----------------------------------------------------------------------------
# ID:            061
# Pack:          Pack 001 (000–100)
# Name:          Timeline Braid Weaver
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Sequence, List, TypeVar, Literal

T = TypeVar("T")
Mode = Literal["truncate", "pad"]

def glyph_061(streams: Sequence[Sequence[T]], *, mode: Mode = "truncate", pad: T | None = None) -> List[T]:
    """
    Timeline Braid Weaver — round-robin interleave multiple timelines.

    Overview
    --------
    Braids N streams by taking one item from each in order. If stream lengths differ:
    - ``truncate`` stops at the shortest,
    - ``pad`` continues to the longest using ``pad`` fill values.

    Parameters
    ----------
    streams : Sequence[Sequence[T]]
        The timelines to braid (N ≥ 1).
    mode : {"truncate","pad"}, optional (default: "truncate")
        Handling for uneven lengths.
    pad : T | None, optional
        Fill token when ``mode="pad"``.

    Returns
    -------
    List[T]
        Interleaved output.

    Examples
    --------
    >>> glyph_061([[1,2,3],[10,20]], mode="truncate")
    [1, 10, 2, 20]
    >>> glyph_061([[1,2,3],[10,20]], mode="pad", pad=0)
    [1, 10, 2, 20, 3, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(sum lengths)
    - Space : O(sum lengths)
    """
    if not streams:
        return []
    lens = [len(s) for s in streams]
    out: List[T] = []
    if mode == "truncate":
        L = min(lens)
        for i in range(L):
            for s in streams:
                out.append(s[i])
        return out
    elif mode == "pad":
        L = max(lens)
        for i in range(L):
            for s in streams:
                out.append(s[i] if i < len(s) else pad)  # type: ignore[arg-type]
        return out
    else:
        raise ValueError("mode must be 'truncate' or 'pad'")
