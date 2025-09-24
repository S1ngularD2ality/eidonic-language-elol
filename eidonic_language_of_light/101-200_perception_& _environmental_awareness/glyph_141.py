# glyph_141.py — Mirror Field Inverter
# -----------------------------------------------------------------------------
# ID:            141
# Pack:          Pack 002 (101–200)
# Name:          Mirror Field Inverter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_141(field: Sequence[Sequence[float]]) -> List[List[float]]:
    """
    Mirror Field Inverter — invert a 2D field around its global mean.

    Overview
    --------
    Computes y = (2*mean - x) for each cell. Useful for phase/opposition analysis.

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    List[List[float]]
        Inverted field.

    Examples
    --------
    >>> glyph_141([[0,1],[2,3]])
    [[3.0, 2.0], [1.0, 0.0]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]: return []
    vals = [v for r in A for v in r]
    m = sum(vals)/len(vals)
    return [[2*m - v for v in r] for r in A]
