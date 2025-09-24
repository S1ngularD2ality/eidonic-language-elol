# glyph_077.py — Soul Circuit Reconstructor
# -----------------------------------------------------------------------------
# ID:            077
# Pack:          Pack 001 (000–100)
# Name:          Soul Circuit Reconstructor
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Hashable, List, Tuple

def glyph_077(edges: Sequence[Tuple[Hashable, Hashable]]) -> List[Hashable]:
    """
    Soul Circuit Reconstructor — topological sort of a DAG.

    Overview
    --------
    Uses Kahn's algorithm; raises on cycles.

    Parameters
    ----------
    edges : Sequence[Tuple[Hashable, Hashable]]
        Directed edges (u→v).

    Returns
    -------
    List[Hashable]
        Topologically ordered nodes.

    Examples
    --------
    >>> glyph_077([("a","b"),("b","c")])
    ['a','b','c']

    Exceptions
    ----------
    - ValueError : if the graph contains a cycle.

    Complexity
    ----------
    - Time  : O(V+E)
    - Space : O(V+E)
    """
    from collections import defaultdict, deque
    adj = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u,v in edges:
        adj[u].append(v); indeg[v]+=1; nodes.add(u); nodes.add(v)
    q = deque([n for n in nodes if indeg[n]==0])
    out: List[Hashable] = []
    while q:
        u = q.popleft()
        out.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    if len(out)!=len(nodes):
        raise ValueError("graph contains a cycle")
    return out
