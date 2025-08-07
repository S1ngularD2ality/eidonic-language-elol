# glyph_329 – BARRIER_SENSE
# Detect invisible or subtle barriers (glass, force fields, boundaries)

def glyph_329(sensor_input):
    """
    sensor_input: dict with keys like 'ultrasound', 'IR', 'visual'
    Returns: True if barrier detected, else False
    """
    threshold = 0.8
    if sensor_input.get('ultrasound', 0) < threshold and sensor_input.get('visual', 1) == 0:
        return True
    return False
