def glyph_170(matrix):
    """
    Counts how many unique values exist in each row of a matrix.

    Example:
    Input: [[1,1,2],[3,4,4]]
    Output: [2,2]
    """
    return [len(set(row)) for row in matrix]
