# glyph_686.py — HEARTBEAT_SYNC
# -----------------------------------------------------------------------------
# ID:            686
# Pack:          Pack 007 (601–700)
# Name:          HEARTBEAT_SYNC
# Class:         therapy.biofeedback
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_686(bpm: float, duration_s: int, subdivisions: int = 4) -> Dict:
    """
    HEARTBEAT_SYNC — produce a metrical cue track aligned to target BPM.

    Overview
    --------
    Builds beat timestamps at 1/subdivisions resolution for gentle pacing cues.

    Parameters
    ----------
    bpm : float
        Target beats per minute (30–180).
    duration_s : int
        Total length in seconds (>= 30).
    subdivisions : int
        Pulses per beat (1..8).

    Returns
    -------
    Dict
        Timeline of cue timestamps (in seconds).

    Examples
    --------
    >>> track = glyph_686(60.0, 120, 2)
    >>> round(track["timeline"][1], 2)
    0.5

    Exceptions
    ----------
    - ValueError : parameter outside safe ranges.

    Complexity
    ----------
    - Time  : O(N) where N=#pulses
    - Space : O(N)
    """
    if duration_s < 30: raise ValueError("duration_s >= 30")
    if not (30.0 <= bpm <= 180.0): raise ValueError("bpm 30–180")
    if not (1 <= subdivisions <= 8): raise ValueError("subdivisions 1..8")

    spb = 60.0 / bpm
    step = spb / subdivisions
    timeline: List[float] = []
    t = 0.0
    while t <= duration_s:
        timeline.append(round(t, 6))
        t += step
    return {"type":"heartbeat_sync","bpm":bpm,"subdivisions":subdivisions,"timeline":timeline}
