# glyph_076.py — Flame Frequency Unwrapper
# -----------------------------------------------------------------------------
# ID:            076
# Pack:          Pack 001 (000–100)
# Name:          Flame Frequency Unwrapper
# Class:         analyzer
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

def glyph_076(seq: Sequence[float]) -> List[float]:
    """
    Flame Frequency Unwrapper — unwrap instantaneous phase from analytic signal (naive Hilbert).

    Overview
    --------
    Approximates an analytic signal via quadrature (90° shift by simple FIR), then
    returns the unwrapped arctangent phase.

    Parameters
    ----------
    seq : Sequence[float]
        Real input.

    Returns
    -------
    List[float]
        Unwrapped phase (radians).

    Examples
    --------
    >>> glyph_076([0,1,0,-1]*4)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return []
    # crude quadrature via 1-sample delay difference
    y = [0.0]*n
    for i in range(1, n):
        y[i] = x[i] - x[i-1]
    phase = [0.0]*n
    for i in range(n):
        phase[i] = math.atan2(y[i], x[i])
    # unwrap
    out = [phase[0]]
    for i in range(1, n):
        p = phase[i]
        dp = p - phase[i-1]
        while dp > math.pi:  dp -= 2*math.pi
        while dp < -math.pi: dp += 2*math.pi
        out.append(out[-1] + dp)
    return out
