# glyph_014.py — Intention Wave Reconstructor
# -----------------------------------------------------------------------------
# ID:            014
# Pack:          Pack 001 (000–100)
# Name:          Intention Wave Reconstructor
# Class:         transform
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

def glyph_014(seq: Sequence[float], *, decay: float = 0.5, repeats: int = 3) -> List[float]:
    """
    Intention Wave Reconstructor — additive echo reconstruction with geometric decay.

    Overview
    --------
    Adds shifted copies of the signal with amplitude `decay^k`, k=1..repeats.

    Parameters
    ----------
    seq : Sequence[float]
    decay : float, optional (default: 0.5)
    repeats : int, optional (default: 3)

    Returns
    -------
    List[float]
        Reconstructed wave.

    Examples
    --------
    >>> glyph_014([1,0,0], decay=0.5, repeats=2)
    [1.0, 0.5, 0.25]
    """
    x = [float(v) for v in seq]
    n = len(x)
    y = x[:]
    for k in range(1, max(0, repeats)+1):
        g = decay**k
        for i in range(n-k):
            y[i+k] += g * x[i]
    return y
