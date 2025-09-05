def glyph_275(matrix):
    """
    Glyph 275 — Cascade Edge Binder
    Returns sum of the outermost elements.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    Output:
    40
    """
    total = sum(matrix[0]) + sum(matrix[-1])
    for row in matrix[1:-1]:
        total += row[0] + row[-1]
    return total
