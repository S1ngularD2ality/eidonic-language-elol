# glyph_243.py — Polarity Anchor Mapper
# -----------------------------------------------------------------------------
# ID:            243
# Pack:          Pack 003 (201–300)
# Name:          Polarity Anchor Mapper
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_243(arr: Sequence[float]) -> int:
    """
    Polarity Anchor Mapper — index of value closest to zero.

    Overview
    --------
    Finds the anchor of least polarity magnitude.

    Parameters
    ----------
    arr : Sequence[float]

    Returns
    -------
    int
        Index of |x| minimum, or -1 if empty.

    Examples
    --------
    >>> glyph_243([3,-0.2,5])
    1

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if not arr:
        return -1
    best_i, best_v = 0, abs(float(arr[0]))
    for i, v in enumerate(arr):
        a = abs(float(v))
        if a < best_v:
            best_i, best_v = i, a
    return best_i
