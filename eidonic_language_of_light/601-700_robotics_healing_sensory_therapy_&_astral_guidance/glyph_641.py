# glyph_641.py — SAFE_LIFT_BALANCE
# -----------------------------------------------------------------------------
# ID:            641
# Pack:          Pack 007 (601–700)
# Name:          SAFE_LIFT_BALANCE
# Class:         manipulation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # algebraic envelope; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Tuple

def glyph_641(object_mass_kg: float, cg_offset_m: float, arm_span_m: float, *,
              max_force_n: float = 200.0) -> Dict[str, float]:
    """
    SAFE_LIFT_BALANCE — distribute lift forces across two end-effectors.

    Overview
    --------
    Models a rigid object lifted by two grippers separated by `arm_span_m`
    with center-of-gravity offset `cg_offset_m` from the midpoint (right=+).
    Solves for static forces (F_left, F_right) with gravity and clamps to
    `max_force_n` per arm. Pure algebra; no actuator I/O.

    Parameters
    ----------
    object_mass_kg : float
        Mass (kg), >= 0.
    cg_offset_m : float
        Lateral CoG offset from span midpoint (meters). Right is positive.
    arm_span_m : float
        Distance between grippers (meters), > 0.
    max_force_n : float, optional (default: ``200.0``)
        Per-arm force cap.

    Returns
    -------
    Dict[str, float]
        {'F_left_n': float, 'F_right_n': float, 'overcap': float}

    Examples
    --------
    >>> out = glyph_641(5.0, 0.05, 0.4)
    >>> abs((out['F_left_n'] + out['F_right_n']) - 5.0*9.81) < 1e-6
    True

    Exceptions
    ----------
    - ValueError : if arm_span_m <= 0 or object_mass_kg < 0.

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if arm_span_m <= 0:
        raise ValueError("arm_span_m must be > 0")
    if object_mass_kg < 0:
        raise ValueError("object_mass_kg must be >= 0")

    g = 9.81
    W = object_mass_kg * g
    # Static equilibrium: F_L + F_R = W; moment about midpoint: F_R* (span/2) - F_L*(span/2) = W*cg_offset
    half = arm_span_m / 2.0
    Fr = (W/2.0) + (W * cg_offset_m) / (2.0 * half)
    Fl = W - Fr

    # Clamp to caps; report overflow magnitude
    over = max(0.0, max(Fl - max_force_n, Fr - max_force_n))
    Fl_c = min(max_force_n, max(0.0, Fl))
    Fr_c = min(max_force_n, max(0.0, Fr))
    return {"F_left_n": float(Fl_c), "F_right_n": float(Fr_c), "overcap": float(over)}
