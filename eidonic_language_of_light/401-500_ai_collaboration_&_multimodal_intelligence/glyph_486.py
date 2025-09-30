# glyph_486.py — Route Discovery
# -----------------------------------------------------------------------------
# ID:            486
# Pack:          Pack 005 (401–500)
# Name:          Route Discovery
# Class:         planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Sequence, List

def glyph_486(graph: Mapping[str, Sequence[str]], src: str, dst: str) -> List[str]:
    """
    Route Discovery — shortest hop path via BFS.

    Overview
    --------
    Returns node list from src to dst inclusive; [] if unreachable.

    Parameters
    ----------
    graph : Mapping[node, neighbors]
    src   : str
    dst   : str

    Returns
    -------
    List[str]

    Examples
    --------
    >>> glyph_486({'A':['B'],'B':['C']}, 'A','C')
    ['A', 'B', 'C']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(V+E)
    - Space : O(V)
    """
    from collections import deque
    q = deque([src])
    parent = {src: None}
    while q:
        u = q.popleft()
        if u == dst:
            break
        for v in graph.get(u, []):
            if v not in parent:
                parent[v] = u
                q.append(v)
    if dst not in parent:
        return []
    path = []
    cur = dst
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]
