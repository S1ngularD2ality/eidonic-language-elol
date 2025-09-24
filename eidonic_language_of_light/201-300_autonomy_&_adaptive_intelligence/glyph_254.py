# glyph_254.py — Light Matrix Collapser
# -----------------------------------------------------------------------------
# ID:            254
# Pack:          Pack 003 (201–300)
# Name:          Light Matrix Collapser
# Class:         reduction
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_254(field: Sequence[Sequence[float]]) -> float:
    """
    Light Matrix Collapser — average of all cells.

    Overview
    --------
    Collapses a 2D grid to a single scalar via arithmetic mean.

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    float
        Mean value (0.0 if empty).

    Examples
    --------
    >>> glyph_254([[1,2],[3,4]])
    2.5

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(1)
    """
    if not field or not field[0]:
        return 0.0
    total = 0.0
    count = 0
    for row in field:
        for v in row:
            total += float(v); count += 1
    return total / count if count else 0.0
