# glyph_040.py — Anchor Field Modulator
# -----------------------------------------------------------------------------
# ID:            040
# Pack:          Pack 001 (000–100)
# Name:          Anchor Field Modulator
# Class:         combinator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_040(field: Sequence[Sequence[float]], mask: Sequence[Sequence[float]], *, alpha: float = 1.0) -> List[List[float]]:
    """
    Anchor Field Modulator — multiplicative blend of a field by a mask.

    Overview
    --------
    Returns field * (1 + alpha*mask) elementwise; shapes must match.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    mask  : Sequence[Sequence[float]]
    alpha : float, optional (default: 1.0)

    Returns
    -------
    List[List[float]]
        Modulated field.

    Examples
    --------
    >>> glyph_040([[1,1],[1,1]], [[0,1],[1,0]], alpha=0.5)
    [[1.0, 1.5], [1.5, 1.0]]

    Exceptions
    ----------
    - ValueError : shape mismatch.

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in field]
    M = [list(map(float, r)) for r in mask]
    if not A or not A[0]: return []
    if len(A)!=len(M) or any(len(A[i])!=len(M[i]) for i in range(len(A))):
        raise ValueError("field and mask shapes must match")
    H,W=len(A),len(A[0])
    a=float(alpha)
    return [[A[y][x]*(1.0 + a*M[y][x]) for x in range(W)] for y in range(H)]
