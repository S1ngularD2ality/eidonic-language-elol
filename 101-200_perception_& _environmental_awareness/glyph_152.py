def glyph_152(matrix):
    """
    Duplicates the last column across the entire row structure.

    Example:
    Input: [[1,2],[3,4]]
    Output: [[2,2],[4,4]]
    """
    return [[row[-1]] * len(row) for row in matrix]
