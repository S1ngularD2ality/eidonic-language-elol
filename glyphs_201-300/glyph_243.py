def glyph_243(matrix):
    """
    Glyph 243 — Dimensional Grid Duplicator
    Duplicates each row in a grid, doubling its vertical depth.

    Example Input:
    [[1, 2],
     [3, 4]]

    Output:
    [[1, 2],
     [1, 2],
     [3, 4],
     [3, 4]]
    """
    return [row for row in matrix for _ in (0, 1)]
