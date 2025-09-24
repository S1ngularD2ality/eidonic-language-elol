# glyph_003.py — Subconscious Phase Splitter
# -----------------------------------------------------------------------------
# ID:            003
# Pack:          Pack 001 (000–100)
# Name:          Subconscious Phase Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_003(signal: Sequence[float], *, trend_window: int = 9) -> Tuple[List[float], List[float]]:
    """
    Subconscious Phase Splitter — decompose a sequence into trend and texture.

    Overview
    --------
    Trend via centered moving average (odd window); texture is residual.

    Parameters
    ----------
    signal : Sequence[float]
        Real-valued input.
    trend_window : int, optional (default: 9)
        Odd window length (>= 1).

    Returns
    -------
    (List[float], List[float])
        (trend, texture)

    Examples
    --------
    >>> t, x = glyph_003([0,1,0,1,0], trend_window=3)
    >>> len(t), len(x)
    (5, 5)
    """
    if trend_window < 1 or trend_window % 2 == 0:
        raise ValueError("trend_window must be odd and >= 1")
    n = len(signal)
    if n == 0:
        return [], []
    k = trend_window // 2
    pad = list(signal[k:0:-1]) + list(signal) + list(signal[-2:-k-2:-1]) if n > 1 else list(signal) * (2*k + 1)
    trend = [sum(float(pad[i+j]) for j in range(trend_window)) / trend_window for i in range(n)]
    texture = [float(signal[i]) - trend[i] for i in range(n)]
    return trend, texture
