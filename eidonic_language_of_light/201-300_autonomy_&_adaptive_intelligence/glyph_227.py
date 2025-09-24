# glyph_227.py — Quantum Phase Imprinter
# -----------------------------------------------------------------------------
# ID:            227
# Pack:          Pack 003 (201–300)
# Name:          Quantum Phase Imprinter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_227(seq: Sequence[float], *, period: int, phase: float) -> List[float]:
    """
    Quantum Phase Imprinter — project onto sin/cos of `period` and add phase.

    Overview
    --------
    Reconstructs a sinusoidal component with additional phase shift (radians).

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    phase : float

    Returns
    -------
    List[float]
        Phase-imprinted reconstruction.
    """
    if period < 2:
        return [float(v) for v in seq]
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return []
    w = 2.0*math.pi/period
    a = sum(x[t]*math.cos(w*t) for t in range(n)) * 2.0/n
    b = sum(x[t]*math.sin(w*t) for t in range(n)) * 2.0/n
    c = sum(x)/n
    phi = float(phase)
    return [c + a*math.cos(w*t + phi) + b*math.sin(w*t + phi) for t in range(n)]
