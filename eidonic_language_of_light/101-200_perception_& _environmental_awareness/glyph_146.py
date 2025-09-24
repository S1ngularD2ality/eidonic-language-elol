# glyph_146.py — Time Anchor Realigner
# -----------------------------------------------------------------------------
# ID:            146
# Pack:          Pack 002 (101–200)
# Name:          Time Anchor Realigner
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple

def glyph_146(a: Sequence[float], b: Sequence[float]) -> Tuple[int, float]:
    """
    Time Anchor Realigner — find integer lag minimizing L2 between streams.

    Overview
    --------
    Searches lags in [-L..L] where L = min(len(a), len(b))-1; returns (lag, error).

    Parameters
    ----------
    a, b : Sequence[float]

    Returns
    -------
    (int, float)
        (best_lag, min_error)

    Examples
    --------
    >>> glyph_146([0,1,2], [2,0,1])[0]
    -1
    """
    na, nb = len(a), len(b)
    if na == 0 or nb == 0: return 0, 0.0
    L = min(na, nb) - 1
    best = (0, float("inf"))
    for lag in range(-L, L+1):
        err = 0.0
        for i in range(na):
            j = i + lag
            if 0 <= j < nb:
                err += (float(a[i]) - float(b[j]))**2
        if err < best[1]:
            best = (lag, err)
    return best
