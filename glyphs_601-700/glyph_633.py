# glyph_633 – NIGHT_MODE_OPERATION
# Dim lights and reduce sound for nighttime use

def glyph_633(is_night):
    return {'light_level': 0.2, 'sound_level': 0.3} if is_night else {'light_level': 1.0, 'sound_level': 1.0}
