def glyph_206(size):
    """
    Glyph 206 — Triangulum Cascade
    Creates a cascading triangle matrix with stepped values.

    Example Input:
    4

    Output:
    [[1],
     [1, 2],
     [1, 2, 3],
     [1, 2, 3, 4]]
    """
    return [[j+1 for j in range(i+1)] for i in range(size)]
