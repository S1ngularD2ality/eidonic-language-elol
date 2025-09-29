# glyph_437.py — Memory Loom
# -----------------------------------------------------------------------------
# ID:            437
# Pack:          Pack 005 (401–500)
# Name:          Memory Loom
# Class:         memory
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_437(chunks: Sequence[str]) -> List[str]:
    """
    Memory Loom — weave chunks into a rolling, de-duplicated context.

    Overview
    --------
    Keeps first occurrence of each string, preserving order.

    Parameters
    ----------
    chunks : Sequence[str]

    Returns
    -------
    List[str]

    Examples
    --------
    >>> glyph_437(["a","b","a","c"])
    ['a', 'b', 'c']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    seen = set()
    out: List[str] = []
    for c in chunks:
        s = str(c)
        if s not in seen:
            seen.add(s); out.append(s)
    return out
