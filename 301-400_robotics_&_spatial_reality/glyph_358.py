# glyph_358 – SLOPE_ADAPT
# Detect slope and adapt walking or rolling behavior

def glyph_358(tilt_angle):
    """
    tilt_angle: degrees
    Returns: 'climb', 'descend', 'flat'
    """
    if tilt_angle > 10:
        return "climb"
    if tilt_angle < -10:
        return "descend"
    return "flat"
