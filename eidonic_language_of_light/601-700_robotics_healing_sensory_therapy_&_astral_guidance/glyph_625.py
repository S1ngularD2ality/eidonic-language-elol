# glyph_625.py — PET_AWARE_MODE
# -----------------------------------------------------------------------------
# ID:            625
# Pack:          Pack 007 (601–700)
# Name:          PET_AWARE_MODE
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

def glyph_625(pets_xy: Sequence[Tuple[float, float]], here_xy: Tuple[float, float], *,
              calm_radius_m: float = 2.0) -> Dict[str, float | str]:
    """
    PET_AWARE_MODE — set etiquette near animals; avoid startle.

    Overview
    --------
    Computes min distance to detected pets and returns motion cue.

    Parameters
    ----------
    pets_xy : Sequence[(float, float)]
    here_xy : (float, float)
    calm_radius_m : float, optional (default: ``2.0``)

    Returns
    -------
    Dict[str, float | str]
        {'mode': 'ok'|'slow'|'hold', 'min_dist': float}

    Examples
    --------
    >>> glyph_625([(0,0)], (1.2,0), calm_radius_m=2.0)['mode']
    'slow'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if not pets_xy:
        return {"mode": "ok", "min_dist": float("inf")}
    dmin = min(math.hypot(here_xy[0]-x, here_xy[1]-y) for x, y in pets_xy)
    mode = "hold" if dmin < 0.5*calm_radius_m else ("slow" if dmin < calm_radius_m else "ok")
    return {"mode": mode, "min_dist": float(dmin)}
