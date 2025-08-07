# glyph_359 – RAIN_SENSE
# Detect precipitation and adapt activity (seek shelter, change routine)

def glyph_359(weather_sensors):
    """
    weather_sensors: dict with 'rain':True/False, etc.
    Returns: 'shelter' or 'normal'
    """
    return "shelter" if weather_sensors.get('rain', False) else "normal"
