# glyph_112.py — Light Sequence Fragmentor
# -----------------------------------------------------------------------------
# ID:            112
# Pack:          Pack 002 (101–200)
# Name:          Light Sequence Fragmentor
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_112(seq: Sequence[int], *, size: int, step: int | None = None) -> List[List[int]]:
    """
    Light Sequence Fragmentor — fixed-size windowing.

    Overview
    --------
    Slice windows of length `size` with stride `step` (default = size). Drops tail.

    Parameters
    ----------
    seq : Sequence[int]
    size : int
    step : int | None, optional

    Returns
    -------
    List[List[int]]
        Fragments.

    Examples
    --------
    >>> glyph_112([1,2,3,4,5], size=2)
    [[1, 2], [3, 4]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if size < 1:
        return []
    st = size if step is None else max(1, int(step))
    out: List[List[int]] = []
    i = 0
    while i + size <= len(seq):
        out.append([int(v) for v in seq[i:i+size]])
        i += st
    return out
