# glyph_266.py — Recursive Mirror Loopbinder
# -----------------------------------------------------------------------------
# ID:            266
# Pack:          Pack 003 (201–300)
# Original Name: Recursive Mirror Loopbinder
# Manifest Name: Recursive Mirror Loopbinder
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_266(depth: int, *, base: int = 0) -> list[int]:
    """
    Recursive Mirror Loopbinder — palindromic index growth.

    Overview
    --------
    S(0)=[]; S(d)=S(d-1)+[base+d-1]+reverse(S(d-1)).

    Parameters
    ----------
    depth : int
    base  : int, optional (default: 0)

    Returns
    -------
    list[int]
        Palindromic indices.

    Examples
    --------
    >>> glyph_266(3, base=5)
    [5, 6, 5, 7, 5, 6, 5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(2^depth)
    - Space : O(2^depth)
    """
    if depth <= 0:
        return []
    prev = glyph_266(depth-1, base=base)
    return prev + [base + depth - 1] + prev[::-1]
