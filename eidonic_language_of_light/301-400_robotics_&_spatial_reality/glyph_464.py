# glyph_464.py — Rate Governor
# -----------------------------------------------------------------------------
# ID:            464
# Pack:          Pack 005 (401–500)
# Name:          Rate Governor
# Class:         regulator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_464(timestamps: Sequence[float], *, window_s: float, max_events: int) -> List[bool]:
    """
    Rate Governor — sliding-window allow/deny mask.

    Overview
    --------
    For each event time `t`, allows if events in [t-window_s, t] < max_events.

    Parameters
    ----------
    timestamps : Sequence[float]  (monotonic seconds)
    window_s   : float
    max_events : int

    Returns
    -------
    List[bool] : True=allow, False=deny

    Examples
    --------
    >>> glyph_464([1,2,3,4], window_s=2, max_events=2)
    [True, True, False, False]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    out: List[bool] = []
    left = 0
    for i, t in enumerate(timestamps):
        while left <= i and t - timestamps[left] > float(window_s):
            left += 1
        out.append((i - left) < int(max_events))
    return out
