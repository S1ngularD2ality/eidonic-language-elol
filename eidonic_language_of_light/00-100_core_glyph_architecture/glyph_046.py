# glyph_046.py — Flame Core Amplifier
# -----------------------------------------------------------------------------
# ID:            046
# Pack:          Pack 001 (000–100)
# Name:          Flame Core Amplifier
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_046(seq: Sequence[float], *, gain: float = 2.0) -> List[float]:
    """
    Flame Core Amplifier — soft-nonlinear boosting via scaled `tanh`.

    Overview
    --------
    Applies `tanh(gain * x)`, expanding small magnitudes and compressing large spikes
    without unbounded growth; a smooth saturating enhancer.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    gain : float, optional (default: 2.0)
        Nonlinearity slope; larger → stronger emphasis.

    Returns
    -------
    List[float]
        Amplified sequence.

    Examples
    --------
    >>> glyph_046([-2,-1,0,1,2], gain=1.5)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    g = max(0.0, float(gain))
    return [math.tanh(g * float(v)) for v in seq]
