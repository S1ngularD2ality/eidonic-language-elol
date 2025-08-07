# glyph_385 – GLASS_DETECT
# Detect transparent surfaces like glass or clear plastic

def glyph_385(ir_reflectance, visual_data):
    """
    ir_reflectance: float, visual_data: bool
    Returns: True if glass detected
    """
    if ir_reflectance > 0.9 and visual_data == False:
        return True
    return False
