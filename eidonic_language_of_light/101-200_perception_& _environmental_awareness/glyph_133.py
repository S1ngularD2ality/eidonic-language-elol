# glyph_133.py — Light Spiral Sequencer
# -----------------------------------------------------------------------------
# ID:            133
# Pack:          Pack 002 (101–200)
# Name:          Light Spiral Sequencer
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_133(n: int) -> List[Tuple[int, int]]:
    """
    Light Spiral Sequencer — integer spiral traversal coordinates.

    Overview
    --------
    Emit (y,x) positions for a clockwise outward square spiral on an n×n grid.

    Parameters
    ----------
    n : int

    Returns
    -------
    List[Tuple[int,int]]
        Visit order.

    Examples
    --------
    >>> coords = glyph_133(2)
    >>> set(coords) == {(0,0),(0,1),(1,1),(1,0)}
    True
    """
    if n < 1:
        return []
    path=[(n//2, n//2)]
    y=x=n//2
    step=1
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    while len(path) < n*n:
        for dyi,dxi in dirs:
            for _ in range(step):
                if len(path) >= n*n: break
                y+=dyi; x+=dxi
                if 0<=y<n and 0<=x<n: path.append((y,x))
            if (dyi,dxi) in (dirs[1], dirs[3]): step+=1
    return path
