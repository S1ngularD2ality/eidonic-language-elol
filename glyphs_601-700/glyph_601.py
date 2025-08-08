# glyph_601 – SAFE_NAV_2D
# Navigate a 2D map avoiding obstacles for nonviolent robots

import numpy as np

def glyph_601(grid, start, goal):
    from queue import PriorityQueue
    rows, cols = grid.shape
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start, []))

    while not pq.empty():
        cost, node, path = pq.get()
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            r, c = node[0]+dr, node[1]+dc
            if 0 <= r < rows and 0 <= c < cols and grid[r,c] == 0:
                pq.put((cost+1, (r,c), path))
    return None
