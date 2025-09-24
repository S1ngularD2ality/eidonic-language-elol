# glyph_187.py — Recursive Mirror Amplifier
# -----------------------------------------------------------------------------
# ID:            187
# Pack:          Pack 002 (101–200)
# Name:          Recursive Mirror Amplifier
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

def glyph_187(depth: int, *, base: int = 1) -> List[int]:
    """
    Recursive Mirror Amplifier — palindromic expansion.

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
        Amplified palindromic index.

    Examples
    --------
    >>> glyph_187(3, base=10)
    [10, 11, 10, 12, 10, 11, 10]
    """
    if depth <= 0:
        return []
    prev = glyph_187(depth-1, base=base)
    return prev + [base + depth - 1] + list(reversed(prev))
