# glyph_344 – SURFACE_FEEL
# Detect and classify surface types (rough, smooth, slippery, sticky)

def glyph_344(tactile_data):
    """
    tactile_data: dict with 'roughness', 'friction', etc.
    Returns: surface classification
    """
    if tactile_data['friction'] > 0.7:
        return "sticky"
    if tactile_data['roughness'] > 0.8:
        return "rough"
    if tactile_data['friction'] < 0.2:
        return "slippery"
    return "smooth"
