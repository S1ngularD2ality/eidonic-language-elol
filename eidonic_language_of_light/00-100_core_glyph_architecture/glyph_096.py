# glyph_096.py — Intention Grid Merger
# -----------------------------------------------------------------------------
# ID:            096
# Pack:          Pack 001 (000–100)
# Name:          Intention Grid Merger
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

def glyph_096(fields: Sequence[Sequence[Sequence[float]]]) -> List[List[float]]:
    """
    Intention Grid Merger — elementwise mean across equal-shaped 2D fields.

    Overview
    --------
    Averages a list of H×W grids; returns empty list if no fields.

    Parameters
    ----------
    fields : Sequence[Sequence[Sequence[float]]]

    Returns
    -------
    List[List[float]]
        Merged grid.

    Exceptions
    ----------
    - ValueError : shape mismatch.

    Complexity
    ----------
    - Time  : O(N·H·W)
    - Space : O(H·W)
    """
    if not fields:
        return []
    H = len(fields[0]); W = len(fields[0][0]) if H else 0
    if any(len(F) != H or any(len(r) != W for r in F) for F in fields):
        raise ValueError("all fields must have equal shape")
    out = [[0.0]*W for _ in range(H)]
    for F in fields:
        for y in range(H):
            for x in range(W):
                out[y][x] += float(F[y][x])
    N = float(len(fields)) or 1.0
    for y in range(H):
        for x in range(W):
            out[y][x] /= N
    return out
