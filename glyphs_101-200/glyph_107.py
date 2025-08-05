def glyph_107(matrix):
    """
    Applies rotational symmetry to the matrix (90° clockwise).
    """
    return [list(reversed(col)) for col in zip(*matrix)]
