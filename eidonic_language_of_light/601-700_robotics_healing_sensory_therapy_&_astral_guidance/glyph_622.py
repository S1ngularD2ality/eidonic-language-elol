# glyph_622.py — PROTECTIVE_BARRIER_DEPLOY
# -----------------------------------------------------------------------------
# ID:            622
# Pack:          Pack 007 (601–700)
# Name:          PROTECTIVE_BARRIER_DEPLOY
# Class:         safety_planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple, Dict

def glyph_622(area_size_m: Tuple[float, float], barrier_span_m: float,
              *, offset: Tuple[float, float] = (0.0, 0.0)) -> Dict[str, List[Tuple[float, float]]]:
    """
    PROTECTIVE_BARRIER_DEPLOY — compute lattice points to place soft barriers.

    Overview
    --------
    Tiling planner that returns a deterministic set of post positions across a rectangle.

    Parameters
    ----------
    area_size_m : (float, float)
        (width, height) of the region (meters).
    barrier_span_m : float
        Spacing between barrier posts (meters).
    offset : (float, float), optional (default: ``(0.0, 0.0)``)
        Origin shift for the lattice.

    Returns
    -------
    Dict[str, List[Tuple[float, float]]]
        {'positions': [(x, y), ...]}

    Examples
    --------
    >>> pts = glyph_622((2.1, 1.1), 1.0)['positions']
    >>> len(pts) >= 4
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O((W/s)·(H/s))
    - Space : O((W/s)·(H/s))
    """
    W, H = max(0.0, area_size_m[0]), max(0.0, area_size_m[1])
    s = max(0.1, barrier_span_m)
    x0, y0 = offset
    nx = int(W // s) + 1
    ny = int(H // s) + 1
    return {"positions": [(x0 + i*s, y0 + j*s) for i in range(nx+1) for j in range(ny+1)]}
