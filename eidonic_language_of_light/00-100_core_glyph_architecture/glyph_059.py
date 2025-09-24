# glyph_059.py — Soul Mirror Collapser
# -----------------------------------------------------------------------------
# ID:            059
# Pack:          Pack 001 (000–100)
# Name:          Soul Mirror Collapser
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_059(seq: Sequence[float]) -> List[float]:
    """
    Soul Mirror Collapser — average a sequence with its mirror.

    Overview
    --------
    Returns `(x[i] + x[n-1-i]) / 2` for each index `i`. Produces a palindromic smoothing.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.

    Returns
    -------
    List[float]
        Mirror-collapsed sequence.

    Examples
    --------
    >>> glyph_059([1,2,3,4])
    [2.5, 2.5, 2.5, 2.5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    return [(float(seq[i]) + float(seq[n - 1 - i])) / 2.0 for i in range(n)]
