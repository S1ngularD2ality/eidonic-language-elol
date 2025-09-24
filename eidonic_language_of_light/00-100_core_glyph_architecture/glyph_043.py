# glyph_043.py — Thought Sequence Divider
# -----------------------------------------------------------------------------
# ID:            043
# Pack:          Pack 001 (000–100)
# Name:          Thought Sequence Divider
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

def glyph_043(seq: Sequence[float], *, parts: int) -> List[List[float]]:
    """
    Thought Sequence Divider — split a sequence into nearly equal contiguous chunks.

    Overview
    --------
    Divides `seq` into `parts` sublists whose sizes differ by at most 1, preserving order.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    parts : int
        Number of chunks (>= 1).

    Returns
    -------
    List[List[float]]
        List of `parts` chunks (some may be empty if `seq` is empty).

    Examples
    --------
    >>> glyph_043([0,1,2,3,4], parts=2)
    [[0,1,2],[3,4]]

    Exceptions
    ----------
    - ValueError : if `parts < 1`.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if parts < 1:
        raise ValueError("parts must be >= 1")
    n = len(seq)
    if n == 0:
        return [[] for _ in range(parts)]
    base, rem = divmod(n, parts)
    out: List[List[float]] = []
    i = 0
    for p in range(parts):
        k = base + (1 if p < rem else 0)
        out.append([float(v) for v in seq[i:i+k]])
        i += k
    return out
