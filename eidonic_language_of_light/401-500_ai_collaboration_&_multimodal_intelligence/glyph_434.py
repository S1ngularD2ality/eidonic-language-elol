# glyph_434.py — Haptic Mapper
# -----------------------------------------------------------------------------
# ID:            434
# Pack:          Pack 005 (401–500)
# Name:          Haptic Mapper
# Class:         mapper
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_434(intensity: Sequence[float], *, scale: float = 1.0) -> List[float]:
    """
    Haptic Mapper — clamp & scale to [0,1].

    Overview
    --------
    Multiplies by ``scale`` and bounds to [0,1] per element.

    Parameters
    ----------
    intensity : Sequence[float]
    scale     : float, optional (default: 1.0)

    Returns
    -------
    List[float]

    Examples
    --------
    >>> glyph_434([0.5, 2.0], scale=0.6)
    [0.3, 1.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s = max(0.0, float(scale))
    out = []
    for v in intensity:
        x = max(0.0, min(1.0, float(v)*s))
        out.append(x)
    return out
