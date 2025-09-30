# glyph_671.py — NON_INTRUSIVE_MONITOR
# -----------------------------------------------------------------------------
# ID:            671
# Pack:          Pack 007 (601–700)
# Name:          NON_INTRUSIVE_MONITOR
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_671(privacy_level: float, activity_level: float) -> dict:
    """
    NON_INTRUSIVE_MONITOR — attenuate presence in private/active spaces.

    Overview
    --------
    Higher privacy → lower signaling; higher activity → slower movement.

    Parameters
    ----------
    privacy_level : float  # 0..1
    activity_level: float  # 0..1

    Returns
    -------
    {'signal_scale': float, 'speed_scale': float, 'mode': str}

    Examples
    --------
    >>> glyph_671(0.9, 0.8)['mode']
    'stealth_soft'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    p = max(0.0, min(1.0, privacy_level))
    a = max(0.0, min(1.0, activity_level))
    signal = max(0.2, 1.0 - 0.8*p)
    speed = max(0.3, 1.0 - 0.7*a)
    mode = "stealth_soft" if p > 0.7 or a > 0.7 else "observe"
    return {"signal_scale": signal, "speed_scale": speed, "mode": mode}
