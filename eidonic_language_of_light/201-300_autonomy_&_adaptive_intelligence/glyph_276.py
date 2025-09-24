# glyph_276.py — Harmonic Memory Splitter
# -----------------------------------------------------------------------------
# ID:            276
# Pack:          Pack 003 (201–300)
# Original Name: Harmonic Memory Splitter
# Manifest Name: Harmonic Memory Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Tuple

def glyph_276(seq: list[float], *, window: int = 5) -> Tuple[list[float], list[float]]:
    """
    Harmonic Memory Splitter — trend/texture decomposition via moving average.

    Overview
    --------
    Trend = mean filter; Texture = residual.

    Parameters
    ----------
    seq : list[float]
    window : int, optional (default: 5)

    Returns
    -------
    (list[float], list[float])
        (trend, texture)

    Examples
    --------
    >>> trend, texture = glyph_276([0, 1, 0, 1, 0], window=3)
    >>> len(trend) == len(texture) == 5
    True

    Exceptions
    ----------
    - ValueError : if `window` is not odd or < 1.

    Complexity
    ----------
    - Time  : O(window·n)
    - Space : O(n)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >=1")
    n = len(seq)
    if n == 0: 
        return [], []
    k = window // 2
    pad = seq[k:0:-1] + seq + seq[-2:-k-2:-1] if n > 1 else seq * (2*k + 1)
    trend = [sum(float(pad[i+j]) for j in range(window)) / window for i in range(n)]
    texture = [float(seq[i]) - trend[i] for i in range(n)]
    return trend, texture
