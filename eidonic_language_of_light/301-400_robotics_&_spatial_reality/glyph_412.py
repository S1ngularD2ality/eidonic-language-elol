# glyph_412.py — Route Weaver
# -----------------------------------------------------------------------------
# ID:            412
# Pack:          Pack 005 (401–500)
# Name:          Route Weaver
# Class:         planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, List

def glyph_412(stops: Sequence[str], costs: Mapping[str, float]) -> List[str]:
    """
    Route Weaver — greedy pass minimizing symbolic hop costs.

    Overview
    --------
    Starting from the first stop, repeatedly selects the remaining stop with the
    lowest cost edge ``"{current}->{candidate}"``; ties broken by order.

    Parameters
    ----------
    stops : Sequence[str]
    costs : Mapping[str,float]

    Returns
    -------
    List[str] : ordered route

    Examples
    --------
    >>> glyph_412(["A","B","C"], {"A->B":1,"A->C":2,"B->C":1})
    ['A', 'B', 'C']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    todo = list(stops)
    if not todo:
        return []
    route = [todo.pop(0)]
    while todo:
        ref = route[-1]
        nxt = min(todo, key=lambda s: float(costs.get(f"{ref}->{s}", 1e18)))
        route.append(nxt)
        todo.remove(nxt)
    return route
