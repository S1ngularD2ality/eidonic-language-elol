# glyph_472.py — Opinion Pool
# -----------------------------------------------------------------------------
# ID:            472
# Pack:          Pack 005 (401–500)
# Name:          Opinion Pool
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

def glyph_472(scores: Sequence[float]) -> float:
    """
    Opinion Pool — normalized mean in [0,1].

    Overview
    --------
    Clamps inputs to [0,1] then averages.

    Parameters
    ----------
    scores : Sequence[float]

    Returns
    -------
    float

    Examples
    --------
    >>> glyph_472([0.2, 0.6, 1.2])
    0.6

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if not scores:
        return 0.0
    vals = [min(1.0, max(0.0, float(s))) for s in scores]
    return sum(vals) / len(vals)
