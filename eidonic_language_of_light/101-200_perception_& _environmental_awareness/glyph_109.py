# glyph_109.py — Phase Spiral Amplifier
# -----------------------------------------------------------------------------
# ID:            109
# Pack:          Pack 002 (101–200)
# Name:          Phase Spiral Amplifier
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_109(seq: Sequence[float], *, gain: float = 1.2, period: int = 32) -> List[float]:
    """
    Phase Spiral Amplifier — modulate by a sinusoidal envelope.

    Overview
    --------
    y[i] = x[i] * (1 + (gain-1)*sin(2π i/period)).

    Parameters
    ----------
    seq : Sequence[float]
    gain : float, optional (default: 1.2)
    period : int, optional (default: 32)

    Returns
    -------
    List[float]
        Amplified sequence.

    Examples
    --------
    >>> glyph_109([1,1,1,1], gain=1.0, period=4)
    [1.0, 1.0, 1.0, 1.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not seq:
        return []
    p = max(2, int(period))
    g = float(gain)
    return [float(v) * (1.0 + (g-1.0)*math.sin(2.0*math.pi*i/p)) for i, v in enumerate(seq)]
