# glyph_049.py — Fractal Cycle Extender
# -----------------------------------------------------------------------------
# ID:            049
# Pack:          Pack 001 (000–100)
# Name:          Fractal Cycle Extender
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_049(cycle: Sequence[float], *, length: int, decay: float = 0.5) -> List[float]:
    """
    Fractal Cycle Extender — extend a base cycle with decaying overtone tiling.

    Overview
    --------
    Tiles `cycle` to `length` as the fundamental, then repeatedly adds the doubled-rate
    cycle scaled by `decay`, `decay^2`, ... until negligible.

    Parameters
    ----------
    cycle : Sequence[float]
        Base periodic motif (non-empty recommended).
    length : int
        Output length (>= 0).
    decay : float, optional (default: 0.5)
        Overtone amplitude multiplier in (0,1].

    Returns
    -------
    List[float]
        Extended sequence.

    Examples
    --------
    >>> glyph_049([1, -1], length=6, decay=0.5)
    # fundamental: [1,-1,1,-1,1,-1]; + overtones at 2× rate

    Exceptions
    ----------
    - ValueError : if `length < 0`.

    Complexity
    ----------
    - Time  : O(length * log_{1/decay}(ε))
    - Space : O(length)
    """
    if length < 0:
        raise ValueError("length must be >= 0")
    if not cycle:
        return [0.0] * length
    base = [float(v) for v in cycle]
    out = [0.0] * length
    # fundamental
    for i in range(length):
        out[i] += base[i % len(base)]
    # overtones
    amp = float(decay)
    while amp > 1e-6:
        for i in range(length):
            out[i] += amp * base[(2 * i) % len(base)]
        amp *= decay
    return out
