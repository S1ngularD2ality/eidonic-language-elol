# glyph_085.py — Dream Cycle Unifier
# -----------------------------------------------------------------------------
# ID:            085
# Pack:          Pack 001 (000–100)
# Name:          Dream Cycle Unifier
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_085(cycles: Sequence[Sequence[int]]) -> int:
    """
    Dream Cycle Unifier — least common multiple of cycle lengths.

    Overview
    --------
    Returns LCM of the lengths of all input cycles. Empty → 0.

    Parameters
    ----------
    cycles : Sequence[Sequence[int]]

    Returns
    -------
    int
        Unified cycle length.

    Examples
    --------
    >>> glyph_085([[1,2,3],[0,1],[9,9,9,9]])
    12

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N log M)
    - Space : O(1)
    """
    import math
    def lcm(a, b):
        return 0 if a*b == 0 else abs(a*b) // math.gcd(a, b)
    L = 1
    for c in cycles:
        L = lcm(L, len(c))
    return 0 if L == 1 and not cycles else L
