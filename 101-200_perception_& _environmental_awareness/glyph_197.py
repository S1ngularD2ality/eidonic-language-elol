def glyph_197(grid):
    """
    Flips 1s to 0s and 0s to 1s in a binary grid.

    Example:
    Input: [[1,0],[0,1]]
    Output: [[0,1],[1,0]]
    """
    return [[1 - val for val in row] for row in grid]
