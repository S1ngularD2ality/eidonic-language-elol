# glyph_839 – CIRCLE_PACKING_ESTIMATOR
# Estimate number of radius-r circles in a rectangle via hex packing.

import math

def glyph_839(width, height, r):
    """
    Uses hexagonal packing density ~0.9069 to estimate capacity.
    """
    if r <= 0 or width <= 0 or height <= 0:
        return 0
    area = width * height
    circle = math.pi * (r ** 2)
    return int((area * 0.9069) // circle)
