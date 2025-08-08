# glyph_648 – ENVIRONMENT_LIGHT_ADAPT
# Adjust visual sensors to current lighting

def glyph_648(light_level):
    if light_level < 0.3:
        return 'increase_exposure'
    elif light_level > 0.7:
        return 'reduce_exposure'
    else:
        return 'normal'
