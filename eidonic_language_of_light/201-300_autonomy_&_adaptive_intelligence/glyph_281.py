# glyph_281.py — Timeline Anchor Breaker
# -----------------------------------------------------------------------------
# ID:            281
# Pack:          Pack 003 (201–300)
# Name:          Timeline Anchor Breaker
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_281(seq: Sequence[float], *, tol: float = 1e-6) -> List[int]:
    """
    Timeline Anchor Breaker — indices of discontinuities.

    Overview
    --------
    Emit i (i>=1) where |x[i] - x[i-1]| > tol.

    Parameters
    ----------
    seq : Sequence[float]
    tol : float, optional (default: 1e-6)

    Returns
    -------
    List[int]
        Discontinuity indices.

    Examples
    --------
    >>> glyph_281([0,0,1,1,3], tol=0.5)
    [2, 4]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    out: List[int] = []
    if not seq: return out
    prev = float(seq[0])
    for i in range(1, len(seq)):
        v = float(seq[i])
        if abs(v - prev) > tol:
            out.append(i)
        prev = v
    return out
