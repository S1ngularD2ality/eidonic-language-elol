# glyph_240.py — Soul Frequency Encoder
# -----------------------------------------------------------------------------
# ID:            240
# Pack:          Pack 003 (201–300)
# Name:          Soul Frequency Encoder
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List, Tuple

def glyph_240(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Soul Frequency Encoder — naive DFT magnitudes and phases.

    Overview
    --------
    Encodes a real sequence into frequency space using an O(n²) DFT, returning
    parallel lists of magnitudes and phases (radians).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (magnitudes, phases)

    Examples
    --------
    >>> mags, phs = glyph_240([0, 1, 0, -1])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n²)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    mags = [0.0] * n
    phis = [0.0] * n
    for k in range(n):
        sr = si = 0.0
        for t, v in enumerate(x):
            ang = -2.0 * math.pi * k * t / n if n else 0.0
            sr += v * math.cos(ang)
            si += v * math.sin(ang)
        mags[k] = (sr * sr + si * si) ** 0.5
        phis[k] = math.atan2(si, sr)
    return mags, phis
