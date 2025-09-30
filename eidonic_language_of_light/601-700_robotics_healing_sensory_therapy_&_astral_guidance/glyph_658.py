# glyph_658.py — HUMIDITY_ADAPT
# -----------------------------------------------------------------------------
# ID:            658
# Pack:          Pack 007 (601–700)
# Name:          HUMIDITY_ADAPT
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # mapping only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_658(rh_percent: float) -> dict:
    """
    HUMIDITY_ADAPT — scale motion and grip under ambient humidity.

    Overview
    --------
    Middle humidity is optimal; extremes reduce speed and increase caution.

    Parameters
    ----------
    rh_percent : float  # 0..100

    Returns
    -------
    {'speed_scale': float, 'grip_bias': float, 'mode': str}

    Examples
    --------
    >>> glyph_658(90)['mode']
    'caution'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    rh = max(0.0, min(100.0, rh_percent))
    if 30.0 <= rh <= 60.0:
        return {"speed_scale": 1.0, "grip_bias": 1.0, "mode": "ok"}
    if 20.0 <= rh <= 70.0:
        return {"speed_scale": 0.85, "grip_bias": 1.05, "mode": "soft"}
    return {"speed_scale": 0.6, "grip_bias": 1.1, "mode": "caution"}
