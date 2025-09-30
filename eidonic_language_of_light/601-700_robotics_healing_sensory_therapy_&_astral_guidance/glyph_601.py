# glyph_601.py — SAFE_NAV_PROTOCOL
# -----------------------------------------------------------------------------
# ID:            601
# Pack:          Pack 007 (601–700)
# Name:          SAFE_NAV_PROTOCOL
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure planner; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Tuple, Sequence, Dict, Any
import math

Grid = Sequence[Sequence[int]]

def glyph_601(grid: Grid, start: Tuple[int, int], goal: Tuple[int, int],
              *, min_clearance: int = 1) -> Dict[str, Any]:
    """
    SAFE_NAV_PROTOCOL — uniform-cost path with human-safe clearances.

    Overview
    --------
    Plans a collision-free path on a 2D occupancy grid using uniform-cost search
    (4-neighborhood) while enforcing a Manhattan clearance radius around obstacles.
    Pure planner: no sensors, no device I/O.

    Parameters
    ----------
    grid : List[List[int]]
        0 = free, 1 = obstacle.
    start, goal : (int,int)
        Grid coordinates (row, col).
    min_clearance : int, optional (default: ``1``)
        Minimum taxicab distance from any obstacle for traversable cells.

    Returns
    -------
    Dict[str,Any]
        {'path': List[(r,c)], 'cost': float, 'expanded': int}

    Examples
    --------
    >>> g = [[0,0,0],
    ...      [1,1,0],
    ...      [0,0,0]]
    >>> out = glyph_601(g, (0,0), (2,2), min_clearance=1)
    >>> isinstance(out['path'], list)
    True

    Exceptions
    ----------
    - ValueError : invalid coordinates or grid.
    - RuntimeError: no safe path exists.

    Complexity
    ----------
    - Time  : O(R·C·log(RC)) with binary frontier
    - Space : O(R·C)
    """
    R = len(grid)
    C = len(grid[0]) if R else 0
    if R == 0 or C == 0:
        raise ValueError("grid must be non-empty")
    sr, sc = start; gr, gc = goal
    if not (0 <= sr < R and 0 <= sc < C and 0 <= gr < R and 0 <= gc < C):
        raise ValueError("start/goal out of bounds")

    # Precompute clearance map (Manhattan)
    obst = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 1]
    def clear(r, c) -> bool:
        if grid[r][c] == 1: return False
        if min_clearance <= 0: return True
        for (or_, oc_) in obst:
            if abs(or_ - r) + abs(oc_ - c) <= min_clearance:
                return False
        return True

    if not clear(sr, sc) or not clear(gr, gc):
        raise RuntimeError("start or goal violates clearance")

    # Dijkstra / uniform-cost with 4-neighborhood
    from heapq import heappush, heappop
    dist = {(sr, sc): 0.0}
    prev: Dict[Tuple[int,int], Tuple[int,int]] = {}
    pq = [(0.0, (sr, sc))]
    seen = set()
    expanded = 0

    def nbrs(r, c):
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and clear(nr, nc):
                yield (nr, nc)

    while pq:
        d, u = heappop(pq)
        if u in seen: continue
        seen.add(u); expanded += 1
        if u == (gr, gc): break
        for v in nbrs(*u):
            nd = d + 1.0
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                prev[v] = u
                heappush(pq, (nd, v))

    if (gr, gc) not in dist:
        raise RuntimeError("no safe path found")

    # Reconstruct path
    path = []
    cur = (gr, gc)
    while cur != (sr, sc):
        path.append(cur)
        cur = prev[cur]
    path.append((sr, sc))
    path.reverse()
    return {"path": path, "cost": float(dist[(gr, gc)]), "expanded": expanded}
