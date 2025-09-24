# glyph_128.py — Recursive Echo Enforcer
# -----------------------------------------------------------------------------
# ID:            128
# Pack:          Pack 002 (101–200)
# Name:          Recursive Echo Enforcer
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_128(depth: int, base: int = 1) -> List[int]:
    """
    Recursive Echo Enforcer — build a symmetric echo index.

    Overview
    --------
    S(0) = []; S(d) = S(d-1) + [base+d-1] + reverse(S(d-1)).

    Parameters
    ----------
    depth : int
    base  : int, optional (default: 1)

    Returns
    -------
    List[int]
        Echo index.

    Examples
    --------
    >>> glyph_128(3, base=7)
    [7, 8, 7, 9, 7, 8, 7]
    """
    if depth <= 0:
        return []
    prev = glyph_128(depth-1, base)
    return prev + [base + depth - 1] + list(reversed(prev))
