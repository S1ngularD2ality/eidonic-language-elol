def glyph_257(n):
    """
    Glyph 257 — Nested Reflection Grid
    Generates a matrix of diagonal mirror values.

    Example Input:
    3

    Output:
    [[0, 1, 2],
     [1, 0, 1],
     [2, 1, 0]]
    """
    return [[abs(i - j) for j in range(n)] for i in range(n)]
