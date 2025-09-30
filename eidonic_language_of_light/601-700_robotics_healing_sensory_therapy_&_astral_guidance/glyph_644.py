# glyph_644.py — RESCUE_MODE
# -----------------------------------------------------------------------------
# ID:            644
# Pack:          Pack 007 (601–700)
# Name:          RESCUE_MODE
# Class:         safety_planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # scoring only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Tuple

def glyph_644(calls: Sequence[Mapping[str, Any]]) -> List[Tuple[str, float]]:
    """
    RESCUE_MODE — prioritize rescue calls with ethical weighting.

    Overview
    --------
    Score = 0.5*urgency + 0.3*vulnerability + 0.2*proximity (all in 0..1).
    Returns sorted list of (id, score), highest first.

    Parameters
    ----------
    calls : Sequence[Mapping[str, Any]]
        Each: {'id': str, 'urgency': float, 'vulnerability': float, 'proximity': float}

    Returns
    -------
    List[Tuple[str, float]]

    Examples
    --------
    >>> out = glyph_644([{'id':'A','urgency':1,'vulnerability':0.5,'proximity':0.2}])
    >>> out[0][0] == 'A'
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    scored = []
    for c in calls:
        u = float(c.get("urgency", 0.0))
        v = float(c.get("vulnerability", 0.0))
        p = float(c.get("proximity", 0.0))
        scored.append((str(c.get("id", "")), 0.5*u + 0.3*v + 0.2*p))
    return sorted(scored, key=lambda x: x[1], reverse=True)
