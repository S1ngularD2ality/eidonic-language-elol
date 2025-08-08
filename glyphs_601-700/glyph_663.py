# glyph_663 – TEMPERATURE_SAFE_CARRY
# Ensure items carried stay within safe temperature range

def glyph_663(item_temp, safe_range=(0, 40)):
    return safe_range[0] <= item_temp <= safe_range[1]
