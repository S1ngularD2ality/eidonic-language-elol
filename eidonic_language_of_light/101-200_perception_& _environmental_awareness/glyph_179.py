# glyph_179.py — Spiral Key Channeler
# -----------------------------------------------------------------------------
# ID:            179
# Pack:          Pack 002 (101–200)
# Name:          Spiral Key Channeler
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple

def glyph_179(n: int, *, channels: int) -> List[List[Tuple[int, int]]]:
    """
    Spiral Key Channeler — bucket spiral coordinates into channels.

    Overview
    --------
    Generates an n×n center-out spiral coordinate path and routes each (y,x) into
    channel (index mod channels).

    Parameters
    ----------
    n : int
    channels : int

    Returns
    -------
    List[List[Tuple[int,int]]]
        Buckets of coordinates.

    Examples
    --------
    >>> buckets = glyph_179(2, channels=2)
    >>> sum(len(b) for b in buckets) == 4
    True
    """
    if n < 1 or channels < 1:
        return []
    c = n//2; y=x=c
    path=[(y,x)]
    step=1
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    while len(path) < n*n:
        for dyi,dxi in dirs:
            for _ in range(step):
                if len(path) >= n*n: break
                y+=dyi; x+=dxi
                if 0<=y<n and 0<=x<n: path.append((y,x))
            if (dyi,dxi) in (dirs[1], dirs[3]): step+=1
    out=[[] for _ in range(channels)]
    for i, coord in enumerate(path):
        out[i % channels].append(coord)
    return out
