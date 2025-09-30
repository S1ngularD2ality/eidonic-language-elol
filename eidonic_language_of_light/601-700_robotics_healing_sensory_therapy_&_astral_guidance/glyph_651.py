# glyph_651.py — MULTI_BOT_FORMATION
# -----------------------------------------------------------------------------
# ID:            651
# Pack:          Pack 007 (601–700)
# Name:          MULTI_BOT_FORMATION
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # geometry only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple, Dict

def glyph_651(n: int, spacing_m: float, *, kind: str = "line") -> Dict[str, List[Tuple[float, float]]]:
    """
    MULTI_BOT_FORMATION — compute 2D slots for simple formations.

    Overview
    --------
    Supported kinds: 'line' (x-axis), 'vee' (V-shape), 'circle'.

    Parameters
    ----------
    n : int
    spacing_m : float
    kind : str, optional (default: ``'line'``)

    Returns
    -------
    {'slots': List[(x,y)]}

    Examples
    --------
    >>> glyph_651(3, 1.0, kind='vee')['slots'][1][1] != 0.0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    import math
    n = max(0, n)
    s = float(spacing_m)
    if kind == "circle":
        r = s * max(1, n) / (2*math.pi)
        return {"slots": [(r*math.cos(2*math.pi*i/n), r*math.sin(2*math.pi*i/n)) for i in range(n)] if n else []}
    if kind == "vee":
        slots = []
        for i in range(n):
            side = -1 if i % 2 == 0 else 1
            k = (i+1)//2
            slots.append((k*s, side*k*s*0.6))
        return {"slots": slots}
    # default line
    return {"slots": [(i*s, 0.0) for i in range(n)]}
