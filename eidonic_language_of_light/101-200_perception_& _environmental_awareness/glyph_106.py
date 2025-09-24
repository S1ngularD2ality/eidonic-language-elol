# glyph_106.py — Dream Cascade Indexer
# -----------------------------------------------------------------------------
# ID:            106
# Pack:          Pack 002 (101–200)
# Name:          Dream Cascade Indexer
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_106(seq: Sequence[int]) -> List[int]:
    """
    Dream Cascade Indexer — cumulative index (1..n).

    Overview
    --------
    Returns [1,2,3,...,n] regardless of element values.

    Parameters
    ----------
    seq : Sequence[int]

    Returns
    -------
    List[int]
        1..n index.

    Examples
    --------
    >>> glyph_106([9,9,9])
    [1, 2, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [i+1 for i in range(len(seq))]
