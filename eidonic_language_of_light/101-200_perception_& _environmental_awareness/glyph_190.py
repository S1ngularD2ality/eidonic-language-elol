# glyph_190.py — Quantum Reflection Collapser
# -----------------------------------------------------------------------------
# ID:            190
# Pack:          Pack 002 (101–200)
# Name:          Quantum Reflection Collapser
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

def glyph_190(seq: Sequence[float]) -> Tuple[int, float]:
    """
    Quantum Reflection Collapser — best mirror lag via L2 distance.

    Overview
    --------
    For lag ℓ, compare x[i] with x[n-1-(i+ℓ)] (valid overlaps). Returns (lag, error)
    minimizing squared error.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (int, float)
        (best_lag, min_error)

    Examples
    --------
    >>> glyph_190([1,2,3,2,1])[0]
    0
    """
    n = len(seq)
    if n == 0:
        return 0, 0.0
    best = (0, float("inf"))
    x = [float(v) for v in seq]
    for lag in range(-n+1, n):
        err = 0.0
        for i in range(n):
            j = n-1-(i+lag)
            if 0 <= j < n:
                err += (x[i] - x[j])**2
        if err < best[1]:
            best = (lag, err)
    return best
