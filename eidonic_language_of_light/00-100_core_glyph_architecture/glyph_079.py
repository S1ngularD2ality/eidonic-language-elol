# glyph_079.py — Harmonic Bridge Dissolver
# -----------------------------------------------------------------------------
# ID:            079
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Bridge Dissolver
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_079(seq: Sequence[float], *, base_period: int, harmonics: int = 3, strength: float = 1.0) -> List[float]:
    """
    Harmonic Bridge Dissolver — notch out a harmonic series via comb subtraction.

    Overview
    --------
    Builds a comb estimate of periodic content at multiples of `base_period` and
    subtracts `strength * comb` from the signal.

    Parameters
    ----------
    seq : Sequence[float]
        Input samples.
    base_period : int
        Fundamental delay (>= 1).
    harmonics : int, optional (default: 3)
        Number of harmonic taps.
    strength : float, optional (default: 1.0)
        Subtraction coefficient.

    Returns
    -------
    List[float]
        De-harmonized sequence.

    Examples
    --------
    >>> glyph_079([1,0,1,0,1,0], base_period=2, harmonics=1, strength=1.0)
    [1,0,0,0,0,0]

    Exceptions
    ----------
    - ValueError : invalid parameters.

    Complexity
    ----------
    - Time  : O(n·harmonics)
    - Space : O(n)
    """
    if base_period < 1 or harmonics < 1:
        raise ValueError("base_period and harmonics must be >= 1")
    n = len(seq)
    if n == 0:
        return []
    weights = [1.0/(h+1) for h in range(harmonics)]
    wsum = sum(weights)
    comb = [0.0]*n
    for i in range(n):
        for h in range(harmonics):
            d = (h+1)*base_period
            if i - d >= 0:
                comb[i] += float(seq[i-d]) * weights[h]
        comb[i] /= wsum
    k = float(strength)
    return [float(seq[i]) - k*comb[i] for i in range(n)]
