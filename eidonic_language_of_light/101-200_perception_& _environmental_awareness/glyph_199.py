# glyph_199.py — Mirror Key Binder
# -----------------------------------------------------------------------------
# ID:            199
# Pack:          Pack 002 (101–200)
# Name:          Mirror Key Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def glyph_199(left: Sequence[T], right: Sequence[U]) -> List[Tuple[T, U]]:
    """
    Mirror Key Binder — pair left with reversed right.

    Overview
    --------
    Returns [(left[i], right[n-1-i])] for i up to min(len(left), len(right)).

    Parameters
    ----------
    left  : Sequence[T]
    right : Sequence[U]

    Returns
    -------
    List[Tuple[T,U]]
        Mirrored pairs.

    Examples
    --------
    >>> glyph_199([1,2,3], ['a','b','c'])
    [(1, 'c'), (2, 'b'), (3, 'a')]
    """
    m = min(len(left), len(right))
    return [(left[i], right[m-1-i]) for i in range(m)]
