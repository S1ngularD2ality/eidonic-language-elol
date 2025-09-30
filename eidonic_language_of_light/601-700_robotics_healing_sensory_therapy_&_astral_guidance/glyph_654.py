# glyph_654.py — ACCESSIBILITY_MODE
# -----------------------------------------------------------------------------
# ID:            654
# Pack:          Pack 007 (601–700)
# Name:          ACCESSIBILITY_MODE
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_654(context: Mapping[str, Any]) -> Dict[str, Any]:
    """
    ACCESSIBILITY_MODE — adapt cues for mobility/vision/hearing needs.

    Overview
    --------
    Returns gentle parameter scales for navigation and signaling.

    Parameters
    ----------
    context : may include:
        {'wheelchair': bool, 'low_vision': bool, 'hard_of_hearing': bool}

    Returns
    -------
    {'speed_scale': float, 'audio_scale': float, 'visual_scale': float, 'mode': str}

    Examples
    --------
    >>> glyph_654({'low_vision': True})['visual_scale'] >= 1.2
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    wc = bool(context.get("wheelchair", False))
    lv = bool(context.get("low_vision", False))
    hh = bool(context.get("hard_of_hearing", False))
    speed = 0.8 if wc else 1.0
    audio = 1.2 if hh else 1.0
    visual = 1.2 if lv else 1.0
    mode = "access" if (wc or lv or hh) else "standard"
    return {"speed_scale": speed, "audio_scale": audio, "visual_scale": visual, "mode": mode}
