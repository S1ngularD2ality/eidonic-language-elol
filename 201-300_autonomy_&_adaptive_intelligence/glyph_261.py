def glyph_261(matrix):
    """
    Glyph 261 — Vortex Column Rotator
    Rotates the columns of a 2D matrix to the right.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6]]

    Output:
    [[3, 1, 2],
     [6, 4, 5]]
    """
    return [row[-1:] + row[:-1] for row in matrix]
