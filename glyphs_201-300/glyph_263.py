def glyph_263(matrix):
    """
    Glyph 263 — Spiral Core Extractor
    Returns the center element(s) of a matrix.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    Output:
    5
    """
    mid = len(matrix) // 2
    return matrix[mid][mid]
