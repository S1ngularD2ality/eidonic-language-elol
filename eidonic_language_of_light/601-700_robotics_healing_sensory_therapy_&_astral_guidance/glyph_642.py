# glyph_642.py — TEMP_SENSITIVE_MODE
# -----------------------------------------------------------------------------
# ID:            642
# Pack:          Pack 007 (601–700)
# Name:          TEMP_SENSITIVE_MODE
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # rule gate
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_642(ambient_c: float, material_limit_c: float, *,
              hysteresis_c: float = 2.0) -> Dict[str, float | str | bool]:
    """
    TEMP_SENSITIVE_MODE — etiquette based on ambient vs. material heat limit.

    Overview
    --------
    Returns conservative mode labels and speed scaling when temperature risk rises.

    Parameters
    ----------
    ambient_c : float
    material_limit_c : float
    hysteresis_c : float, optional (default: ``2.0``)
        Buffer before switching to stricter mode.

    Returns
    -------
    {'mode': 'ok'|'caution'|'halt', 'speed_scale': float, 'violation': bool}

    Examples
    --------
    >>> glyph_642(45, 50)['mode']
    'ok'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if ambient_c <= material_limit_c - hysteresis_c:
        return {"mode": "ok", "speed_scale": 1.0, "violation": False}
    if ambient_c <= material_limit_c:
        return {"mode": "caution", "speed_scale": 0.7, "violation": False}
    return {"mode": "halt", "speed_scale": 0.0, "violation": True}
