# glyph_181.py — Soul Thread Amplifier
# -----------------------------------------------------------------------------
# ID:            181
# Pack:          Pack 002 (101–200)
# Name:          Soul Thread Amplifier
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_181(seq: Sequence[float], *, gain: float = 1.25, center: float = 0.0) -> List[float]:
    """
    Soul Thread Amplifier — saturating gain around a center.

    Overview
    --------
    Applies y = center + tanh(gain * (x - center)) to enhance signal presence
    without exploding magnitude.

    Parameters
    ----------
    seq : Sequence[float]
    gain : float, optional (default: 1.25)
    center : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Amplified sequence.

    Examples
    --------
    >>> glyph_181([-2, -1, 0, 1, 2], gain=2.0)
    [-0.9640275800758169, -0.7615941559557649, 0.0, 0.7615941559557649, 0.9640275800758169]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    import math
    g = float(gain); c = float(center)
    return [c + math.tanh(g * (float(v) - c)) for v in seq]
