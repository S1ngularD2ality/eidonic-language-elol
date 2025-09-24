# glyph_170.py — Recursive Field Projector
# -----------------------------------------------------------------------------
# ID:            170
# Pack:          Pack 002 (101–200)
# Name:          Recursive Field Projector
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_170(field: Sequence[Sequence[float]], *, depth: int = 2) -> List[float]:
    """
    Recursive Field Projector — alternating row/column reductions.

    Overview
    --------
    Repeatedly project a 2D field to 1D by averaging rows, then columns of the
    reshaped 2D (row vector). `depth` controls the number of reductions.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    depth : int, optional (default: 2)

    Returns
    -------
    List[float]
        1D projection.

    Examples
    --------
    >>> glyph_170([[1,2],[3,4]], depth=1)
    [1.5, 3.5]
    """
    A = [list(map(float, r)) for r in field]
    if not A or not A[0]:
        return []
    vec = [sum(r)/len(r) for r in A]  # row means
    for _ in range(max(0, depth-1)):
        # treat vec as single-row matrix, take column means (== vec)
        m = sum(vec)/len(vec)
        vec = [m]
    return vec
