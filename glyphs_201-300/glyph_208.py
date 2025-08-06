def glyph_208(n):
    """
    Glyph 208 — Celestial Ring Pattern
    Constructs a concentric ring pattern from 1 to n.

    Example Input:
    3

    Output:
    [[1, 1, 1],
     [1, 2, 1],
     [1, 1, 1]]
    """
    mat = [[1]*n for _ in range(n)]
    if n > 2:
        for i in range(1, n-1):
            for j in range(1, n-1):
                mat[i][j] = 2
    return mat
