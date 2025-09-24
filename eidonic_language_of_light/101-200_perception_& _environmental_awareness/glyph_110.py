# glyph_110.py — Mirror Lens Separator
# -----------------------------------------------------------------------------
# ID:            110
# Pack:          Pack 002 (101–200)
# Name:          Mirror Lens Separator
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_110(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Mirror Lens Separator — split a sequence into fore/back halves.

    Overview
    --------
    Returns (first_half, reversed_second_half) for mirror comparisons.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (front, mirrored_back)

    Examples
    --------
    >>> glyph_110([1,2,3,4,5,6])
    ([1.0, 2.0, 3.0], [6.0, 5.0, 4.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    k = n // 2
    front = [float(v) for v in seq[:k]]
    back = [float(v) for v in seq[k:]][::-1]
    return front, back
