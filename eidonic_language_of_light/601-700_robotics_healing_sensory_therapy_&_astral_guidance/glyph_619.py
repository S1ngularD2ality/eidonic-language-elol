# glyph_619.py — SAFE_LIFTING_PATH
# -----------------------------------------------------------------------------
# ID:            619
# Pack:          Pack 007 (601–700)
# Name:          SAFE_LIFTING_PATH
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # purely kinematic
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_619(waypoints: Sequence[Tuple[float,float,float]], *,
              jerk_limit: float = 1.0) -> List[Tuple[float,float,float]]:
    """
    SAFE_LIFTING_PATH — jerk-bounded smoothing for lifting trajectories.

    Returns
    -------
    List[(x,y,z)] : smoothed path
    """
    if not waypoints: return []
    out = [waypoints[0]]
    for i in range(1, len(waypoints)-1):
        x0,y0,z0 = waypoints[i-1]
        x1,y1,z1 = waypoints[i]
        x2,y2,z2 = waypoints[i+1]
        # simple midpoint smoothing bounded by jerk_limit factor
        mx,my,mz = (x0+x2)/2, (y0+y2)/2, (z0+z2)/2
        alpha = max(0.0, min(1.0, 1.0/(1.0+jerk_limit)))
        sx,sy,sz = (1-alpha)*x1 + alpha*mx, (1-alpha)*y1 + alpha*my, (1-alpha)*z1 + alpha*mz
        out.append((sx,sy,sz))
    out.append(waypoints[-1])
    return out
