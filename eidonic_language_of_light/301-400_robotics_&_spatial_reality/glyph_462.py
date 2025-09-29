# glyph_462.py — Work Parcel
# -----------------------------------------------------------------------------
# ID:            462
# Pack:          Pack 005 (401–500)
# Name:          Work Parcel
# Class:         packer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, List

def glyph_462(items: Sequence[Mapping[str, float]], *, max_units: float) -> List[int]:
    """
    Work Parcel — greedy bin pack into a single parcel by size (descending).

    Overview
    --------
    Picks largest items first while total 'units' <= max_units. Returns kept indices.

    Parameters
    ----------
    items     : Sequence[{'units': float}]
    max_units : float

    Returns
    -------
    List[int]

    Examples
    --------
    >>> glyph_462([{'units':2},{'units':1},{'units':3}], max_units=3)
    [2]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    idx = list(range(len(items)))
    idx.sort(key=lambda i: -float(items[i].get('units', 0.0)))
    out: List[int] = []
    used = 0.0
    for i in idx:
        u = float(items[i].get('units', 0.0))
        if used + u <= float(max_units):
            used += u
            out.append(i)
    out.sort()
    return out
