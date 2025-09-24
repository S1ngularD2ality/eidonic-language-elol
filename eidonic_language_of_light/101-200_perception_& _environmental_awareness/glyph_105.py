# glyph_105.py — Recursive Mirror Distributor
# -----------------------------------------------------------------------------
# ID:            105
# Pack:          Pack 002 (101–200)
# Name:          Recursive Mirror Distributor
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_105(depth: int) -> List[int]:
    """
    Recursive Mirror Distributor — mirrored cascade indices.

    Overview
    --------
    S(0) = []; S(d) = S(d-1) + [d] + reverse(S(d-1)).

    Parameters
    ----------
    depth : int  # >= 0

    Returns
    -------
    List[int]
        Mirrored cascade.

    Examples
    --------
    >>> glyph_105(3)
    [1, 2, 1, 3, 1, 2, 1]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(2^depth)
    - Space : O(2^depth)
    """
    if depth <= 0:
        return []
    prev = glyph_105(depth-1)
    return prev + [depth] + list(reversed(prev))
