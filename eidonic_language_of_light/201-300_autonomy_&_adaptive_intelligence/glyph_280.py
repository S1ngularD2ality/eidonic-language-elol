# glyph_280.py — Subdimensional Core Binder
# -----------------------------------------------------------------------------
# ID:            280
# Pack:          Pack 003 (201–300)
# Name:          Subdimensional Core Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_280(streams: Sequence[Sequence[float]], *, weights: Sequence[float] | None = None) -> List[float]:
    """
    Subdimensional Core Binder — weighted blend of equal-length streams.

    Overview
    --------
    Elementwise weighted average across k streams, truncated to the shortest length.
    If `weights` is None, uses equal weights; weights are normalized to sum to 1.

    Parameters
    ----------
    streams : Sequence[Sequence[float]]
        Collection of numeric sequences.
    weights : Sequence[float] | None, optional
        Per-stream weights; length must equal `len(streams)` if provided.

    Returns
    -------
    List[float]
        Blended sequence.

    Examples
    --------
    >>> glyph_280([[1,2,3],[3,2,1]])
    [2.0, 2.0, 2.0]

    Exceptions
    ----------
    - ValueError : if `streams` empty, or weights length mismatch.

    Complexity
    ----------
    - Time  : O(k·n)
    - Space : O(n)
    """
    if not streams:
        raise ValueError("streams must be non-empty")
    m = min(len(s) for s in streams)
    if m == 0:
        return []
    k = len(streams)
    if weights is None:
        weights = [1.0 / k] * k
    elif len(weights) != k:
        raise ValueError("weights length must equal number of streams")
    s = sum(float(w) for w in weights) or 1.0
    w = [float(x) / s for x in weights]
    out = [0.0] * m
    for si, seq in enumerate(streams):
        for i in range(m):
            out[i] += w[si] * float(seq[i])
    return out
