# glyph_282.py — Mirror Thread Separator
# -----------------------------------------------------------------------------
# ID:            282
# Pack:          Pack 003 (201–300)
# Name:          Mirror Thread Separator
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_282(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Mirror Thread Separator — decompose into even/odd mirror components.

    Overview
    --------
    even[i]=(x[i]+x[n-1-i])/2; odd[i]=(x[i]-x[n-1-i])/2.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (even_component, odd_component)

    Examples
    --------
    >>> glyph_282([1,2,3,4])
    ([2.5, 2.5, 2.5, 2.5], [-1.5, -0.5, 0.5, 1.5])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    even = [0.0]*n; odd=[0.0]*n
    for i in range(n):
        j = n-1-i
        even[i] = 0.5*(x[i] + x[j])
        odd[i]  = 0.5*(x[i] - x[j])
    return even, odd
