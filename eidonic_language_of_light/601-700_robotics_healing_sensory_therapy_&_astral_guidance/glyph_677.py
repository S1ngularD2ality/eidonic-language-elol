# glyph_677.py — RAPID_RESPONSE_ROUTE
# -----------------------------------------------------------------------------
# ID:            677
# Pack:          Pack 007 (601–700)
# Name:          RAPID_RESPONSE_ROUTE
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # Dijkstra-lite on tiny graphs
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Tuple, List, Dict, Any

def glyph_677(graph: Mapping[int, Mapping[int, float]],
              start: int, goal: int, *,
              hazard_weight: float = 2.0,
              hazards: Mapping[Tuple[int,int], float] | None = None) -> Dict[str, Any]:
    """
    RAPID_RESPONSE_ROUTE — shortest path with hazard penalties.

    Overview
    --------
    Runs uniform-cost search on a small graph, adding `hazard_weight*h`
    for edges tagged with hazard level `h` in `hazards`.

    Parameters
    ----------
    graph : {u:{v:cost}}
    start, goal : int
    hazard_weight : float, optional (default: ``2.0``)
    hazards : {(u,v): h}, optional

    Returns
    -------
    {'path': List[int], 'cost': float}

    Examples
    --------
    >>> g = {0:{1:1}, 1:{2:1}}
    >>> glyph_677(g, 0, 2)['path']
    [0, 1, 2]

    Exceptions
    ----------
    - RuntimeError: if no path exists.

    Complexity
    ----------
    - Time  : O(E log V)
    - Space : O(V)
    """
    import heapq, math
    H = hazards or {}
    dist = {start: 0.0}
    prev: Dict[int,int] = {}
    pq = [(0.0, start)]
    seen = set()

    while pq:
        d,u = heapq.heappop(pq)
        if u in seen: continue
        seen.add(u)
        if u == goal: break
        for v,c in graph.get(u, {}).items():
            h = H.get((u,v), 0.0)
            nd = d + float(c) + hazard_weight*float(h)
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    if goal not in dist:
        raise RuntimeError("no path")

    path: List[int] = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.append(start)
    path.reverse()
    return {"path": path, "cost": float(dist[goal])}
