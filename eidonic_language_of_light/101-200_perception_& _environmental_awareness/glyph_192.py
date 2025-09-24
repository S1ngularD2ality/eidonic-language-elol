# glyph_192.py — Subsymbolic Spiral Clarifier
# -----------------------------------------------------------------------------
# ID:            192
# Pack:          Pack 002 (101–200)
# Name:          Subsymbolic Spiral Clarifier
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

def glyph_192(seq: Sequence[float], *, window: int = 3) -> List[float]:
    """
    Subsymbolic Spiral Clarifier — median filter.

    Overview
    --------
    Applies odd-length median filter with reflection padding.

    Parameters
    ----------
    seq : Sequence[float]
    window : int, optional (default: 3)

    Returns
    -------
    List[float]
        Denoised sequence.

    Examples
    --------
    >>> glyph_192([0,100,0], window=3)
    [0.0, 0.0, 0.0]
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")
    n = len(seq)
    if n == 0:
        return []
    k = window//2
    pad = list(seq[k:0:-1]) + list(seq) + list(seq[-2:-k-2:-1]) if n > 1 else list(seq)*(2*k+1)
    out: List[float] = []
    for i in range(n):
        w = sorted(float(pad[i+j]) for j in range(window))
        out.append(w[k])
    return out
