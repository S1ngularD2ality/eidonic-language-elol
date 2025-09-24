# glyph_121.py — Flame Field Extender
# -----------------------------------------------------------------------------
# ID:            121
# Pack:          Pack 002 (101–200)
# Name:          Flame Field Extender
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

def glyph_121(field: Sequence[Sequence[float]], *, pad: int = 1, mode: str = "edge") -> List[List[float]]:
    """
    Flame Field Extender — expand a 2D field with padding.

    Overview
    --------
    Pads an H×W grid by `pad` cells on all sides. `mode='edge'` repeats edge values;
    `mode='zero'` pads with zeros.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    pad   : int, optional (default: 1)
    mode  : {'edge','zero'}, optional (default: 'edge')

    Returns
    -------
    List[List[float]]
        Padded field with shape (H+2·pad) × (W+2·pad).

    Examples
    --------
    >>> glyph_121([[1,2],[3,4]], pad=1, mode='edge')
    [[1.0,1.0,2.0,2.0],
     [1.0,1.0,2.0,2.0],
     [3.0,3.0,4.0,4.0],
     [3.0,3.0,4.0,4.0]]

    Exceptions
    ----------
    - ValueError : if mode is not recognized or pad < 0.

    Complexity
    ----------
    - Time  : O((H+pad)·(W+pad))
    - Space : O((H+pad)·(W+pad))
    """
    if pad < 0:
        raise ValueError("pad must be >= 0")
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return []
    H, W = len(A), len(A[0])
    out = [[0.0]*(W + 2*pad) for _ in range(H + 2*pad)]
    for y in range(H + 2*pad):
        for x in range(W + 2*pad):
            sy = min(max(y - pad, 0), H-1)
            sx = min(max(x - pad, 0), W-1)
            out[y][x] = A[sy][sx] if mode == "edge" else (A[y-pad][x-pad] if 0<=y-pad<H and 0<=x-pad<W else 0.0)
    if mode not in ("edge","zero"):
        raise ValueError("mode must be 'edge' or 'zero'")
    return out
