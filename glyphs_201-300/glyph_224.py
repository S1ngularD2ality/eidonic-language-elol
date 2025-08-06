def glyph_224(n):
    """
    Glyph 224 — Mirror Gradient Flow
    Builds a symmetrical gradient list around a central peak.

    Example Input:
    4

    Output:
    [1, 2, 3, 4, 3, 2, 1]
    """
    return list(range(1, n+1)) + list(range(n-1, 0, -1))
