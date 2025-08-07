# glyph_372 – FALL_DETECT
# Detect and respond to falls or dangerous tilting

def glyph_372(accel_data):
    """
    accel_data: dict with 'x', 'y', 'z'
    Returns: True if fall detected
    """
    return abs(accel_data['z']) < 0.3
