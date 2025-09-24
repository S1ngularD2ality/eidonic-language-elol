# glyph_067.py — Mirror Trail Redirector
# -----------------------------------------------------------------------------
# ID:            067
# Pack:          Pack 001 (000–100)
# Name:          Mirror Trail Redirector
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Hashable, List, Tuple

def glyph_067(redirects: Mapping[Hashable, Hashable]) -> List[Tuple[Hashable, Hashable]]:
    """
    Mirror Trail Redirector — resolve redirect chains to canonical mirrors.

    Overview
    --------
    For mapping R(u)=v, follows chains u→…→root and returns (u, root). Simple cycles
    are broken by picking the smallest string representation.

    Parameters
    ----------
    redirects : Mapping[Hashable, Hashable]
        Redirect graph.

    Returns
    -------
    List[Tuple[Hashable, Hashable]]
        List of (source, root) pairs.

    Examples
    --------
    >>> glyph_067({"a":"b","b":"c"})
    [('a','c'),('b','c')]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(E) average
    - Space : O(V)
    """
    def root(u):
        seen = []
        while u in redirects and u not in seen:
            seen.append(u)
            u = redirects[u]
        if u in seen:
            u = min(map(str, seen))
        return u
    return [(k, root(k)) for k in redirects.keys()]
