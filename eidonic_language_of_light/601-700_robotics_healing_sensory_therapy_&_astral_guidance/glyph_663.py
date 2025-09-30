# glyph_663.py — TEMPERATURE_SAFE_CARRY
# -----------------------------------------------------------------------------
# ID:            663
# Pack:          Pack 007 (601–700)
# Name:          TEMPERATURE_SAFE_CARRY
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

def glyph_663(load_temp_c: float, ambient_c: float, limit_c: float, *,
              cool_bias: float = 0.6) -> Dict[str, float | str | bool]:
    """
    TEMPERATURE_SAFE_CARRY — etiquette gating based on load vs ambient and limit.

    Overview
    --------
    Returns carry mode with speed scale; encourages cooling if near limits.

    Parameters
    ----------
    load_temp_c : float
    ambient_c   : float
    limit_c     : float
    cool_bias   : float, optional (default: ``0.6``)  # scales speed when hot

    Returns
    -------
    {'ok': bool, 'mode': 'ok'|'caution'|'halt', 'speed_scale': float}

    Examples
    --------
    >>> glyph_663(60, 25, 55)['mode']
    'halt'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if load_temp_c <= limit_c - 3.0:
        return {"ok": True, "mode": "ok", "speed_scale": 1.0}
    if load_temp_c <= limit_c:
        return {"ok": True, "mode": "caution", "speed_scale": max(0.3, 1.0 - cool_bias*0.5)}
    return {"ok": False, "mode": "halt", "speed_scale": 0.0}
