# glyph_682.py — BINAURAL_BEAT_GEN
# -----------------------------------------------------------------------------
# ID:            682
# Pack:          Pack 007 (601–700)
# Name:          BINAURAL_BEAT_GEN
# Class:         therapy.audio
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_682(carrier_hz: float, beat_hz: float, duration_s: int) -> Dict:
    """
    BINAURAL_BEAT_GEN — plan left/right carriers creating a target beat frequency.

    Overview
    --------
    Produces a stereo tone plan where left = carrier - beat/2 and right = carrier + beat/2.
    Bounds carriers to 100–1000 Hz for comfort and beat to 0.1–40 Hz.

    Parameters
    ----------
    carrier_hz : float
        Center frequency for both ears before split.
    beat_hz : float
        Difference frequency (target neural entrainment range).
    duration_s : int
        Session length in seconds (>= 60 recommended).

    Returns
    -------
    Dict
        Stereo plan with per-channel frequencies and envelopes.

    Examples
    --------
    >>> plan = glyph_682(220.0, 7.0, 600)
    >>> plan["left"]["freq_hz"], plan["right"]["freq_hz"]
    (216.5, 223.5)

    Exceptions
    ----------
    - ValueError : parameters outside safe bounds.

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if duration_s < 30:
        raise ValueError("duration_s must be >= 30")
    if not (100.0 <= carrier_hz <= 1000.0):
        raise ValueError("carrier_hz must be in 100–1000 Hz")
    if not (0.1 <= beat_hz <= 40.0):
        raise ValueError("beat_hz must be in 0.1–40 Hz")

    return {
        "type": "binaural_plan",
        "duration_s": duration_s,
        "left":  {"freq_hz": carrier_hz - beat_hz/2, "gain": 0.8},
        "right": {"freq_hz": carrier_hz + beat_hz/2, "gain": 0.8},
        "safety": {"max_gain": 1.0, "beat_range_hz": [0.1, 40.0]},
    }
