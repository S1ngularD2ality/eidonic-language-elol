# glyph_621 – SAFE_LIFT_MECHANISM
# Calculate lift speed to avoid injury or strain

def glyph_621(object_weight, fragility_factor=0.6):
    return max(0.05, min(0.3, fragility_factor / object_weight))
