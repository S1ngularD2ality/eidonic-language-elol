# glyph_340 – WATER_FIND
# Detect the presence and flow of water in the environment

def glyph_340(hydro_sensors):
    """
    hydro_sensors: dict of location:water_level
    Returns: locations with detected water
    """
    return [loc for loc, val in hydro_sensors.items() if val > 0]
