# glyph_614.py — CROWD_NAVIGATION
# -----------------------------------------------------------------------------
# ID:            614
# Pack:          Pack 007 (601–700)
# Name:          CROWD_NAVIGATION
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # field-based planner
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_614(goal: Tuple[float,float], people: Sequence[Tuple[float,float]],
              *, repel_gain: float = 1.0, attract_gain: float = 1.0) -> List[float]:
    """
    CROWD_NAVIGATION — compute 2D velocity from artificial potentials.

    Returns
    -------
    [vx, vy] : List[float]
    """
    import math
    ax = attract_gain * goal[0]
    ay = attract_gain * goal[1]
    rx = ry = 0.0
    for px, py in people:
        dx, dy = -px, -py
        r2 = max(1e-6, dx*dx + dy*dy)
        rx += repel_gain * dx / r2
        ry += repel_gain * dy / r2
    return [ax + rx, ay + ry]
