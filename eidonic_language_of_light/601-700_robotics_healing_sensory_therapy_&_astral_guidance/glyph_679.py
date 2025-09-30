# glyph_679.py — RESPECT_QUIET_ZONE
# -----------------------------------------------------------------------------
# ID:            679
# Pack:          Pack 007 (601–700)
# Name:          RESPECT_QUIET_ZONE
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy mapping
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_679(zone_strictness: float, current_noise_db: float) -> dict:
    """
    RESPECT_QUIET_ZONE — suppress audio/visual output in quiet areas.

    Overview
    --------
    Strict zones and higher ambient noise both demand gentler behavior.

    Parameters
    ----------
    zone_strictness  : float  # 0..1
    current_noise_db : float

    Returns
    -------
    {'signal_scale': float, 'speed_scale': float, 'mode': str}

    Examples
    --------
    >>> glyph_679(1.0, 60)['signal_scale'] <= 0.4
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    z = max(0.0, min(1.0, zone_strictness))
    ns = 0.4 if z > 0.8 else (0.6 if z > 0.5 else 0.8)
    sp = 0.7 if current_noise_db > 70.0 else 1.0
    mode = "quiet_strict" if z > 0.8 else ("quiet_soft" if z > 0.5 else "normal")
    return {"signal_scale": ns, "speed_scale": sp, "mode": mode}
