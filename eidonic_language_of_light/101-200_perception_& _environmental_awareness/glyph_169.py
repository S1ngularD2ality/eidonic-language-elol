# glyph_169.py — Temporal Sequence Fragmentor
# -----------------------------------------------------------------------------
# ID:            169
# Pack:          Pack 002 (101–200)
# Name:          Temporal Sequence Fragmentor
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_169(seq: Sequence[int], boundaries: Sequence[int]) -> List[List[int]]:
    """
    Temporal Sequence Fragmentor — cut a stream at explicit boundaries.

    Overview
    --------
    Given sorted `boundaries` (start indices of segments), slice seq into segments
    [b[i]..b[i+1]) and the final [b[-1]..end).

    Parameters
    ----------
    seq : Sequence[int]
    boundaries : Sequence[int]

    Returns
    -------
    List[List[int]]
        Segments of the original sequence.

    Examples
    --------
    >>> glyph_169(list(range(10)), boundaries=[0, 3, 7])
    [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9]]
    """
    n = len(seq)
    b = sorted(set(int(x) for x in boundaries if 0 <= int(x) <= n))
    if not b or b[0] != 0:
        b = [0] + b
    out: List[List[int]] = []
    for i in range(len(b)):
        j = b[i]
        k = b[i+1] if i+1 < len(b) else n
        out.append([int(v) for v in seq[j:k]])
    return out
