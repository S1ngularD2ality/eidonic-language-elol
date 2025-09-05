def glyph_232(n):
    """
    Glyph 232 — Nested Diagonal Flame
    Creates a nested matrix with diagonals filled incrementally.

    Example Input:
    3

    Output:
    [[1, 0, 0],
     [0, 2, 0],
     [0, 0, 3]]
    """
    return [[i+1 if i == j else 0 for j in range(n)] for i in range(n)]
