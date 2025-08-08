# glyph_650 – HEALING_LIGHT_CONTROL
# Adjust built-in LED lighting for therapeutic use

def glyph_650(mode):
    return {'color': 'warm_white', 'intensity': 0.5} if mode == 'calm' else {'color': 'neutral', 'intensity': 1.0}
