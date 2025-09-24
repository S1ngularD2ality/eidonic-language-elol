# glyph_129.py — Dimensional Anchor Separator
# -----------------------------------------------------------------------------
# ID:            129
# Pack:          Pack 002 (101–200)
# Name:          Dimensional Anchor Separator
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_129(grid: Sequence[Sequence[float]]) -> Tuple[List[float], List[float]]:
    """
    Dimensional Anchor Separator — extract row and column anchors.

    Overview
    --------
    Returns (row_sums, col_sums) across a 2D field.

    Parameters
    ----------
    grid : Sequence[Sequence[float]]

    Returns
    -------
    (List[float], List[float])
        (row_sums, col_sums)
    """
    A = [list(map(float, r)) for r in grid]
    if not A or not A[0]:
        return [], []
    H, W = len(A), len(A[0])
    rows = [sum(A[y][x] for x in range(W)) for y in range(H)]
    cols = [sum(A[y][x] for y in range(H)) for x in range(W)]
    return rows, cols
