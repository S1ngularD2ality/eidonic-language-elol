# glyph_262.py — Phase Gate Unwrapper
# -----------------------------------------------------------------------------
# ID:            262
# Pack:          Pack 003 (201–300)
# Original Name: Phase Gate Unwrapper
# Manifest Name: Phase Gate Unwrapper
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List
import math

def glyph_262(phases: Sequence[float], *, period: float = 2*math.pi) -> List[float]:
    """
    Phase Gate Unwrapper — unwrap wrapped phases into a continuous track.

    Overview
    --------
    Removes ±period jumps to produce a smooth, monotonically evolving phase.

    Parameters
    ----------
    phases : Sequence[float]
    period : float, optional (default: 2π)

    Returns
    -------
    List[float]
        Unwrapped phase.

    Examples
    --------
    >>> out = glyph_262([0.0, 3.2, -3.0, 3.3])  # doctest: +ELLIPSIS
    >>> len(out)
    4

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    p = float(period)
    if not phases:
        return []
    out = [float(phases[0])]
    for v in phases[1:]:
        x = float(v)
        delta = x - out[-1]
        delta -= p * math.floor(delta / p + 0.5)  # map to [-p/2, p/2)
        out.append(out[-1] + delta)
    return out
