# glyph_029.py — Thought Pattern Impressor
# -----------------------------------------------------------------------------
# ID:            029
# Pack:          Pack 001 (000–100)
# Name:          Thought Pattern Impressor
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

def glyph_029(seq: Sequence[float], kernel: Sequence[float]) -> List[float]:
    """
    Thought Pattern Impressor — 1D valid convolution (portable, O(n·k)).

    Overview
    --------
    Slides `kernel` across `seq` without padding; returns length n-k+1.

    Parameters
    ----------
    seq : Sequence[float]
    kernel : Sequence[float]

    Returns
    -------
    List[float]
        Convolved values.

    Examples
    --------
    >>> glyph_029([1,2,3,4], [1,0,-1])
    [ -2.0, -2.0 ]
    """
    x = [float(v) for v in seq]
    h = [float(v) for v in kernel]
    n, k = len(x), len(h)
    if n == 0 or k == 0 or k > n:
        return []
    out = []
    for i in range(n-k+1):
        out.append(sum(x[i+j]*h[j] for j in range(k)))
    return out
