# glyph_118.py — Mirror Channel Divider
# -----------------------------------------------------------------------------
# ID:            118
# Pack:          Pack 002 (101–200)
# Name:          Mirror Channel Divider
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

def glyph_118(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Mirror Channel Divider — split into even/odd index channels.

    Overview
    --------
    Returns (seq[0::2], seq[1::2]).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (even, odd)

    Examples
    --------
    >>> glyph_118([0,1,2,3,4])
    ([0.0, 2.0, 4.0], [1.0, 3.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    even = [float(v) for v in seq[0::2]]
    odd  = [float(v) for v in seq[1::2]]
    return even, odd
