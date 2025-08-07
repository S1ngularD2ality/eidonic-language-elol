# glyph_326 – COLOR_MIND
# Recognize and record dominant color patterns in the environment

def glyph_326(image_data):
    """
    image_data: array-like, shape (H,W,3)
    Returns: dominant color as RGB tuple
    """
    import numpy as np
    avg = np.mean(image_data, axis=(0, 1))
    return tuple(int(x) for x in avg)
