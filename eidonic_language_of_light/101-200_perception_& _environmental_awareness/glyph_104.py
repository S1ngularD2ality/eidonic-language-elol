# glyph_104.py — Dimensional Anchor Reflector
# -----------------------------------------------------------------------------
# ID:            104
# Pack:          Pack 002 (101–200)
# Name:          Dimensional Anchor Reflector
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_104(grid: Sequence[Sequence[float]], *, axis: str = "h") -> List[List[float]]:
    """
    Dimensional Anchor Reflector — reflect a 2D field horizontally or vertically.

    Overview
    --------
    axis='h' → reverse each row; axis='v' → reverse row order.

    Parameters
    ----------
    grid : Sequence[Sequence[float]]
    axis : {'h','v'}

    Returns
    -------
    List[List[float]]
        Reflected grid.

    Examples
    --------
    >>> glyph_104([[1,2],[3,4]], axis='h')
    [[2.0, 1.0], [4.0, 3.0]]

    Exceptions
    ----------
    - ValueError : if axis not in {'h','v'}.

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H·W)
    """
    A = [list(map(float, r)) for r in grid]
    if not A or not A[0]:
        return []
    if axis == "h":
        return [list(reversed(r)) for r in A]
    if axis == "v":
        return list(reversed(A))
    raise ValueError("axis must be 'h' or 'v'")
