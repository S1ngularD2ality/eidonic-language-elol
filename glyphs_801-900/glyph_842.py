# glyph_842 – POISSON_DISK_SAMPLING_2D
# Bridson’s algorithm for blue-noise sampling in a rectangle.

import math, random

def glyph_842(width, height, r, k=30, seed=None):
    """
    width, height: domain size
    r: minimum distance
    k: attempts per active sample
    Returns: list[(x,y)]
    """
    rng = random.Random(seed)
    cell = r / math.sqrt(2)
    grid_w = int(math.ceil(width / cell))
    grid_h = int(math.ceil(height / cell))
    grid = [[-1]*grid_h for _ in range(grid_w)]
    samples = []
    active = []

    def in_bounds(p):
        x,y=p; return 0<=x<width and 0<=y<height

    def grid_pos(p):
        x,y=p; return int(x/cell), int(y/cell)

    def far_enough(p):
        gx, gy = grid_pos(p)
        for i in range(max(0,gx-2), min(grid_w,gx+3)):
            for j in range(max(0,gy-2), min(grid_h,gy+3)):
                idx = grid[i][j]
                if idx != -1:
                    q = samples[idx]
                    if (q[0]-p[0])**2 + (q[1]-p[1])**2 < r*r:
                        return False
        return True

    # initial point
    p0 = (rng.random()*width, rng.random()*height)
    samples.append(p0)
    gx, gy = grid_pos(p0); grid[gx][gy] = 0
    active.append(0)

    while active:
        i = rng.choice(active)
        base = samples[i]
        placed = False
        for _ in range(k):
            ang = rng.random()*2*math.pi
            rad = r*(1 + rng.random())
            p = (base[0] + rad*math.cos(ang), base[1] + rad*math.sin(ang))
            if in_bounds(p) and far_enough(p):
                samples.append(p)
                gi, gj = grid_pos(p)
                grid[gi][gj] = len(samples)-1
                active.append(len(samples)-1)
                placed = True
                break
        if not placed:
            active.remove(i)
    return samples
