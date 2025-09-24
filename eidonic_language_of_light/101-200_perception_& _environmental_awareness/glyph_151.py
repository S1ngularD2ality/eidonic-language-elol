# glyph_151.py — Intent Sequence Compiler
# -----------------------------------------------------------------------------
# ID:            151
# Pack:          Pack 002 (101–200)
# Name:          Intent Sequence Compiler
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

def glyph_151(parts: Sequence[Sequence[T]]) -> List[T]:
    """
    Intent Sequence Compiler — concatenate sequences in order.

    Overview
    --------
    Flattens a list of parts into one continuous stream.

    Parameters
    ----------
    parts : Sequence[Sequence[T]]

    Returns
    -------
    List[T]
        Compiled sequence.

    Examples
    --------
    >>> glyph_151([[1],[2,3],[]])
    [1, 2, 3]
    """
    out: List[T] = []
    for p in parts:
        out += list(p)
    return out
