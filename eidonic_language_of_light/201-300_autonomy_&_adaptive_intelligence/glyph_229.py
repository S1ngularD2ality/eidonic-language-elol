# glyph_229.py — Soul Circuit Mapper
# -----------------------------------------------------------------------------
# ID:            229
# Pack:          Pack 003 (201–300)
# Name:          Soul Circuit Mapper
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def glyph_229(nodes: Sequence[T], edges: Sequence[Tuple[int, int]]) -> List[Tuple[T, T]]:
    """
    Soul Circuit Mapper — map edge indices to node pairs.

    Overview
    --------
    Given nodes and integer edges (i,j), returns [(nodes[i], nodes[j])].

    Parameters
    ----------
    nodes : Sequence[T]
    edges : Sequence[Tuple[int, int]]

    Returns
    -------
    List[Tuple[T,T]]
        Concrete edge list.

    Examples
    --------
    >>> glyph_229(['a','b','c'], [(0,1),(2,1)])
    [('a', 'b'), ('c', 'b')]
    """
    out: List[Tuple[T, T]] = []
    n = len(nodes)
    for i, j in edges:
        if 0 <= i < n and 0 <= j < n:
            out.append((nodes[i], nodes[j]))
    return out
