def glyph_150(matrix):
    """
    Inverts 1s and 0s in a binary matrix.

    Example:
    Input: [[1,0],[0,1]]
    Output: [[0,1],[1,0]]
    """
    return [[1 - val for val in row] for row in matrix]
