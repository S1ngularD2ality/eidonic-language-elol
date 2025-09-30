# glyph_669.py — LOW_VIBRATION_MODE
# -----------------------------------------------------------------------------
# ID:            669
# Pack:          Pack 007 (601–700)
# Name:          LOW_VIBRATION_MODE
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy mapping
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_669(surface_sensitivity: float, payload_fragility: float) -> dict:
    """
    LOW_VIBRATION_MODE — scale speed based on surface and payload fragility.

    Overview
    --------
    Higher sensitivity/fragility → lower speed and softer motion.

    Parameters
    ----------
    surface_sensitivity : float  # 0..1
    payload_fragility   : float  # 0..1

    Returns
    -------
    {'speed_scale': float, 'mode': 'ok'|'soft'|'ultra_soft'}

    Examples
    --------
    >>> glyph_669(0.9, 0.8)['mode']
    'ultra_soft'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    s = max(0.0, min(1.0, surface_sensitivity))
    f = max(0.0, min(1.0, payload_fragility))
    score = 0.5*s + 0.5*f
    if score < 0.3:
        return {"speed_scale": 1.0, "mode": "ok"}
    if score < 0.7:
        return {"speed_scale": 0.75, "mode": "soft"}
    return {"speed_scale": 0.5, "mode": "ultra_soft"}
