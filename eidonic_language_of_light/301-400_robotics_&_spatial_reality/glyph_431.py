# glyph_431.py — Cross-Channel Sync
# -----------------------------------------------------------------------------
# ID:            431
# Pack:          Pack 005 (401–500)
# Name:          Cross-Channel Sync
# Class:         synchronizer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_431(clock_a: Sequence[float], clock_b: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Cross-Channel Sync — median-centering of two time sources.

    Overview
    --------
    Subtract each series’ median to align relative phase without scaling.

    Parameters
    ----------
    clock_a : Sequence[float]
    clock_b : Sequence[float]

    Returns
    -------
    (List[float], List[float]) : (aligned_a, aligned_b)

    Examples
    --------
    >>> glyph_431([0,1,2], [5,6,7])
    ([-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    def norm(ts: Sequence[float]) -> List[float]:
        if not ts: return []
        s = sorted(float(t) for t in ts)
        m = s[len(s)//2] if len(s)%2 else 0.5*(s[len(s)//2-1]+s[len(s)//2])
        return [float(t)-m for t in ts]
    return norm(clock_a), norm(clock_b)
