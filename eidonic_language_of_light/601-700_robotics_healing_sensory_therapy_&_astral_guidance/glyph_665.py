# glyph_665.py — ANIMAL_AVOIDANCE
# -----------------------------------------------------------------------------
# ID:            665
# Pack:          Pack 007 (601–700)
# Name:          ANIMAL_AVOIDANCE
# Class:         animal_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict
import math

def glyph_665(animals_xy: Sequence[Tuple[float, float]],
              waypoints: Sequence[Tuple[float, float]], *,
              min_dist_m: float = 1.5) -> Dict[str, bool | int]:
    """
    ANIMAL_AVOIDANCE — verify that a path respects animal stand-off distance.

    Overview
    --------
    Checks each waypoint against all animal positions and returns the first
    violation index if any.

    Parameters
    ----------
    animals_xy : Sequence[(x,y)]
    waypoints  : Sequence[(x,y)]
    min_dist_m : float, optional (default: ``1.5``)

    Returns
    -------
    {'ok': bool, 'first_violation_idx': int}

    Examples
    --------
    >>> glyph_665([(0,0)], [(1.0,0.0)], min_dist_m=2.0)['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N·M)
    - Space : O(1)
    """
    for i, (wx, wy) in enumerate(waypoints):
        for ax, ay in animals_xy:
            if math.hypot(wx-ax, wy-ay) < min_dist_m:
                return {"ok": False, "first_violation_idx": i}
    return {"ok": True, "first_violation_idx": -1}
