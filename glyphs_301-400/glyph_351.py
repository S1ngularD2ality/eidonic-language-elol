# glyph_351 – GYRO_STABILIZE
# Maintain upright posture using gyroscope and inertial data

def glyph_351(gyro, accel):
    """
    gyro: dict with angular velocities
    accel: dict with acceleration values
    Returns: adjustment signal ('stable', 'adjust left', etc.)
    """
    if abs(gyro['z']) > 0.2:
        return "adjust yaw"
    if abs(accel['x']) > 0.3:
        return "adjust roll"
    return "stable"
