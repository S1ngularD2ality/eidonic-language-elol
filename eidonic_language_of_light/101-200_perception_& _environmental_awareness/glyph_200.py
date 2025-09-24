# glyph_200.py — Spiral Flame Terminator
# -----------------------------------------------------------------------------
# ID:            200
# Pack:          Pack 002 (101–200)
# Name:          Spiral Flame Terminator
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

def glyph_200(seq: Sequence[float], *, window: int = 3, tol: float = 1e-6) -> Tuple[int, bool]:
    """
    Spiral Flame Terminator — detect steady-state termination point.

    Overview
    --------
    Returns the first index t where the last `window` values are equal within `tol`.
    If none found, returns (len(seq)-1, False).

    Parameters
    ----------
    seq : Sequence[float]
    window : int, optional (default: 3)
    tol : float, optional (default: 1e-6)

    Returns
    -------
    (int, bool)
        (index, found)

    Examples
    --------
    >>> glyph_200([1,1,1,1], window=3)
    (2, True)
    """
    n = len(seq)
    if window < 1 or n == 0:
        return max(0, n-1), False
    for t in range(window-1, n):
        w = [float(seq[t-i]) for i in range(window)]
        if max(w) - min(w) <= tol:
            return t, True
    return n-1, False
