# glyph_348 – UV_SENSE
# Detect ultraviolet light or patterns invisible to the human eye

def glyph_348(uv_sensor_data):
    """
    uv_sensor_data: dict of location:uv_intensity
    Returns: locations with UV above threshold
    """
    return [loc for loc, uv in uv_sensor_data.items() if uv > 1.0]
