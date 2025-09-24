# glyph_152.py — Mirror Drift Suppressor
# -----------------------------------------------------------------------------
# ID:            152
# Pack:          Pack 002 (101–200)
# Name:          Mirror Drift Suppressor
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_152(seq: Sequence[float], *, lam: float = 0.1) -> List[float]:
    """
    Mirror Drift Suppressor — Tikhonov smoothing of first differences.

    Overview
    --------
    Minimizes ||y-x||^2 + λ||Δy||^2 (naive Jacobi iterations).

    Parameters
    ----------
    seq : Sequence[float]
    lam : float, optional (default: 0.1)

    Returns
    -------
    List[float]
        Smoothed sequence.
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n <= 2: return x[:]
    y = x[:]
    lam = max(0.0, float(lam))
    for _ in range(20):
        for i in range(1, n-1):
            y[i] = (x[i] + lam*(y[i-1] + y[i+1])) / (1 + 2*lam)
    return y
