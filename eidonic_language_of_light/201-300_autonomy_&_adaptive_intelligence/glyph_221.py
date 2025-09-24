# glyph_221.py — Recursive Mirror Fragmenter
# -----------------------------------------------------------------------------
# ID:            221
# Pack:          Pack 003 (201–300)
# Name:          Recursive Mirror Fragmenter
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_221(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Recursive Mirror Fragmenter — split a signal into mirror-even/odd fragments.

    Overview
    --------
    For x of length n, at each i define j=n-1-i. Output:
      even[i] = (x[i] + x[j]) / 2
      odd[i]  = (x[i] - x[j]) / 2
    This fragments the signal into components stable under reflection.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (even_component, odd_component)

    Examples
    --------
    >>> glyph_221([1,2,3,4])
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
    even = [0.0]*n
    odd  = [0.0]*n
    for i in range(n):
        j = n-1-i
        even[i] = 0.5*(x[i] + x[j])
        odd[i]  = 0.5*(x[i] - x[j])
    return even, odd
