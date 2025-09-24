# glyph_090.py — Recursive Mirror Trigger
# -----------------------------------------------------------------------------
# ID:            090
# Pack:          Pack 001 (000–100)
# Name:          Recursive Mirror Trigger
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

def glyph_090(depth: int) -> List[int]:
    """
    Recursive Mirror Trigger — palindromic index cascade.

    Overview
    --------
    Generates `[0]` at depth 0; at each deeper level, wraps previous list with its
    reverse: `S_{n+1} = S_n + [n+1] + rev(S_n)`.

    Parameters
    ----------
    depth : int
        Depth >= 0.

    Returns
    -------
    List[int]
        Trigger sequence.

    Examples
    --------
    >>> glyph_090(2)
    [0, 1, 0, 2, 0, 1, 0]
    """
    if depth < 0:
        return []
    if depth == 0:
        return [0]
    prev = glyph_090(depth - 1)
    return prev + [depth] + list(reversed(prev))
