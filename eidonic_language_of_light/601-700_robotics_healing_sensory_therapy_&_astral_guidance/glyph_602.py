# glyph_602.py — HUMAN_PRESENCE_AWARENESS
# -----------------------------------------------------------------------------
# ID:            602
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_PRESENCE_AWARENESS
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure geometry; no sensors
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any
import math

def glyph_602(poses: Sequence[Tuple[float, float]], robot: Tuple[float, float],
              *, min_personal_space_m: float = 1.5) -> Dict[str, Any]:
    """
    HUMAN_PRESENCE_AWARENESS — compute proximity & etiquette recommendations.

    Overview
    --------
    Given world-space coordinates of nearby humans (2D) and robot position,
    returns min distance, count within personal space, and etiquette cues
    (slow/stop/ok).

    Parameters
    ----------
    poses : Sequence[(x,y)]
    robot : (x,y)
    min_personal_space_m : float, optional (default: ``1.5``)

    Returns
    -------
    {'min_dist': float, 'count_violate': int, 'cue': 'ok'|'slow'|'stop'}

    Examples
    --------
    >>> glyph_602([(0,0),(2,0)], (1,0), min_personal_space_m=1.0)['cue']
    'slow'
    """
    def d(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])
    ds = [d(p, robot) for p in poses] if poses else [math.inf]
    min_d = min(ds)
    violate = sum(1 for x in ds if x < min_personal_space_m)
    cue = "ok" if violate == 0 else ("slow" if min_d >= 0.75*min_personal_space_m else "stop")
    return {"min_dist": float(min_d), "count_violate": int(violate), "cue": cue}
