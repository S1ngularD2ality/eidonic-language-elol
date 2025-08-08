# glyph_630 – WATER_SAFETY_SHUTDOWN
# Shut down sensitive electronics when entering water zones

def glyph_630(is_in_water_zone):
    return 'SHUTDOWN' if is_in_water_zone else 'ACTIVE'
