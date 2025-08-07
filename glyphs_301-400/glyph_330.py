# glyph_330 – LOCAL_GRAVITY
# Sense and adapt to gravity changes (terrain slope, elevator, falling)

def glyph_330(accel_data):
    """
    accel_data: dict with 'x', 'y', 'z' acceleration
    Returns: gravity_vector and 'event' description
    """
    gravity = (accel_data['x'], accel_data['y'], accel_data['z'])
    if abs(gravity[2]) < 0.5:
        return {'gravity_vector': gravity, 'event': 'freefall or low gravity'}
    return {'gravity_vector': gravity, 'event': 'normal'}
