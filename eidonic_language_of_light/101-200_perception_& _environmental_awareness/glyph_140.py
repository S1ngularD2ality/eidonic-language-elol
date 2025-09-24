# glyph_140.py — Harmonic Frequency Dilator
# -----------------------------------------------------------------------------
# ID:            140
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Frequency Dilator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_140(seq: Sequence[float], *, stretch: float = 1.5) -> List[float]:
    """
    Harmonic Frequency Dilator — resample via phase stretching (naive).

    Overview
    --------
    Treat indices as phase; y[i] = x[floor(i/stretch)] with clamp to last sample.

    Parameters
    ----------
    seq : Sequence[float]
    stretch : float, optional (default: 1.5)

    Returns
    -------
    List[float]
        Dilated series (length equals input).

    Examples
    --------
    >>> glyph_140([0,1,0,1], stretch=2.0)
    [0.0, 0.0, 1.0, 0.0]
    """
    if not seq:
        return []
    s = max(1e-9, float(stretch))
    x = [float(v) for v in seq]
    n = len(x)
    out = []
    for i in range(n):
        j = int(i / s)
        if j >= n: j = n-1
        out.append(x[j])
    return out
