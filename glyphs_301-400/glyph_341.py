# glyph_341 – DUST_SENSE
# Detect airborne particles, dust, or pollutants for health and maintenance

def glyph_341(dust_data):
    """
    dust_data: dict of sensor_id:particle_count
    Returns: True if levels exceed safety
    """
    threshold = 100
    return any(count > threshold for count in dust_data.values())
