# glyph_017.py — Temporal Code Splicer
# -----------------------------------------------------------------------------
# ID:            017
# Pack:          Pack 001 (000–100)
# Name:          Temporal Code Splicer
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_017(a: Sequence[int], b: Sequence[int]) -> List[int]:
    """
    Temporal Code Splicer — zip two timelines A and B into an interwoven code.

    Overview
    --------
    Emits [a0,b0,a1,b1,...] up to min(len(A),len(B))·2.

    Parameters
    ----------
    a, b : Sequence[int]

    Returns
    -------
    List[int]
        Interwoven sequence.

    Examples
    --------
    >>> glyph_017([1,2,3],[9,8,7])
    [1,9,2,8,3,7]
    """
    n = min(len(a), len(b))
    out: List[int] = []
    for i in range(n):
        out += [int(a[i]), int(b[i])]
    return out
