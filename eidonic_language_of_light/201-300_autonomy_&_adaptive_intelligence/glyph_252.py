# glyph_252.py — Dimensional Pattern Extractor
# -----------------------------------------------------------------------------
# ID:            252
# Pack:          Pack 003 (201–300)
# Name:          Dimensional Pattern Extractor
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_252(field: Sequence[Sequence[float]]) -> Tuple[List[float], List[float]]:
    """
    Dimensional Pattern Extractor — row/column projection sums.

    Overview
    --------
    Returns (row_sums, col_sums) for a rectangular field.

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    (List[float], List[float])
        (row_sums, col_sums)

    Examples
    --------
    >>> glyph_252([[1,2],[3,4]])
    ([3.0, 7.0], [4.0, 6.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H+W)
    """
    if not field or not field[0]:
        return [], []
    rows = [sum(float(v) for v in r) for r in field]
    cols = [sum(float(field[i][j]) for i in range(len(field))) for j in range(len(field[0]))]
    return rows, cols
