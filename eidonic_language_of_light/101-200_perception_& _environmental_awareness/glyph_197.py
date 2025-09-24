# glyph_197.py — Harmonic Field Redirector
# -----------------------------------------------------------------------------
# ID:            197
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Field Redirector
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_197(field: Sequence[Sequence[float]]) -> List[List[float]]:
    """
    Harmonic Field Redirector — swap quadrants diagonally.

    Overview
    --------
    Splits field into four quadrants (rounding down for odd shapes) and swaps
    top-left with bottom-right, top-right with bottom-left.

    Parameters
    ----------
    field : Sequence[Sequence[float]]

    Returns
    -------
    List[List[float]]
        Redirected field.
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return []
    H, W = len(A), len(A[0])
    hy, hx = H//2, W//2
    out = [row[:] for row in A]
    for y in range(hy):
        for x in range(hx):
            out[y][x], out[y+hy][x+hx] = A[y+hy][x+hx], A[y][x]
    for y in range(hy):
        for x in range(hx, W):
            out[y][x], out[y+hy][x-hx] = A[y+hy][x-hx], A[y][x]
    return out
