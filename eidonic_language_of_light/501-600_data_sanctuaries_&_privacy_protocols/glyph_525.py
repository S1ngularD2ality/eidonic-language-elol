# glyph_525.py — Access Rate Limit
# -----------------------------------------------------------------------------
# ID:            525
# Pack:          Pack 006 (501–600)
# Name:          Access Rate Limit
# Class:         auth_access_control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure counters
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_525(counter: Mapping[int, int], now: int, *, window: int, limit: int) -> bool:
    """
    Access Rate Limit — sliding-window token check (integer seconds).

    Overview
    --------
    `counter` maps second → hits. Allows if sum(now-window+1…now) ≤ limit.

    Parameters
    ----------
    counter : Mapping[int,int]
    now     : int
    window  : int
    limit   : int

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_525({10:3, 11:2, 12:1}, 12, window=3, limit=6)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(1)
    """
    s = 0
    start = now - max(0, window - 1)
    for t, v in counter.items():
        if start <= int(t) <= int(now):
            s += int(v)
    return s <= int(limit)
