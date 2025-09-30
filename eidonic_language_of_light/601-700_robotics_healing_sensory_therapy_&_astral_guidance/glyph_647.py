# glyph_647.py — VOICE_CALM_MODE
# -----------------------------------------------------------------------------
# ID:            647
# Pack:          Pack 007 (601–700)
# Name:          VOICE_CALM_MODE
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy mapping
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_647(spl_db: float, arousal_score: float) -> Dict[str, float | str]:
    """
    VOICE_CALM_MODE — adapt behavior to loudness and human arousal.

    Overview
    --------
    Larger SPL / arousal → quieter visuals and slower motion.

    Parameters
    ----------
    spl_db : float
        Sound pressure level (dB).
    arousal_score : float
        0..1, where 1 is highly aroused/anxious.

    Returns
    -------
    {'mode': 'ok'|'soothe', 'brightness_scale': float, 'speed_scale': float}

    Examples
    --------
    >>> glyph_647(85, 0.7)['mode']
    'soothe'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    a = max(0.0, min(1.0, arousal_score))
    if spl_db >= 80.0 or a > 0.5:
        return {"mode": "soothe", "brightness_scale": 0.6, "speed_scale": 0.7}
    return {"mode": "ok", "brightness_scale": 1.0, "speed_scale": 1.0}
