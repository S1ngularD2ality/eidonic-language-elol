# glyph_295.py — Recursive Flame Deflector
# -----------------------------------------------------------------------------
# ID:            295
# Pack:          Pack 003 (201–300)
# Name:          Recursive Flame Deflector
# Class:         generator
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_295(depth: int, *, base: int = 0) -> list[int]:
    """
    Recursive Flame Deflector — palindromic index builder.

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
    >>> glyph_295(3, base=5)
    [5, 6, 5, 7, 5, 6, 5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(2^d)
    - Space : O(2^d)
    """
    if depth <= 0: return []
    prev = glyph_295(depth-1, base=base)
    return prev + [base + depth - 1] + prev[::-1]
