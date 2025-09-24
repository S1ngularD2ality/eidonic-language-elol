# glyph_159.py — Recursive Intuition Loop
# -----------------------------------------------------------------------------
# ID:            159
# Pack:          Pack 002 (101–200)
# Name:          Recursive Intuition Loop
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_159(depth: int) -> list[int]:
    """
    Recursive Intuition Loop — palindromic depth index.

    Overview
    --------
    S(0) = [0]; S(d) = S(d-1) + [d] + reverse(S(d-1)).

    Parameters
    ----------
    depth : int

    Returns
    -------
    list[int]
        Intuition loop indices.

    Examples
    --------
    >>> glyph_159(2)
    [0, 1, 0, 2, 0, 1, 0]
    """
    if depth < 0: return []
    if depth == 0: return [0]
    prev = glyph_159(depth-1)
    return prev + [depth] + list(reversed(prev))
