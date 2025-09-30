# glyph_662.py — HUMAN_ASSIST_TRACK
# -----------------------------------------------------------------------------
# ID:            662
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_ASSIST_TRACK
# Class:         navigation_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Tuple, Dict

def glyph_662(human_xy: Tuple[float, float],
              robot_xy: Tuple[float, float], *,
              stand_off_m: float = 0.9,
              max_step: float = 0.25) -> Dict[str, float]:
    """
    HUMAN_ASSIST_TRACK — one-step assist velocity toward a human with stand-off.

    Overview
    --------
    Produces a single bounded velocity vector that reduces the error to the
    human but holds at `stand_off_m`. No state; kinematic only.

    Parameters
    ----------
    human_xy : (x, y)
    robot_xy : (x, y)
    stand_off_m : float, optional (default: ``0.9``)
    max_step : float, optional (default: ``0.25``)
        Max speed in m/s-equivalent step.

    Returns
    -------
    {'vx': float, 'vy': float}

    Examples
    --------
    >>> v = glyph_662((1.0, 0.0), (0.0, 0.0))
    >>> v['vx'] > 0 and abs(v['vy']) < 1e-9
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    dx = human_xy[0] - robot_xy[0]
    dy = human_xy[1] - robot_xy[1]
    d2 = dx*dx + dy*dy
    if d2 <= 0.0:
        return {"vx": 0.0, "vy": 0.0}
    d = d2**0.5
    if d <= stand_off_m:
        return {"vx": 0.0, "vy": 0.0}
    scale = min(max_step, d - stand_off_m) / d
    return {"vx": dx * scale, "vy": dy * scale}
