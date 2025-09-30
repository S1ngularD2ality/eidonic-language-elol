# glyph_674.py — AUTONOMOUS_MEDIC_DELIVERY
# -----------------------------------------------------------------------------
# ID:            674
# Pack:          Pack 007 (601–700)
# Name:          AUTONOMOUS_MEDIC_DELIVERY
# Class:         logistics_planning
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # greedy + priority
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Tuple
import math

def glyph_674(reqs: Sequence[Mapping[str, Any]],
              start_xy: Tuple[float, float]) -> List[Tuple[str, Tuple[float, float]]]:
    """
    AUTONOMOUS_MEDIC_DELIVERY — order deliveries by urgency, then distance.

    Overview
    --------
    Sort by descending urgency, break ties by nearest-next greedy hop.

    Parameters
    ----------
    reqs : [{'id':str,'xy':(x,y),'urgency':float}]
    start_xy : (x,y)

    Returns
    -------
    List[(id, (x,y))] ordered route

    Examples
    --------
    >>> glyph_674([{'id':'A','xy':(1,0),'urgency':1}], (0,0))[0][0]
    'A'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n + n^2)
    - Space : O(n)
    """
    pending = sorted([(r['id'], r['xy'], float(r.get('urgency', 0.0))) for r in reqs],
                     key=lambda t: t[2], reverse=True)
    out: List[Tuple[str, Tuple[float, float]]] = []
    here = start_xy
    while pending:
        # among highest urgency items, pick nearest
        top = [t for t in pending if t[2] == pending[0][2]]
        pick = min(top, key=lambda t: math.hypot(t[1][0]-here[0], t[1][1]-here[1]))
        out.append((pick[0], pick[1]))
        pending.remove(pick)
        here = pick[1]
    return out
