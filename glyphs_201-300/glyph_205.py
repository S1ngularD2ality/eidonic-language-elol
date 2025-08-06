def glyph_205(matrix, threshold):
    """
    Glyph 205 — Threshold Pulse Map
    Highlights all cells in a matrix that pulse above a given threshold.

    Example Input:
    ([[4, 7],
      [2, 9]], 5)

    Output:
    [[False, True],
     [False, True]]
    """
    return [[val > threshold for val in row] for row in matrix]
