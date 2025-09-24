# glyph_099.py — Quantum Key Differentiator
# -----------------------------------------------------------------------------
# ID:            099
# Pack:          Pack 001 (000–100)
# Name:          Quantum Key Differentiator
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_099(keys: Sequence[int]) -> List[int]:
    """
    Quantum Key Differentiator — first differences with wraparound.

    Overview
    --------
    Computes `d[i] = keys[(i+1) mod n] - keys[i]` for i=0..n-1.

    Parameters
    ----------
    keys : Sequence[int]

    Returns
    -------
    List[int]
        Circular differences.

    Examples
    --------
    >>> glyph_099([1,3,6,10])
    [2, 3, 4, -9]
    """
    n = len(keys)
    if n == 0:
        return []
    return [int(keys[(i+1) % n]) - int(keys[i]) for i in range(n)]
