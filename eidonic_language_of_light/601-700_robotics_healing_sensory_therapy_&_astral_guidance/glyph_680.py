# glyph_680.py — PEACEKEEPER_MODE
# -----------------------------------------------------------------------------
# ID:            680
# Pack:          Pack 007 (601–700)
# Name:          PEACEKEEPER_MODE
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy composition
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_680(crowd_level: float, tension_level: float) -> dict:
    """
    PEACEKEEPER_MODE — de-escalation etiquette for crowded or tense spaces.

    Overview
    --------
    Returns conservative speed and signaling scales that bias toward clarity,
    predictability, and non-provocation.

    Parameters
    ----------
    crowd_level   : float  # 0..1
    tension_level : float  # 0..1

    Returns
    -------
    {'mode': 'calm'|'guard'|'freeze', 'speed_scale': float, 'signal_scale': float}

    Examples
    --------
    >>> glyph_680(0.9, 0.9)['mode']
    'freeze'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    c = max(0.0, min(1.0, crowd_level))
    t = max(0.0, min(1.0, tension_level))
    risk = 0.6*c + 0.4*t
    if risk < 0.3:
        return {"mode": "calm", "speed_scale": 1.0, "signal_scale": 0.9}
    if risk < 0.7:
        return {"mode": "guard", "speed_scale": 0.7, "signal_scale": 0.7}
    return {"mode": "freeze", "speed_scale": 0.0, "signal_scale": 0.5}
