# glyph_062.py — Dream Field Expander
# -----------------------------------------------------------------------------
# ID:            062
# Pack:          Pack 001 (000–100)
# Name:          Dream Field Expander
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_062(field: Sequence[Sequence[float]], *, scale: int = 2) -> List[List[float]]:
    """
    Dream Field Expander — nearest-neighbor upscaling for 2D fields.

    Overview
    --------
    Expands an H×W field to (H·scale)×(W·scale) by replicating each value into a
    scale×scale block. Useful for coarse-to-fine pipelines.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
        Input 2D field.
    scale : int, optional (default: 2)
        Integer magnification (>= 1).

    Returns
    -------
    List[List[float]]
        Upscaled field.

    Examples
    --------
    >>> glyph_062([[1,2],[3,4]], scale=2)
    [[1,1,2,2],
     [1,1,2,2],
     [3,3,4,4],
     [3,3,4,4]]

    Exceptions
    ----------
    - ValueError : if `scale < 1`.

    Complexity
    ----------
    - Time  : O(H·W·scale^2)
    - Space : O(H·W·scale^2)
    """
    if scale < 1:
        raise ValueError("scale must be >= 1")
    A = [list(map(float, row)) for row in field]
    if not A or not A[0]:
        return []
    H, W = len(A), len(A[0])
    out = [[0.0]*(W*scale) for _ in range(H*scale)]
    for y in range(H):
        for x in range(W):
            v = A[y][x]
            for dy in range(scale):
                row = out[y*scale + dy]
                row[x*scale:(x+1)*scale] = [v]*scale
    return out
