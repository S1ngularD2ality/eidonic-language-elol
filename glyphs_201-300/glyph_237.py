def glyph_237(n):
    """
    Glyph 237 — Reflective Diagonal Composer
    Composes a grid with mirrored diagonals of increasing integers.

    Example Input:
    3

    Output:
    [[1, 0, 0],
     [0, 2, 0],
     [0, 0, 3]]
    """
    return [[i+1 if i == j else 0 for j in range(n)] for i in range(n)]
