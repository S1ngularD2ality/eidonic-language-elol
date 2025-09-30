# glyph_633.py — NIGHT_MODE_OPERATION
# -----------------------------------------------------------------------------
# ID:            633
# Pack:          Pack 007 (601–700)
# Name:          NIGHT_MODE_OPERATION
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_633(lux: float) -> Dict[str, float | str]:
    """
    NIGHT_MODE_OPERATION — dim visuals & soften motion in darkness.

    Overview
    --------
    Policy function mapping ambient light to brightness/speed scales.

    Parameters
    ----------
    lux : float

    Returns
    -------
    Dict[str, float | str]
        {'brightness_scale': float, 'speed_scale': float, 'mode': 'night'|'twilight'|'day'}

    Examples
    --------
    >>> glyph_633(20)['mode']
    'night'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if lux < 30.0:
        return {"brightness_scale": 0.3, "speed_scale": 0.6, "mode": "night"}
    if lux < 80.0:
        return {"brightness_scale": 0.6, "speed_scale": 0.8, "mode": "twilight"}
    return {"brightness_scale": 1.0, "speed_scale": 1.0, "mode": "day"}
