# glyph_374 – SURVIVOR_SEEK
# Seek, locate, and highlight humans or animals in need (rescue ops)

def glyph_374(image_data, heat_data):
    """
    image_data: visual array, heat_data: thermal array
    Returns: list of candidate (x, y) coordinates
    """
    candidates = []
    for idx, val in enumerate(heat_data):
        if val > 32:  # Example threshold
            candidates.append((idx, val))
    return candidates
