# glyph_055.py — Intuition Field Binder
# -----------------------------------------------------------------------------
# ID:            055
# Pack:          Pack 001 (000–100)
# Name:          Intuition Field Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_055(a: Sequence[Sequence[float]], b: Sequence[Sequence[float]], *, alpha: float = 0.5) -> List[List[float]]:
    """
    Intuition Field Binder — convex blend of two equal-shaped 2D fields.

    Overview
    --------
    Produces `(1-alpha)*A + alpha*B`, preserving shape and treating inputs as float grids.

    Parameters
    ----------
    a, b : Sequence[Sequence[float]]
        H×W fields (identical shape).
    alpha : float, optional (default: 0.5)
        Blend factor in [0,1].

    Returns
    -------
    List[List[float]]
        Blended field.

    Examples
    --------
    >>> glyph_055([[0,0],[0,0]], [[1,1],[1,1]], alpha=0.25)
    [[0.25,0.25],[0.25,0.25]]

    Exceptions
    ----------
    - ValueError : shape mismatch.

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in a]
    B = [list(map(float, r)) for r in b]
    if not A or not A[0]:
        return []
    if len(A) != len(B) or any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("fields must have identical shape")
    t = min(1.0, max(0.0, float(alpha)))
    h, w = len(A), len(A[0])
    return [[(1 - t) * A[y][x] + t * B[y][x] for x in range(w)] for y in range(h)]
