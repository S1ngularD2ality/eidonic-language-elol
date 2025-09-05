def glyph_192(grid):
    """
    Transposes the grid and returns the diagonal sum.

    Example:
    Input: [[1,2],[3,4]]
    Output: 5
    """
    transposed = list(zip(*grid))
    return sum(transposed[i][i] for i in range(len(transposed)))
