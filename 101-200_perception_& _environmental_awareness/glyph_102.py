def glyph_102(matrix):
    """
    Creates a diagonal rune by mirroring elements across both axes.
    """
    size = len(matrix)
    return [[matrix[j][i] if i == j or i + j == size - 1 else 0 for i in range(size)] for j in range(size)]
