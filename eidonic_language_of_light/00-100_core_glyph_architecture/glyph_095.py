# glyph_095.py — Spiral Memory Injector
# -----------------------------------------------------------------------------
# ID:            095
# Pack:          Pack 001 (000–100)
# Name:          Spiral Memory Injector
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

def glyph_095(seq: Sequence[float], *, ratio: float = 0.5) -> List[float]:
    """
    Spiral Memory Injector — progressive echo inward from both ends.

    Overview
    --------
    Adds a decaying contribution from mirrored positions: 
    `y[i] = x[i] + r*x[n-1-i] + r^2*x[i] + ...` truncated at r^k < 1e-6.

    Parameters
    ----------
    seq : Sequence[float]
    ratio : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Injected sequence.
    """
    r = max(0.0, min(0.999, float(ratio)))
    x = [float(v) for v in seq]
    n = len(x)
    y = x[:]
    amp = r
    while amp > 1e-6:
        for i in range(n):
            y[i] += amp * x[n-1-i]
        amp *= r
    return y
