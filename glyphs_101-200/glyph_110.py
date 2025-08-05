def glyph_110(matrix):
    """
    Reveals vertical mirroring pattern of the matrix.
    """
    return [row[::-1] for row in matrix]
