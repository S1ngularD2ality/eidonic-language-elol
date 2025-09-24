# glyph_231.py — Mirror Harmonic Resonator
# -----------------------------------------------------------------------------
# ID:            231
# Pack:          Pack 003 (201–300)
# Name:          Mirror Harmonic Resonator
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

def glyph_231(seq: Sequence[float], *, period: int, gain: float = 1.0) -> List[float]:
    """
    Mirror Harmonic Resonator — reinforce mirror-symmetric sinusoid.

    Overview
    --------
    Projects onto cos(2πt/period) (even component) and amplifies by `gain`.

    Parameters
    ----------
    seq : Sequence[float]
    period : int
    gain : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Resonated signal.
    """
    if period < 2: return [float(v) for v in seq]
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return []
    w = 2.0*math.pi/period
    a = sum(x[t]*math.cos(w*t) for t in range(n))*2.0/n
    c = sum(x)/n
    g = float(gain)
    return [c + g*a*math.cos(w*t) for t in range(n)]
