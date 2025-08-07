# glyph_319 – LIGHT_FIELD
# Adapt to and map changing light conditions in an environment

def glyph_319(light_sensors):
    """
    light_sensors: dict of sensor_id:lux_value
    Returns: environment light map
    """
    avg_light = sum(light_sensors.values()) / len(light_sensors)
    return {'average_lux': avg_light, 'detailed': light_sensors}
