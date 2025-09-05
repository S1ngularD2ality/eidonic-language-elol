# glyph_642 – TEMP_SENSITIVE_MODE
# Adjust operations based on surrounding temperature

def glyph_642(temp_celsius):
    if temp_celsius < 0:
        return 'cold_protect'
    elif temp_celsius > 35:
        return 'heat_protect'
    else:
        return 'normal'
