# glyph_349 – SOLAR_TRACK
# Track and optimize orientation toward the sun for power or navigation

def glyph_349(solar_data):
    """
    solar_data: dict with 'azimuth', 'elevation'
    Returns: optimal orientation
    """
    if solar_data['elevation'] > 45:
        return "face up"
    return f"align to azimuth {solar_data['azimuth']}"
