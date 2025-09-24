# glyph_298.py — Harmonic Phase Amplifier
# -----------------------------------------------------------------------------
# ID:            298
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Phase Amplifier
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_298(seq: Sequence[float], *, period: int, gain: float = 1.0, phase: float = 0.0) -> List[float]:
    """
    Harmonic Phase Amplifier — amplify cosine mode with phase.

    Overview
    --------
    Projects onto cos/sin basis for `period`, re-synthesizes with `gain` and `phase`.

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    gain : float, optional (default: 1.0)
    phase : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Amplified reconstruction.

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if period < 2: return [float(v) for v in seq]
    x=[float(v) for v in seq]; n=len(x)
    if n==0: return []
    w=2.0*math.pi/period
    a=sum(x[t]*math.cos(w*t) for t in range(n))*2.0/n
    b=sum(x[t]*math.sin(w*t) for t in range(n))*2.0/n
    c=sum(x)/n
    g=float(gain); ph=float(phase)
    return [c + g*(a*math.cos(w*t+ph) + b*math.sin(w*t+ph)) for t in range(n)]
