# glyph_660.py — COMPASS_SAFE_NAV
# -----------------------------------------------------------------------------
# ID:            660
# Pack:          Pack 007 (601–700)
# Name:          COMPASS_SAFE_NAV
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # heading correction only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict
import math

def glyph_660(heading_rad: float, goal_vec: Tuple[float, float],
              obstacles: Sequence[Tuple[float, float]], *,
              repel_gain: float = 0.5, attract_gain: float = 1.0) -> Dict[str, float]:
    """
    COMPASS_SAFE_NAV — correct heading using goal attraction + obstacle repulsion.

    Overview
    --------
    Computes a new heading angle from vector sum of an attractive goal field and
    inverse-square obstacle repulsion field (2D), purely geometric.

    Parameters
    ----------
    heading_rad : float
        Current heading angle (radians). Used only for context; not required.
    goal_vec : (float, float)
        Goal direction vector.
    obstacles : Sequence[(float, float)]
        Obstacle vectors in robot frame (x forward, y left).
    repel_gain : float, optional (default: ``0.5``)
    attract_gain : float, optional (default: ``1.0``)

    Returns
    -------
    {'heading_rad': float}

    Examples
    --------
    >>> h = glyph_660(0.0, (1.0,0.0), [(0.5,0.0)])['heading_rad']
    >>> isinstance(h, float)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    gx, gy = goal_vec
    ax, ay = attract_gain*gx, attract_gain*gy
    rx = ry = 0.0
    for ox, oy in obstacles:
        dx, dy = -ox, -oy
        r2 = max(1e-6, dx*dx + dy*dy)
        rx += repel_gain * dx / r2
        ry += repel_gain * dy / r2
    vx, vy = ax + rx, ay + ry
    return {"heading_rad": math.atan2(vy, vx)}
