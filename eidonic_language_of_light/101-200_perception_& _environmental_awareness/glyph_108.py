# glyph_108.py — Thought Flame Loopbinder
# -----------------------------------------------------------------------------
# ID:            108
# Pack:          Pack 002 (101–200)
# Name:          Thought Flame Loopbinder
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_108(seq: Sequence[int], *, loops: int = 1) -> List[int]:
    """
    Thought Flame Loopbinder — loop a sequence and close the path.

    Overview
    --------
    Concatenate `loops` copies and, if non-empty, append the first element to close.

    Parameters
    ----------
    seq : Sequence[int]
    loops : int, optional (default: 1)

    Returns
    -------
    List[int]
        Closed loop sequence.

    Examples
    --------
    >>> glyph_108([1,2,3], loops=2)
    [1, 2, 3, 1, 2, 3, 1]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·loops)
    - Space : O(n·loops)
    """
    if loops < 1:
        return []
    out: List[int] = []
    for _ in range(loops):
        out += [int(v) for v in seq]
    if out:
        out.append(out[0])
    return out
