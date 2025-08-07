# glyph_365 – LASER_LINE
# Use laser or projected lines for alignment and spatial calibration

def glyph_365(laser_data):
    """
    laser_data: list of (x, y)
    Returns: best-fit line parameters
    """
    import numpy as np
    x = np.array([pt[0] for pt in laser_data])
    y = np.array([pt[1] for pt in laser_data])
    m, b = np.polyfit(x, y, 1)
    return {'slope': m, 'intercept': b}
