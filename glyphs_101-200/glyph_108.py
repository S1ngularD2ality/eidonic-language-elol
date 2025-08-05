def glyph_108(matrix):
    """
    Inverts all values relative to the matrix's maximum value.
    """
    max_val = max(max(row) for row in matrix)
    return [[max_val - cell for cell in row] for row in matrix]
