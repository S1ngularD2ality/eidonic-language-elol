# glyph_499.py — Resilience Choir
# -----------------------------------------------------------------------------
# ID:            499
# Pack:          Pack 005 (401–500)
# Name:          Resilience Choir
# Class:         aggregator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_499(uptimes: Sequence[float]) -> float:
    """
    Resilience Choir — harmonic mean of uptimes in [0,1].

    Overview
    --------
    Robustly aggregates multiple availability signals; zeros are clamped to eps.

    Parameters
    ----------
    uptimes : Sequence[float]

    Returns
    -------
    float

    Examples
    --------
    >>> round(glyph_499([0.9, 0.8, 1.0]), 3)
    0.891

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    eps = 1e-12
    if not uptimes:
        return 0.0
    s = 0.0
    for u in uptimes:
        x = max(float(u), eps)
        s += 1.0 / x
    return len(uptimes) / s
