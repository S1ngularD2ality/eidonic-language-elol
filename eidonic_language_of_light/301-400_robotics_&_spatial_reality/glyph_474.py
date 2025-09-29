# glyph_474.py — Consensus Ring
# -----------------------------------------------------------------------------
# ID:            474
# Pack:          Pack 005 (401–500)
# Name:          Consensus Ring
# Class:         topology
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_474(nodes: Sequence[str]) -> List[Tuple[str, str]]:
    """
    Consensus Ring — build directed ring edges (u -> v).

    Overview
    --------
    Returns ordered pairs linking each node to its successor (wrap-around).

    Parameters
    ----------
    nodes : Sequence[str]

    Returns
    -------
    List[(str,str)]

    Examples
    --------
    >>> glyph_474(["a","b","c"])
    [('a', 'b'), ('b', 'c'), ('c', 'a')]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(nodes)
    return [(nodes[i], nodes[(i+1) % n]) for i in range(n)] if n else []
