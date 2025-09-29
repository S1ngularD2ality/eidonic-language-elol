# glyph_435.py — Tactile Echo
# -----------------------------------------------------------------------------
# ID:            435
# Pack:          Pack 005 (401–500)
# Name:          Tactile Echo
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence
import math

def glyph_435(pressures: Sequence[float]) -> float:
    """
    Tactile Echo — estimate decay rate from a pressure trail.

    Overview
    --------
    Uses log(last/first) / (N-1) over positive samples as a crude exponential rate.

    Parameters
    ----------
    pressures : Sequence[float]

    Returns
    -------
    float : decay rate per step (0.0 if insufficient data)

    Examples
    --------
    >>> round(glyph_435([1.0, 0.5, 0.25]), 3)
    -0.347

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    pts = [float(v) for v in pressures if float(v) > 0.0]
    if len(pts) < 2:
        return 0.0
    return math.log(pts[-1] / pts[0]) / max(1.0, len(pts)-1)
