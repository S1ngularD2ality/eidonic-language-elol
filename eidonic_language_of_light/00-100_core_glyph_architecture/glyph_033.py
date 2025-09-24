# glyph_033.py — Symbolic Density Reducer
# -----------------------------------------------------------------------------
# ID:            033
# Pack:          Pack 001 (000–100)
# Name:          Symbolic Density Reducer
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from collections import Counter
from typing import Sequence, List, Tuple

def glyph_033(tokens: Sequence[str], *, topk: int = 10) -> List[Tuple[str, int]]:
    """
    Symbolic Density Reducer — count token frequencies and return top-k.

    Overview
    --------
    Produces a sorted list of (token, count) by descending count then lexicographically.

    Parameters
    ----------
    tokens : Sequence[str]
    topk : int, optional (default: 10)

    Returns
    -------
    List[Tuple[str,int]]
        Top-k token counts.

    Examples
    --------
    >>> glyph_033(["a","b","a","c","a","b"], topk=2)
    [('a',3), ('b',2)]
    """
    c = Counter(tokens)
    items = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:max(0, int(topk))]
