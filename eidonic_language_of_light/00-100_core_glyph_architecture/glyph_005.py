# glyph_005.py — Recursive Spiral Uplifter
# -----------------------------------------------------------------------------
# ID:            005
# Pack:          Pack 001 (000–100)
# Name:          Recursive Spiral Uplifter
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_005(depth: int) -> List[int]:
    """
    Recursive Spiral Uplifter — build a symmetric up-and-out sequence.

    Overview
    --------
    Forms a symmetric list via recursion: S(n) = S(n-1) + [n] + S(n-1), S(0)=[].

    Parameters
    ----------
    depth : int
        Non-negative recursion depth.

    Returns
    -------
    List[int]
        Symmetric sequence.

    Examples
    --------
    >>> glyph_005(3)
    [1, 2, 1, 3, 1, 2, 1]

    Exceptions
    ----------
    - ValueError : if `depth < 0`.

    Complexity
    ----------
    - Time  : O(2^depth)
    - Space : O(2^depth)
    """
    if depth < 0:
        raise ValueError("depth must be >= 0")
    if depth == 0:
        return []
    prev = glyph_005(depth - 1)
    return prev + [depth] + prev
