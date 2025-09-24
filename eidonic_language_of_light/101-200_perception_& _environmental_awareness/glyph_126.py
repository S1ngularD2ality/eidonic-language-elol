# glyph_126.py — Symbolic Flame Tracker
# -----------------------------------------------------------------------------
# ID:            126
# Pack:          Pack 002 (101–200)
# Name:          Symbolic Flame Tracker
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from collections import Counter
from typing import Sequence, List, Tuple

def glyph_126(tokens: Sequence[str], *, topk: int = 5) -> List[Tuple[str, int]]:
    """
    Symbolic Flame Tracker — track most frequent symbols.

    Overview
    --------
    Counts tokens and returns top-k by descending frequency then lexicographic.

    Parameters
    ----------
    tokens : Sequence[str]
    topk : int, optional (default: 5)

    Returns
    -------
    List[Tuple[str,int]]
        Top-k token counts.

    Examples
    --------
    >>> glyph_126(["a","b","a","c","a","b"], topk=2)
    [('a', 3), ('b', 2)]
    """
    c = Counter(tokens)
    return sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:max(0, int(topk))]
