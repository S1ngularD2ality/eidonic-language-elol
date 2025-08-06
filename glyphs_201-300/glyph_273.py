def glyph_273(a, b):
    """
    Glyph 273 — Mirror Phase Comparator
    Compares two lists for mirrored equality.

    Example Input:
    [1, 2, 3], [3, 2, 1]

    Output:
    True
    """
    return a == b[::-1]
