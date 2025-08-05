def glyph_165(matrix):
    """
    Inverts 1s to 0s and 0s to 1s in a binary matrix.

    Example:
    Input: [[1,0],[0,1]]
    Output: [[0,1],[1,0]]
    """
    return [[1 - cell for cell in row] for row in matrix]
