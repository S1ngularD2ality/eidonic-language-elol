# glyph_621.py — SAFE_LIFT_MECHANISM
# -----------------------------------------------------------------------------
# ID:            621
# Pack:          Pack 007 (601–700)
# Name:          SAFE_LIFT_MECHANISM
# Class:         manipulation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_621(object_mass_kg: float, grip_quality: float, *,
              accel_limit_mps2: float = 0.8, safety_margin: float = 1.25) -> Dict[str, float]:
    """
    SAFE_LIFT_MECHANISM — bounded lift acceleration and force envelope.

    Overview
    --------
    Computes a safe vertical acceleration and nominal force target that respects:
    gravity, grip quality, and configured limits. Pure algebraic envelope—no device I/O.

    Parameters
    ----------
    object_mass_kg : float
        Mass of the object in kilograms (>= 0).
    grip_quality : float
        Contact quality in [0,1]; 1.0 = ideal, 0.0 = unusable.
    accel_limit_mps2 : float, optional (default: ``0.8``)
        Maximum allowed lift acceleration.
    safety_margin : float, optional (default: ``1.25``)
        Force multiplier to counter slip and uncertainty.

    Returns
    -------
    Dict[str, float]
        {'amax': float, 'f_target_n': float}

    Examples
    --------
    >>> out = glyph_621(2.0, 0.8)
    >>> 0.0 <= out['amax'] <= 0.8 and out['f_target_n'] > 0
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
    q = max(0.0, min(1.0, grip_quality))
    amax = max(0.0, min(accel_limit_mps2, accel_limit_mps2 * q))
    f = max(0.0, safety_margin * max(0.0, object_mass_kg) * (g + amax))
    return {"amax": float(amax), "f_target_n": float(f)}
