# glyph_004.py — Dimensional Flow Harmonizer
# -----------------------------------------------------------------------------
# ID:            004
# Pack:          Pack 001 (000–100)
# Name:          Dimensional Flow Harmonizer
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_004(matrix: Sequence[Sequence[float]], *, iters: int = 20, eps: float = 1e-9) -> List[List[float]]:
    """
    Dimensional Flow Harmonizer — Sinkhorn row/column balancing toward doubly-stochastic.

    Overview
    --------
    Iteratively normalizes rows then columns so each sums to ~1. Ensures compatibility
    with probability-like downstream glyphs.

    Parameters
    ----------
    matrix : Sequence[Sequence[float]]
        Non-negative matrix (rows).
    iters : int, optional (default: 20)
        Max balancing passes.
    eps : float, optional (default: 1e-9)
        Stabilizer to avoid divide-by-zero.

    Returns
    -------
    List[List[float]]
        Balanced matrix.

    Examples
    --------
    >>> glyph_004([[1,2],[3,4]])  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    - ValueError : negative entries.

    Complexity
    ----------
    - Time  : O(iters · H · W)
    - Space : O(H · W)
    """
    A = [[float(v) for v in row] for row in matrix]
    if any(v < 0 for row in A for v in row):
        raise ValueError("matrix must be non-negative")
    if not A or not A[0]:
        return []
    for _ in range(max(1, iters)):
        for i, row in enumerate(A):
            s = sum(row) or 1.0
            A[i] = [v / (s if s > eps else 1.0) for v in row]
        W = len(A[0])
        for j in range(W):
            s = sum(A[i][j] for i in range(len(A))) or 1.0
            s = s if s > eps else 1.0
            for i in range(len(A)):
                A[i][j] /= s
    return A
