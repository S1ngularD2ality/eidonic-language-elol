# glyph_355 – SAFE_HALT
# Immediate safe stop when hazard is detected

def glyph_355(hazard_detected):
    """
    hazard_detected: bool
    Returns: 'halt' or 'continue'
    """
    return "halt" if hazard_detected else "continue"
