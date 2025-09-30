# glyph_635.py — ASSISTIVE_STEADY_CAM
# -----------------------------------------------------------------------------
# ID:            635
# Pack:          Pack 007 (601–700)
# Name:          ASSISTIVE_STEADY_CAM
# Class:         perception_smooth
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_635(yaw_deg: Sequence[float], *, alpha: float = 0.2) -> List[float]:
    """
    ASSISTIVE_STEADY_CAM — low-pass yaw smoothing for gentle viewing.

    Overview
    --------
    Single-pole IIR smoother (exponential moving average) over yaw samples.

    Parameters
    ----------
    yaw_deg : Sequence[float]
    alpha   : float, optional (default: ``0.2``)
        Blend factor in [0,1]; smaller = smoother.

    Returns
    -------
    List[float]
        Smoothed yaw degrees.

    Examples
    --------
    >>> out = glyph_635([0, 10, 0], alpha=0.5)
    >>> len(out) == 3 and out[0] == 0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    a = max(0.0, min(1.0, alpha))
    out: List[float] = []
    s = 0.0
    for i, y in enumerate(yaw_deg):
        s = y if i == 0 else (a*y + (1-a)*s)
        out.append(float(s))
    return out
