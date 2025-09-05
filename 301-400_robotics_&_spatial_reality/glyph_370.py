# glyph_370 – DIRECTIONAL_LIGHT
# Adapt movement or perception based on the direction/intensity of light

def glyph_370(light_data):
    """
    light_data: dict of sensor_id:lux
    Returns: direction to move for optimal light or 'balanced'
    """
    max_sensor = max(light_data, key=light_data.get)
    if light_data[max_sensor] > 100:
        return f"move toward {max_sensor}"
    return "balanced"
