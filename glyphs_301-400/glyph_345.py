# glyph_345 – NIGHT_VISION
# Enhance or adapt visual perception in low-light environments

def glyph_345(image, gain=2):
    """
    image: 2D array
    gain: amplification factor
    Returns: amplified image
    """
    import numpy as np
    return np.clip(image * gain, 0, 255)
