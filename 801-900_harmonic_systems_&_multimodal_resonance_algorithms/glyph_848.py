# glyph_848 – CIRCULAR_STATS
# Circular mean and variance for angles (radians).

import math

def glyph_848(angles):
    """
    angles: iterable of radians
    returns dict(mean, R, variance)
    """
    if not angles:
        return {"mean": 0.0, "R": 0.0, "variance": 0.0}
    sx = sum(math.cos(a) for a in angles)
    sy = sum(math.sin(a) for a in angles)
    n = len(angles)
    R = math.hypot(sx, sy) / n
    mean = math.atan2(sy, sx)
    var = 1 - R
    return {"mean": mean, "R": R, "variance": var}
