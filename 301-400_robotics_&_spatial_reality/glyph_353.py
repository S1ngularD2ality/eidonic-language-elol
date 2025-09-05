# glyph_353 – WEIGHT_SENSE
# Detect and estimate the weight of carried or manipulated objects

def glyph_353(force_readings, calibration=1.0):
    """
    force_readings: list of numeric sensor readings
    Returns: estimated_weight
    """
    return sum(force_readings) * calibration
