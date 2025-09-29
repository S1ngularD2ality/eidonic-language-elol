# glyph_480.py — Liveness Pulse
# -----------------------------------------------------------------------------
# ID:            480
# Pack:          Pack 005 (401–500)
# Name:          Liveness Pulse
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

def glyph_480(heartbeats: Sequence[float], now_s: float, *, max_silence: float) -> bool:
    """
    Liveness Pulse — True if last heartbeat is within max_silence.

    Overview
    --------
    Checks `now_s - last(heartbeats) <= max_silence`. Empty heartbeats → False.

    Parameters
    ----------
    heartbeats  : Sequence[float]
    now_s       : float
    max_silence : float

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_480([10.0, 20.0], now_s=21.0, max_silence=2.0)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if not heartbeats:
        return False
    return (float(now_s) - float(heartbeats[-1])) <= float(max_silence)
