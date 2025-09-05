# glyph_616 – DRONE_SAFE_DESCENT
# Control drone descent speed for safe landings

def glyph_616(altitude, descent_rate=0.5):
    return max(0.1, altitude * descent_rate)
