# glyph_430.py — Embedding Chorus
# -----------------------------------------------------------------------------
# ID:            430
# Pack:          Pack 005 (401–500)
# Name:          Embedding Chorus
# Class:         encoder
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_430(stack: Sequence[Sequence[float]]) -> List[float]:
    """
    Embedding Chorus — elementwise mean across vectors.

    Overview
    --------
    Returns the average embedding; empty if no vectors are given.

    Parameters
    ----------
    stack : Sequence[Sequence[float]]

    Returns
    -------
    List[float]

    Examples
    --------
    >>> glyph_430([[1,2],[3,4]])
    [2.0, 3.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N·D)
    - Space : O(D)
    """
    if not stack:
        return []
    n = len(stack); m = len(stack[0])
    out = [0.0]*m
    for vec in stack:
        for i,v in enumerate(vec):
            out[i] += float(v)
    return [v/n for v in out]
