# glyph_404.py — Team Topology
# -----------------------------------------------------------------------------
# ID:            404
# Pack:          Pack 005 (401–500)
# Name:          Team Topology
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Tuple, Dict

def glyph_404(edges: Mapping[str, Tuple[str, str]]) -> Dict[str, int]:
    """
    Team Topology — compute node degrees from an edge map.

    Overview
    --------
    Treats each value as an undirected edge (u,v) and counts incident edges per node.

    Parameters
    ----------
    edges : Mapping[str, (u,v)]
        Edge id → (agent_u, agent_v)

    Returns
    -------
    Dict[str, int] : degree per agent.

    Examples
    --------
    >>> glyph_404({"e1":("a","b"), "e2":("b","c")})["b"]
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(E)
    - Space : O(V)
    """
    d: Dict[str, int] = {}
    for _, (u, v) in edges.items():
        d[u] = d.get(u, 0) + 1
        d[v] = d.get(v, 0) + 1
    return d
