# glyph_445.py — Memory Pruner
# -----------------------------------------------------------------------------
# ID:            445
# Pack:          Pack 005 (401–500)
# Name:          Memory Pruner
# Class:         memory
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_445(items: Sequence[Tuple[str, float]], *, keep: int, min_score: float = 0.0) -> List[str]:
    """
    Memory Pruner — keep top-K items by score with a minimum threshold.

    Overview
    --------
    Sorts by score descending, keeps first `keep`, and filters by min_score.

    Parameters
    ----------
    items     : Sequence[(id, score)]
    keep      : int
    min_score : float, optional (default: 0.0)

    Returns
    -------
    List[str] : kept ids.

    Examples
    --------
    >>> glyph_445([("a",0.9),("b",0.1)], keep=1)
    ['a']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    k = max(0, int(keep))
    arr = [(str(i), float(s)) for i, s in items if float(s) >= float(min_score)]
    arr.sort(key=lambda t: -t[1])
    return [i for i, _ in arr[:k]]
