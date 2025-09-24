# glyph_269.py — Liminal Pathway Stitcher
# -----------------------------------------------------------------------------
# ID:            269
# Pack:          Pack 003 (201–300)
# Original Name: Liminal Pathway Stitcher
# Manifest Name: Liminal Pathway Stitcher
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

def glyph_269(a: Sequence[T], b: Sequence[T], *, pivot: int) -> List[T]:
    """
    Liminal Pathway Stitcher — splice A[0:pivot) with B[pivot:].

    Overview
    --------
    Creates a stitched path across two streams at a shared pivot.

    Parameters
    ----------
    a, b : Sequence[T]
    pivot : int

    Returns
    -------
    List[T]
        Spliced sequence.

    Examples
    --------
    >>> glyph_269([1,2,3],[9,8,7], pivot=2)
    [1, 2, 7]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(a)+len(b))
    - Space : O(len(a)+len(b))
    """
    p = max(0, int(pivot))
    return list(a[:p]) + list(b[p:])
