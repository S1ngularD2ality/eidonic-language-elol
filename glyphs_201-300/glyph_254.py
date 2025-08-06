def glyph_254(a, b):
    """
    Glyph 254 — Fractal Merge Stitcher
    Interleaves two arrays in a woven pattern.

    Example Input:
    [1, 3, 5], [2, 4, 6]

    Output:
    [1, 2, 3, 4, 5, 6]
    """
    return [val for pair in zip(a, b) for val in pair]
