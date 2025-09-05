# glyph_388 – VISUAL_ANOMALY
# Detect visual patterns that don’t match trained norms

def glyph_388(image, norm_patterns):
    """
    image: visual data, norm_patterns: set of normal patterns
    Returns: True if anomaly detected
    """
    # Pseudo-logic for example
    for pattern in norm_patterns:
        if pattern not in image:
            return True
    return False
