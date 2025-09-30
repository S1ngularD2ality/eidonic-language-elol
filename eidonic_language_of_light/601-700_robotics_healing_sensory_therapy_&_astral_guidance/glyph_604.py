# glyph_604.py — COLLISION_PREVENTION
# -----------------------------------------------------------------------------
# ID:            604
# Pack:          Pack 007 (601–700)
# Name:          COLLISION_PREVENTION
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # kinematic check; Euclidean
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any
import math

def glyph_604(path: Sequence[Tuple[float,float]],
              obstacles: Sequence[Tuple[float,float]],
              *, radius_m: float = 0.4) -> Dict[str, Any]:
    """
    COLLISION_PREVENTION — validate a path against circular safety buffers.

    Returns
    -------
    {'ok': bool, 'violations': List[int]}

    Examples
    --------
    >>> glyph_604([(0,0),(1,0)], [(0.5,0)], radius_m=0.4)['ok']
    False
    """
    viol = []
    for i, p in enumerate(path):
        for o in obstacles:
            if math.hypot(p[0]-o[0], p[1]-o[1]) < radius_m:
                viol.append(i); break
    return {"ok": len(viol) == 0, "violations": viol}
