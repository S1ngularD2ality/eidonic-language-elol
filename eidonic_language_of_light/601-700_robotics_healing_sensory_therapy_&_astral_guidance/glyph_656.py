# glyph_656.py — PATH_REDUNDANCY_CHECK
# -----------------------------------------------------------------------------
# ID:            656
# Pack:          Pack 007 (601–700)
# Name:          PATH_REDUNDANCY_CHECK
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # geometry-only comparison
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any

def glyph_656(path_a: Sequence[Tuple[float, float]],
              path_b: Sequence[Tuple[float, float]], *,
              tol_m: float = 0.3) -> Dict[str, Any]:
    """
    PATH_REDUNDANCY_CHECK — ensure fallback path is meaningfully distinct.

    Overview
    --------
    Computes fraction of points in A within `tol_m` of any point in B.
    If overlap_ratio > 0.8, the redundancy is considered insufficient.

    Parameters
    ----------
    path_a, path_b : Sequence[(x, y)]
    tol_m : float, optional (default: ``0.3``)

    Returns
    -------
    {'overlap_ratio': float, 'sufficient': bool}

    Examples
    --------
    >>> glyph_656([(0,0),(1,0)], [(0,0.1),(1,0.1)])['sufficient']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(N·M)
    - Space : O(1)
    """
    import math
    if not path_a:
        return {"overlap_ratio": 0.0, "sufficient": True}
    cnt = 0
    for ax, ay in path_a:
        close = any(math.hypot(ax - bx, ay - by) <= tol_m for bx, by in path_b)
        if close:
            cnt += 1
    ratio = cnt / len(path_a)
    return {"overlap_ratio": float(ratio), "sufficient": ratio <= 0.8}
