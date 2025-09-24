# glyph_258.py — Mirror Signature Encoder
# -----------------------------------------------------------------------------
# ID:            258
# Pack:          Pack 003 (201–300)
# Name:          Mirror Signature Encoder
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_258(seq: Sequence[float]) -> List[float]:
    """
    Mirror Signature Encoder — correlation with reversed copy (per-lag).

    Overview
    --------
    Computes Pearson-like similarity between x and reverse(x) over sliding lags.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[float]
        Mirror signature (length n).

    Examples
    --------
    >>> sig = glyph_258([1,2,3,2,1])
    >>> len(sig)
    5

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n²)
    - Space : O(1)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return []
    mu = sum(x) / n
    xr = x[::-1]
    out: List[float] = []
    for lag in range(n):
        num = den1 = den2 = 0.0
        for i in range(n - lag):
            a = x[i] - mu
            b = xr[i + lag] - mu
            num += a * b; den1 += a * a; den2 += b * b
        den = (den1 * den2) ** 0.5 or 1.0
        out.append(num / den)
    return out
