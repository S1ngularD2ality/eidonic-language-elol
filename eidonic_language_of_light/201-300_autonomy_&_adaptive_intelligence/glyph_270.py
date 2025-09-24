# glyph_270.py — Symbolic Pattern Merger
# -----------------------------------------------------------------------------
# ID:            270
# Pack:          Pack 003 (201–300)
# Original Name: Symbolic Pattern Merger
# Manifest Name: Symbolic Pattern Merger
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_270(field: list[list[float]]) -> list[list[float]]:
    """
    Symbolic Pattern Merger — 180° rotation across both axes.

    Overview
    --------
    Produces a field rotated by 180°, aligning patterns across opposite corners.

    Parameters
    ----------
    field : list[list[float]]

    Returns
    -------
    list[list[float]]
        Rotated field.

    Examples
    --------
    >>> glyph_270([[1,2],[3,4]])
    [[4.0, 3.0], [2.0, 1.0]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(1)
    """
    return [list(reversed(row)) for row in reversed(field)]
