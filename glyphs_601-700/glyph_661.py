# glyph_661 – SAFE_RETRACT_MECHANISM
# Retract moving parts slowly to avoid harm

def glyph_661(retract_speed=0.3):
    return max(0.1, min(0.5, retract_speed))
