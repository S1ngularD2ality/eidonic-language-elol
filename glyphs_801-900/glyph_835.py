# glyph_835 – ARC_LENGTH_RESAMPLER
# Resample a polyline to N approximately equal arc-length points.

import math

def glyph_835(points, N: int):
    """
    points: list[(x,y)] with len>=2
    N: number of output points >=2
    """
    if len(points) < 2 or N < 2:
        raise ValueError("Need at least 2 input points and N>=2")
    # cumulative distances
    d=[0.0]
    for i in range(1,len(points)):
        x1,y1 = points[i-1]; x2,y2 = points[i]
        d.append(d[-1] + math.hypot(x2-x1, y2-y1))
    total = d[-1]
    if total == 0:
        return [points[0]]*N
    targets = [i*total/(N-1) for i in range(N)]
    # interpolate
    out=[]
    j=0
    for t in targets:
        while j+1 < len(d) and d[j+1] < t:
            j+=1
        if j+1 == len(d):
            out.append(points[-1]); continue
        t0, t1 = d[j], d[j+1]
        x0,y0 = points[j]; x1,y1 = points[j+1]
        u = 0.0 if t1==t0 else (t - t0)/(t1 - t0)
        out.append((x0 + u*(x1-x0), y0 + u*(y1-y0)))
    return out
