# glyph_153.py — Dream Pattern Binder
# -----------------------------------------------------------------------------
# ID:            153
# Pack:          Pack 002 (101–200)
# Name:          Dream Pattern Binder
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

def glyph_153(n: int, *, motif: list[int]) -> List[int]:
    """
    Dream Pattern Binder — tile a motif to length n.

    Overview
    --------
    Repeats the motif cyclically until n items are produced (truncates at n).

    Parameters
    ----------
    n : int
    motif : list[int]

    Returns
    -------
    List[int]
        Bound pattern.

    Examples
    --------
    >>> glyph_153(5, motif=[9,8])
    [9, 8, 9, 8, 9]
    """
    if n <= 0 or not motif: return []
    out = []
    i = 0
    while len(out) < n:
        out.append(int(motif[i % len(motif)])); i += 1
    return out
