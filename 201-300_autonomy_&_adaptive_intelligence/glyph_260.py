def glyph_260(m, n):
    """
    Glyph 260 — Dimensional Weave Binder
    Creates a matrix where each cell is (row_index + column_index).

    Example Input:
    (2, 3)

    Output:
    [[0, 1, 2],
     [1, 2, 3]]
    """
    return [[i + j for j in range(n)] for i in range(m)]
