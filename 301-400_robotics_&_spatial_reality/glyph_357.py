# glyph_357 – VIBRATION_SENSE
# Detect and classify environmental vibrations (earthquakes, machines, footsteps)

def glyph_357(vib_data, threshold=0.05):
    """
    vib_data: dict of sensor_id:vibration_value
    Returns: True if significant vibration detected
    """
    return any(abs(v) > threshold for v in vib_data.values())
