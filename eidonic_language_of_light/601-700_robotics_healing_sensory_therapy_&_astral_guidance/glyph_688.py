# glyph_688.py — THETA_WAVE_SUPPORT
# -----------------------------------------------------------------------------
# ID:            688
# Pack:          Pack 007 (601–700)
# Name:          THETA_WAVE_SUPPORT
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

def glyph_688(duration_s: int, center_hz: float = 220.0, beat_hz: float = 6.0) -> Dict:
    """
    THETA_WAVE_SUPPORT — gentle 4–8 Hz modulation plan centered on a carrier.

    Overview
    --------
    Builds a mono amplitude-modulated tone with slow ramps and safe levels.

    Parameters
    ----------
    duration_s : int
        Total length (>= 60).
    center_hz : float
        Carrier (100–1000 Hz).
    beat_hz : float
        Modulation frequency (4–8 Hz, theta range).

    Returns
    -------
    Dict
        AM plan specification.

    Examples
    --------
    >>> plan = glyph_688(600, 220.0, 6.0)
    >>> plan["am"]["freq_hz"]
    6.0

    Exceptions
    ----------
    - ValueError : parameters outside safe bounds.
    """
    if duration_s < 60: raise ValueError("duration_s >= 60")
    if not (100 <= center_hz <= 1000): raise ValueError("center_hz 100–1000")
    if not (4.0 <= beat_hz <= 8.0): raise ValueError("beat_hz theta 4–8 Hz")
    return {
        "type":"am_session",
        "duration_s": duration_s,
        "carrier_hz": center_hz,
        "am": {"freq_hz": beat_hz, "depth": 0.4},
        "envelope": {"attack":8.0,"release":12.0}
    }
