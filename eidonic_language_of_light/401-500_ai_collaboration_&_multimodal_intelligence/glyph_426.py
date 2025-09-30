# glyph_426.py — Gesture Read
# -----------------------------------------------------------------------------
# ID:            426
# Pack:          Pack 005 (401–500)
# Name:          Gesture Read
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

def glyph_426(traj: Sequence[float], *, thresh: float = 0.2) -> str:
    """
    Gesture Read — classify simple 1D motion.

    Overview
    --------
    Uses sum(traj) against ±threshold: 'right', 'left', or 'still'.

    Parameters
    ----------
    traj : Sequence[float]
    thresh : float, optional (default: 0.2)

    Returns
    -------
    str : one of {'left','right','still'}

    Examples
    --------
    >>> glyph_426([0.1,0.2,0.1], thresh=0.2)
    'right'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    s = sum(float(v) for v in traj)
    if s > thresh: return "right"
    if s < -thresh: return "left"
    return "still"
