# glyph_283.py — Quantum Field Balancer
# -----------------------------------------------------------------------------
# ID:            283
# Pack:          Pack 003 (201–300)
# Name:          Quantum Field Balancer
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_283(field: Sequence[Sequence[float]]) -> List[List[float]]:
    """
    Quantum Field Balancer — double-centering of a matrix.

    Overview
    --------
    A' = A - row_mean - col_mean + grand_mean (ANOVA-style centering).

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    List[List[float]]
        Balanced field.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H+W)
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]: return []
    H, W = len(A), len(A[0])
    rmean = [sum(r)/W for r in A]
    cmean = [sum(A[i][j] for i in range(H))/H for j in range(W)]
    gmean = sum(rmean)/H
    return [[A[y][x] - rmean[y] - cmean[x] + gmean for x in range(W)] for y in range(H)]
