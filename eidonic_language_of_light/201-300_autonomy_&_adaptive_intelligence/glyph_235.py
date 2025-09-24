# glyph_235.py — Anchor Mirror Realigner
# -----------------------------------------------------------------------------
# ID:            235
# Pack:          Pack 003 (201–300)
# Name:          Anchor Mirror Realigner
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_235(seq: Sequence[int], *, phase: int) -> List[int]:
    """
    Anchor Mirror Realigner — circular shift by integer phase.

    Overview
    --------
    y[i] = x[(i - phase) mod n]. Non-destructive; length-preserving.

    Parameters
    ----------
    seq : Sequence[int]
    phase : int

    Returns
    -------
    List[int]
        Realigned sequence.

    Examples
    --------
    >>> glyph_235([0,1,2,3], phase=1)
    [1, 2, 3, 0]
    """
    n = len(seq)
    if n == 0: return []
    p = ((phase % n) + n) % n
    return [int(seq[(i - p) % n]) for i in range(n)]
