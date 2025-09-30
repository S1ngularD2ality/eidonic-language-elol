# glyph_655.py — SAFE_SPEED_CURVE
# -----------------------------------------------------------------------------
# ID:            655
# Pack:          Pack 007 (601–700)
# Name:          SAFE_SPEED_CURVE
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # profile math only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List, Tuple

def glyph_655(distance_m: float, v_max: float, *,
              a_max: float = 0.6, j_max: float = 1.0) -> Dict[str, List[Tuple[str, float]]]:
    """
    SAFE_SPEED_CURVE — jerk- and accel-bounded 1D speed plan (segments).

    Overview
    --------
    Returns a simple 3-phase profile [('accel', ta), ('cruise', tc), ('decel', td)].

    Parameters
    ----------
    distance_m : float
    v_max : float
    a_max : float, optional (default: ``0.6``)
    j_max : float, optional (default: ``1.0``)  # reserved for future use

    Returns
    -------
    {'segments': List[(phase, seconds)]}

    Examples
    --------
    >>> glyph_655(2.0, 1.0)['segments'][0][0]
    'accel'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    d = max(0.0, distance_m)
    vm = max(0.0, v_max)
    a = max(1e-6, a_max)
    # triangular vs trapezoidal test
    t_to_vmax = vm / a
    d_accel = 0.5 * a * t_to_vmax**2
    if 2*d_accel >= d:  # triangular
        t = (2*d / a)**0.5
        return {"segments": [("accel", t/2), ("decel", t/2)]}
    # trapezoidal
    d_cruise = d - 2*d_accel
    t_cruise = d_cruise / vm if vm > 0 else 0.0
    return {"segments": [("accel", t_to_vmax), ("cruise", t_cruise), ("decel", t_to_vmax)]}
