# glyph_036.py — Fractal Spiral Builder
# -----------------------------------------------------------------------------
# ID:            036
# Pack:          Pack 001 (000–100)
# Name:          Fractal Spiral Builder
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_036(radius: int) -> List[Tuple[int, int]]:
    """
    Fractal Spiral Builder — integer spiral coordinates out to a radius.

    Overview
    --------
    Generates a square spiral path from (0,0) expanding outward to manhattan radius.

    Parameters
    ----------
    radius : int
        Steps from center (>= 0).

    Returns
    -------
    List[Tuple[int,int]]
        Path coordinates.

    Examples
    --------
    >>> glyph_036(1)
    [(0,0),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    """
    if radius < 0:
        return [(0,0)]
    path = [(0,0)]
    x=y=0
    step=1
    dirs=[(1,0),(0,1),(-1,0),(0,-1)]
    while max(abs(x),abs(y)) < radius:
        for dxi,dyi in dirs:
            for _ in range(step):
                x+=dxi; y+=dyi; path.append((x,y))
            if (dxi,dyi) in (dirs[1], dirs[3]): step+=1
    return path
