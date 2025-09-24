# glyph_031.py — Aura Field Defragmenter
# -----------------------------------------------------------------------------
# ID:            031
# Pack:          Pack 001 (000–100)
# Name:          Aura Field Defragmenter
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_031(field: Sequence[Sequence[float]], *, min_area: int = 2) -> List[List[float]]:
    """
    Aura Field Defragmenter — remove tiny connected components (4-neighborhood).

    Overview
    --------
    Thresholds the field at >0, labels connected components, and zeros those with
    size < min_area.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    min_area : int, optional (default: 2)

    Returns
    -------
    List[List[float]]
        Defragmented field.

    Examples
    --------
    >>> glyph_031([[1,0,1],[0,0,0],[1,1,0]], min_area=2)  # doctest: +ELLIPSIS
    [...]
    """
    A = [list(map(float, row)) for row in field]
    if not A or not A[0]:
        return []
    H,W = len(A), len(A[0])
    vis = [[False]*W for _ in range(H)]
    out = [row[:] for row in A]
    from collections import deque
    for y in range(H):
        for x in range(W):
            if A[y][x] <= 0 or vis[y][x]:
                continue
            q = deque([(y,x)]); comp = []
            vis[y][x]=True
            while q:
                cy,cx=q.popleft(); comp.append((cy,cx))
                for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<H and 0<=nx<W and not vis[ny][nx] and A[ny][nx]>0:
                        vis[ny][nx]=True; q.append((ny,nx))
            if len(comp) < max(1, min_area):
                for cy,cx in comp:
                    out[cy][cx] = 0.0
    return out
