# glyph_500.py — Dawn Chorus
# -----------------------------------------------------------------------------
# ID:            500
# Pack:          Pack 005 (401–500)
# Name:          Dawn Chorus
# Class:         scheduler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_500(cron_minutes: Sequence[int], now_minute: int) -> int:
    """
    Dawn Chorus — return next scheduled minute ≥ now from sorted cron list.

    Overview
    --------
    If none ≥ now, returns first entry (wrap).

    Parameters
    ----------
    cron_minutes : Sequence[int]  (sorted ascending, 0..59)
    now_minute   : int            (0..59)

    Returns
    -------
    int : minute value in 0..59, or -1 if list empty.

    Examples
    --------
    >>> glyph_500([0,15,30], 20)
    30

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(log n)  (binary search)
    - Space : O(1)
    """
    arr = list(cron_minutes)
    if not arr:
        return -1
    # Binary search for lower_bound
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < now_minute:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo] if lo < len(arr) else arr[0]
