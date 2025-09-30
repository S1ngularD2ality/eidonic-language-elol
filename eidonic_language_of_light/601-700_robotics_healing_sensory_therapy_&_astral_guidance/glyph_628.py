# glyph_628.py — THERMAL_RESPECT
# -----------------------------------------------------------------------------
# ID:            628
# Pack:          Pack 007 (601–700)
# Name:          THERMAL_RESPECT
# Class:         material_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_628(surface_temp_c: float, material_limit_c: float) -> Dict[str, str | bool]:
    """
    THERMAL_RESPECT — ensure handling respects temperature limits.

    Overview
    --------
    Rule gate returning an etiquette cue based on temperature.

    Parameters
    ----------
    surface_temp_c : float
    material_limit_c : float

    Returns
    -------
    Dict[str, str | bool]
        {'ok': bool, 'cue': 'ok'|'cool'|'reject'}

    Examples
    --------
    >>> glyph_628(80, 70)['cue']
    'reject'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if surface_temp_c <= material_limit_c:
        return {"ok": True, "cue": "ok"}
    if surface_temp_c <= material_limit_c + 5.0:
        return {"ok": False, "cue": "cool"}
    return {"ok": False, "cue": "reject"}
