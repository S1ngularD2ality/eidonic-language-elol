# glyph_026.py — Flame Resonance Unfolder
# -----------------------------------------------------------------------------
# ID:            026
# Pack:          Pack 001 (000–100)
# Name:          Flame Resonance Unfolder
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_026(seq: Sequence[float], *, bins: int = 32) -> List[float]:
    """
    Flame Resonance Unfolder — coarse DFT magnitude profile (portable O(n^2)).

    Overview
    --------
    Computes a naive DFT magnitude at `bins` equally spaced frequencies in [0, π].

    Parameters
    ----------
    seq : Sequence[float]
        Real-valued samples.
    bins : int, optional (default: 32)
        Number of frequency probes.

    Returns
    -------
    List[float]
        Magnitudes per probe.

    Examples
    --------
    >>> glyph_026([0,1,0,-1]*8, bins=8)  # doctest: +ELLIPSIS
    [...]
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0 or bins < 1:
        return [0.0]*max(0,bins)
    mags: List[float] = []
    for k in range(bins):
        w = math.pi * k / (bins-1 if bins>1 else 1)
        sr = si = 0.0
        for t, v in enumerate(x):
            ang = w * t
            sr += v * math.cos(ang)
            si += v * math.sin(ang)
        mags.append((sr*sr + si*si)**0.5)
    return mags
