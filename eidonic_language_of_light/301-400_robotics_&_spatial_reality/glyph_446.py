# glyph_446.py — Timewalk Query
# -----------------------------------------------------------------------------
# ID:            446
# Pack:          Pack 005 (401–500)
# Name:          Timewalk Query
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_446(series: Sequence[Tuple[float, float]], *, window: int = 3) -> List[float]:
    """
    Timewalk Query — moving-sum over (t, value) sequences by index window.

    Overview
    --------
    Ignores timestamps; returns sums of size `window` with reflection edges.

    Parameters
    ----------
    series : Sequence[(t,value)]
    window : int, optional (default: 3) — odd recommended.

    Returns
    -------
    List[float]

    Examples
    --------
    >>> glyph_446([(0,1),(1,2),(2,3)], window=3)
    [3.0, 6.0, 5.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·w)
    - Space : O(n)
    """
    if not series:
        return []
    n = len(series)
    w = max(1, int(window))
    k = w // 2
    vals = [float(v) for _, v in series]
    if n == 1:
        return vals
    pad = vals[k:0:-1] + vals + vals[-2:-k-2:-1] if n > 1 else vals * (2*k + 1)
    out: List[float] = []
    for i in range(n):
        s = 0.0
        for j in range(w):
            s += pad[i + j]
        out.append(s)
    return out
