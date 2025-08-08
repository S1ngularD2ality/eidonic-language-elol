# glyph_836 – HOLOGRAPHIC_PROJECTION_MATRIX
# Build a simple 3×3 2D projection matrix with rotation+shear.

import math

def glyph_836(theta: float, shear: float = 0.0, scale: float = 1.0):
    """
    theta: radians, shear: x-shear factor, scale: uniform scale
    Returns 3x3 matrix as list of lists.
    """
    c, s = math.cos(theta)*scale, math.sin(theta)*scale
    return [
        [c, -s + shear, 0.0],
        [s,  c,         0.0],
        [0.0, 0.0,      1.0]
    ]
