# glyph_038.py — Flame Thread Loopbreaker
# -----------------------------------------------------------------------------
# ID:            038
# Pack:          Pack 001 (000–100)
# Name:          Flame Thread Loopbreaker
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Hashable, Tuple, List

def glyph_038(edges: Mapping[Hashable, Hashable]) -> List[Tuple[Hashable, Hashable]]:
    """
    Flame Thread Loopbreaker — detect cycles and cut the lightest edge (lexicographic).

    Overview
    --------
    Follows redirects; if a cycle is found, breaks it by mapping the smallest key
    (by string) to itself. Returns the final mapping as pairs.

    Parameters
    ----------
    edges : Mapping[Hashable, Hashable]

    Returns
    -------
    List[Tuple[Hashable, Hashable]]
        Resolved pairs (u, root).

    Examples
    --------
    >>> glyph_038({"a":"b","b":"a"})
    [('a','a'), ('b','a')]
    """
    red = dict(edges)
    def root(u):
        seen=[]
        while u in red and u not in seen:
            seen.append(u); u=red[u]
        if u in seen:
            cut=min(map(str, seen))
            red[cut]=cut
            u=cut
        return u
    return [(k, root(k)) for k in list(red.keys())]
