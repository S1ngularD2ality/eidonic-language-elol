def glyph_241(n):
    """
    Glyph 241 — Mirror Cascade Constructor
    Creates a symmetric pyramid pattern reflected vertically.

    Example Input:
    3

    Output:
    [[1],
     [1, 2],
     [1, 2, 3],
     [1, 2],
     [1]]
    """
    pattern = [[j + 1 for j in range(i + 1)] for i in range(n)]
    return pattern + pattern[::-1][1:]
