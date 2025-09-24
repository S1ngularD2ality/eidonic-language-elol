# glyph_082.py — Dimensional Reflection Loop
# -----------------------------------------------------------------------------
# ID:            082
# Pack:          Pack 001 (000–100)
# Name:          Dimensional Reflection Loop
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

def glyph_082(seq: Sequence[float], *, loops: int = 2) -> List[float]:
    """
    Dimensional Reflection Loop — alternate forward and mirrored passes.

    Overview
    --------
    Concatenate the sequence with its reverse repeatedly:
    `[x, rev(x), x, rev(x), ...]` for `loops` cycles.

    Parameters
    ----------
    seq : Sequence[float]
    loops : int, optional (default: 2)
        Number of forward+reverse cycles (>= 1).

    Returns
    -------
    List[float]
        Looped sequence.

    Examples
    --------
    >>> glyph_082([1,2], loops=2)
    [1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0]

    Exceptions
    ----------
    - ValueError : if loops < 1.

    Complexity
    ----------
    - Time  : O(n·loops)
    - Space : O(n·loops)
    """
    L = [float(v) for v in seq]
    if loops < 1:
        raise ValueError("loops must be >= 1")
    out: List[float] = []
    R = list(reversed(L))
    for _ in range(loops):
        out += L + R
    return out
