# glyph_624 – CHILD_SAFETY_MODE
# Lower all operational speeds and increase awareness around children

def glyph_624(is_child_nearby):
    return {'speed_limit': 0.4, 'scan_frequency': 2} if is_child_nearby else {'speed_limit': 1.0, 'scan_frequency': 1}
