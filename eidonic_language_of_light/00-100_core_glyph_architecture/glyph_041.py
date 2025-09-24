# glyph_041.py — Light Pulse Distributor
# -----------------------------------------------------------------------------
# ID:            041
# Pack:          Pack 001 (000–100)
# Name:          Light Pulse Distributor
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Sequence, List

def glyph_041(pulses: Sequence[float], *, bins: int, spread: int = 0) -> List[float]:
    """
    Light Pulse Distributor — accumulate pulse energy into modular bins, with optional spread.

    Overview
    --------
    Routes each input `pulses[i]` into bin `(i mod bins)`. With `spread>0`, energy is
    distributed across neighboring bins using a symmetric triangular kernel—useful for
    soft routing and anti-aliasing in modular time/frequency spaces.

    Parameters
    ----------
    pulses : Sequence[float]
        Non-negative magnitudes (not enforced; negatives pass through).
    bins : int
        Number of output bins (>= 1).
    spread : int, optional (default: 0)
        Half-width of triangular kernel. 0 → exact bin, 1 → distribute to neighbors, etc.

    Returns
    -------
    List[float]
        Length `bins` energy per bin.

    Examples
    --------
    >>> glyph_041([1, 2, 3, 4], bins=2)
    [1+3, 2+4]
    >>> glyph_041([1, 0, 0, 0], bins=4, spread=1)
    # distributes 1.0 into bins [3,0,1] with weights 1:2:1 normalized

    Exceptions
    ----------
    - ValueError : if `bins < 1` or `spread < 0`.

    Complexity
    ----------
    - Time  : O(len(pulses) * (2*spread+1))
    - Space : O(bins)
    """
    if bins < 1:
        raise ValueError("bins must be >= 1")
    if spread < 0:
        raise ValueError("spread must be >= 0")

    out = [0.0] * bins
    if spread == 0:
        for i, p in enumerate(pulses):
            out[i % bins] += float(p)
        return out

    weights = [spread + 1 - abs(k) for k in range(-spread, spread + 1)]
    wsum = float(sum(weights)) or 1.0
    for i, p in enumerate(pulses):
        p = float(p)
        c = i % bins
        for off, w in zip(range(-spread, spread + 1), weights):
            out[(c + off) % bins] += p * (w / wsum)
    return out
