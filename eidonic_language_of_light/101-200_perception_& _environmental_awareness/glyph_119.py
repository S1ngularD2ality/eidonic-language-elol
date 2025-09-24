# glyph_119.py — Harmonic Key Condenser
# -----------------------------------------------------------------------------
# ID:            119
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Key Condenser
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List, Tuple

def glyph_119(seq: Sequence[float], *, topk: int = 3) -> List[Tuple[int, float]]:
    """
    Harmonic Key Condenser — pick top-k DFT magnitudes (naive O(n^2)).

    Overview
    --------
    Computes complex DFT; returns [(k, |X_k|)] sorted by magnitude desc.

    Parameters
    ----------
    seq : Sequence[float]
    topk : int, optional (default: 3)

    Returns
    -------
    List[Tuple[int,float]]
        Top frequency bins.

    Examples
    --------
    >>> glyph_119([0,1,0,-1]*4, topk=2)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n^2)
    - Space : O(n)
    """
    n = len(seq)
    if n == 0:
        return []
    X = []
    for k in range(n):
        sr = si = 0.0
        for t, v in enumerate(seq):
            ang = -2.0*math.pi*k*t/n
            sr += float(v)*math.cos(ang)
            si += float(v)*math.sin(ang)
        X.append((k, (sr*sr + si*si)**0.5))
    X.sort(key=lambda kv: -kv[1])
    return X[:max(0, int(topk))]
