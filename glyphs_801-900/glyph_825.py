# glyph_825 – POLAR_VORTEX_SEGMENTER
# Segment points into angular bins around a center; returns {bin: [points]}.

import math

def glyph_825(points, center=(0.0, 0.0), bins=12):
    """
    points: list[(x,y)]
    center: (cx, cy)
    bins: number of angular sectors
    """
    if bins < 1:
        raise ValueError("bins >= 1")
    cx, cy = center
    sectors = {i: [] for i in range(bins)}
    for x, y in points:
        ang = (math.atan2(y - cy, x - cx) + 2*math.pi) % (2*math.pi)
        b = int((ang / (2*math.pi)) * bins)
        sectors[b].append((x, y))
    return sectors
