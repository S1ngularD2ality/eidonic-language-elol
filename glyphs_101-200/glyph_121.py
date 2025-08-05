def glyph_121(matrix):
    """
    💠 Transposes a 2D mirror matrix.
    Used for orientation reversal in mirrored dimensions.
    """
    return [list(row) for row in zip(*matrix)]
