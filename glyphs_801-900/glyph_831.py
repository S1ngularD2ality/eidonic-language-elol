# glyph_831 – PHI_SPIRAL_SORT
# Sort 2D points by polar angle offset by the golden angle (spiral-friendly).

import math

def glyph_831(points):
    """
    points: list[(x,y)]
    Returns new list sorted for golden-spiral traversal.
    """
    if not points:
        return []
    golden = 2*math.pi*(1 - 1/((1 + 5**0.5)/2))
    def key(p):
        x, y = p
        ang = (math.atan2(y, x) - golden) % (2*math.pi)
        r = (x*x + y*y)
        return (ang, r)
    return sorted(points, key=key)
