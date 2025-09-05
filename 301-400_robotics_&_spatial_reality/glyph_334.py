# glyph_334 – ECHO_MAP
# Build spatial map from sonar or echo-location pulses

def glyph_334(echo_data):
    """
    echo_data: list of (distance, angle)
    Returns: spatial_map (polar coordinates)
    """
    return [{'distance': d, 'angle': a} for d, a in echo_data]
