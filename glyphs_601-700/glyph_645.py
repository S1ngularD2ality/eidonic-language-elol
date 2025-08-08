# glyph_645 – SOFT_CONTACT_SENSOR
# Detect gentle touch to initiate safe interaction

def glyph_645(pressure_value, threshold=0.2):
    return pressure_value <= threshold
