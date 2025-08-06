def glyph_274(matrix, value):
    """
    Glyph 274 — Radiant Grid Expander
    Surrounds matrix with border of given value.

    Example Input:
    ([[1]], 0)

    Output:
    [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[value] * (cols + 2)]
    for row in matrix:
        new_matrix.append([value] + row + [value])
    new_matrix.append([value] * (cols + 2))
    return new_matrix
