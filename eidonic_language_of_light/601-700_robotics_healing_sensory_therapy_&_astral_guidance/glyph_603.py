# glyph_603.py — FALL_PREVENTION
# -----------------------------------------------------------------------------
# ID:            603
# Pack:          Pack 007 (601–700)
# Name:          FALL_PREVENTION
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure heightmap logic
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any

def glyph_603(heightmap: Sequence[Sequence[float]], *, max_step_m: float = 0.05) -> Dict[str, Any]:
    """
    FALL_PREVENTION — mark unsafe cells based on height discontinuity.

    Overview
    --------
    Computes a binary mask of cells where the absolute height delta to any
    4-neighbor exceeds `max_step_m`. Suitable for pre-planning gating.

    Parameters
    ----------
    heightmap : List[List[float]]
    max_step_m : float, optional (default: ``0.05``)

    Returns
    -------
    {'unsafe': List[List[int]], 'count': int}
    """
    H = len(heightmap); W = len(heightmap[0]) if H else 0
    unsafe = [[0]*W for _ in range(H)]
    cnt = 0
    for r in range(H):
        for c in range(W):
            here = heightmap[r][c]
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W:
                    if abs(heightmap[nr][nc] - here) > max_step_m:
                        if unsafe[r][c] == 0:
                            unsafe[r][c] = 1; cnt += 1
                        break
    return {"unsafe": unsafe, "count": cnt}
