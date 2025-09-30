# glyph_673.py — HUMAN_COMFORT_ZONE
# -----------------------------------------------------------------------------
# ID:            673
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_COMFORT_ZONE
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # rule map
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_673(personal_space_m: float, noise_db: float) -> dict:
    """
    HUMAN_COMFORT_ZONE — etiquette scales from space and noise.

    Overview
    --------
    Larger distance and lower noise → normal mode; else soften.

    Parameters
    ----------
    personal_space_m : float
    noise_db         : float

    Returns
    -------
    {'mode': 'ok'|'soft', 'speed_scale': float, 'signal_scale': float}

    Examples
    --------
    >>> glyph_673(0.5, 85)['mode']
    'soft'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    soft = (personal_space_m < 1.0) or (noise_db > 75.0)
    return {"mode": "soft" if soft else "ok",
            "speed_scale": 0.7 if soft else 1.0,
            "signal_scale": 0.7 if soft else 1.0}
