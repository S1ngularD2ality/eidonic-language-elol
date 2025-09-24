# glyph_089.py — Inner Symbol Decoder
# -----------------------------------------------------------------------------
# ID:            089
# Pack:          Pack 001 (000–100)
# Name:          Inner Symbol Decoder
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from collections import Counter
from typing import Sequence, List, Tuple

def glyph_089(tokens: Sequence[str], *, topk: int = 8) -> List[Tuple[str, int]]:
    """
    Inner Symbol Decoder — reveal dominant tokens.

    Overview
    --------
    Counts token frequencies and returns top-k sorted by count then lexicographically.

    Parameters
    ----------
    tokens : Sequence[str]
    topk : int, optional (default: 8)

    Returns
    -------
    List[Tuple[str,int]]
        Top tokens.

    Examples
    --------
    >>> glyph_089(["a","b","a","c","a","b"], topk=2)
    [('a', 3), ('b', 2)]
    """
    c = Counter(tokens)
    return sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:max(0, int(topk))]
