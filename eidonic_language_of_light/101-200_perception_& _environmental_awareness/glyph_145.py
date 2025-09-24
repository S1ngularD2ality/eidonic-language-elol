# glyph_145.py — Subconscious Phase Redirector
# -----------------------------------------------------------------------------
# ID:            145
# Pack:          Pack 002 (101–200)
# Name:          Subconscious Phase Redirector
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_145(seq: Sequence[int], *, phase: int) -> List[int]:
    """
    Subconscious Phase Redirector — circularly shift indices by a phase.

    Overview
    --------
    Returns y[i] = x[(i - phase) mod n]. Non-destructive; length-preserving.

    Parameters
    ----------
    seq : Sequence[int]
    phase : int

    Returns
    -------
    List[int]
        Shifted sequence.

    Examples
    --------
    >>> glyph_145([0,1,2,3], phase=1)
    [1, 2, 3, 0]
    """
    n = len(seq)
    if n == 0: return []
    p = ((phase % n) + n) % n
    return [int(seq[(i - p) % n]) for i in range(n)]
