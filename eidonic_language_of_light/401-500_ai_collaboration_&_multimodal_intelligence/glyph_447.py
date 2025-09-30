# glyph_447.py — Thread Merge
# -----------------------------------------------------------------------------
# ID:            447
# Pack:          Pack 005 (401–500)
# Name:          Thread Merge
# Class:         merger
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_447(threads: Sequence[Sequence[str]]) -> List[str]:
    """
    Thread Merge — interleave multiple message threads deterministically.

    Overview
    --------
    Round-robin across `threads`, skipping empties, until all are exhausted.

    Parameters
    ----------
    threads : Sequence[Sequence[str]]

    Returns
    -------
    List[str]

    Examples
    --------
    >>> glyph_447([["a1","a2"], ["b1"]])
    ['a1', 'b1', 'a2']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N)
    - Space : O(N)
    """
    queues = [list(t) for t in threads]
    out: List[str] = []
    changed = True
    while changed:
        changed = False
        for q in queues:
            if q:
                out.append(q.pop(0))
                changed = True
    return out
