# glyph_261.py — Timeline Flow Breaker
# -----------------------------------------------------------------------------
# ID:            261
# Pack:          Pack 003 (201–300)
# Original Name: Timeline Flow Breaker
# Manifest Name: Timeline Flow Breaker
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_261(seq: Sequence[float], *, tol: float = 1e-6) -> List[int]:
    """
    Timeline Flow Breaker — return indices of discontinuities.

    Overview
    --------
    Flags positions i (i>=1) where |x[i] - x[i-1]| > tol. Useful to segment
    timelines into coherent chunks before higher-order processing.

    Parameters
    ----------
    seq : Sequence[float]
    tol : float, optional (default: 1e-6)

    Returns
    -------
    List[int]
        Indices where a break occurs.

    Examples
    --------
    >>> glyph_261([0, 0, 1, 1, 3], tol=0.5)
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
    if not seq: 
        return out
    prev = float(seq[0])
    for i in range(1, len(seq)):
        v = float(seq[i])
        if abs(v - prev) > tol:
            out.append(i)
        prev = v
    return out
