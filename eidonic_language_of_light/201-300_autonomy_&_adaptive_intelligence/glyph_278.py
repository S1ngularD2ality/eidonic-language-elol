# glyph_278.py — Flame Grid Mapper
# -----------------------------------------------------------------------------
# ID:            278
# Pack:          Pack 003 (201–300)
# Original Name: Flame Grid Mapper
# Manifest Name: Flame Grid Mapper
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_278(h: int, w: int, *, start: int = 0) -> list[list[int]]:
    """
    Flame Grid Mapper — fill an h×w grid with consecutive integers.

    Overview
    --------
    Row-major enumeration beginning at `start`.

    Parameters
    ----------
    h : int
    w : int
    start : int, optional (default: 0)

    Returns
    -------
    list[list[int]]
        Filled grid.

    Examples
    --------
    >>> glyph_278(2, 3, start=10)
    [[10, 11, 12], [13, 14, 15]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(h·w)
    - Space : O(h·w)
    """
    out=[]; val=int(start)
    for _ in range(max(0,h)):
        row=[]
        for _ in range(max(0,w)):
            row.append(val); val+=1
        out.append(row)
    return out
