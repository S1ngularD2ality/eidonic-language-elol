# glyph_638.py — OBJECT_SOFT_PLACE
# -----------------------------------------------------------------------------
# ID:            638
# Pack:          Pack 007 (601–700)
# Name:          OBJECT_SOFT_PLACE
# Class:         manipulation_gentle
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_638(height_m: float, mass_kg: float, *, settle_time_s: float = 1.0) -> Dict[str, float]:
    """
    OBJECT_SOFT_PLACE — compute decel profile to land with near-zero impulse.

    Overview
    --------
    Approximates needed entry speed and deceleration for a gentle set-down.

    Parameters
    ----------
    height_m : float
        Drop height before soft landing profile engages.
    mass_kg : float
        Object mass (kg).
    settle_time_s : float, optional (default: ``1.0``)
        Time window to dissipate residual velocity.

    Returns
    -------
    Dict[str, float]
        {'v_entry': float, 'a_decel': float}

    Examples
    --------
    >>> out = glyph_638(0.2, 1.0, settle_time_s=1.5)
    >>> out['v_entry'] > 0 and out['a_decel'] > 0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    g = 9.81
    v_entry = (2.0 * g * max(0.0, height_m)) ** 0.5
    a = min(1.5, max(0.1, v_entry / max(0.1, settle_time_s)))
    return {"v_entry": float(v_entry), "a_decel": float(a)}
