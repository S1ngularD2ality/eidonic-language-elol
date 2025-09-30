# glyph_690.py — LIGHT_PULSE_THERAPY
# -----------------------------------------------------------------------------
# ID:            690
# Pack:          Pack 007 (601–700)
# Name:          LIGHT_PULSE_THERAPY
# Class:         therapy.visual
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_690(frequency_hz: float, duty: float = 0.25, duration_s: int = 300) -> Dict:
    """
    LIGHT_PULSE_THERAPY — safe flicker plan for visual stimulation.

    Overview
    --------
    **Safety gates:** frequency ∈ [0.1, 30] Hz, duty ∈ (0, 0.5]. Emits a plan only—
    renderer must ask consent and screen for photosensitivity.

    Parameters
    ----------
    frequency_hz : float
        Pulse frequency.
    duty : float, optional
        Duty cycle (on-fraction), <= 0.5.
    duration_s : int, optional
        Total duration (>= 60).

    Returns
    -------
    Dict
        Pulse plan with safety flags.

    Examples
    --------
    >>> plan = glyph_690(3.0, 0.25, 180)
    >>> plan["safety"]["consent_required"]
    True
    """
    if duration_s < 60: raise ValueError("duration_s >= 60")
    if not (0.1 <= frequency_hz <= 30.0): raise ValueError("frequency 0.1–30 Hz")
    if not (0.0 < duty <= 0.5): raise ValueError("duty in (0,0.5]")

    return {
        "type":"light_pulse",
        "frequency_hz": frequency_hz,
        "duty": duty,
        "duration_s": duration_s,
        "safety": {
            "consent_required": True,
            "photosensitivity_screen": True,
            "max_hz": 30.0,
            "max_duty": 0.5
        }
    }
