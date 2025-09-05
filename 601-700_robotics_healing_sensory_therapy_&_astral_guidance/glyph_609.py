# glyph_609 – SOFT_TOUCH_GRIP
# Calculate grip force to avoid damaging objects

def glyph_609(object_weight, fragility_factor=0.5):
    return max(0.1, object_weight * fragility_factor)
