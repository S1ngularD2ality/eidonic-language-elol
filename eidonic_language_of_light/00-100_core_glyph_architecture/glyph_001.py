# glyph_001.py — Harmonic Pulse Filter
# -----------------------------------------------------------------------------
# ID:            001
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Pulse Filter
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_001(signal: Sequence[float], *, window: int = 5, eps: float = 1e-12) -> List[float]:
    """
    Harmonic Pulse Filter — smooth using a harmonic-mean window (odd, centered).

    Overview
    --------
    Applies a centered odd window whose aggregate is the harmonic mean of |samples|,
    preserving edges better than arithmetic averaging and attenuating spikes.

    Parameters
    ----------
    signal : Sequence[float]
        Real-valued samples.
    window : int, optional (default: 5)
        Odd window size (>= 1). Reflection padding at edges.
    eps : float, optional (default: 1e-12)
        Numerical floor to avoid division by zero.

    Returns
    -------
    List[float]
        Smoothed sequence (same length as input).

    Examples
    --------
    >>> glyph_001([1, 100, 1, 1, 1], window=3)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    - ValueError : if `window < 1` or even.

    Complexity
    ----------
    - Time  : O(n·w)
    - Space : O(n)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >= 1")

    n = len(signal)
    if n == 0:
        return []
    k = window // 2
    pad = list(signal[k:0:-1]) + list(signal) + list(signal[-2:-k-2:-1]) if n > 1 else list(signal) * (2*k + 1)

    out: List[float] = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(window):
            v = abs(float(pad[i + j]))
            s += 1.0 / max(v, eps)
        out[i] = window / max(s, eps)
    return out
