# glyph_250.py — Flame Core Condenser
# -----------------------------------------------------------------------------
# ID:            250
# Pack:          Pack 003 (201–300)
# Name:          Flame Core Condenser
# Class:         reduction
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_250(seq: Sequence[float]) -> float:
    """
    Flame Core Condenser — robust central energy (trimmed mean).

    Overview
    --------
    Drops min and max if available, averages the rest.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    float
        Condensed scalar.

    Examples
    --------
    >>> glyph_250([1, 100, 2, 3])
    2.0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(1) to O(n) (implementation-dependent)
    """
    x = [float(v) for v in seq]
    if not x:
        return 0.0
    if len(x) <= 2:
        return sum(x) / len(x)
    x.sort()
    core = x[1:-1]
    return sum(core) / len(core)
