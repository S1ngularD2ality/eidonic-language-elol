# glyph_627.py — HUMAN_FOLLOW_MODE
# -----------------------------------------------------------------------------
# ID:            627
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_FOLLOW_MODE
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

def glyph_627(human_xy: Tuple[float, float], robot_xy: Tuple[float, float], *,
              stand_off_m: float = 1.0, gain: float = 0.8) -> Dict[str, float]:
    """
    HUMAN_FOLLOW_MODE — compute gentle velocity toward a human at stand-off.

    Overview
    --------
    Kinematic stand-off controller: zero velocity inside the stand-off radius.

    Parameters
    ----------
    human_xy : (float, float)
    robot_xy : (float, float)
    stand_off_m : float, optional (default: ``1.0``)
    gain : float, optional (default: ``0.8``)

    Returns
    -------
    Dict[str, float]
        {'vx': float, 'vy': float}

    Examples
    --------
    >>> v = glyph_627((2,0), (0,0), stand_off_m=1.0)
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
    dist2 = dx*dx + dy*dy
    if dist2 <= 0.0:
        return {"vx": 0.0, "vy": 0.0}
    dist = dist2 ** 0.5
    scale = max(0.0, (dist - stand_off_m) / dist)
    return {"vx": gain * dx * scale, "vy": gain * dy * scale}
