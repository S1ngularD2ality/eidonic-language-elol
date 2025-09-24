# glyph_171.py — Anchor Phase Modifier
# -----------------------------------------------------------------------------
# ID:            171
# Pack:          Pack 002 (101–200)
# Name:          Anchor Phase Modifier
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

def glyph_171(seq: Sequence[float], *, period: int, shift: float) -> List[float]:
    """
    Anchor Phase Modifier — phase-shift a periodic template fit.

    Overview
    --------
    Projects onto sine/cosine with integer `period`, then reconstructs with an
    added phase shift `shift` (radians).

    Parameters
    ----------
    seq : Sequence[float]
    period : int           # >= 2
    shift  : float         # radians

    Returns
    -------
    List[float]
        Phase-shifted reconstruction.

    Examples
    --------
    >>> y = glyph_171([0,1,0,-1]*4, period=4, shift=1.57079632679)  # ~+π/2
    """
    if period < 2:
        return [float(v) for v in seq]
    n = len(seq)
    if n == 0:
        return []
    x = [float(v) for v in seq]
    w = 2.0*math.pi/period
    a = sum(x[t]*math.cos(w*t) for t in range(n)) * 2.0/n
    b = sum(x[t]*math.sin(w*t) for t in range(n)) * 2.0/n
    c = sum(x)/n
    phi = float(shift)
    return [c + a*math.cos(w*t + phi) + b*math.sin(w*t + phi) for t in range(n)]
