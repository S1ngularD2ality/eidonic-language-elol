# glyph_063.py — Anchoring Harmonics Grid
# -----------------------------------------------------------------------------
# ID:            063
# Pack:          Pack 001 (000–100)
# Name:          Anchoring Harmonics Grid
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List
import math

def glyph_063(n: int, *, base: float = 1.0, ratio: float = 2.0) -> List[List[float]]:
    """
    Anchoring Harmonics Grid — 2D harmonic ladder (outer product).

    Overview
    --------
    Generates a grid G where rows and columns follow a geometric progression:
    G[i][j] = base * ratio^(i) * ratio^(j). This provides a stable anchoring of
    harmonic magnitudes for downstream alignment.

    Parameters
    ----------
    n : int
        Grid size (n×n).
    base : float, optional (default: 1.0)
        Starting magnitude.
    ratio : float, optional (default: 2.0)
        Multiplicative step per index.

    Returns
    -------
    List[List[float]]
        Harmonics grid.

    Examples
    --------
    >>> glyph_063(2, base=1.0, ratio=2.0)
    [[1.0, 2.0],
     [2.0, 4.0]]

    Exceptions
    ----------
    - ValueError : if `n < 1`.

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n^2)
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    out = [[0.0]*n for _ in range(n)]
    row = [base * (ratio ** i) for i in range(n)]
    for i in range(n):
        ri = row[i]
        for j in range(n):
            out[i][j] = ri * row[j]
    return out
