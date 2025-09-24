# glyph_135.py — Anchor Shift Collapser
# -----------------------------------------------------------------------------
# ID:            135
# Pack:          Pack 002 (101–200)
# Name:          Anchor Shift Collapser
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

def glyph_135(a: Sequence[float], b: Sequence[float]) -> Tuple[int, float]:
    """
    Anchor Shift Collapser — find circular shift minimizing L2 distance.

    Overview
    --------
    Returns (k, error) where b is rotated by k to best match a.

    Parameters
    ----------
    a, b : Sequence[float]

    Returns
    -------
    (int, float)
        (best_shift, min_error)
    """
    n = min(len(a), len(b))
    if n == 0:
        return 0, 0.0
    import math
    best_k, best_e = 0, float("inf")
    A = [float(v) for v in a[:n]]
    B = [float(v) for v in b[:n]]
    for k in range(n):
        e = sum((A[i] - B[(i+k) % n])**2 for i in range(n))
        if e < best_e:
            best_e = e; best_k = k
    return best_k, best_e
