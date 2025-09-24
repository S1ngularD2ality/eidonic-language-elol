# glyph_286.py — Light Gate Harmonizer
# -----------------------------------------------------------------------------
# ID:            286
# Pack:          Pack 003 (201–300)
# Name:          Light Gate Harmonizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_286(seq: Sequence[float], *, window: int = 3) -> List[float]:
    """
    Light Gate Harmonizer — median filter with reflection padding.

    Overview
    --------
    Robust to impulsive outliers; preserves edges.

    Parameters
    ----------
    seq : Sequence[float]
    window : int, optional (default: 3, must be odd)

    Returns
    -------
    List[float]
        Harmonized sequence.

    Exceptions
    ----------
    - ValueError : if `window` not odd or < 1.

    Complexity
    ----------
    - Time  : O(window·n)
    - Space : O(n)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >=1")
    n = len(seq)
    if n == 0: return []
    k = window//2
    pad = list(seq[k:0:-1]) + list(seq) + list(seq[-2:-k-2:-1]) if n > 1 else list(seq)*(2*k+1)
    out=[]
    for i in range(n):
        w = sorted(float(pad[i+j]) for j in range(window))
        out.append(w[len(w)//2])
    return out
