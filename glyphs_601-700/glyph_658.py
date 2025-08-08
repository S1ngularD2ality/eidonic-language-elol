# glyph_658 – HUMIDITY_ADAPT
# Adjust operations for humidity-sensitive components

def glyph_658(humidity):
    return 'reduce_speed' if humidity > 70 else 'normal'
