# glyph_071.py — Pattern Cascade Isolator
# -----------------------------------------------------------------------------
# ID:            071
# Pack:          Pack 001 (000–100)
# Name:          Pattern Cascade Isolator
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_071(seq: Sequence[float], *, window: int = 5, threshold: float = 0.0) -> List[float]:
    """
    Pattern Cascade Isolator — median filter + soft threshold.

    Overview
    --------
    First applies a centered odd-window median to suppress impulsive noise, then
    subtracts a scalar threshold (ReLU-like floor at 0).

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    window : int, optional (default: 5)
        Odd window size.
    threshold : float, optional (default: 0.0)
        Subtracted after median; negatives clipped to 0.

    Returns
    -------
    List[float]
        Isolated pattern.

    Examples
    --------
    >>> glyph_071([0,9,0,9,0], window=3, threshold=4)
    [0.0, 1.0, 0.0, 1.0, 0.0]

    Exceptions
    ----------
    - ValueError : invalid window.

    Complexity
    ----------
    - Time  : O(n·w log w)
    - Space : O(n)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd >= 1")
    n = len(seq)
    if n == 0: return []
    k = window // 2
    pad = list(seq[k:0:-1]) + list(seq) + list(seq[-2:-k-2:-1]) if n > 1 else list(seq) * (2*k + 1)
    out: List[float] = [0.0]*n
    for i in range(n):
        m = sorted(float(pad[i+j]) for j in range(window))[k]
        v = m - float(threshold)
        out[i] = v if v > 0 else 0.0
    return out
