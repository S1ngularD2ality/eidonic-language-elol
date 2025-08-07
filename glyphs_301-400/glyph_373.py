# glyph_373 – WIND_DIRECTION
# Determine wind direction and magnitude for drones/robots

def glyph_373(anemometer_data):
    """
    anemometer_data: dict with 'speed', 'direction'
    Returns: direction (degrees), speed (m/s)
    """
    return (anemometer_data.get('direction', 0), anemometer_data.get('speed', 0))
