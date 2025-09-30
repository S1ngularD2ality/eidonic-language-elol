# glyph_623.py — ASSISTIVE_PUSH
# -----------------------------------------------------------------------------
# ID:            623
# Pack:          Pack 007 (601–700)
# Name:          ASSISTIVE_PUSH
# Class:         manipulation_gentle
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple, Dict
import math

def glyph_623(direction_xy: Tuple[float, float], desired_newton: float, *,
              max_newton: float = 10.0) -> Dict[str, float]:
    """
    ASSISTIVE_PUSH — compute a gentle push force bounded by ethics.

    Overview
    --------
    Projects a desired magnitude onto a unit vector with a safety cap.

    Parameters
    ----------
    direction_xy : (float, float)
        Desired push direction; zero vector defaults to +x.
    desired_newton : float
        Requested magnitude.
    max_newton : float, optional (default: ``10.0``)
        Maximum allowed magnitude.

    Returns
    -------
    Dict[str, float]
        {'fx': float, 'fy': float, 'f_mag': float}

    Examples
    --------
    >>> out = glyph_623((1, 0), 12.0)
    >>> out['f_mag'] == 10.0 and abs(out['fx'] - 10.0) < 1e-9
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    dx, dy = direction_xy
    mag = math.hypot(dx, dy)
    ux, uy = (1.0, 0.0) if mag == 0.0 else (dx/mag, dy/mag)
    fm = max(0.0, min(max_newton, desired_newton))
    return {"fx": ux*fm, "fy": uy*fm, "f_mag": fm}
