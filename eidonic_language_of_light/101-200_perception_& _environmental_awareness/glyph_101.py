# glyph_101.py — Soul Resonance Filter
# -----------------------------------------------------------------------------
# ID:            101
# Pack:          Pack 002 (101–200)
# Name:          Soul Resonance Filter
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_101(signal: Sequence[float], *, window: int = 5) -> List[float]:
    """
    Soul Resonance Filter — robust smoothing via median-of-means.

    Overview
    --------
    Splits an odd window into 3 contiguous chunks, averages each chunk, and takes
    the median of those three averages. Reflection padding preserves length.

    Parameters
    ----------
    signal : Sequence[float]
    window : int, optional (default: 5)
        Must be odd and >= 3.

    Returns
    -------
    List[float]
        Smoothed sequence (same length as input).

    Examples
    --------
    >>> glyph_101([0, 100, 0, 0, 0], window=5)
    [0.0, 0.0, 0.0, 0.0, 0.0]

    Exceptions
    ----------
    - ValueError : if window < 3 or window is even.

    Complexity
    ----------
    - Time  : O(n·w)
    - Space : O(n)
    """
    if window < 3 or window % 2 == 0:
        raise ValueError("window must be odd and >= 3")
    n = len(signal)
    if n == 0:
        return []
    k = window // 2
    pad = list(signal[k:0:-1]) + list(signal) + list(signal[-2:-k-2:-1]) if n > 1 else list(signal)*(2*k+1)
    thirds = [window // 3, window // 3, window - 2*(window // 3)]
    out: List[float] = [0.0]*n
    for i in range(n):
        w = [float(pad[i+j]) for j in range(window)]
        m = []
        idx = 0
        for t in thirds:
            chunk = w[idx:idx+t]; idx += t
            m.append(sum(chunk)/len(chunk))
        m.sort()
        out[i] = m[1]
    return out
