def glyph_101(matrix):
    """
    Expands each cell by its row index, magnifying positional context.
    """
    return [[cell * i for cell in row] for i, row in enumerate(matrix)]
