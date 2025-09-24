# glyph_056.py — Quantum Harmonic Decoder
# -----------------------------------------------------------------------------
# ID:            056
# Pack:          Pack 001 (000–100)
# Name:          Quantum Harmonic Decoder
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

def glyph_056(seq: Sequence[float], bins: Sequence[int]) -> List[float]:
    """
    Quantum Harmonic Decoder — Goertzel power for selected DFT bins.

    Overview
    --------
    Computes single-bin DFT power estimates for requested integer frequencies using
    the Goertzel recurrence; efficient for sparse frequency queries.

    Parameters
    ----------
    seq : Sequence[float]
        Input samples.
    bins : Sequence[int]
        Integer bin indexes (0..n-1).

    Returns
    -------
    List[float]
        Power per requested bin.

    Examples
    --------
    >>> glyph_056([1,0,-1,0]*8, bins=[2,6])  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(|bins|·n)
    - Space : O(1) per bin
    """
    x = [float(v) for v in seq]
    n = len(x)
    out: List[float] = []
    for k in bins:
        if n == 0:
            out.append(0.0)
            continue
        w = 2.0 * math.pi * k / n
        cw = 2.0 * math.cos(w)
        s0 = s1 = s2 = 0.0
        for v in x:
            s0 = v + cw * s1 - s2
            s2 = s1
            s1 = s0
        power = s1 * s1 + s2 * s2 - cw * s1 * s2
        out.append(power)
    return out
