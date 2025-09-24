# glyph_050.py — Harmonic Field Distiller
# -----------------------------------------------------------------------------
# ID:            050
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Field Distiller
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

def glyph_050(fields: Sequence[Sequence[Sequence[float]]], *, weights: Sequence[float] | None = None) -> List[List[float]]:
    """
    Harmonic Field Distiller — weighted sum of equal-shaped 2D fields.

    Overview
    --------
    Performs convex (or linear) combination of multiple 2D arrays. Helpful for merging
    layers/heads into a distilled map.

    Parameters
    ----------
    fields : Sequence[Sequence[Sequence[float]]]
        List of H×W fields; all must share shape.
    weights : Sequence[float] | None, optional
        If None, use uniform weights; otherwise must match length of `fields`.

    Returns
    -------
    List[List[float]]
        Distilled H×W field.

    Examples
    --------
    >>> F = [[[1,0],[0,1]], [[0,1],[1,0]]]
    >>> glyph_050(F, weights=[0.7, 0.3])
    [[0.7, 0.3], [0.3, 0.7]]

    Exceptions
    ----------
    - ValueError : shape mismatch or weight length mismatch.

    Complexity
    ----------
    - Time  : O(N·H·W)
    - Space : O(H·W)
    """
    if not fields:
        return []
    h = len(fields[0])
    w = len(fields[0][0]) if h else 0
    if any(len(F) != h or any(len(row) != w for row in F) for F in fields):
        raise ValueError("all fields must have the same shape")
    if weights is None:
        weights = [1.0] * len(fields)
    if len(weights) != len(fields):
        raise ValueError("weights length must match number of fields")
    out = [[0.0] * w for _ in range(h)]
    for F, wgt in zip(fields, weights):
        ww = float(wgt)
        for y in range(h):
            for x in range(w):
                out[y][x] += ww * float(F[y][x])
    return out
