def glyph_149(matrix):
    """
    Flattens a 2D matrix to a 1D list while preserving order.

    Example:
    Input: [[1,2],[3,4]]
    Output: [1,2,3,4]
    """
    return [item for row in matrix for item in row]
