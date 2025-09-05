# glyph_626 – ENVIRONMENTAL_HAZARD_ALERT
# Warn about slippery, uneven, or dangerous terrain

def glyph_626(terrain_map, threshold=0.5):
    return [loc for loc, safety in terrain_map.items() if safety < threshold]
