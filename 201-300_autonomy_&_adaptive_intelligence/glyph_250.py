def glyph_250(n):
    """
    Glyph 250 — Singular Matrix Beacon
    Places a 1 at the center of a matrix; else 0s.

    Example Input:
    3

    Output:
    [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
    """
    return [[1 if i == j == n//2 else 0 for j in range(n)] for i in range(n)]
