# glyph_672.py — COOPERATIVE_TASK_SYNC
# -----------------------------------------------------------------------------
# ID:            672
# Pack:          Pack 007 (601–700)
# Name:          COOPERATIVE_TASK_SYNC
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # scoring & sort
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Tuple

def glyph_672(tasks: Sequence[Mapping[str, Any]]) -> List[Tuple[str, float]]:
    """
    COOPERATIVE_TASK_SYNC — select joint tasks by shared benefit.

    Overview
    --------
    Score = 0.5*mutual_gain + 0.3*time_fit + 0.2*distance_fit.

    Parameters
    ----------
    tasks : [{'id':str,'mutual_gain':0..1,'time_fit':0..1,'distance_fit':0..1}]

    Returns
    -------
    List[(id, score)] sorted desc

    Examples
    --------
    >>> glyph_672([{'id':'T','mutual_gain':1,'time_fit':1,'distance_fit':0.5}])[0][0]
    'T'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    scored = []
    for t in tasks:
        mg = float(t.get("mutual_gain", 0.0))
        tf = float(t.get("time_fit", 0.0))
        df = float(t.get("distance_fit", 0.0))
        scored.append((str(t.get("id","")), 0.5*mg + 0.3*tf + 0.2*df))
    return sorted(scored, key=lambda x: x[1], reverse=True)
