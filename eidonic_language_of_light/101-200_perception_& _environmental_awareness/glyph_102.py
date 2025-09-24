# glyph_102.py — Harmonic Time Anchor
# -----------------------------------------------------------------------------
# ID:            102
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Time Anchor
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List
import math

def glyph_102(n: int, *, period: int = 16) -> List[float]:
    """
    Harmonic Time Anchor — emit a normalized sinusoid timeline.

    Overview
    --------
    Produces length-n samples: s[t] = 0.5 + 0.5*sin(2π t/period), range [0,1].

    Parameters
    ----------
    n : int
    period : int, optional (default: 16)  # >= 2

    Returns
    -------
    List[float]
        Anchoring envelope.

    Examples
    --------
    >>> len(glyph_102(8, period=4))
    8

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if n <= 0:
        return []
    p = max(2, int(period))
    return [0.5 + 0.5*math.sin(2.0*math.pi*t/p) for t in range(n)]
