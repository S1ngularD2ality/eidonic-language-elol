# glyph_339 – MAGNETIC_SENSE
# Detect and respond to magnetic fields for orientation or navigation

def glyph_339(mag_data):
    """
    mag_data: dict with 'x', 'y', 'z' components
    Returns: magnitude and direction
    """
    import math
    mag = (mag_data['x']**2 + mag_data['y']**2 + mag_data['z']**2)**0.5
    return {'magnitude': mag, 'vector': (mag_data['x'], mag_data['y'], mag_data['z'])}
