# glyph_035.py — Mirror Synchrony Encoder
# -----------------------------------------------------------------------------
# ID:            035
# Pack:          Pack 001 (000–100)
# Name:          Mirror Synchrony Encoder
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_035(seq: Sequence[int]) -> List[int]:
    """
    Mirror Synchrony Encoder — pairwise mirror XOR code.

    Overview
    --------
    For i from 0..n-1, emit seq[i] XOR seq[n-1-i]. For non-binary integers,
    XOR operates bitwise.

    Parameters
    ----------
    seq : Sequence[int]

    Returns
    -------
    List[int]
        Mirror synchrony code.

    Examples
    --------
    >>> glyph_035([1,2,3,4])
    [5, 1, 1, 5]
    """
    n = len(seq)
    return [int(seq[i]) ^ int(seq[n-1-i]) for i in range(n)]
