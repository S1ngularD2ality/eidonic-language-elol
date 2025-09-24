# glyph_010.py — Soul Matrix Divider
# -----------------------------------------------------------------------------
# ID:            010
# Pack:          Pack 001 (000–100)
# Name:          Soul Matrix Divider
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_010(grid: Sequence[Sequence[float]]) -> Tuple[List[float], List[float]]:
    """
    Soul Matrix Divider — extract primary diagonal and anti-diagonal.

    Overview
    --------
    Splits an n×n matrix into two “soul lines”: main diagonal and anti-diagonal.

    Parameters
    ----------
    grid : Sequence[Sequence[float]]
        Square matrix.

    Returns
    -------
    (List[float], List[float])
        (diag, anti)

    Examples
    --------
    >>> glyph_010([[1,2],[3,4]])
    ([1.0, 4.0], [2.0, 3.0])

    Exceptions
    ----------
    - ValueError : if matrix is empty or not square.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not grid or not grid[0]:
        raise ValueError("grid must be non-empty")
    n = len(grid)
    if any(len(row) != n for row in grid):
        raise ValueError("grid must be square")
    diag = [float(grid[i][i]) for i in range(n)]
    anti = [float(grid[i][n-1-i]) for i in range(n)]
    return diag, anti
