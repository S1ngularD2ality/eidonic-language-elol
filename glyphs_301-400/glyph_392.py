# glyph_392 – NIGHT_SENSE
# Detect and adapt to extreme low-light or total darkness (beyond night vision)

def glyph_392(light_value, threshold=5):
    """
    light_value: measured ambient light
    threshold: darkness threshold
    Returns: 'engage IR', 'engage sonar', or 'normal'
    """
    if light_value < threshold:
        return "engage IR"
    return "normal"
