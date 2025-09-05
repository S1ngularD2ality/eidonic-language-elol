# glyph_325 – SMELL_TRACE
# Detect chemical or olfactory signatures and track their movement

def glyph_325(smell_sensors):
    """
    smell_sensors: dict of sensor_id:concentration
    Returns: detected_signatures and peak location
    """
    peak = max(smell_sensors, key=smell_sensors.get)
    return {'peak_sensor': peak, 'peak_value': smell_sensors[peak], 'all_data': smell_sensors}
