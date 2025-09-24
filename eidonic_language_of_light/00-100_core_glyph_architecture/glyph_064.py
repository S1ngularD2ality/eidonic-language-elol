# glyph_064.py — Frequency Pattern Stretcher
# -----------------------------------------------------------------------------
# ID:            064
# Pack:          Pack 001 (000–100)
# Name:          Frequency Pattern Stretcher
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

def glyph_064(seq: Sequence[float], *, factor: float) -> List[float]:
    """
    Frequency Pattern Stretcher — resample by rational factor (nearest time-warp).

    Overview
    --------
    Stretches or compresses a sequence by factor r>0 using nearest-neighbor
    resampling of the time axis: y[t] = x[t/r]. Preserves endpoints.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    factor : float
        Positive stretch factor (>0). >1 = longer, <1 = shorter.

    Returns
    -------
    List[float]
        Resampled sequence, length round(len(seq)*factor).

    Examples
    --------
    >>> glyph_064([0,10,0], factor=2.0)
    [0.0, 10.0, 0.0, 0.0, 0.0, 0.0]

    Exceptions
    ----------
    - ValueError : if `factor <= 0`.

    Complexity
    ----------
    - Time  : O(n·factor)
    - Space : O(n·factor)
    """
    if factor <= 0:
        raise ValueError("factor must be > 0")
    n = len(seq)
    if n == 0:
        return []
    m = max(1, int(round(n * factor)))
    out = [0.0]*m
    for t in range(m):
        src = int(round(t / factor))
        if src >= n:
            src = n-1
        out[t] = float(seq[src])
    return out
