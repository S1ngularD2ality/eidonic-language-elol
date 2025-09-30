# glyph_648.py — ENVIRONMENT_LIGHT_ADAPT
# -----------------------------------------------------------------------------
# ID:            648
# Pack:          Pack 007 (601–700)
# Name:          ENVIRONMENT_LIGHT_ADAPT
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # mapping only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_648(lux: float) -> Dict[str, float | str]:
    """
    ENVIRONMENT_LIGHT_ADAPT — brightness and contrast policy from ambient light.

    Overview
    --------
    Gentle curve ensures no sudden jumps in visuals across lux ranges.

    Parameters
    ----------
    lux : float

    Returns
    -------
    {'mode': str, 'brightness': float, 'contrast': float}

    Examples
    --------
    >>> glyph_648(10)['mode']
    'dark'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if lux < 30.0:
        return {"mode": "dark", "brightness": 0.35, "contrast": 0.9}
    if lux < 120.0:
        return {"mode": "dim", "brightness": 0.6, "contrast": 0.95}
    if lux < 400.0:
        return {"mode": "normal", "brightness": 0.85, "contrast": 1.0}
    return {"mode": "bright", "brightness": 1.0, "contrast": 1.0}
