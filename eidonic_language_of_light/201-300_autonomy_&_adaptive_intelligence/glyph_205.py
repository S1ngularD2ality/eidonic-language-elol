# glyph_205.py — Flame Cycle Organizer
# -----------------------------------------------------------------------------
# ID:            205
# Pack:          Pack 003 (201–300)
# Name:          Flame Cycle Organizer
# Class:         generator
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_205(n: int, *, start: int = 0) -> List[int]:
    """
    Flame Cycle Organizer — emit cyclic indices 0..n-1 starting at `start`.

    Overview
    --------
    Produces a canonical cycle of length `n` that can be used as a base clock or
    carrier for other glyphs.

    Parameters
    ----------
    n : int
        Cycle length (n >= 0).
    start : int, optional (default: 0)
        Starting index within the cycle.

    Returns
    -------
    List[int]
        Indices [start, start+1, ...] modulo n (empty if n <= 0).

    Examples
    --------
    >>> glyph_205(5, start=2)
    [2, 3, 4, 0, 1]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if n <= 0:
        return []
    s = ((start % n) + n) % n
    return [(s + i) % n for i in range(n)]
