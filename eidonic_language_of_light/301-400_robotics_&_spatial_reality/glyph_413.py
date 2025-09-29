# glyph_413.py — Heartbeat Monitor
# -----------------------------------------------------------------------------
# ID:            413
# Pack:          Pack 005 (401–500)
# Name:          Heartbeat Monitor
# Class:         detector
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_413(intervals_ms: Sequence[float], *, max_gap_ms: float) -> bool:
    """
    Heartbeat Monitor — True if any inter-beat interval exceeds max_gap_ms.

    Overview
    --------
    Simple watchdog for missed heartbeats using a scalar threshold.

    Parameters
    ----------
    intervals_ms : Sequence[float]
    max_gap_ms   : float

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_413([100, 120, 400], max_gap_ms=300)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    for dt in intervals_ms:
        if float(dt) > float(max_gap_ms):
            return True
    return False
