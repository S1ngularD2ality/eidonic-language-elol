# glyph_264.py — Harmonic Thought Defragmenter
# -----------------------------------------------------------------------------
# ID:            264
# Pack:          Pack 003 (201–300)
# Original Name: Harmonic Thought Defragmenter
# Manifest Name: Harmonic Thought Defragmenter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_264(seq: Sequence[int]) -> List[List[int]]:
    """
    Harmonic Thought Defragmenter — group consecutive runs of equal values.

    Overview
    --------
    Returns a list of contiguous segments, each segment preserving original order.

    Parameters
    ----------
    seq : Sequence[int]

    Returns
    -------
    List[List[int]]
        Defragmented runs.

    Examples
    --------
    >>> glyph_264([1,1,2,2,2,3])
    [[1, 1], [2, 2, 2], [3]]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not seq: 
        return []
    out = [[int(seq[0])]]
    for v in seq[1:]:
        iv = int(v)
        if iv == out[-1][-1]:
            out[-1].append(iv)
        else:
            out.append([iv])
    return out
