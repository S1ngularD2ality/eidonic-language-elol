# glyph_638 – OBJECT_SOFT_PLACE
# Place objects down gently to avoid impact damage

def glyph_638(object_weight, fragility):
    return 'gentle_place' if fragility > 0.5 else 'normal_place'
